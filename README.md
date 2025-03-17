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

This template is for a project managed with [uv](https://astral.sh/uv).
It requires uv.

Python &ge; 3.10 and [Copier](https://github.com/copier-org/copier)
are required to render the template.

Additionally, using the template requires:

- [Poe the Poet](https://poethepoet.natn.io/)&thinsp;&mdash;&thinsp;task runner
- (Optional) [pre-commit](https://pre-commit.com/)&thinsp;&mdash;&thinsp;Git pre-commit check runner.
  When you create a Git repository for a rendered template,
  run the command `pre-commit install` in it.
- (Optional) [tox](https://tox.wiki/) with [tox-uv](https://github.com/tox-dev/tox-uv)

The recommended way to install the requirements is with
[`uv tool`](https://docs.astral.sh/uv/guides/tools/#installing-tools):

```shell
uv tool install copier
uv tool install poethepoet
uv tool install pre-commit
uv tool install tox --with tox-uv
```


## Assumptions

The template assumes certain things about you and your work.
It assumes you want:

- Type annotations
- Extensive linting but not for missing documentation like function docstrings
- Automatic formatting with the
  [Ruff formatter](https://docs.astral.sh/ruff/formatter/)
- Virtual environments managed automatically
- Tests included in sdists
- An `src/package_foo/` directory structure
  ([discussion](https://github.com/pypa/packaging.python.org/issues/320))

The default project type is an application that is an installable package.
Minor changes,
like removing the console script,
are required for a library.


## Included tooling

- [Ruff](https://docs.astral.sh/ruff)&thinsp;&mdash;&thinsp;formatter and linter
- [Pyright](https://github.com/microsoft/pyright)&thinsp;&mdash;&thinsp;type-checker
- [Pytest](https://pytest.org/)&thinsp;&mdash;&thinsp;test framework
- [shiv](https://github.com/linkedin/shiv)&thinsp;&mdash;&thinsp;[zipapp](https://docs.python.org/3/library/zipapp.html)
  builder.
  Builds zipapps for distribution that include their dependencies.


## Testing

Run `test.py` to test the template with filler values.

There are additional requirements for testing:

- Git


## License

MIT No Attribution.
See [LICENSE](LICENSE).
