DWDM Mini Project - Customer Shopping Behaviour Analysis (Market Basket Analysis)

FILES
1. customer_shopping_transactions.csv  - synthetic dataset (600 transactions, 2,404 rows).
   Contains 8 deliberately dirty rows (3 duplicates, 2 missing products, 1 negative quantity,
   1 zero price, 1 missing city) so the preprocessing step has real work to do.
2. shopping_baskets.arff               - basket-form ARFF for WEKA (600 transactions, 20 products,
   values: t = bought, ? = not bought).
3. DWDM_Shopping_Behaviour.ipynb       - notebook: preprocessing, star schema, data cube
   (roll-up, drill-down, slice, dice), CSV->ARFF, Apriori (Python), hash tree.

HOW TO RUN
- Open the notebook in Jupyter or Google Colab, upload the CSV next to it, run cells top to bottom.
- If mlxtend is missing: pip install pandas numpy mlxtend
- WEKA: Explorer -> Preprocess -> open shopping_baskets.arff -> Associate -> Apriori
  (lowerBoundMinSupport 0.05, minMetric 0.3, metricType Confidence, numRules 500) -> Start.

NOTE: The dataset is synthetic and for educational use. State this in your report.
