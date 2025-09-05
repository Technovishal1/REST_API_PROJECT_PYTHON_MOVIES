import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# ---------------------------
# Load Movies from Database
# ---------------------------
def load_movies(db_path="database/movies.db"):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM top_movies", conn)
    conn.close()
    return df


# ---------------------------
# Streamlit Page Config
# ---------------------------
st.set_page_config(
    page_title="🎬 Multi-Language Movies Dashboard",
    layout="wide",
    page_icon="🎬"
)

# # ---------------------------
# # Custom CSS
# # ---------------------------
# st.markdown("""
# <style>
# .card {
#     display: inline-block;
#     width: 230px;
#     height: 480px;
#     margin: 10px;
#     padding: 12px;
#     border-radius: 12px;
#     background: #1e1e1e;
#     color: white;
#     box-shadow: 0 4px 8px rgba(0,0,0,0.3);
#     vertical-align: top;
#     overflow-y: auto;
#     flex-shrink: 0;
# }
# .poster {
#     width: 100%;
#     height: 300px;
#     object-fit: cover;
#     border-radius: 10px;
# }
# .title {
#     font-size: 16px;
#     font-weight: bold;
#     margin-top: 8px;
# }
# .stars {
#     color: gold;
#     margin-top: 4px;
# }
# .meta {
#     font-size: 13px;
#     color: #bbb;
#     margin-top: 3px;
# }
# .meta.overview {
#     font-size: 12px;
#     margin-top: 5px;
#     color: #ddd;
# }
# .scroll-container {
#     display: flex;
#     overflow-x: auto;
#     padding-bottom: 10px;
# }
# .scroll-container::-webkit-scrollbar {
#     height: 8px;
# }
# .scroll-container::-webkit-scrollbar-thumb {
#     background: #888;
#     border-radius: 4px;
# }
# .scroll-container::-webkit-scrollbar-thumb:hover {
#     background: #555;
# }
# </style>
# """, unsafe_allow_html=True)
# ---------------------------
# Custom CSS + Auto Scroll JS
# ---------------------------
st.markdown("""
<style>
.card {
    display: inline-block;
    width: 230px;
    height: 480px;
    margin: 10px;
    padding: 12px;
    border-radius: 12px;
    background: #1e1e1e;
    color: white;
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    vertical-align: top;
    overflow-y: auto;
    flex-shrink: 0;
}
.poster {
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 10px;
}
.title {
    font-size: 16px;
    font-weight: bold;
    margin-top: 8px;
}
.stars {
    color: gold;
    margin-top: 4px;
}
.meta {
    font-size: 13px;
    color: #bbb;
    margin-top: 3px;
}
.meta.overview {
    font-size: 12px;
    margin-top: 5px;
    color: #ddd;
}
/* 🔥 Back-and-forth auto scroll */            
.auto-scroll {
    display: flex;
    gap: 10px;
    animation: scroll-bounce 15s ease-in-out infinite alternate;
    will-change: transform;
}

@keyframes scroll-bounce {
    from {
        transform: translateX(0);
    }
    to {
        transform: translateX(-50%);
    }
}


</style>

<script>
    function autoScrollContainers() {
        const containers = document.querySelectorAll('.auto-scroll');
        containers.forEach(container => {
            let scrollAmount = 0;
            function step() {
                if (scrollAmount < container.scrollWidth - container.clientWidth) {
                    container.scrollLeft += 1;
                    scrollAmount += 1;
                } else {
                    scrollAmount = 0;
                    container.scrollLeft = 0;
                }
                requestAnimationFrame(step);
            }
            step();
        });
    }
    window.addEventListener('load', autoScrollContainers);
</script>
""", unsafe_allow_html=True)


# ---------------------------
# Title & Timestamp
# ---------------------------
st.markdown(
    f"""
    <div style="
        position: absolute;
        top: 10px;
        right: 20px;
        color: #FF0000;
        font-size: 0.9rem;">
        ⏰ Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    </div>
    """,
    unsafe_allow_html=True
)
st.title("🎬 VISHAL - Multi-Language Movies Dashboard")
st.write("Showing Top Movies from multiple languages — posters with details and table from database.")

# ---------------------------
# Load Data
# ---------------------------
movies_df = load_movies()

# ---------------------------
# Clean Column Names
# ---------------------------
movies_df.columns = movies_df.columns.str.strip()  # Remove spaces
lang_cols = [col for col in movies_df.columns if "lang" in col.lower()]
if lang_cols:
    lang_col = lang_cols[0]
else:
    st.warning("No language column found! Using 'Unknown'.")
    movies_df["Language"] = "Unknown"
    lang_col = "Language"

# ---------------------------
# Sidebar Filters
# ---------------------------
st.sidebar.header("MOVIES")
languages = movies_df[lang_col].dropna().unique()

selected_langs = st.sidebar.multiselect(
    "Select Languages",
    options=list(languages),
    default=list(languages)  # show all by default
)

# ---------------------------
# Show Movies by Language
# ---------------------------
for lang in selected_langs:   # ✅ only loop over chosen languages
    st.subheader(f"🌐 {lang} Movies")
    lang_df = movies_df[movies_df[lang_col] == lang].head(10)

    #html_content = '<div class="scroll-container">'          #  for manually scroll
    html_content = '<div class="auto-scroll">'

    for _, row in lang_df.iterrows():
        try:
            rating = float(row.get('rating', 0))
            stars = '★' * int(rating) + '☆' * (10 - int(rating))
        except:
            stars = '☆☆☆☆☆☆☆☆☆☆'
        
        html_content += f'<div class="card">'
        html_content += f'<img src="{row.get("poster","")}" class="poster">'
        html_content += f'<div class="title">{row.get("title","N/A")}</div>'
        html_content += f'<div class="stars"><b>Rating:</b> <span style="color:gold;">{stars}</span> <span style="color:green;">{row.get("rating","N/A")}</span>/10</div>'
        html_content += f'<div class="meta"><b>Release date:</b> {row.get("release_date","N/A")}</div>'
        html_content += f'<div class="meta"><b>Director:</b> {row.get("director","N/A")}</div>'
        html_content += f'<div class="meta"><b>Producer:</b> {row.get("producer","N/A")}</div>'
        html_content += f'<div class="meta"><b>Music:</b> {row.get("music","N/A")}</div>'
        html_content += f'<div class="meta"><b>Studio:</b> {row.get("studio","N/A")}</div>'
        html_content += f'<div class="meta overview"><b>Description:</b> {str(row.get("overview","N/A"))[:200]}...</div>'
        html_content += '</div>'
    html_content += '</div>'
    st.markdown(html_content, unsafe_allow_html=True)

# ---------------------------
# Show DB Table
# ---------------------------
st.subheader("📊 Movies Database Table")

if selected_langs:  # show only if user picked at least one language
    table_df = movies_df[movies_df[lang_col].isin(selected_langs)][
        ["title", "rating", "release_date", lang_col,"timestamp"]
    ]

    table_df = table_df.rename(columns={
        "title": "Title",
        "rating": "Rating",
        "release_date": "Release Date",
        lang_col: "Language",
        "timestamp": "Time Stamp"
    })

    st.dataframe(table_df)
else:
    st.info("Please select a language from the sidebar to see the movies table.")

