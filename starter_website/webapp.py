from flask import Flask, render_template
from flask import request, redirect, flash, jsonify, json
from db_connector.db_connector import connect_to_database, execute_query
# create the web application
webapp = Flask(__name__)
webapp.secret_key = "Super Secret Key That You Can't Guess"


@webapp.route('/')
def index():
    return render_template('index.html')


# ANIMALS
@webapp.route('/animals')
def animals():
    db_connection = connect_to_database()

    # Animals
    query_animals = "SELECT animal_id, type, sex, name, age, weight, temperament, last_name FROM Animals " \
                    "LEFT JOIN Zookeepers ON Animals.zookeeper_id = Zookeepers.zookeeper_id " \
                    "ORDER BY animal_id ASC;"

    result_animals = execute_query(db_connection, query_animals).fetchall()

    # Medications
    query_medications = "SELECT med_id, name FROM Medications;"
    result_medications = execute_query(db_connection, query_medications).fetchall()

    # Animals_Medications
    query_animals_medications = "SELECT id, Animals_Medications.animal_id, Animals_Medications.med_id " \
                                "FROM Animals_Medications " \
                                "INNER JOIN Animals ON Animals_Medications.animal_id = Animals.animal_id " \
                                "INNER JOIN Medications ON Animals_Medications.med_id = Medications.med_id;"

    result_animals_medications = execute_query(db_connection, query_animals_medications).fetchall()

    # Zookeepers - for Animals table
    query_zookeepers = "SELECT zookeeper_id, first_name, last_name FROM Zookeepers;"
    result_zookeepers = execute_query(db_connection, query_zookeepers).fetchall()

    return render_template('animals.html',
                           rows_animals=result_animals,
                           rows_medications=result_medications,
                           rows_animals_medications=result_animals_medications,
                           rows_zookeepers=result_zookeepers,
                           json_zookeepers=json.dumps(result_zookeepers))


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

        if zookeeper_id == 'NULL':
            zookeeper_id = None

        query = "UPDATE Animals " \
                "SET type = %s, sex = %s, name = %s, age = %s, weight = %s, temperament = %s, zookeeper_id = %s " \
                "WHERE animal_id = %s;"

        data = (type, sex, name, age, weight, temperament, zookeeper_id, animal_id)

        try:
            result = execute_query(db_connection, query, data)

            if result is None:
                flash("Could not update animal!", 'error')
            else:
                flash(f"{result.rowcount} Animal(s) updated", 'success')
        except Exception as e:
            try:
                error = str(e).split(',')[1].replace('\\', '').replace(')', '').replace('"', '')
            except:
                error = "no duplicate or NULL entries!"

            flash(f"Animal not updated - {error}", 'error')

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

        if zookeeper_id == 'NULL':
            zookeeper_id = None

        query = "INSERT INTO Animals (type, sex, name, age, weight, temperament, zookeeper_id) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s);"

        data = (type, sex, name, age, weight, temperament, zookeeper_id)

        try:
            execute_query(db_connection, query, data)
            flash('Animal added successfully!', "success")
        except Exception as e:
            try:
                error = str(e).split(',')[1].replace('\\', '').replace(')', '').replace('"', '')
            except:
                error = "no duplicate or NULL entries!"

            flash(f"Animal not added - {error}", 'error')

        return redirect('/animals')


@webapp.route('/delete_animal', methods=['POST'])
def delete_animal():
    db_connection = connect_to_database()
    animal_id = request.form['animal_id']
    delete_query = "DELETE FROM Animals WHERE animal_id = %s;" % animal_id
    execute_query(db_connection, delete_query)

    flash('Animal deleted successfully!', 'success')
    return redirect('/animals')


# MEDICATIONS
@webapp.route('/add_medication', methods=['POST', 'GET'])
def add_medication():
    db_connection = connect_to_database()
    if request.method == 'POST':
        med_id = 'DEFAULT'
        name = request.form['name']

        query = "INSERT INTO Medications (med_id, name) VALUES (%s, %s);"
        data = (med_id, name)

        try:
            execute_query(db_connection, query, data)
            flash('Medication added successfully!', 'success')
        except Exception as e:
            try:
                error = str(e).split(',')[1].replace('\\', '').replace(')', '').replace('"', '')
            except:
                error = "no duplicate or NULL entries!"

            flash(f"Medication not added - {error}", 'error')

        return redirect('/animals')


