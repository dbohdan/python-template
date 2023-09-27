#! /usr/bin/env python3
# Project tasks.
# This file must only depend on the Python standard library.

from __future__ import annotations

import argparse
import os
import re
import shlex
import subprocess as sp
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Generator

    Task = Callable[..., None]


tasks: dict[str, Task] = {}


def run(*args: str | Path, check: bool = True, quiet: bool = False) -> None:
    if not quiet:
        print(">", shlex.join(str(arg) for arg in args))

    sp.run(args, check=check)


def source_files() -> Generator[Path, None, None]:
    return (
        path
        for path in Path().glob("**/*.py")
        if path.parent.name != "attic" and not re.search(r"(?:^|[/\\])\.", str(path))
    )


def task(*, name: str = ""):
    def inner(f: Task) -> Task:
        nonlocal name
        tasks[name if name else f.__name__.replace("_", "-")] = f

        return f

    return inner


@task()
def check(*, fix: bool = False) -> None:
    format_()
    lint(fix=fix)
    type_()


@task()
def files() -> None:
    print("\n".join(str(path) for path in source_files()))


@task(name="format")
def format_() -> None:
    run("poetry", "run", "black", *source_files(), check=False)


@task()
def lint(*, fix: bool = False) -> None:
    extra = ["--fix"] if fix else []
    run(
        "poetry",
        "run",
        "ruff",
        *extra,
        *source_files(),
        check=False,
    )


@task()
def test() -> None:
    run(
        "poetry",
        "run",
        "tox",
        "run",
    )


@task(name="type")
def type_() -> None:
    run(
        "poetry",
        "run",
        "pyright",
        *source_files(),
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
