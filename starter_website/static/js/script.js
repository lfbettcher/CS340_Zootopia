// Listeners for buttons
const animalsTable = document.getElementById("animalsTable");
if (animalsTable) {
    animalsTable.addEventListener("click", (event) => {
        if (event.target.tagName !== "BUTTON")
            return;
        if (event.target.name === "Edit") {
            enableRow(event.target.parentNode.parentNode.id);
            toggleEditButton(event.target);
        }
        if (event.target.name === "Search")
            runSearch();
        if (event.target.name === "Delete")
            runDelete(event, 'Animals');
    });
}

const medicationsTable = document.getElementById("medicationsTable");
if (medicationsTable) {
    medicationsTable.addEventListener("click", (event) => {
        if (event.target.tagName !== "BUTTON") return;
        if (event.target.name === "Edit") {
            enableRow(event.target.parentNode.parentNode.id);
            toggleEditButton(event.target);
        }
        if (event.target.name === "Delete")
            runDelete(event, 'Medications');
    });
}

const animalsMedicationsTable = document.getElementById("animalsMedicationsTable");
if (animalsMedicationsTable) {
    animalsMedicationsTable.addEventListener("click", (event) => {
        if (event.target.tagName !== "BUTTON") return;
        if (event.target.name === "Edit") {
            enableRow(event.target.parentNode.parentNode.id);
            toggleEditButton(event.target);
        }
        if (event.target.name === "Delete")
            runDelete(event, 'Animals_Medications');
    });
}

const zookeepersTable = document.getElementById("zookeepersTable");
if (zookeepersTable) {
    zookeepersTable.addEventListener("click", (event) => {
        if (event.target.tagName !== "BUTTON") return;
        if (event.target.name === "Edit") {
            enableRow(event.target.parentNode.parentNode.id);
            toggleEditButton(event.target);
        }
        if (event.target.name === "Delete")
            runDelete(event, 'Zookeepers');
    });
}

const zookeepersWorkdaysTable = document.getElementById("zookeepersWorkdaysTable");
if (zookeepersWorkdaysTable) {
    zookeepersWorkdaysTable.addEventListener("click", (event) => {
        if (event.target == null || event.target.tagName !== "BUTTON") return;
        if (event.target.name === "Edit") {
            enableRow(event.target.parentNode.parentNode.id);
            toggleEditButton(event.target);
        }
        if (event.target.name === "Delete")
            runDelete(event, 'Zookeepers_Workdays');
    });
}

function toggleEditButton(button) {
    if (button.textContent === "Edit") {
        button.className = "update-btn hidden";
        button.previousElementSibling.className = "update-btn";
    }
};

function enableRow(rowID) {
    // enable inputs when edit button is clicked
    let tdList = Array.from(document.getElementById(rowID).children);
    tdList.forEach((td) => {
        let element = td.firstElementChild;
        if (element.tagName === "INPUT" || element.tagName === "SELECT") {
            element.disabled = false;
            element.className += " editable";
        }
    });
};

function disableRow(rowID) {
    // disable inputs when save button is clicked
    let tdList = Array.from(document.getElementById(rowID).children);
    tdList.forEach((td) => {
        if (td.firstChild.tagName === "INPUT") {
            td.firstChild.disabled = true;
        }
    });
};

function disableAllInput() {
    // disable inputs in table until update button is clicked
    document.querySelectorAll("tbody input").forEach((input) => {
        input.disabled = true;
    });
};

// function gets string data from search bar, creates object, and posts to path shown
function runSearch() {
    var searchString = document.getElementById("search_inputs");
    var searchedString = searchString.value;
    var searchObject = {
        searchString: searchedString
    };
    post(`/search`, searchObject);
}

/**
 * @param {event} clicked event (used to get value of row)
 * @param {string} tableName is name of table to delete from (used for path url)
 */
function runDelete(event, tableName) {
    var entityID = event.target.value;
    if (tableName === 'Animals') {
        var animalObject = {
            animal_id: entityID
        };
        post('/delete_animal', animalObject);
    }
    if (tableName === 'Medications') {
        var medObject = {
            med_id: entityID
        };
        post('/delete_medication', medObject);
    }
    if (tableName === 'Animals_Medications') {
        var animalMedObject = {
            id: entityID
        };
        post('/delete_animal_medication', animalMedObject);
    }
    if (tableName === 'Zookeepers') {
        var zookeeperObject = {
            zookeeper_id: entityID
        };
        post('/delete_zookeeper', zookeeperObject);
    }
    if (tableName === 'Zookeepers_Workdays') {
        var zookeeperWorkdayObject = {
            id: entityID
        };
        post('/delete_zookeeper_workday', zookeeperWorkdayObject);
    }
}

/**
 * REF: https://stackoverflow.com/questions/133925/javascript-post-request-like-a-form-submit
 * sends a request to the specified url from a form. this will change the window location.
 * @param {string} path the path to send the post request to
 * @param {object} params the paramiters to add to the url
 * @param {string} [method=post] the method to use on the form
 */
function post(path, params, method = 'post') {

    // The rest of this code assumes you are not using a library.
    // It can be made less wordy if you use one.
    const form = document.createElement('form');
    form.method = method;
    form.action = path;

    for (const key in params) {
        if (params.hasOwnProperty(key)) {
            const hiddenField = document.createElement('input');
            hiddenField.type = 'hidden';
            hiddenField.name = key;
            hiddenField.value = params[key];

            form.appendChild(hiddenField);
        }
    }

    document.body.appendChild(form);
    form.submit();
}
