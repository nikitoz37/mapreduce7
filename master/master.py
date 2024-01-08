
from flask import Flask
from flask import request, render_template, redirect, url_for, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import insert
#import psycopg2

from os import environ



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)

'''app = Flask(__name__)
conn = psycopg2.connect(
            dbname=environ.get('DB_NAME'),
            user=environ.get('USER'), 
            password=environ.get('PASSWORD'), 
            host=environ.get('HOST')
        )
cursor = conn.cursor()

query1 = 'CREATE TABLE IF NOT EXISTS "Top_words" ("id" serial NOT NULL PRIMARY KEY, "name" varchar NOT NUll UNIQUE, "num" integer);'
cursor.execute(query1)

cursor.close()
conn.close()'''



class Word(db.Model):
    __tablename__ = 'top_words'

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(30), unique=True, nullable=False)
    num = db.Column(db.Integer, nullable=False)

    def __init__(self, word, num):
        self.word = word
        self.num = num
    
    def json(self):
        return {'id': self.id,'word': self.word, 'email': self.num}


with app.app_context():
    db.create_all()



@app.route('/test', methods=['GET'])
def test():
  return make_response(jsonify({'message': 'test route'}), 200)


# create a user
'''@app.route('/users', methods=['POST'])
def create_user():
  try:
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return make_response(jsonify({'message': 'user created'}), 201)
  except e:
    return make_response(jsonify({'message': 'error creating user'}), 500)'''


'''@app.route('/', methods=['GET'])
def index():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['text']
    post = Post(text)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('index'))'''



'''@app.route('/test', methods=['GET'])
def test():
  return make_response(jsonify({'message': 'test route'}), 200)'''

'''
@app.route('/add', methods=['GET'])
def data_to_db():
    try:
        conn = psycopg2.connect(
            dbname=environ.get('DB_NAME'),
            user=environ.get('USER'), 
            password=environ.get('PASSWORD'), 
            host=environ.get('HOST')
        )
    except:
        print('Не возможно установить соединение')


    with conn.cursor as cursor:
        conn.autocommit = True
        
        query1 = "CREATE DATABASE metanit"
        cursor.execute(query1)

        query2 = "CREATE TABLE people (id SERIAL PRIMARY KEY, name VARCHAR(50),  age INTEGER)"
        cursor.execute(query2)
        
        all_users = cursor.fetchall()
'''

'''
@app.route('/add', methods=['GET'])
def add():
    stmt = insert(my_table).values(user_email='a@b.com', data='inserted data')
    stmt = stmt.on_conflict_do_update(
    index_elements=[my_table.c.user_email],
    index_where=my_table.c.user_email.like('%@gmail.com'),
    set_=dict(data=stmt.excluded.data)
)
conn.execute(stmt)
'''

@app.route('/add', methods=['GET'])
def add():
    new_word = 'город'
    new_num = 5

    '''stmt = insert('top_words').values(word=new_word, num=new_num)
    stmt = stmt.on_conflict_do_update(
        index_elements=['word'],
        #index_elements=['num'],
        #index_where=my_table.c.user_email.like('%@gmail.com'),
        set_=dict(num=new_num)
        )'''
    
    stmt = insert(Word).values(
        word=new_word,
        num=new_num)
    on_update_stmt = stmt.on_conflict_do_update(
        index_elements=[Word.word],
        set_=dict(num=Word.num + new_num)
        )
   

    '''
        word_ = Word(word=new_word)



        # Use on_conflict_do_update() to handle conflicts
        stmt = word_.__table__.insert().values(word=new_word)
        stmt = stmt.on_conflict_do_update(
            index_elements=['word'],
            set_=dict(num += new_word)
        )
    '''
    db.session.execute(stmt)
    db.session.commit()


@app.route('/', methods=['GET'])
def index():
    return 'Im master'





