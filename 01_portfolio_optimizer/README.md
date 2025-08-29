# Supplier Portfolio Optimization for Cost Stability

## 1. Business Problem

This project aims to solve a budgeting and supply chain problem for an **imaginary** company that purchases an essential product, 'P', from two different suppliers (A and B). The company needs to set a fixed monthly purchase ratio between these two suppliers for an upcoming 12-month budget period.

Based on historical price data, the objective is to determine the optimal percentage split between Supplier A and Supplier B that results in the most stable and predictable monthly costs. The chosen strategy is to **minimize the variance** of the combined monthly purchase price.

## 2. Data

The analysis is based on historical monthly average prices provided in the `prices.csv` file. This synthetic dataset contains prices for both suppliers from January 2019 to December 2022.

## 3. Methodology

The problem is modeled as a two-asset portfolio optimization problem:

* The supplies from Supplier A and Supplier B are treated as two assets.

* The "weight" (`w`) of the portfolio is the percentage of the product purchased from Supplier A. The remaining `(1 - w)` is purchased from Supplier B.

* The `main.py` script systematically tests a range of possible weights (from 0% to 100% for Supplier A).

* For each weight, it calculates the historical variance of the combined monthly cost.

* The script identifies the weight that results in the lowest variance.

## 4. Results

The analysis concludes that the optimal strategy to achieve the most stable monthly cost is:

* **Purchase 47% of the product from Supplier A.**

* **Purchase 53% of the product from Supplier B.**

This 47/53 split minimizes the month-to-month price volatility, providing the most predictable cost basis for the company's budget with a minimum cost variance of 3.74.

## 5. How to Use


1.  **Set up the environment:**
    * Create the conda environment using the `environment.yml` file. This will install all necessary dependencies.
    ```bash
    conda env create -f environment.yml
    ```

2.  **Activate the environment:**
    ```bash
    conda activate portfolio_optimizer
    ```

3.  **Run the analysis:**
    * Execute the optimizer script. The results will be printed to the console.
    ```bash
    python main.py
    ```