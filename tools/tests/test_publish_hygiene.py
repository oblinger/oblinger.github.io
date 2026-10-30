"""Privacy and publish-hygiene tests (deep scan r1 fixes P1-P7, 2026-10-29).

Run: PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python3 -m pytest tools/tests -q   (from the repo root)
"""

import importlib.machinery
import importlib.util
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
VAULT_ASIO = Path.home() / "ob" / "kmr" / "ASIO"

# Strings that mark vault machinery; none may reach a published page.
VAULT_MARKERS = [":>>", "# BRIEF", "hook://", "ha://", "[[", "~/ob", "/Users/",
                 "auto-generated anchor file"]
PRIVATE = ["Bache", "oblinger@gmail.com", "494 9499", "94110"]
CLEANED_PAGES = ["gitproj/gitproj.md", "gitproj/DeliberativeCoherence/DeliberativeCoherence.md",
                 "gitproj/AlienBiology/AlienBiology.md"]


def load_strip_vault():
    sys.dont_write_bytecode = True
    loader = importlib.machinery.SourceFileLoader("strip_vault", str(REPO / "tools" / "strip-vault"))
    spec = importlib.util.spec_from_loader("strip_vault", loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


def front_matter(path):
    text = path.read_text()
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    return match.group(1) if match else ""


def markers_in(text):
    return [m for m in VAULT_MARKERS if m in text]


@pytest.fixture(scope="module")
def built_site(tmp_path_factory):
    out = tmp_path_factory.mktemp("site")
    result = subprocess.run(
        ["bundle", "exec", "jekyll", "build", "-q", "-s", str(REPO), "-d", str(out)],
        cwd=REPO, capture_output=True, text=True,
        env={**os.environ, "BUNDLE_GEMFILE": str(REPO / "Gemfile")})
    assert result.returncode == 0, result.stderr[-2000:]
    return out


# P1: the home page carries no private contact details; /hotline/ keeps them.

def test_home_page_source_has_no_private_contact():
    text = (REPO / "index.markdown").read_text()
    assert [p for p in PRIVATE if p in text] == []
    hotline = (REPO / "hotline.markdown").read_text()
    assert "Bache" in hotline and "oblinger@gmail.com" in hotline


def test_built_home_page_has_no_private_contact(built_site):
    html = (built_site / "index.html").read_text()
    assert [p for p in PRIVATE if p in html] == []


@pytest.mark.parametrize("page", ["hotline.markdown", "publications/MAPPING.md"])
def test_page_is_kept_out_of_the_sitemap(page):
    assert re.search(r"^sitemap:\s*false\b", front_matter(REPO / page), re.M)


def test_built_sitemap_omits_hotline_and_mapping(built_site):
    sitemap = (built_site / "sitemap.xml").read_text()
    assert "/hotline" not in sitemap and "MAPPING" not in sitemap


def test_mapping_page_names_no_local_path():
    assert markers_in((REPO / "publications" / "MAPPING.md").read_text()) == []


# P3: sync-asio strips vault machinery.

def test_strip_drops_breadcrumb_brief_stubs_and_hook_links():
    sv = load_strip_vault()
    text = (
        "---\ntitle: T\ndescription: \"site (symlink into `~/ob/grove/x`)\"\n---\n"
        ":>> [[kmr]] → [[ASIO]] → [A](hook://p/A) \n"
        "Body cites [[B]] and [[Missing Page]] and [[B|the B claim]] and [Doc](ha://p/Doc).\n"
        "[ASIO markdown](hook://ASIO%20markdown) - \n"
        "\n---\n\n# ASIO\n\nThis is an auto-generated anchor file for patch 'ASIO'.\n\nAdd your content here.\n"
        "\n# BRIEF\n\n- agent contract\n- more\n"
    )
    out = sv.clean(text, {"B": "B.html"})
    assert markers_in(out) == []
    assert "title: T" in out and "description" not in out
    assert "[B](B.html)" in out and "[the B claim](B.html)" in out
    assert "Missing Page" in out and "Body cites" in out and "Doc" in out
    assert "agent contract" not in out and "ASIO markdown" not in out


def test_strip_rewrites_a_masthead_table_and_keeps_its_rows():
    sv = load_strip_vault()
    text = ("| -[[ASIO]]- | : <br>→ [[kmr]] → [ASIO](ha://p/ASIO) |\n| --- | --- |\n"
            "| [[A]] | Claim: a. |\n| ~~[X](hook://X)~~ | gone |\n| ... |  |\n")
    out = sv.clean(text, {"A": "A.html"})
    assert markers_in(out) == []
    assert "| [A](A.html) | Claim: a. |" in out
    assert "gone" not in out and "| ... |" not in out
    assert out.splitlines()[1].startswith("| ---")


def test_strip_drops_a_masthead_only_table_and_its_zone():
    sv = load_strip_vault()
    text = "| -[[P]]- | +> |\n\n    [[A]], [[B.pdf]], [x](hook://x) \n\n**Body**\n"
    out = sv.clean(text, {"A": "A.html"})
    assert markers_in(out) == [] and out.lstrip().startswith("**Body**")


def test_strip_lifts_front_matter_above_a_breadcrumb():
    """Jekyll reads front matter only at byte 0; the vault puts the breadcrumb first."""
    out = load_strip_vault().clean(":>> [[kmr]] → [A](hook://p/A) \n\n---\ntitle: T\n---\nBody\n", {})
    assert out == "---\ntitle: T\n---\nBody\n"


def test_strip_drops_a_stray_mid_page_front_matter_block():
    sv = load_strip_vault()
    out = sv.clean("---\n---\nText\n\n---\nlayout: cayman\ntitle: .\ndescription: .\n---\nMore\n", {})
    assert "layout: cayman" not in out and "Text" in out and "More" in out


def test_strip_links_resolve_permalinks_and_spaces(tmp_path):
    sv = load_strip_vault()
    (tmp_path / "A.md").write_text("[[ASI_Outcomes]] [[ASIO Log|Log]] [[File.pdf]]\n")
    (tmp_path / "ASI_Outcomes.md").write_text("---\npermalink: /ASIO/ASI_Outcomes/\n---\nx\n")
    (tmp_path / "ASIO Log.md").write_text("log\n")
    (tmp_path / "File.pdf").write_bytes(b"%PDF")
    sv.clean_tree(tmp_path, "/ASIO/")
    out = (tmp_path / "A.md").read_text()
    assert "[ASI_Outcomes](/ASIO/ASI_Outcomes/)" in out
    assert "[Log](/ASIO/ASIO%20Log.html)" in out and "[File.pdf](/ASIO/File.pdf)" in out


def test_strip_refuses_a_local_path_it_cannot_remove(tmp_path):
    (tmp_path / "A.md").write_text("See /Users/someone/notes for details.\n")
    result = subprocess.run([sys.executable, str(REPO / "tools" / "strip-vault"), str(tmp_path), "/x/"],
                            capture_output=True, text=True)
    assert result.returncode != 0 and "/Users/" in result.stderr


@pytest.mark.skipif(not VAULT_ASIO.is_dir(), reason="vault ASIO not on this machine")
def test_sync_asio_on_a_scratch_copy_of_the_vault_publishes_no_vault_machinery(tmp_path):
    vault_copy = tmp_path / "vault-ASIO"
    shutil.copytree(VAULT_ASIO, vault_copy)
    site = tmp_path / "site"
    (site / "ASIO").mkdir(parents=True)
    (site / "ASIO" / "orphan.md").write_text("renamed away in the vault\n")
    result = subprocess.run(
        ["just", "--justfile", str(REPO / "justfile"), "--set", "website_repo", str(site), "sync-asio"],
        capture_output=True, text=True, env={**os.environ, "WEB_VAULT_ASIO": str(vault_copy)})
    assert result.returncode == 0, result.stderr
    pages = sorted((site / "ASIO").rglob("*.md"))
    assert len(pages) == len(list(vault_copy.rglob("*.md")))
    assert not (site / "ASIO" / "orphan.md").exists()
    assert not list((site / "ASIO").rglob(".anchor")) and not list((site / "ASIO").rglob(".DS_Store"))
    dirty = {p.name: markers_in(p.read_text()) for p in pages if markers_in(p.read_text())}
    assert dirty == {}


@pytest.mark.parametrize("page", sorted(str(p.relative_to(REPO)) for p in (REPO / "ASIO").rglob("*.md"))
                         + CLEANED_PAGES)
def test_committed_page_carries_no_vault_machinery(page):
    assert markers_in((REPO / page).read_text()) == []


def test_built_asio_page_has_no_raw_wikilinks(built_site):
    html = (built_site / "ASIO" / "ASIO.html").read_text()
    assert markers_in(html) == []
    assert 'href="/ASIO/Cant_Stop.html"' in html


# P4: publish recipes stage explicit paths.

def test_publish_recipes_never_stage_everything():
    justfile = (REPO / "justfile").read_text()
    assert "add -A" not in justfile and "add --all" not in justfile and "add ." not in justfile


# P5: local preview runs what GitHub Pages runs.

def test_gemfile_uses_the_github_pages_gem():
    gemfile = (REPO / "Gemfile").read_text()
    assert re.search(r'^gem "github-pages"', gemfile, re.M)
    assert not re.search(r'^gem "jekyll"', gemfile, re.M)


# P6: in-repo links point at pages that exist.

@pytest.mark.parametrize("source, href", [
    ("projects.markdown", "/gitproj/dans-anchor-system/"),
    ("gitproj/AlienBiology/index.md", "/abio-docs/ABIO%20Demos/ABIO%20Demo%20Gallery.html"),
    ("gitproj/DeliberativeCoherence/index.md", "/abio-docs/ABIO%20Demos/ABIO%20Demo%20Gallery.html"),
    ("gitproj/Forwardism.html", "/assets/pandoc.css"),
])
def test_fixed_link_resolves(built_site, source, href):
    assert href in (REPO / source).read_text()
    target = built_site / href.lstrip("/").replace("%20", " ")
    assert (target / "index.html").exists() if href.endswith("/") else target.exists()


@pytest.mark.parametrize("source, dead", [
    ("projects.markdown", "/gitproj/ob-skills/"),
    ("gitproj/AlienBiology/index.md", "/abio-docs/demos/index.html"),
    ("gitproj/DeliberativeCoherence/index.md", "/abio-docs/demos/index.html"),
    ("gitproj/Forwardism.html", "/assets/css/pandoc.css"),
])
def test_dead_link_is_gone(source, dead):
    assert dead not in (REPO / source).read_text()


# P7: Finder metadata and the justfile stay off the site.

def test_no_ds_store_is_tracked():
    tracked = subprocess.run(["git", "ls-files"], cwd=REPO, capture_output=True, text=True).stdout
    assert [f for f in tracked.splitlines() if f.endswith(".DS_Store")] == []
    assert subprocess.run(["git", "check-ignore", "-q", "assets/.DS_Store"], cwd=REPO).returncode == 0


def test_justfile_is_not_published(built_site):
    assert not (built_site / "justfile").exists()
