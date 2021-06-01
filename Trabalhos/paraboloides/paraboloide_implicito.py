from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

n1 = 50
n2 = 50
r = 2

a = 0

def f1(i,j):
    theta = (math.pi*i/(n1-1))-(math.pi/2)
    phi = 2*math.pi*j/(n2-1)
    x = r*math.cos(theta)*math.cos(phi)
    y = r*math.sin(theta)
    z = r*math.cos(theta)*math.sin(phi)
    return x,y,z

def mesh():
    glPushMatrix()
    glRotatef(a,1.0,0.0,0.0)

    glBegin(GL_QUAD_STRIP)
    #glBegin(GL_POINTS)
    
    for i in range(0,round(n1/2)): 
        #glColor3fv(((1.0*i/(n1-1)),0,1 - (1.0*i/(n1-1))))
        for j in range(0,n2): 
            glColor3fv(((1.0*(i+1)/(n1-1)),0,1 - (1.0*(i+1)/(n1-1))))
            x,y,z = f1(i,j)
            glVertex3f(x,y,z)
            x,y,z = f1(i+1,j)
            glVertex3f(x,y,z)

    glEnd()
    glPopMatrix()

def desenha():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    global a 
    a+=1
    mesh()
    glutSwapBuffers()
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(600,600)
glutCreateWindow("Paraboloide Implicito")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0,0,0,1)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-10)
glutTimerFunc(10,timer,1)
glutMainLoop()




"""
 phi = 2*math.pi*j/(n2-1)
            x = r*math.cos(theta)*math.cos(phi)
            y = r*math.sin(theta)
            z = r*math.cos(theta)*math.sin(phi)
            """