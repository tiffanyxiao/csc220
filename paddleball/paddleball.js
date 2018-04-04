/* ******************* */
/* *** BEGIN SETUP *** */
/* ******************* */

/* -----------------
   Set up the canvas
   ----------------- */
var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");
    ctx.font = "16px Arial";
    ctx.fillStyle = "#002855";
    
/* ----------------------------------
   Parameters for setting up the ball
   ---------------------------------- */
// Ball will have a radius of 10px 
var ballRadius = 10;

// Ball starts off centered horizontally, 30px from the bottom
var ballX = canvas.width/2;
var ballY = canvas.height-30;

// And when it moves, we'll shift 2px at a time
var dx = 2;
var dy = -2;


/* ------------------------------------
   Parameters for setting up the paddle
   ------------------------------------ */
var paddleHeight = 10;
var paddleWidth = 75;
var paddleX = (canvas.width-paddleWidth)/2;

/* ------------------------------------
   Parameters for setting up the bricks
   ------------------------------------ */
var brickWidth = 75;
var brickHeight = 20;
var brickPadding = 10;
var brickOffsetTop = 30;
var brickOffsetLeft = 30;

// An array to keep track of the remaining bricks
var bricks = [];

// Set up a 5x3 grid of bricks as a default
var brickRowCount = 5;
var brickColumnCount = 3;
for(c = 0; c < brickColumnCount; c++) {
    bricks[c] = [];
    for(r = 0; r < brickRowCount; r++) {
    	// Each brick has x,y coordinates and a status
        bricks[c][r] = { x: 0, y: 0, status: 1 };
    }
}

/* ------------------------------------
   State params to keep track of whether 
   the paddle should be moving L or R,
   the score, and the remaining lives
   ----------------------------------- */
var rightPressed = false;
var leftPressed = false;
var score = 0;
var lives = 3;

/* ---------------------------------------
   Draw the score in the upper left corner
   --------------------------------------- */
function drawScore() {
    ctx.fillText("Score: "+score, 8, 20);
}

/* ----------------------------------------
   Draw the lives in the upper right corner
   ---------------------------------------- */
function drawLives() {
    ctx.fillText("Lives: "+lives, canvas.width-65, 20);
}

/* -------------------------------------------------
   Draw a circle on the canvas to represent the ball
   ------------------------------------------------- */
function drawBall() {
    ctx.beginPath();
    ctx.arc(ballX, ballY, ballRadius, 0, Math.PI*2);
    ctx.fill();
    ctx.closePath();
}

/* ------------------------------------------------------
   Draw a rectangle on the canvas to represent the paddle
   ------------------------------------------------------ */
function drawPaddle() {
    ctx.beginPath();
    ctx.rect(paddleX, canvas.height-paddleHeight, paddleWidth, paddleHeight);
    ctx.fill();
    ctx.closePath();
}

/* ------------------------------------------------------
   Draw rectangles on the canvas to represent the bricks,
   and keep track of their position and status in array
   ------------------------------------------------------ */
function drawBricks() {

    // Loop over all columns
    for(c = 0; c < brickColumnCount; c++) {
    
        // Loop over all rows
        for(r = 0; r < brickRowCount; r++) {
            if(bricks[c][r].status == 1) {
            
            	// Calculate and store the brick's position
                var brickX = (r*(brickWidth+brickPadding))+brickOffsetLeft;
                var brickY = (c*(brickHeight+brickPadding))+brickOffsetTop;
                bricks[c][r].x = brickX;
                bricks[c][r].y = brickY;
                
                // Actually draw the corresponding rectangle to the canvas
                ctx.beginPath();
                ctx.rect(brickX, brickY, brickWidth, brickHeight);
                ctx.fill();
                ctx.closePath();
            }
        }
    }
}

/* -----------------------------------------------------
   Bring it all together to draw all the game components
   ----------------------------------------------------- */
function draw() {

	// Clear the canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Draw various game components
    drawBricks();
    drawBall();
    drawPaddle();
    drawScore();
    drawLives();
    
    // This is a function you will implement below
    // to test whether the ball hits a brick
    collisionDetection();
    
    // If the ball hits the LEFT/RIGHT WALL,
    // switch horizontal travel direction
    if(ballX + dx > canvas.width-ballRadius || ballX + dx < ballRadius) {
        dx = -dx;
    }
    
    // If the ball hits the TOP WALL
    // switch vertical travel direction
    if(ballY + dy < ballRadius) {
        dy = -dy;
    }
    
    // If ball hits the PADDLE,
    // switch vertical travel direction
    else if(ballY + dy > canvas.height-ballRadius) {
        if(ballX > paddleX && ballX < paddleX + paddleWidth) {
            dy = -dy;
        }
        
        // If ball hits the BOTTOM WALL
        else {
        
        	// Lose a life
            lives--;
            
            // If you're out of lives, GAME OVER
            if(!lives) {
                alert("GAME OVER");
                document.location.reload();
            }
            
            // If you're not out of lives, RESET BALL and PADDLE
            else {
                ballX = canvas.width/2;
                ballY = canvas.height-30;
                dx = 3;
                dy = -3;
                paddleX = (canvas.width-paddleWidth)/2;
            }
        }
    }
    
    // If PADDLE should be moving right and it isn't
    // already at the RIGHT WALL, move it to the right
    if(rightPressed && paddleX < canvas.width-paddleWidth) {
        paddleX += 7;
    }
    
    // If PADDLE should be moving left and it isn't
    // already at the LEFT WALL, move it to the left
    else if(leftPressed && paddleX > 0) {
        paddleX -= 7;
    }
    
    // Move the ball
    ballX += dx;
    ballY += dy;
    
    // Tell JS to animate the frame be recursively calling draw()
    requestAnimationFrame(draw);
}


/* ***************** */
/* *** END SETUP *** */
/* ***************** */