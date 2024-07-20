
# TO USE FLASK MIGRATION FIRST

* `flask db init` initialize flask migration if the `first time`
* then make model change
* Run `flask db migrate -m "Add phone column to User model."` to create a migration script that includes your changes.
* `flask db upgrade` Apply the migration to update the database schema with the new column.

