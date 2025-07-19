# Glider Visualization

A 3D visualization of Conway's Game of Life 
- Rendered in Three.js and driven by a Flask backend. 
- Designed for modular clarity, performance testing, and integration with recursive pattern engines.
- Architected for future expansion integrating AI based projects.

## Features

- Real-time simulation of Game of Life
- 3D grid rendered via Three.js
- RESTful control endpoints (`/start`, `/stop`, `/tick`, `/clear`, etc.)
- Live polling frontend state
- Modular Python backend logic
- Pattern reset on Clear

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

## Setup

```bash
# Run the Server

# Set up environment (only once)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Start the server
python runner.py
```

## Run the Server

```bash
flask run
```
Then visit: `http://localhost:5000`

## File Layout

```
glider/
├── core/
│   ├── engine.py
│   ├── glider_state_adapter.py
│   └── tick_controller.py
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       ├── render3d/
│       │   ├── init_grid.js
│       │   ├── init_scene.js
│       │   └── update_loop.js
│       └── ui/
│           ├── buttons.js
│           └── events.js
│       ├── bootstrap_combined.js
│       ├── render.js
│       ├── render3d.js
│       ├── three.core.js
│       └── three.module.js
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── index_3d.html
│   ├── index_combined.html
│   └── index_controls.html
├── __init__.py
├── models.py
├── routes.py
├── routes_3d.py
└── routes_combined.py
├── websocket.py
│
├── .env
├── .gitignore
├── Makefile
├── README.md
├── readme_glider_project.md
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

- AI shape injection and saving
- AI training based on shape movement
- 3rd axis in Z direction
