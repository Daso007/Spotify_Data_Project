# End-to-End Spotify Data Analytics Pipeline

## Project Objective

This project demonstrates a full, end-to-end ELT (Extract, Load, Transform) data engineering pipeline. Raw playlist data is extracted from the Spotify API, loaded into a Google BigQuery data warehouse, transformed into a clean, analytical model using dbt, and visualized in a business intelligence dashboard. The goal is to translate raw data into actionable insights about musical trends.

---

## 🚀 Live Dashboard

A live, interactive dashboard visualizing the final data can be viewed here:
**[Link to your public Looker Studio dashboard]**  *(Go to your Looker dashboard, click "Share," and get a public link to paste here)*

---

## Technical Architecture

This project uses a modern data stack to process the data.



1.  **Extract:** A Python script uses the Spotify API to extract raw data for a given playlist.
2.  **Load:** The extracted data is loaded into Google BigQuery, our cloud data warehouse.
3.  **Transform:** dbt connects to BigQuery to transform the raw data into clean, documented, and tested analytical models. This separates raw data from business logic.
4.  **Visualize:** Google Looker Studio connects to the final dbt model in BigQuery to create an interactive dashboard.

---

## Tech Stack

*   **Data Extraction:** Python (`requests`, `pandas`)
*   **Data Warehouse:** Google BigQuery
*   **Data Transformation:** dbt (data build tool)
*   **Data Visualization:** Google Looker Studio
*   **Cloud & Security:** Google Cloud Platform (IAM, Service Accounts)

---

## How to Run This Project Locally

1.  **Clone the repository:**
    `git clone https://github.com/your-username/spotify_analytics_project.git`
2.  **Set up a virtual environment and install dependencies:**
    `pip install -r requirements.txt`
3.  **Set up your environment variables** by creating a `.env` file with your Spotify keys and a `google_credentials.json` with your GCP key.
4.  **Run the ELT scripts:**
    `python extract.py`
    `python load.py`
5.  **Run the dbt models:**
    `cd spotify_dbt_project`
    `dbt run`