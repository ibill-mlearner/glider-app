import * as THREE from '/static/js/three.module.js';

export let cubes = [];

export function initGrid(scene, gridW = 50, gridH = 30, cellSize = 1) {
    const geometry = new THREE.BoxGeometry(cellSize, cellSize, cellSize);
    const materialOff = new THREE.MeshBasicMaterial({ color: 0x222222 });

    for (let y = 0; y < gridH; y++) {
        for (let x = 0; x < gridW; x++) {
            const cube = new THREE.Mesh(geometry, materialOff.clone());
            cube.position.set(x * cellSize, y * cellSize, 0);
            scene.add(cube);
            cubes.push(cube);
        }
    }
}