from backend.server import app
from dotenv import load_dotenv
from mangum import Mangum
load_dotenv()

handler = Mangum(app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)