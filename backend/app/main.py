from fastapi import FastAPI

app = FastAPI(
    title="Interview Prep Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message" : "Interview Prep Platform Backend Running"
    }