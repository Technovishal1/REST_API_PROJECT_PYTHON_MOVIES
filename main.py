#importing functions from other files 
from utils.extract import fetch_movies     # Importing the function 'fetch_movies' from extract.py to fetch movies from TMDb API
from utils.transform import process_movies # Importing the function 'process_movies' from transform.py to process/filter the fetched movies (like selecting top 5) 
from utils.load import save_to_db, db_path          # Saves the processed top movies into a SQLite database. This is “L” in ETL
from utils.visualize import plot_top5      # Creates charts or plots for the top 5 movies for each language.
import os                                  # <-- import os for saving CSV
import pandas as pd                        #Data handling and processing.


languages = { "Kannada": "kn","Tamil": "ta","Malayalam": "ml","Japanese": "ja" } # dictionary mapping Language names → TMDb API language codes.


#  Separate function to save each language's movies to CSV
# def save_language_csv(movies, lang_name):
#     os.makedirs("data", exist_ok=True)     # ensure folder exists
#     file_path = f"data/{lang_name}.csv"
#     pd.DataFrame(movies).to_csv(file_path, index=False, encoding="utf-8")
#     print(f" Saved {len(movies)} movies to {file_path}")


#  main Exicution block
if __name__ == "__main__":

    all_data = []                          #this will store the processed top 5 movies for all languages.

    for lang_name, lang_code in languages.items():              # Loop through each language and its API code
        movies = fetch_movies(language=lang_code, pages=1)      # Fetch raw movies from API (5 pages)
        print(f" {lang_name}: Fetched {len(movies)} movies")    # Print number of movies fetched

        # save raw data as csv
        # save_language_csv(movies, lang_name)
        

        df_top5 = process_movies(movies, lang_name)             # Get top 5 movies for this language
         #  Check columns before appending (debugging safety)
        
        all_data.append(df_top5)                                # Add top 5 DataFrame to list
        
        # Save and plot
        #plot_top5(df_top5, lang_name)

    # combine all languages
    final_df = pd.concat(all_data, ignore_index=True)           # Combine all languages into one DataFrame
    save_to_db(final_df, db_path)                                        # Save combined top 5 movies to database
    print("\n Final Top 5 Movies in Each Language:")
    #print(final_df)
