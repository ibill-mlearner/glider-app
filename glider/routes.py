from flask import render_template, jsonify, request
from glider.core.engine import GliderEngine

engine = GliderEngine(50, 30)

block = [
    [1, 1],
    [1, 1]
]

engine.load_pattern(block, offset_x=10, offset_y=10)


def init_app(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/api/state', methods=['GET'])
    def get_state():
        cells = []
        for y, row in enumerate(engine.grid):
            for x, cell in enumerate(row):
                if cell:
                    cells.append([x, y])
        return jsonify({'status': 'ok', 'gliders': [{'cells': cells}]})