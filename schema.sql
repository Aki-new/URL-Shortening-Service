BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "urls" (
	"url_id"	INTEGER NOT NULL,
	"url"	TEXT NOT NULL UNIQUE,
	"short_code"	INTEGER NOT NULL UNIQUE,
	"created_at"	TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
	"updated_at"	TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
	"clicks"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("url_id" AUTOINCREMENT)
);

CREATE TRIGGER IF NOT EXISTS actualizar_fecha_urls
AFTER UPDATE ON "urls"
BEGIN
    UPDATE "urls" 
    SET "updated_at" = datetime('now', 'localtime') 
    WHERE "url_id" = NEW."url_id";
END;

COMMIT;
