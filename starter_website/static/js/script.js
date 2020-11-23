// Animal table listener for edit/save and delete buttons
const animalTable = document.getElementById("animalTable");
animalTable.addEventListener("click", (event) => {
  let target = event.target;
  if (target.tagName !== "BUTTON") return;
  if (target.name === "Save") {
    disableRow(target.parentNode.parentNode.id);
    toggleEditButton(target);
    updateAnimal(event, target.parentNode.parentNode.id);
  } else if (target.name === "Edit") {
    enableRow(target.parentNode.parentNode.id);
    toggleEditButton(target);
  } else if (target.name === "Delete") {
    deleteAnimal(event, target.parentNode.parentNode.id);
  }
});

// Animal UPDATE
function updateAnimal(event, id) {
  let payload = {};
  let inputs = document.querySelectorAll(`[id='${id}'] input`);
  inputs.forEach((input) => {
    payload[input.name] = input.value;
  });
  fetch('/update_animal', {
    headers: {
      'Content-Type': 'application/json'
    },
    method: 'POST',
    body: JSON.stringify(payload)
  }).then(function (res) {
    return res.text();
  // }).then(function (text) {
  //   console.log('POST response: ');
  //   console.log(text);
  })
}

// Animal DELETE
function deleteAnimal(event, id) {
  let input = document.querySelector(`[id='${id}'] input[name='animal_id']`);
  let payload = { animal_id: input.value }
  fetch('/delete_animal', {
    headers: {
      'Content-Type': 'application/json'
    },
    method: 'POST',
    body: JSON.stringify(payload)
  }).then(function (res) {
    return res.text();
  })
}

// const tables = Array.from(document.getElementsByTagName("table"));
// tables.forEach((table) => {
//   addEventListener("click", (event) => {
//     let target = event.target;
//     console.log(target);
//     if (target.tagName !== "BUTTON") return;
//     if (target.name === "Save") {
//       onUpdate(event, target.parentNode.parentNode.id);
//       disableRow(target.parentNode.parentNode.id);
//       toggleEditButton(target);
//     } else if (target.name === "Edit") {
//       enableRow(target.parentNode.parentNode.id);
//       toggleEditButton(target);
//     } else if (target.name === "Delete") {
//       onDelete(event, target.parentNode.parentNode.id);
//     }
//   });
// });

function toggleEditButton(button) {
  if (button.textContent === "Edit") {
    button.textContent = "Save";
    button.name = "Save";
  } else {
    button.textContent = "Edit";
    button.name = "Edit";
  }
};

function disableAllInput() {
  // disable inputs in table until update button is clicked
  document.querySelectorAll("tbody input").forEach((input) => {
    input.disabled = true;
  });
};

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

function enableRow(rowID) {
  // enable inputs when edit button is clicked
  let tdList = Array.from(document.getElementById(rowID).children);
  tdList.forEach((td) => {
    if (td.firstChild.tagName === "INPUT") {
      td.firstChild.disabled = false;
    }
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
