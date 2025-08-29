import pandas as pd
from pathlib import Path
from PortfolioOptimizer import PortfolioOptimizer


def run_analysis():
    """
    Loads data, runs the portfolio optimization, and prints the results.
    """
    try:
        # --- 1. Data Loading ---
        # Build a path to the data file that is relative to this script's location
        # This makes the script runnable from anywhere.
        SCRIPT_DIR = Path(__file__).resolve().parent
        PRICE_FILE_PATH = SCRIPT_DIR / "prices.csv"
        price_data = pd.read_csv(PRICE_FILE_PATH)

        # --- 2. Data Preparation ---
        prices_A = price_data["price_supplier_a_dollars_per_item"].to_numpy()
        prices_B = price_data["price_supplier_b_dollars_per_item"].to_numpy()

        # --- 3. Analysis ---
        optimizer = PortfolioOptimizer(prices_A, prices_B)
        optimum_weight, optimum_loss = optimizer.find_optimal_weight()

        # --- 4. Results ---
        print("--- Optimal Portfolio (Minimum Variance Strategy) ---")
        print(f"Optimal percentage from Supplier A: {optimum_weight:.0%}")
        print(f"Optimal percentage from Supplier B: {1 - optimum_weight:.0%}")
        print(f"Resulting Minimum Cost Variance: {optimum_loss:.2f}")

    except FileNotFoundError:
        print(f"Error: `prices.csv` not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# --- Execution Block ---
# This code will only run if the script is executed directly
if __name__ == "__main__":
    run_analysis()
