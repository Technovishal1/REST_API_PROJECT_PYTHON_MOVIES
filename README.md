# REST API Movies Dashboard

## 1. Introduction
This project is about building a Movie Dashboard Application that:
- Fetches real-time movie data from REST APIs (TMDb/OMDb).
- Applies an ETL process (Extract, Transform, Load) to structure the data.
- Stores the processed data in a SQLite database.
- Presents the results in an interactive Streamlit dashboard with posters, ratings, and release dates. 

## 2. Objectives
- Learn how REST APIs work in real-world projects.
- Perform data extraction, cleaning, and transformation.
- Store structured data in a relational database.
- Visualize insights with an interactive dashboard.
- Explore multi-language movie datasets in a single platform.
   
<img width="600" height="400" alt="e868a90b-796c-4529-88e6-7680fd4d98fe" src="https://github.com/user-attachments/assets/69c4a024-395f-4f8d-b7e5-e41a785259a1" />



## 3. Technologies Used

### Python

**Why?** Python is powerful for data processing and has libraries for everything.  
**Used for:** API requests, data transformation, and dashboard development.  

Libraries:  
- `requests` → fetch data from REST API  
- `pandas` → clean, transform, and manage data  
- `sqlite3` → connect and store data in SQLite DB  
- `streamlit` → create interactive dashboard  

### SQLite Database
**Why?** Lightweight and portable database (no server setup).  
**Used for:** Storing processed movies in a structured format.  

Table Structure:  
- Title  
- Rating  
- Language  
- Release Date  
- Poster  
- Director / Producer / Studio  
- Overview  
- Timestamp

### REST API (TMDb/OMDb)
**Why?** Provides live, multilingual movie data.  
**Used for:** Fetching real-time movies in Hindi, Kannada, Tamil, Telugu, Malayalam, English, etc.  
**Format:** JSON responses  
## Basics of REST API

A **REST API (Representational State Transfer Application Programming Interface)** allows two systems to communicate using HTTP requests.  
It is **stateless**, meaning each request from a client must contain all necessary information (server does not remember previous requests).  

### Key HTTP Methods
- **GET** → Retrieve data (used to fetch movies).  
- **POST** → Send data to the server.  
- **PUT** → Update existing data.  
- **DELETE** → Remove data.  

### Example JSON Response from Movie API
```json
{
  "title": "Kantara",
  "language": "Kannada",
  "release_date": "2022-09-30",
  "rating": 8.5,
  "overview": "A mystical thriller set in the forests of Karnataka.",
  "poster": "https://image.tmdb.org/t/p/w500/sample.jpg"
}
```

<img width="704" height="259" alt="rest-api-model" src="https://github.com/user-attachments/assets/20a2c7c9-2a83-4200-93e8-005358d5e737" />


### Streamlit
**Why?** Easy to build dashboards with Python.  
**Used for:** Displaying posters, ratings, release dates, and database tables interactively.  

## 4. Why Pandas?
- Converts raw JSON → DataFrame easily.  
- Helps in cleaning, filtering, and schema consistency.  
- Allows adding computed fields like timestamp.  
- Great for small-to-medium datasets like this project.  

## 5. Implementation Steps

## Step 1: Extract (utils/extract.py)
- Fetch movies from REST API.  
- Select movies by language.  
- Store raw results in JSON format.
  
<img width="700" height="400" alt="361f1d1f-fe56-4ea7-9b44-0e4d9a402107" src="https://github.com/user-attachments/assets/fcd4ff2d-1ce0-4ffe-895f-f43936baef7a" />


## Step 2: Transform (utils/transform.py) 
- Convert JSON → Pandas DataFrame.  
- Standardize column names.  
- Pick Top 5 movies per language.  
- Add timestamp for reporting.
   
<img width="700" height="400" alt="b6602d91-84f1-4217-b926-84b9de4bbaf8" src="https://github.com/user-attachments/assets/d0016e78-d1b7-497d-ae24-1810b6be939e" />


## Step 3: Load (utils/load.py) 

- Create SQLite database `movies.db`.  
- Save DataFrame into `top_movies` table.  
- Schema ensures consistent storage.
  
<img width="700" height="400" alt="0e6f0b5b-177a-4a6f-b64c-4f22ec097f56" src="https://github.com/user-attachments/assets/ca1f8c0a-c32e-4626-9885-e352a207da54" />
<img width="497" height="337" alt="Screenshot 2025-09-04 172613" src="https://github.com/user-attachments/assets/3dcd2812-34a2-40b3-b196-9ffb5921b13b" />



## Step 4: Visualize (dashboard.py) 
- Load data from SQLite.  
- Display movie posters with details.  
- Show database table (Title, Rating, Release Date, Language, Timestamp).  
- Allow filtering by language selection.
  

## 6. Project Structure
<img width="700" height="400" alt="294374df-9413-4725-9eb2-b2e1150e6e84" src="https://github.com/user-attachments/assets/1582d90e-1e05-4a69-ae59-8c9d6add7301" />


## 7. API Key Handling
Never expose your API key in public repositories.
**Store it in `.env`:**


**Add `.env` to `.gitignore`.**

**Load it in Python with:**
```python
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")
```
## How to Run

```bash
# Clone repository
git clone https://github.com/yourusername/movie-dashboard.git
cd movie-dashboard

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run dashboard.py
```

## Project Outcome

- Successfully built an **end-to-end ETL pipeline** (Extract → Transform → Load) for real-time movie data.  
- Implemented **secure API key handling** using `.env` files and `.gitignore`.  
- Created a **SQLite database** (`movies.db`) for structured movie storage.  
- Designed an **interactive Streamlit dashboard** that displays:  
  - Movie posters  
  - Ratings  
  - Release dates  
  - Language-based filtering  
- Gained hands-on experience in **REST API integration, data engineering, and visualization**.  
- Provided a scalable base for future extensions such as embedded device integration and advanced analytics.
  
<img width="1357" height="611" alt="Screenshot 2025-09-04 201606" src="https://github.com/user-attachments/assets/a29e930b-ef3c-46de-a637-3ed2320b81d4" />
<img width="1356" height="553" alt="Screenshot 2025-09-04 202557" src="https://github.com/user-attachments/assets/f35db1b3-c67b-46c6-9d8a-93f47fcfac71" />
<img width="895" height="487" alt="Screenshot 2025-09-04 202753" src="https://github.com/user-attachments/assets/e8c250aa-d7e7-4608-95a7-6f254d7a6528" />

https://github.com/user-attachments/assets/9b404bba-d017-415d-87eb-f4a38f63be6e

---

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.  


