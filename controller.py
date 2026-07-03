from pydantic import HttpUrl
from fastapi import HTTPException, status
from datetime import datetime
from model import Database

class URLController:
    def __init__(self):
        self.db = Database()

    def create_shorten_url(self, url: HttpUrl):
        url = str(url)  # Convert HttpUrl to string
        self._ensure_short_code_exists(url)

        shortCode = self.generate_short_code()

        data = self.db.save_shorten_url(url, shortCode)
        data["shortCode"] = shortCode

        return data

    def get_shorten_url(self, shortCode: str):
        # If the short code does not exist, neither does the URL.
        not self._ensure_short_code_exists(shortCode)
        # Logic for retrieving the shortened URL details
        return self.db.get_shorten_url(shortCode)

    def update_shorten_url(self, shortCode: str, url: HttpUrl):
        url = str(url)  # Convert HttpUrl to string
        # If the shortCode does not exist, return a 404 error
        self._ensure_short_code_exists(shortCode)
        # If the URL is already registered, return a 409 error
        self._ensure_url_not_exists(url)

        return self.db.update_shorten_url(shortCode, url)

    def delete_shorten_url(self, shortCode: str):
        # If the shortCode does not exist, return a 404 error
        self._ensure_short_code_exists(shortCode)

        return self.db.delete_shorten_url(shortCode)

    def get_shorten_url_stats(self, shortCode: str):
        # If the shortCode does not exist, return a 404 error
        self._ensure_short_code_exists(shortCode)
        
        return self.db.get_shorten_url_stats(shortCode)
    
    def generate_short_code(self):
        import random
        import string

        chars = string.ascii_letters + string.digits
        result = ''.join(random.choices(chars, k=6))

        return result
    
    def _ensure_short_code_exists(self, shortCode: str):
        """Lanza 404 si el shortCode NO existe."""
        if not self.db.short_code_exists(shortCode):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Shortened URL not found."
            )

    def _ensure_url_not_exists(self, url: str):
        """Lanza 409 si la URL YA existe."""
        if self.db.url_exists(url):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="URL is already registered."
            )