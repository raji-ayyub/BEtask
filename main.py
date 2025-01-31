
from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/")
def read_root():
    current_datetime = datetime.now(pytz.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")  # Correct format
    return {
        "email": "your-email@example.com",
        "current_datetime": current_datetime,
        "github_url": "https://github.com/yourusername/your-repo"
    }
