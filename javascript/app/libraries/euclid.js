function Euclid() {};

Euclid.distance = function(A, B) {
    var i,
        temp = 0;
        length = A.length; 
    for(i = 0; i < length; i++) {
        temp += Math.pow(A[i] - B[i], 2);
    }
    return Math.sqrt(temp);
};