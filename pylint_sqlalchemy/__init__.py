"""Establish pylint_sqlalchemy package."""

import astroid
from astroid import MANAGER

from pylint_sqlalchemy import plugin
from pylint_sqlalchemy._version import __version__  # pylint: disable=unused-import
from pylint_sqlalchemy.dml_no_argument import strip_dml


def register(_):
    """Register plugins with pylint."""
    MANAGER.register_transform(astroid.FunctionDef, strip_dml)


__all__ = ["plugin"]
