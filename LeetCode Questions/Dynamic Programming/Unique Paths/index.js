
function uniquePaths(m,n){
    const dpMatrix = [];
    //create the matrix by adding an empty array for the number of rows
    for (let row = 1; row <= n; row++) {
        dpMatrix.push([])
    }
    //fill the first row with 1
    for (let row = 0; row < n; row++) {
        dpMatrix[row][0] = 1;
    }
    //fill the first col with 1
    for (let col = 0; col < m; col++) {
        dpMatrix[0][col] = 1;
    }

    for (let row = 1; row < n; row++) {
        for(let col = 1; col < m; col++){
            dpMatrix[row][col] = dpMatrix[row][col-1] + dpMatrix[row-1][col]
        }
    }

    return dpMatrix[n-1][m-1]
}