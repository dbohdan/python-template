#! /usr/bin/env python3
# Project tasks.
# This file must only depend on the Python standard library.

from __future__ import annotations

import argparse
import os
import re
import subprocess as sp
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Generator

    Task = Callable[..., None]


tasks: dict[str, Task] = {}


def source_files() -> Generator[Path, None, None]:
    return (
        path
        for path in Path().glob("**/*.py")
        if path.parent.name != "attic" and not re.search(r"(?:^|[/\\])\.", str(path))
    )


def task(f: Task) -> Task:
    tasks[f.__name__] = f
    return f


@task
def check(*, fix: bool = False) -> None:
    format()
    lint(fix=fix)
    type()


@task
def files() -> None:
    print("\n".join(str(path) for path in source_files()))


@task
def format() -> None:
    sp.run(["poetry", "run", "black", *source_files()], check=False)


@task
def lint(*, fix: bool = False) -> None:
    extra = ["--fix"] if fix else []
    args = [
        "poetry",
        "run",
        "ruff",
        *extra,
        *source_files(),
    ]
    sp.run(
        args,
        check=False,
    )


@task
def run() -> None:
    for action in ("scan", "send"):
        sp.run(
            ["poetry", "run", "python", "-m", "telegram_watch", action],
            check=False,
        )


@task
def test() -> None:
    sp.run(
        ["poetry", "run", "tox", "run"],
        check=False,
    )


@task
def type() -> None:
    args = [
        "poetry",
        "run",
        "pyright",
        *source_files(),
    ]
    sp.run(
        args,
        check=False,
    )


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(required=True)

    spar_by_task = {}
    for name, func in tasks.items():
        subparser = subparsers.add_parser(name)
        subparser.set_defaults(func=func)
        spar_by_task[name] = subparser

    for task in ("check", "lint"):
        spar_by_task[task].add_argument(
            "--fix",
            action="store_true",
            default=False,
            help="fix linter errors",
        )

    return parser.parse_args()


def main():
    os.chdir(Path(__file__).resolve().parent)

    args = cli()
    args_dict = vars(args)
    func_args = {key: args_dict[key] for key in args_dict if key != "func"}
    args.func(**func_args)


if __name__ == "__main__":
    main()
