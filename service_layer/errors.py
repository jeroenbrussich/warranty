# ./service_layer/errors.py


class StorageError(Exception):
    """Het opslaan of wijzigen in de database is mislukt om een andere reden
    dan een dubbele waarde. De UI hoeft zo niets van SQLite te kennen."""
