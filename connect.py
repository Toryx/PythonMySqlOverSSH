import pymysql
from sshtunnel import SSHTunnelForwarder
from dotenv import load_dotenv
import os
load_dotenv()

sql_hostname = os.getenv('SQL_HOSTNAME')
sql_username = os.getenv('SQL_USERNAME')
sql_password =  os.getenv('SQL_PASSWORD') 
sql_main_database = os.getenv('SQL_DB') 
sql_port = int(os.getenv('SQL_PORT') )
ssh_host = os.getenv('SSH_HOST')  
ssh_user = os.getenv('SSH_USER')
ssh_port = int(os.getenv('SSH_PORT') )
sql_ip = os.getenv('SQL_IP')
mypkey = os.getenv('SSH_PASSWORD')

with SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_user,
        ssh_password=mypkey,
        remote_bind_address=(sql_hostname, sql_port)) as tunnel:
    conn = pymysql.connect(host='127.0.0.1', user=sql_username,
            passwd=sql_password, db=sql_main_database,
            port=tunnel.local_bind_port)
    query = '''SELECT * FROM [TABLE]'''
    mycursor = conn.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    for row in myresult:
        company_id = row[0]
        print(str(company_id))


