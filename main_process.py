# main_process.py

import os
import json
import sys  # Import sys module for modifying Python path
sys.path.append(r'D:\Project\Harvard-Art_Museum')  # Add the directory containing db_utils.py to the Python path
from db_utils import get_db_connection, close_db_connection, upload_json_to_sql

# Function to process all JSON files in a directory
def process_json_files(directory, target_folders):
    conn, cursor = get_db_connection()
    if not conn or not cursor:
        return

    try:
        for table_dir in target_folders:
            table_path = os.path.join(directory, table_dir)
            if os.path.isdir(table_path):
                table_name = table_dir.capitalize()
                print(f"Processing table directory: {table_name}")
                for filename in os.listdir(table_path):
                    if filename.endswith('.json'):
                        file_path = os.path.join(table_path, filename)
                        with open(file_path, 'r') as file:
                            try:
                                data = json.load(file)
                                print(f"Uploading data for table: {table_name}")
                                upload_json_to_sql(table_name, data, cursor)
                            except json.JSONDecodeError as e:
                                print(f"Error reading JSON file {file_path}: {str(e)}")

        conn.commit()
        print("All data inserted successfully.")
    except Exception as e:
        print(f"Error processing JSON files: {str(e)}")
    finally:
        close_db_connection(conn, cursor)

# Usage example
if __name__ == "__main__":
    directory = r'D:\Project\Harvard-Art_Museum\Data'
    target_folders = ['activity', 'annotation', 'audio', 'century', 'classification', 'color', 'culture', 'exhibition', 'gallery', 'group']
    process_json_files(directory, target_folders)
