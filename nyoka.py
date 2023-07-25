import tkinter as tk
import random
import time

# Constants
GRID_SIZE = 20
GRID_WIDTH = 600
GRID_HEIGHT = 600
DELAY = 100

class SnakeGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Snake Game")
        self.geometry(f"{GRID_WIDTH}x{GRID_HEIGHT}")
        self.resizable(0, 0)

        self.canvas = tk.Canvas(self, bg="black", width=GRID_WIDTH, height=GRID_HEIGHT)
        self.canvas.pack()

        self.snake = [(0, 0)]
        self.direction = "Right"
        self.food = self.spawn_food()

        self.bind("<KeyPress>", self.on_key_press)

        self.update()

    def on_key_press(self, event):
        key = event.keysym.lower()
        if key in ("up", "down", "left", "right"):
            if self.direction == "Up" and key != "Down":
                self.direction = key.capitalize()
            elif self.direction == "Down" and key != "Up":
                self.direction = key.capitalize()
            elif self.direction == "Left" and key != "Right":
                self.direction = key.capitalize()
            elif self.direction == "Right" and key != "Left":
                self.direction = key.capitalize()

    def spawn_food(self):
        x = random.randint(0, GRID_WIDTH // GRID_SIZE - 1) * GRID_SIZE
        y = random.randint(0, GRID_HEIGHT // GRID_SIZE - 1) * GRID_SIZE
        self.canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill="yellow")
        return x, y

    def move_snake(self):
        head_x, head_y = self.snake[-1]
        if self.direction == "Up":
            new_head = (head_x, head_y - GRID_SIZE)
        elif self.direction == "Down":
            new_head = (head_x, head_y + GRID_SIZE)
        elif self.direction == "Left":
            new_head = (head_x - GRID_SIZE, head_y)
        elif self.direction == "Right":
            new_head = (head_x + GRID_SIZE, head_y)

        self.snake.append(new_head)
        if new_head == self.food:
            self.food = self.spawn_food()
        else:
            self.snake.pop(0)

        self.draw_snake()

    def draw_snake(self):
        self.canvas.delete("snake")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill="green", tags="snake")

    def check_collision(self):
        head_x, head_y = self.snake[-1]
        return head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT or len(set(self.snake)) != len(self.snake)

    def update(self):
        if self.check_collision():
            self.canvas.create_text(
                GRID_WIDTH // 2,
                GRID_HEIGHT // 2,
                text="HII IMEENDA!",
                fill="white",
                font=("Helvetica", 30)
            )
            return

        self.move_snake()

        self.after(DELAY, self.update)

if __name__ == "__main__":
    game = SnakeGame()
    game.mainloop()
