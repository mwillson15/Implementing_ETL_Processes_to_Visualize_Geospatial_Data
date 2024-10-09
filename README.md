# Implementing_ETL_Processes_to_Visualize_Geospatial_Data
This repository contains files for a project which implemented ETL processes to visualize geospatial data using the GeoAPI API. There are 9 files for this project in the "Implementing_ETL_Processes_to_Visualize_Geospatial_Data" folder.

## Objectives
- Apply/practice ETL processes such as extracting data from different sources and loading data into a database
- Practice intergrating Python and SQL programming
- Gain a better understanding of interacting with APIs

## Motivations
This was one of the final projects in a Python specialization I completed which aimed to apply many of the topics taught throughout the specialization including Python/SQL programming and interacting with APIs.

## Reading Through Files
Below are descriptions of the project files in the order you should go about reading them.

### "Visualizing_Geospatial_Data_env_requirements.txt"
This is a text file which contains the requirements for the virtual environment used in this project. Note, the "sqlite3" module used in this project requires SQLite 3.15.2 or newer.

### "Project_Outline"
This is a JPEG file which contains an outline of the steps of the project. Look at this image first for a visual layout of how the project was conducted.

### "where.data"
This is a "Brackets" document or more generally a text file containing location names at each line (e.g., University of Central Florida).

### "geoload.py"
This is a Python script file which contains the code for the first step of this project. This script parses the location names in "where.data" and constructs URLs to request geospatial coordinate data from a proxy of the GeoAPI API. Then, caches these data into an SQLite database.

### "opengeo.sqlite" and "opengeo_copy.sqlite"
These are SQLite database files. The "opengeo.sqlite" file is the database created by "geoload.py" and can potentially be modified if you makes changes to the code in "geoload.py". The "opengeo_copy.sqlite" file is a copy of this database and will not be modified, regardless of any changes to the project scripts. 

### "geodump.py"
This is a Python script file which contains the code for the second step of this project. This script parses the location name and corresponding coordinate data from "opengeo.sqlite". Then, writes these data into a JavaScript file.

### "where.js" 
This is a JavaScript file created by "geodump.py" which contains the location name and coordinate pairs. 

### "where.html"
This is a HTML document which extracts the data from "where.js" and visualizes it using the Open Street Map browser application. This document runs the code automatically as this project was more an excerise in ETL processes. In other words, when you open "where.html", a Open Street Map browser tab is opened with all the corresponding locations plotted on a map. Refer to the link provided in the map visualization to understand how the code works. However, it is written in Polish so translation may be necessary.

## Notes
The proxy to the GeoAPI API used in this project is highly rate limited. Running these scripts too much will result in very slow computation times. I recommend reading through the scripts to understand the programming involved, browsing through the database that was created, and opening "where.html" to see the final visualization.

