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
    query_animals = "SELECT animal_id, type, sex, name, age, weight, temperament, last_name FROM Animals INNER JOIN Zookeepers ON Animals.zookeeper_id = Zookeepers.zookeeper_id ORDER BY animal_id ASC;"
    result_animals = execute_query(db_connection, query_animals).fetchall()
    # print(result_animals)

    query_medications = "SELECT med_id, name FROM Medications;"
    result_medications = execute_query(db_connection, query_medications).fetchall()
    # print(result_medications)

    query_animals_meds = "SELECT id, Animals.name, Medications.name FROM Animals_Medications INNER JOIN Animals ON Animals_Medications.animal_id = Animals.animal_id INNER JOIN Medications ON Animals_Medications.med_id = Medications.med_id;"
    result_animals_meds = execute_query(db_connection, query_animals_meds).fetchall()
    # print(result_animals_meds)

    query_zookeepers = "SELECT zookeeper_id, first_name, last_name FROM Zookeepers;"
    result_zookeepers = execute_query(db_connection, query_zookeepers).fetchall()

    return render_template('animals.html',
                           rows_animals=result_animals,
                           rows_medications=result_medications,
                           rows_animals_meds=result_animals_meds,
                           rows_zookeepers=result_zookeepers)


@webapp.route('/update_animal', methods=['POST'])
def update_animal():
    db_connection = connect_to_database()
    if request.method == 'POST':
        animal_id = request.form['animal_id']
        type = request.form['type']
        sex = request.form['sex']
        name = request.form['name']
        age = request.form['age']
        weight = request.form['weight']
        temperament = request.form['temperament']
        zookeeper_id = request.form['zookeeper_id']

        query = "UPDATE Animals SET type = %s, sex = %s, name = %s, age = %s, weight = %s, temperament = %s, zookeeper_id = %s WHERE animal_id = %s;"
        data = (type, sex, name, age, weight, temperament, zookeeper_id, animal_id)
        result = execute_query(db_connection, query, data)

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

        flash("Animal added successfully!")
        return redirect('/animals')

@webapp.route('/delete_animal', methods=['POST'])
def delete_animal():
    db_connection = connect_to_database()
    animal_id = request.form['animal_id']
    delete_query = "DELETE FROM Animals WHERE animal_id = %s;" % animal_id
    execute_query(db_connection, delete_query)

    flash('Animal deleted successfully!', 'success')
    return redirect('/animals')

@webapp.route('/add_medication', methods=['POST', 'GET'])
def add_medication():
    db_connection = connect_to_database()
    if request.method == 'POST':
        med_id = 'DEFAULT'
        name = request.form['name']

        query = 'INSERT INTO Medications (med_id, name) VALUES (%s, %s)'
        data = (med_id, name)
        execute_query(db_connection, query, data)

        flash("Medication added successfully!")
        return redirect('/animals')

# @webapp.route('/update_medication', methods=['POST'])
# def update_medication():
#     db_connection = connect_to_database()
#     if request.method == 'POST'
#         med_id = Medications.query.filter_by(id=request.form['id']).first()
#         name = request.form['name']
#
#         query = 'UPDATE Medications SET name = %s WHERE med_id = %s;'
#         data = (med_id, name)
#         execute_query(db_connection, query, data)
#
#         flash("Medication updated successfully!")
#         return redirect('/animals')


@webapp.route('/delete_medication', methods=['POST'])
def delete_medication():
    db_connection = connect_to_database()
    med_id = request.form['med_id']
    delete_query = "DELETE FROM Medications WHERE med_id = %s;" % med_id
    execute_query(db_connection, delete_query)

    flash('Medication deleted successfully!', 'success')
    return redirect('/animals')

@webapp.route('/add_animal_medication', methods=['POST', 'GET'])
def add_animal_medication():
    db_connection = connect_to_database()
    if request.method == 'POST':
        id = 'DEFAULT'
        animal_id = request.form['animal_id']
        med_id = request.form['med_id']

        query = 'INSERT INTO Animals_Medications (id, animal_id, med_id) VALUES (%s, %s, %s)'
        data = (id, animal_id, med_id)
        execute_query(db_connection, query, data)

        flash("Animal medication added successfully!")
        return redirect('/animals')

