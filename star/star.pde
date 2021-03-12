

void setup() 
{
  size(800,800);
}

void draw()
{
  background(200);
  pushMatrix();
  translate(width/2,height/2);
  rotate(frameCount/-85.0);
  float n = map(mouseX,0,width,100,300);
  starx(0,0,40,n);
  fill(66,154,244);
  popMatrix();
}
void starx(float x, float y, float r1, float r2) {
  float n = round(map(mouseY,20,height-20,2,20));
  float angle = TWO_PI/n;
  float halfAngle = angle/2.0;
  beginShape();
  for (float a = 0; a < TWO_PI; a += angle){
    float sx = x + cos(a) * r2;
    float sy = y + sin(a) * r2;
    vertex(sx,sy);
    float tx = x + cos(a+halfAngle) * r1;
    float ty = y + sin(a+halfAngle) * r1;
    vertex(tx,ty);
  }
  endShape(CLOSE);
}
