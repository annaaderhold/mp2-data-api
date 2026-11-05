

This project is a FastAPI application, for uploading, inspecting, and cleaning CSV data. It provides endpoints to check API health (`GET /health`), uploads a CSV file (`POST /upload`), retrieves stored rows with a row limit (`GET /datasets/{id}`), and validates/processes a stored dataset using the reusable MP1 pipeline (`POST /datasets/{id}/process`). 