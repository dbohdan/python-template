#! /usr/bin/env python3

import os
import shutil
import subprocess as sp
from pathlib import Path


TEST_DIR = "test"


def main() -> None:
    root = Path(__file__).resolve().parent
    test_dir = root / "test"

    os.chdir(root)
    if test_dir.is_dir():
        shutil.rmtree(test_dir)
    sp.run(
        [
            "copier",
            "copy",
            "-d",
            "project_name=foo",
            "-d",
            "package_name=baz",
            "template",
            TEST_DIR,
        ],
        check=True,
    )

    os.chdir(root / TEST_DIR)
    sp.run(["poetry", "install"], check=True)
    sp.run(["poetry", "run", "pytest"], check=True)


if __name__ == "__main__":
    main()
