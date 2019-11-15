// materialize preset-pack select drop-down
document.addEventListener('DOMContentLoaded', function() {
    var elems_select = document.querySelectorAll('select');
    var instances_select = M.FormSelect.init(elems_select, {});
});

let login = document.querySelector("#login")
let register = document.querySelector("#register")
let login_toggle = document.querySelector("#login_toggle")
let register_toggle = document.querySelector("#register_toggle")


// loads the login page with only the "login" option
register.style.display = "none"
login.style.display = ""

// toggles the login form
login_toggle.addEventListener("click", function() {
    register.style.display = "none"
    login.style.display = ""
})

//toggles the register form
register_toggle.addEventListener("click", function() {
    login.style.display = "none"
    register.style.display = ""
})