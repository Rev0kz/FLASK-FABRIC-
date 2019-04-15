from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:lablam@localhost:5432/novelstore'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)



class Authors(db.Model):
          
          name = db.Column(db.String(), unique=True, primary_key=True)
          book = db.Column(db.String(), unique=True)


          def __init__(self, name, book): 
		self.name = name
		self.book = book 
    
          

   	  def __repr__(self):   
		return "<Name: {}>".format(self.name)   


          def serialize(self):
		return {
            		'name':  self.name, 
            		'book' : self.book
           		}
    
    
@app.route('/authors', methods=['GET'])
def get_authors():
       
	if request.method == 'GET': 
		all_authors = Authors.query.all() 
		return jsonify([e.serialize() for e in all_authors])	



@app.route('/authors', methods=['POST'])
def create_author():
	if request.method == 'POST':
		name=request.args.get('name')
		book=request.args.get('book')  
		
	try:
        	author=Authors(
            	   name=name,
            	   book=book
                 )
        	db.session.add(author)
        	db.session.commit()
		return "Author added. author name={}".format(author.name) 
	except Exception as e:
		return(str(e))    


@app.route('/authors/<name>', methods=['PUT'])
def update():
	if request.method == 'PUT':
		author = Authors.query.get(name)
		name = request.json['name'] 
		book = request.json['book'] 
		

		author.name = name
		author.book = book 

                db.session.commit()
		return jsonify([e.serialize() for e in author])


@app.route('/authors/<name>', methods=['DELETE'])
def del_author():
    if request.method == 'DELETE':  
		author = Authors.query.get(name)
		db.session.delete(author)
		db.session.commit() 
		return "Author deleted. author name={}".format(author.name)


       
if __name__ == '__main__':  
	app.run(debug=True, port=5000)


 


    


   



