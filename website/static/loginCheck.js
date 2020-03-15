// Checking for valid credentials

// Sjekk dette i ektetid!
function checkForMatch() {
    var username = document.getElementById('username');
    var password = document.getElementById('password');
    // You're onto something henrik, keep going!
    if (username.value.length > 1) {
        document.getElementById("loginButton").disabled = false;
    } else {
        document.getElementById("loginButton").disabled = true;
    }
}

setInterval(checkForMatch, 40)