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
        shutil.rmtree(test_dir)

    run(
        "copier",
        "copy",
        *data(),
        "template",
        TEST_DIR,
    )

    os.chdir(root / TEST_DIR)
    try:
        run("poetry", "install")
        run("poetry", "run", "baz")
        run("poe", "check")
    finally:
        run("poetry", "env", "remove", "--all")

    run("tox", "run", "-e", "py38")
    run("nox", "--pythons", "3.8")


if __name__ == "__main__":
    main()
