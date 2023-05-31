# Create a list of animation frames
from math import sin, floor, cos
import pygame
from pygame import *

clock = pygame.time.Clock()
screen_height = 700
screen_widht = 700
screen = pygame.display.set_mode((screen_widht, screen_height))
player_image = pygame.image.load("media/images/knight/knight iso char_idle_0.png")

global pause, ket
ket = False
pause = False
animation_frames_idle = [
    pygame.image.load("media/images/knight/knight iso char_idle_0.png"),
    pygame.image.load("media/images/knight/knight iso_char_idle_1.png"),
    pygame.image.load("media/images/knight/knight iso char_idle_2.png"),
    pygame.image.load("media/images/knight/knight iso char_idle_3.png"),
]
animation_frames_up = [
    pygame.image.load("media/images/knight/knight iso char_run up_0.png"),
    pygame.image.load("media/images/knight/knight iso char_run up_1.png"),
    pygame.image.load("media/images/knight/knight iso char_run up_2.png"),
    pygame.image.load("media/images/knight/knight iso char_run up_3.png"),
    pygame.image.load("media/images/knight/knight iso char_run up_4.png"),
]
animation_frames_down = [
    pygame.image.load("media/images/knight/knight iso char_run down_0.png"),
    pygame.image.load("media/images/knight/knight iso char_run down_1.png"),
    pygame.image.load("media/images/knight/knight iso char_run down_2.png"),
    pygame.image.load("media/images/knight/knight iso char_run down_3.png"),
    pygame.image.load("media/images/knight/knight iso char_run down_4.png"),
]
animation_frames_left = [
    pygame.image.load("media/images/knight/knight iso char_run left_0.png"),
    pygame.image.load("media/images/knight/knight iso char_run left_1.png"),
    pygame.image.load("media/images/knight/knight iso char_run left_2.png"),
    pygame.image.load("media/images/knight/knight iso char_run left_3.png"),
    pygame.image.load("media/images/knight/knight iso char_run left_4.png"),
]
animation_frames_right = [
    pygame.image.load("media/images/knight/knight iso char_run right_0.png"),
    pygame.image.load("media/images/knight/knight iso char_run right_1.png"),
    pygame.image.load("media/images/knight/knight iso char_run right_2.png"),
    pygame.image.load("media/images/knight/knight iso char_run right_3.png"),
    pygame.image.load("media/images/knight/knight iso char_run right_4.png"),
]

animation_frames_attack_up = [
    pygame.image.load("media/images/knight/Attack_animation_up/attack_up_0.png"),
    pygame.image.load("media/images/knight/Attack_animation_up/attack_up_1.png"),
    pygame.image.load("media/images/knight/Attack_animation_up/attack_up_2.png"),
]
animation_frames_attack_down = [
    pygame.image.load("media/images/knight/Attack_animation_down/attack_down_0.png"),
    pygame.image.load("media/images/knight/Attack_animation_down/attack_down_1.png"),
    pygame.image.load("media/images/knight/Attack_animation_down/attack_down_2.png"),
]

