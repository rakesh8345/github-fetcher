from fastapi import FastAPI
from fastapi.responses import FileResponse
import requests
import uvicorn

app = FastAPI()



@app.get("/")
async def read_index():
    return FileResponse('index.html')

@app.get("/api/repos/{username}")
async def get_repos(username: str):
    response = requests.get(f"https://api.github.com/users/{username}/repos")
    repos = response.json()
    return repos

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=2167)
