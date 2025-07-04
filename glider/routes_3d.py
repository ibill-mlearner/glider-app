from flask import render_template

def init_3d_routes(app):
    @app.route('/3d')
    def index_3d():
        return render_template('index_3d.html')