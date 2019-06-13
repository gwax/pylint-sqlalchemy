"""Pylint sqlachemy hack module."""


class Session(object):
    """Session hack for sqlalchemy session."""

    public_methods = (
        "__contains__",
        "__iter__",
        "add",
        "add_all",
        "begin",
        "begin_nested",
        "close",
        "commit",
        "connection",
        "delete",
        "execute",
        "expire",
        "expire_all",
        "expunge",
        "expunge_all",
        "flush",
        "get_bind",
        "is_modified",
        "bulk_save_objects",
        "bulk_insert_mappings",
        "bulk_update_mappings",
        "merge",
        "query",
        "refresh",
        "rollback",
        "scalar",
    )

    def __init__(self, *args, **kwargs):
        """
        Init method.
        """

    def __call__(self):
        """Return public method."""
        return self.public_methods
