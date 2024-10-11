import random
import pygame
from pygame.locals import *
from dataclasses import dataclass
from typing import List, Tuple

# Definición de clases
@dataclass
class GameObject:
    position: Tuple[int, int]

@dataclass
class Player(GameObject):
    health: int
    lives: int
    inventory: List[str]

    def move(self, direction: Tuple[int, int], grid_size: int):
        new_position = (self.position[0] + direction[0], self.position[1] + direction[1])
        if self.can_move(new_position, grid_size):
            self.position = new_position

    def can_move(self, position: Tuple[int, int], grid_size: int) -> bool:
        return (0 <= position[0] < grid_size and 0 <= position[1] < grid_size)

@dataclass
class Enemy(GameObject):
    health: int

    def move_randomly(self, grid_size: int):
        possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(possible_moves)
        for move in possible_moves:
            new_position = (self.position[0] + move[0], self.position[1] + move[1])
            if self.can_move(new_position, grid_size):
                self.position = new_position
                break

    def can_move(self, position: Tuple[int, int], grid_size: int) -> bool:
        return (0 <= position[0] < grid_size and 0 <= position[1] < grid_size)

@dataclass
class Medicine(GameObject):
    healing_amount: int

class Block(GameObject):
    pass

# Inicializar pygame y el juego
def initialize_game():
    pygame.init()
    screen_size = 500
    grid_size = 10
    block_size = screen_size // grid_size
    screen = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption('Juego con pygame')
    
    return screen, grid_size, block_size

# Función para inicializar la grilla con posiciones aleatorias
def initialize_grid(grid_size: int, num_blocks: int, num_enemies: int):
    def random_position():
        return (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))

    # Colocar jugador

    player = Player(health=100, lives=3, position=random_position(), inventory=[])
    
    # Colocar medicina
    medicine = Medicine(position=random_position(), healing_amount=25)
    
    # Colocar bloques
    blocks = [Block(position=random_position()) for _ in range(num_blocks)]
    
    # Colocar enemigos
    enemies = [Enemy(health=50, position=random_position()) for _ in range(num_enemies)]
    
    return player, enemies, medicine, blocks

# Función para dibujar la grilla
def draw_grid(screen, grid_size, block_size, player, enemies, medicine, blocks):
    screen.fill((0, 0, 0))
    for x in range(0, grid_size * block_size, block_size):
        for y in range(0, grid_size * block_size, block_size):
            pygame.draw.rect(screen, (50, 50, 50), (x, y, block_size, block_size), 1)

    # Dibujar jugador
    pygame.draw.rect(screen, (0, 255, 0), (player.position[1] * block_size, player.position[0] * block_size, block_size, block_size))
    
    # Dibujar enemigos
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), (enemy.position[1] * block_size, enemy.position[0] * block_size, block_size, block_size))
    
    # Dibujar medicina
    pygame.draw.rect(screen, (0, 0, 255), (medicine.position[1] * block_size, medicine.position[0] * block_size, block_size, block_size))
    
    # Dibujar bloques
    for block in blocks:
        pygame.draw.rect(screen, (128, 128, 128), (block.position[1] * block_size, block.position[0] * block_size, block_size, block_size))
    
    pygame.display.update()

# Función principal del juego
def main():
    screen, grid_size, block_size = initialize_game()
    player, enemies, medicine, blocks = initialize_grid(grid_size, num_blocks=5, num_enemies=2)
    
    running = True
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        direction = (0, 0)
        
        if keys[pygame.K_UP]:
            direction = (-1, 0)
        elif keys[pygame.K_DOWN]:
            direction = (1, 0)
        elif keys[pygame.K_LEFT]:
            direction = (0, -1)
        elif keys[pygame.K_RIGHT]:
            direction = (0, 1)
        
        player.move(direction, grid_size)
        
        # Mover enemigos
        for enemy in enemies:
            enemy.move_randomly(grid_size)
        
        # Dibujar la grilla
        draw_grid(screen, grid_size, block_size, player, enemies, medicine, blocks)
        
        # Limitar la tasa de frames por segundo
        clock.tick(10)
    
    pygame.quit()

if __name__ == "__main__":
    main()
    
