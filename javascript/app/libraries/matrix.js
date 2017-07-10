function Matrix() {};

Matrix.arrayEqual = function(A,B) {
    var m = A.length, 
        n = A[0].length;
    if(m != B.length || n != B[0].length) {
        return false;
    }
    for(var i = 0; i < m; i++) {
        for(var j = 0; j < n; j++) {
            if(A[i][j] != B[i][j]) {
                return false;
            }
        }
    }
    return true;
};

Matrix.column = function(matrix, col) {
    var column = [],
        length = matrix.length;
    for(var i = 0; i < length; i++) {
        column.push(matrix[i][col]);
    }
    return column;
};

Matrix.copy = function(A) {
    var newArray = [],
        length = A.length;
    for(var i = 0; i < length; i++) {
        newArray[i] = A[i].slice();   
    }
    return newArray
};