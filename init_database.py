import sqlite3
import os

# Create the database directory if it doesn't exist
os.makedirs('database', exist_ok=True)  

# Established a connection to the SQLite database
conexion = sqlite3.connect('database/url_shortener.db')
cursor = conexion.cursor()

# Read the schema from the schema.sql file
with open('schema.sql', 'r', encoding='utf-8') as schema_file:
    schema = schema_file.read()

# Apply the schema to the database
cursor.executescript(schema)

# Save the changes and close the connection
conexion.commit()
conexion.close()
