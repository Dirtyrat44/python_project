# Snake Game

## Description

This project is a Python implementation of the classic **Snake** game, developed using the Pygame library. The player controls a snake that navigates the screen, consuming targets (food) to grow longer. The goal is to grow the snake as long as possible without colliding with the screen edges or the snake's own body.

The game offers multiple difficulty levels that affect the snake's speed, and a scoring system tracks the number of targets consumed. The game ends with a "Game Over" screen if the snake collides, where players can choose to replay, return to the main menu, or quit.

## Main Features

- **Dynamic Gameplay**: Real-time snake movement and food consumption.
- **Difficulty Levels**: Choose between easy, medium, and hard, affecting the snake's speed.
- **Score Display**: The player's score is shown during gameplay.
- **Game Over Screen**: Allows restarting the game or returning to the main menu.

## Files Overview

- **`project.py`**: Entry point of the game. Manages the game loop, menu, difficulty selection, and main gameplay.
- **`test_project.py`**: Contains tests or additional functionality to validate and improve the game mechanics.
- **`requirements.txt`**: Lists all the dependencies required to run the project, including Pygame.
- **`keys.png`**: Image used in the main menu as a visual guide for the player.
- **`README.md`**: This file, providing an overview of the project.

## Design Decisions

This project uses a function-based approach for simplicity and maintainability, with clear separation between game states (menu, gameplay, game over). The snake is represented as a list of segments, and the game includes a simple collision detection mechanism. Fixed difficulty levels provide different gameplay experiences, offering a balance between challenge and accessibility.

## Conclusion

This project was a great opportunity to explore game development concepts, such as game loops, event handling, and collision detection. It also helped reinforce my Python and Pygame skills. The Snake Game was developed as part of the CS50x course by **DirtyRat44**.
