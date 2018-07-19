import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from math import *

d2r=3.14/180;r2d=180/3.14;
lw_radius = 120;#Linish Wheel radius
length = 166;lb2=length/2;
width = 48;wb2=width/2;
vr = 4;#23.499;#0 < vertex_radius < length/2,width/2
sqrt_l2pw2 = sqrt(lb2**2+wb2**2)
lb2r=lb2-vr;wb2r=wb2-vr
latan = atan((lw_radius+lb2)/(wb2r))*r2d
watan = atan((lw_radius+wb2)/(lb2r))*r2d
lwRvr=lw_radius+vr
lb2rwb2r = sqrt((lb2r)**2+(wb2r)**2)
thetavr=atan((wb2r)/(lb2r))*r2d

def Circle(angle):
    glPushMatrix()
    glTranslatef(0.0,lw_radius,0.0)
    glRotatef(angle,0,0,1)
    glColor4f(1,1,1,1)
    num_triangles = 1000
    glBegin(GL_LINES)
    for i in range(num_triangles):
        glVertex2f(0,0)
        glVertex2f(lw_radius*cos(i*2*3.14/num_triangles), lw_radius*sin(i*2*3.14/num_triangles))
    glEnd()
    glColor4f(1,0,0,1)
    glBegin(GL_LINES)
    glVertex2f(0.0,0.0)
    glVertex2f(0.0,lw_radius)
    glEnd()
    glPopMatrix()

def Rect(y,angle):
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

def rRect(y,angle):
    glPushMatrix()
    glTranslatef(0.0,y,0.0)
    glRotatef(angle,0,0,1)

    glColor4f(1,1,0,1)
    glBegin(GL_QUADS)
    glVertex2f(-wb2,-lb2r)
    glVertex2f(wb2,-lb2r)
    glVertex2f(wb2,lb2r)
    glVertex2f(-wb2,lb2r)
    glEnd()

    glColor4f(1,1,0,1)
    glBegin(GL_QUADS)
    glVertex2f(-wb2r,lb2r)
    glVertex2f(wb2r,lb2r)
    glVertex2f(wb2r,lb2)
    glVertex2f(-wb2r,lb2)
    glEnd()
    glColor4f(1,1,0,1)
    glBegin(GL_QUADS)
    glVertex2f(-wb2r,-lb2)
    glVertex2f(wb2r,-lb2)
    glVertex2f(wb2r,-lb2r)
    glVertex2f(-wb2r,-lb2r)
    glEnd()

    num_triangles = 1000
    glBegin(GL_LINES)
    for i in range(int(num_triangles/2)):
        glVertex2f(wb2r,lb2r)
        glVertex2f(wb2r+vr*cos(i*3.14/num_triangles),lb2r+vr*sin(i*3.14/num_triangles))
    glEnd()
    glBegin(GL_LINES)
    for i in range(int(num_triangles/2),num_triangles):
        glVertex2f(-wb2r,lb2r)
        glVertex2f(-wb2r+vr*cos(i*3.14/num_triangles),lb2r+vr*sin(i*3.14/num_triangles))
    glEnd()
    glBegin(GL_LINES)
    for i in range(num_triangles,3*int(num_triangles/2)):
        glVertex2f(-wb2r,-lb2r)
        glVertex2f(-wb2r+vr*cos(i*3.14/num_triangles),-lb2r+vr*sin(i*3.14/num_triangles))
    glEnd()
    glBegin(GL_LINES)
    for i in range(3*int(num_triangles/2),2*num_triangles):
        glVertex2f(wb2r,-lb2r)
        glVertex2f(wb2r+vr*cos(i*3.14/num_triangles),-lb2r+vr*sin(i*3.14/num_triangles))
    glEnd()

    glColor4f(1,0,0,1)
    glBegin(GL_LINES)
    glVertex2f(0.0,0.0)
    glVertex2f(0.0,lb2)
    glEnd()

    glPopMatrix()


