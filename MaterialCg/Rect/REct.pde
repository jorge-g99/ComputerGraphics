class C {
  float x, y, raio;
  
  C(float x, float y, float raio) {
    this.x = x;
    this.y = y;
    this.raio = raio;
  }
  
  void desenha() {
    ellipseMode(CENTER);
    fill(255,255,0);
    circle(x,y,raio);
  }
}

void setup() {
  size(800, 600);
  //println(frameRate);
  rectMode(CENTER);
  ellipseMode(CENTER);
}

void draw() {
  background(200);
  // rect(mouseX, mouseY, 20, 40);
  // int lado = min(frameCount, 200);
  // float lado = (cos(frameCount/50.0)*200)+20;
  float lado =((cos(frameCount/50.0)+1)/2)*180+20;
  fill(0,0,255);
  rect(width/2,height/2, lado, lado);
  C c = new C(width/2,height/2, lado*0.9);
  c.desenha();
}
