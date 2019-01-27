function buildURL() {
    var activity = document.getElementById("query").value;
    var searchIndex = window.location.href.search("/index.html");
    var builtURL = "/map/" + activity;
    window.location.href = builtURL;
}
