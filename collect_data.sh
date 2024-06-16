#!/bin/sh

# Define SQLite database file path
DB_FILE="visitors.db"

# Get visitor's IP address
IP_ADDRESS=$(curl -s https://api.ipify.org)

# Get current date and time
VISIT_TIME=$(date '+%Y-%m-%d %H:%M:%S')

# Referrer URL (assuming passed as argument)
REFERRER="$1"

# Ensure SQLite database file exists; create table if it doesn't exist
sqlite3 $DB_FILE <<EOF
CREATE TABLE IF NOT EXISTS visitors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip_address TEXT,
    visit_time TEXT,
    referrer TEXT
);
EOF

# Insert visitor data into SQLite database
sqlite3 $DB_FILE <<EOF
INSERT INTO visitors (ip_address, visit_time, referrer)
VALUES ('$IP_ADDRESS', '$VISIT_TIME', '$REFERRER');
EOF
