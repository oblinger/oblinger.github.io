"""Regression tests for the site's build scripts (deep scan r1, 2026-10-29).

Run: python3 -m pytest tools/tests -q   (from the repo root)
"""

import importlib.machinery
import importlib.util
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]


def load_trip_index():
    sys.dont_write_bytecode = True
    loader = importlib.machinery.SourceFileLoader("trip_index", str(REPO / "tools" / "trip-index"))
    spec = importlib.util.spec_from_loader("trip_index", loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


def test_local_build_succeeds_with_configured_plugins():
    """_config.yml names jekyll-sitemap; the Gemfile must carry it or `just preview` dies."""
    with tempfile.TemporaryDirectory() as out:
        result = subprocess.run(
            ["bundle", "exec", "jekyll", "build", "-q", "-s", str(REPO), "-d", out],
            cwd=REPO, capture_output=True, text=True,
            env={**__import__("os").environ, "BUNDLE_GEMFILE": str(REPO / "Gemfile")})
        assert result.returncode == 0, result.stderr[-2000:]
        assert (Path(out) / "sitemap.xml").exists()


def test_python_bytecode_is_ignored():
    """`just publish` runs `git add -A`; a stray tools/__pycache__ must not reach the public repo."""
    probe = "tools/__pycache__/trip-indexcpython-312.pyc"
    result = subprocess.run(["git", "check-ignore", "-q", probe], cwd=REPO)
    assert result.returncode == 0


@pytest.mark.parametrize("text, expected", [
    ("password:: hunter\n", "hunter"),
    ("password::  two words here  \nnext:: x\n", "two words here"),
])
def test_password_is_the_whole_line(text, expected):
    assert load_trip_index().parse_password(text) == expected


def test_empty_password_line_does_not_borrow_the_next_line():
    with pytest.raises(SystemExit):
        load_trip_index().parse_password("password::\nnext:: value\n")
