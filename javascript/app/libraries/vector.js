function Vector() {};

Vector.module = function(vector) {
    var temp = 0,
        length = vector.length;
    for(var i = 0; i < length; i++) {
        temp += vector[i] * vector[i];
    }
    return Math.sqrt(temp);
};

Vector.multiplication = function(vector_a, vector_b) {
    var temp = 0,
        length = vector_a.length;
    for(var i = 0; i < length; i++) {
        temp += vector_a[i] * vector_b[i];
    }
    return temp;
};

Vector.normalize = function(vector) {
    var temp = [],
        length = vector.length,
        module = this.module(vector);
    for(var i = 0; i < length; i++) {
        temp[i] = vector[i]/module;
    }
    return temp;
};

Vector.angle = function(vector_a, vector_b) {
    return this.multiplication(vector_a, vector_b)/(this.module(vector_a) * this.module(vector_b));
};