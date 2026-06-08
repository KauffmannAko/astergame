# Asteroid Game

A small Asteroids-style arcade game built with Python and Pygame.

You control a triangular player ship, dodge incoming asteroids, and fire shots to destroy them. The project is a work in progress and is being built step by step as a learning project.

## Features

- Player movement and rotation
- Shooting with cooldown
- Random asteroid spawning
- Collision detection
- Game over when the player hits an asteroid
- Shot and asteroid collision handling
- JSONL debug/event logging

## Controls

| Key | Action |
| --- | --- |
| Up Arrow | Move forward |
| Down Arrow | Move backward |
| Left Arrow | Rotate left |
| Right Arrow | Rotate right |
| Space | Shoot |
| Close Window | Quit game |

## Requirements

- Python 3.13+
- Pygame 2.6.1

## Installation


```bash
Using uv: uv sync

Or with pip: pip install pygame==2.6.1
```
## Running the Game


```bash
python3 main.py

        Or 

uv run python main.py
```


## Project Structure
```bash
main.py             # Game loop and sprite group setup
player.py           # Player ship behavior
asteroid.py         # Asteroid behavior
asteroidfield.py    # Asteroid spawning
shot.py             # Bullet behavior
circleshape.py      # Base class for circular game objects
constants.py        # Game constants
logger.py           # Debug and event logging
```

# Roadmap

- [ ] Add a scoring system
- [ ] Implement multiple lives and respawning
- [ ] Add an explosion effect for the asteroids
- [ ] Add acceleration to the player movement
- [ ] Make the objects wrap around the screen instead of disappearing
- [ ] Add a background image
- [ ] Create different weapon types
- [ ] Make the asteroids lumpy instead of perfectly round
- [ ] Make the ship have a triangular hit box instead of a circular one
- [ ] Add a shield power-up
- [ ] Add a speed power-up
- [ ] Add bombs that can be dropped

# Logs
- The game can write debug/event logs to:

```bash
game_state.jsonl
game_events.jsonl
```