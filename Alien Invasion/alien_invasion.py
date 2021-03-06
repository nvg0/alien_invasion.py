# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 18:42:05 2017

@author: Noah
"""
import sys
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from bullet import Bullet
from alien import Alien

def run_game():
    #Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    
    #Make a ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in 
    bullets = Group()
    # Make a group of aliens
    aliens = Group()
    
    # Create the fleet of aliens
    gf.create_fleet(ai_settings, stats, screen, ship, aliens)
    
    #Set the background color.
    bg_color = (230, 230, 230)
    
    #start the main loop for the game.
    while True:
        
        #watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
    
    