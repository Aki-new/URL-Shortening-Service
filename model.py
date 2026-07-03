import sqlite3 as db
from datetime import datetime

class Database:
    def __init__(self):
        self.connection = db.connect("database/url_shortener.db")
        self.cursor = self.connection.cursor()

    def save_shorten_url(self, url: str, shortCode: str):
        """
            Save a URL to the database
        """
        # Logic for saving the shortened URL to the database
        self.cursor.execute(
            "INSERT INTO urls (url, short_code) VALUES (?, ?)",
            (url, shortCode)
        )
        self.connection.commit()
        return {
            "id": self.cursor.lastrowid,
            "url": url,
            "shortCode": shortCode,
            "createdAt": datetime.now(),
            "updatedAt": datetime.now(),
        }
    
    def get_shorten_url(self, shortCode: str):
        """
            Get a URL using the shortcode from the database
        """
        # Logic for retrieving the shortened URL details from the database
        self.cursor.execute(
            "SELECT url_id, url, short_code, created_at, updated_at FROM urls WHERE short_code = ?",
            (shortCode,)
        )

        result = self.cursor.fetchone()
        if result is None:
            return None
        
        return {
            "id": result[0],
            "url": result[1],
            "shortCode": result[2],
            "createdAt": result[3],
            "updatedAt": result[4],
        }

    def update_shorten_url(self, shortCode: str, url: str):
        """
            Updates a URL associated with a shortcode in the database
        """
        # Logic for updating the shortened URL in the database
        self.cursor.execute(
            "UPDATE urls SET url = ? WHERE short_code = ?",
            (url, shortCode)
        )

        self.connection.commit()

        return self.get_shorten_url(shortCode)

    def delete_shorten_url(self, shortCode: str):
        """
            Deletes a shortcode and its associated URL from the database
        """
        # Logic for deleting the shortened URL from the database
        self.cursor.execute(
            "DELETE FROM urls WHERE short_code = ?",
            (shortCode,)
        )
        self.connection.commit()

        return True
    
    def get_shorten_url_stats(self, shortCode: str):
        """
            Retrieves statistics for a short code
        """
        # Logic for retrieving the statistics of the shortened URL from the database
        self.cursor.execute(
            "SELECT * FROM urls WHERE short_code = ?",
            (shortCode,)
        )

        result = self.cursor.fetchone()
        if result is None:
            return None
        
        return {
            "id": result[0],
            "url": result[1],
            "shortCode": result[2],
            "createdAt": result[3],
            "updatedAt": result[4],
            "clicks": result[5]
        }
    
    def url_exists(self, url: str):
        """
            Checks if a URL exists.
            Returns True if it exists.
            Returns False if it does not exist.
        """
        self.cursor.execute(
            "SELECT COUNT(*) FROM urls WHERE url = ? LIMIT 1",
            (url,)    
        )

        result = self.cursor.fetchone()

        count = result[0]

        if count == 0:
            return False
        
        return True

    def short_code_exists(self, shortCode: str):
        """
            Checks if a Short code exists.
            Returns True if it exists.
            Returns False if it does not exist.
        """
        self.cursor.execute(
            "SELECT COUNT(*) FROM urls WHERE short_code = ? LIMIT 1",
            (shortCode,)    
        )

        result = self.cursor.fetchone()

        count = result[0]

        if count == 0:
            return False

        return True

    def close(self):
        self.connection.close()