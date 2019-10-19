let flickr_photos = document.querySelector("#flickr_photos")
let flickr_search = document.querySelector("#flickr_search")
let flickr_sort = document.querySelector("#flickr_sort")
let radios = document.getElementsByName("sort_radio")

let btn_next = document.querySelector("#btn_next")
let btn_previous = document.querySelector("#btn_previous")


flickr_search.focus()
btn_next.style.display = "none"
btn_previous.style.display = "none"

let page_num = 1
let sort_order = "interestingness-desc"

function loadFlickrPhotos() {
  let url = "https://www.flickr.com/services/rest/?method=flickr.photos.search"
  console.log(url)
  axios({
      method: "get",
      url: url,
      responseType: "text",
      params: {
        api_key: flickr_api_key,
        text: flickr_search.value,
        format: "json",
        nojsoncallback: 1,
        content_type: 1,
        page: page_num,
        per_page: 20,
        sort: sort_order
      }
    })
    .then(function(response) {
      console.log(response.data.photos.photo)
      let photos = response.data.photos.photo
      let total_pages = response.data.photos.pages
      for (let i = 0; i < photos.length; ++i) {
        let owner_name = photos[i].owner_name
        let id = photos[i].id
        let farm = photos[i].farm
        let server = photos[i].server
        let secret = photos[i].secret
        let owner = photos[i].owner
        let title = photos[i].title
        let photo_url = `https://farm${farm}.staticflickr.com/${server}/${id}_${secret}.jpg`

        let a = document.createElement("A")
        a.setAttribute("href", `https://www.flickr.com/photos/${owner}/${id}`)
        a.setAttribute("target", "_blank")
        a.setAttribute("title", `${title} (Click to view on Flickr)`)
        flickr_photos.appendChild(a)

        let img = document.createElement("IMG")
        img.setAttribute("src", photo_url)

        a.appendChild(img)

      }
    })
}

flickr_search.addEventListener("keyup", function(event) {
  console.log("entered")
  // Number 13 is the "Enter" key on the keyboard
  if (event.keyCode === 13) {
    // Trigger the button element with a click
    flickr_search_btn.click()
  }
})


// sets sort order
flickr_sort.addEventListener("change", function() {
  flickr_photos.innerHTML = ""
  sort_order = document.querySelector('input[name="sort_radio"]:checked').value
  console.log(sort_order)
  loadFlickrPhotos()
})

flickr_search_btn.addEventListener("click", function() {
  flickr_photos.innerHTML = ""
  loadFlickrPhotos()
  flickr_search.select()
  btn_next.style.display = null
})

flickr_search.addEventListener("change", function() {
  flickr_photos.innerHTML = ""
})

btn_next.addEventListener("click", function() {
  page_num += 1
  flickr_photos.innerHTML = ""
  loadFlickrPhotos()
  btn_previous.style.display = null
})

btn_previous.addEventListener("click", function() {
  page_num -= 1
  flickr_photos.innerHTML = ""
  loadFlickrPhotos()
  if (page_num == 1) {
    btn_previous.style.display = "none"
  }
})

// materialize
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.tooltipped');
  var instances = M.Tooltip.init(elems, {});
});