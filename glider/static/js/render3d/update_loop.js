import { renderer, camera, scene } from './init_scene.js';
import { cubes } from './init_grid.js';

const gridW = 50;
const gridH = 30;

async function fetchState() {
    const res = await fetch('/api/state');
    const data = await res.json();
    return new Set(data.gliders?.flatMap(g => g.cells).map(([x, y]) => `${x},${y}`) || []);
}

export async function animate() {
    requestAnimationFrame(animate);
    const liveCells = await fetchState();

    cubes.forEach((cube, i) => {
        const x = i % gridW;
        const y = Math.floor(i / gridW);
        const key = `${x},${y}`;
        cube.material.color.setHex(liveCells.has(key) ? 0x00ff00 : 0x222222);
    });

    renderer.render(scene, camera);
}