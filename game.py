import random
import curses
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

    def move(self, direction: Tuple[int, int], grid: List[List[GameObject]]):
        new_position = (self.position[0] + direction[0], self.position[1] + direction[1])
        if self.can_move(new_position, grid):
            self.position = new_position

    def can_move(self, position: Tuple[int, int], grid: List[List[GameObject]]) -> bool:
        return (0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0])
                and not isinstance(grid[position[0]][position[1]], Block))

@dataclass
class Enemy(GameObject):
    health: int

    def move_randomly(self, grid: List[List[GameObject]]):
        possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(possible_moves)
        for move in possible_moves:
            new_position = (self.position[0] + move[0], self.position[1] + move[1])
            if self.can_move(new_position, grid):
                self.position = new_position
                break

    def can_move(self, position: Tuple[int, int], grid: List[List[GameObject]]) -> bool:
        return (0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0])
                and not isinstance(grid[position[0]][position[1]], Block))

class Block(GameObject):
    pass

@dataclass
class Medicine(GameObject):
    healing_amount: int

# Función para imprimir la matriz
def print_grid(grid: List[List[GameObject]], player: Player, enemies: List[Enemy], medicine: Medicine, blocks: List[Block], screen):
    screen.clear()
    for i in range(len(grid)):
        row = []
        for j in range(len(grid[i])):
            if player.position == (i, j):
                row.append("P")  # Jugador
            elif any(enemy.position == (i, j) for enemy in enemies):
                row.append("E")  # Enemigo
            elif medicine.position == (i, j):
                row.append("M")  # Medicina
            elif any(block.position == (i, j) for block in blocks):
                row.append("B")  # Bloque
            else:
                row.append(".")  # Espacio vacío
        screen.addstr(" ".join(row) + "\n")
    screen.refresh()

# Función para inicializar la grilla con posiciones aleatorias
def initialize_grid(size: int, num_blocks: int, num_enemies: int):
    grid = [[None for _ in range(size)] for _ in range(size)]
    
    def random_position():
        return (random.randint(0, size - 1), random.randint(0, size - 1))
    
    # Colocar jugador
    player = Player(health=100, lives=3, position=random_position(), inventory=[])
    
    # Colocar medicina
    medicine = Medicine(position=random_position(), healing_amount=25)
    
    # Colocar bloques
    blocks = [Block(position=random_position()) for _ in range(num_blocks)]
    
    # Colocar enemigos
    enemies = [Enemy(health=50, position=random_position()) for _ in range(num_enemies)]
    
    return grid, player, enemies, medicine, blocks

# Función principal del juego
def main(screen):
    curses.curs_set(0)
    size = 10
    num_blocks = 5
    num_enemies = 2
    
    grid, player, enemies, medicine, blocks = initialize_grid(size, num_blocks, num_enemies)
    
    while player.lives > 0:
        print_grid(grid, player, enemies, medicine, blocks, screen)
        
        # Leer tecla de movimiento
        key = screen.getch()
        direction = (0, 0)
        
        if key == curses.KEY_UP:
            direction = (-1, 0)
        elif key == curses.KEY_DOWN:
            direction = (1, 0)
        elif key == curses.KEY_LEFT:
            direction = (0, -1)
        elif key == curses.KEY_RIGHT:
            direction = (0, 1)
        
        player.move(direction, grid)
        
        # Mover enemigos
        for enemy in enemies:
            enemy.move_randomly(grid)

        # Pausar un poco para ver el movimiento
        curses.napms(200)
        
if __name__ == "__main__":
    curses.wrapper(main)
