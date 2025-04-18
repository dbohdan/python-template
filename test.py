#! /usr/bin/env python3

from __future__ import annotations

import os
import shutil
import subprocess as sp
from pathlib import Path

DATA = {
    "project_slug": "foo",
    "package_name": "baz",
}
TEST_DIR = "test"


def run(*args: str, **kwargs) -> sp.CompletedProcess:
    return sp.run(args, check=True, **kwargs)


def data() -> list[str]:
    return [x for key, value in DATA.items() for x in ("--data", f"{key}={value}")]


def main() -> None:
    root = Path(__file__).resolve().parent
    test_dir = root / TEST_DIR

    os.chdir(root)
    if test_dir.is_dir():
        for item in test_dir.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()

    run(
        "copier",
        "copy",
        *data(),
        "template",
        TEST_DIR,
    )

    os.chdir(root / TEST_DIR)
    try:
        run("uv", "sync")
        run("uv", "run", DATA["package_name"])

        run("poe", DATA["package_name"])
        run("poe", "check")
        run("poe", "files")
        run("poe", "test", "--cov")
        run("poe", "zipapp")

        run("git", "init")
        run("pre-commit", "install")
        run("git", "add", ".")
        run("git", "config", "user.email", "user@example.com")
        run("git", "config", "user.name", "User")
        run("git", "commit", "-a", "-m", "Initial commit")
    finally:
        venv_path = Path(".venv")
        if venv_path.exists():
            shutil.rmtree(venv_path)

    run("tox")


if __name__ == "__main__":
    main()
