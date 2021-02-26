void setup(){
  size(800,800);
}

float px = 100;
float py = 100;
boolean arrastandoP1 = false;

void draw(){
  background(200);
  
  if(arrastandoP1){
    px=mouseX;
    py=mouseY;
  }
  circle(px,py,10);
}
void mousePressed() {
  if(dist(px,py,mouseX,mouseY)<10){
    arrastandoP1 = true;
  }
}

void mouseReleased(){
  arrastandoP1 = false;
}
