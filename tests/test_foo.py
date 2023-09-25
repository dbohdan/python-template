from __future__ import annotations

import unittest

import foo


class TestFoo(unittest.TestCase):
    def test_basic(self) -> None:
        assert foo.bar()
