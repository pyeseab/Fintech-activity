from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import portfolios

app = FastAPI(title="Vito API")

# CORS (frontend will work later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(portfolios.router)
