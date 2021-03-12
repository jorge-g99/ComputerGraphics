from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

a = 0

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def tronco():
    raio1 = 2
    raio2 = 1
    N = 6
    H = 4
    pontosBase1 = []
    pontosBase2 = []
    angulo = (2*math.pi)/N

    glPushMatrix()
    glTranslatef(0,-2,0)
    glRotatef(a,0.0,1.0,0.0)
    glRotatef(-110,1.0,0.0,0.0)
    glColor3fv(cores[0])

    # BASE
    glBegin(GL_POLYGON)
    for i in range(0,N):
        x = raio1 * math.cos(i*angulo)
        y = raio1 * math.sin(i*angulo)
        pontosBase1 += [ (x,y) ]
        glVertex3f(x,y,0.0)
    glEnd()

    #LATERAL
    glBegin(GL_QUAD_STRIP)
    for i in range(0,N):
        x = raio1 * math.cos(i*angulo)
        y = raio1 * math.sin(i*angulo)
        pontosBase1 += [ (x,y) ]
        glColor3fv(cores[(i+1)%len(cores)])
        glVertex3f(pontosBase1[i][0],pontosBase1[i][1],H/2)
        glVertex3f(pontosBase1[(i+1)%N][0],pontosBase1[(i+1)%N][1],H/2)
        glVertex3f(pontosBase1[i][0],pontosBase1[i][1],0.0)
        glVertex3f(pontosBase1[(i+1)%N][0],pontosBase1[(i+1)%N][1],0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for i in range(0,N):
        x = raio2 * math.cos(i*angulo)
        y = raio2 * math.sin(i*angulo)
        pontosBase1 += [ (x,y) ]
        glVertex3f(x,y,H)
    glEnd()

    glPopMatrix()
def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    tronco()
    a+=1
    glutSwapBuffers()
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PIRAMIDE")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0,0,0,1)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-10)
glutTimerFunc(10,timer,1)
glutMainLoop()