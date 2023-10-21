# Pacman Search Project

This project involves running the Pacman game with different search algorithms to find paths through mazes of varying sizes. You can use the provided code to run Pacman in different maze configurations. 

## Getting Started

To get started, you need to have Python and the Pacman codebase set up. If you haven't already, follow the instructions to set up the Pacman project on your local machine.

### Prerequisites

- Python (version 3.6 or higher)
- Pacman codebase

### Running the Project

To run the project with different maze configurations using the SearchAgent, follow these steps:

1. Open your terminal or command prompt.

2. Navigate to the directory where your Pacman codebase is located.

3. Use the following commands to run Pacman with different mazes:
   - move to project folder 
   ```bash
    cd project
   ``` 
   - To run Pacman in the "tinyMaze" configuration:
     ```bash
     python pacman.py -l tinyMaze -p SearchAgent
     ```

   - To run Pacman in the "mediumMaze" configuration:
     ```bash
     python pacman.py -l mediumMaze -p SearchAgent
     ```

   - To run Pacman in the "bigMaze" configuration with a search agent and a search delay of 0.5 seconds:
     ```bash
     python pacman.py -l bigMaze -z 0.5 -p SearchAgent
     ```

## Additional Notes

- You can explore other maze configurations and agent types by modifying the `-l` and `-p` flags in the provided commands.
- Feel free to experiment with different search algorithms and parameters to see how Pacman performs in various scenarios.

