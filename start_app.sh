PORT_FRONTEND=8080

# Start the backend server
uvicorn api.main:app --reload --port 8000 --host 0.0.0.0 &

# Serve the frontend
echo Access frontend http://localhost:$PORT_FRONTEND
python3 -m http.server -d frontend $PORT_FRONTEND

