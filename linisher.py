import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from math import *

def cCircle(angle):
    glPushMatrix()
    glTranslatef(0.0,1,0.0)
    glRotatef(angle,0,0,1)
    glColor4f(1,1,1,1)
    num_triangles = 1000
    glBegin(GL_LINES)
    for i in range(num_triangles):
        glVertex2f(0,0)
        glVertex2f(cos(i*2*3.14/num_triangles), sin(i*2*3.14/num_triangles))
    glEnd()
    glColor4f(1,0,0,1)
    glBegin(GL_LINES)
    glVertex2f(0.0,0.0)
    glVertex2f(0.0,1.0)
    glEnd()
    glPopMatrix()

def Circle(angle):
    glColor4f(1,1,1,1)
    glBegin(GL_LINES)
    num_triangles = 1000
    x=0
    y=1
    r=1
    for i in range(num_triangles-6):
        glVertex2f(x,y)
        glVertex2f(x+r*cos(angle+i*2*3.14/num_triangles), y+r*sin(angle+i*2*3.14/num_triangles))
    glEnd()

def Rect(y,angle):
    length = 2
    width = 0.4
    glPushMatrix()
    glTranslatef(0.0,y,0.0)
    glRotatef(angle,0,0,1)
    glColor4f(1,1,0,1)
    glBegin(GL_QUADS)
    glVertex2f(-width/2.0,-length/2.0)
    glVertex2f(width/2.0,-length/2.0)
    glColor4f(1,1,0,1)
    glVertex2f(width/2.0,length/2.0)
    glVertex2f(-width/2.0,length/2.0)
    glEnd()
    glColor4f(1,0,0,1)
    glBegin(GL_LINES)
    glVertex2f(0.0,0.0)
    glVertex2f(0.0,length/2.0)
    glEnd()
    glPopMatrix()

def get_y(angle):
    latan = atan((1+1)/0.2)*180/3.14
    watan = atan((1+0.2)/1)*180/3.14
    if (angle > 0 and angle < (90 - latan)):
        y = (1+1) / sin((angle+90)*3.14/180)
    elif (angle > watan and angle < (180 - watan)):
        y = (1+0.2) / sin(angle * 3.14 / 180)
    elif (angle > (90+latan) and angle < (270 - latan)):
        y = (1+1) / sin((angle-90) * 3.14 / 180)
    elif (angle > (180+watan) and angle < (360-watan)):
        y = (1+0.2) / sin((angle-180) * 3.14 / 180)
    elif (angle > (270+latan) and angle <= 360):
        y = (1+1) / sin((angle-270)*3.14/180)
    else:
        y = 0
    return 1-y

def Line():
    glPushMatrix()
    glLineWidth(2.5);
    glColor3f(0.0, 0.0, 1.0);
    glBegin(GL_LINES);
    glVertex3f(0.0, 0.0, 0.0);
    glVertex3f(0.0,-3.0, 0);
    glEnd();
    glPopMatrix()

def main():
    pygame.init()
    display = (600,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    glMatrixMode(GL_MODELVIEW)

    latan = atan((1+1)/0.2)*180/3.14
    watan = atan((1+0.2)/1)*180/3.14
    a=0
    while True:
        a=a+1
        if a>360:
            a=a-360

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cCircle(a)
        #Circle(a*3.14/180)
        Rect(get_y(a),a)
        Line()
        pygame.display.flip()

        if (a > 0 and a < (90 - latan)):
            pygame.time.wait(1000)
        elif (a > (90+latan) and a < (270 - latan)):
            pygame.time.wait(1000)
        elif (a > (270+latan) and a <= 360):
            pygame.time.wait(1000)
        else:
            pygame.time.wait(100)


main()
