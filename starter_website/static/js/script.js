// Listeners for edit buttons
const animalTable = document.getElementById("animalTable");
animalTable.addEventListener("click", (event) => {
  if (event.target.tagName !== "BUTTON") return;
  if (event.target.name === "Edit") {
    enableRow(event.target.parentNode.parentNode.id);
    toggleEditButton(event.target);
  }
});

const medTable = document.getElementById("medTable");
medTable.addEventListener("click", (event) => {
  if (event.target.tagName !== "BUTTON") return;
  if (event.target.name === "Edit") {
    enableRow(event.target.parentNode.parentNode.id);
    toggleEditButton(event.target);
  }
});

const animalMedTable = document.getElementById("animalMedTable");
animalMedTable.addEventListener("click", (event) => {
  if (event.target.tagName !== "BUTTON") return;
  if (event.target.name === "Edit") {
    enableRow(event.target.parentNode.parentNode.id);
    toggleEditButton(event.target);
  }
});

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

const searchClicked = document.getElementById("search_button");
searchClicked.addEventListener("click", function() {
document.getElementById("demo").innerHTML = "Hello World";});

function disableRow(rowID) {
  // disable inputs when save button is clicked
  let tdList = Array.from(document.getElementById(rowID).children);
  tdList.forEach((td) => {
    // console.log(td.firstChild.tagName);
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

// Huber -- under construction. . .
//const searchClicked = document.getElementById("search_button");
//searchClicked.addEventListener("click", function() {
//document.getElementById("demo").innerHTML = "Hello World";});

// function onUpdate(event, id) {
//   let payload = { id: id };
//   let inputs = document.querySelectorAll(
//     `[id='${id}'] input:not([type=submit]):not([type=radio]),
//               [id='${id}'] input[type=radio]:checked`
//   );
//   inputs.forEach((input) => {
//     payload[input.name] = input.value;
//   });
//   $.ajax({
//     type: "POST",
//     contentType: "application/json",
//     url: "/test_table/update,
//     traditional: "true",
//     data: JSON.stringify(payload),
//     dataType: "json"
//   });
//   // makeRequest("PUT", payload, baseURL);
//   event.preventDefault();
// }
//
// function makeRequest(type, payload, url) {
//   let req = new XMLHttpRequest();
//   req.open(type, url, true);
//   req.setRequestHeader("Content-Type", "application/json");
//   req.addEventListener("load", () => {
//     if (req.status >= 200 && req.status < 400) {
//       let response = JSON.parse(req.responseText);
//       deleteTable();
//       makeTable(response);
//     } else {
//       console.log("Error: " + req.statusText);
//     }
//   });
//   req.send(JSON.stringify(payload));
// }
//
// document.getElementById("reset-table").addEventListener("click", (event) => {
//   makeRequest("GET", null, baseURL + "reset-table");
//   event.preventDefault();
// });