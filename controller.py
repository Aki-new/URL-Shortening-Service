from pydantic import HttpUrl
from fastapi import HTTPException, status
from datetime import datetime
from model import Database

class URLController:
    def __init__(self):
        self.db = Database()

    def create_shorten_url(self, url: HttpUrl):
        url = str(url)  # Convert HttpUrl to string

        # Check if URL exists
        if self.db.url_exists(url):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="URL is already registered."
            )

        shortCode = self.generate_short_code()

        data = self.db.save_shorten_url(url, shortCode)

        data["shortCode"] = shortCode

        return data

    def get_shorten_url(self, shortCode: str):
        data = self.db.get_shorten_url(shortCode)

        # If URL no exists
        if data is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, # Not Found
                detail="Shortened URL not found."
            )   

        # Logic for retrieving the shortened URL details
        return data

    def update_shorten_url(self, shortCode: str, url: HttpUrl):
        url = str(url)  # Convert HttpUrl to string

        # If the shortCode does not exist, return a 404 error
        if not self.db.short_code_exists(shortCode):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Shortened URL not found."
            )

        # If the URL is already registered, return a 409 error
        if self.db.url_exists(url):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="URL is already registered."
            )
    
        # Logic for updating the shortened URL
        return self.db.update_shorten_url(shortCode, url)

    def delete_shorten_url(self, shortCode: str):
        # If the shortCode does not exist, return a 404 error
        if not self.db.short_code_exists(shortCode):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Shortened URL not found."
            )

        self.db.delete_shorten_url(shortCode)

        # Logic for deleting the shortened URL
        return None

    def get_shorten_url_stats(self, shortCode: str):
        # If the shortCode does not exist, return a 404 error
        if not self.db.short_code_exists(shortCode):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Shortened URL not found."
            )

        # Logic for retrieving the shortened URL statistics
        return self.db.get_shorten_url_stats(shortCode)
    
    def generate_short_code(self):
        import random
        import string

        chars = string.ascii_letters + string.digits
        result = ''.join(random.choices(chars, k=6))

        return result