def get_y(angle):
    if (angle >= 0 and angle <= (90-latan)):
        #print("0<a("+str(angle)+")<"+str(90-latan))
        y = (lw_radius+lb2) / sin((angle+90)*d2r)
    elif (angle > (90-latan) and angle < watan):
        #print(str(90-latan)+"<a1("+str(angle)+")<"+str(watan))
        sa = 90*(angle - (90-latan))/(watan-(90-latan))
        y = sqrt(lwRvr**2+lb2rwb2r**2-2*lwRvr*lb2rwb2r*cos((thetavr+90+(90-sa))*d2r))
    elif (angle >= watan and angle <= (180 - watan)):
        #print(str(watan)+"<b("+str(angle)+")<"+str(180-watan))
        y = (lw_radius+wb2) / sin(angle * d2r)
    elif (angle > (180-watan) and angle < (90+latan)):
        #print(str(180-watan)+"<b1("+str(angle)+")<"+str(90+latan))
        sa = 90*(angle - (180-watan))/((90+latan)-(180-watan))
        y = sqrt(lwRvr**2+lb2rwb2r**2-2*lwRvr*lb2rwb2r*cos((thetavr+90+sa)*d2r))
    elif (angle >= (90+latan) and angle <= (270 - latan)):
        #print(str(90+watan)+"<c("+str(angle)+")<"+str(270-latan))
        y = (lw_radius+lb2) / sin((angle-90) * d2r)
    elif (angle > (270-latan) and angle < (180+watan)):
        #print(str(270-latan)+"<c1("+str(angle)+")<"+str(180+watan))
        sa = 90*(angle - (270-latan))/((180+watan)-(270-latan))
        y = sqrt(lwRvr**2+lb2rwb2r**2-2*lwRvr*lb2rwb2r*cos((thetavr+90+(90-sa))*d2r))
    elif (angle >= (180+watan) and angle <= (360-watan)):#360+wacos
        #print(str(180+watan)+"<d("+str(angle)+")<"+str(360-watan))
        y = (lw_radius+wb2) / sin((angle-180) * d2r)
    elif (angle > (360-watan) and angle < (270+latan)):#360+wacos
        #print(str(360-watan)+"<d1("+str(angle)+")<"+str(270+latan))
        sa = 90*(angle - (360-watan))/((270+latan)-(360-watan))
        y = sqrt(lwRvr**2+lb2rwb2r**2-2*lwRvr*lb2rwb2r*cos((thetavr+90+sa)*d2r))
    elif (angle >= (270+latan) and angle <= 360):
        #print(str(270+latan)+"<e("+str(angle)+")<360")
        y = (lw_radius+lb2) / sin((angle-270)*d2r)
    else:
        print("-")
        y = lw_radius+sqrt_l2pw2
    return y

def Line():
    glPushMatrix()
    glLineWidth(2.5);
    glColor3f(0.0, 0.0, 1.0);
    glBegin(GL_LINES);
    glVertex3f(0.0, 0.0, 0.0);
    glVertex3f(0.0,-length, 0);
    glEnd();
    glPopMatrix()

def main():
    pygame.init()
    display = (600,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 450.0)

    prev_pressed=False
    #zoom_position = -5
    glTranslatef(0.0,0.0, -450.0)

    glMatrixMode(GL_MODELVIEW)

    step_angle=1.5
    a=-step_angle
    forward=True
    run=True
    while True:
        if run:
            if forward:
                a=a+step_angle
            else:
                a=a-step_angle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if (event.type == pygame.KEYDOWN) and (prev_pressed==False):
                if event.key == pygame.K_DOWN:
                    glTranslatef(0.0,0.5,0.0)
                if event.key == pygame.K_UP:
                    glTranslatef(0.0,-0.5,0.0)
                if event.key == pygame.K_LEFT:
                    glTranslatef(0.5,0.0,0.0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(-0.5,0.0,0.0)
                if event.key == pygame.K_KP_MINUS:
                    glTranslatef(0.0,0.0, -50)
                if event.key == pygame.K_KP_PLUS:
                    glTranslatef(0.0,0.0, 50)
                if event.key == pygame.K_r:
                    forward = not forward
                if event.key == pygame.K_SPACE:
                    run = not run
                if event.key == pygame.K_PAGEUP:
                    a=a+step_angle
                if event.key == pygame.K_PAGEDOWN:
                    a=a-step_angle
                prev_pressed=True
            else:
                prev_pressed=False



        if a>360:
            a=a-360
        elif a<0:
            a=a+360
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        gear_ratio=30
        Circle(a*gear_ratio)
        #Circle(a*3.14/180)
        ydist=get_y(a)
        print(str(a-90)+","+str(ydist)+",")
        rRect(lw_radius-ydist,a)
        Line()
        pygame.display.flip()

        #if (a > 0 and a < (90 - latan)):
        #    pygame.time.wait(1000)
        #elif (a > (90+latan) and a < (270 - latan)):
        #    pygame.time.wait(1000)
        #elif (a > (270+latan) and a <= 360):
        #    pygame.time.wait(1000)
        #else:
        #    pygame.time.wait(100)
        pygame.time.wait(100)


main()
