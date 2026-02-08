from fastapi import FastAPI


app = FastAPI()


@app.get("/predict")
def predict_model(age: int, sex:str):
    if age <= 15 and sex == 'F':
        return {'survived':1}
    return {'survived':0}


