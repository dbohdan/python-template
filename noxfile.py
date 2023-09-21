from __future__ import annotations

import nox

PYTHON_VERSIONS = ["3.8", "3.9", "3.10", "3.11"]


@nox.session(python=PYTHON_VERSIONS, tags=["test"])
def tests(session: nox.Session) -> None:
    session.run("poetry", "install", "--no-root", "--sync", external=True)
    session.run("pytest")
