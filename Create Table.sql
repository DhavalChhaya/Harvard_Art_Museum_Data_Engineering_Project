CREATE TABLE Activity (
    id INT PRIMARY KEY,
    objectid INT,
    date DATE,
    activitytype VARCHAR(50),
    activitycount INT,
    lastupdate DATETIMEOFFSET
);


CREATE TABLE Annotation (
    imageid INT,
    idsid INT,
    confidence FLOAT,
    accesslevel INT,
    raw_confidence FLOAT,
    raw_name_en VARCHAR(100),
    raw_annotationFragment VARCHAR(100),
    createdate DATETIMEOFFSET,
    annotationid INT PRIMARY KEY,
    source VARCHAR(50),
    body VARCHAR(Max),
    type VARCHAR(50),
    selectors_type VARCHAR(50),
    selectors_value VARCHAR(100),
    target VARCHAR(500),
    feature VARCHAR(50),
    id INT,
    lastupdate DATETIMEOFFSET,
    fileid INT
);

CREATE TABLE Audio (
    duration INT,
    copyright VARCHAR(255),
    audioid INT PRIMARY KEY,
    description TEXT,
    id INT,
    lastupdate DATETIMEOFFSET,
    transcripturl VARCHAR(255),
    fileid INT,
    primaryurl VARCHAR(255)
);

CREATE TABLE Century (
    objectcount INT,
    name VARCHAR(255),
    id INT PRIMARY KEY,
    lastupdate DATETIMEOFFSET,
    temporalorder INT
);

CREATE TABLE Classification (
    objectcount INT,
    name VARCHAR(255),
    id INT PRIMARY KEY,
    lastupdate DATETIMEOFFSET,
    classificationid INT
);

CREATE TABLE Color (
    colorid INT PRIMARY KEY,
    name VARCHAR(255),
    hex CHAR(7),
    id INT,
    lastupdate DATETIMEOFFSET
);

CREATE TABLE Culture (
    objectcount INT,
    name VARCHAR(255),
    id INT PRIMARY KEY,
    lastupdate DATETIMEOFFSET
);

CREATE TABLE Exhibition (
    shortdescription TEXT,
    htmldescription TEXT,
    begindate DATE,
    color VARCHAR(255),
    description TEXT,
    exhibitionid INT PRIMARY KEY,
    title VARCHAR(255),
    temporalorder INT,
    url VARCHAR(255),
    textiledescription TEXT,
    enddate DATE,
    id INT,
    lastupdate DATETIMEOFFSET
);

CREATE TABLE Gallery (
    gallerynumber VARCHAR(255),
    labeltext TEXT,
    objectcount INT,
    galleryid INT PRIMARY KEY,
    name VARCHAR(255),
    theme TEXT,
    id INT,
    lastupdate DATETIMEOFFSET,
    floor VARCHAR(255),
    donorname VARCHAR(255),
    url VARCHAR(255)
);

CREATE TABLE [Group] (
    name VARCHAR(255),
    id INT PRIMARY KEY,
    lastupdate DATETIMEOFFSET
);