@webapp.route('/update_medications', methods=['POST'])
def update_medications():
    db_connection = connect_to_database()
    if request.method == 'POST':
        med_id = request.form["med_id"]
        name = request.form['name']

        query = "UPDATE Medications SET name = %s WHERE med_id = %s;"
        data = (name, med_id)

        try:
            result = execute_query(db_connection, query, data)

            if result is None:
                flash('Could not update medication!', 'error')
            else:
                flash(f"{result.rowcount} Medication(s) updated", 'success')
        except Exception as e:
            try:
                error = str(e).split(',')[1].replace('\\', '').replace(')', '').replace('"', '')
            except:
                error = "no duplicate or NULL entries!"

            flash(f"Medication not updated - {error}", 'error')

        return redirect('/animals')


@webapp.route('/delete_medication', methods=['POST'])
def delete_medication():
    db_connection = connect_to_database()
    med_id = request.form['med_id']
    delete_query = "DELETE FROM Medications WHERE med_id = %s;" % med_id
    execute_query(db_connection, delete_query)

    flash('Medication deleted successfully!', 'success')
    return redirect('/animals')


# ANIMALS MEDICATIONS
@webapp.route('/add_animal_medication', methods=['POST', 'GET'])
def add_animal_medication():
    db_connection = connect_to_database()
    if request.method == 'POST':
        id = 'DEFAULT'
        animal_id = request.form['animal_id']
        med_id = request.form['med_id']

        query = "INSERT INTO Animals_Medications (id, animal_id, med_id) VALUES (%s, %s, %s);"
        data = (id, animal_id, med_id)

        try:
            execute_query(db_connection, query, data)
            flash('Animal Medication added successfully!', 'success')
        except Exception as e:
            try:
                error = str(e).split(',')[1].replace('\\', '').replace(')', '').replace('"', '')
            except:
                error = "no duplicate or NULL entries!"

            flash(f"Animal Medication not added - {error}", 'error')

        return redirect('/animals')


@webapp.route('/update_animals_medications', methods=['POST'])
def update_animals_medications():
    db_connection = connect_to_database()
    if request.method == 'POST':
        id = request.form["id"]
        animal_id = request.form["animal_id"]
        med_id = request.form["med_id"]

        query = "UPDATE Animals_Medications SET animal_id = %s, med_id = %s WHERE id = %s;"
        data = (animal_id, med_id, id)

        try:
            result = execute_query(db_connection, query, data)

            if result is None:
                flash("Could not update animal's medications!", 'error')
            else:
                flash(f"{result.rowcount} Animals Medications updated", "success")
        except Exception as e:
            try:
                error = str(e).split(',')[1].replace('\\', '').replace(')', '').replace('"', '')
            except:
                error = "no duplicate or NULL entries!"

            flash(f"Animals Medications not updated - {error}", 'error')

        return redirect('/animals')


@webapp.route('/delete_animal_medication', methods=['POST'])
def delete_animal_medication():
    db_connection = connect_to_database()
    id = request.form['id']
    delete_query = "DELETE FROM Animals_Medications WHERE id = %s;" % id
    execute_query(db_connection, delete_query)

    flash("Animal's medication deleted successfully!", 'success')
    return redirect('/animals')


# ZOOKEEPERS
@webapp.route('/zookeepers')
def zookeepers():
    db_connection = connect_to_database()

    # Zookeepers
    query_zookeepers = "SELECT zookeeper_id, first_name, last_name FROM Zookeepers;"
    result_zookeepers = execute_query(db_connection, query_zookeepers).fetchall()

    # Workdays
    query_workdays = "SELECT workday_id, day FROM Workdays;"
    result_workdays = execute_query(db_connection, query_workdays).fetchall()

    # Zookeepers_Workdays
    query_zookeepers_workdays = "SELECT Zookeepers_Workdays.zookeeper_id, first_name, last_name, " \
                                "Zookeepers_Workdays.workday_id, day, id " \
                                "FROM Zookeepers_Workdays " \
                                "INNER JOIN Zookeepers ON Zookeepers_Workdays.zookeeper_id = Zookeepers.zookeeper_id " \
                                "INNER JOIN Workdays ON Zookeepers_Workdays.workday_id = Workdays.workday_id " \
                                "ORDER BY Zookeepers_Workdays.workday_id, Zookeepers.last_name ASC;"

    result_zookeepers_workdays = execute_query(db_connection, query_zookeepers_workdays).fetchall()

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

        query = "INSERT INTO Zookeepers (first_name, last_name) VALUES (%s, %s);"
        data = (first_name, last_name)

        try:
            execute_query(db_connection, query, data)
            flash("Zookeeper added successfully!", 'success')
        except Exception as e:
            try:
                error = str(e).split(',')[1].replace('\\', '').replace(')', '').replace('"', '')
            except:
                error = "no duplicate or NULL entries!"

            flash(f"Zookeeper not added - {error}", 'error')

        return redirect('/zookeepers')


