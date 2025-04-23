from fastapi import FastAPI

app = FastAPI(title="MLOps Demo API")


@app.get("/")
async def root():
    return {"message": "Welcome to the MLOps Demo API"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


# Add model prediction endpoint
@app.post("/predict")
async def predict(data: dict):
    # Implement prediction logic here
    return {"prediction": "Not implemented yet", "data": data}
