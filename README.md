# Snake Game

#### Video Demo: [Youtube](https://youtu.be/qTXU4N7HciE)

#### Description:
This project is a Python implementation of the classic Snake game, developed using the Pygame library. The player controls a snake that navigates around the screen, consuming targets to grow longer. The objective is to grow the snake as long as possible without running into the screen's edges or the snake’s own body.

The game features multiple difficulty levels that affect the speed at which the snake moves. A scoring system tracks the number of targets consumed by the snake, which is displayed in real-time at the top of the screen. The game concludes with a "Game Over" screen if the player loses, from which they can choose to play again, return to the main menu, or exit the game.

### Files in the Project:
1. **main.py**:
   - **Purpose**: The main entry point for the game. It contains the primary game loop and handles the initialization of the game, menus, and other essential functions.
   - **Key Functions**:
     - `menu()`: Displays the main menu where players can start the game, select the difficulty, or quit.
     - `play(level=10)`: The core gameplay function that starts a new game with the selected difficulty level.
     - `difficulty()`: Allows players to choose the difficulty level of the game.
     - `game_over(speed)`: Displays the "Game Over" screen with options to replay, return to the main menu, or quit.

2. **snake.py**:
   - **Purpose**: Manages the snake's logic, including its movement and interactions with the game environment.
   - **Key Functions**:
     - `snake_init()`: Initializes the snake's starting position, size, and color.
     - `check_direction(direction, x, y)`: Updates the snake’s position based on the current direction of movement.
     - `target_init(rect_x, rect_y)`: Initializes the target (food) in a random position on the screen, ensuring it does not overlap with the snake's current position.

3. **utils.py**:
   - **Purpose**: Contains utility functions that support the main gameplay, including random position generation and difficulty checks.
   - **Key Functions**:
     - `random_starting_position()`: Generates a random valid starting position for the snake or target.
     - `check_difficulty(level)`: Adjusts the speed of the snake based on the selected difficulty level.

4. **README.md**:
   - **Purpose**: This document provides a comprehensive overview of the project, including descriptions of the game's features, files, and design choices.

5. **keys.png**:
   - **Purpose**: An image used in the main menu screen as a visual guide for players.

### Design Choices:
One of the key design decisions involved the structure of the game loop and how to handle different states, such as the main menu, gameplay, and game over screens. Initially, I debated whether to use a more object-oriented approach by creating classes for the snake, game state, and target. However, I chose a more function-based approach to keep the structure simple and maintainable, given the relatively small scope of the project.

Another consideration was how to implement the collision detection logic. I opted to use a straightforward list structure to represent the snake's body segments, iterating through the list to check for collisions. This method was chosen for its simplicity and clarity, which made the code easier to debug and maintain.

Regarding the difficulty settings, I decided to allow the player to choose between three fixed levels: easy, medium, and hard. The snake's speed increases with difficulty, providing a progressively challenging experience. I considered implementing a dynamic difficulty system that would increase the speed as the player’s score increased, but I opted to keep it simple to ensure the game remained accessible to all players.

### Conclusion:
This project was both a learning experience and an opportunity to revisit a classic game from a developer's perspective. By implementing this game, I gained a deeper understanding of game loops, event handling, and collision detection. The project also reinforced my understanding of Python and Pygame, particularly in creating interactive graphical applications.

This project was created by DirtyRat44 as part of the CS50x course.
