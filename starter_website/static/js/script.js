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
    if (td.firstChild.tagName === "INPUT") {
      td.firstChild.disabled = false;
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
