from flask import Flask, render_template
from flask import request, redirect, flash, jsonify
from db_connector.db_connector import connect_to_database, execute_query
# create the web application
webapp = Flask(__name__)
webapp.secret_key = "Secret Key"


@webapp.route('/')
def index():
    return render_template('index.html')


@webapp.route('/animals')
def animals():
    print("Fetching and rendering Animals web page")
    db_connection = connect_to_database()
    query_animals = "SELECT animal_id, type, sex, name, age, weight, temperament, zookeeper_id FROM Animals;"
    result_animals = execute_query(db_connection, query_animals).fetchall()
    # print(result_animals)

    query_medications = "SELECT med_id, name FROM Medications;"
    result_medications = execute_query(db_connection, query_medications).fetchall()
    # print(result_medications)

    query_animals_meds = "SELECT id, animal_id, med_id FROM Animals_Medications;"
    result_animals_meds = execute_query(db_connection, query_animals_meds).fetchall()
    # print(result_animals_meds)

    return render_template('animals.html', rows_animals=result_animals,
                           rows_medications=result_medications,
                           rows_animals_meds=result_animals_meds)


@webapp.route('/update_animal', methods=['POST', 'GET'])
def update_animal():
    db_connection = connect_to_database()
    if request.method == 'POST':
        print("Incoming post in update_animal")
        update_data = request.get_json()
        animal_id = update_data['animal_id']
        type = update_data['type']
        sex = update_data['sex']
        name = update_data['name']
        age = update_data['age']
        weight = update_data['weight']
        temperament = update_data['temperament']
        zookeeper_id = update_data['zookeeper_id']

        # Updating animal_id does not work
        query = "UPDATE Animals SET animal_id = %s, type = %s, sex = %s, name = %s, age = %s, weight = %s, temperament = %s, zookeeper_id = %s WHERE animal_id = %s;"
        data = (animal_id, type, sex, name, age, weight, temperament, zookeeper_id, animal_id)
        result = execute_query(db_connection, query, data)
        print("====================")
        print(str(result.rowcount) + " row(s) updated")

        # TODO: handle failed UPDATE and make flash message work
        flash("why doesn't flash work here?")
        if result is None:
            flash("Could not UPDATE")
        else:
            flash(f"{result.rowcount} row(s) updated")

        return redirect('/animals')


@webapp.route('/add_animal', methods=['POST', 'GET'])
def add_animal():
    db_connection = connect_to_database()
    if request.method == 'POST':
        type = request.form['type']
        sex = request.form['sex']
        name = request.form['name']
        age = request.form['age']
        weight = request.form['weight']
        temperament = request.form['temperament']
        zookeeper_id = request.form['zookeeper_id']

        query = 'INSERT INTO Animals (type, sex, name, age, weight, temperament, zookeeper_id) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        data = (type, sex, name, age, weight, temperament, zookeeper_id)
        execute_query(db_connection, query, data)

        flash("Animal added successfully")
        return redirect('/animals')

# -- Huber Revision Start --
# @webapp.route('/delete_animal', methods=['POST', 'GET'])
# def delete_animal():
#     db_connection = connect_to_database()
#     print("Incoming post in delete_animal")
#     update_data = request.get_json()
#     animal_id = update_data['animal_id']
#     query = "DELETE FROM Animals WHERE animal_id = %s"
#     data = (animal_id,)
#     result = execute_query(db_connection, query, data)
#     print(str(result.rowcount) + " row deleted")
#     flash(str(result.rowcount) + " row deleted")
#     return redirect('/animals')

@webapp.route('/delete_animal/<string:id>', methods=['POST'])
def delete_animal(id):
    db_connection = connect_to_database()
    print("Incoming post in delete_animal")
    query = "DELETE FROM Animals WHERE animal_id = %s"
    execute_query(db_connection, query, [id])

    flash('Animal Deleted', 'success')
    return redirect('/animals')
# -- Huber Revision End --

@webapp.route('/zookeepers')
def zookeepers():
    # print("Fetching and rendering Zookeepers web page")
    db_connection = connect_to_database()
    query_zookeepers = "SELECT zookeeper_id, first_name, last_name FROM Zookeepers;"
    result_zookeepers = execute_query(db_connection, query_zookeepers).fetchall()
    # print(result_zookeepers)

    query_workdays = "SELECT workday_id, day FROM Workdays;"
    result_workdays = execute_query(db_connection, query_workdays).fetchall()
    # print(result_workdays)

    query_zookeepers_workdays = "SELECT id, zookeeper_id, workday_id FROM Zookeepers_Workdays;"
    result_zookeepers_workdays = execute_query(db_connection, query_zookeepers_workdays).fetchall()
    # print(result_zookeepers_workdays)

    return render_template('zookeepers.html', rows_zookeepers=result_zookeepers,
                            rows_workdays=result_workdays,
                            rows_zookeepers_workdays=result_zookeepers_workdays)


@webapp.route('/browse_bsg_people')
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
