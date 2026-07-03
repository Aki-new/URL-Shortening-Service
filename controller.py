from pydantic import HttpUrl
from fastapi import HTTPException, status
from datetime import datetime

class URLController:
    def create_shorten_url(self, url: HttpUrl):
        if url == "https://example.com/shortened-url":
            return HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="URL is already registered."
            )

        # Logic for creating the shortened URL
        return {
            "id": 1,
            "url": "https://example.com/shortened-url",
            "shortCode": "abc123",
            "createdAt": datetime(2023, 1, 1, 0, 0, 0),
            "updatedAt": datetime(2023, 1, 1, 0, 0, 0),
        }

    def get_shorten_url(self, shortCode: str):
        # Check if shortCode exists
        if shortCode != "abc123":
            return HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, # Not Found
                detail="Shortened URL not found."
            )   

        # Logic for retrieving the shortened URL details
        return {
            "id": 1,
            "url": "https://example.com/shortened-url",
            "shortCode": f"{shortCode}",
            "createdAt": datetime(2023, 1, 1, 0, 0, 0),
            "updatedAt": datetime(2023, 1, 1, 0, 0, 0),
        }

    def update_shorten_url(self, shortCode: str, url: HttpUrl):
        # If the shortCode does not exist, return a 404 error
        if shortCode != "abc123":
            return HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Shortened URL not found."
            )

        # If the URL is already registered, return a 409 error
        if url == "https://example.com/shortened-url":
            return HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="URL is already registered."
            )
    
        # Logic for updating the shortened URL
        return {
            "id": 1,
            "url": "https://example.com/shortened-url",
            "shortCode": f"{shortCode}",
            "createdAt": datetime(2023, 1, 1, 0, 0, 0),
            "updatedAt": datetime(2023, 1, 1, 0, 0, 0),
        }

    def delete_shorten_url(self, shortCode: str):
        # If the shortCode does not exist, return a 404 error
        if shortCode != "abc123":
            return HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Shortened URL not found."
            )

        # Logic for deleting the shortened URL
        return {
            "id": 1,
            "url": "https://example.com/shortened-url",
            "shortCode": f"{shortCode}",
            "createdAt": datetime(2023, 1, 1, 0, 0, 0),
            "updatedAt": datetime(2023, 1, 1, 0, 0, 0),
        }

    def get_shorten_url_stats(self, shortCode: str):
        # If the shortCode does not exist, return a 404 error
        if shortCode != "abc123":
                    return HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail="Shortened URL not found."
                    )

        # Logic for retrieving the shortened URL statistics
        return {
            "id": 1,
            "url": "https://example.com/shortened-url",
            "shortCode": f"{shortCode}",
            "createdAt": datetime(2023, 1, 1, 0, 0, 0),
            "updatedAt": datetime(2023, 1, 1, 0, 0, 0),
            "clicks": 100,
        }