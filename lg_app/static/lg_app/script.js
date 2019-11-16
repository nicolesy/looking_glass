// materialize preset-pack select drop-down
document.addEventListener('DOMContentLoaded', function() {
    var elems_select = document.querySelectorAll('select');
    var instances_select = M.FormSelect.init(elems_select, {});
    var elems_modal = document.querySelectorAll('.modal');
    var instances_modal = M.Modal.init(elems_modal, {});
});

// let dropdown_trigger = document.querySelector(".dropdown_trigger")
// 
// $(document).ready(function() {
//     $(dropdown_trigger).dropdown();
// });

let login = document.querySelector("#login")
let register = document.querySelector("#register")
let login_toggle = document.querySelector("#login_toggle")
let register_toggle = document.querySelector("#register_toggle")


// shows only the most recent thumbnails from the last image upload
let image_after = document.querySelector("#image_after")
let image_thumbnails = document.querySelectorAll(".image_thumbnail")

for (let i = 0; i < image_thumbnails.length; ++i) {
    image_thumbnails[i].addEventListener("click", function() {
        image_after.src = this.src
    })
}


//disables right-click
document.addEventListener('contextmenu', event => event.preventDefault());