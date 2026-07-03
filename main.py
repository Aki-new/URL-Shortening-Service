from fastapi import FastAPI, status
from pydantic import BaseModel, HttpUrl
from datetime import datetime

app = FastAPI()

# This class validate if a URL is valid using Pydantic's HttpUrl type. 
# If the URL is not valid, it will raise a ValidationError.
class URLInput(BaseModel):
    url: HttpUrl

# This class is used to define the output model for the shortened URL.
class URLOutput(BaseModel):
    id: int
    url: HttpUrl
    shortCode: str
    createdAt: datetime
    updatedAt: datetime

# This class is used to define the output model for the shortened URL with statistics.
class URLOutputStats(URLOutput):
    clicks: int


@app.post("/shorten", response_model=URLOutput, status_code=status.HTTP_201_CREATED)
async def create_shorten_url(url: URLInput):    
    # Logic for creating the shortened URL


    # Return a JSON response with the shortened URL details
    return {
            "id": 1,
            "url": "https://example.com/shortened-url",
            "shortCode": "abc123",
            "createdAt": datetime(2023, 1, 1, 0, 0, 0),
            "updatedAt": datetime(2023, 1, 1, 0, 0, 0),
        }


@app.get("/shorten/{shortCode}", response_model=URLOutput, status_code=status.HTTP_200_OK)
async def get_shorten_url(shortCode: str):
    # Logic for retrieving the shortened URL details


    # Return a JSON response with the shortened URL details
    return {
            "id": 1,
            "url": "https://example.com/shortened-url",
            "shortCode": f"{shortCode}",
            "createdAt": datetime(2023, 1, 1, 0, 0, 0),
            "updatedAt": datetime(2023, 1, 1, 0, 0, 0),
        }
        

@app.put("/shorten/{shortCode}", response_model=URLOutput, status_code=status.HTTP_200_OK)
async def update_shorten_url(shortCode: str, url: URLInput): 
    # Logic for updating the shortened URL


    return {
            "id": 1,
            "url": f"{url.url}",
            "shortCode": f"{shortCode}",
            "createdAt": datetime(2023, 1, 1, 0, 0, 0),
            "updatedAt": datetime(2023, 1, 1, 0, 0, 0),
        }
    

@app.delete("/shorten/{shortCode}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_shorten_url(shortCode: str):
    # Logic for deleting the shortened URL

    
    return None 


@app.get("/shorten/{shortCode}/stats", response_model=URLOutputStats, status_code=status.HTTP_200_OK)
async def get_shorten_url_stats(shortCode: str):
    # Logic for retrieving the shortened URL statistics

    # Return a JSON response with the shortened URL statistics
    return {
            "id": 1,
            "url": "https://example.com/shortened-url",
            "shortCode": f"{shortCode}",
            "createdAt": datetime(2023, 1, 1, 0, 0, 0),
            "updatedAt": datetime(2023, 1, 1, 0, 0, 0),
            "clicks": 100,
        }