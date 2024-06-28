import json
import pyodbc
from datetime import datetime
import os

# Define your SQL Server connection parameters
server = 'Sever_name' # Change with Your Server name
database = 'Your_Database' # Change with your Database
driver = 'ODBC Driver 18 for SQL Server'  # Use the correct ODBC driver

# Connection string for Windows Authentication with TrustServerCertificate=yes
conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;TrustServerCertificate=yes'

# Function to convert date format to YYYY-MM-DD
def convert_date_format(date_str):
    if date_str is None:
        return None
    
    try:
        # Convert date string to datetime object
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        # Format datetime object to string in YYYY-MM-DD format
        return date_obj.strftime('%Y-%m-%d')
    except ValueError:
        return None

# Function to upload data from a single JSON file
def upload_json_to_sql(filename, cursor):
    try:
        # Read JSON file
        with open(filename, 'r') as file:
            data = json.load(file)

            # Assuming data is a list of JSON objects
            for obj in data:
                # Extract fields from JSON object and convert date
                date = convert_date_format(obj.get('date'))
                copyright = obj.get('copyright')
                imageid = obj.get('imageid')
                idsid = obj.get('idsid')
                accesslevel = obj.get('accesslevel')
                format = obj.get('format')
                caption = obj.get('caption')
                description = obj.get('description')
                technique = obj.get('technique')
                renditionnumber = obj.get('renditionnumber')
                baseimageurl = obj.get('baseimageurl')
                alttext = obj.get('alttext')
                width = obj.get('width')
                id = obj.get('id')
                lastupdate = convert_date_format(obj.get('lastupdate'))
                iiifbaseuri = obj.get('iiifbaseuri')
                fileid = obj.get('fileid')
                height = obj.get('height')

                # Prepare and execute the SQL insert statement
                sql = """
                INSERT INTO Image (date, copyright, imageid, idsid, accesslevel, format, 
                                   caption, description, technique, renditionnumber, 
                                   baseimageurl, alttext, width, id, lastupdate, 
                                   iiifbaseuri, fileid, height)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                """
                cursor.execute(sql, (date, copyright, imageid, idsid, accesslevel, format,
                                     caption, description, technique, renditionnumber,
                                     baseimageurl, alttext, width, id, lastupdate,
                                     iiifbaseuri, fileid, height))
        
        print(f"Data from {filename} inserted successfully.")

    except Exception as e:
        print(f"Error uploading data from {filename} to SQL Server: {str(e)}")

# Function to process all JSON files in a directory
def process_json_files(directory):
    conn = None
    cursor = None
    try:
        # Connect to SQL Server
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Iterate through files in the directory
        for filename in os.listdir(directory):
            if filename.endswith('.json'):
                file_path = os.path.join(directory, filename)
                upload_json_to_sql(file_path, cursor)
        
        # Commit the transaction
        conn.commit()
        print("All data inserted successfully.")

    except Exception as e:
        print(f"Error processing JSON files in {directory}: {str(e)}")
    finally:
        # Close connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Usage example
if __name__ == "__main__":
    directory = r'Your_path'  # Directory containing JSON files
    process_json_files(directory)