@webapp.route('/update_zookeepers', methods=['POST'])
def update_zookeepers():
    db_connection = connect_to_database()
    if request.method == 'POST':
        zookeeper_id = request.form['zookeeper_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        query = "UPDATE Zookeepers SET first_name = %s, last_name = %s WHERE zookeeper_id = %s;"
        data = (first_name, last_name, zookeeper_id)

        try:
            result = execute_query(db_connection, query, data)
            if result is None:
                flash("Could not update zookeeper!", 'error')
            else:
                flash(f"{result.rowcount} Zookeeper(s) updated", 'success')
        except Exception as e:
            try:
                error = str(e).split(',')[1].replace('\\', '').replace(')', '').replace('"', '')
            except:
                error = "no duplicate or NULL entries!"

            flash(f"Zookeeper not updated - {error}", 'error')

        return redirect('/zookeepers')


@webapp.route('/delete_zookeeper', methods=['POST'])
def delete_zookeeper():
    db_connection = connect_to_database()
    zookeeper_id = request.form['zookeeper_id']
    delete_query = "DELETE FROM Zookeepers WHERE zookeeper_id = %s;" % zookeeper_id
    execute_query(db_connection, delete_query)

    flash("Zookeeper deleted successfully!", 'success')
    return redirect('/zookeepers')


# ZOOKEEPERS WORKDAYS
@webapp.route('/add_zookeeper_workday', methods=['POST'])
def add_zookeeper_workday():
    db_connection = connect_to_database()
    if request.method == 'POST':
        zookeeper_id = request.form['zookeeper_id']
        workday_id = request.form['workday_id']

        query = "INSERT INTO Zookeepers_Workdays (zookeeper_id, workday_id) VALUES (%s, %s);"
        data = (zookeeper_id, workday_id)

        try:
            execute_query(db_connection, query, data)
            flash("Zookeeper Workday added successfully!", 'success')

        except Exception as e:
            try:
                error = str(e).split(',')[1].replace('\\', '').replace(')', '').replace('"', '')
            except:
                error = "no duplicate or NULL entries!"

            flash(f"Zookeeper Workday not added - {error}", 'error')

        return redirect('/zookeepers')


@webapp.route('/update_zookeepers_workdays', methods=['POST'])
def update_zookeepers_workdays():
    db_connection = connect_to_database()
    if request.method == 'POST':
        id = request.form['id']
        zookeeper_id = request.form['zookeeper_id']
        workday_id = request.form['workday_id']

        query = "UPDATE Zookeepers_Workdays SET zookeeper_id = %s, workday_id = %s WHERE id = %s;"
        data = (zookeeper_id, workday_id, id)

        try:
            result = execute_query(db_connection, query, data)

            if result is None:
                flash("Could not update Zookeepers Workdays", 'error')
            else:
                flash(f"{result.rowcount} Zookeepers Workdays updated", 'success')

        except Exception as e:
            try:
                error = str(e).split(',')[1].replace('\\', '').replace(')', '').replace('"', '')
            except:
                error = "no duplicate or NULL entries!"

            flash(f"Zookeepers Workdays not updated - {error}", 'error')

        return redirect('/zookeepers')


@webapp.route('/delete_zookeeper_workday', methods=['POST'])
def delete_zookeeper_workday():
    db_connection = connect_to_database()
    id = request.form['id']
    delete_query = "DELETE FROM Zookeepers_Workdays WHERE id = %s;" % id
    execute_query(db_connection, delete_query)

    flash("Zookeeper workday deleted successfully!", 'success')
    return redirect('/zookeepers')


# WORKDAYS
@webapp.route('/add_workday', methods=['POST', 'GET'])
def add_workday():
    db_connection = connect_to_database()
    if request.method == 'POST':
        workday_id = 'DEFAULT'
        workday_name = request.form['workday_name']

        query = "INSERT INTO Workdays (workday_id, day) VALUES (%s, %s);"
        data = (workday_id, workday_name)

        try:
            execute_query(db_connection, query, data)
            flash('Workday added successfully!', 'success')

        except Exception as e:
            try:
                error = str(e).split(',')[1].replace('\\', '').replace(')', '').replace('"', '')
            except:
                error = "no duplicate or NULL entries!"

            flash(f"Workday not added - {error}", 'error')

        return redirect('/zookeepers')


@webapp.route('/update_workdays', methods=['POST'])
def update_workdays():
    db_connection = connect_to_database()
    if request.method == 'POST':
        workday_id = request.form["workday_id"]
        workday_name = request.form['workday_name']

        query = "UPDATE Workdays SET day = %s WHERE workday_id = %s;"
        data = (workday_name, workday_id)

        try:
            result = execute_query(db_connection, query, data)

            if result is None:
                flash('Could not update Workday!', 'error')
            else:
                flash(f"{result.rowcount} Workday(s) updated", 'success')

        except Exception as e:
            try:
                error = str(e).split(',')[1].replace('\\', '').replace(')', '').replace('"', '')
            except:
                error = "no duplicate or NULL entries!"

            flash(f"Workdays not updated - {error}", 'error')

        return redirect('/zookeepers')


@webapp.route('/delete_workday', methods=['POST'])
def delete_workday():
    db_connection = connect_to_database()
    workday_id = request.form['workday_id']
    delete_query = "DELETE FROM Workdays WHERE workday_id = %s;" % workday_id
    execute_query(db_connection, delete_query)

    flash('Workday deleted successfully!', 'success')
    return redirect('/zookeepers')


# SEARCH
# Dynamic search with JavaScript
@webapp.route('/search_animals')
def search_animals():
    db_connection = connect_to_database()
    search_string = "%" + request.args.get("search") + "%"
    search_query = "SELECT animal_id, type, sex, name, age, weight, temperament, last_name FROM Animals " \
                   "LEFT JOIN Zookeepers ON Animals.zookeeper_id = Zookeepers.zookeeper_id " \
                   "WHERE animal_id LIKE %s OR type LIKE %s OR sex LIKE %s OR name LIKE %s " \
                   "OR age LIKE %s OR weight LIKE %s OR temperament LIKE %s OR IFNULL(last_name, 'NULL') LIKE %s;"
    data = (
        [search_string], [search_string], [search_string], [search_string],
        [search_string], [search_string], [search_string], [search_string],
    )

    if search_string:
        search_results = execute_query(db_connection, search_query, data).fetchall()

    return jsonify(search_results)


# Search with buttons, reload page
@webapp.route('/search', methods=['POST'])
def search_Animals():
    db_connection = connect_to_database()
    if request.method == 'POST':
        searchString = "%" + request.form['searchString'] + "%"

        search_query = "SELECT animal_id, type, sex, name, age, weight, temperament, last_name FROM Animals " \
                       "LEFT JOIN Zookeepers ON Animals.zookeeper_id = Zookeepers.zookeeper_id " \
                       "WHERE animal_id LIKE %s OR type LIKE %s OR sex LIKE %s OR name LIKE %s " \
                       "OR age LIKE %s OR weight LIKE %s OR temperament LIKE %s OR IFNULL(last_name, 'NULL') LIKE %s;"

        data = ([searchString], [searchString], [searchString], [searchString], [searchString], [searchString], [searchString], [searchString], )
        result_search = execute_query(db_connection, search_query, data).fetchall()

        query_medications = "SELECT med_id, name FROM Medications;"
        result_medications = execute_query(db_connection, query_medications).fetchall()

        query_animals_medications = "SELECT id, Animals.name, Medications.name FROM Animals_Medications " \
                                    "INNER JOIN Animals ON Animals_Medications.animal_id = Animals.animal_id " \
                                    "INNER JOIN Medications ON Animals_Medications.med_id = Medications.med_id;"

        result_animals_medications = execute_query(db_connection, query_animals_medications).fetchall()

        query_zookeepers = "SELECT zookeeper_id, first_name, last_name FROM Zookeepers;"
        result_zookeepers = execute_query(db_connection, query_zookeepers).fetchall()

        if not result_search:
            flash("Error: No results found!", 'error')
            return redirect('/animals')

        return render_template('animals.html',
                               rows_animals=result_search,
                               rows_medications=result_medications,
                               rows_animals_medications=result_animals_medications,
                               rows_zookeepers=result_zookeepers)
