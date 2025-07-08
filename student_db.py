import sqlite3

# Connect to (or create) student.db in your current directory
conn = sqlite3.connect('student.db')

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Create a table named 'students' if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    grade INTEGER
)
''')

# Optionally insert some sample data
cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ("Alice", 85))
cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ("Bob", 90))

# Commit changes and close the connection
conn.commit()
conn.close()

print("✅ student.db created with sample 'students' table.")
