from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import portfolios, users, advice

from routes.users import add_user, get_user_by_id


app = FastAPI(title="Vito API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router,      prefix="/api/users",      tags=["users"])
app.include_router(portfolios.router, prefix="/api/portfolios", tags=["portfolios"])
app.include_router(advice.router,     prefix="/api/advice",     tags=["advice"])
