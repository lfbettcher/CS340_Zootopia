// listener for edit/save and delete buttons
const tables = Array.from(document.getElementsByTagName("table"));
tables.forEach((table) => {
  addEventListener("click", (event) => {
    let target = event.target;
    console.log(target);
    if (target.tagName !== "BUTTON") return;
    if (target.name === "Edit") {
      toggleEditButton(target);
      enableRow(target.parentNode.parentNode.id);
    } else if (target.name === "Save") {
      toggleEditButton(target);
      disableRow(target.parentNode.parentNode.id);
      onUpdate(event, target.parentNode.parentNode.id);
    }
    if (target.name === "Delete") {
      onDelete(event, target.parentNode.parentNode.id);
    }
  });
});

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
    console.log(td.firstChild.tagName);
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

// send PUT request to server
function onUpdate(event, id) {
  let payload = { id: id };
  let inputs = document.querySelectorAll(
    `[id='${id}'] input:not([type=submit]):not([type=radio]),
              [id='${id}'] input[type=radio]:checked`
  );
  inputs.forEach((input) => {
    payload[input.name] = input.value;
  });
  makeRequest("PUT", payload, baseURL);
  event.preventDefault();
}

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

// send DELETE request to server
function onDelete(event, id) {
  let payload = { id: id };
  makeRequest("DELETE", payload, baseURL);
  event.preventDefault();
}

function makeRequest(type, payload, url) {
  let req = new XMLHttpRequest();
  req.open(type, url, true);
  req.setRequestHeader("Content-Type", "application/json");
  req.addEventListener("load", () => {
    if (req.status >= 200 && req.status < 400) {
      let response = JSON.parse(req.responseText);
      deleteTable();
      makeTable(response);
    } else {
      console.log("Error: " + req.statusText);
    }
  });
  req.send(JSON.stringify(payload));
}

// submit the add form and rebuild table
document.getElementById("addForm").addEventListener("submit", (event) => {
  let payload = {};
  let inputs = document.querySelectorAll(
    `#addForm input:not([type=submit]):not([type=radio]),
              #addForm input[type=radio]:checked`
  );
  inputs.forEach((input) => {
    payload[input.name] = input.value;
  });
  makeRequest("POST", payload, baseURL);
  event.preventDefault();
});

document.getElementById("reset-table").addEventListener("click", (event) => {
  makeRequest("GET", null, baseURL + "reset-table");
  event.preventDefault();
});
