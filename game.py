# Cal Rushton, ccr8wr
# Kaycie O'Boyle ko2re


'''
Starting Screen:
Game Title:
Instructions: Left Arrow Key: Left
             Right Arrow Key: Right
             Space Key: Spinning Attack
Names and Computing Ids:
            Cal Rushton ccr8wr
            Kaycie O'Boyle ko2re
'''

'''
General Game Design:
Vertical Platformer with randomly generated platfoms
    Can go through bottom of the platform, bounce on the top
    Continuous Vertical scrolling, if user's character hits bottom of screen --> game over
    if character hits an enemy, 25% health loss
    if character interacts with a collectible, health increases by 10% 
    character can shoot enemies to eliminate from screen
    health meter shown in top right
    score based on a combination of time survived and enemies killed
        time survived shown throughout the game
        enemies killed shown throughout the game
        when player loses, overall score is shown
    If player goes off left or right of screen, player appears on the opposite side
'''
'''
Game Aesthetics:
    every 30 secs played background changes
    User controls knight
    enemies are flying bats
    platforms come in green - player doesn't continuously fall

    link to knight/bat sprites : https://goglilol.itch.io/cute-knight
'''

import random
import gamebox
import pygame
from time import sleep

camera = gamebox.Camera(800, 600)

#Sprites
knight = gamebox.load_sprite_sheet("sheet_hero_jump.png",1,5)
fireball = gamebox.load_sprite_sheet("fire_spritesheet.png",8,8)
bat = gamebox.load_sprite_sheet("sheet_bat_fly.png",1,4)

# Variables
height_based_score = 0
enemy_based_score = 0
time = 0
impact_time = 0
attack_time = 0
health = 100
frame = 0
frame2 = 0

# Platforms

starting_platform1 = gamebox.from_color(400, 500, 'black', 70, 15)
starting_platform2 = gamebox.from_color(300, 400, 'black', 70, 15)
starting_platform3 = gamebox.from_color(600, 400, 'black', 70, 15)
starting_platform4 = gamebox.from_color(200, 300, 'black', 70, 15)
starting_platform5 = gamebox.from_color(750, 300, 'black', 70, 15)
starting_platform6 = gamebox.from_color(100, 50, 'black', 70, 15)
starting_platform7 = gamebox.from_color(50, 0, 'black', 70, 15)
starting_platform8 = gamebox.from_color(400, 350, 'black', 70, 15)
starting_platform9 = gamebox.from_color(400, 200, 'black', 70, 15)
starting_platform10 = gamebox.from_color(600, 200, 'black', 70, 15)
starting_platform11 = gamebox.from_color(500, 100, 'black', 70, 15)
starting_platform12 = gamebox.from_color(300, 100, 'black', 70, 15)

starting_platform = [starting_platform1, starting_platform2, starting_platform3, starting_platform4,
                     starting_platform5, starting_platform6, starting_platform7, starting_platform8,
                     starting_platform9, starting_platform10, starting_platform11, starting_platform12]

green_platforms = []
health_pack = []

#possible characters
character = gamebox.from_image(400, camera.y, knight[frame])
attack = gamebox.from_image(400, -300, fireball[frame])

enemies = []

movement_y = 10
movement_x = 20

# Starting Screen
background = gamebox.from_image(300, 300, "milky-way.jpg")
camera.draw(background)
camera.draw(gamebox.from_text(400, 100, "Knight Explorers", 100, "Khaki", bold=True))
camera.draw(gamebox.from_text(400, 200, "Press Space to Start", 50, "Khaki ", bold=True))
camera.draw(gamebox.from_text(400, 250, "Press Right to go right", 30, "Gold ", bold=True))
camera.draw(gamebox.from_text(400, 300, "Press Left to go left", 30, "Gold", bold=True))
camera.draw(gamebox.from_text(400, 350, "Press Up to jump", 30, "Gold", bold=True))
camera.draw(gamebox.from_text(400, 400, "Press Space to shoot", 30, "Gold", bold=True))
camera.draw(gamebox.from_text(400, 525, "By: Cal Rushton (ccr8wr)", 50, "Steel Blue", bold=True))
camera.draw(gamebox.from_text(400, 575, "      Kaycie O'Boyle (ko2re)", 50, "Steel Blue", bold=True))

camera.display()

game_on = False


def tick(keys):

    global health, frame, time, game_on, enemy, character, generation_x, generation_y
    global enemy_based_score, height_based_score, green_platforms, impact_time, health_pack
    global impact_time, attack_time, frame2, attack

    if pygame.K_SPACE in keys:
        game_on = True

    if game_on:

#Player Controls
        if pygame.K_LEFT in keys:
            character.x -= movement_x
        if pygame.K_RIGHT in keys:
            character.x += movement_x
        if pygame.K_UP in keys:
            for obstacle in starting_platform:
                if character.bottom_touches(obstacle):
                    character.y -= movement_y * 12
            for obstacle in green_platforms:
                if character.bottom_touches(obstacle):
                    character.y -= movement_y * 12
        if pygame.K_SPACE in keys:
            if time > attack_time + 30:
                attack = gamebox.from_image(character.x, character.y, fireball[frame2])
                attack_time = time

        generation_x = random.randint(50, 750)
        generation_y = camera.y - 450
        generation_plat1 = random.randint(50, 250)
        generation_plat2 = random.randint(250, 500)
        generation_plat3 = random.randint(500, 750)
        generation_plat4 = random.randint(50, 250)
        generation_plat5 = random.randint(250, 500)
        generation_plat6 = random.randint(500, 750)
        generation_plat7 = random.randint(50, 250)
        generation_plat8 = random.randint(250, 500)
        generation_plat9 = random.randint(500, 750)
        generation_plat_y = camera.y - 400

