
var a = document.getElementById("up");
a.style.display = "none";
var a = document.getElementById("ag");
a.style.display = "none";

function autogen() {
    var ag = document.getElementById("ag");
    var up = document.getElementById("up");
    ag.style.display="block";
    up.style.display="none";
} 

function upload() {
    var ag = document.getElementById("ag");
    var up = document.getElementById("up");
    up.style.display="block";
    ag.style.display="none";
} 