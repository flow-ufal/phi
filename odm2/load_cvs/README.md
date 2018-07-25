This folder contains a Python script for automatically loading CV terms from the master lists at http://vocabulary.odm2.org into a blank instance of an ODM2 database. It should work with ODM2 databases in Microsoft SQL Server, MySQL, and PostgreSQL.  
  
This script should be run from the command line. The following is an example:  
  
`python cvload.py postgrsql+psycopg2://phi:passwd@localhost:5432/odm2`  
  
The connection string can be any format supported by sqlalchemy. For example:  
  
`{database type}+{driver name}://{username}:{password}@{server address}:{port number}/{database name}`  
  
This script has the following dependencies: Python 2.7 or 3 Sqlalchemy Database Driver (choose the one for your database)  
  
+ mysql: pymysql  
+ mssql: pyodbc  
+ postgresql: psycopg2  
  
For SQLite, the connection string looks like the following:  
  
`sqlite:///{database name}`  
  
For example:  
  
`sqlite:///odm2.sqlite`

\
\
_This guide was written based on the 'read me' file at [ODM2 repository](https://github.com/ODM2/ODM2/tree/master/src/load_cvs)._
