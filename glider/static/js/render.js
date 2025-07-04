// glider/static/js/render.js

const canvas = document.getElementById("glider-canvas");
const ctx = canvas.getContext("2d");

const cellSize = 10;
const gridWidth = 100;
const gridHeight = 60;

canvas.width = cellSize * gridWidth;
canvas.height = cellSize * gridHeight;

function drawGrid(grid) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let y = 0; y < grid.length; y++) {
        for (let x = 0; x < grid[y].length; x++) {
            if (grid[y][x]) {
                ctx.fillStyle = "black";
                ctx.fillRect(x * cellSize, y * cellSize, cellSize, cellSize);
            }
        }
    }
}

// Example usage with dummy data
fetch('/api/state')
    .then(res => res.json())
    .then(data => {
        const grid = Array.from({ length: gridHeight }, () => Array(gridWidth).fill(0));
        for (const glider of data.gliders) {
            for (const [x, y] of glider.cells) {
                if (y >= 0 && y < gridHeight && x >= 0 && x < gridWidth) {
                    grid[y][x] = 1;
                }
            }
        }
        drawGrid(grid);
    });