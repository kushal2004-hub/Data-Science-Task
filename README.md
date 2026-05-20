# Globussoft Data Science Task

This repository contains my solutions for the Globussoft Data Science technical assessment.

## Task 1: Amazon Laptop Web Scraping
A web scraper designed to extract laptop product data (names, prices, ratings) from Amazon.
- **Folder:** `Amazon Laptop Web Scraping`
- **Tools Used:** Python, BeautifulSoup, Requests

## Task 2: Face Authentication API
A REST API that uses state-of-the-art Deep Learning (DeepFace) to verify if two uploaded images contain the same person. It accurately returns the verification status, similarity score, and bounding box coordinates for the detected faces.
- **Folder:** `Face Authentication`
- **Tools Used:** Python, FastAPI, Uvicorn, DeepFace

### How to Run the Face Authentication API Locally
1. Open a terminal and navigate into the `Face Authentication` directory.
2. Install the required dependencies:
   `pip install fastapi uvicorn python-multipart deepface`
3. Start the server (ensure you are using Python 3.11 or 3.12):
   `py -3.11 -m uvicorn main:app --reload`
4. Open your web browser and navigate to the interactive Swagger dashboard to test the API:
   `http://127.0.0.1:8000/docs`
