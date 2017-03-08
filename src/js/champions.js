(window.onload = function() {
    var axios = require('axios')
    var champions = new Vue({
        el: '.champions',
        delimiters: ['[[', ']]'],
        data: {
            champions: []
        },
        created: function() {
            var self = this
            axios.get('/api/v1/champions.json').then(res => {
                this.champions = res.data.data
            });
        }
    })
});
