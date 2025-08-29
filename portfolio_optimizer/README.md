# Supplier Portfolio Optimization for Cost Stability

## 1. Business Problem

This project aims to solve a budgeting and supply chain problem for an **imaginary** company that purchases an essential product, 'P', from two different suppliers (A and B). The company needs to set a fixed monthly purchase ratio between these two suppliers for an upcoming 12-month budget period.

Based on historical price data, the objective is to determine the optimal percentage split between Supplier A and Supplier B that results in the most stable and predictable monthly costs. The chosen strategy is to **minimize the variance** of the combined monthly purchase price.

## 2. Data

The analysis is based on historical monthly average prices provided in the `prices.csv` file, located in the root `tutorials` directory. This synthetic dataset contains prices for both suppliers from January 2019 to December 2022.

## 3. Methodology

The problem is modeled as a two-asset portfolio optimization problem. The core logic is encapsulated in the `PortfolioOptimizer` class, which systematically tests a range of purchase ratios to find the one that results in the lowest historical cost variance.

## 4. Results

The analysis concludes that the optimal strategy to achieve the most stable monthly cost is:

* **Purchase 47% of the product from Supplier A.**
* **Purchase 53% of the product from Supplier B.**

This 47/53 split minimizes the month-to-month price volatility, providing the most predictable cost basis for the company's budget with a minimum cost variance of 3.74.

## 5. Project Structure

The project is organized as a Python module to promote reusability and maintain a clean structure.
