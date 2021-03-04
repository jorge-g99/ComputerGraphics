float px = 100;
float py = 100;
boolean arrastandoP = false;
float qx = 100;
float qy = 100;
boolean arrastandoQ = false;

void setup()
{
  size(800,800);
}

void draw() {
  background(200);
  
  if(arrastandoP)
  {
    px = mouseX;
    py = mouseY;
  }
  else if(arrastandoQ)
  {
    qx = mouseX;
    qy = mouseY;
  }
  
  line(px,py,qx,qy);
  circle(px, py,10);
  circle(qx, qy,10);
}

void mousePressed()
{
    if(dist(px,py,mouseX,mouseY)<10)
    {
      arrastandoP = true;
    }
    if(dist(qx,qy,mouseX,mouseY)<10)
    {
      arrastandoQ = true;
    }
  
}

void mouseReleased()
{
  arrastandoP = false;
  arrastandoQ = false;
}
