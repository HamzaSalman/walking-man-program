# Created by: Hamza Salman
# Course: ICS3U
# Created date: October 2016
# this program makes a gif

import ui
import time


box = [1, './assets/walk1.bmp', './assets/walk2.bmp', './assets/walk3.bmp', './assets/walk4.bmp', './assets/walk5.bmp', './assets/walk6.bmp', './assets/walk7.bmp', './assets/walk8.bmp', './assets/walk9.bmp', './assets/walk10.bmp']

image_counter = 4

walking_man_image = ui.Image.named(box[image_counter])
walking_man_imageview = ui.ImageView(frame=(30, 0, 180, 180))
walking_man_imageview.image = walking_man_image

@ui.in_background

def start_button_touch_up_inside(sender):
    
    global image_counter
    global walking_man_image
    
    while True:
        if image_counter <= 10:
            walking_man_image = ui.Image.named(box[image_counter])
            walking_man_imageview = ui.ImageView(frame=(200,0,180,180))
            walking_man_imageview.image = walking_man_image
            image_counter = image_counter + 1
            time.sleep(0.05)
        else:
            image_counter = 1
        
        view.add_subview(walking_man_imageview)

view = ui.load_view()
view.present('sheet')
