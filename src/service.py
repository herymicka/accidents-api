import time
import jwt
import bentoml
import pandas as pd

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel, Field


SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"

USERS = {
    "user123": "password123"
}


class Credentials(BaseModel):
    username: str
    password: str


class LoginRequest(BaseModel):
    credentials: Credentials


class AccidentInput(BaseModel):
    place: int
    catu: int
    sexe: int
    secu1: float
    year_acc: int
    victim_age: int
    catv: int
    obsm: int
    motor: int
    catr: int
    circ: int
    surf: int
    situ: int
    vma: int
    jour: int
    mois: int
    lum: int
    dep: int
    com: int
    agg_: int
    int_: int = Field(alias="int")
    atm: int
    col: int
    lat: float
    long: float
    hour: int
    nb_victim: int
    nb_vehicules: int


class PredictRequest(BaseModel):
    input_data: AccidentInput


def create_token(username: str) -> str:
    payload = {
        "sub": username,
        "exp": int(time.time()) + 3600
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])


class JWTAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        if request.url.path == "/predict":
            auth = request.headers.get("Authorization")

            if not auth or not auth.startswith("Bearer "):
                return JSONResponse({"error": "Unauthorized"}, status_code=401)

            token = auth.split(" ")[1]

            try:
                verify_token(token)
            except Exception:
                return JSONResponse({"error": "Invalid token"}, status_code=401)

        return await call_next(request)


@bentoml.service
class RFModelService:

    def __init__(self):
        self.model = bentoml.sklearn.load_model("accidents_rf:latest")

    @bentoml.api
    def predict(self, input_data: dict):
        df = pd.DataFrame([input_data])
        pred = self.model.predict(df)
        return {"prediction": pred.tolist()}


@bentoml.service(middlewares=[JWTAuthMiddleware])
class RFClassifierService:

    model_service = bentoml.depends(RFModelService)

    @bentoml.api
    def login(self, request: LoginRequest):
        username = request.credentials.username
        password = request.credentials.password

        if USERS.get(username) != password:
            return {"error": "Invalid credentials"}

        token = create_token(username)
        return {"token": token}

    @bentoml.api
    def predict(self, request: PredictRequest):
        data = request.input_data.model_dump(by_alias=True)
        return self.model_service.predict(data)