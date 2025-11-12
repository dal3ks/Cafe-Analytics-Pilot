## Cafe-Analytics-Pilot
Data analytics pilot project for a local café chain — analysing sales, profit, and customer buying habits, removed PII using Python and Power BI. 

*Final interactive Power BI dashboard showcasing sales, trends, customer insights and forecasts.*

<img width="1444" height="861" alt="image" src="https://github.com/user-attachments/assets/e36b99eb-c43d-4899-95ed-797ab34939f7" />

---
## Project Overview
The goal of this pilot was to help the café chain understand:
- Which branches perform best by sales and profit
- Customer purchasing behaviour by drink type
- Payment preferences (cash vs card)
- Overall sales trends and potential forecasts
---
## Tools and Technologies used:
**Python (VS Code)** Data Cleaning and anonymisation
** Power BI** Interactive dashboard and visual analytics
**Github** Documentation and version control
---
## Data Process
1. Extracted raw café transaction data from a text file
2. Transformed the data in Python:
   - Removed names and card numbers (PII).  
   - Corrected malformed entries.  
   - Exported to `cleaned_data.csv`.
3. Loaded the cleaned data into Power BI for visualisation.
---
## Dashboard Features

**KPIS:**
- Total Sales (£)
- Profit (£)
- Transactions Count
- Average Spend Per Customer
- Card vs Cash Sales %
---
**Visuals**
  -Sales by Branch (Bar Chart)
  -Top Drinks (Column Chart)
  -Sales Trend and Forecast (Line Chart with Analytics)
  -Payment Type Breakdown (Pie Chart)
---
## Insights & Recommendations
-**Woking** is the best performing branch by total sales
-**Macchiato** is the most popular drink, followed by **Espresso**
-**Card payments** slightly outnumber ** cash transactions** (around 52%)
-Sales dipped mid-year but show an **upward recovery** towards winter- suggesting **seasonal demand**
-Recommend adding loyalty incentives or promotions for slower months
---
## Deliverables
| File | Description |
- `cleaning_script.py`:Python ETL script for data cleaning and anonymisation
- `cleaned_data.csv` :Processed dataset used in Power BI 
- `Cafe_Analytics_Pilot.pbix`: Power BI dashboard 
- `Cafe_Analytics_Pilot_Client_Presentation.pptx`: Client-facing summary presentation 
---
## Project Reflection
This project strengthend my skills in:
- Data cleaning and ETL with Python
- Power BI dashboard design and storytelling
- Version control with GitHub
- Translating data insights into business recommendations
---
## Future Improvements
-Automate the ETL piple using a database connection
-Deploy the dashboard to a cloud workspace for scalability

---

## How to Run This Project
1- Close this repository: 
git clone https://github.com/dal3ks/Cafe-Analytics-Pilot.git
cd Cafe-Analytics-Pilot

2- Prepare the raw data
Place provided raw_data.txt file into the data/raw/ folder

3- Run the cleaning script
Open cleaning script.py in VS Code or your IDE
Runt the file generate cleaned_data.csv inside data/processed/

4- Visualise in Power BI
Open Power BI Desktop
Load data/processed/cleaned_data.csv
Explore visuals for Total Sales, Proft, Transactions and Payment Trends.
---

---
## Power BI Dashboard
The final dashboard is available in:
[`powerbi/Cafe_Analytics_Pilot.pbix`](powerbi/Cafe_Analytics_Pilot.pbix)

Open it in **Power BI Desktop** to explore the interactive visualisations and KPIs.
*All personal data has been anonymised in compliance with GDPR*

  
