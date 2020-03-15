// Checking for valid credentials
function init(){
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var dangerUsername = document.getElementById('dangerUsername');
    var dangerPassword = document.getElementById('dangerPassword');
    
    dangerUsername.style.visibility = "hidden";
    dangerPassword.style.visibility = "hidden";
    dangerUsername.disabled = true;
    dangerPassword.disabled = true;
}

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

