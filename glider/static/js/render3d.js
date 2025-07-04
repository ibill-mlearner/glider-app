import { scene, initScene } from './render3d/init_scene.js';
import { initGrid } from './render3d/init_grid.js';
import { animate } from './render3d/update_loop.js';

initScene();
initGrid(scene); // scene is declared in init_scene.js and exported
animate();

