import unittest
import numpy as np
from services.advice.engine import evaluate_sharpe
from services.optimizer import optimize_portfolio

class TestAnalytics(unittest.TestCase):

#test sharpe ratio logic:

    def test_evaluate_sharpe_high(self):
        self.assertEqual(
            evaluate_sharpe(1.7),
            "Excellent risk-adjusted returns! Portfolio looks strong."
        )

    def test_evaluate_sharpe_low(self):
        self.assertEqual(
            evaluate_sharpe(0.3),
            "Low risk-adjusted returns; portfolio may be underperforming."
        )

