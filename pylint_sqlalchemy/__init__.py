"""Establish pylint_sqlalchemy package."""

import astroid
from astroid import MANAGER

from pylint_sqlalchemy._version import __version__  # pylint: disable=unused-import
import pylint_sqlalchemy.dml_no_argument


def register(_):
    """Register plugins with pylint."""
    MANAGER.register_transform(
        astroid.FunctionDef, pylint_sqlalchemy.dml_no_argument.strip_dml
    )
