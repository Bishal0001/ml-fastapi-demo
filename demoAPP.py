from fastapi import FastAPI


app = FastAPI()


@app.get("/predict")
def predict_model(age: int, sex:str, income:int):
    if age <= 15 and sex == 'F' and income>10000:
        return {'survived':1}
    return {'survived':0}


