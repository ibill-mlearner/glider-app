import * as THREE from '/static/js/three.module.js';

export let cubes = [];

export function initGrid(scene, gridW = 100, gridH = 100, cellSize = 1) {
    cubes.length = 0; // starts top left

    // lazy sizing
    const geometry = new THREE.BoxGeometry(cellSize, cellSize, cellSize);
    const materialOff = new THREE.MeshBasicMaterial({ color: new THREE.Color('dimgray')  });

    // draw y first
    for (let y = 0; y < gridH; y++) {
        // draw x second
        for (let x = 0; x < gridW; x++) {
            const cube = new THREE.Mesh(geometry, materialOff.clone());
            cube.position.set(x * cellSize, (gridH - y - 1) * cellSize, 0);
            scene.add(cube);
            cubes.push(cube);
        }
    }
}