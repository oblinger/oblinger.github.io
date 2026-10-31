"""strip-vault regression tests (deep scan r2, 2026-10-30): content it silently lost or mislinked.

Run: PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python3 -m pytest tools/tests -q   (from the repo root)
"""

import importlib.machinery
import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]


def load_strip_vault():
    sys.dont_write_bytecode = True
    loader = importlib.machinery.SourceFileLoader("strip_vault_r2", str(REPO / "tools" / "strip-vault"))
    spec = importlib.util.spec_from_loader("strip_vault_r2", loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def sv():
    return load_strip_vault()


# Broke when a one-line paragraph between two horizontal rules opened with a word and a
# colon ("Note: ..."), because the stray-front-matter pass took any `Word:` line for YAML
# and deleted the whole block.

def test_prose_paragraph_between_rules_is_kept(sv):
    out = sv.clean("Intro.\n\n---\nNote: this paragraph is the whole point.\n---\n\nAfter.\n", {})
    assert "Note: this paragraph is the whole point." in out


def test_stray_front_matter_block_is_still_dropped(sv):
    out = sv.clean("Text\n\n---\nlayout: cayman\ntitle: Claim: it ends with a period.\n---\nMore\n", {})
    assert "layout: cayman" not in out and "Text" in out and "More" in out


# Broke when a sentence began with a hook:// or ha:// link, because the stub-line pass
# dropped every line that *started* with a vault link, sentence and all.

def test_sentence_opening_with_a_vault_link_keeps_its_text(sv):
    out = sv.clean("One.\n\n[The catalog](ha://p/CAT) explains why the market cannot stop.\n\nThree.\n", {})
    assert "The catalog explains why the market cannot stop." in out
    assert sv.residue(out) == []


def test_line_of_only_vault_links_is_dropped(sv):
    out = sv.clean("[ASIO markdown](hook://ASIO%20markdown) - \n- [A](ha://p/A), [B](ha://p/B)\nBody\n", {})
    assert out == "Body\n"


# Broke on a same-page heading link `[[#Section]]`, which came out as the literal text
# "#Section" because an empty page name resolves to no URL.

def test_same_page_heading_link_becomes_an_anchor(sv):
    out = sv.clean("See [[#Why it matters]] and [[#Why it matters|why]].\n", {})
    assert out == "See [Why it matters](#why-it-matters) and [why](#why-it-matters).\n"


# Broke when a wikilink's case differed from the file name ([[asio log]] for `ASIO Log.md`),
# which Obsidian resolves and strip-vault turned into plain text.

def test_wikilink_resolves_case_insensitively(sv, tmp_path):
    (tmp_path / "A.md").write_text("[[asio log]] and [[ASIO Log]]\n")
    (tmp_path / "ASIO Log.md").write_text("log\n")
    sv.clean_tree(tmp_path, "/ASIO/")
    out = (tmp_path / "A.md").read_text()
    assert out == "[asio log](/ASIO/ASIO%20Log.html) and [ASIO Log](/ASIO/ASIO%20Log.html)\n"


# Broke on a heading with punctuation: kramdown (GitHub Pages) ids a heading "Profit, Power?"
# as `profit-power`, while the link carried `profit%2C-power%3F`, a dead anchor.

@pytest.mark.parametrize("heading, anchor", [
    ("Why it matters", "why-it-matters"),
    ("Profit, Power? Control!", "profit-power-control"),
    ("2. The second claim", "the-second-claim"),
    ("Don't stop", "dont-stop"),
    ("???", "section"),
])
def test_heading_anchor_matches_kramdown_id(sv, heading, anchor):
    out = sv.clean(f"[[Other#{heading}|x]]\n", {"Other": "/ASIO/Other.html"})
    assert out == f"[x](/ASIO/Other.html#{anchor})\n"


# Broke in efe9d17's own stub rule: a line that is "nothing but vault links and punctuation" took a
# heading or a blockquote whose text is one link for a stub, and dropped it whole; the rule it
# replaced kept `## [Essay notes](hook://x)` as `## Essay notes` (regression review 2026-10-30).
@pytest.mark.parametrize("line, kept", [
    ("## [Essay notes](hook://x)", "## Essay notes"),
    ("> [Quoted](ha://y)", "> Quoted"),
])
def test_heading_or_quote_that_is_a_vault_link_keeps_its_text(sv, line, kept):
    assert sv.clean(f"{line}\nbody\n", {}) == f"{kept}\nbody\n"


def test_bulleted_vault_stub_is_still_dropped(sv):
    assert sv.clean("- [ASIO markdown](hook://x) - [Log](ha://y)\nbody\n", {}) == "body\n"
