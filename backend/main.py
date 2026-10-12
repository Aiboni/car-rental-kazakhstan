from fastapi import FastAPI

app = FastAPI(
    title="Car Rental Marketplace Kazakhstan",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}
