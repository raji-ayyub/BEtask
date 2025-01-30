
# 🚀 HNG12 Stage 0 - FastAPI Public API

This is a *public API* built with *FastAPI* for the *HNG12 Stage 0 Backend Task*.  
It provides basic information, including the registered email, the current UTC datetime, and the GitHub repository URL.

---

## 📌 Features
- Returns JSON response with:
  - Your registered *HNG12 email*.
  - *Current UTC datetime* in ISO 8601 format.
  - *GitHub repository URL*.
- Uses *FastAPI* for fast and efficient responses.
- *CORS enabled* for cross-origin access.

---

## 🚀 Live API URL
*Base URL:* [https://publicapi-ix3u.onrender.com](https://publicapi-ix3u.onrender.com)  
(Replace with your deployed Render URL)

---

## 🛠️ How to Run Locally

1. *Clone the Repository*
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo

2. Create a Virtual Environment (Optional)

python -m venv env
source env/bin/activate  # On Windows, use: env\Scripts\activate


3. Install Dependencies

pip install -r requirements.txt


4. Run the API

uvicorn main:app --host 0.0.0.0 --port 8000


5. Test in Browser or Postman Open http://127.0.0.1:8000/ in your browser to see the JSON response.




---

📌 API Documentation

🔹 Request

Method: GET

Endpoint: /

Example URL:

https://publicapi-ix3u.onrender.com/


🔹 Response Format (200 OK)

{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}


---

📌 Example Usage

Using Curl

curl -X GET https://publicapi-ix3u.onrender.com

Using Python (Requests Library)

import requests

response = requests.get("https://publicapi-ix3u.onrender.com")
print(response.json())

Using JavaScript (Fetch API)

fetch("https://publicapi-ix3u.onrender.com")
  .then(response => response.json())
  .then(data => console.log(data));


---

📜 Deployment Instructions

This API is deployed on Render. If you want to deploy your own version:

1. Push Your Code to GitHub

git add .
git commit -m "Deploy FastAPI on Render"
git push origin main


2. Deploy on Render

Go to Render

Create a New Web Service

Connect your GitHub repository

Use the following Start Command:

uvicorn main:app --host 0.0.0.0 --port $PORT

Click Deploy.





---

💼 Looking to Hire?

Looking to hire Python developers? Check out HNG Python Developers.


---

📝 License

This project is open-source and available under the MIT License.

---