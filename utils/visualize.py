# import matplotlib.pyplot as plt

# def plot_top5(df, lang_name):
#     """Plot top 5 movies for given language"""
#     plt.figure(figsize=(8,5))
#     plt.barh(df["title"], df["vote_average"], color="skyblue")
#     plt.xlabel("Rating")
#     plt.title(f"Top 5 {lang_name} Movies")
#     plt.gca().invert_yaxis()  # highest rating at top
#     plt.tight_layout()
#     plt.savefig(f"charts/{lang_name}_top5.png")
#     plt.close()
#     print(f" Chart saved: charts/{lang_name}_top5.png")

import matplotlib.pyplot as plt

def plot_top5(df, lang_name):
    """Plot top 5 movies for given language with attractive styling"""
    plt.figure(figsize=(10,6))
    
    # Use different colors for each bar
    colors = plt.cm.viridis(df["vote_average"] / df["vote_average"].max())  # gradient colors
    
    bars = plt.barh(df["title"], df["vote_average"], color=colors, edgecolor='black')
    
    # Add rating labels on bars
    for bar in bars:
        width = bar.get_width()
        plt.text(width + 0.1, bar.get_y() + bar.get_height()/2,
                 f"{width:.1f}", va='center', fontsize=10, fontweight='bold')
    
    plt.xlabel("Rating", fontsize=12)
    plt.ylabel("Movie Title", fontsize=12)
    plt.title(f"Top 5 {lang_name} Movies", fontsize=14, fontweight='bold')
    
    plt.gca().invert_yaxis()  # highest rating at top
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    # Save chart
    plt.savefig(f"charts/{lang_name}_top5.png", dpi=150, facecolor='w')
    plt.close()
    
    print(f"✅ Chart saved: charts/{lang_name}_top5.png")
