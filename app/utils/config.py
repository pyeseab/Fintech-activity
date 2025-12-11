#entralized place for all constants, file paths, thresholds, and settings your app may need.

import os

# -----------------------
# Database configuration
# -----------------------
DB_FILE = os.getenv("DB_FILE", "portfolio.db")  # Default SQLite file

# -----------------------
# Risk-free rate for Sharpe ratio
# -----------------------
RISK_FREE_RATE = 0.01  # 1% default

# -----------------------
# Cache settings
# -----------------------
CACHE_TTL = 300  # seconds

# -----------------------
# Optimizer settings
# -----------------------
OPTIMIZER_MAX_ITER = 1000  # max iterations for optimization
OPTIMIZER_TOL = 1e-6       # tolerance for convergence

# -----------------------
# Logging
# -----------------------
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# -----------------------
# API settings (optional)
# -----------------------
# Example if you later use Yahoo Finance or another API
STOCK_API_KEY = os.getenv("STOCK_API_KEY", "")
