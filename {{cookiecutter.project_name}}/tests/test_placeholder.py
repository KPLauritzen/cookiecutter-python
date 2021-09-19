from pathlib import Path


def test_placeholder():
    assert True


def test_project_root():
    from src.utils import get_project_root

    assert Path(__file__).parent.parent == get_project_root()
