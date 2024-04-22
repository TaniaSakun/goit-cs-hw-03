class Constants:
    read_operation = """
        Read data from the 'cats' collection in the database by id or name. Read all data if no args.
        """
    create_operation = """
    Create a new record in the 'cats' collection of the database.
    """
    update_operation = """
    Update all fields of the cat by id or update age/features by name.
    """

    delete_operation = """
    Delete cat by id or name. Delete all if no args.
    """

    unknown_operation = "Unknown operation"
    error_message = "Error: {0}"
    not_found = "Can't find the record {0} in the database"
