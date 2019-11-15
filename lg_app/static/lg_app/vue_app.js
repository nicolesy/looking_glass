var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        preset_name: []
    }
    methods: {

    }

    created: function() {
        axios({
            url: '{% lg_app:get_presets %}',
            method: get,
            headers: {
                'X-CSRFToken': '{{ csrf_token }}'
            }
        }).then(response + > {
            console.log(response.data)

        })
    }
})