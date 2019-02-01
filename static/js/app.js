/*jslint browser: true*/
/*global $ */
var url = 'http://127.0.0.1:8000/api/v1/polls/';

function rand() {
    return Math.random();
}

var result = $.get(url, function(data){
    var arr = data.message;
    Plotly.plot('graph', [{
        y: arr.map(rand)
    }, {
        y: arr.map(rand)
    }]);

    var cnt = 0;

    var interval = setInterval(function() {
        Plotly.extendTraces('graph', {
            y: [[rand()], [rand()]]
        }, [0, 1])
        if(cnt === 100) 
            clearInterval(interval);
    }, 300);
});
