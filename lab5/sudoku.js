// A suduko puzzle is a 9x9 array with numbers from 0-9.

// Some examples:

var diagonal =
    [ [1,0,0,0,0,0,0,0,0]
    , [0,2,0,0,0,0,0,0,0]
    , [0,0,3,0,0,0,0,0,0]
    , [0,0,0,4,0,0,0,0,0]
    , [0,0,0,0,5,0,0,0,0]
    , [0,0,0,0,0,6,0,0,0]
    , [0,0,0,0,0,0,7,0,0]
    , [0,0,0,0,0,0,0,8,0]
    , [0,0,0,0,0,0,0,0,9] ];

var easy =
    [ [0,2,0,4,5,6,7,8,9]
    , [4,5,7,0,8,0,2,3,6]
    , [6,8,9,2,3,7,0,4,0]
    , [0,0,5,3,6,2,9,7,4]
    , [2,7,4,0,9,0,6,5,3]
    , [3,9,6,5,7,4,8,0,0]
    , [0,4,0,6,1,8,3,9,7]
    , [7,6,1,0,4,0,5,2,8]
    , [9,3,8,7,2,5,0,6,0] ];

var medium =
    [ [0,4,0,0,0,2,0,1,9]
    , [0,0,0,3,5,1,0,8,6]
    , [3,1,0,0,9,4,7,0,0]
    , [0,9,4,0,0,0,0,0,7]
    , [0,0,0,0,0,0,0,0,0]
    , [2,0,0,0,0,0,8,9,0]
    , [0,0,9,5,2,0,0,4,1]
    , [4,2,0,1,6,9,0,0,0]
    , [1,6,0,8,0,0,0,7,0] ];

var hard =
    [ [0,2,0,0,0,0,0,0,0]
    , [0,0,0,6,0,0,0,0,3]
    , [0,7,4,0,8,0,0,0,0]
    , [0,0,0,0,0,3,0,0,2]
    , [0,8,0,0,4,0,0,1,0]
    , [6,0,0,5,0,0,0,0,0]
    , [0,0,0,0,1,0,7,8,0]
    , [5,0,0,0,0,9,0,0,0]
    , [0,0,0,0,0,0,0,4,0] ];

var almostsolved =
    [ [0,2,3,4,5,6,7,8,9]
    , [4,5,7,1,8,9,2,3,6]
    , [6,8,9,2,3,7,1,4,5]
    , [8,1,5,3,6,2,9,7,4]
    , [2,7,4,8,9,1,6,5,3]
    , [3,9,6,5,7,4,8,1,2]
    , [5,4,2,6,1,8,3,9,7]
    , [7,6,1,9,4,3,5,2,8]
    , [9,3,8,7,2,5,4,6,1] ];

var solved =
    [ [1,2,3,4,5,6,7,8,9]
    , [4,5,7,1,8,9,2,3,6]
    , [6,8,9,2,3,7,1,4,5]
    , [8,1,5,3,6,2,9,7,4]
    , [2,7,4,8,9,1,6,5,3]
    , [3,9,6,5,7,4,8,1,2]
    , [5,4,2,6,1,8,3,9,7]
    , [7,6,1,9,4,3,5,2,8]
    , [9,3,8,7,2,5,4,6,1] ];

// Return an empty sudoku
function emptySudoku() {
    return [ [0,0,0,0,0,0,0,0,0]
           , [0,0,0,0,0,0,0,0,0]
           , [0,0,0,0,0,0,0,0,0]
           , [0,0,0,0,0,0,0,0,0]
           , [0,0,0,0,0,0,0,0,0]
           , [0,0,0,0,0,0,0,0,0]
           , [0,0,0,0,0,0,0,0,0]
           , [0,0,0,0,0,0,0,0,0]
           , [0,0,0,0,0,0,0,0,0] ];
}


// Convert an array of arrays to a string keeping track of the inner
// arrays.
function arrayToString(arr) {
    res = "";
    for (i = 0; i < arr.length; i++) {
        res += "[" + arr[i] + "]<br>";
    }
    return res;
}


// Compute all 27 blocks of a sudoku. Returns all 9 rows, 9 cols and 9
// 3x3 blocks
function blocks(sud) {
    var n = sud.length;
    var sudCols = emptySudoku();
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            sudCols[j][i] = sud[i][j];
        }
    }
    threeByThree = []
    for (i = 0; i < n; i = i+3) {
        for (j = 0; j < n; j = j+3) {
            threeByThree.push(slice3x3(sud, i, j, i+3, j+3));
        }
    }
    return sud.concat(sudCols, threeByThree);
}


function slice3x3(A, startx, starty, endx, endy) {
    var B = [];
    for (y = starty; y < endy; y++) {
        for (x = startx; x < endx; x++) {
            B.push(A[y][x]);
        }
    }
    return B;
    }

// Check that a block is valid (i.e. that it contains no duplicate
// number 1-9, but multiple 0 is fine).
function isValidBlock(b) {
    return b.filter((a, i) => a === 0 || b.indexOf(a) === i).length == b.length;
}


// Check that a sudoku is valid by checking that all of its blocks are
// valid.
function isValid(sud) {
    return blocks(sud).map(isValidBlock).filter(a => a == false).length == 0;
}


// Check if a sudoku is solved by checking that there are no zeroes
// and that it is valid.
function isSolved(sud) {
    return (isValid(sud)) && blocks(sud).filter(a => a.includes(0)).length === 0;
}


// Draw the start sudoku
function init(sud) {
    var n = sud.length
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            var id = `c${i}x${j}`;
            if (sud[i][j] !== 0) {
                document.getElementById(id).innerHTML = sud[i][j];
                document.getElementById(id).style.backgroundColor = "#b6d9ee";
            } else {
                document.getElementById(id).onclick = klick;
            }
        }
    }
}


// What to do when the user clicks on a tile
function klick() {
    var inputValue = prompt("Enter a digit between 1-9");
    if ((inputValue > 0 && inputValue < 10) || inputValue == "" || inputValue == null){
        this.innerHTML = inputValue;
        if (isValid(getSudoku())){
            if (isSolved(getSudoku())){
                alert("You Won.")
            }
        } else {
            this.innerHTML = '';
            alert("Sudoko not valid, try again.");
        }
    } else {
        alert("Please input a number between 1-9.");
    }
}

// Fetch the current sudoku
function getSudoku() {
    var res = emptySudoku();
    var n = res.length;
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            var id = `c${i}x${j}`;
            var val = document.getElementById(id).innerHTML;
            if (val !== ""){
                res[i][j] = val;
            }
        }
    }
    console.log(arrayToString(res))
    return res
}
