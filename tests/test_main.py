"""End to End tests of app"""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

#eof
