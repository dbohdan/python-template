# Python project template

This is D. Bohdan's personal template for starting Python projects.
As such,
it may change without warning,
and the maintainer is likely to reject contributions.


## Contents

- [Requirements](#requirements)
- [Assumptions](#assumptionS)
    - [A note on PyTorch](#a-note-on-pytorch)
- [Included tooling](#included-tooling)
- [Testing](#testing)
- [License](#license)


## Requirements

Python &ge; 3.9
and
[Copier](https://github.com/copier-org/copier)
are required to render the template.
I suggest installing recent Python with,
e.g.,
[pyenv](https://github.com/pyenv/pyenv).

Additionally,
using the template requires:

- [Poetry](https://python-poetry.org/)&thinsp;&mdash;&thinsp;project manager
- [Poe the Poet](https://poethepoet.natn.io/)&thinsp;&mdash;&thinsp;task runner
- (Optional) [pre-commit](https://pre-commit.com/)&thinsp;&mdash;&thinsp;Git pre-commit check runner.
  When you create a Git repository for a rendered template,
  run the command `pre-commit install` in it.
- (Optional)
  Either
  [tox](https://tox.wiki/)
  or
  [nox](https://nox.thea.codes/)&thinsp;&mdash;&thinsp;test automation.
  I have included both
  with the assumption that
  any project will keep only one of them.

The recommended way to install the requirements is with
[pipx](https://github.com/pypa/pipx):

```shell
pipx install copier
pipx install nox
pipx install poethepoet
pipx install poetry
pipx install pre-commit
pipx install tox
```


## Assumptions

The template assumes certain things about you and your work.
It assumes you want:

- Type annotations
- Extensive linting but not for missing documentation like function docstrings
- Automatic formatting a-la
[Black](https://black.readthedocs.io/)
  (actually using the
[Ruff formatter](https://docs.astral.sh/ruff/formatter/))
- Virtual environments managed automatically (with Poetry)
- Tests included in sdists
- An `src/package_foo/` directory structure
  ([discussion](https://github.com/pypa/packaging.python.org/issues/320))
- No PyTorch

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

- [Ruff](https://docs.astral.sh/ruff)&thinsp;&mdash;&thinsp;formatter and linter
- [Pyright](https://github.com/microsoft/pyright)&thinsp;&mdash;&thinsp;type-checker
- [Pytest](https://pytest.org/)&thinsp;&mdash;&thinsp;test framework
- [shiv](https://github.com/linkedin/shiv)&thinsp;&mdash;&thinsp;[zipapp](https://docs.python.org/3/library/zipapp.html)
  builder.
  Builds zipapps that include their dependencies
  for distribution.


## Testing

Run `test.py` to test the template with filler values.

There are additional requirements for testing:

- Git


## License

MIT No Attribution.
See
[LICENSE](LICENSE).