animation_frames_attack_left = [
    pygame.image.load("media/images/knight/Attack_animation_left/attack_left_0.png"),
    pygame.image.load("media/images/knight/Attack_animation_left/attack_left_1.png"),
    pygame.image.load("media/images/knight/Attack_animation_left/attack_left_2.png"),
]
animation_frames_attack_right = [
    pygame.image.load("media/images/knight/Attack_animation_right/attack_right_0.png"),
    pygame.image.load("media/images/knight/Attack_animation_right/attack_right_1.png"),
    pygame.image.load("media/images/knight/Attack_animation_right/attack_right_2.png"),
]
global bg
bg = pygame.image.load("media/images/Map/mapgrass.png")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Set the initial animation frame
        self.image = animation_frames_idle[0]
        self.rect = self.image.get_rect()
        self.speed = 15
        self.rect.x = 300
        self.rect.y = screen_height - self.rect.height - 50
        self.health = 100
        self.defence = 10
        # Store the screen dimensions
        self.screen_width = screen_widht
        self.screen_height = screen_height
        # Create a counter variable to keep track of the animation frame
        self.animation_frame = 0
        self.animation_attack_frame = 0
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        self.standing = True
        self.damage = 5
        self.direction_up = False
        self.direction_down = False
        self.direction_left = False
        self.direction_right = False
        self.attacking = False
        self.x = 21
        self.y = 21

    def animate(self):
        # Update the animation frame
        self.animation_frame += 1
        if not self.standing:
            # If we're moving, use the moving animation frames
            if self.moving_up:
                # If we've reached the end of the moving animation frames, start over
                if self.animation_frame >= len(animation_frames_up):
                    self.animation_frame = 0
                self.image = animation_frames_up[self.animation_frame]
            # Otherwise, use the idle animation frames

            elif self.moving_down:
                # If we've reached the end of the moving animation frames, start over
                if self.animation_frame >= len(animation_frames_down):
                    self.animation_frame = 0
                self.image = animation_frames_down[self.animation_frame]
            # Otherwise, use the idle animation frames

            elif self.moving_left:
                # If we've reached the end of the moving animation frames, start over
                if self.animation_frame >= len(animation_frames_left):
                    self.animation_frame = 0
                self.image = animation_frames_left[self.animation_frame]
            # Otherwise, use the idle animation frames

            if self.moving_right:
                # If we've reached the end of the moving animation frames, start over
                if self.animation_frame >= len(animation_frames_right):
                    self.animation_frame = 0
                self.image = animation_frames_right[self.animation_frame]
            # Otherwise, use the idle animation frames
        else:
            if self.animation_frame >= len(animation_frames_idle):
                self.animation_frame = 0
            self.image = animation_frames_idle[self.animation_frame]

    def attack(self):
        if self.attacking:
            if self.direction_up:
                self.animation_attack_frame += 1
                if self.animation_attack_frame == len(animation_frames_attack_up):
                    self.animation_attack_frame = 0
                    self.direction_up = False
                self.image = animation_frames_attack_up[self.animation_attack_frame]

            elif self.direction_down:
                self.animation_attack_frame += 1
                if self.animation_attack_frame == len(animation_frames_attack_down):
                    self.animation_attack_frame = 0
                    self.direction_down = False

                self.image = animation_frames_attack_down[self.animation_attack_frame]

            elif self.direction_left:
                self.animation_attack_frame += 1
                if self.animation_attack_frame == len(animation_frames_attack_left):
                    self.animation_attack_frame = 0
                    self.direction_left = False

                self.image = animation_frames_attack_left[self.animation_attack_frame]
            elif self.direction_right:
                self.animation_attack_frame += 1
                if self.animation_attack_frame == len(animation_frames_attack_right):
                    self.animation_attack_frame = 0
                    self.direction_right = False
                self.image = animation_frames_attack_right[self.animation_attack_frame]

    def collide_with_enemies(self, enemies):
        global pause
        # Check for collisions between the player and the enemies
        collided_enemies = pygame.sprite.spritecollide(self, enemies, False)
        lvl = False
        # Handle the collisions
        for enemy in collided_enemies:
            if self.attacking:
                enemy.health -= self.damage
                self.attacking = False
                if enemy.health <= 0:
                    lvl = True
                    enemies.remove(enemy)
                    level_2()

        if player.rect.x < 305 and player.rect.y < 10:
            level_3()

    def update(self):
        # Check if the player's position is within the boundaries of the screen
        if self.rect.left < 1:
            self.rect.left = 1
        elif self.rect.right > self.screen_width:
            self.rect.right = self.screen_width

        if self.rect.top < 1:
            self.rect.top = 1
        elif self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height


# ENEMY

enemy_image = pygame.image.load("media/images/enemy/idle/hyena_00_idle.png")

enemy_idle = [
    pygame.image.load("media/images/enemy/idle/hyena_00_idle.png"),
    pygame.image.load("media/images/enemy/idle/hyena_01_idle.png"),
    pygame.image.load("media/images/enemy/idle/hyena_02_idle.png"),
    pygame.image.load("media/images/enemy/idle/hyena_03_idle.png"),
]

enemy_walk = [
    pygame.image.load("media/images/enemy/move/hyena_00_.png"),
    pygame.image.load("media/images/enemy/move/hyena_01_.png"),
    pygame.image.load("media/images/enemy/move/hyena_02_.png"),
    pygame.image.load("media/images/enemy/move/hyena_03_.png"),
    pygame.image.load("media/images/enemy/move/hyena_04_.png"),
    pygame.image.load("media/images/enemy/move/hyena_05_.png"),
]


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_idle[0]
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 30
        self.speed = 4
        self.screen_width = screen_widht
        self.screen_height = screen_height
        self.animation = 0
        self.health = 100
        self.damage = 30
        self.attacking = False

    def move(self):
        self.rect.x += self.speed
        self.rect.y = 100 * self.rect.x / 720

    def update(self):
        # Check if the player's position is within the boundaries of the screen
        if self.rect.left < 1:
            self.rect.left = 1
        elif self.rect.right > self.screen_width - 130:
            self.rect.right = self.screen_width - 130

        if self.rect.top < 1:
            self.rect.top = 1
        elif self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height

        if self.rect.right == self.screen_width - 130:
            self.image = enemy_idle[self.animation % len(enemy_idle)]
        else:
            self.image = enemy_walk[self.animation % len(enemy_walk)]

        self.animation += 1

    def collide_with_player(self, players):
        global pause
        collided_player = pygame.sprite.spritecollide(self, players, False)
        for players in collided_player:
            self.attacking = True
            if self.attacking:
                player.health -= self.damage
                self.attacking = False


