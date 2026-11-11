"""Baseline task tests. They import only baseline.tasks: the lesson 4 test rule."""
import pytest

from baseline.tasks import first_missing


@pytest.mark.req("BASELINE-04")
def test_first_missing_returns_first_absent_item():
    assert first_missing(["a", "b", "c"], ["a", "c"]) == "b"


@pytest.mark.req("BASELINE-04")
def test_first_missing_returns_none_when_all_present():
    assert first_missing(["a", "b"], ["b", "a"]) is None