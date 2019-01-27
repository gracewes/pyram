function buildURL(activity) {
    //var activity = document.getElementById("query").value;
    var searchIndex = window.location.href.search("/index.html");
    var builtURL = "/map/" + activity;
    window.location.href = builtURL;
}

function addButton(activity, container) {
    var fieldElement = document.createElement("div");
    fieldElement.className = "field";
    container.appendChild(fieldElement);

    var controlElement = document.createElement("div");
    controlElement.className = "control";
    fieldElement.appendChild(controlElement);

    var formElement = document.createElement("form");
    controlElement.appendChild(formElement);

    var buttonElement = document.createElement("button");
    buttonElement.className = "input is-large is-dark";
    buttonElement.type = "button";
    buttonElement.onclick = function() {buildURL(activity);};
    buttonElement.innerHTML = activity;
    formElement.appendChild(buttonElement);
}

function populateMatches() {
    var matchContainer = document.getElementById("matchButtons");
    // delete all old children
    while (matchContainer.firstChild) {
        matchContainer.removeChild(matchContainer.firstChild);
    }

    var matches = ["Golf", "Go Karts", "GoLang"];
    for (var i = 0; i < matches.length; i++) {
        addButton(matches[i], matchContainer);
    }
}
