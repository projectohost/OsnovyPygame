from pygame import *

window = display.set_mode((700, 500))
display.set_caption("Доганялки")
background = transform.scale(image.load("bg.jpg"), 
                             (700, 500))

#дані про спрайт-картинку
x1 = 100
y1 = 300

x2 = 300
y2 = 300
 
sprite1 = transform.scale(image.load('sprite.png'), 
                          (100, 100))
sprite2 = transform.scale(image.load('enemy2.png'), 
                          (100, 100))
speed = 10
 
#ігровий цикл
run = True
clock = time.Clock()
FPS = 60
 
while run:
    window.blit(background,(0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    keys_pressed = key.get_pressed()
    
    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 395:
        y1 += speed
    
    if keys_pressed[K_a] and x2 > 5:  # вліво
        x2 -= speed
    if keys_pressed[K_d] and x2 < 595:
        x2 += speed # speed = 10
    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed
    if keys_pressed[K_s] and y2 < 395:
        y2 += speed
    
    display.update()
    clock.tick(FPS)
