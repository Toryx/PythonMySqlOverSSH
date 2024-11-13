# List of libraries used : 
1. pymysql
2. sshtunnel
3. dotenv


Since we have fetchall all the rows will be returned in myresult. ``` myresult = mycursor.fetchall() ```.
If you want only one to check if it is working u can use fetchone or fetchmany(x) where x is the number of records you want to return 
> [!WARNING]   
However if you choose fetchone it is not considered a list so the following ```for``` wont work .

So in the next lines of code : 
```
    for row in myresult:
        company_id = row[0]
        print(str(company_id))
```
only the first column of the query is printed.

> [!TIP]
You can then run an update for the specific company_id 
by writing the following code after the print : 
```
 update_query = '''UPDATE [TABLE] SET X=Y WHERE TABLE.ID = $s'''
 mycursor.execute(update_query,(company_id))
 conn.commit()
```

