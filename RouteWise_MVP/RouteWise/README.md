# RouteWise

A Python-powered route-planning and algorithm-comparison demo. It compares custom implementations of Dijkstra's algorithm and A* search on a small illustrative weighted graph inspired by Navi Mumbai.

## Features
- Custom Dijkstra and A* implementations using Python's `heapq`
- Flask API for route calculation
- Interactive SVG graph visualization
- Comparison of path cost and expanded-node counts
- Unit tests for algorithm correctness

## Important scope note
This first version uses a **simulated graph and illustrative distances**. It is not live navigation, does not use real road geometry, and does not provide live traffic information. The map is an abstract network visualization.

## Run locally
Requires Python 3.10+.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

## Run tests
```bash
python -m unittest discover -s tests -v
```

## API
`GET /api/locations` returns the demo locations.

`POST /api/route`
```json
{"start": "uran", "goal": "airoli"}
```

Returns each algorithm's path, illustrative distance and number of expanded nodes.

## Algorithms
- Dijkstra: uses a min-priority queue and relaxes edge weights.
- A*: uses `f(n) = g(n) + h(n)`, where `g(n)` is the known path cost and `h(n)` is a Euclidean heuristic based on abstract coordinates.

The demo edge weights are chosen so the heuristic remains a lower bound for the illustrative graph.

## Next improvements
- Import real OpenStreetMap road-network data
- Add alternative routes
- Add configurable simulated traffic weights
- Benchmark across generated graphs of increasing size
- Add integration tests and deployment configuration

## Tech
Python, Flask, HTML, CSS, vanilla JavaScript, SVG, unittest.
