# Example test file for how you would write tests for FastAPI
# This is a simple test for the root endpoint

# To run this test file, run the following command:
# pytest tests/example_test.py

# You may have to install pytest first with "pip install pytest"
# and httpx with "pip install httpx"

# to run tests use the following command:
#       pytest
# in your terminal, in the root directory of the project (/quantrack) or in the root directory of the git repo (/QUANTRACK)

from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
