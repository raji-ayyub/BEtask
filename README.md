I# HNG12 Stage 0 - FastAPI Public API

This is a simple public API built using *FastAPI* for the *HNG12 Stage 0 Backend Task*.

## 📌 Features
- Returns JSON response with:
  - Your registered HNG12 email.
  - Current UTC datetime in ISO 8601 format.
  - GitHub repository URL.
- Uses FastAPI for quick responses.
- Supports Cross-Origin Resource Sharing (CORS).

## 🚀 Live API URL
*Base URL:* [https://your-app.onrender.com](https://your-app.onrender.com)  
(Replace with your deployed Render URL)

## 🛠️ How to Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/raji-ayyub/BEtaskgit

   cd your-repo

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Run the API: 
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000

4. visit http://127.0.0.1:8000/ in your browser.


📌 API Documentation

GET /

Returns:

{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}



## 🚀 Live API URL
*Base URL:* [https://publicapi-ix3u.onrender.com](https://publicapi-ix3u.onrender.com)

💼 Looking to Hire?

Looking to hire Python developers? Check out HNG Python Developers.