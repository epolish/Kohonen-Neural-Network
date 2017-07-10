function Plot() {};

Plot.draw = function(element, data) {
    var data = [
        this.getTrace(data[0], 'rgb(255, 0, 0)', 'Координаты центров кластеров (Евклидово расстояние)'),
        this.getTrace(data[1], 'rgb(0, 255, 0)', 'Координаты центров кластеров (Угловое расстояние)'),
        this.getTrace(data[2], 'rgb(0, 0, 255)', 'Координаты точек')
    ];
    
    Plotly.newPlot(element, data, this.getLayout());
};

Plot.getLayout = function() {
    return {
        margin: {
            l: 0,
            r: 0,
            b: 0,
            t: 0
        }
    };
};

Plot.getTrace = function(data, rgbColor, traceName) {
    return {
        x: data[0],
        y: data[1],
        z: data[2],
        mode: 'markers',
        marker: {
            color: rgbColor,
            size: 12,
            symbol: 'circle',
            line: {
                color: 'rgba(217, 217, 217, 0.14)',
                width: 0.5
            },
            opacity: 0.8
        },
        type: 'scatter3d',
        name: traceName
    };
};