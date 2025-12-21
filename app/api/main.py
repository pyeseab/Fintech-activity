from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.users import router as users_router
from app.routes.portfolios import router as portfolios_router
from app.routes.advice import router as advice_router  # make sure advice.py has router

app = FastAPI(title="Vito API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Use the imported router variables, not `users` or `portfolios`
app.include_router(users_router,      prefix="/api/users",      tags=["users"])
app.include_router(portfolios_router, prefix="/api/portfolios", tags=["portfolios"])
app.include_router(advice_router,     prefix="/api/advice",     tags=["advice"])
