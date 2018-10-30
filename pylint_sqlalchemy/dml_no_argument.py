"""Linter to fix missing `dml` argument for pylint and sqlalchemy."""
import astroid
import astroid.node_classes


def strip_dml(node):
    """Strip dml argument from insert/update/delete nodes."""
    if isinstance(node, astroid.FunctionDef) and node.qname() in (
        "sqlalchemy.sql.selectable.TableClause.delete",
        "sqlalchemy.sql.selectable.TableClause.insert",
        "sqlalchemy.sql.selectable.TableClause.update",
    ):
        node.args.args = [
            a
            for a in node.args.args
            if not (isinstance(a, astroid.AssignName) and a.name == "dml")
        ]
