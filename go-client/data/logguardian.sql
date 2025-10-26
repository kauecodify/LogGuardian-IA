# database

package main

import (
	"database/sql"
	"log"
	"time"
	_ "modernc.org/sqlite"
)

var db *sql.DB

func InitDB() {
	var err error
	db, err = sql.Open("sqlite", "./data/logguardian.db")
	if err != nil {
		log.Fatal(err)
	}

	createTables := `
	CREATE TABLE IF NOT EXISTS users (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		username TEXT UNIQUE,
		password_hash TEXT,
		role TEXT,
		created_at DATETIME DEFAULT CURRENT_TIMESTAMP
	);

	CREATE TABLE IF NOT EXISTS logs (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		log_line TEXT,
		is_anomaly BOOLEAN,
		score REAL,
		timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
		synced BOOLEAN DEFAULT 0
	);
	`
	if _, err := db.Exec(createTables); err != nil {
		log.Fatal(err)
	}
}

func SaveLog(line string, anomaly bool, score float64) {
	_, err := db.Exec(
		"INSERT INTO logs (log_line, is_anomaly, score) VALUES (?, ?, ?)",
		line, anomaly, score,
	)
	if err != nil {
		log.Println("Erro ao salvar log:", err)
	}
}

func UnsyncedLogs() *sql.Rows {
	rows, _ := db.Query("SELECT id, log_line, is_anomaly, score FROM logs WHERE synced=0")
	return rows
}

func MarkSynced(id int) {
	db.Exec("UPDATE logs SET synced=1 WHERE id=?", id)
}
