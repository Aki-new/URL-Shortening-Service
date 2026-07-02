from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import status
from fastapi.responses import JSONResponse

app = FastAPI()

def validate_url(url):
    protocol = url.split(":")[0]

    if protocol not in ["http", "https"]:
        return False
    return True

class URLCreate(BaseModel):
    url: str

@app.post("/shorten")
async def create_shorten_url(url: URLCreate):
    # Check if the URL is valid
    if not validate_url(url.url):
        return JSONResponse(
            status_code=400, # Bad Request
            content={"error": "Invalid URL protocol. Only http and https are allowed."}
        )
    
    # Check if the URL is already registered
    if url.url == "https://example.com/shortened-url":
        return JSONResponse(
            status_code=409, # Conflict
            content={"error": "URL is already registered."}
        )


    # Logic for creating the shortened URL


    # Return a JSON response with the shortened URL details
    return JSONResponse(
        status_code=201, # Created
        content={
            "id": "1",
            "url": "https://example.com/shortened-url",
            "shortCode": "abc123",
            "createdAt": "2023-01-01T00:00:00Z",
            "updatedAt": "2023-01-01T00:00:00Z",
        "IsTesting": True
        }
    )


@app.get("/shorten/{shortCode}")
async def get_shorten_url(shortCode: str):
    # Check if shortCode exists
    if shortCode != "abc123":
        return JSONResponse(
            status_code=404, # Not Found
            content={"error": "Shortened URL not found."}
        )   


    # Logic for retrieving the shortened URL details


    # Return a JSON response with the shortened URL details
    return JSONResponse(
        status_code=200, # OK
        content={
            "id": "1",
            "url": "https://example.com/shortened-url",
            "shortCode": f"{shortCode}",
            "createdAt": "2023-01-01T00:00:00Z",
            "updatedAt": "2023-01-01T00:00:00Z",
            }
        )


@app.put("/shorten/{shortCode}")
async def update_shorten_url(shortCode: str, url: URLCreate):
    # If the shortCode does not exist, return a 404 error
    if shortCode != "abc123":
        return JSONResponse(
            status_code=404, # Not Found
            content={"error": "Shortened URL not found."}
        )

    # Validate the URL
    if not validate_url(url.url):
        return JSONResponse(
            status_code=400, # Bad Request
            content={"error": "Invalid URL protocol. Only http and https are allowed."}
        )

    # If the URL is already registered, return a 409 error
    if url.url == "https://example.com/shortened-url":
        return JSONResponse(
            status_code=409, # Conflict
            content={"error": "URL is already registered."}
        )
    
    # Logic for updating the shortened URL


    return JSONResponse(
        status_code=200, # OK
        content={
            "id": "1",
            "url": f"{url.url}",
            "shortCode": f"{shortCode}",
            "createdAt": "2023-01-01T00:00:00Z",
            "updatedAt": "2023-01-01T00:00:00Z",
        }
    )


@app.delete("/shorten/{shortCode}")
async def delete_shorten_url(shortCode: str):
    # If the shortCode does not exist, return a 404 error
    if shortCode != "abc123":
        return JSONResponse(
            status_code=404, # Not Found
            content={"error": "Shortened URL not found."}
        )

    # Logic for deleting the shortened URL

    # Return a JSON response indicating successful deletion
    return JSONResponse(
        status_code=204, # No Content
        content=None
    )


@app.get("/shorten/{shortCode}/stats")
async def get_shorten_url_stats(shortCode: str):
    # If the shortCode does not exist, return a 404 error
    if shortCode != "abc123":
        return JSONResponse(
            status_code=404, # Not Found
            content={"error": "Shortened URL not found."}
        )

    # Logic for retrieving the shortened URL statistics

    # Return a JSON response with the shortened URL statistics
    return JSONResponse(
        status_code=200, # OK
        content={
            "shortCode": f"{shortCode}",
            "clicks": 100,
            "createdAt": "2023-01-01T00:00:00Z",
            "updatedAt": "2023-01-01T00:00:00Z",
        }
    )