@webapp.route('/delete_animal_medication', methods=['POST'])
def delete_animal_medication():
    db_connection = connect_to_database()
    id = request.form['id']
    delete_query = "DELETE FROM Animals_Medications WHERE id = %s;" % id
    execute_query(db_connection, delete_query)

    flash("Animal's medication deleted successfully!", 'success')
    return redirect('/animals')

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

    query_zookeepers_workdays = "SELECT Zookeepers_Workdays.zookeeper_id, first_name, last_name, Zookeepers_Workdays.workday_id, day, id FROM Zookeepers_Workdays INNER JOIN Zookeepers ON Zookeepers_Workdays.zookeeper_id = Zookeepers.zookeeper_id INNER JOIN Workdays ON Zookeepers_Workdays.workday_id = Workdays.workday_id ORDER BY Zookeepers_Workdays.workday_id, Zookeepers.last_name ASC;"
    result_zookeepers_workdays = execute_query(db_connection, query_zookeepers_workdays).fetchall()
    # print(result_zookeepers_workdays)

    return render_template('zookeepers.html',
                           rows_zookeepers=result_zookeepers,
                           rows_workdays=result_workdays,
                           rows_zookeepers_workdays=result_zookeepers_workdays)


@webapp.route('/add_zookeeper', methods=['POST'])
def add_zookeeper():
    db_connection = connect_to_database()
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        query = 'INSERT INTO Zookeepers (first_name, last_name) VALUES (%s, %s)'
        data = (first_name, last_name)
        execute_query(db_connection, query, data)

        flash("Zookeeper added successfully!")
        return redirect('/zookeepers')

@webapp.route('/delete_zookeeper', methods=['POST'])
def delete_zookeeper():
    db_connection = connect_to_database()
    zookeeper_id = request.form['zookeeper_id']
    delete_query = "DELETE FROM Zookeepers WHERE zookeeper_id = %s;" % zookeeper_id
    execute_query(db_connection, delete_query)

    flash("Zookeeper deleted successfully!", 'success')
    return redirect('/zookeepers')

@webapp.route('/add_zookeeper_workday', methods=['POST'])
def add_zookeeper_workday():
    db_connection = connect_to_database()
    if request.method == 'POST':
        zookeeper_id = request.form['zookeeper_id']
        workday_id = request.form['workday_id']

        query = 'INSERT INTO Zookeepers_Workdays (zookeeper_id, workday_id) VALUES (%s, %s)'

        data = (zookeeper_id, workday_id)
        execute_query(db_connection, query, data)

        flash("Zookeeper Workday added successfully!")
        return redirect('/zookeepers')

@webapp.route('/delete_zookeeper_workday', methods=['POST'])
def delete_zookeeper_workday():
    db_connection = connect_to_database()
    id = request.form['id']
    delete_query = "DELETE FROM Zookeepers_Workdays WHERE id = %s;" % id
    execute_query(db_connection, delete_query)

    flash("Zookeeper workday deleted successfully!", 'success')
    return redirect('/zookeepers')

@webapp.route('/search', methods=['POST'])
def search_Animals():
    db_connection = connect_to_database()
    if request.method == 'POST':
        searchString = request.form['searchString']
#         print(searchString)

        search_query = "SELECT animal_id, type, sex, name, age, weight, temperament, last_name FROM Animals INNER JOIN Zookeepers ON Animals.zookeeper_id = Zookeepers.zookeeper_id WHERE animal_id LIKE %s OR type LIKE %s OR sex LIKE %s OR name LIKE %s OR age LIKE %s OR weight LIKE %s OR temperament LIKE %s OR last_name LIKE %s;"
        data = ([searchString], [searchString], [searchString], [searchString], [searchString], [searchString], [searchString], [searchString], )
        result_search = execute_query(db_connection, search_query, data).fetchall()
#         print (result_search)

        query_medications = "SELECT med_id, name FROM Medications;"
        result_medications = execute_query(db_connection, query_medications).fetchall()
#         print(result_medications)

        query_animals_meds = "SELECT id, Animals.name, Medications.name FROM Animals_Medications INNER JOIN Animals ON Animals_Medications.animal_id = Animals.animal_id INNER JOIN Medications ON Animals_Medications.med_id = Medications.med_id;"
        result_animals_meds = execute_query(db_connection, query_animals_meds).fetchall()
#         print(result_animals_meds)

        query_zookeepers = "SELECT zookeeper_id, first_name, last_name FROM Zookeepers;"
        result_zookeepers = execute_query(db_connection, query_zookeepers).fetchall()
#         print(result_zookeepers)

        if not result_search:
            flash("No results found!")
            return redirect('/animals')

        return render_template('animals.html',
                               rows_animals=result_search,
                               rows_medications=result_medications,
                               rows_animals_meds=result_animals_meds,
                               rows_zookeepers=result_zookeepers)


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
    return render_template('home.html', result=result)


@webapp.route('/db_test')
def test_database_connection():
    print("Executing a sample query on the database using the credentials from db_credentials.py")
    db_connection = connect_to_database()
    query = "SELECT * from bsg_people;"
    result = execute_query(db_connection, query)
    return render_template('db_test.html', rows=result)
