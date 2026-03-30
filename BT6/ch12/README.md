📐 Matrix Distance API (Flask)
📌 Description

This project is a lightweight Flask-based REST API for calculating distances between two vectors. It supports:

Manhattan Distance (L1)
Euclidean Distance (L2)

The application uses NumPy for efficient numerical computation and exposes a simple HTTP endpoint for integration with other systems.

⚙️ Installation
1. Clone the repository
git clone <your-repo-url>
cd <your-repo-folder>
2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows
3. Install dependencies
pip install flask numpy
🚀 Running the Application
python app.py

By default, the server will run at:

http://127.0.0.1:5000
📡 API Documentation
🔹 Endpoint
POST /distances
🔹 Description

Calculate the distance between two vectors using either Manhattan (L1) or Euclidean (L2) metric.

🔹 Request Body (JSON)
{
  "df1": [1, 2, 3],
  "df2": [4, 5, 6],
  "distance": "L1"
}
🔹 Parameters
Field	Type	Description
df1	array	First vector (list of numbers)
df2	array	Second vector (same length as df1)
distance	string	Distance type: "L1" or "L2"
🔹 Response (Success)
{
  "distance": 9.0
}
🔹 Supported Distance Types
Type	Name	Formula Description
L1	Manhattan	Sum of absolute differences
L2	Euclidean	Sum of squared differences
🧪 cURL Example
Manhattan Distance (L1)
curl -X POST http://127.0.0.1:5000/distances \
-H "Content-Type: application/json" \
-d '{
  "df1": [1, 2, 3],
  "df2": [4, 5, 6],
  "distance": "L1"
}'
Euclidean Distance (L2)
curl -X POST http://127.0.0.1:5000/distances \
-H "Content-Type: application/json" \
-d '{
  "df1": [1, 2, 3],
  "df2": [4, 5, 6],
  "distance": "L2"
}'
⚠️ Notes & Limitations
Both vectors (df1, df2) must have the same length
No validation is currently implemented for:
Missing fields
Invalid distance types
Non-numeric values
Euclidean distance currently returns sum of squares (not square root)
📈 Future Improvements
Add input validation and error handling
Support more distance metrics (Cosine, Minkowski)
Return true Euclidean distance (with square root)
Add unit tests and API documentation tools (Swagger/OpenAPI)
👨‍💻 Author

Developed as a simple microservice for vector distance computation using Flask and NumPy.