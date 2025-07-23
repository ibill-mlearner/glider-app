# Glider Visualization

### Conway's Game of Life rules.
   - Each cell has 8 neighbors (adjacent horizontally, vertically, and diagonally).
   - A live cell survives if it has 2 or 3 live neighbors; otherwise it dies.
   - A dead cell becomes alive only if it has exactly 3 live neighbors.
   - This function counts the number of live neighbors around a given cell (x, y).

A 3D visualization of Conway's Game of Life 
- Rendered in Three.js and driven by a Flask backend. 
- Designed for modular clarity, performance testing, and integration with recursive pattern engines.
- Architected for future expansion integrating AI based projects.

## Features

- 3D grid rendered via Three.js
- Live polling frontend state
- Pattern reset on Clear and Rebasing

- The project includes a real-time simulation of Conway's Game of Life powered by logic in `glider/core/engine.py`.
- It renders a 3D grid using Three.js modules located in `static/js/render3d/`.
- Interaction is handled through a set of RESTful control endpoints (`/api/start`, `/api/stop`, `/api/tick`, `/api/clear`, `/api/state`) exposed via Flask.
- Frontend state updates are driven by live polling mechanisms implemented in `bootstrap_combined.js`.
- The backend is modular, with core responsibilities split across `engine.py`, `tick_controller.py`, and `app.py`.
- The clear action resets the simulation pattern by calling `engine.reset()` with a shape and default offset, immediately visible after the next update cycle.


## Requirements

- Python 3.10+
- pip / virtualenv
- Compatible browser (WebGL support)
_________________________________________________________________________________________
## Running the Server

### 1. Set up the environment (one-time setup)

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
```

#### Activate the environment:

- **PowerShell (Windows):**

  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```

- **Command Prompt (Windows):**

  ```cmd
  .venv\Scripts\activate.bat
  ```

- **Git Bash / WSL / macOS / Linux:**

  ```bash
  source .venv/bin/activate
  ```

Then install dependencies:

```bash
pip install -r requirements.txt
```

---

### 2. Start the server

```bash
python runner.py
```

_________________________________________________________________________________________


Then visit: `http://localhost:5000` or click the IP address server flashes when starting.

## File Layout

```
glider/
├── core/
│   ├── engine.py
│   ├── engine_3d.py
│   ├── glider_state_adapter.py
│   └── tick_controller.py
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       ├── render2d/
│       │   ├── init_grid.js
│       │   ├── init_scene.js
│       ├── render3d/
│       │   ├── init_grid.js
│       │   ├── init_scene.js
│       └── ui/
│           ├── buttons.js
│           └── events.js
│       ├── bootstrap_2d.js
│       ├── bootstrap_3d.js
│       ├── OrbitControls.js
│       ├── three.core.js
│       └── three.module.js
├── templates/
│   ├── 2dplane.html
│   ├── 3dplane.html
│   └── base.html
├── __init__.py
├── models.py
├── routes_combined.py
├── resources.py
├── shapes.py
├── .env
├── .gitignore
├── README.md
└── runner.py
```

## Clear Function Logic

`/api/clear` invokes the tick controller, which calls engine.reset(pattern), placing a pattern at a default offset. The state is visible in the next poll cycle.
`/api/start` launches the background tick loop via tick_controller.start().
`/api/stop` halts the background loop through tick_controller.stop().
`/api/tick` steps the simulation forward by one frame using tick_controller.step_once().
`/api/state` returns the current engine grid for frontend rendering.

## Status

This project is stable and functional. Future updates may include:

- CUDA core rendering for 3d engine
- AI shape injection and saving
- AI training based on shape movement
