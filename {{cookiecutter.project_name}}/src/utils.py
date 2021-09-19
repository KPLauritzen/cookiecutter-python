from pathlib import Path


def get_project_root() -> Path:
    """Return the root dir of this project."""
    root = Path(__file__).resolve().parent.parent
    if root.is_dir() and root.exists():
        return root
    else:
        raise ValueError("Could not find project root. Something has gone really wrong.")
