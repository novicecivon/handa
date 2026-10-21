import pytest

from handa.ingest.sources import SOURCES, get_source


def test_source_keys_are_unique() -> None:
    keys = [s.key for s in SOURCES]
    assert len(keys) == len(set(keys))


def test_every_source_declares_a_licence() -> None:
    assert all(s.licence for s in SOURCES)


def test_unknown_source_raises() -> None:
    with pytest.raises(KeyError):
        get_source("does-not-exist")
