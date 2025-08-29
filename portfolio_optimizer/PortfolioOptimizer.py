import pandas as pd
import numpy as np


class PortfolioOptimizer:
    """
    Analyzes historical price data for two suppliers to find the optimal
    portfolio split that minimizes cost variance.
    """

    def __init__(
        self, prices_for_item_A: np.ndarray, prices_for_item_B: np.ndarray
    ) -> None:
        """
        Initializes the optimizer with pice arrays for two items.
        """
        self.prices_A = prices_for_item_A
        self.prices_B = prices_for_item_B

    def _calculate_portfolio_costs(self, w_A: float) -> np.ndarray:
        """
        Calculates the time series of portfolio costs for a given weight of supplier A.
        Private method intended for internal use.
        """
        #  f(w) = w * p_a + (1 - w) * p_b
        return w_A * self.prices_A + (1 - w_A) * self.prices_B

    def _calculate_variance(self, w_A: float) -> float:
        """
        Calculate the variance (loss) of portfolio costs for a given weight.
        Private method intended for internal use.
        """
        costs = self._calculate_portfolio_costs(w_A)
        return float(np.var(costs))

    def find_optimal_weight(self, steps: int = 101) -> tuple[float, float]:
        """
        Finds the optimal weight for supplier A by iterating through possible values.

        Args:
            steps (int): The number of different weights to set between 0 and 1.

        Returns:
            A tuple containing the optimal weight for supplier A and the minimum variance.
        """
        w_values = np.linspace(0, 1, steps, endpoint=True)
        l_values = np.array([self._calculate_variance(w) for w in w_values])

        min_loss_index = l_values.argmin()
        optimal_w = w_values[min_loss_index]
        min_loss = l_values[min_loss_index]

        return float(optimal_w), float(min_loss)
