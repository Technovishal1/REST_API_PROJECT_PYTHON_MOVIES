import sqlite3
import os

db_path = r"F:\DIGICOMM SEMI\python training\REST_API_Project\database\movies.db"

def save_to_db(df, db_path=db_path):
    """Save dataframe into SQLite database"""
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)

    # Final schema for DB
    required_cols = [
        "title", "rating", "language", "release_date", "poster",
        "director", "producer", "music", "studio", "overview", "timestamp"
    ]
    df_db = df[[col for col in required_cols if col in df.columns]].copy()

    df_db.to_sql("top_movies", conn, if_exists="replace", index=False)
    conn.close()
    print("✅ Data saved to database")
