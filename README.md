# Globussoft Data Science Task

**Applicant:** Kushal Gowda H M  
**Date:** May 2026

This repository contains the complete, production-ready solutions for the Globussoft Data Science technical assessment. 

---

## 📦 Repository Structure

```text
├── Amazon Laptop Web Scraping/
│   ├── scraper.py
│   ├── main.py
│   └── amazon_page.html
├── Face Authentication/
│   └── main.py
├── .gitattributes
└── README.md
```


🛒 Task 1: Amazon.in Web ScraperDirectory: Amazon Laptop Web ScrapingOverviewA robust web scraper designed to extract laptop product listings from Amazon. Due to Amazon's strict 503 Service Unavailable anti-bot measures, this script is engineered to parse a locally saved HTML dump of the search results, ensuring reliable, uninterrupted data extraction without triggering IP blocks.Data Extracted:Product TitlePriceRating / ReviewsProduct LinkHow to Run:Bashcd "Amazon Laptop Web Scraping"
python main.py
👤 Task 2: Face Authentication APIDirectory: Face AuthenticationOverviewA fully functional REST API built with FastAPI that utilizes the state-of-the-art DeepFace library to verify whether two uploaded facial images belong to the same person. The API enforces face detection, calculates mathematical embeddings, and returns a structured JSON response matching the precise assessment requirements.Engineering Decisions:Environment: Explicitly pinned to Python 3.11 to ensure absolute stability with the underlying TensorFlow/C++ backend required by DeepFace.Model: DeepFace (VGG-Face metric) for highly accurate, low-distance facial matching.How to Run Locally:1. Install Dependencies:Bashpip install fastapi uvicorn python-multipart deepface tf-keras
2. Start the Server:(Ensure you are routing through a stable Python 3.11/3.12 environment)Bashcd "Face Authentication"
py -3.11 -m uvicorn main:app --reload
3. Test the API:Open your browser and navigate to the interactive Swagger UI dashboard:👉 http://127.0.0.1:8000/docsExpand the POST /verify endpoint, click "Try it out", upload two images, and click "Execute".Sample API ResponseJSON{
  "verification_result": "same person",
  "similarity_score": 0.220651,
  "bounding_boxes": {
    "image1": {
      "x": 341,
      "y": 226,
      "w": 381,
      "h": 381,
      "left_eye": [588, 368],
      "right_eye": [453, 375]
    },
    "image2": {
      "x": 289,
      "y": 184,
      "w": 323,
      "h": 323,
      "left_eye": [496, 297],
      "right_eye": [386, 301]
    }
  }
}
🛠️ Technology Stack & LibrariesCategoryLibraryPurposeWeb ScrapingBeautifulSoup4Parsing complex DOM structures and extracting product data.Web ScrapingrequestsHandling HTTP operations.API FrameworkFastAPIBuilding the high-performance asynchronous REST API.ServeruvicornASGI web server implementation for FastAPI.Machine LearningdeepfaceCore AI engine for facial detection, alignment, and verification.ML Backendtf-keras / tensorflowDeep learning mathematical backend.
