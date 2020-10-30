from flask import Flask, render_template
from flask import request, redirect
from db_connector.db_connector import connect_to_database, execute_query
#create the web application
webapp = Flask(__name__)


@webapp.route('/')
def index():
    return render_template('index.html')


@webapp.route('/animals')
def animals():
    print("Fetching and rendering Animals web page")
    db_connection = connect_to_database()
    query_animals = "SELECT animal_id, type, sex, name, age, weight, temperament, zookeeper_id FROM Animals;"
    result_animals = execute_query(db_connection, query_animals).fetchall()
    print(result_animals)

    query_medications = "SELECT med_id, name FROM Medications;"
    result_medications = execute_query(db_connection, query_medications).fetchall()
    print(result_medications)
    return render_template('animals.html', rows_animals=result_animals, rows_medications=result_medications)


@webapp.route('/add_new_animals', methods=['POST','GET'])
def add_new_animals():
    db_connection = connect_to_database()
    if request.method == 'GET':
        query = 'SELECT animal_id, name from Animals'
        result = execute_query(db_connection, query).fetchall()
        print(result)

        return render_template('animals_add_new.html') # see people e.g.
    elif request.method == 'POST':
        print("Add new animal!")
        type = request.form['type']
        sex = request.form['sex']
        name = request.form['name']
        age = request.form['age']
        weight = request.form['weight']
        temperament = request.form['temperament']

        query = 'INSERT INTO Animals (type, sex, name, age, weight, temperament) VALUES (%s,%s,%s,%s,%s,%s)'
        data = (type, sex, name, age, weight, temperament)
        execute_query(db_connection, query, data)
        return ('Animal added!')

# NOTE: this code isn't needed anymore since medications is on animals page
# @webapp.route('/browse_Medications')
# #the name of this function is just a cosmetic thing
# def browse_Medications():
#     print("Fetching and rendering Medications web page")
#     db_connection = connect_to_database()
#     query = "SELECT med_id, name FROM Medications;"
#     result = execute_query(db_connection, query).fetchall()
#     print(result)
#     return render_template('Medications_browse.html', rows=result)

# @webapp.route('/')
# def index():
#     return "<p>Are you looking for /db_test or /hello or <a href='/browse_bsg_people'>/browse_bsg_people</a> or /add_new_people or /update_people/id or /delete_people/id </p>"


@webapp.route('/browse_bsg_people')
#the name of this function is just a cosmetic thing
def browse_people():
    print("Fetching and rendering people web page")
    db_connection = connect_to_database()
    query = "SELECT fname, lname, homeworld, age, id from bsg_people;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('people_browse.html', rows=result)


@webapp.route('/add_new_people', methods=['POST','GET'])
def add_new_people():
    db_connection = connect_to_database()
    if request.method == 'GET':
        query = 'SELECT id, name from bsg_planets'
        result = execute_query(db_connection, query).fetchall()
        print(result)

        return render_template('people_add_new.html', planets = result)
    elif request.method == 'POST':
        print("Add new people!")
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        homeworld = request.form['homeworld']

        query = 'INSERT INTO bsg_people (fname, lname, age, homeworld) VALUES (%s,%s,%s,%s)'
        data = (fname, lname, age, homeworld)
        execute_query(db_connection, query, data)
        return ('Person added!')


@webapp.route('/home')
def home():
    db_connection = connect_to_database()
    query = "DROP TABLE IF EXISTS diagnostic;"
    execute_query(db_connection, query)
    query = "CREATE TABLE diagnostic(id INT PRIMARY KEY, text VARCHAR(255) NOT NULL);"
    execute_query(db_connection, query)
    query = "INSERT INTO diagnostic (text) VALUES ('MySQL is working');"
    execute_query(db_connection, query)
    query = "SELECT * from diagnostic;"
    result = execute_query(db_connection, query)
    for r in result:
        print(f"{r[0]}, {r[1]}")
    return render_template('home.html', result = result)

@webapp.route('/db_test')
def test_database_connection():
    print("Executing a sample query on the database using the credentials from db_credentials.py")
    db_connection = connect_to_database()
    query = "SELECT * from bsg_people;"
    result = execute_query(db_connection, query)
    return render_template('db_test.html', rows=result)

#display update form and process any updates, using the same function
@webapp.route('/update_people/<int:id>', methods=['POST','GET'])
def update_people(id):
    print('In the function')
    db_connection = connect_to_database()
    #display existing data
    if request.method == 'GET':
        print('The GET request')
        people_query = 'SELECT id, fname, lname, homeworld, age from bsg_people WHERE id = %s'  % (id)
        people_result = execute_query(db_connection, people_query).fetchone()

        if people_result == None:
            return "No such person found!"

        planets_query = 'SELECT id, name from bsg_planets'
        planets_results = execute_query(db_connection, planets_query).fetchall()

        print('Returning')
        return render_template('people_update.html', planets = planets_results, person = people_result)
    elif request.method == 'POST':
        print('The POST request')
        character_id = request.form['character_id']
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        homeworld = request.form['homeworld']

        query = "UPDATE bsg_people SET fname = %s, lname = %s, age = %s, homeworld = %s WHERE id = %s"
        data = (fname, lname, age, homeworld, character_id)
        result = execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated")

        return redirect('/browse_bsg_people')

@webapp.route('/delete_people/<int:id>')
def delete_people(id):
    '''deletes a person with the given id'''
    db_connection = connect_to_database()
    query = "DELETE FROM bsg_people WHERE id = %s"
    data = (id,)

    result = execute_query(db_connection, query, data)
    return (str(result.rowcount) + "row deleted")
