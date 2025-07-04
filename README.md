# Glider Visualization

A Flask-based simulation platform for modeling and rendering glider structures derived from cellular automata (e.g. Conway’s Game of Life).

## Features

- Modular backend engine using the Flask app factory pattern
- Real-time visualization with HTML5 Canvas (Three.js-ready)
- API and WebSocket scaffolding for remote simulation control
- Pattern collision, motion tracking, and deterministic tick logic
- Version controlled via GitHub with Docker deployment support

## Development Setup

1. Clone the repository
2. Create a virtual environment and install dependencies
3. Run the app using the runner:
   ```bash
   python -m runner