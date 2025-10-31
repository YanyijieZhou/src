"""Top-level src package initializer.

This file makes the `src` directory a proper Python package so imports like
`from src import project_folder` work inside notebooks and scripts when the
repository root is on sys.path.

Note: alternatively you can add `src/` to PYTHONPATH or install the package
editable with `pip install -e .`.
"""

# Optional: re-export subpackages for convenience
try:
    from . import create_project  # noqa: F401
    from . import getmy  # noqa: F401
except Exception:
    # keep import-time robust if package layout is adjusted
    pass
