from __future__ import annotations

__all__ = ["__version__", "bar", "main"]
__version__ = "0.1.0"


def bar() -> bool:
    return True


def main() -> None:
    print("Hello!")  # noqa: T201


if __name__ == "__main__":
    main()
