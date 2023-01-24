from fastapi import FastAPI
import pickle
import sklearn
model = pickle.load(open('src/model.save','rb'))
app = FastAPI()

# дефолтные параметры взяты из тренировочного набора
# для удобства тестирования например через localhost/docs
@app.get("/")
def home_view(
        age: int = 61,
        sex: int = 1,
        cp: int = 0,
        trestbps: int = 134,
        chol: int = 234,
        fbs: int = 0,
        restecg: int = 0,
        thalach: int = 145,
        exang: int = 0,
        oldpeak: float = 2.6,
        slope: int = 1,
        ca: int = 1,
        thal: int = 0,
    ):

    result =  {"condition": 
        model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,
            thalach, exang, oldpeak, slope, ca, thal],]).tolist()[0]}

    return result

