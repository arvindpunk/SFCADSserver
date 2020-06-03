function forward() {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("result").innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", "/move/forward");
    xhttp.send();
}

function left() {
    let xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/move/left");
    xhttp.send();
}

function right() {
    let xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/move/right");
    xhttp.send();
}

function halt() {
    let xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/move/halt");
    xhttp.send();
}

function connect() {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("result").innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", "/connect");
    xhttp.send();
}