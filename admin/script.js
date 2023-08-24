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
        content.innerHTML = '';
        content.innerHTML = `<div class="dash-content">
        <div class="overview">
            <div class="title">
                <span class="text">Rooms</span>
            </div>

            <div class="boxes" id="boxesCount">
            </div>
            <script>
                // const API_URL = "http://127.0.0.1:5000/fetchData";

                // const requestOptions = {
                //     method: "GET",
                //     headers: {
                //         "Content-Type": "application/json",
                //     },
                // };

                // fetch(API_URL, requestOptions)
                //     .then(response => response.json())
                //     .then(data => {
                //         // Process the fetched data here
                //         console.log(data); // Log the fetched data to the console
                //         // You can use data to update your HTML content
                //         // For example, if you have a div with id "dataContainer", you can do:
                //         // document.getElementById("dataContainer").textContent = JSON.stringify(data);
                //     })
                //     .catch(error => {
                //         console.error("Error:", error);
                //         alert("An error occurred while fetching the data.");
                //     });

                const rooms = {}; // Use an object instead of an array to store room data
                const model = {};

                fetch("../rooms.json")
                    .then(response => response.json())
                    .then(data => {
                        for (const roomNumber in data) {
                            if (data.hasOwnProperty(roomNumber)) {
                                const room = data[roomNumber];
                                rooms[roomNumber] = room; // Store room data in the object

                                // Process each model in the room
                                let layout = '<table  class="table table-striped"><tr><th scope="col">Model Name</th><th scope="col">Status</th><th scope="col">Problems</th></tr>';
                                for (const modelData of room.model) {
                                    layout +='<tr><td>${modelData.Model}</td><td>${modelData.Status}</td><td>${modelData.Problem}</td></tr>';
                                }
                                layout += '</table>';
                                model[roomNumber] = layout;

                                // Create a div with class "box" for each room
                                const roomDiv = document.createElement("div");
                                roomDiv.className = "box box1";
                                roomDiv.onclick = () => changeList(roomNumber); // Assuming changeList is a function

                                // Create and append content to the div
                                roomDiv.innerHTML = '<span class="text"> ${roomNumber}</span >
                                <span class="number">${room.count} ACs</span>';
                                rooms[roomNumber] = roomDiv;
                            }
                        }
                    for (var i in rooms) {
                        displayALL(i);
                    }}).catch (error => {
                        console.error("Error:", error);
                    });
                    function displayALL(roomNumber) {
                        var id = document.getElementById("boxesCount");
                        id.appendChild(rooms[roomNumber])
                    }
                    function changeList(roomNumber) {
                        var id = document.getElementById("activity-data");
                        id.innerHTML = '';
                        id.innerHTML += model[roomNumber];
                    }
                    </script >
                        <div class="activity">
                            <div class="title">
                                <span class="text">AC Activity</span>
                            </div>
                            <div class="activity-data" id="activity-data">
                            </div>
                        </div>
                            </div >
                        </div > `;

    } else if (i == 1) {
        content.innerHTML = '';
        content2.innerHTML = `<div class="container mt-5 custom-container" >
    <div class="row">
        <div class="col-md-6">
            <div class="input-group">
                <input type="text" class="form-control" placeholder="Enter Room Name" id="roomName">
                    <div class="input-group-append">
                        <button class="btn btn-primary" type="button" onclick="action()">Add</button>
                    </div>
            </div>
        </div>
    </div>
    </div >
    <style>
        .custom-container {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }

        .input-group {
            margin-bottom: 15px;
        }
    </style>
    <script>
        function action() {
            const API_URL = "http://127.0.0.1:5000/addRoom?size=" + document.getElementById('roomName').value;
            // Define the properties and message for the API request
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
        </script>`;
    } else {
        content.innerHTML = '';
        content2.innerHTML = `<div class="container mt-5 custom-container">
    <div class="row">
        <div class="col-md-6">
            <div class="input-group">
                <input type="text" class="form-control" placeholder="Enter Model Name" id="modelName"><br><br>
                    <input type="text" class="form-control" placeholder="Enter Temparature(in Celsius)" id="temperature">
                        <div class="input-group-append">
                            <button class="btn btn-primary" type="button" id="addButton">Add</button>
                        </div>
                    </div>
                </div>
                </div>
            <style>
                .custom-container {
                    background - color: #f8f9fa;
                padding: 20px;
                border-radius: 5px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }

                .input-group {
                    margin - bottom: 15px;
        }
            </style>
            <script>
                function action() {
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
            });
        }
            </script>`;
    }
}

