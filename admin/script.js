const body = document.querySelector("body"),
    modeToggle = body.querySelector(".mode-toggle");
sidebar = body.querySelector("nav");
sidebarToggle = body.querySelector(".sidebar-toggle");

let getMode = localStorage.getItem("mode");
if (getMode && getMode === "dark") {
    body.classList.toggle("dark");
}

let getStatus = localStorage.getItem("status");
if (getStatus && getStatus === "close") {
    sidebar.classList.toggle("close");
}

modeToggle.addEventListener("click", () => {
    body.classList.toggle("dark");
    if (body.classList.contains("dark")) {
        localStorage.setItem("mode", "dark");
    } else {
        localStorage.setItem("mode", "light");
    }
});

sidebarToggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    if (sidebar.classList.contains("close")) {
        localStorage.setItem("status", "close");
    } else {
        localStorage.setItem("status", "open");
    }
});

function onClickMenu(i) {
    var content = document.getElementById("main-content");
    var content2 = document.getElementById("dash-content");
    if (i == 0) {
        refreshInterval = setInterval(function () {
            console.log('j');
            document.getElementById("boxesCount").innerHTML = ' ';
            fetcher();
        }, 5000);
        content2.innerHTML = `<div class="overview">
        <div class="title">
            <span class="text">Rooms</span>
        </div>

        <div class="boxes" id="boxesCount">
        </div>

        <div class="activity">
            <div class="title">
                <span class="text">AC Activity</span>
            </div>
            <div id="activity-data">
            </div>
        </div>
    </div>`;
        document.getElementById("boxesCount").innerHTML = ' ';
        fetcher();
    } else if (i == 1) { // 30000 milliseconds = 30 seconds
        content.innerHTML = '';
        content2.innerHTML = ` <div style="width: 50%;box-shadow: 0 0 2px;text-align:center;margin:auto;border-radius:4px;">
        <div style="text-align: center;"><br>

        <p style="font-size:20px;">Add Room</p>
        <br>
        <input type="text" class="box" placeholder="Enter Room Name" id="roomName">
            
        <br>
        <br>

        <button class="btn btn-primary" type="button" onclick="action1()">Add</button><br><br><br>
            
        </div>
        </div>
    
    <style>

    .box{
        border-radius: 10px;
        border: none;
        background: #e6e5e5;
        padding-top: 10px;
        padding-bottom: 10px;
        padding-left: 10px;
        padding-right: 10px;
        font-size: 18px;


    }
    </style>`;
    } else { // 30000 milliseconds = 30 seconds
        content.innerHTML = '';
        content2.innerHTML = `<div style="width: 50%;box-shadow: 0 0 2px;text-align:center;margin:auto;border-radius:4px;">
        <div style="text-align: center;"><br>

        <p style="font-size:20px;">Add AC Information</p>
        <br>
        <input type="text" class="box" placeholder="Enter Model Name" id="modelName">
            
        <br>

        <br>
        
        
        <input type="text" class="box" placeholder="Enter Room Name" id="temperature">
            
        <br>
        <br>

        <button class="btn btn-primary" type="button" onclick="action2()" id="addButton">Add</button><br><br><br>
            
        </div>
        </div>
    
    <style>

    .box{
        border-radius: 10px;
        border: none;
        background: #e6e5e5;
        padding-top: 10px;
        padding-bottom: 10px;
        padding-left: 10px;
        padding-right: 10px;
        font-size: 18px;
    }
    </style>`;
    }
}

function action1() {
    const API_URL = "http://127.0.0.1:5000/addRoom?size=" + document.getElementById('roomName').value;
    // Define the properties and message for the API request
    console.log(API_URL);
    const requestOptions = {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    };

    // Send GET request to API, get response and set the reponse as paragraph text
    fetch(API_URL, requestOptions).then(res => res.json()).then(data => {
        alert("Room addded successfully");
    }).catch(() => {
        alert("error");
    });
}
function action2() {
    const API_URL = "http://127.0.0.1:5000/addACModel?model=" + document.getElementById('modelName').value + "&temp=" +document.getElementById('temperature').value;
        // Define the properties and message for the API request
        const requestOptions = {
            method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    };

    // Send GET request to API, get response and set the reponse as paragraph text
    fetch(API_URL, requestOptions).then(res => res.json()).then(data => {
            alert("AC Model addded successfully");
    }).catch(() => {
            alert("error");
    });}