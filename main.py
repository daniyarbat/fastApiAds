from fastapi import FastAPI

app = FastAPI(
    title="FlatBoard - сервис объявлений о продаже квартир",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
