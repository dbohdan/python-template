from __future__ import annotations

import os
import shlex
from pathlib import Path


def source_files() -> list[Path]:
    sources = os.environ["PYTHON_SOURCES"]

    files = []
    for x in shlex.split(sources):
        path = Path(x)
        if path.is_dir():
            files.extend(path.glob("*.py"))
        else:
            files.append(path)

    return sorted(files)


def files() -> None:
    print("\n".join(str(path) for path in source_files()))
