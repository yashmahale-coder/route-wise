from flask import Flask, jsonify, render_template, request
from algorithms.graph import GRAPH, COORDS, LOCATIONS
from algorithms.dijkstra import dijkstra
from algorithms.astar import astar

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html", locations=LOCATIONS)

@app.get("/api/locations")
def locations():
    return jsonify([
        {"id": key, "name": name, "x": COORDS[key][0], "y": COORDS[key][1]}
        for key, name in LOCATIONS.items()
    ])

@app.post("/api/route")
def calculate_route():
    data = request.get_json(silent=True) or {}
    start, goal = data.get("start"), data.get("goal")
    if start not in GRAPH or goal not in GRAPH:
        return jsonify({"error": "Please choose valid start and destination locations."}), 400
    if start == goal:
        return jsonify({"error": "Start and destination must be different."}), 400

    d_path, d_cost, d_visited = dijkstra(GRAPH, start, goal)
    a_path, a_cost, a_visited = astar(GRAPH, COORDS, start, goal)

    def path_names(path):
        return [LOCATIONS[node] for node in path]

    return jsonify({
        "start": start,
        "goal": goal,
        "dijkstra": {
            "path": d_path,
            "names": path_names(d_path),
            "distance": round(d_cost, 2),
            "visited": d_visited
        },
        "astar": {
            "path": a_path,
            "names": path_names(a_path),
            "distance": round(a_cost, 2),
            "visited": a_visited
        },
        "note": "Demo network with illustrative road distances, not live navigation data."
    })

if __name__ == "__main__":
    app.run(debug=True)
