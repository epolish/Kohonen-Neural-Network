function Kohonen() {};

Kohonen._k = null;
Kohonen.euclid = Euclid;
Kohonen.matrix = Matrix;
Kohonen.vector = Vector;

Kohonen.getK = function() {
    return this._k;
};

Kohonen.setK = function(value) {
    this._k = value;
};

Kohonen.solve = function(P, W) {
    return {
        dist: this.era(P, this.matrix.copy(W), 'byDist'),
        angle: this.era(P, this.matrix.copy(W), 'byAngle')
    };
};

Kohonen.era = function(P, W, method) {
    var iteration = 0,
        Wprev = this.matrix.copy(W);
    this[method](P, W);
    while(!this.matrix.arrayEqual(Wprev, W)) {
        iteration++;
        Wprev = this.matrix.copy(W);
        this[method](P, W);
        if(iteration == 99) {
            break;
        }
    }
    return {W: W, iteration: iteration};
};

Kohonen.byDist = function(P, W) {
    var i = 0,
        j = 0,
        lengthRow = P[0].length,
        lengthColumn = this.matrix.column(W, 0).length;
    for(j = 0; j < lengthRow; j++) {
        var temp = 0,
            index = 0,
            minimum = this.euclid.distance(this.matrix.column(P, j), this.matrix.column(W, index));
        for(i = 0; i < lengthColumn; i++) {
            temp = this.euclid.distance(this.matrix.column(P, j), this.matrix.column(W, i));
            if(temp < minimum) {
                minimum = temp;
                index = i;
            }
        }
        for(i = 0; i < lengthColumn; i++) {
            W[index][i] = W[index][i] + this._k * (P[i][j] - W[index][i]);
        }
    }
    return W;
};

Kohonen.byAngle = function(P, W) {
    var i = 0,
        j = 0,
        lengthRow = P[0].length,
        lengthColumn = this.matrix.column(W, 0).length;
    for(j = 0; j < lengthRow; j++) {
        var temp = 0,
            index = 0,
            divider = 0,
            maximum = this.vector.angle(this.matrix.column(P, j), this.matrix.column(W, i));
            for(i = 0; i < lengthColumn; i++) {
                temp = this.vector.angle(this.matrix.column(P, j), this.matrix.column(W, i));
                if(temp > maximum) {
                    maximum = temp;
                    index = i;
                }
            }
            temp = this.vector.module(this.matrix.column(W, index));
            for(i = 0; i < lengthColumn; i++) {
                divider += Math.pow(this.matrix.column(W, index)[i] / temp + this._k * this.vector.normalize(this.matrix.column(P, j))[i], 2);
            }
            divider = Math.sqrt(divider);
            for(i = 0; i < lengthColumn; i++) {
                W[i][index] = (W[i][index] / temp + this._k * this.vector.normalize(this.matrix.column(P, j))[i]) / divider;
            }
    }
    return W;
};