//Checking if input in registration form is valid
// Getting parameters from python - main and passed into html as a script parameter
function verifyRegistration(userExists, passwordValid) {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var conf_password = document.getElementById('conf_password').value;
    var dangerUsername = document.getElementById('dangerUsername');
    var dangerPassword = document.getElementById('dangerPassword');
    var dangerConfPassword = document.getElementById('dangerConfPassword');

    if (userExists === "True") {
        dangerUsername.innerHTML = "Username already exists!";
        dangerUsername.style.visibility = "visible";
    } else {
        if (passwordValid === "False") {
            dangerConfPassword.innerHTML = "Passwords do not match!";
            dangerConfPassword.style.visibility = "visible";
        }
    }
}

function checkCredentials() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var conf_password = document.getElementById('conf_password').value;
    var dangerUsername = document.getElementById('dangerUsername');
    var dangerPassword = document.getElementById('dangerPassword');
    var dangerConfPassword = document.getElementById('dangerConfPassword');
    var loginButton = document.getElementById('loginButton');
    loginButton.disabled = true;

    if (username.length > 1 && username.length < 6) {
        dangerUsername.innerHTML = "Username must be 6 chars!";
        dangerUsername.style.visibility = "visible";
    } else {
        dangerUsername.style.visibility = "hidden";
    }

    if (password.length > 1 && password.length < 6) {
        dangerPassword.innerHTML = "Password must be 6 chars!";
        dangerPassword.style.visibility = "visible";
    } else {
        dangerPassword.style.visibility = "hidden";
    }

    if (conf_password.length > 2) {
        if (conf_password != password) {
            dangerConfPassword.innerHTML = "Passwords do not match!";
            dangerConfPassword.style.visibility = "visible";
        } else {
            dangerConfPassword.style.visibility = "hidden";
        }
    }

    if (username.length >= 6) {
        if (password.length >= 6) {
            if (password === conf_password) {
                loginButton.disabled = false;
            }
        }
    }
}

setInterval(checkCredentials, 1000);