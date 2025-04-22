# Retail Sales Forecasting Pipeline 🛒📈

This repository contains a **step‑by‑step time‑series pipeline** for cleaning daily sales data, benchmarking forecasting models and deploying an interactive Streamlit app.  
It was designed for supermarket stores with **hundreds of products** and shows how a simple *Random Forest* can outperform a naïve baseline.

---

## Project structure

| Stage | Script | What it does |
|-------|--------|--------------|
| **1 · Prepare data** | `forecasting_01.py` | Reads `data_prueba_Forecasting.csv`, filters the selected *store format* (e.g. *Hiper‑Intermedio*), fills missing calendar dates and pivots into a “products‑as‑columns” matrix saved as `t*_store.csv`. citeturn2view0 |
| **2 · Evaluate models** | `forecasting_02_e.py` | Removes products with ≥50 % missing values, linearly interpolates gaps, then compares a **Naive Drift** baseline against a **Random Forest** (lags = 15). It exports **MAE, MAPE, RMSE** per product to `t*_store‑metricas.csv`. citeturn3view0 |
| **3 · Forecast horizon** | `forecasting_03_c.py` | Generates 15‑day forecasts (1–15 Nov 2021) for each product and writes them to `t*_store‑pronostico.csv`. |
| **4 · Model win‑rate** | `forecasting_04_b.py` | Counts how many products the Random Forest beats the baseline on each error metric. citeturn9view0 |
| **5 · Web app** | `forecasting_03_c_deploy.py` | Streamlit front‑end that trains the Random Forest on‑demand and plots historical sales + forecast for a user‑selected product. Live demo: **[atrenux‑enki‑demo.hf.space](https://atrenux-enki-demo.hf.space)** citeturn8view0 |

> **Tip:** Each script contains *commented sections* to switch between the six store formats (Híper‑Básico, Híper‑Intermedio, … Super‑Plus).

---

## Quick start

```bash
# 1. Clone
git clone https://github.com/felipeortizh/forecasting.git
cd forecasting

# 2. Create env
python -m venv .venv && source .venv/bin/activate

# 3. Install deps
pip install -r requirements.txt   # or see list below

# 4. Run data prep for store 2 (Híper‑Intermedio)
python forecasting_01.py
python forecasting_02_e.py
python forecasting_03_c.py

# 5. Launch Streamlit app
streamlit run forecasting_03_c_deploy.py
```

---

## Dependencies

```text
pandas>=1.5
darts>=0.28          # Time‑series models (NaiveDrift, RandomForest)
matplotlib>=3.8
streamlit>=1.30
scikit‑learn>=1.4    # pulled by darts
```

If you only need the CLI workflow (no app) you can omit `streamlit`.

---

## Input data

* **`raw-data.zip`**: compressed source datasets. Unzip, inspect the CSV inside, then edit `forecasting_01.py` to point to the file path. citeturn0view0

The scripts generate intermediary CSVs (`t*_store*.csv`) that drive the downstream phases.

---

## Results snapshot

* For *Híper‑Intermedio* the Random Forest achieved **lower MAE on 923 / 1 261 products** (and similar wins for MAPE & RMSE). citeturn9view0
* A 15‑day ahead forecast is plotted interactively in the Streamlit UI.

---

## Contributing

Feel free to open issues or PRs for:

* Hyper‑parameter tuning (e.g. boosting, Prophet, LightGBM)
* Better gap‑filling strategies
* Dockerizing the Streamlit app

---

## License

MIT.  

Created with ❤️ by Felipe Ortiz.
