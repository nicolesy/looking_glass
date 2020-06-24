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



// updates the "after" image with the preset thumbnail that is clicked on
// also scrolls the image to the before/after photos after clicking
let image_after = document.querySelector("#image_after")
let image_thumbnails = document.querySelectorAll(".image_thumbnail")
let description_after = document.querySelector("#description_after")
let preset_name = document.querySelectorAll(".preset_name")

for (let i = 0; i < image_thumbnails.length; ++i) {
    image_thumbnails[i].addEventListener("click", function() {
        image_after.src = this.src
        description_after.innerHTML = ""
        description_after.innerHTML = image_thumbnails[i].title
        image_after.scrollIntoView({
            behavior: 'smooth'
        });
    })
}

let upload_button = document.querySelector("#upload_button")
let upload_input = document.querySelector("#upload_input")
let loader = document.querySelector("#loader")
let cover = document.querySelector("#cover")
let upload_alert = document.querySelector("#upload_alert")

// resets the transparent overlay and loading icon
cover.style.display = "none"
loader.style.display = "none"

// function used in event listener below
function makeVisible() {
    upload_button.disabled = false
}

// makes the "Upload" button visible, with a 1-second delay
upload_input.addEventListener("click", function() {
    setTimeout("makeVisible()", 1000)
})


function buttonLoading1() {
    upload_button.innerText = "Uploading..."
}

// prevents user from uploading a blank input
// also displays text to show the user the upload is working
// adds a loading screen
upload_button.addEventListener("click", function() {
    if (upload_input.files.length == 0) {
        upload_button.disabled = true
        // upload_alert.innerText = "You must select a photo to continue:"

    } else {
        cover.style.display = ""
        loader.style.display = ""

        let timer = 2000
        setTimeout("buttonLoading1()", timer)
    }
})



// loading screen for index page when selecting a preset pack
let select_list = document.querySelector("#select_list")
let cover_index = document.querySelector("#cover_index")
let loader_index = document.querySelector("#loader_index")


select_list.addEventListener("click", function() {
    cover_index.style.display = ""
    loader_index.style.display = ""
})



//disables right-click
document.addEventListener('contextmenu', event => event.preventDefault());