# Animates the Character
        if frame == 5:
            frame = 0
        if frame2 == 61:
            frame2 = 0
        if time % 1 == 0:
            character.image = knight[frame]
            attack.image = fireball[frame2]
            frame += 1
            frame2 += 1

        # Generating Platforms, enemies, and potions
        if time % 8 == 0:
            new_enemy = gamebox.from_image(generation_x, generation_y, bat[1])
            enemies.append(new_enemy)

        if time % 30 == 0:
            new_potion = gamebox.from_image(generation_x, generation_plat_y + 10, "Potion_of_Healing.png")
            health_pack.append(new_potion)

        if character.y < camera.y - 150:
            normal_platform = gamebox.from_color(generation_plat1, generation_plat_y, 'green', 70, 15)
            green_platforms.append(normal_platform)
            normal_platform2 = gamebox.from_color(generation_plat2, generation_plat_y, 'green', 70, 15)
            green_platforms.append(normal_platform2)
            normal_platform3 = gamebox.from_color(generation_plat3, generation_plat_y, 'green', 70, 15)
            green_platforms.append(normal_platform3)
            normal_platform4 = gamebox.from_color(generation_plat4, generation_plat_y - 100, 'green', 70, 15)
            green_platforms.append(normal_platform4)
            normal_platform5 = gamebox.from_color(generation_plat5, generation_plat_y - 100, 'green', 70, 15)
            green_platforms.append(normal_platform5)
            normal_platform6 = gamebox.from_color(generation_plat6, generation_plat_y - 100, 'green', 70, 15)
            green_platforms.append(normal_platform6)
            normal_platform7 = gamebox.from_color(generation_plat7, generation_plat_y - 200, 'green', 70, 15)
            green_platforms.append(normal_platform7)
            normal_platform8 = gamebox.from_color(generation_plat8, generation_plat_y - 200, 'green', 70, 15)
            green_platforms.append(normal_platform8)
            normal_platform9 = gamebox.from_color(generation_plat9, generation_plat_y - 200, 'green', 70, 15)
            green_platforms.append(normal_platform9)
            height_based_score += 1
            camera.y -= 300

        # Determines Background Color
        if time / 10 < 100:
            camera.clear('light cyan')
        elif 100 < time / 10 <= 200:
            camera.clear("pale turquoise")
        elif 200 < time / 10 <= 300:
            camera.clear("powder blue")
        elif 300 < time / 10 <= 400:
            camera.clear("cornflower blue")
        elif 400 < time / 10 <= 500:
            camera.clear("royal blue")
        elif 500 < time / 10 <= 600:
            camera.clear("blue")
        elif 600 < time / 10 <= 700:
            camera.clear("medium blue")
        elif 700 < time / 10 <= 800:
            camera.clear("navy blue")
        elif 800 < time / 10 <= 900:
            camera.clear("midnight blue")
        else:
            camera.clear("black")

# Platfroms Interactions
        for obstacle in starting_platform:
            if character.bottom_touches(obstacle):
                character.move_to_stop_overlapping(obstacle)
        for obstacle in green_platforms:
            if character.bottom_touches(obstacle):
                character.move_to_stop_overlapping(obstacle)

        for i in starting_platform:
            camera.draw(i)
        for i in green_platforms:
            camera.draw(i)

# Enemy Interactions
        for enemy in enemies:
            camera.draw(enemy)
            enemy.x += 10
            if enemy.x >= 800:
                enemy.x = 10
            if character.touches(enemy):
                if time > impact_time + 30:
                    # character.move_to_stop_overlapping(enemy)
                    impact_time = time
                    health -= 25
            if attack.touches(enemy):
                enemies.remove(enemy)
                enemy_based_score += 1
            if enemy.y > camera.y + 500:
                enemies.remove(enemy)

# Health Interactions
        for healing in health_pack:
            camera.draw(healing)
            if character.touches(healing):
                character.move_to_stop_overlapping(healing)
                health += 10
                health_pack.remove(healing)
        time += 1

 # Health Bar, Time Survived, Enemies Killed
        health_bar = gamebox.from_color(725, camera.y - 275, "tomato", health, 20)
        camera.draw(health_bar)
        camera.draw(gamebox.from_text(725, camera.y - 275, "Health: " + str(health), 20, "red", bold=False))
        camera.draw(
            gamebox.from_text(725, camera.y - 250, "Enemies Killed: " + str(enemy_based_score), 20, "Gold", bold=False))
        camera.draw(gamebox.from_text(725, camera.y - 225, "Time Elapsed: " + str(time // 30), 20, "Gold", bold=False))

# side movement
        if character.x < 0:
            character.x = 790
        if character.x > 800:
            character.x = 10
        if health > 100:
            health = 100
# Game Over Scenarios
        if health <= 0:
            camera.draw(gamebox.from_text(400, camera.y-200, "Game Over!", 80, "Blue", bold=False))
            overall_score = time // 30 + 2 * enemy_based_score
            camera.draw(gamebox.from_text(400, camera.y - 100, "Score: " + str(overall_score), 60, "Blue", bold=False))
            gamebox.pause()

        if character.y >= camera.y + 300:
            health = 0
            camera.draw(gamebox.from_text(400, camera.y - 200, "Game Over!", 80, "Blue", bold=False))
            overall_score = time // 30 + 2 * enemy_based_score
            camera.draw(gamebox.from_text(400, camera.y - 100, "Score: " + str(overall_score), 60, "Blue", bold=False))
            gamebox.pause()


        camera.draw(character)
        camera.draw(attack)
        camera.display()

    gravity = 1
    character.speedy += gravity
    character.move_speed()
    attack.y -= 30


ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)