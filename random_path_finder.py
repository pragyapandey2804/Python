import curses
from curses import wrapper
import random
import time

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [["🔥" for _ in range(self.width)] for _ in range(self.height)]  # Initially fully blocked with fire emoji
        self.start_pos = (random.randint(1, self.height - 2), random.randint(1, self.width - 2))
        self.end_pos = (random.randint(1, self.height - 2), random.randint(1, self.width - 2))

    def generate_maze(self, stdscr):
        BLUE = curses.color_pair(1)

        # Display the maze fully blocked with fire emojis
        stdscr.clear()
        self.print_maze(stdscr, display_fire=True)
        stdscr.refresh()
        time.sleep(1)  # Pause to let the user see the initial maze

        # Slowly carve out the maze by setting random positions to empty space
        for i in range(1, self.height - 1):
            for j in range(1, self.width - 1):
                if random.random() > 0.3:
                    self.maze[i][j] = " "  # Carve out an empty space
                
                stdscr.clear()
                self.print_maze(stdscr)
                stdscr.refresh()
                time.sleep(0.05)  # Pause to visualize the formation of the maze

        # Set the start and end positions after the maze is generated
        self.maze[self.start_pos[0]][self.start_pos[1]] = "O"
        self.maze[self.end_pos[0]][self.end_pos[1]] = "X"
        stdscr.clear()
        self.print_maze(stdscr)
        stdscr.refresh()

    def print_maze(self, stdscr, path=[], highlight_path=False, display_fire=False):
        BLUE = curses.color_pair(1)
        RED = curses.color_pair(2)
        GREEN = curses.color_pair(3) if highlight_path else RED

        for i, row in enumerate(self.maze):
            for j, value in enumerate(row):
                if (i, j) in path:
                    stdscr.addstr(i, j*2, "X", GREEN)  # Highlight the path in green
                else:
                    stdscr.addstr(i, j*2, value, BLUE)

        # Display start and end coordinates below the maze
        stdscr.addstr(self.height + 1, 0, f"Start (O): {self.start_pos}", curses.color_pair(1))
        stdscr.addstr(self.height + 2, 0, f"End (X): {self.end_pos}", curses.color_pair(1))

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.start = self.maze.start_pos

    def solve_maze(self, stdscr):
        q = []
        q.append((self.start, [self.start]))  # Queue with (current_position, path_so_far)
        visited = set()

        while q:
            current_pos, path = q.pop(0)
            row, col = current_pos

            stdscr.clear()
            self.maze.print_maze(stdscr, path)
            stdscr.refresh()
            time.sleep(0.2)

            if self.maze.maze[row][col] == "X":
                return path  # Return the shortest path
            
            neighbors = self._find_neighbors(row, col)
            for neighbor in neighbors:
                r, c = neighbor
                if neighbor in visited or self.maze.maze[r][c] == "🔥":
                    continue

                new_path = path + [neighbor]
                q.append((neighbor, new_path))
                visited.add(neighbor)

    def _find_neighbors(self, row, col):
        neighbors = []
        if row > 0:  # UP
            neighbors.append((row - 1, col))
        if row + 1 < len(self.maze.maze):  # DOWN
            neighbors.append((row + 1, col))
        if col > 0:  # LEFT
            neighbors.append((row, col - 1))
        if col + 1 < len(self.maze.maze[0]):  # RIGHT
            neighbors.append((row, col + 1))
        return neighbors

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    width, height = 15, 15  # Adjusted to be more square-like
    maze = Maze(width, height)
    maze.generate_maze(stdscr)
    solver = MazeSolver(maze)
    path = solver.solve_maze(stdscr)
    
    stdscr.clear()
    maze.print_maze(stdscr, path, highlight_path=True)
    stdscr.refresh()
    stdscr.getch()

wrapper(main)

