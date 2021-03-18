// function setup() {
//   createCanvas(600, 600);
// }

// function draw() {
//   background(220);
//   ellipse(mouseX, mouseY, 100, 100);
// }

let pts = [];

function setup() {
  createCanvas(400, 400);
  pts = [
    createVector(50, 50),
    createVector(100, 300),
    createVector(300, 300),
    createVector(350, 50)
  ];
}

function draw() {
  background(220);
  noFill();
  stroke(0);
  bezier(pts[0].x, pts[0].y,
         pts[1].x, pts[1].y,
         pts[2].x, pts[2].y,
         pts[3].x, pts[3].y);
  
  noStroke();
  fill(255);
  for (let pt of pts) {
  	ellipse(pt.x, pt.y, 20, 20);
  }
  
  if (mouseIsPressed) {
    for (let pt of pts) {
      if (dist(mouseX, mouseY, pt.x, pt.y) < 20) {
        pt.x = mouseX;
        pt.y = mouseY;
        break;
      }
    }
  }
  
  noStroke();
  fill(0);
  textSize(12);
  text("bezier curve demo / drag the handles to change the curve", 4, height-4);
  
}