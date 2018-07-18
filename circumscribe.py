import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from math import *

def cCircle(angle):
    glPushMatrix()
    #glTranslatef(0.0,1,0.0)
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

def main():
    pygame.init()
    display = (600,600)

    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    prev_pressed=False
    glTranslatef(0.0,0.0, -5.0)
    glMatrixMode(GL_MODELVIEW)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if (event.type == pygame.KEYDOWN) and (prev_pressed==False):
                if event.key == pygame.K_DOWN:
                    glTranslatef(0.0,-0.5,0.0)
                if event.key == pygame.K_UP:
                    glTranslatef(0.0,0.5,0.0)
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5,0.0,0.0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5,0.0,0.0)
                if event.key == pygame.K_KP_MINUS:
                    glTranslatef(0.0,0.0, -0.5)
                if event.key == pygame.K_KP_PLUS:
                    glTranslatef(0.0,0.0, 0.5)
                prev_pressed=True
            else:
                prev_pressed=False
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cCircle(0)
        Rect(0,0)
        pygame.display.flip()
        pygame.time.wait(100)

main()
