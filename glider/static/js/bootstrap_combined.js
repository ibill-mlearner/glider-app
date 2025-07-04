// glider/static/js/bootstrap_combined.js

import { scene, camera, renderer, initScene } from './render3d/init_scene.js';
import { initGrid, cubes } from './render3d/init_grid.js';
import { createButtonBar } from './ui/buttons.js';
import { attachButtonHandlers } from './ui/events.js';

let lastTime = 0;
let liveCells = new Set();

const gridW = 50;
const gridH = 30;
const targetFPS = 20;
const frameInterval = 1000 / targetFPS;


initScene();
initGrid(scene, gridW, gridH);

// insert renderer canvas at end of body
document.body.appendChild(renderer.domElement);

// build control buttons
createButtonBar();

// Wire handlers to backend control routes
attachButtonHandlers({
    onStart: () => fetch('/api/start', { method: 'POST' }),
    onStop:  () => fetch('/api/stop',  { method: 'POST' }),
    onStep:  () => fetch('/api/step',  { method: 'POST' })
    // onClear can be added later
});
startPolling();
// -------------------------------- live state polling --------------------------------
// async function fetchState() {
//     const res = await fetch('/api/state');
//     const data = await res.json();
//     return new Set(data.gliders?.flatMap(g => g.cells).map(([x, y]) => `${x},${y}`) || []);
// }

function startPolling(interval = 500) {
    async function poll() {
        try {
            const res = await fetch('/api/state');
            const data = await res.json();
            liveCells = new Set(
                data.gliders?.flatMap(g => g.cells).map(([x, y]) => `${x},${y}`) || []
            );
        } catch (err) {
            console.warn("Polling error:", err);
        } finally {
            setTimeout(poll, interval);
        }
    }
    poll();
}

async function animate(timestamp) {
    requestAnimationFrame(animate);

    if (timestamp - lastTime < frameInterval) return;
    lastTime = timestamp;

    cubes.forEach((cube, i) => {
        const x = i % gridW;
        const y = Math.floor(i / gridW);
        const key = `${x},${y}`;
        cube.material.color.setHex(liveCells.has(key) ? 0x00ff00 : 0x222222);
    });

    renderer.render(scene, camera);
}
animate();