#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 15:52:08 2019

@author: DannySwift
"""

from cv2 import *
import numpy as np

class GravLens:

    def __init__(self):
        G = 6.67408 * 10**(-11) #m^3 kg^-1 s^-2
        solar_mass = 1.989*10**30 #kg
        black_hole_size = 100 #solar masses
        c = 299792458 # m/s
        observer_distance = 30000000 # m
        source_distance = 30000000 # m
        meters_per_pixel = 30000 #46845 at pi/4

        M = solar_mass * black_hole_size
        rs = 2 * G * M / c**2
        self.observer_distance_pixels = observer_distance / meters_per_pixel
        self.source_distance_pixels = source_distance / meters_per_pixel
        self.rs_pixels = int(round(rs / meters_per_pixel))
        
        cam = VideoCapture(0)
        self.x_range = int(cam.get(CAP_PROP_FRAME_WIDTH))
        self.mid_x = self.x_range / 2
        self.y_range = int(cam.get(CAP_PROP_FRAME_HEIGHT))
        self.mid_y = self.y_range / 2
        cam.release()
        self.arange = np.arange
        
        self.x = np.arange(self.x_range)
        self.y = np.arange(self.y_range)[:, np.newaxis]
        self.r_sqr = (self.x - self.mid_x) ** 2 + (self.y - self.mid_y) ** 2
        self.r = np.sqrt(self.r_sqr)
        self.alpha = np.arctan(self.r / (self.observer_distance_pixels + self.source_distance_pixels)**2)
        self.theta = 2 * self.rs_pixels / self.r
        self.offset = self.source_distance_pixels * (
            1 / np.tan(np.pi / 2 + self.alpha - self.theta) + 
            (1 / np.tan(np.pi / 2 - self.alpha)))
        
        mid_x = self.mid_x
        mid_y = self.mid_y     
        bh_x_coord = mid_x
        bh_y_coord = mid_y
        bh_offset_sqr = (bh_x_coord - mid_x)**2 + (bh_y_coord - mid_y)**2
        bh_offset = np.sqrt(bh_offset_sqr)
        #bh_to_obs_sqr = bh_offset_sqr + observer_distance_pixels**2
        #bh_to_obs = np.sqrt(bh_to_obs_sqr)
        
        x = self.x
        y = self.y

        dx = x - bh_x_coord
        dy = y - bh_y_coord

        m = dy / dx
        #b = y - m * x

        delta_x = np.round(-1 * self.offset * dx / self.r).astype(int)
        x_prime = x + delta_x
        self.x_prime = np.clip(x_prime, 0, self.x_range - 1)
        y_prime = np.round(y + m * delta_x).astype(int)
        self.y_prime = np.clip(y_prime, 0, self.y_range - 1)
    
    def grav_lens_2(self, img):

        new_img = img[self.y_prime, self.x_prime]

        return(new_img)
    
    def play(self):
        cam = VideoCapture(0)
        s, img = cam.read()
        window = namedWindow('window')
        while(s == 1):
            s, img = cam.read()
            imshow('window', self.grav_lens_2(img))
            k = waitKey(1)
            if k == 27:
                destroyAllWindows()
                cam.release()
                s = 0
            
def main():
    gl = GravLens()
    gl.play()
    

if __name__ == "__main__":
    main()