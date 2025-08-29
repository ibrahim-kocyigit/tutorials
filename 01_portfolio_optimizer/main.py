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


if __name__ == "__main__":
    # Data loading and preparation
    try:
        price_data = pd.read_csv("./prices.csv")
        prices_A = np.array(price_data["price_supplier_a_dollars_per_item"])
        prices_B = np.array(price_data["price_supplier_b_dollars_per_item"])
    except:
        print(
            "Error: prices.csv not found. Please ensure that the fie is in the correct directory."
        )
        exit()

    # Analysis
    optimizer = PortfolioOptimizer(prices_A, prices_B)
    optimum_weight, optimum_loss = optimizer.find_optimal_weight()

    # Results
    print("--- Optimal Portfolio (Minimum Variance Strategy) ---")
    print(f"Optimal percentage from Supplier A: {optimum_weight:.0%}")
    print(f"Optimal percentage from Supplier B: {1 - optimum_weight:.0%}")
    print(f"Resulting Minimum Cost Variance: {optimum_loss:.2f}")
