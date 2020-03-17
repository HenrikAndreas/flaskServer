// Checking for valid credentials
// Getting parameters from python - main and passed into html as a script parameter
function checkCredentials(userValidator, passwordValidator) {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var dangerUsername = document.getElementById('dangerUsername');
    var dangerPassword = document.getElementById('dangerPassword');

    if (userValidator === "True") {
        if (passwordValidator === "False") {
            dangerPassword.innerHTML = "Incorrect Password";
            dangerPassword.style.visibility = "visible";
        }
    } else if (userValidator === "False") {
        dangerUsername.innerHTML = "Username non existent";
        dangerUsername.style.visibility = "visible";
    }
}

