import pygame
import random
import sys
import json
import os
import copy

pygame.init()
WIDTH, HEIGHT = 400, 500  # Increased height for score display
TILE_SIZE = WIDTH // 4
FONT = pygame.font.SysFont("comicsansms", 40)
SCORE_FONT = pygame.font.SysFont("comicsansms", 24)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048 Game")

WHITE = (250, 248, 239)
BLACK = (119, 110, 101)
GRAY = (187, 173, 160)
SCORE_BG = (187, 173, 160)
TILE_COLORS = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

# Game state variables
grid = [[0] * 4 for _ in range(4)]
score = 0
high_score = 0
move_history = []  # For undo/redo functionality
redo_history = []
SCORE_FILE = "high_score.json"

def load_high_score():
    """Load high score from file"""
    global high_score
    try:
        if os.path.exists(SCORE_FILE):
            with open(SCORE_FILE, 'r') as f:
                data = json.load(f)
                high_score = data.get('high_score', 0)
    except:
        high_score = 0

def save_high_score():
    """Save high score to file"""
    try:
        with open(SCORE_FILE, 'w') as f:
            json.dump({'high_score': high_score}, f)
    except:
        pass

def save_game_state():
    """Save current game state for undo functionality"""
    global move_history, redo_history
    state = {
        'grid': copy.deepcopy(grid),
        'score': score
    }
    move_history.append(state)
    # Clear redo history when new move is made
    redo_history.clear()
    # Limit history to last 10 moves to save memory
    if len(move_history) > 10:
        move_history.pop(0)

def undo_move():
    """Undo the last move"""
    global grid, score, move_history, redo_history
    if move_history:
        # Save current state for redo
        current_state = {
            'grid': copy.deepcopy(grid),
            'score': score
        }
        redo_history.append(current_state)
        
        # Restore previous state
        previous_state = move_history.pop()
        grid = previous_state['grid']
        score = previous_state['score']
        return True
    return False

def redo_move():
    """Redo the last undone move"""
    global grid, score, move_history, redo_history
    if redo_history:
        # Save current state for undo
        current_state = {
            'grid': copy.deepcopy(grid),
            'score': score
        }
        move_history.append(current_state)
        
        # Restore redo state
        redo_state = redo_history.pop()
        grid = redo_state['grid']
        score = redo_state['score']
        return True
    return False

def add_tile():
    empty = [(r, c) for r in range(4) for c in range(4) if grid[r][c] == 0]
    if empty:
        r, c = random.choice(empty)
        grid[r][c] = 2 if random.random() < 0.9 else 4

def draw_grid():
    screen.fill(WHITE)
    
    # Draw score area
    score_area = pygame.Rect(0, 0, WIDTH, 100)
    pygame.draw.rect(screen, SCORE_BG, score_area)
    
    # Draw current score
    score_text = SCORE_FONT.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (20, 20))
    
    # Draw high score
    high_score_text = SCORE_FONT.render(f"High Score: {high_score}", True, BLACK)
    screen.blit(high_score_text, (20, 50))
    
    # Draw controls
    controls_text = SCORE_FONT.render("U: Undo | R: Redo | ESC: Restart", True, BLACK)
    screen.blit(controls_text, (20, 75))
    
    # Draw game grid (offset by 100 pixels down for score area)
    for r in range(4):
        for c in range(4):
            val = grid[r][c]
            rect = pygame.Rect(c * TILE_SIZE, r * TILE_SIZE + 100, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, TILE_COLORS.get(val, (60, 58, 50)), rect)
            pygame.draw.rect(screen, BLACK, rect, 2)  # Border
            if val:
                text = FONT.render(str(val), True, BLACK)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)
    pygame.display.update()

def compress(row):
    new_row = [num for num in row if num != 0]
    new_row += [0] * (4 - len(new_row))
    return new_row

def merge(row):
    global score
    for i in range(3):
        if row[i] == row[i + 1] and row[i] != 0:
            row[i] *= 2
            score += row[i]  # Add to score when tiles merge
            row[i + 1] = 0
    return row

def move_left():
    save_game_state()  # Save state before move
    moved = False
    for i in range(4):
        row = compress(grid[i])
        merged = merge(row)
        new_row = compress(merged)
        if grid[i] != new_row:
            moved = True
            grid[i] = new_row
    return moved

def move_right():
    save_game_state()  # Save state before move
    moved = False
    for i in range(4):
        row = list(reversed(grid[i]))
        row = compress(row)
        merged = merge(row)
        new_row = list(reversed(compress(merged)))
        if grid[i] != new_row:
            moved = True
            grid[i] = new_row
    return moved

def move_up():
    save_game_state()  # Save state before move
    moved = False
    for c in range(4):
        col = [grid[r][c] for r in range(4)]
        col = compress(col)
        col = merge(col)
        col = compress(col)
        for r in range(4):
            if grid[r][c] != col[r]:
                moved = True
                grid[r][c] = col[r]
    return moved

def move_down():
    save_game_state()  # Save state before move
    moved = False
    for c in range(4):
        col = [grid[r][c] for r in range(4)]
        col = list(reversed(col))
        col = compress(col)
        col = merge(col)
        col = compress(col)
        col = list(reversed(col))
        for r in range(4):
            if grid[r][c] != col[r]:
                moved = True
                grid[r][c] = col[r]
    return moved

def game_over():
    for r in range(4):
        for c in range(4):
            if grid[r][c] == 0:
                return False
            if c < 3 and grid[r][c] == grid[r][c + 1]:
                return False
            if r < 3 and grid[r][c] == grid[r + 1][c]:
                return False
    return True

def show_game_over():
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))
    over_text = FONT.render("Game Over", True, WHITE)
    screen.blit(over_text, over_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 20)))
    
    final_score_text = SCORE_FONT.render(f"Final Score: {score}", True, WHITE)
    screen.blit(final_score_text, final_score_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 20)))
    
    restart_text = SCORE_FONT.render("Press ESC to restart", True, WHITE)
    screen.blit(restart_text, restart_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 50)))
    
    pygame.display.update()

def reset_game():
    """Reset the game to initial state"""
    global grid, score, move_history, redo_history
    grid = [[0] * 4 for _ in range(4)]
    score = 0
    move_history.clear()
    redo_history.clear()
    add_tile()
    add_tile()

def main():
    global high_score
    load_high_score()  # Load high score at start
    reset_game()  # Initialize game
    running = True
    game_over_state = False
    clock = pygame.time.Clock()

    while running:
        draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if score > high_score:
                    high_score = score
                    save_high_score()
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Restart game
                    if score > high_score:
                        high_score = score
                        save_high_score()
                    reset_game()
                    game_over_state = False
                    continue
                
                if game_over_state:
                    continue
                
                moved = False
                if event.key == pygame.K_LEFT:
                    moved = move_left()
                elif event.key == pygame.K_RIGHT:
                    moved = move_right()
                elif event.key == pygame.K_UP:
                    moved = move_up()
                elif event.key == pygame.K_DOWN:
                    moved = move_down()
                elif event.key == pygame.K_u:
                    # Undo move
                    if undo_move():
                        draw_grid()
                    continue
                elif event.key == pygame.K_r:
                    # Redo move
                    if redo_move():
                        draw_grid()
                    continue

                if moved:
                    add_tile()
                    draw_grid()
                    
                    # Update high score if current score is higher
                    if score > high_score:
                        high_score = score
                        save_high_score()
                    
                    if game_over():
                        show_game_over()
                        game_over_state = True

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()