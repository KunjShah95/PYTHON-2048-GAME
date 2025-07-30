# 2048 Game - Windows Desktop Edition

## How to Play
1. Download and extract the `release` folder or the provided zip file.
2. Double-click `2048_Game.exe` to start the game on your Windows laptop or PC.
3. Use the arrow keys to move tiles and combine numbers to reach 2048!

### Controls
- Arrow Keys: Move tiles
- U: Undo last move
- R: Redo move
- ESC: Restart game

## Distribution
- Share the `2048_Game.exe` file or the zipped `release` folder with anyone.
- No Python or installation required—just run the executable.

## System Requirements
- Windows 7 or later
- No installation needed
- ~15 MB disk space

## Troubleshooting
- If Windows Defender warns about the file, click "More info" > "Run anyway" (this is a common false positive for PyInstaller apps).
- If the game doesn't start, try running as administrator or check antivirus settings.

## Files Included
- `2048_Game.exe`: The game executable
- `DISTRIBUTION_README.txt`: Quick start guide
- `Play_2048_Game.bat`: Optional launcher batch file

## Clean Project
Unnecessary files have been removed for easy sharing. Only essential files for running and distributing the game are included in the `release` folder.

Enjoy playing and sharing the 2048 Game!
# 2048 Game - Python Edition

A feature-rich implementation of the classic 2048 puzzle game built with Python and Pygame, featuring score tracking, undo/redo functionality, and persistent high score storage.

![2048 Game](https://img.shields.io/badge/Game-2048-blue)
![Python](https://img.shields.io/badge/Python-3.7+-green)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🎮 Game Overview

2048 is a sliding block puzzle game where the objective is to slide numbered tiles on a grid to combine them and create a tile with the number 2048. This implementation includes modern gaming features like undo/redo functionality and persistent score tracking.

## ✨ Features

### Core Gameplay
- **Classic 2048 Mechanics**: Slide tiles in four directions to combine matching numbers
- **Smooth Animations**: Responsive tile movement with visual feedback
- **Win Condition**: Reach the 2048 tile to win the game
- **Game Over Detection**: Automatic detection when no moves are possible

### Enhanced Features
- **📊 Score Tracking**: Real-time score display with points awarded for tile merges
- **🏆 High Score System**: Persistent high score storage across game sessions
- **↩️ Undo/Redo Functionality**: Revert up to 10 previous moves
- **🎨 Professional UI**: Clean, modern interface with intuitive controls
- **💾 Auto-Save**: Automatic high score saving and loading

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.7 or higher installed on your system.

```bash
python --version
```

### Installation

1. **Clone or download the repository**
   ```
   git clone <repository-url>
   cd python-game
   ```

2. **Install Pygame**
   ```bash
   pip install pygame
   ```

3. **Run the game**
   ```bash
   python main.py
   ```

## 🎯 How to Play

### Basic Controls
- **Arrow Keys**: Move tiles in the corresponding direction
  - ⬅️ **Left Arrow**: Move tiles left
  - ➡️ **Right Arrow**: Move tiles right
  - ⬆️ **Up Arrow**: Move tiles up
  - ⬇️ **Down Arrow**: Move tiles down

### Advanced Controls
- **U Key**: Undo last move (up to 10 moves back)
- **R Key**: Redo previously undone move
- **ESC Key**: Restart the game at any time

### Game Rules
1. Use arrow keys to slide all tiles in one direction
2. When two tiles with the same number touch, they merge into one
3. After each move, a new tile (2 or 4) appears in a random empty spot
4. The goal is to create a tile with the number 2048
5. The game ends when no more moves are possible

### Scoring System
- Points are awarded when tiles merge
- The score equals the value of the newly created tile
- Example: Merging two 64 tiles creates a 128 tile and awards 128 points

## 📁 Project Structure

```
python-game/
│
├── main.py              # Main game file
├── high_score.json      # High score storage (auto-generated)
└── README.md           # This file
```

## 🛠️ Technical Details

### Technologies Used
- **Python 3.7+**: Core programming language
- **Pygame 2.0+**: Graphics and game engine
- **JSON**: High score data persistence

### Key Components
- **Game Grid**: 4x4 matrix for tile management
- **State Management**: Game state tracking for undo/redo
- **Score System**: Real-time scoring with persistent storage
- **Event Handling**: Keyboard input processing
- **Rendering Engine**: Pygame-based graphics rendering

## 🎨 Customization

### Color Scheme
The game uses a warm, professional color palette:
- **Background**: Cream white (#FAF8EF)
- **Tiles**: Gradient from light beige to golden yellow
- **Text**: Dark brown (#776E65)
- **Score Area**: Light gray (#BBB3A0)

### Game Configuration
You can easily modify game parameters in `main.py`:
- **Window Size**: Adjust `WIDTH` and `HEIGHT` constants
- **Grid Size**: Modify the 4x4 grid dimensions
- **Tile Colors**: Customize the `TILE_COLORS` dictionary
- **Fonts**: Change font styles and sizes

## 🏆 High Score System

The game automatically tracks and saves your highest score:
- High scores are stored in `high_score.json`
- Scores persist between game sessions
- Automatic saving when achieving new high scores
- Display of current and high scores during gameplay

## 🔄 Undo/Redo System

Advanced state management allows players to:
- **Undo**: Revert up to 10 previous moves
- **Redo**: Restore undone moves
- **Smart History**: Automatic state saving before each move
- **Memory Efficient**: Limited history to prevent memory issues

## 🚨 Troubleshooting

### Common Issues

**Game won't start:**
- Ensure Python 3.7+ is installed
- Install Pygame: `pip install pygame`
- Check file permissions

**High score not saving:**
- Ensure write permissions in the game directory
- Check if `high_score.json` can be created

**Performance issues:**
- Close other applications to free up system resources
- Ensure your system meets minimum requirements

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:
- Report bugs and issues
- Suggest new features
- Improve documentation
- Submit pull requests

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the original 2048 game by Gabriele Cirulli
- Built with the excellent Pygame library
- Thanks to the Python community for continuous support

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review the code comments in `main.py`
3. Create an issue in the repository

---

**Enjoy playing 2048! 🎉**

*Challenge yourself to reach the 2048 tile and beyond!*
