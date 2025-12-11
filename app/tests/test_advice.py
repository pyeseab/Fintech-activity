#creating test scenarios
import unittest
from services.advice.engine import evaluate_sharpe

class TestAdviceEngine(unittest.TestCase):

    def test_high_sharpe(self):
        self.assertEqual(
            evaluate_sharpe(1.8),
            "Excellent risk-adjusted returns! Portfolio looks strong."
        )

    def test_good_sharpe(self):
        self.assertEqual(
            evaluate_sharpe(1.2),
            "Good performance, but there may be room for improvement."
        )

    def test_average_sharpe(self):
        self.assertEqual(
            evaluate_sharpe(0.7),
            "Average performance, consider rebalancing or diversifying."
        )

    def test_low_sharpe(self):
        self.assertEqual(
            evaluate_sharpe(0.2),
            "Low risk-adjusted returns; portfolio may be underperforming."
        )

if __name__ == "__main__":
    unittest.main()
