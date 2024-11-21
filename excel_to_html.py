import pandas as pd
<<<<<<< HEAD
from bs4 import BeautifulSoup
import os

# List of input and output files
files = [
    {"input": "kicker_stats.html", "output": "kicker_table.html"},
    {"input": "def_stats.html", "output": "def_table.html"},
    {"input": "qb_stats.html", "output": "qb_table.html"},
    {"input": "te_stats.html", "output": "te_table.html"},
    {"input": "wr_stats.html", "output": "wr_table.html"},
]

def extract_and_clean_table(input_file, output_file):
    try:
        # Check if the HTML contains frames
        with open(input_file, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
        
        # Look for a frame or iframe and follow its source
        frame = soup.find("frame") or soup.find("iframe")
        if frame and frame.get("src"):
            frame_src = os.path.join(os.path.dirname(input_file), frame.get("src"))
            print(f"Following frame source: {frame_src}")
            input_file = frame_src  # Redirect to the frame source

        # Try extracting tables with pandas
        tables = pd.read_html(input_file)
        if tables:
            # Extract the first table
            df = tables[0]
            
            # Remove NaN values by replacing with an empty string
            df.fillna("", inplace=True)
            
            # Force conversion of all numeric columns to integers if possible
            for column in df.columns:
                if pd.api.types.is_numeric_dtype(df[column]):
                    # Try converting to int only if all values are whole numbers
                    try:
                        df[column] = df[column].astype(int)
                    except ValueError:
                        pass  # Skip columns where conversion isn't valid
            
            # Save the table to a clean HTML file
            df.to_html(output_file, index=False, border=0)
            print(f"Extracted and cleaned table saved to {output_file}")
        else:
            print(f"No tables found in {input_file}.")
    except Exception as e:
        print(f"Error processing {input_file}: {e}")

# Process each file
for file in files:
    extract_and_clean_table(file["input"], file["output"])

=======

# Function to convert Excel to HTML and save to file
def excel_to_html_table(file_path, output_file, table_id):
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # Convert the DataFrame to HTML with the specified table ID and class for styling
    html_table = df.to_html(index=False, table_id=table_id, classes='stats-table')
    
    # Write to the output HTML file with UTF-8 encoding
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_table)

# Convert each position's stats Excel file to an HTML table
excel_to_html_table("C:/Users/LiLBitch/Downloads/COMM118 PROJECTS/20_time/wr Stats.xlsx", "wr_stats.html", "wr-table")
excel_to_html_table("C:/Users/LiLBitch/Downloads/COMM118 PROJECTS/20_time/te Stats.xlsx", "te_stats.html", "te-table")
excel_to_html_table("C:/Users/LiLBitch/Downloads/COMM118 PROJECTS/20_time/rb stats.xlsx", "rb_stats.html", "rb-table")
excel_to_html_table("C:/Users/LiLBitch/Downloads/COMM118 PROJECTS/20_time/qb stats.xlsx", "qb_stats.html", "qb-table")
>>>>>>> 369e1d1b22f6bf749b12d02d9ddf720ddab44720

