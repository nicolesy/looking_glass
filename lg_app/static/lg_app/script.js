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



if (preset_packs != null) {
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
}

let loading_presets = ["Beautiful B&W", "Cross Processed", "Down Under", "Everyday", "Faded Floral", "Instant Hipster", "Lovely Landscapes", "Lush", "Muted", "Nostalgia Portrait", "Nuclear Grunge", "Retro Film", "Seattle B&W", "Stylized Food", "Teal &amp; Orange", "Vintage Fade"]

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

function buttonLoading2() {
    upload_button.innerText = "applying presets"
}

function buttonLoading3() {
    upload_button.innerText = "creating thumbnails"
}

function buttonLoading4() {
    upload_button.innerText = "finishing"
}

// prevents user from uploading a blank input
// also displays text to show the user the upload is working
upload_button.addEventListener("click", function() {
    if (upload_input.files.length == 0) {
        upload_button.disabled = true
        // upload_alert.innerText = "You must select a photo to continue:"

    } else {
        cover.style.display = ""
        loader.style.display = ""

        let timer = 2000
        setTimeout("buttonLoading1()", timer)
        timer += 5000
        setTimeout("buttonLoading2()", timer)
        timer += 2000
        setTimeout("buttonLoading3()", timer)
        timer += 4000
        setTimeout("buttonLoading4()", timer)
        timer += 8000



        // 

        // can't get this to work!!!
        // let timer = 1000
        // for (let i = 0; i < loading_presets.length; ++i) {
        //     let current_preset = loading_presets[i]
        //     console.log(current_preset)
        // 
        //     function loadPresets() {
        //         upload_button.innerText = current_preset
        //     }
        //     setTimeout("loadPresets()", timer)
        //     timer += 500
        //     console.log(timer)
        // 
        // }


    }
})



//disables right-click
document.addEventListener('contextmenu', event => event.preventDefault());