# TREES

Tree_image = pygame.image.load("media/images/Map/treee.png")


class Tree(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = Tree_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.animat = 0


colom2_image = pygame.image.load("media/images/Map/colona02.png")


class Colon2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = colom2_image
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 300
        self.anime = 0


colom_image = pygame.image.load("media/images/Map/colona01.png")


class Colon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = colom_image
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 100
        self.anime = 0


Colona2 = Colon2()
Coloni2 = pygame.sprite.Group()
Coloni2.add(Colona2)
Colona = Colon()
Coloni = pygame.sprite.Group()
Coloni.add(Colona)
tree = Tree(250, 120)
tree2 = Tree(450, 450)
trees = pygame.sprite.Group()
trees.add(tree, tree2)
running = True
enemy = Enemy()
enemies = pygame.sprite.Group()
enemies.add(enemy)
player = Player()
players = pygame.sprite.Group()
players.add(player)


def level_2():
    global bg, ket, enemy
    ket = True
    bg = pygame.image.load("media/images/Map/map_lv_2.png")
    player.rect.x = 300
    player.rect.y = screen_height - player.rect.height - 50


def level_3():
    global bg, ket, enemy
    ket = True
    bg = pygame.image.load("media/images/Map/map_lv_3.png")
    player.rect.x = 300
    player.rect.y = screen_height - player.rect.height - 50


# Main game loop
while running:
    prev_pos = (player.rect.x, player.rect.y)
    # Handle events
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        player.rect.y -= player.speed
        player.moving_up = True
        player.moving_down = False
        player.moving_right = False
        player.moving_left = False
        player.standing = False
    elif keys[pygame.K_DOWN]:
        player.rect.y += player.speed
        player.moving_down = True
        player.moving_up = False
        player.moving_right = False
        player.moving_left = False
        player.standing = False
    elif keys[pygame.K_LEFT]:
        player.rect.x -= player.speed
        player.moving_left = True
        player.moving_up = False
        player.moving_down = False
        player.moving_right = False
        player.standing = False
    elif keys[pygame.K_RIGHT]:
        player.rect.x += player.speed
        player.moving_up = False
        player.moving_down = False
        player.moving_left = False
        player.moving_right = True
        player.standing = False
    else:
        player.moving_up = False
        player.moving_down = False
        player.moving_right = False
        player.moving_left = False
        player.standing = True
    if keys[pygame.K_SPACE]:
        player.attacking = True
        if player.moving_up:
            player.direction_up = True
        elif player.moving_down:
            player.direction_down = True
        elif player.moving_left:
            player.direction_left = True
        elif player.moving_right:
            player.direction_right = True
    player.attack()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    pygame.display.flip()
    player.update()
    player.animate()
    # Draw the game objects
    screen.blit(Tree_image, (tree.rect.x, tree.rect.y))
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    if player.health <= 0:
        pause = True
    if pause:
        pygame.time.delay(int(1000 / 60))

    if player.attacking:
        player.attack()
    if not keys:
        screen.blit(player_image, (player.rect.x, player.rect.y))
    if not ket:
        if (
            player.rect.colliderect(tree.rect)
            or player.rect.colliderect(tree2.rect)
            or player.rect.colliderect(Colona.rect)
            or player.rect.colliderect(Colona2.rect)
        ):
            # If there is a collision, prevent the player from moving

            # (e.g., by resetting the player's position)
            player.rect.x = prev_pos[0]  # Keep the player's x position the same
            player.rect.y = prev_pos[1]
        Coloni.draw(screen)
        Coloni2.draw(screen)

    enemy.collide_with_player(players)
    player.collide_with_enemies(enemies)
    enemy.move()
    enemy.update()

    if not ket:
        trees.draw(screen)
    enemies.draw(screen)
    players.draw(screen)

    clock.tick(15)
