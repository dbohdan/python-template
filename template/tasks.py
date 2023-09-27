#! /usr/bin/env python3

import os
import re
import shlex
import subprocess as sp
import sys
from pathlib import Path

import click


def run(*args, check=True, quiet=False):
    if not quiet:
        print(">", shlex.join(str(arg) for arg in args))

    sp.run(args, check=check)


def source_files():
    return (
        path
        for path in Path().glob("**/*.py")
        if path.parent.name != "attic" and not re.search(r"(?:^|[/\\])\.", str(path))
    )


@click.group()
def cli():
    pass


@cli.command()
@click.option("--fix", is_flag=True, help="Fix linter errors")
@click.pass_context
def check(ctx, fix: bool = False) -> None:
    ctx.invoke(format_)
    ctx.invoke(lint, fix=fix)
    ctx.invoke(type_)


@cli.command()
def files() -> None:
    print("\n".join(str(path) for path in source_files()))


@cli.command(name="format")
def format_() -> None:
    run("poetry", "run", "black", *source_files())


@cli.command()
@click.option("--fix", is_flag=True, help="fix linter errors")
def lint(fix: bool = False) -> None:
    extra = ["--fix"] if fix else []
    run(
        "poetry",
        "run",
        "ruff",
        *extra,
        *source_files(),
    )


@cli.command()
def test() -> None:
    run(
        "poetry",
        "run",
        "tox",
        "run",
    )


@cli.command(name="type")
def type_() -> None:
    run(
        "poetry",
        "run",
        "pyright",
        *source_files(),
    )


def main() -> None:
    os.chdir(Path(__file__).resolve().parent)
    try:
        cli()
    except sp.CalledProcessError as e:
        sys.exit(e.returncode)


if __name__ == "__main__":
    main()
