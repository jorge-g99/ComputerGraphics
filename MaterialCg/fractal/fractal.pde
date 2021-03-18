void setup() {
  size(600, 600);
}

void curvakoch(float ax, float ay, float bx, float by, int K) {
  
  if(K == 0) {
    vertex(ax,ay);
    vertex(bx,by);
  } else {
    float p1x = ax + 1.0/3.0 * (bx-ax);
    float p1y = ay + 1.0/3.0 * (by-ay);
    float p2x = ax + 2.0/3.0 * (bx-ax);
    float p2y = ay + 2.0/3.0 * (by-ay);
    float p3x = ((p2x-p1x)*cos(PI/3) + (p2y-p1y)*sin(PI/3))+p1x;
    float p3y = (-(p2x-p1x)*sin(PI/3) + (p2y-p1y)*cos(PI/3))+p1y;
    
    curvakoch(ax, ay, p1x, p1y, K-1);  
    curvakoch(p1x,p1y, p3x, p3y, K-1);
    curvakoch(p3x,p3y, p2x, p2y, K-1);
    curvakoch(p2x,p2y, bx, by, K-1);
  }
}

void draw() {
  background(200);
  float margem = 100;
  float ax = margem;
  float ay = height-margem;
  float bx = width-margem;
  float by = height-margem;
  float cx = ((bx-ax)*cos(PI/3) + (by-ay)*sin(PI/3))+ax;
  float cy = (-(bx-ax)*sin(PI/3) + (by-ay)*cos(PI/3))+ay;
  
  noFill();
  int N = round(map(mouseX,0,width,0,6));
  beginShape();
  curvakoch(bx,by,ax,ay,N);
  curvakoch(ax,ay,cx,cy,N);
  curvakoch(cx,cy,bx,by,N);
  endShape();
}
