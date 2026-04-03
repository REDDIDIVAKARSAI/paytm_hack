from fastapi import FastAPI
from app.database import Base, engine

from app.routes import voice, bill, payment, status

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten this in production
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(voice.router)
app.include_router(bill.router)
app.include_router(payment.router)
app.include_router(status.router)
