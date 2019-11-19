// materialize preset-pack select drop-down
document.addEventListener('DOMContentLoaded', function() {
    var elems_select = document.querySelectorAll('select');
    var instances_select = M.FormSelect.init(elems_select, {});
    var elems_modal = document.querySelectorAll('.modal');
    var instances_modal = M.Modal.init(elems_modal, {});
    var elems_tooltipped = document.querySelectorAll('.tooltipped');
    var instances_tooltipped = M.Tooltip.init(elems_tooltipped, {});
    var elems_collapsible = document.querySelectorAll('.collapsible');
    var instances_collapsible = M.Collapsible.init(elems_collapsible, {});
});

let login = document.querySelector("#login")
let register = document.querySelector("#register")
let login_toggle = document.querySelector("#login_toggle")
let register_toggle = document.querySelector("#register_toggle")


// shows only the most recent thumbnails from the last image upload
let image_after = document.querySelector("#image_after")
let image_thumbnails = document.querySelectorAll(".image_thumbnail")
let description_after = document.querySelector("#description_after")
let preset_name = document.querySelectorAll(".preset_name")

for (let i = 0; i < image_thumbnails.length; ++i) {
    image_thumbnails[i].addEventListener("click", function() {
        image_after.src = this.src
        description_after.innerHTML = ""
        description_after.innerHTML = image_thumbnails[i].title
    })
}


// changes the thumbnails visible when the drop - down changes
let preset_packs = document.querySelector("#preset_packs")




preset_packs.addEventListener("change", function() {
    let divs = document.querySelectorAll(".preset_list")
    let pack_info = document.querySelectorAll(".pack_info")
    for (let i = 0; i < divs.length; ++i) {

        if (preset_packs.value == divs[i].id) {
            divs[i].style.display = ""
            pack_info[i].style.display = ""
        } else {
            divs[i].style.display = "none"
            pack_info[i].style.display = "none"
        }

    }
})




//disables right-click
document.addEventListener('contextmenu', event => event.preventDefault());