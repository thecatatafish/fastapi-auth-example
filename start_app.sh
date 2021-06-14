# Start the backend server
uvicorn backend.api.main:app --reload --port 8000 --host 0.0.0.0 &

# Serve the frontend
python3 -m http.server -d frontend 8080