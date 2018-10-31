"""Tests for pylint_sqlalchemy.dml_no_argument"""
# pylint: disable=redefined-outer-name

import astroid
from pylint.checkers.typecheck import TypeChecker
from pylint.testutils import UnittestLinter
import pytest

import pylint_sqlalchemy


@pytest.fixture
def linter():
    """Fixture providing a testing linter."""
    pylinter = UnittestLinter()
    pylint_sqlalchemy.register(pylinter)
    return pylinter


@pytest.fixture
def checker(linter):
    """Fixture providing a testing TypeChecker."""
    checker = TypeChecker(linter)
    checker.open()
    return checker


def test_dml_no_argument(linter, checker):
    call = astroid.extract_node(
        """
        import sqlalchemy

        TABLE = sqlalchemy.Table(
            'name', sqlalchemy.MetaData(),
            sqlalchemy.Column('id', sqlalchemy.Integer),
        )
        TABLE.insert()
        """
    )
    checker.visit_call(call)

    assert not linter.release_messages()
