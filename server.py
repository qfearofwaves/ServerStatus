from flask import Flask, jsonify
import time

def create_app(test_config=None):
    app = Flask(__name__)
    start_time = time.time()
    simulation_duration = 10  # duration to switch from pending to completed

    @app.route('/status')
    def status():
        if time.time() - start_time < simulation_duration:
            return jsonify({"result": "pending"})
        elif time.time() - start_time < simulation_duration + 5:
            return jsonify({"result": "completed"})
        else:
            return jsonify({"result": "error"})
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
