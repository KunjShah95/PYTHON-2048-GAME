# 2048 Game - Distribution Package

## What's Included

- **2048_Game.exe** - The main game executable (standalone, no installation required)
- **DISTRIBUTION_README.txt** - Quick start guide for users
- **README.md** - Full project documentation
- **requirements.txt** - Python dependencies (for developers)

## How to Play

1. **Double-click** on `2048_Game.exe` to start the game
2. Use **arrow keys** to move tiles
3. Combine tiles with the same number to reach 2048!

## Controls

- **Arrow Keys** - Move tiles (Up, Down, Left, Right)
- **U** - Undo last move
- **R** - Redo move
- **ESC** - Restart game

## System Requirements

- Windows 7 or later
- No additional software installation required
- ~15 MB disk space

## Troubleshooting

### Windows Defender Warning
If Windows Defender flags the executable as suspicious:
1. This is a false positive common with PyInstaller executables
2. Click "More info" → "Run anyway"
3. Or add an exception in Windows Defender

### Game Won't Start
1. Make sure you have sufficient disk space
2. Try running as administrator
3. Check if antivirus is blocking the file

## Distribution

This executable can be freely shared and distributed. No installation required - just copy the .exe file and run!

## Technical Details

- Built with Python 3.13.5
- Uses Pygame 2.6.1 for graphics
- Created with PyInstaller 6.14.2
- Self-contained executable (no external dependencies)

Enjoy the game!
