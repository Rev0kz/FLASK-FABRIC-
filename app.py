from flask import Flask, request, jsonify
import json 
import psycopg2  


app = Flask(__name__)

 

@app.route('/api/v1/info', methods=['GET'])
def get_info():
     conn = psycopg2.connect(user='postgres',
                             password='cantwinkatyou',
                             host='127.0.0.1',
                             port='5432',
                             database='bookstore')
     print("database connected successfully")
     cursor = conn.cursor()
     table_select_query = "select * from apiinfo"
     cursor.execute(table_select_query)
     print("retrieving values from the apiinfo table")
     apiinfo_records = cursor.fetchall()
     api_list=[] 
     for row in apiinfo_records: 
       a_dict = {}
       a_dict['buildate'] = row[0]
       a_dict['version'] = row[1]
       a_dict['methods'] = row[2]
       api_list.append(a_dict)
     conn.close()
     return jsonify({'api_version' : api_list}), 200      



@app.route('/api/v1/authors', methods=['GET', 'POST])
def get_authors():   
     conn = psycopg2.connect(user='postgres',
                             password='cantwinkatyou',
                             host='127.0.0.1',
                             port='5432',
                             database='bookstore')  
    print("database connected successfully")
    cursor = conn.cursor()
    table_select_query = "select * from authors"
    cursor.execute(table_select_query)
    print("retrieving values from the authors table")
    authors_records = cursor.fetchall() 
    authors=[]  
    for row in authors_records:  
      a_dict = {}
      a_dict['ID'] = row[0]
      a_dict['name'] = row[1] 
      a_dict['country'] = row[2]
      a_dict['gender'] =row[3]    
      a_dict['book'] = row[4]   
      authors.append(a_dict)
    conn.close()
    return jsonify({'authors_list' : authors}), 200     



