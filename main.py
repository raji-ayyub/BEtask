
from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/")
def read_root():
    current_datetime = datetime.now(pytz.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")  # Correct format
    return {
        "email": "ayyubraji87@gmail.com",
        "current_datetime": current_datetime,
        "github_url": "https://github.com/raji-ayyub/BEtask"
    }
