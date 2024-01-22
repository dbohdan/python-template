# Python project template

This is D. Bohdan's personal template for starting Python projects.
As such,
it may change without warning,
and the maintainer is likely to reject contributions.

Python &ge; 3.9 and
[Copier](https://github.com/copier-org/copier)
are required to render the template.


## Contents

- [Assumptions](#assumptionS)
    - [A note on PyTorch](#a-note-on-pytorch)
- [Included tooling](#included-tooling)
- [Testing](#testing)
- [License](#license)


## Assumptions

The template assumes certain things about you and your work.
It assumes you want:

- Type annotations;
- Extensive linting but not for missing documentation like function docstrings;
- Automatic formatting a-la
[Black](https://black.readthedocs.io/)
  (actually using the
[Ruff formatter](https://docs.astral.sh/ruff/formatter/));
- Virtual environments managed automatically (with Poetry);
- Tests included in sdists;
- An `src/package_foo/` directory structure
  ([discussion](https://github.com/pypa/packaging.python.org/issues/320));
- No PyTorch.

The default project type is an application that is an installable package.
Minor changes,
like removing the console script,
are required for a library.

### A note on PyTorch

Installing PyTorch,
especially CPU-only,
is a
[problem in Poetry](https://github.com/python-poetry/poetry/issues/6409).
I use
[pip-tools](https://github.com/jazzband/pip-tools)
instead
in a project that depends on PyTorch.
You could also try
[miniconda](https://docs.conda.io/projects/miniconda/en/latest/)
or
[micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html).


## Included tooling

- [Poetry](https://python-poetry.org/)&thinsp;&mdash;&thinsp;packaging, dependency, and virtual environment management.
- [Poe the Poet](https://poethepoet.natn.io/)&thinsp;&mdash;&thinsp;running tasks.
- [pre-commit](https://pre-commit.com/) (configuration only)&thinsp;&mdash;&thinsp;Git pre-commit checks.
  When you create a Git repository,
  run `pre-commit install` in it.
- [Ruff](https://docs.astral.sh/ruff)&thinsp;&mdash;&thinsp;formatting and linting.
- [Pyright](https://github.com/microsoft/pyright)&thinsp;&mdash;&thinsp;type-checking.
- [Pytest](https://pytest.org/)&thinsp;&mdash;&thinsp;testing.
- Both [tox](https://tox.wiki/) and [nox](https://nox.thea.codes/)&thinsp;&mdash;&thinsp;test automation.
  The assumption is that you will only keep one of them.
- [shiv](https://github.com/linkedin/shiv)&thinsp;&mdash;&thinsp;building
  [zipapps](https://docs.python.org/3/library/zipapp.html)
  that include their dependencies.


## Testing

Run `test.py` to test the template with filler values.

There are additional dependencies for testing:

- Git
- pre-commit


## License

MIT No Attribution.
See
[LICENSE](LICENSE).
