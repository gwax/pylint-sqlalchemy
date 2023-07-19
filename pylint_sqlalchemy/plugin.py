"""Pylint sqlalchemy plugin module."""
import astroid
from astroid import MANAGER
from astroid.builder import AstroidBuilder

from pylint_sqlalchemy.orm import Session


def handle_session(cls):
    """Handle the sqlalchemy.orm.scoping.scoped_session."""
    if cls.name == "scoped_session":
        source_files = cls.parent.file.split("/")
        source_files[-1] = "session.py"
        module = AstroidBuilder(MANAGER).file_build(
            "/".join(source_files), "sqlalchemy.orm.session"
        )

        session = None
        for node in module.body:
            if isinstance(node, astroid.ClassDef) and node.name == "Session":
                session = node
                break

        if session:
            for method in Session.public_methods:
                cls.locals[method] = session.locals.get(method, None)

        return cls

    return None


MANAGER.register_transform(astroid.ClassDef, handle_session)
