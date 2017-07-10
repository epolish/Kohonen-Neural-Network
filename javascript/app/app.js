(function($) {
    $(function() {
        var draw = function(P, W) {
                var data = Kohonen.solve(P, W);
                $('#content').css('height', '85vh');
                $('#euclid-result').html(data.dist.iteration);
                $('#angle-result').html(data.angle.iteration);
                Plot.draw('content', [data.dist.W, data.angle.W, P]);
            },
            randArray = function(min, max, count) {
                var arr = [];
                while(arr.length < count) {
                    var randomNumber = Math.random() * (max - min) + min;
                    if(arr.indexOf(randomNumber) > -1) {
                        continue;
                    }
                    arr[arr.length] = randomNumber;
                }
                return arr;
            },
            main = function() {
                Kohonen.setK($('#ratio').val());
                if(typeof Weight == 'undefined') {
                    Weight = [];
                    for(var i = 0; i < count; i++) {
                        Weight[i] = randArray(min, max, count);
                    }
                }
                $('#ratio').change(function() {
                   Kohonen.setK($(this).val());
                   draw(Points, Weight);
                });
                draw(Points, Weight); 
            };
        main();
    });
}(jQuery));