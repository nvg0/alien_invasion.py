# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 18:57:35 2017

@author: Noah
"""
class Settings():
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings."""
        #screen settings
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        
        #Ship settings
        self.ship_speed_factor = 1.5
        
        #Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        #Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        
        