import pandas as pd
from bs4 import BeautifulSoup
import os

# Input and output file paths
input_directory = "rb_stats_files"  # Directory containing the referenced files
input_file = os.path.join(input_directory, "sheet001.html")  # The referenced data file
output_file = "rb_cleaned_table.html"  # Output for the cleaned table

def clean_table(input_file, output_file):
    try:
        # Read the HTML file and extract tables
        tables = pd.read_html(input_file)
        if tables:
            df = tables[0]  # Get the first table
            
            # Replace NaN values with an empty string
            df.fillna("", inplace=True)
            
            # Remove .0 by converting appropriate columns to integers
            for column in df.columns:
                if pd.api.types.is_numeric_dtype(df[column]):
                    try:
                        # Convert column to integer if possible
                        df[column] = df[column].apply(lambda x: int(x) if isinstance(x, float) and x.is_integer() else x)
                    except ValueError:
                        continue
            
            # Save the cleaned table to an HTML file
            df.to_html(output_file, index=False, border=0)
            print(f"Cleaned table saved to {output_file}")
        else:
            print(f"No tables found in {input_file}")
    except Exception as e:
        print(f"Error processing {input_file}: {e}")

# Clean the RB stats table
clean_table(input_file, output_file)
