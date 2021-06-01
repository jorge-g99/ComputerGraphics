from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import math 
import sys
import random


dist = 2

n_lados = random.randrange(6, 12)


def draw_pyramid():
	height = 4
	side_rads_size = (2*math.pi)/n_lados
	down_radius = 2
	up_radius = 1
	down_vertices = []
	up_vertices = []

	glPushMatrix()
	glRotatef(-110,1.0,0.0,0.0)
	

	# Creating and drawing down vertices
	glBegin(GL_POLYGON)
	for i in range(0,n_lados):
		x = down_radius * math.cos(i*side_rads_size) - dist
		y = down_radius * math.sin(i*side_rads_size) - dist
		down_vertices += [ (x,y) ]
		glVertex3f(x,y,0.0)
	glEnd()

	# Creating and drawing up vertices
	glBegin(GL_POLYGON)
	for i in range(0,n_lados):
		x = up_radius * math.cos(i*side_rads_size) - dist
		y = up_radius * math.sin(i*side_rads_size) - dist
		up_vertices += [ (x,y) ]
		
		glVertex3f(x,y,height)
	glEnd()


	#Drawing side faces
	glBegin(GL_QUADS)
	for i in range(0,n_lados):
		glNormal3fv(calculaNormalFaceTri( (down_vertices[i][0],down_vertices[i][1],0.0), (-dist,-dist,height), (down_vertices[(i+1)%n_lados][0],down_vertices[(i+1)%n_lados][1],0.0)))
		glVertex3f(down_vertices[i][0],down_vertices[i][1],0.0)
		glVertex3f(up_vertices[i][0],up_vertices[i][1],height)
		glVertex3f(up_vertices[(i+1)%n_lados][0],up_vertices[(i+1)%n_lados][1],height)
		glVertex3f(down_vertices[(i+1)%n_lados][0],down_vertices[(i+1)%n_lados][1],0.0)
	glEnd()

	glPopMatrix()

def calculaNormalFaceTri(a, b, c):
    x = 0
    y = 1
    z = 2
    v0 = a
    v1 = b
    v2 = c
    U = ( v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
    V = ( v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
    N = ( (U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))
    NLength = sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])
    return ( N[x]/NLength, N[y]/NLength, N[z]/NLength)

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    draw_pyramid()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h),0.1,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt( 10,0,0, 0,0,0,     0,1,0 )

def init():
    mat_ambient = (0.4, 0.0, 0.0, 1.0)
    mat_diffuse = (1.0, 0.0, 0.0, 1.0)
    mat_specular = (1.0, 0.5, 0.5, 1.0)
    mat_shininess = (50,)
    light_position = (5.0, 5.0, 5.0, 0.0)
    glClearColor(0.0,0.0,0.0,0.0)
    glShadeModel(GL_FLAT)
    #glShadeModel(GL_SMOOTH)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Cubo")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutTimerFunc(50,timer,1)
    init()
    glutMainLoop()

main()
