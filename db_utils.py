# db_utils.py

import pyodbc
from datetime import datetime

# Define your SQL Server connection parameters
server = 'DESKTOP-5BLFN3I'
database = 'Harvard_Art_Museum'
driver = 'ODBC Driver 18 for SQL Server'  # Use the correct ODBC driver

# Connection string for Windows Authentication with TrustServerCertificate=yes
conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;TrustServerCertificate=yes'

def get_db_connection():
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        return conn, cursor
    except pyodbc.Error as e:
        print(f"Error connecting to SQL Server: {str(e)}")
        return None, None

def close_db_connection(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()

def convert_date_format(date_str):
    if date_str is None:
        return None
    try:
        date_obj = datetime.fromisoformat(date_str)
        return date_obj.strftime('%Y-%m-%d')
    except ValueError:
        return None

def convert_datetimeoffset_format(datetime_str):
    if datetime_str is None:
        return None
    try:
        datetime_obj = datetime.fromisoformat(datetime_str.replace("Z", "+00:00"))
        return datetime_obj.isoformat()
    except ValueError:
        return None

def upload_json_to_sql(table, data, cursor):
    try:
        if table == 'Activity':
            for obj in data:
                date = convert_date_format(obj.get('date'))
                lastupdate = convert_datetimeoffset_format(obj.get('lastupdate'))
                sql = """
                INSERT INTO Activity (id, objectid, date, activitytype, activitycount, lastupdate)
                VALUES (?, ?, ?, ?, ?, ?);
                """
                cursor.execute(sql, (obj.get('id'), obj.get('objectid'), date, obj.get('activitytype'), obj.get('activitycount'), lastupdate))
        
        elif table == 'Annotation':
            for obj in data:
                createdate = convert_datetimeoffset_format(obj.get('createdate'))
                lastupdate = convert_datetimeoffset_format(obj.get('lastupdate'))
                sql = """
                INSERT INTO Annotation (imageid, idsid, confidence, accesslevel, raw_confidence, raw_name_en, raw_annotationFragment, createdate, annotationid, source, body, type, selectors_type, selectors_value, target, feature, id, lastupdate, fileid)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                """
                raw = obj.get('raw', {})
                selectors = obj.get('selectors', [{}])[0]
                cursor.execute(sql, (obj.get('imageid'), obj.get('idsid'), obj.get('confidence'), obj.get('accesslevel'), raw.get('confidence'), raw.get('name', {}).get('en'),
                                     raw.get('annotationFragment'), createdate, obj.get('annotationid'), obj.get('source'), obj.get('body'), obj.get('type'),
                                     selectors.get('type'), selectors.get('value'), obj.get('target'), obj.get('feature'), obj.get('id'), lastupdate, obj.get('fileid')))
        
        elif table == 'Audio':
            for obj in data:
                lastupdate = convert_datetimeoffset_format(obj.get('lastupdate'))
                sql = """
                INSERT INTO Audio (duration, copyright, audioid, description, id, lastupdate, transcripturl, fileid, primaryurl)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
                """
                cursor.execute(sql, (obj.get('duration'), obj.get('copyright'), obj.get('audioid'), obj.get('description'),
                                     obj.get('id'), lastupdate, obj.get('transcripturl'), obj.get('fileid'), obj.get('primaryurl')))
        
        elif table == 'Century':
            for obj in data:
                lastupdate = convert_datetimeoffset_format(obj.get('lastupdate'))
                sql = """
                INSERT INTO Century (objectcount, name, id, lastupdate, temporalorder)
                VALUES (?, ?, ?, ?, ?);
                """
                cursor.execute(sql, (obj.get('objectcount'), obj.get('name'), obj.get('id'), lastupdate, obj.get('temporalorder')))
        
        elif table == 'Classification':
            for obj in data:
                lastupdate = convert_datetimeoffset_format(obj.get('lastupdate'))
                sql = """
                INSERT INTO Classification (objectcount, name, id, lastupdate, classificationid)
                VALUES (?, ?, ?, ?, ?);
                """
                cursor.execute(sql, (obj.get('objectcount'), obj.get('name'), obj.get('id'), lastupdate, obj.get('classificationid')))
        
        elif table == 'Color':
            for obj in data:
                lastupdate = convert_datetimeoffset_format(obj.get('lastupdate'))
                sql = """
                INSERT INTO Color (colorid, name, hex, id, lastupdate)
                VALUES (?, ?, ?, ?, ?);
                """
                cursor.execute(sql, (obj.get('colorid'), obj.get('name'), obj.get('hex'), obj.get('id'), lastupdate))
        
        elif table == 'Culture':
            for obj in data:
                lastupdate = convert_datetimeoffset_format(obj.get('lastupdate'))
                sql = """
                INSERT INTO Culture (objectcount, name, id, lastupdate)
                VALUES (?, ?, ?, ?);
                """
                cursor.execute(sql, (obj.get('objectcount'), obj.get('name'), obj.get('id'), lastupdate))
        
        elif table == 'Exhibition':
            for obj in data:
                begindate = convert_date_format(obj.get('begindate'))
                enddate = convert_date_format(obj.get('enddate'))
                lastupdate = convert_datetimeoffset_format(obj.get('lastupdate'))
                sql = """
                INSERT INTO Exhibition (shortdescription, htmldescription, begindate, color, description, exhibitionid, title, temporalorder, url, textiledescription, enddate, id, lastupdate)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                """
                cursor.execute(sql, (obj.get('shortdescription'), obj.get('htmldescription'), begindate, obj.get('color'), obj.get('description'),
                                     obj.get('exhibitionid'), obj.get('title'), obj.get('temporalorder'), obj.get('url'), obj.get('textiledescription'),
                                     enddate, obj.get('id'), lastupdate))
        
        elif table == 'Gallery':
            for obj in data:
                lastupdate = convert_datetimeoffset_format(obj.get('lastupdate'))
                sql = """
                INSERT INTO Gallery (gallerynumber, labeltext, objectcount, galleryid, name, theme, id, lastupdate, floor, donorname, url)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                """
                cursor.execute(sql, (obj.get('gallerynumber'), obj.get('labeltext'), obj.get('objectcount'), obj.get('galleryid'), obj.get('name'),
                                     obj.get('theme'), obj.get('id'), lastupdate, obj.get('floor'), obj.get('donorname'), obj.get('url')))
        
        elif table == 'Group':
            for obj in data:
                lastupdate = convert_datetimeoffset_format(obj.get('lastupdate'))
                sql = """
                INSERT INTO [Group] (name, id, lastupdate)
                VALUES (?, ?, ?);
                """
                cursor.execute(sql, (obj.get('name'), obj.get('id'), lastupdate))
        
        print(f"Data for {table} inserted successfully.")
    except Exception as e:
        print(f"Error uploading data for {table} to SQL Server: {str(e)}")
