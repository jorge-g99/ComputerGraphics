float p1x = 100;
float p1y = 800/2;
boolean arrastandoP1 = false;

float p2x = 600;
float p2y = 600/4;
boolean arrastandoP2 = false;

float p3x = 200;
float p3y = 600*(3/4);
boolean arrastandoP3 = false;

float p4x = 600;
float p4y = 800/2;
boolean arrastandoP4 = false;

void setup()
{
  size(800,600);
}

void draw()
{
  background(128);
  
  if(arrastandoP1){
    p1x = mouseX;
    p1y = mouseY;
  }else if(arrastandoP2){
    p2x = mouseX;
    p2y = mouseY;
  }else if(arrastandoP3){
    p3x = mouseX;
    p3y = mouseY;
  }else if(arrastandoP4){
    p4x = mouseX;
    p4y = mouseY;
  }
  circle(p1x, p1y, 10);
  circle(p2x, p2y, 10);
  circle(p3x, p3y, 10);
  circle(p4x, p4y, 10);
  noFill();
  beginShape();
  vertex(p1x, p1y);
  for(float t = 0; t <= 1; t += 0.05)
  {
    float ax = p1x + t*(p2x-p1x);
    float bx = p2x + t*(p3x-p2x);
    float cx = p3x + t*(p4x-p3x);
    
    float ay = p1y + t*(p2y-p1y);
    float by = p2y + t*(p3y-p2y);
    float cy = p3y + t*(p4y-p3y);
    
    
    float dx = ax + t*(bx-ax);
    float dy = ay + t*(by-ay);
    float ex = bx + t*(cx-bx);
    float ey = by + t*(cy-by);
    
    float fx = dx + t*(ex-dx);
    float fy = dy + t*(ey-dy);
    
    vertex(fx,fy);  
  }
  vertex(p4x, p4y);
  endShape();
}

void mousePressed()
{
    if(dist(p1x,p1y,mouseX,mouseY)<10)
    {
      arrastandoP1 = true;
    }
    if(dist(p2x,p2y,mouseX,mouseY)<10)
    {
      arrastandoP2 = true;
    }
    if(dist(p3x,p3y,mouseX,mouseY)<10)
    {
      arrastandoP3 = true;
    }
    if(dist(p4x,p4y,mouseX,mouseY)<10)
    {
      arrastandoP4 = true;
    }
  
}

void mouseReleased()
{
  arrastandoP1 = false;
  arrastandoP2 = false;
  arrastandoP3 = false;
  arrastandoP4 = false;
}
