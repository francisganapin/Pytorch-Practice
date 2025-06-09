from fastapi import FastAPI


app = FastAPI()

@app.get("/fruits")
def get_fruits():
    fruits = ['apple','banana','orange']
    return fruits