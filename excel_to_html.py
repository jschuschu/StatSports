import pandas as pd
from bs4 import BeautifulSoup
import os

# Directory where your script and HTML files are located
input_dir = "C:/Users/LiLBitch/Downloads/COMM118 PROJECTS/20_time/"  # Adjust if necessary

# List of input and output files
files = [
    {"input": "defense_stats.html", "output": "defense_table.html"},
    {"input": "kicker_stats.html", "output": "kicker_table.html"},
    {"input": "rec_stats.html", "output": "rec_table.html"},
    {"input": "rb_stats.html", "output": "rb_table.html"},
    {"input": "qb_stats.html", "output": "qb_table.html"},
]

# Table styles for better alignment and appearance
table_style = """
<style>
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
        font-size: 18px;
        text-align: left;
    }
    th, td {
        border: 1px solid #dddddd;
        padding: 8px;
        text-align: center;
    }
    th {
        background-color: #f2f2f2;
        font-weight: bold;
    }
    tr:nth-child(even) {
        background-color: #f9f9f9;
    }
</style>
"""

def extract_and_clean_table(input_file, output_file):
    try:
        input_path = os.path.join(input_dir, input_file)
        output_path = os.path.join(input_dir, output_file)

        # Open and parse the HTML file
        with open(input_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

        # Check if the HTML file contains a frame pointing to the actual content
        frame = soup.find("frame", {"src": True})
        if frame:
            # Extract the source of the frame
            frame_src = frame["src"]
            frame_path = os.path.join(input_dir, frame_src)
            with open(frame_path, "r", encoding="utf-8") as frame_file:
                soup = BeautifulSoup(frame_file, "html.parser")

        # Try extracting tables using pandas
        try:
            tables = pd.read_html(str(soup))
            if tables:
                df = tables[0]
            else:
                print(f"No tables found in {input_file}.")
                return
        except Exception as e:
            print(f"Error processing {input_file}: {e}")
            return

        # Clean the DataFrame
        df.fillna("", inplace=True)  # Replace NaN with empty strings
        
        # Try converting numeric columns to integers where applicable
        for column in df.columns:
            if pd.api.types.is_numeric_dtype(df[column]):
                try:
                    df[column] = df[column].astype(int)
                except ValueError:
                    pass  # Ignore columns that cannot be converted
        
        # Convert the DataFrame to HTML with added table styles
        html_content = table_style + df.to_html(index=False, border=0)
        
        # Save the cleaned table as an HTML file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        print(f"Extracted and cleaned table saved to {output_path}")
    except Exception as e:
        print(f"Error processing {input_file}: {e}")

# Process each file in the list
for file in files:
    extract_and_clean_table(file["input"], file["output"])
