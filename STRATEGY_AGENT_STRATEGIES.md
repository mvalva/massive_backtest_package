# Agente strategie SEC — Tutte le strategie (tutte le combinazioni filtro + hold)

Cluster backtestati: 10 | Errori/saltati: 0 | Strategie (righe ranking): 4200

Ogni riga = una combinazione (filtro, orizzonte, metrica, entry). **Ranking** = posizione per macrocategoria (Base_name), ordinata per **Score** decrescente.

**Come si calcola lo Score (0–100):** per ogni macrocategoria (Base_name) si calcola la media di *Avg_ret_%* e la media di *Win_rate_%* sulle righe che la compongono. Le due medie vengono normalizzate tra 0 e 1 (min e max sul set di tutte le macrocategorie). Score = 50% × (media rendimento normalizzata) + 50% × (media win rate normalizzata), in scala 0–100. Più alto lo Score, migliore la posizione nel ranking.

| # | Ranking | Score | Strategia | Base_name | Metric_kind | Horizon_days | Entry_kind | N | Win_rate_% | Avg_ret_% | Median_ret_% | Total_ret_% | Std_% | Sharpe | Min_% | Max_% |
|---|--------|------|-----------|-----------|------------|--------------|-----------|---|------------|-----------|--------------|-------------|------|--------|-------|-------|
| 1 | 4 | 82.51 | CEO + Director (combo) — hold ret_high_60d_open | CEO + Director (combo) | high | 60 | open | 1 | 100.0 | 39.42 | 39.42 | 39.42 | nan | nan | 39.42 | 39.42 |
| 2 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_high_60d_open | Small cap (≤1B) CEO/CFO | high | 60 | open | 1 | 100.0 | 39.42 | 39.42 | 39.42 | nan | nan | 39.42 | 39.42 |
| 3 | 4 | 82.51 | CEO + Director (combo) — hold ret_high_90d_open | CEO + Director (combo) | high | 90 | open | 1 | 100.0 | 39.42 | 39.42 | 39.42 | nan | nan | 39.42 | 39.42 |
| 4 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_high_90d_open | Small cap (≤1B) CEO/CFO | high | 90 | open | 1 | 100.0 | 39.42 | 39.42 | 39.42 | nan | nan | 39.42 | 39.42 |
| 5 | 4 | 82.51 | CEO + Director (combo) — hold ret_high_60d_news | CEO + Director (combo) | high | 60 | news | 1 | 100.0 | 38.1 | 38.1 | 38.1 | nan | nan | 38.1 | 38.1 |
| 6 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_high_60d_news | Small cap (≤1B) CEO/CFO | high | 60 | news | 1 | 100.0 | 38.1 | 38.1 | 38.1 | nan | nan | 38.1 | 38.1 |
| 7 | 4 | 82.51 | CEO + Director (combo) — hold ret_high_90d_news | CEO + Director (combo) | high | 90 | news | 1 | 100.0 | 38.1 | 38.1 | 38.1 | nan | nan | 38.1 | 38.1 |
| 8 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_high_90d_news | Small cap (≤1B) CEO/CFO | high | 90 | news | 1 | 100.0 | 38.1 | 38.1 | 38.1 | nan | nan | 38.1 | 38.1 |
| 9 | 6 | 77.62 | CEO only — hold ret_high_90d_news | CEO only | high | 90 | news | 3 | 100.0 | 26.95 | 25.19 | 80.84 | 10.39 | 2.59 | 17.55 | 38.1 |
| 10 | 6 | 77.62 | CEO only — hold ret_high_90d_open | CEO only | high | 90 | open | 3 | 100.0 | 25.78 | 23.43 | 77.35 | 12.63 | 2.04 | 14.5 | 39.42 |
| 11 | 6 | 77.62 | CEO only — hold ret_high_60d_news | CEO only | high | 60 | news | 3 | 100.0 | 25.22 | 25.19 | 75.66 | 12.87 | 1.96 | 12.37 | 38.1 |
| 12 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_high_7d_news | CEO only + Value ≥500k | high | 7 | news | 1 | 100.0 | 25.19 | 25.19 | 25.19 | nan | nan | 25.19 | 25.19 |
| 13 | 1 | 100.0 | CEO only + Position +10% — hold ret_high_7d_news | CEO only + Position +10% | high | 7 | news | 1 | 100.0 | 25.19 | 25.19 | 25.19 | nan | nan | 25.19 | 25.19 |
| 14 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_high_7d_news | Near 52w high + CEO/CFO | high | 7 | news | 1 | 100.0 | 25.19 | 25.19 | 25.19 | nan | nan | 25.19 | 25.19 |
| 15 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_high_10d_news | CEO only + Value ≥500k | high | 10 | news | 1 | 100.0 | 25.19 | 25.19 | 25.19 | nan | nan | 25.19 | 25.19 |
| 16 | 1 | 100.0 | CEO only + Position +10% — hold ret_high_10d_news | CEO only + Position +10% | high | 10 | news | 1 | 100.0 | 25.19 | 25.19 | 25.19 | nan | nan | 25.19 | 25.19 |
| 17 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_high_10d_news | Near 52w high + CEO/CFO | high | 10 | news | 1 | 100.0 | 25.19 | 25.19 | 25.19 | nan | nan | 25.19 | 25.19 |
| 18 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_high_14d_news | CEO only + Value ≥500k | high | 14 | news | 1 | 100.0 | 25.19 | 25.19 | 25.19 | nan | nan | 25.19 | 25.19 |
| 19 | 1 | 100.0 | CEO only + Position +10% — hold ret_high_14d_news | CEO only + Position +10% | high | 14 | news | 1 | 100.0 | 25.19 | 25.19 | 25.19 | nan | nan | 25.19 | 25.19 |
| 20 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_high_14d_news | Near 52w high + CEO/CFO | high | 14 | news | 1 | 100.0 | 25.19 | 25.19 | 25.19 | nan | nan | 25.19 | 25.19 |
| 21 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_high_30d_news | CEO only + Value ≥500k | high | 30 | news | 1 | 100.0 | 25.19 | 25.19 | 25.19 | nan | nan | 25.19 | 25.19 |
| 22 | 1 | 100.0 | CEO only + Position +10% — hold ret_high_30d_news | CEO only + Position +10% | high | 30 | news | 1 | 100.0 | 25.19 | 25.19 | 25.19 | nan | nan | 25.19 | 25.19 |
| 23 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_high_30d_news | Near 52w high + CEO/CFO | high | 30 | news | 1 | 100.0 | 25.19 | 25.19 | 25.19 | nan | nan | 25.19 | 25.19 |
| 24 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_high_60d_news | CEO only + Value ≥500k | high | 60 | news | 1 | 100.0 | 25.19 | 25.19 | 25.19 | nan | nan | 25.19 | 25.19 |
| 25 | 1 | 100.0 | CEO only + Position +10% — hold ret_high_60d_news | CEO only + Position +10% | high | 60 | news | 1 | 100.0 | 25.19 | 25.19 | 25.19 | nan | nan | 25.19 | 25.19 |
| 26 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_high_60d_news | Near 52w high + CEO/CFO | high | 60 | news | 1 | 100.0 | 25.19 | 25.19 | 25.19 | nan | nan | 25.19 | 25.19 |
| 27 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_high_90d_news | CEO only + Value ≥500k | high | 90 | news | 1 | 100.0 | 25.19 | 25.19 | 25.19 | nan | nan | 25.19 | 25.19 |
| 28 | 1 | 100.0 | CEO only + Position +10% — hold ret_high_90d_news | CEO only + Position +10% | high | 90 | news | 1 | 100.0 | 25.19 | 25.19 | 25.19 | nan | nan | 25.19 | 25.19 |
| 29 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_high_90d_news | Near 52w high + CEO/CFO | high | 90 | news | 1 | 100.0 | 25.19 | 25.19 | 25.19 | nan | nan | 25.19 | 25.19 |
| 30 | 6 | 77.62 | CEO only — hold ret_high_60d_open | CEO only | high | 60 | open | 3 | 100.0 | 24.1 | 23.43 | 72.31 | 14.99 | 1.61 | 9.46 | 39.42 |
| 31 | 10 | 66.41 | CEO/CFO — hold ret_high_90d_news | CEO/CFO | high | 90 | news | 4 | 100.0 | 23.99 | 21.37 | 95.97 | 10.34 | 2.32 | 15.13 | 38.1 |
| 32 | 11 | 66.41 | Officer/President — hold ret_high_90d_news | Officer/President | high | 90 | news | 4 | 100.0 | 23.99 | 21.37 | 95.97 | 10.34 | 2.32 | 15.13 | 38.1 |
| 33 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_high_90d_news | Large cap (≥250M) CEO/CFO | high | 90 | news | 4 | 100.0 | 23.99 | 21.37 | 95.97 | 10.34 | 2.32 | 15.13 | 38.1 |
| 34 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_high_90d_news | Large cap (≥500M) CEO/CFO | high | 90 | news | 4 | 100.0 | 23.99 | 21.37 | 95.97 | 10.34 | 2.32 | 15.13 | 38.1 |
| 35 | 10 | 66.41 | CEO/CFO — hold ret_high_90d_open | CEO/CFO | high | 90 | open | 4 | 100.0 | 23.92 | 20.88 | 95.69 | 10.96 | 2.18 | 14.5 | 39.42 |
| 36 | 11 | 66.41 | Officer/President — hold ret_high_90d_open | Officer/President | high | 90 | open | 4 | 100.0 | 23.92 | 20.88 | 95.69 | 10.96 | 2.18 | 14.5 | 39.42 |
| 37 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_high_90d_open | Large cap (≥250M) CEO/CFO | high | 90 | open | 4 | 100.0 | 23.92 | 20.88 | 95.69 | 10.96 | 2.18 | 14.5 | 39.42 |
| 38 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_high_90d_open | Large cap (≥500M) CEO/CFO | high | 90 | open | 4 | 100.0 | 23.92 | 20.88 | 95.69 | 10.96 | 2.18 | 14.5 | 39.42 |
| 39 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_high_5d_news | CEO only + Value ≥500k | high | 5 | news | 1 | 100.0 | 23.65 | 23.65 | 23.65 | nan | nan | 23.65 | 23.65 |
| 40 | 1 | 100.0 | CEO only + Position +10% — hold ret_high_5d_news | CEO only + Position +10% | high | 5 | news | 1 | 100.0 | 23.65 | 23.65 | 23.65 | nan | nan | 23.65 | 23.65 |
| 41 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_high_5d_news | Near 52w high + CEO/CFO | high | 5 | news | 1 | 100.0 | 23.65 | 23.65 | 23.65 | nan | nan | 23.65 | 23.65 |
| 42 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_high_7d_open | CEO only + Value ≥500k | high | 7 | open | 1 | 100.0 | 23.43 | 23.43 | 23.43 | nan | nan | 23.43 | 23.43 |
| 43 | 1 | 100.0 | CEO only + Position +10% — hold ret_high_7d_open | CEO only + Position +10% | high | 7 | open | 1 | 100.0 | 23.43 | 23.43 | 23.43 | nan | nan | 23.43 | 23.43 |
| 44 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_high_7d_open | Near 52w high + CEO/CFO | high | 7 | open | 1 | 100.0 | 23.43 | 23.43 | 23.43 | nan | nan | 23.43 | 23.43 |
| 45 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_high_10d_open | CEO only + Value ≥500k | high | 10 | open | 1 | 100.0 | 23.43 | 23.43 | 23.43 | nan | nan | 23.43 | 23.43 |
| 46 | 1 | 100.0 | CEO only + Position +10% — hold ret_high_10d_open | CEO only + Position +10% | high | 10 | open | 1 | 100.0 | 23.43 | 23.43 | 23.43 | nan | nan | 23.43 | 23.43 |
| 47 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_high_10d_open | Near 52w high + CEO/CFO | high | 10 | open | 1 | 100.0 | 23.43 | 23.43 | 23.43 | nan | nan | 23.43 | 23.43 |
| 48 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_high_14d_open | CEO only + Value ≥500k | high | 14 | open | 1 | 100.0 | 23.43 | 23.43 | 23.43 | nan | nan | 23.43 | 23.43 |
| 49 | 1 | 100.0 | CEO only + Position +10% — hold ret_high_14d_open | CEO only + Position +10% | high | 14 | open | 1 | 100.0 | 23.43 | 23.43 | 23.43 | nan | nan | 23.43 | 23.43 |
| 50 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_high_14d_open | Near 52w high + CEO/CFO | high | 14 | open | 1 | 100.0 | 23.43 | 23.43 | 23.43 | nan | nan | 23.43 | 23.43 |
| 51 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_high_30d_open | CEO only + Value ≥500k | high | 30 | open | 1 | 100.0 | 23.43 | 23.43 | 23.43 | nan | nan | 23.43 | 23.43 |
| 52 | 1 | 100.0 | CEO only + Position +10% — hold ret_high_30d_open | CEO only + Position +10% | high | 30 | open | 1 | 100.0 | 23.43 | 23.43 | 23.43 | nan | nan | 23.43 | 23.43 |
| 53 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_high_30d_open | Near 52w high + CEO/CFO | high | 30 | open | 1 | 100.0 | 23.43 | 23.43 | 23.43 | nan | nan | 23.43 | 23.43 |
| 54 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_high_60d_open | CEO only + Value ≥500k | high | 60 | open | 1 | 100.0 | 23.43 | 23.43 | 23.43 | nan | nan | 23.43 | 23.43 |
| 55 | 1 | 100.0 | CEO only + Position +10% — hold ret_high_60d_open | CEO only + Position +10% | high | 60 | open | 1 | 100.0 | 23.43 | 23.43 | 23.43 | nan | nan | 23.43 | 23.43 |
| 56 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_high_60d_open | Near 52w high + CEO/CFO | high | 60 | open | 1 | 100.0 | 23.43 | 23.43 | 23.43 | nan | nan | 23.43 | 23.43 |
| 57 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_high_90d_open | CEO only + Value ≥500k | high | 90 | open | 1 | 100.0 | 23.43 | 23.43 | 23.43 | nan | nan | 23.43 | 23.43 |
| 58 | 1 | 100.0 | CEO only + Position +10% — hold ret_high_90d_open | CEO only + Position +10% | high | 90 | open | 1 | 100.0 | 23.43 | 23.43 | 23.43 | nan | nan | 23.43 | 23.43 |
| 59 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_high_90d_open | Near 52w high + CEO/CFO | high | 90 | open | 1 | 100.0 | 23.43 | 23.43 | 23.43 | nan | nan | 23.43 | 23.43 |
| 60 | 10 | 66.41 | CEO/CFO — hold ret_high_60d_news | CEO/CFO | high | 60 | news | 4 | 100.0 | 22.7 | 20.16 | 90.79 | 11.65 | 1.95 | 12.37 | 38.1 |
| 61 | 11 | 66.41 | Officer/President — hold ret_high_60d_news | Officer/President | high | 60 | news | 4 | 100.0 | 22.7 | 20.16 | 90.79 | 11.65 | 1.95 | 12.37 | 38.1 |
| 62 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_high_60d_news | Large cap (≥250M) CEO/CFO | high | 60 | news | 4 | 100.0 | 22.7 | 20.16 | 90.79 | 11.65 | 1.95 | 12.37 | 38.1 |
| 63 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_high_60d_news | Large cap (≥500M) CEO/CFO | high | 60 | news | 4 | 100.0 | 22.7 | 20.16 | 90.79 | 11.65 | 1.95 | 12.37 | 38.1 |
| 64 | 10 | 66.41 | CEO/CFO — hold ret_high_60d_open | CEO/CFO | high | 60 | open | 4 | 100.0 | 22.66 | 20.88 | 90.65 | 12.58 | 1.8 | 9.46 | 39.42 |
| 65 | 11 | 66.41 | Officer/President — hold ret_high_60d_open | Officer/President | high | 60 | open | 4 | 100.0 | 22.66 | 20.88 | 90.65 | 12.58 | 1.8 | 9.46 | 39.42 |
| 66 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_high_60d_open | Large cap (≥250M) CEO/CFO | high | 60 | open | 4 | 100.0 | 22.66 | 20.88 | 90.65 | 12.58 | 1.8 | 9.46 | 39.42 |
| 67 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_high_60d_open | Large cap (≥500M) CEO/CFO | high | 60 | open | 4 | 100.0 | 22.66 | 20.88 | 90.65 | 12.58 | 1.8 | 9.46 | 39.42 |
| 68 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_high_5d_open | CEO only + Value ≥500k | high | 5 | open | 1 | 100.0 | 21.91 | 21.91 | 21.91 | nan | nan | 21.91 | 21.91 |
| 69 | 1 | 100.0 | CEO only + Position +10% — hold ret_high_5d_open | CEO only + Position +10% | high | 5 | open | 1 | 100.0 | 21.91 | 21.91 | 21.91 | nan | nan | 21.91 | 21.91 |
| 70 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_high_5d_open | Near 52w high + CEO/CFO | high | 5 | open | 1 | 100.0 | 21.91 | 21.91 | 21.91 | nan | nan | 21.91 | 21.91 |
| 71 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_high_90d_news | CEO only + Value ≥100k | high | 90 | news | 2 | 100.0 | 21.37 | 21.37 | 42.74 | 5.4 | 3.96 | 17.55 | 25.19 |
| 72 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_high_90d_news | Price > MA50 + CEO/CFO | high | 90 | news | 2 | 100.0 | 21.37 | 21.37 | 42.74 | 5.4 | 3.96 | 17.55 | 25.19 |
| 73 | 4 | 82.51 | CEO + Director (combo) — hold ret_mean_90d_open | CEO + Director (combo) | mean | 90 | open | 1 | 100.0 | 20.93 | 20.93 | 20.93 | nan | nan | 20.93 | 20.93 |
| 74 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_mean_90d_open | Small cap (≤1B) CEO/CFO | mean | 90 | open | 1 | 100.0 | 20.93 | 20.93 | 20.93 | nan | nan | 20.93 | 20.93 |
| 75 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_high_30d_open | Mid cap (1B–10B) CEO/CFO | high | 30 | open | 2 | 100.0 | 20.88 | 20.88 | 41.77 | 3.6 | 5.8 | 18.34 | 23.43 |
| 76 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_high_60d_open | Mid cap (1B–10B) CEO/CFO | high | 60 | open | 2 | 100.0 | 20.88 | 20.88 | 41.77 | 3.6 | 5.8 | 18.34 | 23.43 |
| 77 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_high_90d_open | Mid cap (1B–10B) CEO/CFO | high | 90 | open | 2 | 100.0 | 20.88 | 20.88 | 41.77 | 3.6 | 5.8 | 18.34 | 23.43 |
| 78 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_high_60d_open | Multiple buys (n≥2) | high | 60 | open | 3 | 100.0 | 20.77 | 18.34 | 62.3 | 17.57 | 1.18 | 4.54 | 39.42 |
| 79 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_high_90d_open | Multiple buys (n≥2) | high | 90 | open | 3 | 100.0 | 20.77 | 18.34 | 62.3 | 17.57 | 1.18 | 4.54 | 39.42 |
| 80 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_high_30d_news | Mid cap (1B–10B) CEO/CFO | high | 30 | news | 2 | 100.0 | 20.16 | 20.16 | 40.32 | 7.11 | 2.83 | 15.13 | 25.19 |
| 81 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_high_60d_news | Mid cap (1B–10B) CEO/CFO | high | 60 | news | 2 | 100.0 | 20.16 | 20.16 | 40.32 | 7.11 | 2.83 | 15.13 | 25.19 |
| 82 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_high_90d_news | Mid cap (1B–10B) CEO/CFO | high | 90 | news | 2 | 100.0 | 20.16 | 20.16 | 40.32 | 7.11 | 2.83 | 15.13 | 25.19 |
| 83 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_high_14d_open | Mid cap (1B–10B) CEO/CFO | high | 14 | open | 2 | 100.0 | 19.9 | 19.91 | 39.81 | 4.99 | 3.99 | 16.38 | 23.43 |
| 84 | 4 | 82.51 | CEO + Director (combo) — hold ret_high_30d_open | CEO + Director (combo) | high | 30 | open | 1 | 100.0 | 19.9 | 19.9 | 19.9 | nan | nan | 19.9 | 19.9 |
| 85 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_high_30d_open | Small cap (≤1B) CEO/CFO | high | 30 | open | 1 | 100.0 | 19.9 | 19.9 | 19.9 | nan | nan | 19.9 | 19.9 |
| 86 | 4 | 82.51 | CEO + Director (combo) — hold ret_mean_90d_news | CEO + Director (combo) | mean | 90 | news | 1 | 100.0 | 19.78 | 19.78 | 19.78 | nan | nan | 19.78 | 19.78 |
| 87 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_mean_90d_news | Small cap (≤1B) CEO/CFO | mean | 90 | news | 1 | 100.0 | 19.78 | 19.78 | 19.78 | nan | nan | 19.78 | 19.78 |
| 88 | 21 | 53.67 | Qty ≥5k shares — hold ret_high_90d_open | Qty ≥5k shares | high | 90 | open | 6 | 100.0 | 19.32 | 17.32 | 115.89 | 11.36 | 1.7 | 7.07 | 39.42 |
| 89 | 20 | 53.67 | Qty ≥10k shares — hold ret_high_90d_open | Qty ≥10k shares | high | 90 | open | 6 | 100.0 | 19.32 | 17.32 | 115.89 | 11.36 | 1.7 | 7.07 | 39.42 |
| 90 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_high_90d_news | CEO/CFO + Value ≥100k | high | 90 | news | 3 | 100.0 | 19.29 | 17.55 | 57.87 | 5.25 | 3.67 | 15.13 | 25.19 |
| 91 | 21 | 53.67 | Qty ≥5k shares — hold ret_high_90d_news | Qty ≥5k shares | high | 90 | news | 6 | 100.0 | 19.29 | 16.18 | 115.75 | 10.86 | 1.78 | 7.96 | 38.1 |
| 92 | 20 | 53.67 | Qty ≥10k shares — hold ret_high_90d_news | Qty ≥10k shares | high | 90 | news | 6 | 100.0 | 19.29 | 16.18 | 115.75 | 10.86 | 1.78 | 7.96 | 38.1 |
| 93 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_high_90d_news | Large cap (≥750M) CEO/CFO | high | 90 | news | 3 | 100.0 | 19.29 | 17.55 | 57.87 | 5.25 | 3.67 | 15.13 | 25.19 |
| 94 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_high_90d_news | Large cap (≥1B) CEO/CFO | high | 90 | news | 3 | 100.0 | 19.29 | 17.55 | 57.87 | 5.25 | 3.67 | 15.13 | 25.19 |
| 95 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_high_60d_news | Multiple buys (n≥2) | high | 60 | news | 3 | 100.0 | 19.26 | 15.13 | 57.77 | 17.16 | 1.12 | 4.54 | 38.1 |
| 96 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_high_90d_news | Multiple buys (n≥2) | high | 90 | news | 3 | 100.0 | 19.26 | 15.13 | 57.77 | 17.16 | 1.12 | 4.54 | 38.1 |
| 97 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_high_14d_news | Mid cap (1B–10B) CEO/CFO | high | 14 | news | 2 | 100.0 | 19.21 | 19.21 | 38.41 | 8.46 | 2.27 | 13.22 | 25.19 |
| 98 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_high_90d_open | CEO only + Value ≥100k | high | 90 | open | 2 | 100.0 | 18.96 | 18.96 | 37.93 | 6.31 | 3.0 | 14.5 | 23.43 |
| 99 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_high_90d_open | Price > MA50 + CEO/CFO | high | 90 | open | 2 | 100.0 | 18.96 | 18.96 | 37.93 | 6.31 | 3.0 | 14.5 | 23.43 |
| 100 | 21 | 53.67 | Qty ≥5k shares — hold ret_high_60d_open | Qty ≥5k shares | high | 60 | open | 6 | 100.0 | 18.92 | 16.14 | 113.52 | 11.52 | 1.64 | 7.07 | 39.42 |
| 101 | 20 | 53.67 | Qty ≥10k shares — hold ret_high_60d_open | Qty ≥10k shares | high | 60 | open | 6 | 100.0 | 18.92 | 16.14 | 113.52 | 11.52 | 1.64 | 7.07 | 39.42 |
| 102 | 21 | 53.67 | Qty ≥5k shares — hold ret_high_60d_news | Qty ≥5k shares | high | 60 | news | 6 | 100.0 | 18.89 | 14.98 | 113.36 | 10.99 | 1.72 | 7.96 | 38.1 |
| 103 | 20 | 53.67 | Qty ≥10k shares — hold ret_high_60d_news | Qty ≥10k shares | high | 60 | news | 6 | 100.0 | 18.89 | 14.98 | 113.36 | 10.99 | 1.72 | 7.96 | 38.1 |
| 104 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_high_7d_news | CEO only + Value ≥100k | high | 7 | news | 2 | 100.0 | 18.78 | 18.78 | 37.56 | 9.07 | 2.07 | 12.37 | 25.19 |
| 105 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_high_7d_news | Price > MA50 + CEO/CFO | high | 7 | news | 2 | 100.0 | 18.78 | 18.78 | 37.56 | 9.07 | 2.07 | 12.37 | 25.19 |
| 106 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_high_10d_news | CEO only + Value ≥100k | high | 10 | news | 2 | 100.0 | 18.78 | 18.78 | 37.56 | 9.07 | 2.07 | 12.37 | 25.19 |
| 107 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_high_10d_news | Price > MA50 + CEO/CFO | high | 10 | news | 2 | 100.0 | 18.78 | 18.78 | 37.56 | 9.07 | 2.07 | 12.37 | 25.19 |
| 108 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_high_14d_news | CEO only + Value ≥100k | high | 14 | news | 2 | 100.0 | 18.78 | 18.78 | 37.56 | 9.07 | 2.07 | 12.37 | 25.19 |
| 109 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_high_14d_news | Price > MA50 + CEO/CFO | high | 14 | news | 2 | 100.0 | 18.78 | 18.78 | 37.56 | 9.07 | 2.07 | 12.37 | 25.19 |
| 110 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_high_30d_news | CEO only + Value ≥100k | high | 30 | news | 2 | 100.0 | 18.78 | 18.78 | 37.56 | 9.07 | 2.07 | 12.37 | 25.19 |
| 111 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_high_30d_news | Price > MA50 + CEO/CFO | high | 30 | news | 2 | 100.0 | 18.78 | 18.78 | 37.56 | 9.07 | 2.07 | 12.37 | 25.19 |
| 112 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_high_60d_news | CEO only + Value ≥100k | high | 60 | news | 2 | 100.0 | 18.78 | 18.78 | 37.56 | 9.07 | 2.07 | 12.37 | 25.19 |
| 113 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_high_60d_news | Price > MA50 + CEO/CFO | high | 60 | news | 2 | 100.0 | 18.78 | 18.78 | 37.56 | 9.07 | 2.07 | 12.37 | 25.19 |
| 114 | 6 | 77.62 | CEO only — hold ret_high_30d_news | CEO only | high | 30 | news | 3 | 100.0 | 18.77 | 18.76 | 56.32 | 6.41 | 2.93 | 12.37 | 25.19 |
| 115 | 4 | 82.51 | CEO + Director (combo) — hold ret_high_30d_news | CEO + Director (combo) | high | 30 | news | 1 | 100.0 | 18.76 | 18.76 | 18.76 | nan | nan | 18.76 | 18.76 |
| 116 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_high_30d_news | Small cap (≤1B) CEO/CFO | high | 30 | news | 1 | 100.0 | 18.76 | 18.76 | 18.76 | nan | nan | 18.76 | 18.76 |
| 117 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_high_90d_open | CEO/CFO + Value ≥100k | high | 90 | open | 3 | 100.0 | 18.76 | 18.34 | 56.27 | 4.48 | 4.19 | 14.5 | 23.43 |
| 118 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_high_90d_open | Large cap (≥750M) CEO/CFO | high | 90 | open | 3 | 100.0 | 18.76 | 18.34 | 56.27 | 4.48 | 4.19 | 14.5 | 23.43 |
| 119 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_high_90d_open | Large cap (≥1B) CEO/CFO | high | 90 | open | 3 | 100.0 | 18.76 | 18.34 | 56.27 | 4.48 | 4.19 | 14.5 | 23.43 |
| 120 | 26 | 50.0 | Qty ≥50k shares — hold ret_high_7d_news | Qty ≥50k shares | high | 7 | news | 2 | 100.0 | 18.67 | 18.67 | 37.34 | 9.22 | 2.02 | 12.15 | 25.19 |
| 121 | 27 | 50.0 | Value ≥1M — hold ret_high_7d_news | Value ≥1M | high | 7 | news | 2 | 100.0 | 18.67 | 18.67 | 37.34 | 9.22 | 2.02 | 12.15 | 25.19 |
| 122 | 26 | 50.0 | Qty ≥50k shares — hold ret_high_10d_news | Qty ≥50k shares | high | 10 | news | 2 | 100.0 | 18.67 | 18.67 | 37.34 | 9.22 | 2.02 | 12.15 | 25.19 |
| 123 | 27 | 50.0 | Value ≥1M — hold ret_high_10d_news | Value ≥1M | high | 10 | news | 2 | 100.0 | 18.67 | 18.67 | 37.34 | 9.22 | 2.02 | 12.15 | 25.19 |
| 124 | 26 | 50.0 | Qty ≥50k shares — hold ret_high_14d_news | Qty ≥50k shares | high | 14 | news | 2 | 100.0 | 18.67 | 18.67 | 37.34 | 9.22 | 2.02 | 12.15 | 25.19 |
| 125 | 27 | 50.0 | Value ≥1M — hold ret_high_14d_news | Value ≥1M | high | 14 | news | 2 | 100.0 | 18.67 | 18.67 | 37.34 | 9.22 | 2.02 | 12.15 | 25.19 |
| 126 | 26 | 50.0 | Qty ≥50k shares — hold ret_high_30d_news | Qty ≥50k shares | high | 30 | news | 2 | 100.0 | 18.67 | 18.67 | 37.34 | 9.22 | 2.02 | 12.15 | 25.19 |
| 127 | 27 | 50.0 | Value ≥1M — hold ret_high_30d_news | Value ≥1M | high | 30 | news | 2 | 100.0 | 18.67 | 18.67 | 37.34 | 9.22 | 2.02 | 12.15 | 25.19 |
| 128 | 26 | 50.0 | Qty ≥50k shares — hold ret_high_60d_news | Qty ≥50k shares | high | 60 | news | 2 | 100.0 | 18.67 | 18.67 | 37.34 | 9.22 | 2.02 | 12.15 | 25.19 |
| 129 | 27 | 50.0 | Value ≥1M — hold ret_high_60d_news | Value ≥1M | high | 60 | news | 2 | 100.0 | 18.67 | 18.67 | 37.34 | 9.22 | 2.02 | 12.15 | 25.19 |
| 130 | 26 | 50.0 | Qty ≥50k shares — hold ret_high_90d_news | Qty ≥50k shares | high | 90 | news | 2 | 100.0 | 18.67 | 18.67 | 37.34 | 9.22 | 2.02 | 12.15 | 25.19 |
| 131 | 27 | 50.0 | Value ≥1M — hold ret_high_90d_news | Value ≥1M | high | 90 | news | 2 | 100.0 | 18.67 | 18.67 | 37.34 | 9.22 | 2.02 | 12.15 | 25.19 |
| 132 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_high_3d_news | CEO only + Value ≥500k | high | 3 | news | 1 | 100.0 | 18.36 | 18.36 | 18.36 | nan | nan | 18.36 | 18.36 |
| 133 | 1 | 100.0 | CEO only + Position +10% — hold ret_high_3d_news | CEO only + Position +10% | high | 3 | news | 1 | 100.0 | 18.36 | 18.36 | 18.36 | nan | nan | 18.36 | 18.36 |
| 134 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_high_3d_news | Near 52w high + CEO/CFO | high | 3 | news | 1 | 100.0 | 18.36 | 18.36 | 18.36 | nan | nan | 18.36 | 18.36 |
| 135 | 49 | 32.78 | CFO only — hold ret_high_30d_open | CFO only | high | 30 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 136 | 48 | 32.78 | CFO + Director (combo) — hold ret_high_30d_open | CFO + Director (combo) | high | 30 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 137 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_high_30d_open | CFO only + Value ≥50k | high | 30 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 138 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_high_30d_open | CFO only + Value ≥100k | high | 30 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 139 | 47 | 32.78 | CFO only + Position +10% — hold ret_high_30d_open | CFO only + Position +10% | high | 30 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 140 | 46 | 32.78 | CFO only + Position +20% — hold ret_high_30d_open | CFO only + Position +20% | high | 30 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 141 | 44 | 32.78 | RSI oversold (<30) — hold ret_high_30d_open | RSI oversold (<30) | high | 30 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 142 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_high_30d_open | RSI oversold + CEO/CFO | high | 30 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 143 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_high_30d_open | RSI oversold + Value ≥100k | high | 30 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 144 | 49 | 32.78 | CFO only — hold ret_high_60d_open | CFO only | high | 60 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 145 | 48 | 32.78 | CFO + Director (combo) — hold ret_high_60d_open | CFO + Director (combo) | high | 60 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 146 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_high_60d_open | CFO only + Value ≥50k | high | 60 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 147 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_high_60d_open | CFO only + Value ≥100k | high | 60 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 148 | 47 | 32.78 | CFO only + Position +10% — hold ret_high_60d_open | CFO only + Position +10% | high | 60 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 149 | 46 | 32.78 | CFO only + Position +20% — hold ret_high_60d_open | CFO only + Position +20% | high | 60 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 150 | 44 | 32.78 | RSI oversold (<30) — hold ret_high_60d_open | RSI oversold (<30) | high | 60 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 151 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_high_60d_open | RSI oversold + CEO/CFO | high | 60 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 152 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_high_60d_open | RSI oversold + Value ≥100k | high | 60 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 153 | 49 | 32.78 | CFO only — hold ret_high_90d_open | CFO only | high | 90 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 154 | 48 | 32.78 | CFO + Director (combo) — hold ret_high_90d_open | CFO + Director (combo) | high | 90 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 155 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_high_90d_open | CFO only + Value ≥50k | high | 90 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 156 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_high_90d_open | CFO only + Value ≥100k | high | 90 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 157 | 47 | 32.78 | CFO only + Position +10% — hold ret_high_90d_open | CFO only + Position +10% | high | 90 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 158 | 46 | 32.78 | CFO only + Position +20% — hold ret_high_90d_open | CFO only + Position +20% | high | 90 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 159 | 44 | 32.78 | RSI oversold (<30) — hold ret_high_90d_open | RSI oversold (<30) | high | 90 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 160 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_high_90d_open | RSI oversold + CEO/CFO | high | 90 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 161 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_high_90d_open | RSI oversold + Value ≥100k | high | 90 | open | 1 | 100.0 | 18.34 | 18.34 | 18.34 | nan | nan | 18.34 | 18.34 |
| 162 | 4 | 82.51 | CEO + Director (combo) — hold ret_high_14d_open | CEO + Director (combo) | high | 14 | open | 1 | 100.0 | 18.27 | 18.27 | 18.27 | nan | nan | 18.27 | 18.27 |
| 163 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_high_14d_open | Small cap (≤1B) CEO/CFO | high | 14 | open | 1 | 100.0 | 18.27 | 18.27 | 18.27 | nan | nan | 18.27 | 18.27 |
| 164 | 6 | 77.62 | CEO only — hold ret_high_14d_news | CEO only | high | 14 | news | 3 | 100.0 | 18.23 | 17.14 | 54.7 | 6.48 | 2.81 | 12.37 | 25.19 |
| 165 | 26 | 50.0 | Qty ≥50k shares — hold ret_high_5d_news | Qty ≥50k shares | high | 5 | news | 2 | 100.0 | 17.9 | 17.9 | 35.8 | 8.13 | 2.2 | 12.15 | 23.65 |
| 166 | 27 | 50.0 | Value ≥1M — hold ret_high_5d_news | Value ≥1M | high | 5 | news | 2 | 100.0 | 17.9 | 17.9 | 35.8 | 8.13 | 2.2 | 12.15 | 23.65 |
| 167 | 10 | 66.41 | CEO/CFO — hold ret_high_30d_news | CEO/CFO | high | 30 | news | 4 | 100.0 | 17.86 | 16.95 | 71.45 | 5.54 | 3.22 | 12.37 | 25.19 |
| 168 | 11 | 66.41 | Officer/President — hold ret_high_30d_news | Officer/President | high | 30 | news | 4 | 100.0 | 17.86 | 16.95 | 71.45 | 5.54 | 3.22 | 12.37 | 25.19 |
| 169 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_high_30d_news | Large cap (≥250M) CEO/CFO | high | 30 | news | 4 | 100.0 | 17.86 | 16.95 | 71.45 | 5.54 | 3.22 | 12.37 | 25.19 |
| 170 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_high_30d_news | Large cap (≥500M) CEO/CFO | high | 30 | news | 4 | 100.0 | 17.86 | 16.95 | 71.45 | 5.54 | 3.22 | 12.37 | 25.19 |
| 171 | 10 | 66.41 | CEO/CFO — hold ret_high_30d_open | CEO/CFO | high | 30 | open | 4 | 100.0 | 17.78 | 19.12 | 71.13 | 5.94 | 2.99 | 9.46 | 23.43 |
| 172 | 11 | 66.41 | Officer/President — hold ret_high_30d_open | Officer/President | high | 30 | open | 4 | 100.0 | 17.78 | 19.12 | 71.13 | 5.94 | 2.99 | 9.46 | 23.43 |
| 173 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_high_30d_open | Large cap (≥250M) CEO/CFO | high | 30 | open | 4 | 100.0 | 17.78 | 19.12 | 71.13 | 5.94 | 2.99 | 9.46 | 23.43 |
| 174 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_high_30d_open | Large cap (≥500M) CEO/CFO | high | 30 | open | 4 | 100.0 | 17.78 | 19.12 | 71.13 | 5.94 | 2.99 | 9.46 | 23.43 |
| 175 | 6 | 77.62 | CEO only — hold ret_high_30d_open | CEO only | high | 30 | open | 3 | 100.0 | 17.6 | 19.9 | 52.79 | 7.26 | 2.42 | 9.46 | 23.43 |
| 176 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_high_30d_news | CEO/CFO + Value ≥100k | high | 30 | news | 3 | 100.0 | 17.56 | 15.13 | 52.69 | 6.75 | 2.6 | 12.37 | 25.19 |
| 177 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_high_30d_news | Large cap (≥750M) CEO/CFO | high | 30 | news | 3 | 100.0 | 17.56 | 15.13 | 52.69 | 6.75 | 2.6 | 12.37 | 25.19 |
| 178 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_high_30d_news | Large cap (≥1B) CEO/CFO | high | 30 | news | 3 | 100.0 | 17.56 | 15.13 | 52.69 | 6.75 | 2.6 | 12.37 | 25.19 |
| 179 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_high_60d_news | CEO/CFO + Value ≥100k | high | 60 | news | 3 | 100.0 | 17.56 | 15.13 | 52.69 | 6.75 | 2.6 | 12.37 | 25.19 |
| 180 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_high_60d_news | Large cap (≥750M) CEO/CFO | high | 60 | news | 3 | 100.0 | 17.56 | 15.13 | 52.69 | 6.75 | 2.6 | 12.37 | 25.19 |
| 181 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_high_60d_news | Large cap (≥1B) CEO/CFO | high | 60 | news | 3 | 100.0 | 17.56 | 15.13 | 52.69 | 6.75 | 2.6 | 12.37 | 25.19 |
| 182 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_high_90d_news | Large cap (≥3B) CEO/CFO | high | 90 | news | 1 | 100.0 | 17.55 | 17.55 | 17.55 | nan | nan | 17.55 | 17.55 |
| 183 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_high_90d_news | Large cap (≥5B) CEO/CFO | high | 90 | news | 1 | 100.0 | 17.55 | 17.55 | 17.55 | nan | nan | 17.55 | 17.55 |
| 184 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_high_90d_news | Large cap (≥10B) CEO/CFO | high | 90 | news | 1 | 100.0 | 17.55 | 17.55 | 17.55 | nan | nan | 17.55 | 17.55 |
| 185 | 35 | 40.48 | Value ≥500k — hold ret_high_90d_news | Value ≥500k | high | 90 | news | 4 | 100.0 | 17.42 | 16.18 | 69.69 | 5.58 | 3.12 | 12.15 | 25.19 |
| 186 | 26 | 50.0 | Qty ≥50k shares — hold ret_high_7d_open | Qty ≥50k shares | high | 7 | open | 2 | 100.0 | 17.38 | 17.38 | 34.75 | 8.56 | 2.03 | 11.32 | 23.43 |
| 187 | 27 | 50.0 | Value ≥1M — hold ret_high_7d_open | Value ≥1M | high | 7 | open | 2 | 100.0 | 17.38 | 17.38 | 34.75 | 8.56 | 2.03 | 11.32 | 23.43 |
| 188 | 26 | 50.0 | Qty ≥50k shares — hold ret_high_10d_open | Qty ≥50k shares | high | 10 | open | 2 | 100.0 | 17.38 | 17.38 | 34.75 | 8.56 | 2.03 | 11.32 | 23.43 |
| 189 | 27 | 50.0 | Value ≥1M — hold ret_high_10d_open | Value ≥1M | high | 10 | open | 2 | 100.0 | 17.38 | 17.38 | 34.75 | 8.56 | 2.03 | 11.32 | 23.43 |
| 190 | 26 | 50.0 | Qty ≥50k shares — hold ret_high_14d_open | Qty ≥50k shares | high | 14 | open | 2 | 100.0 | 17.38 | 17.38 | 34.75 | 8.56 | 2.03 | 11.32 | 23.43 |
| 191 | 27 | 50.0 | Value ≥1M — hold ret_high_14d_open | Value ≥1M | high | 14 | open | 2 | 100.0 | 17.38 | 17.38 | 34.75 | 8.56 | 2.03 | 11.32 | 23.43 |
| 192 | 26 | 50.0 | Qty ≥50k shares — hold ret_high_30d_open | Qty ≥50k shares | high | 30 | open | 2 | 100.0 | 17.38 | 17.38 | 34.75 | 8.56 | 2.03 | 11.32 | 23.43 |
| 193 | 27 | 50.0 | Value ≥1M — hold ret_high_30d_open | Value ≥1M | high | 30 | open | 2 | 100.0 | 17.38 | 17.38 | 34.75 | 8.56 | 2.03 | 11.32 | 23.43 |
| 194 | 26 | 50.0 | Qty ≥50k shares — hold ret_high_60d_open | Qty ≥50k shares | high | 60 | open | 2 | 100.0 | 17.38 | 17.38 | 34.75 | 8.56 | 2.03 | 11.32 | 23.43 |
| 195 | 27 | 50.0 | Value ≥1M — hold ret_high_60d_open | Value ≥1M | high | 60 | open | 2 | 100.0 | 17.38 | 17.38 | 34.75 | 8.56 | 2.03 | 11.32 | 23.43 |
| 196 | 26 | 50.0 | Qty ≥50k shares — hold ret_high_90d_open | Qty ≥50k shares | high | 90 | open | 2 | 100.0 | 17.38 | 17.38 | 34.75 | 8.56 | 2.03 | 11.32 | 23.43 |
| 197 | 27 | 50.0 | Value ≥1M — hold ret_high_90d_open | Value ≥1M | high | 90 | open | 2 | 100.0 | 17.38 | 17.38 | 34.75 | 8.56 | 2.03 | 11.32 | 23.43 |
| 198 | 35 | 40.48 | Value ≥500k — hold ret_high_90d_open | Value ≥500k | high | 90 | open | 4 | 100.0 | 17.35 | 17.32 | 69.4 | 5.01 | 3.46 | 11.32 | 23.43 |
| 199 | 6 | 77.62 | CEO only — hold ret_high_10d_news | CEO only | high | 10 | news | 3 | 100.0 | 17.22 | 14.1 | 51.66 | 6.96 | 2.48 | 12.37 | 25.19 |
| 200 | 4 | 82.51 | CEO + Director (combo) — hold ret_high_14d_news | CEO + Director (combo) | high | 14 | news | 1 | 100.0 | 17.14 | 17.14 | 17.14 | nan | nan | 17.14 | 17.14 |
| 201 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_high_14d_news | Small cap (≤1B) CEO/CFO | high | 14 | news | 1 | 100.0 | 17.14 | 17.14 | 17.14 | nan | nan | 17.14 | 17.14 |
| 202 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_high_30d_open | CEO/CFO + Value ≥100k | high | 30 | open | 3 | 100.0 | 17.08 | 18.34 | 51.23 | 7.07 | 2.42 | 9.46 | 23.43 |
| 203 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_high_30d_open | Large cap (≥750M) CEO/CFO | high | 30 | open | 3 | 100.0 | 17.08 | 18.34 | 51.23 | 7.07 | 2.42 | 9.46 | 23.43 |
| 204 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_high_30d_open | Large cap (≥1B) CEO/CFO | high | 30 | open | 3 | 100.0 | 17.08 | 18.34 | 51.23 | 7.07 | 2.42 | 9.46 | 23.43 |
| 205 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_high_60d_open | CEO/CFO + Value ≥100k | high | 60 | open | 3 | 100.0 | 17.08 | 18.34 | 51.23 | 7.07 | 2.42 | 9.46 | 23.43 |
| 206 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_high_60d_open | Large cap (≥750M) CEO/CFO | high | 60 | open | 3 | 100.0 | 17.08 | 18.34 | 51.23 | 7.07 | 2.42 | 9.46 | 23.43 |
| 207 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_high_60d_open | Large cap (≥1B) CEO/CFO | high | 60 | open | 3 | 100.0 | 17.08 | 18.34 | 51.23 | 7.07 | 2.42 | 9.46 | 23.43 |
| 208 | 4 | 82.51 | CEO + Director (combo) — hold ret_mean_60d_open | CEO + Director (combo) | mean | 60 | open | 1 | 100.0 | 17.06 | 17.06 | 17.06 | nan | nan | 17.06 | 17.06 |
| 209 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_mean_60d_open | Small cap (≤1B) CEO/CFO | mean | 60 | open | 1 | 100.0 | 17.06 | 17.06 | 17.06 | nan | nan | 17.06 | 17.06 |
| 210 | 6 | 77.62 | CEO only — hold ret_high_14d_open | CEO only | high | 14 | open | 3 | 100.0 | 17.05 | 18.27 | 51.16 | 7.06 | 2.41 | 9.46 | 23.43 |
| 211 | 10 | 66.41 | CEO/CFO — hold ret_high_14d_news | CEO/CFO | high | 14 | news | 4 | 100.0 | 16.98 | 15.18 | 67.92 | 5.85 | 2.9 | 12.37 | 25.19 |
| 212 | 11 | 66.41 | Officer/President — hold ret_high_14d_news | Officer/President | high | 14 | news | 4 | 100.0 | 16.98 | 15.18 | 67.92 | 5.85 | 2.9 | 12.37 | 25.19 |
| 213 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_high_14d_news | Large cap (≥250M) CEO/CFO | high | 14 | news | 4 | 100.0 | 16.98 | 15.18 | 67.92 | 5.85 | 2.9 | 12.37 | 25.19 |
| 214 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_high_14d_news | Large cap (≥500M) CEO/CFO | high | 14 | news | 4 | 100.0 | 16.98 | 15.18 | 67.92 | 5.85 | 2.9 | 12.37 | 25.19 |
| 215 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_high_14d_news | CEO/CFO + Value ≥100k | high | 14 | news | 3 | 100.0 | 16.93 | 13.22 | 50.78 | 7.17 | 2.36 | 12.37 | 25.19 |
| 216 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_high_14d_news | Large cap (≥750M) CEO/CFO | high | 14 | news | 3 | 100.0 | 16.93 | 13.22 | 50.78 | 7.17 | 2.36 | 12.37 | 25.19 |
| 217 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_high_14d_news | Large cap (≥1B) CEO/CFO | high | 14 | news | 3 | 100.0 | 16.93 | 13.22 | 50.78 | 7.17 | 2.36 | 12.37 | 25.19 |
| 218 | 10 | 66.41 | CEO/CFO — hold ret_high_14d_open | CEO/CFO | high | 14 | open | 4 | 100.0 | 16.88 | 17.32 | 67.54 | 5.78 | 2.92 | 9.46 | 23.43 |
| 219 | 11 | 66.41 | Officer/President — hold ret_high_14d_open | Officer/President | high | 14 | open | 4 | 100.0 | 16.88 | 17.32 | 67.54 | 5.78 | 2.92 | 9.46 | 23.43 |
| 220 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_high_14d_open | Large cap (≥250M) CEO/CFO | high | 14 | open | 4 | 100.0 | 16.88 | 17.32 | 67.54 | 5.78 | 2.92 | 9.46 | 23.43 |
| 221 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_high_14d_open | Large cap (≥500M) CEO/CFO | high | 14 | open | 4 | 100.0 | 16.88 | 17.32 | 67.54 | 5.78 | 2.92 | 9.46 | 23.43 |
| 222 | 38 | 34.53 | Price < MA50 — hold ret_high_60d_open | Price < MA50 | high | 60 | open | 5 | 100.0 | 16.84 | 11.32 | 84.18 | 13.54 | 1.24 | 4.54 | 39.42 |
| 223 | 38 | 34.53 | Price < MA50 — hold ret_high_90d_open | Price < MA50 | high | 90 | open | 5 | 100.0 | 16.84 | 11.32 | 84.18 | 13.54 | 1.24 | 4.54 | 39.42 |
| 224 | 35 | 40.48 | Value ≥500k — hold ret_high_60d_news | Value ≥500k | high | 60 | news | 4 | 100.0 | 16.82 | 14.98 | 67.3 | 5.74 | 2.93 | 12.15 | 25.19 |
| 225 | 15 | 62.43 | Price > MA50 — hold ret_high_90d_news | Price > MA50 | high | 90 | news | 5 | 100.0 | 16.8 | 17.22 | 83.98 | 6.12 | 2.74 | 7.96 | 25.19 |
| 226 | 35 | 40.48 | Value ≥500k — hold ret_high_60d_open | Value ≥500k | high | 60 | open | 4 | 100.0 | 16.76 | 16.14 | 67.03 | 5.31 | 3.16 | 11.32 | 23.43 |
| 227 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_high_3d_open | CEO only + Value ≥500k | high | 3 | open | 1 | 100.0 | 16.69 | 16.69 | 16.69 | nan | nan | 16.69 | 16.69 |
| 228 | 1 | 100.0 | CEO only + Position +10% — hold ret_high_3d_open | CEO only + Position +10% | high | 3 | open | 1 | 100.0 | 16.69 | 16.69 | 16.69 | nan | nan | 16.69 | 16.69 |
| 229 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_high_3d_open | Near 52w high + CEO/CFO | high | 3 | open | 1 | 100.0 | 16.69 | 16.69 | 16.69 | nan | nan | 16.69 | 16.69 |
| 230 | 26 | 50.0 | Qty ≥50k shares — hold ret_high_5d_open | Qty ≥50k shares | high | 5 | open | 2 | 100.0 | 16.62 | 16.62 | 33.23 | 7.49 | 2.22 | 11.32 | 21.91 |
| 231 | 27 | 50.0 | Value ≥1M — hold ret_high_5d_open | Value ≥1M | high | 5 | open | 2 | 100.0 | 16.62 | 16.62 | 33.23 | 7.49 | 2.22 | 11.32 | 21.91 |
| 232 | 14 | 65.45 | Price > MA200 — hold ret_high_90d_news | Price > MA200 | high | 90 | news | 4 | 100.0 | 16.61 | 16.64 | 66.43 | 7.05 | 2.36 | 7.96 | 25.19 |
| 233 | 31 | 47.75 | Value ≥50k — hold ret_high_90d_news | Value ≥50k | high | 90 | news | 9 | 100.0 | 16.46 | 15.13 | 148.15 | 10.12 | 1.63 | 4.54 | 38.1 |
| 234 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_high_7d_open | CEO only + Value ≥100k | high | 7 | open | 2 | 100.0 | 16.44 | 16.45 | 32.89 | 9.88 | 1.66 | 9.46 | 23.43 |
| 235 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_high_7d_open | Price > MA50 + CEO/CFO | high | 7 | open | 2 | 100.0 | 16.44 | 16.45 | 32.89 | 9.88 | 1.66 | 9.46 | 23.43 |
| 236 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_high_10d_open | CEO only + Value ≥100k | high | 10 | open | 2 | 100.0 | 16.44 | 16.45 | 32.89 | 9.88 | 1.66 | 9.46 | 23.43 |
| 237 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_high_10d_open | Price > MA50 + CEO/CFO | high | 10 | open | 2 | 100.0 | 16.44 | 16.45 | 32.89 | 9.88 | 1.66 | 9.46 | 23.43 |
| 238 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_high_14d_open | CEO only + Value ≥100k | high | 14 | open | 2 | 100.0 | 16.44 | 16.45 | 32.89 | 9.88 | 1.66 | 9.46 | 23.43 |
| 239 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_high_14d_open | Price > MA50 + CEO/CFO | high | 14 | open | 2 | 100.0 | 16.44 | 16.45 | 32.89 | 9.88 | 1.66 | 9.46 | 23.43 |
| 240 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_high_30d_open | CEO only + Value ≥100k | high | 30 | open | 2 | 100.0 | 16.44 | 16.45 | 32.89 | 9.88 | 1.66 | 9.46 | 23.43 |
| 241 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_high_30d_open | Price > MA50 + CEO/CFO | high | 30 | open | 2 | 100.0 | 16.44 | 16.45 | 32.89 | 9.88 | 1.66 | 9.46 | 23.43 |
| 242 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_high_60d_open | CEO only + Value ≥100k | high | 60 | open | 2 | 100.0 | 16.44 | 16.45 | 32.89 | 9.88 | 1.66 | 9.46 | 23.43 |
| 243 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_high_60d_open | Price > MA50 + CEO/CFO | high | 60 | open | 2 | 100.0 | 16.44 | 16.45 | 32.89 | 9.88 | 1.66 | 9.46 | 23.43 |
| 244 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_high_14d_open | CEO/CFO + Value ≥100k | high | 14 | open | 3 | 100.0 | 16.42 | 16.38 | 49.27 | 6.99 | 2.35 | 9.46 | 23.43 |
| 245 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_high_14d_open | Large cap (≥750M) CEO/CFO | high | 14 | open | 3 | 100.0 | 16.42 | 16.38 | 49.27 | 6.99 | 2.35 | 9.46 | 23.43 |
| 246 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_high_14d_open | Large cap (≥1B) CEO/CFO | high | 14 | open | 3 | 100.0 | 16.42 | 16.38 | 49.27 | 6.99 | 2.35 | 9.46 | 23.43 |
| 247 | 28 | 48.48 | Tutti — hold ret_high_90d_news | Tutti | high | 90 | news | 10 | 100.0 | 16.42 | 15.59 | 164.21 | 9.54 | 1.72 | 4.54 | 38.1 |
| 248 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_high_90d_open | Large cap (≥2B) CEO/CFO | high | 90 | open | 2 | 100.0 | 16.42 | 16.42 | 32.84 | 2.72 | 6.05 | 14.5 | 18.34 |
| 249 | 49 | 32.78 | CFO only — hold ret_high_14d_open | CFO only | high | 14 | open | 1 | 100.0 | 16.38 | 16.38 | 16.38 | nan | nan | 16.38 | 16.38 |
| 250 | 48 | 32.78 | CFO + Director (combo) — hold ret_high_14d_open | CFO + Director (combo) | high | 14 | open | 1 | 100.0 | 16.38 | 16.38 | 16.38 | nan | nan | 16.38 | 16.38 |
| 251 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_high_14d_open | CFO only + Value ≥50k | high | 14 | open | 1 | 100.0 | 16.38 | 16.38 | 16.38 | nan | nan | 16.38 | 16.38 |
| 252 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_high_14d_open | CFO only + Value ≥100k | high | 14 | open | 1 | 100.0 | 16.38 | 16.38 | 16.38 | nan | nan | 16.38 | 16.38 |
| 253 | 47 | 32.78 | CFO only + Position +10% — hold ret_high_14d_open | CFO only + Position +10% | high | 14 | open | 1 | 100.0 | 16.38 | 16.38 | 16.38 | nan | nan | 16.38 | 16.38 |
| 254 | 46 | 32.78 | CFO only + Position +20% — hold ret_high_14d_open | CFO only + Position +20% | high | 14 | open | 1 | 100.0 | 16.38 | 16.38 | 16.38 | nan | nan | 16.38 | 16.38 |
| 255 | 44 | 32.78 | RSI oversold (<30) — hold ret_high_14d_open | RSI oversold (<30) | high | 14 | open | 1 | 100.0 | 16.38 | 16.38 | 16.38 | nan | nan | 16.38 | 16.38 |
| 256 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_high_14d_open | RSI oversold + CEO/CFO | high | 14 | open | 1 | 100.0 | 16.38 | 16.38 | 16.38 | nan | nan | 16.38 | 16.38 |
| 257 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_high_14d_open | RSI oversold + Value ≥100k | high | 14 | open | 1 | 100.0 | 16.38 | 16.38 | 16.38 | nan | nan | 16.38 | 16.38 |
| 258 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_high_90d_news | Mid cap (1B–10B) Value ≥100k | high | 90 | news | 4 | 100.0 | 16.38 | 16.18 | 65.5 | 7.09 | 2.31 | 7.96 | 25.19 |
| 259 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_high_90d_news | Large cap (≥2B) CEO/CFO | high | 90 | news | 2 | 100.0 | 16.34 | 16.34 | 32.68 | 1.71 | 9.55 | 15.13 | 17.55 |
| 260 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_high_90d_open | Mid cap (1B–10B) Value ≥100k | high | 90 | open | 4 | 100.0 | 16.29 | 17.32 | 65.15 | 6.84 | 2.38 | 7.07 | 23.43 |
| 261 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_high_5d_news | CEO only + Value ≥100k | high | 5 | news | 2 | 100.0 | 16.27 | 16.27 | 32.54 | 10.44 | 1.56 | 8.89 | 23.65 |
| 262 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_high_5d_news | Price > MA50 + CEO/CFO | high | 5 | news | 2 | 100.0 | 16.27 | 16.27 | 32.54 | 10.44 | 1.56 | 8.89 | 23.65 |
| 263 | 31 | 47.75 | Value ≥50k — hold ret_high_90d_open | Value ≥50k | high | 90 | open | 9 | 100.0 | 16.17 | 14.5 | 145.49 | 10.45 | 1.55 | 4.54 | 39.42 |
| 264 | 28 | 48.48 | Tutti — hold ret_high_90d_open | Tutti | high | 90 | open | 10 | 100.0 | 16.16 | 15.28 | 161.55 | 9.85 | 1.64 | 4.54 | 39.42 |
| 265 | 38 | 34.53 | Price < MA50 — hold ret_high_60d_news | Price < MA50 | high | 60 | news | 5 | 100.0 | 16.05 | 12.15 | 80.23 | 12.92 | 1.24 | 4.54 | 38.1 |
| 266 | 38 | 34.53 | Price < MA50 — hold ret_high_90d_news | Price < MA50 | high | 90 | news | 5 | 100.0 | 16.05 | 12.15 | 80.23 | 12.92 | 1.24 | 4.54 | 38.1 |
| 267 | 6 | 77.62 | CEO only — hold ret_high_10d_open | CEO only | high | 10 | open | 3 | 100.0 | 16.03 | 15.19 | 48.08 | 7.02 | 2.28 | 9.46 | 23.43 |
| 268 | 14 | 65.45 | Price > MA200 — hold ret_high_60d_news | Price > MA200 | high | 60 | news | 4 | 100.0 | 16.01 | 15.45 | 64.04 | 7.08 | 2.26 | 7.96 | 25.19 |
| 269 | 4 | 82.51 | CEO + Director (combo) — hold ret_mean_60d_news | CEO + Director (combo) | mean | 60 | news | 1 | 100.0 | 15.95 | 15.95 | 15.95 | nan | nan | 15.95 | 15.95 |
| 270 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_mean_60d_news | Small cap (≤1B) CEO/CFO | mean | 60 | news | 1 | 100.0 | 15.95 | 15.95 | 15.95 | nan | nan | 15.95 | 15.95 |
| 271 | 30 | 48.32 | Value ≥100k — hold ret_high_90d_news | Value ≥100k | high | 90 | news | 6 | 100.0 | 15.87 | 16.18 | 95.2 | 5.8 | 2.73 | 7.96 | 25.19 |
| 272 | 6 | 77.62 | CEO only — hold ret_high_7d_news | CEO only | high | 7 | news | 3 | 100.0 | 15.82 | 12.37 | 47.46 | 8.21 | 1.93 | 9.9 | 25.19 |
| 273 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_high_60d_news | Mid cap (1B–10B) Value ≥100k | high | 60 | news | 4 | 100.0 | 15.78 | 14.98 | 63.11 | 7.1 | 2.22 | 7.96 | 25.19 |
| 274 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_high_7d_open | Mid cap (1B–10B) CEO/CFO | high | 7 | open | 2 | 100.0 | 15.76 | 15.75 | 31.51 | 10.85 | 1.45 | 8.08 | 23.43 |
| 275 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_high_10d_open | Mid cap (1B–10B) CEO/CFO | high | 10 | open | 2 | 100.0 | 15.76 | 15.75 | 31.51 | 10.85 | 1.45 | 8.08 | 23.43 |
| 276 | 14 | 65.45 | Price > MA200 — hold ret_high_90d_open | Price > MA200 | high | 90 | open | 4 | 100.0 | 15.72 | 16.18 | 62.87 | 6.7 | 2.35 | 7.07 | 23.43 |
| 277 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_high_60d_open | Mid cap (1B–10B) Value ≥100k | high | 60 | open | 4 | 100.0 | 15.7 | 16.14 | 62.78 | 6.94 | 2.26 | 7.07 | 23.43 |
| 278 | 28 | 48.48 | Tutti — hold ret_high_60d_news | Tutti | high | 60 | news | 10 | 100.0 | 15.66 | 13.6 | 156.64 | 9.6 | 1.63 | 4.54 | 38.1 |
| 279 | 31 | 47.75 | Value ≥50k — hold ret_high_60d_news | Value ≥50k | high | 60 | news | 9 | 100.0 | 15.62 | 12.37 | 140.58 | 10.19 | 1.53 | 4.54 | 38.1 |
| 280 | 15 | 62.43 | Price > MA50 — hold ret_high_90d_open | Price > MA50 | high | 90 | open | 5 | 100.0 | 15.47 | 16.06 | 77.37 | 5.83 | 2.65 | 7.07 | 23.43 |
| 281 | 33 | 41.81 | Director — hold ret_high_90d_open | Director | high | 90 | open | 8 | 100.0 | 15.45 | 13.69 | 123.62 | 10.79 | 1.43 | 4.54 | 39.42 |
| 282 | 28 | 48.48 | Tutti — hold ret_high_60d_open | Tutti | high | 60 | open | 10 | 100.0 | 15.41 | 12.63 | 154.14 | 10.08 | 1.53 | 4.54 | 39.42 |
| 283 | 31 | 47.75 | Value ≥50k — hold ret_high_60d_open | Value ≥50k | high | 60 | open | 9 | 100.0 | 15.34 | 11.32 | 138.08 | 10.69 | 1.43 | 4.54 | 39.42 |
| 284 | 15 | 62.43 | Price > MA50 — hold ret_high_60d_news | Price > MA50 | high | 60 | news | 5 | 100.0 | 15.28 | 14.83 | 76.41 | 6.35 | 2.41 | 7.96 | 25.19 |
| 285 | 26 | 50.0 | Qty ≥50k shares — hold ret_high_3d_news | Qty ≥50k shares | high | 3 | news | 2 | 100.0 | 15.26 | 15.25 | 30.51 | 4.39 | 3.47 | 12.15 | 18.36 |
| 286 | 27 | 50.0 | Value ≥1M — hold ret_high_3d_news | Value ≥1M | high | 3 | news | 2 | 100.0 | 15.26 | 15.25 | 30.51 | 4.39 | 3.47 | 12.15 | 18.36 |
| 287 | 4 | 82.51 | CEO + Director (combo) — hold ret_high_10d_open | CEO + Director (combo) | high | 10 | open | 1 | 100.0 | 15.19 | 15.19 | 15.19 | nan | nan | 15.19 | 15.19 |
| 288 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_high_10d_open | Small cap (≤1B) CEO/CFO | high | 10 | open | 1 | 100.0 | 15.19 | 15.19 | 15.19 | nan | nan | 15.19 | 15.19 |
| 289 | 33 | 41.81 | Director — hold ret_high_90d_news | Director | high | 90 | news | 8 | 100.0 | 15.18 | 13.64 | 121.47 | 10.2 | 1.49 | 4.54 | 38.1 |
| 290 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_high_7d_news | Mid cap (1B–10B) CEO/CFO | high | 7 | news | 2 | 100.0 | 15.17 | 15.17 | 30.34 | 14.17 | 1.07 | 5.15 | 25.19 |
| 291 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_high_10d_news | Mid cap (1B–10B) CEO/CFO | high | 10 | news | 2 | 100.0 | 15.17 | 15.17 | 30.34 | 14.17 | 1.07 | 5.15 | 25.19 |
| 292 | 33 | 41.81 | Director — hold ret_high_60d_open | Director | high | 60 | open | 8 | 100.0 | 15.16 | 12.63 | 121.25 | 10.79 | 1.4 | 4.54 | 39.42 |
| 293 | 30 | 48.32 | Value ≥100k — hold ret_high_90d_open | Value ≥100k | high | 90 | open | 6 | 100.0 | 15.16 | 15.4 | 90.97 | 5.66 | 2.68 | 7.07 | 23.43 |
| 294 | 49 | 32.78 | CFO only — hold ret_high_30d_news | CFO only | high | 30 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 295 | 48 | 32.78 | CFO + Director (combo) — hold ret_high_30d_news | CFO + Director (combo) | high | 30 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 296 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_high_30d_news | CFO only + Value ≥50k | high | 30 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 297 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_high_30d_news | CFO only + Value ≥100k | high | 30 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 298 | 47 | 32.78 | CFO only + Position +10% — hold ret_high_30d_news | CFO only + Position +10% | high | 30 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 299 | 46 | 32.78 | CFO only + Position +20% — hold ret_high_30d_news | CFO only + Position +20% | high | 30 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 300 | 44 | 32.78 | RSI oversold (<30) — hold ret_high_30d_news | RSI oversold (<30) | high | 30 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 301 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_high_30d_news | RSI oversold + CEO/CFO | high | 30 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 302 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_high_30d_news | RSI oversold + Value ≥100k | high | 30 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 303 | 49 | 32.78 | CFO only — hold ret_high_60d_news | CFO only | high | 60 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 304 | 48 | 32.78 | CFO + Director (combo) — hold ret_high_60d_news | CFO + Director (combo) | high | 60 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 305 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_high_60d_news | CFO only + Value ≥50k | high | 60 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 306 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_high_60d_news | CFO only + Value ≥100k | high | 60 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 307 | 47 | 32.78 | CFO only + Position +10% — hold ret_high_60d_news | CFO only + Position +10% | high | 60 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 308 | 46 | 32.78 | CFO only + Position +20% — hold ret_high_60d_news | CFO only + Position +20% | high | 60 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 309 | 44 | 32.78 | RSI oversold (<30) — hold ret_high_60d_news | RSI oversold (<30) | high | 60 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 310 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_high_60d_news | RSI oversold + CEO/CFO | high | 60 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 311 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_high_60d_news | RSI oversold + Value ≥100k | high | 60 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 312 | 49 | 32.78 | CFO only — hold ret_high_90d_news | CFO only | high | 90 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 313 | 48 | 32.78 | CFO + Director (combo) — hold ret_high_90d_news | CFO + Director (combo) | high | 90 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 314 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_high_90d_news | CFO only + Value ≥50k | high | 90 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 315 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_high_90d_news | CFO only + Value ≥100k | high | 90 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 316 | 47 | 32.78 | CFO only + Position +10% — hold ret_high_90d_news | CFO only + Position +10% | high | 90 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 317 | 46 | 32.78 | CFO only + Position +20% — hold ret_high_90d_news | CFO only + Position +20% | high | 90 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 318 | 44 | 32.78 | RSI oversold (<30) — hold ret_high_90d_news | RSI oversold (<30) | high | 90 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 319 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_high_90d_news | RSI oversold + CEO/CFO | high | 90 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 320 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_high_90d_news | RSI oversold + Value ≥100k | high | 90 | news | 1 | 100.0 | 15.13 | 15.13 | 15.13 | nan | nan | 15.13 | 15.13 |
| 321 | 14 | 65.45 | Price > MA200 — hold ret_high_60d_open | Price > MA200 | high | 60 | open | 4 | 100.0 | 15.12 | 15.0 | 60.5 | 6.74 | 2.25 | 7.07 | 23.43 |
| 322 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_high_2d_news | CEO only + Value ≥500k | high | 2 | news | 1 | 100.0 | 15.02 | 15.02 | 15.02 | nan | nan | 15.02 | 15.02 |
| 323 | 1 | 100.0 | CEO only + Position +10% — hold ret_high_2d_news | CEO only + Position +10% | high | 2 | news | 1 | 100.0 | 15.02 | 15.02 | 15.02 | nan | nan | 15.02 | 15.02 |
| 324 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_high_2d_news | Near 52w high + CEO/CFO | high | 2 | news | 1 | 100.0 | 15.02 | 15.02 | 15.02 | nan | nan | 15.02 | 15.02 |
| 325 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_high_90d_news | Far 52w high + Value ≥100k | high | 90 | news | 3 | 100.0 | 14.94 | 15.13 | 44.83 | 2.7 | 5.52 | 12.15 | 17.55 |
| 326 | 35 | 40.48 | Value ≥500k — hold ret_high_30d_news | Value ≥500k | high | 30 | news | 4 | 100.0 | 14.9 | 13.64 | 59.6 | 7.61 | 1.96 | 7.13 | 25.19 |
| 327 | 33 | 41.81 | Director — hold ret_high_60d_news | Director | high | 60 | news | 8 | 100.0 | 14.88 | 13.49 | 119.08 | 10.17 | 1.46 | 4.54 | 38.1 |
| 328 | 35 | 40.48 | Value ≥500k — hold ret_high_30d_open | Value ≥500k | high | 30 | open | 4 | 100.0 | 14.85 | 14.83 | 59.39 | 7.56 | 1.96 | 6.3 | 23.43 |
| 329 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_high_90d_open | Far 52w high + Value ≥100k | high | 90 | open | 3 | 100.0 | 14.72 | 14.5 | 44.16 | 3.52 | 4.19 | 11.32 | 18.34 |
| 330 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_mean_10d_news | CEO only + Value ≥500k | mean | 10 | news | 1 | 100.0 | 14.68 | 14.68 | 14.68 | nan | nan | 14.68 | 14.68 |
| 331 | 1 | 100.0 | CEO only + Position +10% — hold ret_mean_10d_news | CEO only + Position +10% | mean | 10 | news | 1 | 100.0 | 14.68 | 14.68 | 14.68 | nan | nan | 14.68 | 14.68 |
| 332 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_mean_10d_news | Near 52w high + CEO/CFO | mean | 10 | news | 1 | 100.0 | 14.68 | 14.68 | 14.68 | nan | nan | 14.68 | 14.68 |
| 333 | 6 | 77.62 | CEO only — hold ret_high_7d_open | CEO only | high | 7 | open | 3 | 100.0 | 14.62 | 10.96 | 43.85 | 7.67 | 1.91 | 9.46 | 23.43 |
| 334 | 30 | 48.32 | Value ≥100k — hold ret_high_60d_news | Value ≥100k | high | 60 | news | 6 | 100.0 | 14.61 | 13.6 | 87.63 | 5.79 | 2.52 | 7.96 | 25.19 |
| 335 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_high_90d_open | Large cap (≥3B) CEO/CFO | high | 90 | open | 1 | 100.0 | 14.5 | 14.5 | 14.5 | nan | nan | 14.5 | 14.5 |
| 336 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_high_90d_open | Large cap (≥5B) CEO/CFO | high | 90 | open | 1 | 100.0 | 14.5 | 14.5 | 14.5 | nan | nan | 14.5 | 14.5 |
| 337 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_high_90d_open | Large cap (≥10B) CEO/CFO | high | 90 | open | 1 | 100.0 | 14.5 | 14.5 | 14.5 | nan | nan | 14.5 | 14.5 |
| 338 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_mean_14d_news | CEO only + Value ≥500k | mean | 14 | news | 1 | 100.0 | 14.49 | 14.49 | 14.49 | nan | nan | 14.49 | 14.49 |
| 339 | 1 | 100.0 | CEO only + Position +10% — hold ret_mean_14d_news | CEO only + Position +10% | mean | 14 | news | 1 | 100.0 | 14.49 | 14.49 | 14.49 | nan | nan | 14.49 | 14.49 |
| 340 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_mean_14d_news | Near 52w high + CEO/CFO | mean | 14 | news | 1 | 100.0 | 14.49 | 14.49 | 14.49 | nan | nan | 14.49 | 14.49 |
| 341 | 21 | 53.67 | Qty ≥5k shares — hold ret_high_30d_open | Qty ≥5k shares | high | 30 | open | 6 | 100.0 | 14.39 | 14.83 | 86.36 | 7.16 | 2.01 | 6.3 | 23.43 |
| 342 | 21 | 53.67 | Qty ≥5k shares — hold ret_high_30d_news | Qty ≥5k shares | high | 30 | news | 6 | 100.0 | 14.39 | 13.64 | 86.32 | 6.86 | 2.1 | 7.13 | 25.19 |
| 343 | 20 | 53.67 | Qty ≥10k shares — hold ret_high_30d_open | Qty ≥10k shares | high | 30 | open | 6 | 100.0 | 14.39 | 14.83 | 86.36 | 7.16 | 2.01 | 6.3 | 23.43 |
| 344 | 20 | 53.67 | Qty ≥10k shares — hold ret_high_30d_news | Qty ≥10k shares | high | 30 | news | 6 | 100.0 | 14.39 | 13.64 | 86.32 | 6.86 | 2.1 | 7.13 | 25.19 |
| 345 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_high_30d_open | Multiple buys (n≥2) | high | 30 | open | 3 | 100.0 | 14.26 | 18.34 | 42.78 | 8.45 | 1.69 | 4.54 | 19.9 |
| 346 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_high_7d_news | CEO/CFO + Value ≥100k | high | 7 | news | 3 | 100.0 | 14.24 | 12.37 | 42.71 | 10.15 | 1.4 | 5.15 | 25.19 |
| 347 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_high_7d_news | Large cap (≥750M) CEO/CFO | high | 7 | news | 3 | 100.0 | 14.24 | 12.37 | 42.71 | 10.15 | 1.4 | 5.15 | 25.19 |
| 348 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_high_7d_news | Large cap (≥1B) CEO/CFO | high | 7 | news | 3 | 100.0 | 14.24 | 12.37 | 42.71 | 10.15 | 1.4 | 5.15 | 25.19 |
| 349 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_high_10d_news | CEO/CFO + Value ≥100k | high | 10 | news | 3 | 100.0 | 14.24 | 12.37 | 42.71 | 10.15 | 1.4 | 5.15 | 25.19 |
| 350 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_high_10d_news | Large cap (≥750M) CEO/CFO | high | 10 | news | 3 | 100.0 | 14.24 | 12.37 | 42.71 | 10.15 | 1.4 | 5.15 | 25.19 |
| 351 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_high_10d_news | Large cap (≥1B) CEO/CFO | high | 10 | news | 3 | 100.0 | 14.24 | 12.37 | 42.71 | 10.15 | 1.4 | 5.15 | 25.19 |
| 352 | 10 | 66.41 | CEO/CFO — hold ret_high_10d_news | CEO/CFO | high | 10 | news | 4 | 100.0 | 14.2 | 13.23 | 56.81 | 8.29 | 1.71 | 5.15 | 25.19 |
| 353 | 11 | 66.41 | Officer/President — hold ret_high_10d_news | Officer/President | high | 10 | news | 4 | 100.0 | 14.2 | 13.23 | 56.81 | 8.29 | 1.71 | 5.15 | 25.19 |
| 354 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_high_10d_news | Large cap (≥250M) CEO/CFO | high | 10 | news | 4 | 100.0 | 14.2 | 13.23 | 56.81 | 8.29 | 1.71 | 5.15 | 25.19 |
| 355 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_high_10d_news | Large cap (≥500M) CEO/CFO | high | 10 | news | 4 | 100.0 | 14.2 | 13.23 | 56.81 | 8.29 | 1.71 | 5.15 | 25.19 |
| 356 | 4 | 82.51 | CEO + Director (combo) — hold ret_high_10d_news | CEO + Director (combo) | high | 10 | news | 1 | 100.0 | 14.1 | 14.1 | 14.1 | nan | nan | 14.1 | 14.1 |
| 357 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_high_10d_news | Small cap (≤1B) CEO/CFO | high | 10 | news | 1 | 100.0 | 14.1 | 14.1 | 14.1 | nan | nan | 14.1 | 14.1 |
| 358 | 14 | 65.45 | Price > MA200 — hold ret_high_30d_news | Price > MA200 | high | 30 | news | 4 | 100.0 | 14.08 | 12.01 | 56.34 | 8.43 | 1.67 | 7.13 | 25.19 |
| 359 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_high_5d_open | Mid cap (1B–10B) CEO/CFO | high | 5 | open | 2 | 100.0 | 14.06 | 14.06 | 28.13 | 11.09 | 1.27 | 6.22 | 21.91 |
| 360 | 10 | 66.41 | CEO/CFO — hold ret_high_10d_open | CEO/CFO | high | 10 | open | 4 | 100.0 | 14.04 | 12.32 | 56.16 | 6.98 | 2.01 | 8.08 | 23.43 |
| 361 | 11 | 66.41 | Officer/President — hold ret_high_10d_open | Officer/President | high | 10 | open | 4 | 100.0 | 14.04 | 12.32 | 56.16 | 6.98 | 2.01 | 8.08 | 23.43 |
| 362 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_high_10d_open | Large cap (≥250M) CEO/CFO | high | 10 | open | 4 | 100.0 | 14.04 | 12.32 | 56.16 | 6.98 | 2.01 | 8.08 | 23.43 |
| 363 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_high_10d_open | Large cap (≥500M) CEO/CFO | high | 10 | open | 4 | 100.0 | 14.04 | 12.32 | 56.16 | 6.98 | 2.01 | 8.08 | 23.43 |
| 364 | 26 | 50.0 | Qty ≥50k shares — hold ret_high_3d_open | Qty ≥50k shares | high | 3 | open | 2 | 100.0 | 14.0 | 14.01 | 28.01 | 3.8 | 3.69 | 11.32 | 16.69 |
| 365 | 27 | 50.0 | Value ≥1M — hold ret_high_3d_open | Value ≥1M | high | 3 | open | 2 | 100.0 | 14.0 | 14.01 | 28.01 | 3.8 | 3.69 | 11.32 | 16.69 |
| 366 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_high_5d_open | CEO only + Value ≥100k | high | 5 | open | 2 | 100.0 | 13.99 | 13.99 | 27.98 | 11.2 | 1.25 | 6.07 | 21.91 |
| 367 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_high_5d_open | Price > MA50 + CEO/CFO | high | 5 | open | 2 | 100.0 | 13.99 | 13.99 | 27.98 | 11.2 | 1.25 | 6.07 | 21.91 |
| 368 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_mean_7d_news | CEO only + Value ≥500k | mean | 7 | news | 1 | 100.0 | 13.99 | 13.99 | 13.99 | nan | nan | 13.99 | 13.99 |
| 369 | 1 | 100.0 | CEO only + Position +10% — hold ret_mean_7d_news | CEO only + Position +10% | mean | 7 | news | 1 | 100.0 | 13.99 | 13.99 | 13.99 | nan | nan | 13.99 | 13.99 |
| 370 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_mean_7d_news | Near 52w high + CEO/CFO | mean | 7 | news | 1 | 100.0 | 13.99 | 13.99 | 13.99 | nan | nan | 13.99 | 13.99 |
| 371 | 15 | 62.43 | Price > MA50 — hold ret_high_60d_open | Price > MA50 | high | 60 | open | 5 | 100.0 | 13.99 | 13.94 | 69.96 | 6.36 | 2.2 | 7.07 | 23.43 |
| 372 | 30 | 48.32 | Value ≥100k — hold ret_high_60d_open | Value ≥100k | high | 60 | open | 6 | 100.0 | 13.93 | 12.63 | 83.56 | 6.06 | 2.3 | 7.07 | 23.43 |
| 373 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_high_30d_open | Large cap (≥2B) CEO/CFO | high | 30 | open | 2 | 100.0 | 13.9 | 13.9 | 27.8 | 6.28 | 2.21 | 9.46 | 18.34 |
| 374 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_high_60d_open | Large cap (≥2B) CEO/CFO | high | 60 | open | 2 | 100.0 | 13.9 | 13.9 | 27.8 | 6.28 | 2.21 | 9.46 | 18.34 |
| 375 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_high_30d_news | Mid cap (1B–10B) Value ≥100k | high | 30 | news | 4 | 100.0 | 13.85 | 11.54 | 55.41 | 8.37 | 1.66 | 7.13 | 25.19 |
| 376 | 35 | 40.48 | Value ≥500k — hold ret_high_14d_news | Value ≥500k | high | 14 | news | 4 | 100.0 | 13.8 | 12.69 | 55.19 | 8.5 | 1.62 | 4.63 | 25.19 |
| 377 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_high_30d_open | Mid cap (1B–10B) Value ≥100k | high | 30 | open | 4 | 100.0 | 13.78 | 12.71 | 55.14 | 8.46 | 1.63 | 6.3 | 23.43 |
| 378 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_high_30d_news | Large cap (≥2B) CEO/CFO | high | 30 | news | 2 | 100.0 | 13.75 | 13.75 | 27.5 | 1.95 | 7.05 | 12.37 | 15.13 |
| 379 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_high_60d_news | Large cap (≥2B) CEO/CFO | high | 60 | news | 2 | 100.0 | 13.75 | 13.75 | 27.5 | 1.95 | 7.05 | 12.37 | 15.13 |
| 380 | 35 | 40.48 | Value ≥500k — hold ret_high_14d_open | Value ≥500k | high | 14 | open | 4 | 100.0 | 13.74 | 13.85 | 54.95 | 8.27 | 1.66 | 3.82 | 23.43 |
| 381 | 15 | 62.43 | Price > MA50 — hold ret_high_30d_news | Price > MA50 | high | 30 | news | 5 | 100.0 | 13.74 | 12.37 | 68.71 | 7.34 | 1.87 | 7.13 | 25.19 |
| 382 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_high_7d_open | CEO/CFO + Value ≥100k | high | 7 | open | 3 | 100.0 | 13.66 | 9.46 | 40.97 | 8.49 | 1.61 | 8.08 | 23.43 |
| 383 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_high_7d_open | Large cap (≥750M) CEO/CFO | high | 7 | open | 3 | 100.0 | 13.66 | 9.46 | 40.97 | 8.49 | 1.61 | 8.08 | 23.43 |
| 384 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_high_7d_open | Large cap (≥1B) CEO/CFO | high | 7 | open | 3 | 100.0 | 13.66 | 9.46 | 40.97 | 8.49 | 1.61 | 8.08 | 23.43 |
| 385 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_high_10d_open | CEO/CFO + Value ≥100k | high | 10 | open | 3 | 100.0 | 13.66 | 9.46 | 40.97 | 8.49 | 1.61 | 8.08 | 23.43 |
| 386 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_high_10d_open | Large cap (≥750M) CEO/CFO | high | 10 | open | 3 | 100.0 | 13.66 | 9.46 | 40.97 | 8.49 | 1.61 | 8.08 | 23.43 |
| 387 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_high_10d_open | Large cap (≥1B) CEO/CFO | high | 10 | open | 3 | 100.0 | 13.66 | 9.46 | 40.97 | 8.49 | 1.61 | 8.08 | 23.43 |
| 388 | 6 | 77.62 | CEO only — hold ret_high_5d_news | CEO only | high | 5 | news | 3 | 100.0 | 13.64 | 8.89 | 40.92 | 8.67 | 1.57 | 8.38 | 23.65 |
| 389 | 26 | 50.0 | Qty ≥50k shares — hold ret_high_2d_news | Qty ≥50k shares | high | 2 | news | 2 | 100.0 | 13.58 | 13.59 | 27.17 | 2.03 | 6.69 | 12.15 | 15.02 |
| 390 | 27 | 50.0 | Value ≥1M — hold ret_high_2d_news | Value ≥1M | high | 2 | news | 2 | 100.0 | 13.58 | 13.59 | 27.17 | 2.03 | 6.69 | 12.15 | 15.02 |
| 391 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_high_3d_news | CEO only + Value ≥100k | high | 3 | news | 2 | 100.0 | 13.58 | 13.58 | 27.16 | 6.76 | 2.01 | 8.8 | 18.36 |
| 392 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_high_3d_news | Price > MA50 + CEO/CFO | high | 3 | news | 2 | 100.0 | 13.58 | 13.58 | 27.16 | 6.76 | 2.01 | 8.8 | 18.36 |
| 393 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_mean_30d_news | CEO only + Value ≥500k | mean | 30 | news | 1 | 100.0 | 13.57 | 13.57 | 13.57 | nan | nan | 13.57 | 13.57 |
| 394 | 1 | 100.0 | CEO only + Position +10% — hold ret_mean_30d_news | CEO only + Position +10% | mean | 30 | news | 1 | 100.0 | 13.57 | 13.57 | 13.57 | nan | nan | 13.57 | 13.57 |
| 395 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_mean_30d_news | Near 52w high + CEO/CFO | mean | 30 | news | 1 | 100.0 | 13.57 | 13.57 | 13.57 | nan | nan | 13.57 | 13.57 |
| 396 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_high_5d_news | Mid cap (1B–10B) CEO/CFO | high | 5 | news | 2 | 100.0 | 13.5 | 13.49 | 26.99 | 14.36 | 0.94 | 3.34 | 23.65 |
| 397 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_high_2d_open | CEO only + Value ≥500k | high | 2 | open | 1 | 100.0 | 13.41 | 13.41 | 13.41 | nan | nan | 13.41 | 13.41 |
| 398 | 1 | 100.0 | CEO only + Position +10% — hold ret_high_2d_open | CEO only + Position +10% | high | 2 | open | 1 | 100.0 | 13.41 | 13.41 | 13.41 | nan | nan | 13.41 | 13.41 |
| 399 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_high_2d_open | Near 52w high + CEO/CFO | high | 2 | open | 1 | 100.0 | 13.41 | 13.41 | 13.41 | nan | nan | 13.41 | 13.41 |
| 400 | 51 | 20.1 | Position +30% — hold ret_high_60d_open | Position +30% | high | 60 | open | 3 | 100.0 | 13.41 | 11.32 | 40.22 | 4.29 | 3.13 | 10.56 | 18.34 |
| 401 | 51 | 20.1 | Position +30% — hold ret_high_90d_open | Position +30% | high | 90 | open | 3 | 100.0 | 13.41 | 11.32 | 40.22 | 4.29 | 3.13 | 10.56 | 18.34 |
| 402 | 21 | 53.67 | Qty ≥5k shares — hold ret_high_14d_open | Qty ≥5k shares | high | 14 | open | 6 | 100.0 | 13.38 | 13.85 | 80.29 | 7.34 | 1.82 | 3.82 | 23.43 |
| 403 | 21 | 53.67 | Qty ≥5k shares — hold ret_high_14d_news | Qty ≥5k shares | high | 14 | news | 6 | 100.0 | 13.38 | 12.69 | 80.29 | 7.23 | 1.85 | 4.63 | 25.19 |
| 404 | 20 | 53.67 | Qty ≥10k shares — hold ret_high_14d_open | Qty ≥10k shares | high | 14 | open | 6 | 100.0 | 13.38 | 13.85 | 80.29 | 7.34 | 1.82 | 3.82 | 23.43 |
| 405 | 20 | 53.67 | Qty ≥10k shares — hold ret_high_14d_news | Qty ≥10k shares | high | 14 | news | 6 | 100.0 | 13.38 | 12.69 | 80.29 | 7.23 | 1.85 | 4.63 | 25.19 |
| 406 | 30 | 48.32 | Value ≥100k — hold ret_high_30d_news | Value ≥100k | high | 30 | news | 6 | 100.0 | 13.32 | 12.26 | 79.93 | 6.53 | 2.04 | 7.13 | 25.19 |
| 407 | 49 | 32.78 | CFO only — hold ret_high_14d_news | CFO only | high | 14 | news | 1 | 100.0 | 13.22 | 13.22 | 13.22 | nan | nan | 13.22 | 13.22 |
| 408 | 48 | 32.78 | CFO + Director (combo) — hold ret_high_14d_news | CFO + Director (combo) | high | 14 | news | 1 | 100.0 | 13.22 | 13.22 | 13.22 | nan | nan | 13.22 | 13.22 |
| 409 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_high_14d_news | CFO only + Value ≥50k | high | 14 | news | 1 | 100.0 | 13.22 | 13.22 | 13.22 | nan | nan | 13.22 | 13.22 |
| 410 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_high_14d_news | CFO only + Value ≥100k | high | 14 | news | 1 | 100.0 | 13.22 | 13.22 | 13.22 | nan | nan | 13.22 | 13.22 |
| 411 | 47 | 32.78 | CFO only + Position +10% — hold ret_high_14d_news | CFO only + Position +10% | high | 14 | news | 1 | 100.0 | 13.22 | 13.22 | 13.22 | nan | nan | 13.22 | 13.22 |
| 412 | 46 | 32.78 | CFO only + Position +20% — hold ret_high_14d_news | CFO only + Position +20% | high | 14 | news | 1 | 100.0 | 13.22 | 13.22 | 13.22 | nan | nan | 13.22 | 13.22 |
| 413 | 44 | 32.78 | RSI oversold (<30) — hold ret_high_14d_news | RSI oversold (<30) | high | 14 | news | 1 | 100.0 | 13.22 | 13.22 | 13.22 | nan | nan | 13.22 | 13.22 |
| 414 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_high_14d_news | RSI oversold + CEO/CFO | high | 14 | news | 1 | 100.0 | 13.22 | 13.22 | 13.22 | nan | nan | 13.22 | 13.22 |
| 415 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_high_14d_news | RSI oversold + Value ≥100k | high | 14 | news | 1 | 100.0 | 13.22 | 13.22 | 13.22 | nan | nan | 13.22 | 13.22 |
| 416 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_high_30d_news | Far 52w high + Value ≥100k | high | 30 | news | 3 | 100.0 | 13.22 | 12.37 | 39.65 | 1.66 | 7.96 | 12.15 | 15.13 |
| 417 | 14 | 65.45 | Price > MA200 — hold ret_high_30d_open | Price > MA200 | high | 30 | open | 4 | 100.0 | 13.22 | 11.56 | 52.86 | 8.12 | 1.63 | 6.3 | 23.43 |
| 418 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_high_60d_news | Far 52w high + Value ≥100k | high | 60 | news | 3 | 100.0 | 13.22 | 12.37 | 39.65 | 1.66 | 7.96 | 12.15 | 15.13 |
| 419 | 10 | 66.41 | CEO/CFO — hold ret_high_7d_news | CEO/CFO | high | 7 | news | 4 | 100.0 | 13.15 | 11.13 | 52.61 | 8.57 | 1.54 | 5.15 | 25.19 |
| 420 | 11 | 66.41 | Officer/President — hold ret_high_7d_news | Officer/President | high | 7 | news | 4 | 100.0 | 13.15 | 11.13 | 52.61 | 8.57 | 1.54 | 5.15 | 25.19 |
| 421 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_high_7d_news | Large cap (≥250M) CEO/CFO | high | 7 | news | 4 | 100.0 | 13.15 | 11.13 | 52.61 | 8.57 | 1.54 | 5.15 | 25.19 |
| 422 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_high_7d_news | Large cap (≥500M) CEO/CFO | high | 7 | news | 4 | 100.0 | 13.15 | 11.13 | 52.61 | 8.57 | 1.54 | 5.15 | 25.19 |
| 423 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_mean_10d_open | CEO only + Value ≥500k | mean | 10 | open | 1 | 100.0 | 13.07 | 13.07 | 13.07 | nan | nan | 13.07 | 13.07 |
| 424 | 1 | 100.0 | CEO only + Position +10% — hold ret_mean_10d_open | CEO only + Position +10% | mean | 10 | open | 1 | 100.0 | 13.07 | 13.07 | 13.07 | nan | nan | 13.07 | 13.07 |
| 425 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_mean_10d_open | Near 52w high + CEO/CFO | mean | 10 | open | 1 | 100.0 | 13.07 | 13.07 | 13.07 | nan | nan | 13.07 | 13.07 |
| 426 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_high_14d_open | Multiple buys (n≥2) | high | 14 | open | 3 | 100.0 | 13.06 | 16.38 | 39.19 | 7.44 | 1.76 | 4.54 | 18.27 |
| 427 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_high_30d_open | Far 52w high + Value ≥100k | high | 30 | open | 3 | 100.0 | 13.04 | 11.32 | 39.12 | 4.68 | 2.78 | 9.46 | 18.34 |
| 428 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_high_60d_open | Far 52w high + Value ≥100k | high | 60 | open | 3 | 100.0 | 13.04 | 11.32 | 39.12 | 4.68 | 2.78 | 9.46 | 18.34 |
| 429 | 10 | 66.41 | CEO/CFO — hold ret_high_7d_open | CEO/CFO | high | 7 | open | 4 | 100.0 | 12.98 | 10.21 | 51.93 | 7.06 | 1.84 | 8.08 | 23.43 |
| 430 | 11 | 66.41 | Officer/President — hold ret_high_7d_open | Officer/President | high | 7 | open | 4 | 100.0 | 12.98 | 10.21 | 51.93 | 7.06 | 1.84 | 8.08 | 23.43 |
| 431 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_high_7d_open | Large cap (≥250M) CEO/CFO | high | 7 | open | 4 | 100.0 | 12.98 | 10.21 | 51.93 | 7.06 | 1.84 | 8.08 | 23.43 |
| 432 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_high_7d_open | Large cap (≥500M) CEO/CFO | high | 7 | open | 4 | 100.0 | 12.98 | 10.21 | 51.93 | 7.06 | 1.84 | 8.08 | 23.43 |
| 433 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_high_14d_open | Large cap (≥2B) CEO/CFO | high | 14 | open | 2 | 100.0 | 12.92 | 12.92 | 25.84 | 4.89 | 2.64 | 9.46 | 16.38 |
| 434 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_mean_14d_open | CEO only + Value ≥500k | mean | 14 | open | 1 | 100.0 | 12.89 | 12.89 | 12.89 | nan | nan | 12.89 | 12.89 |
| 435 | 1 | 100.0 | CEO only + Position +10% — hold ret_mean_14d_open | CEO only + Position +10% | mean | 14 | open | 1 | 100.0 | 12.89 | 12.89 | 12.89 | nan | nan | 12.89 | 12.89 |
| 436 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_mean_14d_open | Near 52w high + CEO/CFO | mean | 14 | open | 1 | 100.0 | 12.89 | 12.89 | 12.89 | nan | nan | 12.89 | 12.89 |
| 437 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_high_30d_news | Multiple buys (n≥2) | high | 30 | news | 3 | 100.0 | 12.81 | 15.13 | 38.43 | 7.39 | 1.73 | 4.54 | 18.76 |
| 438 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_high_14d_news | Large cap (≥2B) CEO/CFO | high | 14 | news | 2 | 100.0 | 12.8 | 12.79 | 25.59 | 0.6 | 21.29 | 12.37 | 13.22 |
| 439 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_high_14d_news | Mid cap (1B–10B) Value ≥100k | high | 14 | news | 4 | 100.0 | 12.75 | 10.59 | 51.0 | 9.02 | 1.41 | 4.63 | 25.19 |
| 440 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_high_14d_open | Mid cap (1B–10B) Value ≥100k | high | 14 | open | 4 | 100.0 | 12.68 | 11.72 | 50.7 | 8.93 | 1.42 | 3.82 | 23.43 |
| 441 | 30 | 48.32 | Value ≥100k — hold ret_high_30d_open | Value ≥100k | high | 30 | open | 6 | 100.0 | 12.65 | 10.39 | 75.92 | 6.81 | 1.86 | 6.3 | 23.43 |
| 442 | 30 | 48.32 | Value ≥100k — hold ret_high_14d_news | Value ≥100k | high | 14 | news | 6 | 100.0 | 12.59 | 12.26 | 75.52 | 6.99 | 1.8 | 4.63 | 25.19 |
| 443 | 22 | 53.36 | RSI overbought (>70) — hold ret_high_90d_news | RSI overbought (>70) | high | 90 | news | 2 | 100.0 | 12.59 | 12.59 | 25.18 | 6.55 | 1.92 | 7.96 | 17.22 |
| 444 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_high_14d_news | Far 52w high + Value ≥100k | high | 14 | news | 3 | 100.0 | 12.58 | 12.37 | 37.74 | 0.57 | 22.26 | 12.15 | 13.22 |
| 445 | 32 | 44.63 | Position +10% — hold ret_high_60d_news | Position +10% | high | 60 | news | 6 | 100.0 | 12.55 | 11.23 | 75.28 | 7.17 | 1.75 | 4.54 | 25.19 |
| 446 | 32 | 44.63 | Position +10% — hold ret_high_90d_news | Position +10% | high | 90 | news | 6 | 100.0 | 12.55 | 11.23 | 75.28 | 7.17 | 1.75 | 4.54 | 25.19 |
| 447 | 32 | 44.63 | Position +10% — hold ret_high_60d_open | Position +10% | high | 60 | open | 6 | 100.0 | 12.54 | 10.94 | 75.26 | 7.09 | 1.77 | 4.54 | 23.43 |
| 448 | 32 | 44.63 | Position +10% — hold ret_high_90d_open | Position +10% | high | 90 | open | 6 | 100.0 | 12.54 | 10.94 | 75.26 | 7.09 | 1.77 | 4.54 | 23.43 |
| 449 | 51 | 20.1 | Position +30% — hold ret_high_60d_news | Position +30% | high | 60 | news | 3 | 100.0 | 12.53 | 12.15 | 37.59 | 2.43 | 5.15 | 10.31 | 15.13 |
| 450 | 51 | 20.1 | Position +30% — hold ret_high_90d_news | Position +30% | high | 90 | news | 3 | 100.0 | 12.53 | 12.15 | 37.59 | 2.43 | 5.15 | 10.31 | 15.13 |
| 451 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_mean_5d_news | CEO only + Value ≥500k | mean | 5 | news | 1 | 100.0 | 12.51 | 12.51 | 12.51 | nan | nan | 12.51 | 12.51 |
| 452 | 1 | 100.0 | CEO only + Position +10% — hold ret_mean_5d_news | CEO only + Position +10% | mean | 5 | news | 1 | 100.0 | 12.51 | 12.51 | 12.51 | nan | nan | 12.51 | 12.51 |
| 453 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_mean_5d_news | Near 52w high + CEO/CFO | mean | 5 | news | 1 | 100.0 | 12.51 | 12.51 | 12.51 | nan | nan | 12.51 | 12.51 |
| 454 | 6 | 77.62 | CEO only — hold ret_high_5d_open | CEO only | high | 5 | open | 3 | 100.0 | 12.47 | 9.42 | 37.4 | 8.35 | 1.49 | 6.07 | 21.91 |
| 455 | 15 | 62.43 | Price > MA50 — hold ret_high_30d_open | Price > MA50 | high | 30 | open | 5 | 100.0 | 12.46 | 9.46 | 62.32 | 7.23 | 1.72 | 6.3 | 23.43 |
| 456 | 37 | 35.58 | Director only + Value ≥100k — hold ret_high_90d_news | Director only + Value ≥100k | high | 90 | news | 3 | 100.0 | 12.44 | 12.15 | 37.33 | 4.64 | 2.68 | 7.96 | 17.22 |
| 457 | 14 | 65.45 | Price > MA200 — hold ret_high_14d_news | Price > MA200 | high | 14 | news | 4 | 100.0 | 12.43 | 9.95 | 49.72 | 9.02 | 1.38 | 4.63 | 25.19 |
| 458 | 15 | 62.43 | Price > MA50 — hold ret_high_14d_news | Price > MA50 | high | 14 | news | 5 | 100.0 | 12.42 | 11.94 | 62.09 | 7.81 | 1.59 | 4.63 | 25.19 |
| 459 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_mean_7d_open | CEO only + Value ≥500k | mean | 7 | open | 1 | 100.0 | 12.39 | 12.39 | 12.39 | nan | nan | 12.39 | 12.39 |
| 460 | 1 | 100.0 | CEO only + Position +10% — hold ret_mean_7d_open | CEO only + Position +10% | mean | 7 | open | 1 | 100.0 | 12.39 | 12.39 | 12.39 | nan | nan | 12.39 | 12.39 |
| 461 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_mean_7d_open | Near 52w high + CEO/CFO | mean | 7 | open | 1 | 100.0 | 12.39 | 12.39 | 12.39 | nan | nan | 12.39 | 12.39 |
| 462 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_high_14d_open | Far 52w high + Value ≥100k | high | 14 | open | 3 | 100.0 | 12.39 | 11.32 | 37.16 | 3.58 | 3.46 | 9.46 | 16.38 |
| 463 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_high_7d_news | Large cap (≥3B) CEO/CFO | high | 7 | news | 1 | 100.0 | 12.37 | 12.37 | 12.37 | nan | nan | 12.37 | 12.37 |
| 464 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_high_7d_news | Large cap (≥5B) CEO/CFO | high | 7 | news | 1 | 100.0 | 12.37 | 12.37 | 12.37 | nan | nan | 12.37 | 12.37 |
| 465 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_high_7d_news | Large cap (≥10B) CEO/CFO | high | 7 | news | 1 | 100.0 | 12.37 | 12.37 | 12.37 | nan | nan | 12.37 | 12.37 |
| 466 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_high_10d_news | Large cap (≥3B) CEO/CFO | high | 10 | news | 1 | 100.0 | 12.37 | 12.37 | 12.37 | nan | nan | 12.37 | 12.37 |
| 467 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_high_10d_news | Large cap (≥5B) CEO/CFO | high | 10 | news | 1 | 100.0 | 12.37 | 12.37 | 12.37 | nan | nan | 12.37 | 12.37 |
| 468 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_high_10d_news | Large cap (≥10B) CEO/CFO | high | 10 | news | 1 | 100.0 | 12.37 | 12.37 | 12.37 | nan | nan | 12.37 | 12.37 |
| 469 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_high_14d_news | Large cap (≥3B) CEO/CFO | high | 14 | news | 1 | 100.0 | 12.37 | 12.37 | 12.37 | nan | nan | 12.37 | 12.37 |
| 470 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_high_14d_news | Large cap (≥5B) CEO/CFO | high | 14 | news | 1 | 100.0 | 12.37 | 12.37 | 12.37 | nan | nan | 12.37 | 12.37 |
| 471 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_high_14d_news | Large cap (≥10B) CEO/CFO | high | 14 | news | 1 | 100.0 | 12.37 | 12.37 | 12.37 | nan | nan | 12.37 | 12.37 |
| 472 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_high_30d_news | Large cap (≥3B) CEO/CFO | high | 30 | news | 1 | 100.0 | 12.37 | 12.37 | 12.37 | nan | nan | 12.37 | 12.37 |
| 473 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_high_30d_news | Large cap (≥5B) CEO/CFO | high | 30 | news | 1 | 100.0 | 12.37 | 12.37 | 12.37 | nan | nan | 12.37 | 12.37 |
| 474 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_high_30d_news | Large cap (≥10B) CEO/CFO | high | 30 | news | 1 | 100.0 | 12.37 | 12.37 | 12.37 | nan | nan | 12.37 | 12.37 |
| 475 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_high_60d_news | Large cap (≥3B) CEO/CFO | high | 60 | news | 1 | 100.0 | 12.37 | 12.37 | 12.37 | nan | nan | 12.37 | 12.37 |
| 476 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_high_60d_news | Large cap (≥5B) CEO/CFO | high | 60 | news | 1 | 100.0 | 12.37 | 12.37 | 12.37 | nan | nan | 12.37 | 12.37 |
| 477 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_high_60d_news | Large cap (≥10B) CEO/CFO | high | 60 | news | 1 | 100.0 | 12.37 | 12.37 | 12.37 | nan | nan | 12.37 | 12.37 |
| 478 | 26 | 50.0 | Qty ≥50k shares — hold ret_high_2d_open | Qty ≥50k shares | high | 2 | open | 2 | 100.0 | 12.36 | 12.37 | 24.73 | 1.48 | 8.37 | 11.32 | 13.41 |
| 479 | 27 | 50.0 | Value ≥1M — hold ret_high_2d_open | Value ≥1M | high | 2 | open | 2 | 100.0 | 12.36 | 12.37 | 24.73 | 1.48 | 8.37 | 11.32 | 13.41 |
| 480 | 28 | 48.48 | Tutti — hold ret_high_30d_news | Tutti | high | 30 | news | 10 | 100.0 | 12.26 | 12.26 | 122.61 | 6.8 | 1.8 | 3.32 | 25.19 |
| 481 | 53 | 0.0 | Qty ≥100k shares — hold ret_high_1d_news | Qty ≥100k shares | high | 1 | news | 1 | 100.0 | 12.15 | 12.15 | 12.15 | nan | nan | 12.15 | 12.15 |
| 482 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_high_1d_news | Small cap (≤1B) Value ≥100k | high | 1 | news | 1 | 100.0 | 12.15 | 12.15 | 12.15 | nan | nan | 12.15 | 12.15 |
| 483 | 53 | 0.0 | Qty ≥100k shares — hold ret_high_2d_news | Qty ≥100k shares | high | 2 | news | 1 | 100.0 | 12.15 | 12.15 | 12.15 | nan | nan | 12.15 | 12.15 |
| 484 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_high_2d_news | Small cap (≤1B) Value ≥100k | high | 2 | news | 1 | 100.0 | 12.15 | 12.15 | 12.15 | nan | nan | 12.15 | 12.15 |
| 485 | 53 | 0.0 | Qty ≥100k shares — hold ret_high_3d_news | Qty ≥100k shares | high | 3 | news | 1 | 100.0 | 12.15 | 12.15 | 12.15 | nan | nan | 12.15 | 12.15 |
| 486 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_high_3d_news | Small cap (≤1B) Value ≥100k | high | 3 | news | 1 | 100.0 | 12.15 | 12.15 | 12.15 | nan | nan | 12.15 | 12.15 |
| 487 | 53 | 0.0 | Qty ≥100k shares — hold ret_high_5d_news | Qty ≥100k shares | high | 5 | news | 1 | 100.0 | 12.15 | 12.15 | 12.15 | nan | nan | 12.15 | 12.15 |
| 488 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_high_5d_news | Small cap (≤1B) Value ≥100k | high | 5 | news | 1 | 100.0 | 12.15 | 12.15 | 12.15 | nan | nan | 12.15 | 12.15 |
| 489 | 53 | 0.0 | Qty ≥100k shares — hold ret_high_7d_news | Qty ≥100k shares | high | 7 | news | 1 | 100.0 | 12.15 | 12.15 | 12.15 | nan | nan | 12.15 | 12.15 |
| 490 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_high_7d_news | Small cap (≤1B) Value ≥100k | high | 7 | news | 1 | 100.0 | 12.15 | 12.15 | 12.15 | nan | nan | 12.15 | 12.15 |
| 491 | 53 | 0.0 | Qty ≥100k shares — hold ret_high_10d_news | Qty ≥100k shares | high | 10 | news | 1 | 100.0 | 12.15 | 12.15 | 12.15 | nan | nan | 12.15 | 12.15 |
| 492 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_high_10d_news | Small cap (≤1B) Value ≥100k | high | 10 | news | 1 | 100.0 | 12.15 | 12.15 | 12.15 | nan | nan | 12.15 | 12.15 |
| 493 | 53 | 0.0 | Qty ≥100k shares — hold ret_high_14d_news | Qty ≥100k shares | high | 14 | news | 1 | 100.0 | 12.15 | 12.15 | 12.15 | nan | nan | 12.15 | 12.15 |
| 494 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_high_14d_news | Small cap (≤1B) Value ≥100k | high | 14 | news | 1 | 100.0 | 12.15 | 12.15 | 12.15 | nan | nan | 12.15 | 12.15 |
| 495 | 53 | 0.0 | Qty ≥100k shares — hold ret_high_30d_news | Qty ≥100k shares | high | 30 | news | 1 | 100.0 | 12.15 | 12.15 | 12.15 | nan | nan | 12.15 | 12.15 |
| 496 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_high_30d_news | Small cap (≤1B) Value ≥100k | high | 30 | news | 1 | 100.0 | 12.15 | 12.15 | 12.15 | nan | nan | 12.15 | 12.15 |
| 497 | 53 | 0.0 | Qty ≥100k shares — hold ret_high_60d_news | Qty ≥100k shares | high | 60 | news | 1 | 100.0 | 12.15 | 12.15 | 12.15 | nan | nan | 12.15 | 12.15 |
| 498 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_high_60d_news | Small cap (≤1B) Value ≥100k | high | 60 | news | 1 | 100.0 | 12.15 | 12.15 | 12.15 | nan | nan | 12.15 | 12.15 |
| 499 | 53 | 0.0 | Qty ≥100k shares — hold ret_high_90d_news | Qty ≥100k shares | high | 90 | news | 1 | 100.0 | 12.15 | 12.15 | 12.15 | nan | nan | 12.15 | 12.15 |
| 500 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_high_90d_news | Small cap (≤1B) Value ≥100k | high | 90 | news | 1 | 100.0 | 12.15 | 12.15 | 12.15 | nan | nan | 12.15 | 12.15 |
| 501 | 28 | 48.48 | Tutti — hold ret_high_30d_open | Tutti | high | 30 | open | 10 | 100.0 | 12.0 | 10.39 | 119.97 | 7.0 | 1.71 | 3.55 | 23.43 |
| 502 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_mean_30d_open | CEO only + Value ≥500k | mean | 30 | open | 1 | 100.0 | 11.97 | 11.97 | 11.97 | nan | nan | 11.97 | 11.97 |
| 503 | 1 | 100.0 | CEO only + Position +10% — hold ret_mean_30d_open | CEO only + Position +10% | mean | 30 | open | 1 | 100.0 | 11.97 | 11.97 | 11.97 | nan | nan | 11.97 | 11.97 |
| 504 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_mean_30d_open | Near 52w high + CEO/CFO | mean | 30 | open | 1 | 100.0 | 11.97 | 11.97 | 11.97 | nan | nan | 11.97 | 11.97 |
| 505 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_high_5d_news | CEO/CFO + Value ≥100k | high | 5 | news | 3 | 100.0 | 11.96 | 8.89 | 35.88 | 10.5 | 1.14 | 3.34 | 23.65 |
| 506 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_high_5d_news | Large cap (≥750M) CEO/CFO | high | 5 | news | 3 | 100.0 | 11.96 | 8.89 | 35.88 | 10.5 | 1.14 | 3.34 | 23.65 |
| 507 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_high_5d_news | Large cap (≥1B) CEO/CFO | high | 5 | news | 3 | 100.0 | 11.96 | 8.89 | 35.88 | 10.5 | 1.14 | 3.34 | 23.65 |
| 508 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_high_2d_news | CEO only + Value ≥100k | high | 2 | news | 2 | 100.0 | 11.91 | 11.91 | 23.82 | 4.4 | 2.71 | 8.8 | 15.02 |
| 509 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_high_2d_news | Price > MA50 + CEO/CFO | high | 2 | news | 2 | 100.0 | 11.91 | 11.91 | 23.82 | 4.4 | 2.71 | 8.8 | 15.02 |
| 510 | 30 | 48.32 | Value ≥100k — hold ret_high_14d_open | Value ≥100k | high | 14 | open | 6 | 100.0 | 11.91 | 10.39 | 71.48 | 7.04 | 1.69 | 3.82 | 23.43 |
| 511 | 6 | 77.62 | CEO only — hold ret_high_3d_news | CEO only | high | 3 | news | 3 | 100.0 | 11.85 | 8.8 | 35.54 | 5.64 | 2.1 | 8.38 | 18.36 |
| 512 | 31 | 47.75 | Value ≥50k — hold ret_high_30d_news | Value ≥50k | high | 30 | news | 9 | 100.0 | 11.84 | 12.15 | 106.55 | 7.07 | 1.67 | 3.32 | 25.19 |
| 513 | 39 | 34.48 | Position +20% — hold ret_high_60d_open | Position +20% | high | 60 | open | 4 | 100.0 | 11.82 | 10.94 | 47.29 | 4.72 | 2.5 | 7.07 | 18.34 |
| 514 | 39 | 34.48 | Position +20% — hold ret_high_90d_open | Position +20% | high | 90 | open | 4 | 100.0 | 11.82 | 10.94 | 47.29 | 4.72 | 2.5 | 7.07 | 18.34 |
| 515 | 22 | 53.36 | RSI overbought (>70) — hold ret_high_90d_open | RSI overbought (>70) | high | 90 | open | 2 | 100.0 | 11.69 | 11.69 | 23.38 | 6.53 | 1.79 | 7.07 | 16.31 |
| 516 | 37 | 35.58 | Director only + Value ≥100k — hold ret_high_60d_news | Director only + Value ≥100k | high | 60 | news | 3 | 100.0 | 11.65 | 12.15 | 34.94 | 3.46 | 3.36 | 7.96 | 14.83 |
| 517 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_high_14d_news | Multiple buys (n≥2) | high | 14 | news | 3 | 100.0 | 11.63 | 13.22 | 34.9 | 6.45 | 1.8 | 4.54 | 17.14 |
| 518 | 37 | 35.58 | Director only + Value ≥100k — hold ret_high_90d_open | Director only + Value ≥100k | high | 90 | open | 3 | 100.0 | 11.57 | 11.32 | 34.7 | 4.62 | 2.5 | 7.07 | 16.31 |
| 519 | 14 | 65.45 | Price > MA200 — hold ret_high_14d_open | Price > MA200 | high | 14 | open | 4 | 100.0 | 11.56 | 9.5 | 46.26 | 8.59 | 1.35 | 3.82 | 23.43 |
| 520 | 31 | 47.75 | Value ≥50k — hold ret_high_30d_open | Value ≥50k | high | 30 | open | 9 | 100.0 | 11.55 | 9.46 | 103.91 | 7.26 | 1.59 | 3.55 | 23.43 |
| 521 | 38 | 34.53 | Price < MA50 — hold ret_high_30d_open | Price < MA50 | high | 30 | open | 5 | 100.0 | 11.53 | 11.32 | 57.65 | 7.57 | 1.52 | 3.55 | 19.9 |
| 522 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_high_5d_open | CEO/CFO + Value ≥100k | high | 5 | open | 3 | 100.0 | 11.4 | 6.22 | 34.2 | 9.1 | 1.25 | 6.07 | 21.91 |
| 523 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_high_5d_open | Large cap (≥750M) CEO/CFO | high | 5 | open | 3 | 100.0 | 11.4 | 6.22 | 34.2 | 9.1 | 1.25 | 6.07 | 21.91 |
| 524 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_high_5d_open | Large cap (≥1B) CEO/CFO | high | 5 | open | 3 | 100.0 | 11.4 | 6.22 | 34.2 | 9.1 | 1.25 | 6.07 | 21.91 |
| 525 | 22 | 53.36 | RSI overbought (>70) — hold ret_high_60d_news | RSI overbought (>70) | high | 60 | news | 2 | 100.0 | 11.4 | 11.39 | 22.79 | 4.86 | 2.35 | 7.96 | 14.83 |
| 526 | 39 | 34.48 | Position +20% — hold ret_high_60d_news | Position +20% | high | 60 | news | 4 | 100.0 | 11.39 | 11.23 | 45.55 | 3.03 | 3.76 | 7.96 | 15.13 |
| 527 | 39 | 34.48 | Position +20% — hold ret_high_90d_news | Position +20% | high | 90 | news | 4 | 100.0 | 11.39 | 11.23 | 45.55 | 3.03 | 3.76 | 7.96 | 15.13 |
| 528 | 32 | 44.63 | Position +10% — hold ret_high_30d_open | Position +10% | high | 30 | open | 6 | 100.0 | 11.38 | 9.2 | 68.25 | 8.0 | 1.42 | 3.55 | 23.43 |
| 529 | 32 | 44.63 | Position +10% — hold ret_high_30d_news | Position +10% | high | 30 | news | 6 | 100.0 | 11.38 | 10.05 | 68.29 | 8.11 | 1.4 | 3.32 | 25.19 |
| 530 | 36 | 36.54 | Director only (no C-level) — hold ret_high_90d_news | Director only (no C-level) | high | 90 | news | 6 | 100.0 | 11.37 | 11.23 | 68.24 | 4.82 | 2.36 | 4.54 | 17.22 |
| 531 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_high_3d_open | CEO only + Value ≥100k | high | 3 | open | 2 | 100.0 | 11.34 | 11.34 | 22.67 | 7.57 | 1.5 | 5.98 | 16.69 |
| 532 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_high_3d_open | Price > MA50 + CEO/CFO | high | 3 | open | 2 | 100.0 | 11.34 | 11.34 | 22.67 | 7.57 | 1.5 | 5.98 | 16.69 |
| 533 | 35 | 40.48 | Value ≥500k — hold ret_high_10d_news | Value ≥500k | high | 10 | news | 4 | 100.0 | 11.33 | 8.65 | 45.32 | 10.05 | 1.13 | 2.83 | 25.19 |
| 534 | 53 | 0.0 | Qty ≥100k shares — hold ret_high_1d_open | Qty ≥100k shares | high | 1 | open | 1 | 100.0 | 11.32 | 11.32 | 11.32 | nan | nan | 11.32 | 11.32 |
| 535 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_high_1d_open | Small cap (≤1B) Value ≥100k | high | 1 | open | 1 | 100.0 | 11.32 | 11.32 | 11.32 | nan | nan | 11.32 | 11.32 |
| 536 | 53 | 0.0 | Qty ≥100k shares — hold ret_high_2d_open | Qty ≥100k shares | high | 2 | open | 1 | 100.0 | 11.32 | 11.32 | 11.32 | nan | nan | 11.32 | 11.32 |
| 537 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_high_2d_open | Small cap (≤1B) Value ≥100k | high | 2 | open | 1 | 100.0 | 11.32 | 11.32 | 11.32 | nan | nan | 11.32 | 11.32 |
| 538 | 53 | 0.0 | Qty ≥100k shares — hold ret_high_3d_open | Qty ≥100k shares | high | 3 | open | 1 | 100.0 | 11.32 | 11.32 | 11.32 | nan | nan | 11.32 | 11.32 |
| 539 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_high_3d_open | Small cap (≤1B) Value ≥100k | high | 3 | open | 1 | 100.0 | 11.32 | 11.32 | 11.32 | nan | nan | 11.32 | 11.32 |
| 540 | 53 | 0.0 | Qty ≥100k shares — hold ret_high_5d_open | Qty ≥100k shares | high | 5 | open | 1 | 100.0 | 11.32 | 11.32 | 11.32 | nan | nan | 11.32 | 11.32 |
| 541 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_high_5d_open | Small cap (≤1B) Value ≥100k | high | 5 | open | 1 | 100.0 | 11.32 | 11.32 | 11.32 | nan | nan | 11.32 | 11.32 |
| 542 | 53 | 0.0 | Qty ≥100k shares — hold ret_high_7d_open | Qty ≥100k shares | high | 7 | open | 1 | 100.0 | 11.32 | 11.32 | 11.32 | nan | nan | 11.32 | 11.32 |
| 543 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_high_7d_open | Small cap (≤1B) Value ≥100k | high | 7 | open | 1 | 100.0 | 11.32 | 11.32 | 11.32 | nan | nan | 11.32 | 11.32 |
| 544 | 53 | 0.0 | Qty ≥100k shares — hold ret_high_10d_open | Qty ≥100k shares | high | 10 | open | 1 | 100.0 | 11.32 | 11.32 | 11.32 | nan | nan | 11.32 | 11.32 |
| 545 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_high_10d_open | Small cap (≤1B) Value ≥100k | high | 10 | open | 1 | 100.0 | 11.32 | 11.32 | 11.32 | nan | nan | 11.32 | 11.32 |
| 546 | 53 | 0.0 | Qty ≥100k shares — hold ret_high_14d_open | Qty ≥100k shares | high | 14 | open | 1 | 100.0 | 11.32 | 11.32 | 11.32 | nan | nan | 11.32 | 11.32 |
| 547 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_high_14d_open | Small cap (≤1B) Value ≥100k | high | 14 | open | 1 | 100.0 | 11.32 | 11.32 | 11.32 | nan | nan | 11.32 | 11.32 |
| 548 | 53 | 0.0 | Qty ≥100k shares — hold ret_high_30d_open | Qty ≥100k shares | high | 30 | open | 1 | 100.0 | 11.32 | 11.32 | 11.32 | nan | nan | 11.32 | 11.32 |
| 549 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_high_30d_open | Small cap (≤1B) Value ≥100k | high | 30 | open | 1 | 100.0 | 11.32 | 11.32 | 11.32 | nan | nan | 11.32 | 11.32 |
| 550 | 53 | 0.0 | Qty ≥100k shares — hold ret_high_60d_open | Qty ≥100k shares | high | 60 | open | 1 | 100.0 | 11.32 | 11.32 | 11.32 | nan | nan | 11.32 | 11.32 |
| 551 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_high_60d_open | Small cap (≤1B) Value ≥100k | high | 60 | open | 1 | 100.0 | 11.32 | 11.32 | 11.32 | nan | nan | 11.32 | 11.32 |
| 552 | 53 | 0.0 | Qty ≥100k shares — hold ret_high_90d_open | Qty ≥100k shares | high | 90 | open | 1 | 100.0 | 11.32 | 11.32 | 11.32 | nan | nan | 11.32 | 11.32 |
| 553 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_high_90d_open | Small cap (≤1B) Value ≥100k | high | 90 | open | 1 | 100.0 | 11.32 | 11.32 | 11.32 | nan | nan | 11.32 | 11.32 |
| 554 | 28 | 48.48 | Tutti — hold ret_high_14d_news | Tutti | high | 14 | news | 10 | 100.0 | 11.25 | 12.04 | 112.46 | 6.65 | 1.69 | 3.32 | 25.19 |
| 555 | 21 | 53.67 | Qty ≥5k shares — hold ret_high_10d_news | Qty ≥5k shares | high | 10 | news | 6 | 100.0 | 11.23 | 10.05 | 67.38 | 8.03 | 1.4 | 2.83 | 25.19 |
| 556 | 20 | 53.67 | Qty ≥10k shares — hold ret_high_10d_news | Qty ≥10k shares | high | 10 | news | 6 | 100.0 | 11.23 | 10.05 | 67.38 | 8.03 | 1.4 | 2.83 | 25.19 |
| 557 | 35 | 40.48 | Value ≥500k — hold ret_high_10d_open | Value ≥500k | high | 10 | open | 4 | 100.0 | 11.22 | 9.7 | 44.86 | 9.01 | 1.25 | 2.03 | 23.43 |
| 558 | 21 | 53.67 | Qty ≥5k shares — hold ret_high_10d_open | Qty ≥5k shares | high | 10 | open | 6 | 100.0 | 11.19 | 9.7 | 67.12 | 7.43 | 1.5 | 2.03 | 23.43 |
| 559 | 20 | 53.67 | Qty ≥10k shares — hold ret_high_10d_open | Qty ≥10k shares | high | 10 | open | 6 | 100.0 | 11.19 | 9.7 | 67.12 | 7.43 | 1.5 | 2.03 | 23.43 |
| 560 | 31 | 47.75 | Value ≥50k — hold ret_high_14d_news | Value ≥50k | high | 14 | news | 9 | 100.0 | 11.17 | 12.15 | 100.52 | 7.05 | 1.58 | 3.32 | 25.19 |
| 561 | 15 | 62.43 | Price > MA50 — hold ret_high_14d_open | Price > MA50 | high | 14 | open | 5 | 100.0 | 11.14 | 9.46 | 55.72 | 7.49 | 1.49 | 3.82 | 23.43 |
| 562 | 26 | 50.0 | Qty ≥50k shares — hold ret_high_1d_news | Qty ≥50k shares | high | 1 | news | 2 | 100.0 | 11.08 | 11.09 | 22.17 | 1.51 | 7.36 | 10.02 | 12.15 |
| 563 | 27 | 50.0 | Value ≥1M — hold ret_high_1d_news | Value ≥1M | high | 1 | news | 2 | 100.0 | 11.08 | 11.09 | 22.17 | 1.51 | 7.36 | 10.02 | 12.15 |
| 564 | 51 | 20.1 | Position +30% — hold ret_high_30d_open | Position +30% | high | 30 | open | 3 | 100.0 | 11.07 | 11.32 | 33.21 | 7.4 | 1.5 | 3.55 | 18.34 |
| 565 | 10 | 66.41 | CEO/CFO — hold ret_high_5d_news | CEO/CFO | high | 5 | news | 4 | 100.0 | 11.06 | 8.64 | 44.26 | 8.76 | 1.26 | 3.34 | 23.65 |
| 566 | 11 | 66.41 | Officer/President — hold ret_high_5d_news | Officer/President | high | 5 | news | 4 | 100.0 | 11.06 | 8.64 | 44.26 | 8.76 | 1.26 | 3.34 | 23.65 |
| 567 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_high_5d_news | Large cap (≥250M) CEO/CFO | high | 5 | news | 4 | 100.0 | 11.06 | 8.64 | 44.26 | 8.76 | 1.26 | 3.34 | 23.65 |
| 568 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_high_5d_news | Large cap (≥500M) CEO/CFO | high | 5 | news | 4 | 100.0 | 11.06 | 8.64 | 44.26 | 8.76 | 1.26 | 3.34 | 23.65 |
| 569 | 32 | 44.63 | Position +10% — hold ret_high_14d_news | Position +10% | high | 14 | news | 6 | 100.0 | 11.06 | 10.05 | 66.38 | 7.97 | 1.39 | 3.32 | 25.19 |
| 570 | 32 | 44.63 | Position +10% — hold ret_high_14d_open | Position +10% | high | 14 | open | 6 | 100.0 | 11.05 | 9.2 | 66.29 | 7.7 | 1.44 | 3.55 | 23.43 |
| 571 | 28 | 48.48 | Tutti — hold ret_high_14d_open | Tutti | high | 14 | open | 10 | 100.0 | 10.98 | 10.39 | 109.78 | 6.7 | 1.64 | 3.55 | 23.43 |
| 572 | 36 | 36.54 | Director only (no C-level) — hold ret_high_60d_news | Director only (no C-level) | high | 60 | news | 6 | 100.0 | 10.98 | 11.23 | 65.85 | 4.31 | 2.54 | 4.54 | 16.06 |
| 573 | 36 | 36.54 | Director only (no C-level) — hold ret_high_90d_open | Director only (no C-level) | high | 90 | open | 6 | 100.0 | 10.98 | 10.94 | 65.86 | 4.72 | 2.33 | 4.54 | 16.31 |
| 574 | 4 | 82.51 | CEO + Director (combo) — hold ret_high_7d_open | CEO + Director (combo) | high | 7 | open | 1 | 100.0 | 10.96 | 10.96 | 10.96 | nan | nan | 10.96 | 10.96 |
| 575 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_high_7d_open | Small cap (≤1B) CEO/CFO | high | 7 | open | 1 | 100.0 | 10.96 | 10.96 | 10.96 | nan | nan | 10.96 | 10.96 |
| 576 | 35 | 40.48 | Value ≥500k — hold ret_high_7d_news | Value ≥500k | high | 7 | news | 4 | 100.0 | 10.94 | 8.65 | 43.76 | 10.51 | 1.04 | 1.27 | 25.19 |
| 577 | 30 | 48.32 | Value ≥100k — hold ret_high_10d_news | Value ≥100k | high | 10 | news | 6 | 100.0 | 10.94 | 10.05 | 65.65 | 7.93 | 1.38 | 2.83 | 25.19 |
| 578 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_mean_5d_open | CEO only + Value ≥500k | mean | 5 | open | 1 | 100.0 | 10.93 | 10.93 | 10.93 | nan | nan | 10.93 | 10.93 |
| 579 | 1 | 100.0 | CEO only + Position +10% — hold ret_mean_5d_open | CEO only + Position +10% | mean | 5 | open | 1 | 100.0 | 10.93 | 10.93 | 10.93 | nan | nan | 10.93 | 10.93 |
| 580 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_mean_5d_open | Near 52w high + CEO/CFO | mean | 5 | open | 1 | 100.0 | 10.93 | 10.93 | 10.93 | nan | nan | 10.93 | 10.93 |
| 581 | 10 | 66.41 | CEO/CFO — hold ret_high_5d_open | CEO/CFO | high | 5 | open | 4 | 100.0 | 10.9 | 7.82 | 43.62 | 7.5 | 1.45 | 6.07 | 21.91 |
| 582 | 11 | 66.41 | Officer/President — hold ret_high_5d_open | Officer/President | high | 5 | open | 4 | 100.0 | 10.9 | 7.82 | 43.62 | 7.5 | 1.45 | 6.07 | 21.91 |
| 583 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_high_5d_open | Large cap (≥250M) CEO/CFO | high | 5 | open | 4 | 100.0 | 10.9 | 7.82 | 43.62 | 7.5 | 1.45 | 6.07 | 21.91 |
| 584 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_high_5d_open | Large cap (≥500M) CEO/CFO | high | 5 | open | 4 | 100.0 | 10.9 | 7.82 | 43.62 | 7.5 | 1.45 | 6.07 | 21.91 |
| 585 | 15 | 62.43 | Price > MA50 — hold ret_high_10d_news | Price > MA50 | high | 10 | news | 5 | 100.0 | 10.9 | 7.96 | 54.52 | 8.7 | 1.25 | 2.83 | 25.19 |
| 586 | 33 | 41.81 | Director — hold ret_high_30d_open | Director | high | 30 | open | 8 | 100.0 | 10.88 | 9.2 | 87.08 | 6.47 | 1.68 | 3.55 | 19.9 |
| 587 | 31 | 47.75 | Value ≥50k — hold ret_high_14d_open | Value ≥50k | high | 14 | open | 9 | 100.0 | 10.87 | 9.46 | 97.84 | 7.1 | 1.53 | 3.55 | 23.43 |
| 588 | 35 | 40.48 | Value ≥500k — hold ret_high_7d_open | Value ≥500k | high | 7 | open | 4 | 100.0 | 10.83 | 9.7 | 43.31 | 9.55 | 1.13 | 0.48 | 23.43 |
| 589 | 38 | 34.53 | Price < MA50 — hold ret_high_14d_open | Price < MA50 | high | 14 | open | 5 | 100.0 | 10.81 | 11.32 | 54.06 | 6.69 | 1.62 | 3.55 | 18.27 |
| 590 | 38 | 34.53 | Price < MA50 — hold ret_high_30d_news | Price < MA50 | high | 30 | news | 5 | 100.0 | 10.78 | 12.15 | 53.9 | 6.69 | 1.61 | 3.32 | 18.76 |
| 591 | 37 | 35.58 | Director only + Value ≥100k — hold ret_high_60d_open | Director only + Value ≥100k | high | 60 | open | 3 | 100.0 | 10.78 | 11.32 | 32.33 | 3.47 | 3.11 | 7.07 | 13.94 |
| 592 | 6 | 77.62 | CEO only — hold ret_high_3d_open | CEO only | high | 3 | open | 3 | 100.0 | 10.7 | 9.42 | 32.09 | 5.47 | 1.96 | 5.98 | 16.69 |
| 593 | 30 | 48.32 | Value ≥100k — hold ret_high_7d_news | Value ≥100k | high | 7 | news | 6 | 100.0 | 10.68 | 10.05 | 64.09 | 8.27 | 1.29 | 1.27 | 25.19 |
| 594 | 33 | 41.81 | Director — hold ret_high_30d_news | Director | high | 30 | news | 8 | 100.0 | 10.63 | 10.05 | 85.05 | 5.71 | 1.86 | 3.32 | 18.76 |
| 595 | 15 | 62.43 | Price > MA50 — hold ret_high_7d_news | Price > MA50 | high | 7 | news | 5 | 100.0 | 10.59 | 7.96 | 52.96 | 9.08 | 1.17 | 1.27 | 25.19 |
| 596 | 36 | 36.54 | Director only (no C-level) — hold ret_high_60d_open | Director only (no C-level) | high | 60 | open | 6 | 100.0 | 10.58 | 10.94 | 63.49 | 4.26 | 2.48 | 4.54 | 16.06 |
| 597 | 14 | 65.45 | Price > MA200 — hold ret_high_10d_news | Price > MA200 | high | 10 | news | 4 | 100.0 | 10.54 | 7.06 | 42.15 | 10.0 | 1.05 | 2.83 | 25.19 |
| 598 | 22 | 53.36 | RSI overbought (>70) — hold ret_high_60d_open | RSI overbought (>70) | high | 60 | open | 2 | 100.0 | 10.5 | 10.5 | 21.01 | 4.86 | 2.16 | 7.07 | 13.94 |
| 599 | 6 | 77.62 | CEO only — hold ret_high_2d_news | CEO only | high | 2 | news | 3 | 100.0 | 10.48 | 8.8 | 31.44 | 3.98 | 2.64 | 7.62 | 15.02 |
| 600 | 51 | 20.1 | Position +30% — hold ret_high_14d_open | Position +30% | high | 14 | open | 3 | 100.0 | 10.42 | 11.32 | 31.25 | 6.46 | 1.61 | 3.55 | 16.38 |
| 601 | 4 | 82.51 | CEO + Director (combo) — hold ret_mean_30d_open | CEO + Director (combo) | mean | 30 | open | 1 | 100.0 | 10.42 | 10.42 | 10.42 | nan | nan | 10.42 | 10.42 |
| 602 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_mean_30d_open | Small cap (≤1B) CEO/CFO | mean | 30 | open | 1 | 100.0 | 10.42 | 10.42 | 10.42 | nan | nan | 10.42 | 10.42 |
| 603 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_high_10d_news | Mid cap (1B–10B) Value ≥100k | high | 10 | news | 4 | 100.0 | 10.28 | 6.55 | 41.13 | 10.16 | 1.01 | 2.83 | 25.19 |
| 604 | 21 | 53.67 | Qty ≥5k shares — hold ret_high_7d_news | Qty ≥5k shares | high | 7 | news | 6 | 100.0 | 10.27 | 8.93 | 61.62 | 8.23 | 1.25 | 1.27 | 25.19 |
| 605 | 20 | 53.67 | Qty ≥10k shares — hold ret_high_7d_news | Qty ≥10k shares | high | 7 | news | 6 | 100.0 | 10.27 | 8.93 | 61.62 | 8.23 | 1.25 | 1.27 | 25.19 |
| 606 | 30 | 48.32 | Value ≥100k — hold ret_high_10d_open | Value ≥100k | high | 10 | open | 6 | 100.0 | 10.23 | 8.77 | 61.39 | 7.18 | 1.42 | 2.03 | 23.43 |
| 607 | 21 | 53.67 | Qty ≥5k shares — hold ret_high_7d_open | Qty ≥5k shares | high | 7 | open | 6 | 100.0 | 10.22 | 9.52 | 61.34 | 7.56 | 1.35 | 0.48 | 23.43 |
| 608 | 20 | 53.67 | Qty ≥10k shares — hold ret_high_7d_open | Qty ≥10k shares | high | 7 | open | 6 | 100.0 | 10.22 | 9.52 | 61.34 | 7.56 | 1.35 | 0.48 | 23.43 |
| 609 | 51 | 20.1 | Position +30% — hold ret_high_30d_news | Position +30% | high | 30 | news | 3 | 100.0 | 10.2 | 12.15 | 30.6 | 6.14 | 1.66 | 3.32 | 15.13 |
| 610 | 14 | 65.45 | Price > MA200 — hold ret_high_7d_news | Price > MA200 | high | 7 | news | 4 | 100.0 | 10.15 | 7.06 | 40.59 | 10.42 | 0.97 | 1.27 | 25.19 |
| 611 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_high_10d_open | Mid cap (1B–10B) Value ≥100k | high | 10 | open | 4 | 100.0 | 10.15 | 7.58 | 40.61 | 9.24 | 1.1 | 2.03 | 23.43 |
| 612 | 35 | 40.48 | Value ≥500k — hold ret_high_5d_news | Value ≥500k | high | 5 | news | 4 | 100.0 | 10.1 | 7.75 | 40.41 | 10.19 | 0.99 | 1.27 | 23.65 |
| 613 | 38 | 34.53 | Price < MA50 — hold ret_high_14d_news | Price < MA50 | high | 14 | news | 5 | 100.0 | 10.07 | 12.15 | 50.37 | 5.92 | 1.7 | 3.32 | 17.14 |
| 614 | 39 | 34.48 | Position +20% — hold ret_high_30d_open | Position +20% | high | 30 | open | 4 | 100.0 | 10.07 | 9.2 | 40.28 | 6.36 | 1.58 | 3.55 | 18.34 |
| 615 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_high_3d_open | Mid cap (1B–10B) CEO/CFO | high | 3 | open | 2 | 100.0 | 10.04 | 10.04 | 20.08 | 9.4 | 1.07 | 3.39 | 16.69 |
| 616 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_high_1d_news | CEO only + Value ≥500k | high | 1 | news | 1 | 100.0 | 10.02 | 10.02 | 10.02 | nan | nan | 10.02 | 10.02 |
| 617 | 1 | 100.0 | CEO only + Position +10% — hold ret_high_1d_news | CEO only + Position +10% | high | 1 | news | 1 | 100.0 | 10.02 | 10.02 | 10.02 | nan | nan | 10.02 | 10.02 |
| 618 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_high_1d_news | Near 52w high + CEO/CFO | high | 1 | news | 1 | 100.0 | 10.02 | 10.02 | 10.02 | nan | nan | 10.02 | 10.02 |
| 619 | 35 | 40.48 | Value ≥500k — hold ret_high_5d_open | Value ≥500k | high | 5 | open | 4 | 100.0 | 9.98 | 8.77 | 39.93 | 9.1 | 1.1 | 0.48 | 21.91 |
| 620 | 30 | 48.32 | Value ≥100k — hold ret_high_7d_open | Value ≥100k | high | 7 | open | 6 | 100.0 | 9.97 | 8.77 | 59.84 | 7.55 | 1.32 | 0.48 | 23.43 |
| 621 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_mean_7d_news | CEO only + Value ≥100k | mean | 7 | news | 2 | 100.0 | 9.94 | 9.94 | 19.88 | 5.73 | 1.74 | 5.89 | 13.99 |
| 622 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_mean_7d_news | Price > MA50 + CEO/CFO | mean | 7 | news | 2 | 100.0 | 9.94 | 9.94 | 19.88 | 5.73 | 1.74 | 5.89 | 13.99 |
| 623 | 26 | 50.0 | Qty ≥50k shares — hold ret_high_1d_open | Qty ≥50k shares | high | 1 | open | 2 | 100.0 | 9.9 | 9.9 | 19.8 | 2.01 | 4.93 | 8.48 | 11.32 |
| 624 | 27 | 50.0 | Value ≥1M — hold ret_high_1d_open | Value ≥1M | high | 1 | open | 2 | 100.0 | 9.9 | 9.9 | 19.8 | 2.01 | 4.93 | 8.48 | 11.32 |
| 625 | 4 | 82.51 | CEO + Director (combo) — hold ret_high_7d_news | CEO + Director (combo) | high | 7 | news | 1 | 100.0 | 9.9 | 9.9 | 9.9 | nan | nan | 9.9 | 9.9 |
| 626 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_high_7d_news | Small cap (≤1B) CEO/CFO | high | 7 | news | 1 | 100.0 | 9.9 | 9.9 | 9.9 | nan | nan | 9.9 | 9.9 |
| 627 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_high_7d_news | Mid cap (1B–10B) Value ≥100k | high | 7 | news | 4 | 100.0 | 9.89 | 6.55 | 39.57 | 10.56 | 0.94 | 1.27 | 25.19 |
| 628 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_high_7d_news | Far 52w high + Value ≥100k | high | 7 | news | 3 | 100.0 | 9.89 | 12.15 | 29.67 | 4.11 | 2.41 | 5.15 | 12.37 |
| 629 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_high_10d_news | Far 52w high + Value ≥100k | high | 10 | news | 3 | 100.0 | 9.89 | 12.15 | 29.67 | 4.11 | 2.41 | 5.15 | 12.37 |
| 630 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_high_7d_open | Mid cap (1B–10B) Value ≥100k | high | 7 | open | 4 | 100.0 | 9.76 | 7.58 | 39.06 | 9.71 | 1.01 | 0.48 | 23.43 |
| 631 | 31 | 47.75 | Value ≥50k — hold ret_high_10d_news | Value ≥50k | high | 10 | news | 9 | 100.0 | 9.73 | 7.96 | 87.61 | 7.16 | 1.36 | 2.83 | 25.19 |
| 632 | 32 | 44.63 | Position +10% — hold ret_high_7d_news | Position +10% | high | 7 | news | 6 | 100.0 | 9.72 | 6.55 | 58.31 | 8.21 | 1.18 | 3.32 | 25.19 |
| 633 | 32 | 44.63 | Position +10% — hold ret_high_10d_news | Position +10% | high | 10 | news | 6 | 100.0 | 9.72 | 6.55 | 58.31 | 8.21 | 1.18 | 3.32 | 25.19 |
| 634 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_high_2d_open | CEO only + Value ≥100k | high | 2 | open | 2 | 100.0 | 9.7 | 9.7 | 19.39 | 5.25 | 1.85 | 5.98 | 13.41 |
| 635 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_high_2d_open | Price > MA50 + CEO/CFO | high | 2 | open | 2 | 100.0 | 9.7 | 9.7 | 19.39 | 5.25 | 1.85 | 5.98 | 13.41 |
| 636 | 14 | 65.45 | Price > MA200 — hold ret_high_10d_open | Price > MA200 | high | 10 | open | 4 | 100.0 | 9.68 | 6.62 | 38.7 | 9.43 | 1.03 | 2.03 | 23.43 |
| 637 | 32 | 44.63 | Position +10% — hold ret_high_7d_open | Position +10% | high | 7 | open | 6 | 100.0 | 9.66 | 7.58 | 57.99 | 7.28 | 1.33 | 3.55 | 23.43 |
| 638 | 32 | 44.63 | Position +10% — hold ret_high_10d_open | Position +10% | high | 10 | open | 6 | 100.0 | 9.66 | 7.58 | 57.99 | 7.28 | 1.33 | 3.55 | 23.43 |
| 639 | 39 | 34.48 | Position +20% — hold ret_high_30d_news | Position +20% | high | 30 | news | 4 | 100.0 | 9.64 | 10.05 | 38.56 | 5.14 | 1.88 | 3.32 | 15.13 |
| 640 | 15 | 62.43 | Price > MA50 — hold ret_high_10d_open | Price > MA50 | high | 10 | open | 5 | 100.0 | 9.63 | 7.07 | 48.16 | 8.17 | 1.18 | 2.03 | 23.43 |
| 641 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_high_7d_open | Far 52w high + Value ≥100k | high | 7 | open | 3 | 100.0 | 9.62 | 9.46 | 28.86 | 1.63 | 5.92 | 8.08 | 11.32 |
| 642 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_high_10d_open | Far 52w high + Value ≥100k | high | 10 | open | 3 | 100.0 | 9.62 | 9.46 | 28.86 | 1.63 | 5.92 | 8.08 | 11.32 |
| 643 | 14 | 65.45 | Price > MA200 — hold ret_high_5d_news | Price > MA200 | high | 5 | news | 4 | 100.0 | 9.61 | 6.75 | 38.43 | 9.72 | 0.99 | 1.27 | 23.65 |
| 644 | 33 | 41.81 | Director — hold ret_high_14d_open | Director | high | 14 | open | 8 | 100.0 | 9.61 | 9.2 | 76.89 | 5.75 | 1.67 | 3.55 | 18.27 |
| 645 | 39 | 34.48 | Position +20% — hold ret_high_14d_open | Position +20% | high | 14 | open | 4 | 100.0 | 9.58 | 9.2 | 38.32 | 5.54 | 1.73 | 3.55 | 16.38 |
| 646 | 51 | 20.1 | Position +30% — hold ret_high_14d_news | Position +30% | high | 14 | news | 3 | 100.0 | 9.56 | 12.15 | 28.69 | 5.43 | 1.76 | 3.32 | 13.22 |
| 647 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_high_3d_news | Mid cap (1B–10B) CEO/CFO | high | 3 | news | 2 | 100.0 | 9.48 | 9.47 | 18.95 | 12.57 | 0.75 | 0.59 | 18.36 |
| 648 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_mean_3d_news | CEO only + Value ≥500k | mean | 3 | news | 1 | 100.0 | 9.47 | 9.47 | 9.47 | nan | nan | 9.47 | 9.47 |
| 649 | 1 | 100.0 | CEO only + Position +10% — hold ret_mean_3d_news | CEO only + Position +10% | mean | 3 | news | 1 | 100.0 | 9.47 | 9.47 | 9.47 | nan | nan | 9.47 | 9.47 |
| 650 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_mean_3d_news | Near 52w high + CEO/CFO | mean | 3 | news | 1 | 100.0 | 9.47 | 9.47 | 9.47 | nan | nan | 9.47 | 9.47 |
| 651 | 15 | 62.43 | Price > MA50 — hold ret_high_5d_news | Price > MA50 | high | 5 | news | 5 | 100.0 | 9.46 | 7.34 | 47.32 | 8.43 | 1.12 | 1.27 | 23.65 |
| 652 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_high_7d_open | Large cap (≥3B) CEO/CFO | high | 7 | open | 1 | 100.0 | 9.46 | 9.46 | 9.46 | nan | nan | 9.46 | 9.46 |
| 653 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_high_7d_open | Large cap (≥5B) CEO/CFO | high | 7 | open | 1 | 100.0 | 9.46 | 9.46 | 9.46 | nan | nan | 9.46 | 9.46 |
| 654 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_high_7d_open | Large cap (≥10B) CEO/CFO | high | 7 | open | 1 | 100.0 | 9.46 | 9.46 | 9.46 | nan | nan | 9.46 | 9.46 |
| 655 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_high_10d_open | Large cap (≥3B) CEO/CFO | high | 10 | open | 1 | 100.0 | 9.46 | 9.46 | 9.46 | nan | nan | 9.46 | 9.46 |
| 656 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_high_10d_open | Large cap (≥5B) CEO/CFO | high | 10 | open | 1 | 100.0 | 9.46 | 9.46 | 9.46 | nan | nan | 9.46 | 9.46 |
| 657 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_high_10d_open | Large cap (≥10B) CEO/CFO | high | 10 | open | 1 | 100.0 | 9.46 | 9.46 | 9.46 | nan | nan | 9.46 | 9.46 |
| 658 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_high_14d_open | Large cap (≥3B) CEO/CFO | high | 14 | open | 1 | 100.0 | 9.46 | 9.46 | 9.46 | nan | nan | 9.46 | 9.46 |
| 659 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_high_14d_open | Large cap (≥5B) CEO/CFO | high | 14 | open | 1 | 100.0 | 9.46 | 9.46 | 9.46 | nan | nan | 9.46 | 9.46 |
| 660 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_high_14d_open | Large cap (≥10B) CEO/CFO | high | 14 | open | 1 | 100.0 | 9.46 | 9.46 | 9.46 | nan | nan | 9.46 | 9.46 |
| 661 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_high_30d_open | Large cap (≥3B) CEO/CFO | high | 30 | open | 1 | 100.0 | 9.46 | 9.46 | 9.46 | nan | nan | 9.46 | 9.46 |
| 662 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_high_30d_open | Large cap (≥5B) CEO/CFO | high | 30 | open | 1 | 100.0 | 9.46 | 9.46 | 9.46 | nan | nan | 9.46 | 9.46 |
| 663 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_high_30d_open | Large cap (≥10B) CEO/CFO | high | 30 | open | 1 | 100.0 | 9.46 | 9.46 | 9.46 | nan | nan | 9.46 | 9.46 |
| 664 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_high_60d_open | Large cap (≥3B) CEO/CFO | high | 60 | open | 1 | 100.0 | 9.46 | 9.46 | 9.46 | nan | nan | 9.46 | 9.46 |
| 665 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_high_60d_open | Large cap (≥5B) CEO/CFO | high | 60 | open | 1 | 100.0 | 9.46 | 9.46 | 9.46 | nan | nan | 9.46 | 9.46 |
| 666 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_high_60d_open | Large cap (≥10B) CEO/CFO | high | 60 | open | 1 | 100.0 | 9.46 | 9.46 | 9.46 | nan | nan | 9.46 | 9.46 |
| 667 | 30 | 48.32 | Value ≥100k — hold ret_high_5d_news | Value ≥100k | high | 5 | news | 6 | 100.0 | 9.44 | 8.12 | 56.64 | 7.97 | 1.18 | 1.27 | 23.65 |
| 668 | 4 | 82.51 | CEO + Director (combo) — hold ret_high_3d_open | CEO + Director (combo) | high | 3 | open | 1 | 100.0 | 9.42 | 9.42 | 9.42 | nan | nan | 9.42 | 9.42 |
| 669 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_high_3d_open | Small cap (≤1B) CEO/CFO | high | 3 | open | 1 | 100.0 | 9.42 | 9.42 | 9.42 | nan | nan | 9.42 | 9.42 |
| 670 | 4 | 82.51 | CEO + Director (combo) — hold ret_high_5d_open | CEO + Director (combo) | high | 5 | open | 1 | 100.0 | 9.42 | 9.42 | 9.42 | nan | nan | 9.42 | 9.42 |
| 671 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_high_5d_open | Small cap (≤1B) CEO/CFO | high | 5 | open | 1 | 100.0 | 9.42 | 9.42 | 9.42 | nan | nan | 9.42 | 9.42 |
| 672 | 31 | 47.75 | Value ≥50k — hold ret_high_10d_open | Value ≥50k | high | 10 | open | 9 | 100.0 | 9.41 | 8.08 | 84.67 | 6.65 | 1.42 | 2.03 | 23.43 |
| 673 | 28 | 48.48 | Tutti — hold ret_high_10d_news | Tutti | high | 10 | news | 10 | 100.0 | 9.38 | 7.06 | 93.78 | 6.85 | 1.37 | 2.83 | 25.19 |
| 674 | 21 | 53.67 | Qty ≥5k shares — hold ret_high_5d_news | Qty ≥5k shares | high | 5 | news | 6 | 100.0 | 9.36 | 7.86 | 56.13 | 7.98 | 1.17 | 1.27 | 23.65 |
| 675 | 20 | 53.67 | Qty ≥10k shares — hold ret_high_5d_news | Qty ≥10k shares | high | 5 | news | 6 | 100.0 | 9.36 | 7.86 | 56.13 | 7.98 | 1.17 | 1.27 | 23.65 |
| 676 | 33 | 41.81 | Director — hold ret_high_14d_news | Director | high | 14 | news | 8 | 100.0 | 9.36 | 9.95 | 74.9 | 4.98 | 1.88 | 3.32 | 17.14 |
| 677 | 4 | 82.51 | CEO + Director (combo) — hold ret_mean_30d_news | CEO + Director (combo) | mean | 30 | news | 1 | 100.0 | 9.36 | 9.36 | 9.36 | nan | nan | 9.36 | 9.36 |
| 678 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_mean_30d_news | Small cap (≤1B) CEO/CFO | mean | 30 | news | 1 | 100.0 | 9.36 | 9.36 | 9.36 | nan | nan | 9.36 | 9.36 |
| 679 | 6 | 77.62 | CEO only — hold ret_high_2d_open | CEO only | high | 2 | open | 3 | 100.0 | 9.35 | 8.65 | 28.04 | 3.76 | 2.48 | 5.98 | 13.41 |
| 680 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_high_1d_news | CEO only + Value ≥100k | high | 1 | news | 2 | 100.0 | 9.34 | 9.34 | 18.68 | 0.96 | 9.71 | 8.66 | 10.02 |
| 681 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_high_1d_news | Price > MA50 + CEO/CFO | high | 1 | news | 2 | 100.0 | 9.34 | 9.34 | 18.68 | 0.96 | 9.71 | 8.66 | 10.02 |
| 682 | 15 | 62.43 | Price > MA50 — hold ret_high_7d_open | Price > MA50 | high | 7 | open | 5 | 100.0 | 9.32 | 7.07 | 46.61 | 8.55 | 1.09 | 0.48 | 23.43 |
| 683 | 21 | 53.67 | Qty ≥5k shares — hold ret_high_5d_open | Qty ≥5k shares | high | 5 | open | 6 | 100.0 | 9.3 | 7.94 | 55.8 | 7.19 | 1.29 | 0.48 | 21.91 |
| 684 | 20 | 53.67 | Qty ≥10k shares — hold ret_high_5d_open | Qty ≥10k shares | high | 5 | open | 6 | 100.0 | 9.3 | 7.94 | 55.8 | 7.19 | 1.29 | 0.48 | 21.91 |
| 685 | 14 | 65.45 | Price > MA200 — hold ret_high_7d_open | Price > MA200 | high | 7 | open | 4 | 100.0 | 9.29 | 6.62 | 37.15 | 9.87 | 0.94 | 0.48 | 23.43 |
| 686 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_mean_10d_news | CEO only + Value ≥100k | mean | 10 | news | 2 | 100.0 | 9.28 | 9.28 | 18.56 | 7.64 | 1.22 | 3.88 | 14.68 |
| 687 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_mean_10d_news | Price > MA50 + CEO/CFO | mean | 10 | news | 2 | 100.0 | 9.28 | 9.28 | 18.56 | 7.64 | 1.22 | 3.88 | 14.68 |
| 688 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_high_10d_open | Multiple buys (n≥2) | high | 10 | open | 3 | 100.0 | 9.27 | 8.08 | 27.81 | 5.42 | 1.71 | 4.54 | 15.19 |
| 689 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_high_3d_news | CEO/CFO + Value ≥100k | high | 3 | news | 3 | 100.0 | 9.25 | 8.8 | 27.75 | 8.89 | 1.04 | 0.59 | 18.36 |
| 690 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_high_3d_news | Large cap (≥750M) CEO/CFO | high | 3 | news | 3 | 100.0 | 9.25 | 8.8 | 27.75 | 8.89 | 1.04 | 0.59 | 18.36 |
| 691 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_high_3d_news | Large cap (≥1B) CEO/CFO | high | 3 | news | 3 | 100.0 | 9.25 | 8.8 | 27.75 | 8.89 | 1.04 | 0.59 | 18.36 |
| 692 | 39 | 34.48 | Position +20% — hold ret_high_14d_news | Position +20% | high | 14 | news | 4 | 100.0 | 9.16 | 10.05 | 36.65 | 4.51 | 2.03 | 3.32 | 13.22 |
| 693 | 31 | 47.75 | Value ≥50k — hold ret_high_7d_news | Value ≥50k | high | 7 | news | 9 | 100.0 | 9.09 | 7.96 | 81.85 | 7.18 | 1.27 | 1.27 | 25.19 |
| 694 | 28 | 48.48 | Tutti — hold ret_high_10d_open | Tutti | high | 10 | open | 10 | 100.0 | 9.08 | 7.58 | 90.84 | 6.35 | 1.43 | 2.03 | 23.43 |
| 695 | 37 | 35.58 | Director only + Value ≥100k — hold ret_high_30d_news | Director only + Value ≥100k | high | 30 | news | 3 | 100.0 | 9.08 | 7.96 | 27.24 | 2.69 | 3.37 | 7.13 | 12.15 |
| 696 | 10 | 66.41 | CEO/CFO — hold ret_high_3d_news | CEO/CFO | high | 3 | news | 4 | 100.0 | 9.03 | 8.59 | 36.13 | 7.27 | 1.24 | 0.59 | 18.36 |
| 697 | 11 | 66.41 | Officer/President — hold ret_high_3d_news | Officer/President | high | 3 | news | 4 | 100.0 | 9.03 | 8.59 | 36.13 | 7.27 | 1.24 | 0.59 | 18.36 |
| 698 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_high_3d_news | Large cap (≥250M) CEO/CFO | high | 3 | news | 4 | 100.0 | 9.03 | 8.59 | 36.13 | 7.27 | 1.24 | 0.59 | 18.36 |
| 699 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_high_3d_news | Large cap (≥500M) CEO/CFO | high | 3 | news | 4 | 100.0 | 9.03 | 8.59 | 36.13 | 7.27 | 1.24 | 0.59 | 18.36 |
| 700 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_high_5d_news | Mid cap (1B–10B) Value ≥100k | high | 5 | news | 4 | 100.0 | 8.9 | 5.34 | 35.6 | 10.15 | 0.88 | 1.27 | 23.65 |
| 701 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_high_5d_news | Large cap (≥3B) CEO/CFO | high | 5 | news | 1 | 100.0 | 8.89 | 8.89 | 8.89 | nan | nan | 8.89 | 8.89 |
| 702 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_high_5d_news | Large cap (≥5B) CEO/CFO | high | 5 | news | 1 | 100.0 | 8.89 | 8.89 | 8.89 | nan | nan | 8.89 | 8.89 |
| 703 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_high_5d_news | Large cap (≥10B) CEO/CFO | high | 5 | news | 1 | 100.0 | 8.89 | 8.89 | 8.89 | nan | nan | 8.89 | 8.89 |
| 704 | 10 | 66.41 | CEO/CFO — hold ret_high_3d_open | CEO/CFO | high | 3 | open | 4 | 100.0 | 8.87 | 7.7 | 35.48 | 5.77 | 1.54 | 3.39 | 16.69 |
| 705 | 11 | 66.41 | Officer/President — hold ret_high_3d_open | Officer/President | high | 3 | open | 4 | 100.0 | 8.87 | 7.7 | 35.48 | 5.77 | 1.54 | 3.39 | 16.69 |
| 706 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_high_3d_open | Large cap (≥250M) CEO/CFO | high | 3 | open | 4 | 100.0 | 8.87 | 7.7 | 35.48 | 5.77 | 1.54 | 3.39 | 16.69 |
| 707 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_high_3d_open | Large cap (≥500M) CEO/CFO | high | 3 | open | 4 | 100.0 | 8.87 | 7.7 | 35.48 | 5.77 | 1.54 | 3.39 | 16.69 |
| 708 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_high_2d_news | Large cap (≥3B) CEO/CFO | high | 2 | news | 1 | 100.0 | 8.8 | 8.8 | 8.8 | nan | nan | 8.8 | 8.8 |
| 709 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_high_2d_news | Large cap (≥5B) CEO/CFO | high | 2 | news | 1 | 100.0 | 8.8 | 8.8 | 8.8 | nan | nan | 8.8 | 8.8 |
| 710 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_high_2d_news | Large cap (≥10B) CEO/CFO | high | 2 | news | 1 | 100.0 | 8.8 | 8.8 | 8.8 | nan | nan | 8.8 | 8.8 |
| 711 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_high_3d_news | Large cap (≥3B) CEO/CFO | high | 3 | news | 1 | 100.0 | 8.8 | 8.8 | 8.8 | nan | nan | 8.8 | 8.8 |
| 712 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_high_3d_news | Large cap (≥5B) CEO/CFO | high | 3 | news | 1 | 100.0 | 8.8 | 8.8 | 8.8 | nan | nan | 8.8 | 8.8 |
| 713 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_high_3d_news | Large cap (≥10B) CEO/CFO | high | 3 | news | 1 | 100.0 | 8.8 | 8.8 | 8.8 | nan | nan | 8.8 | 8.8 |
| 714 | 28 | 48.48 | Tutti — hold ret_high_7d_news | Tutti | high | 7 | news | 10 | 100.0 | 8.8 | 7.06 | 88.02 | 6.83 | 1.29 | 1.27 | 25.19 |
| 715 | 6 | 77.62 | CEO only — hold ret_high_1d_news | CEO only | high | 1 | news | 3 | 100.0 | 8.77 | 8.66 | 26.3 | 1.2 | 7.28 | 7.62 | 10.02 |
| 716 | 31 | 47.75 | Value ≥50k — hold ret_high_7d_open | Value ≥50k | high | 7 | open | 9 | 100.0 | 8.77 | 8.08 | 78.89 | 6.56 | 1.34 | 0.48 | 23.43 |
| 717 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_high_7d_open | Large cap (≥2B) CEO/CFO | high | 7 | open | 2 | 100.0 | 8.77 | 8.77 | 17.54 | 0.98 | 8.99 | 8.08 | 9.46 |
| 718 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_high_10d_open | Large cap (≥2B) CEO/CFO | high | 10 | open | 2 | 100.0 | 8.77 | 8.77 | 17.54 | 0.98 | 8.99 | 8.08 | 9.46 |
| 719 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_high_5d_open | Mid cap (1B–10B) Value ≥100k | high | 5 | open | 4 | 100.0 | 8.76 | 6.33 | 35.06 | 9.19 | 0.95 | 0.48 | 21.91 |
| 720 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_high_7d_news | Large cap (≥2B) CEO/CFO | high | 7 | news | 2 | 100.0 | 8.76 | 8.76 | 17.52 | 5.11 | 1.72 | 5.15 | 12.37 |
| 721 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_high_10d_news | Large cap (≥2B) CEO/CFO | high | 10 | news | 2 | 100.0 | 8.76 | 8.76 | 17.52 | 5.11 | 1.72 | 5.15 | 12.37 |
| 722 | 14 | 65.45 | Price > MA200 — hold ret_high_5d_open | Price > MA200 | high | 5 | open | 4 | 100.0 | 8.75 | 6.31 | 35.01 | 9.19 | 0.95 | 0.48 | 21.91 |
| 723 | 30 | 48.32 | Value ≥100k — hold ret_high_5d_open | Value ≥100k | high | 5 | open | 6 | 100.0 | 8.74 | 6.33 | 52.45 | 7.31 | 1.2 | 0.48 | 21.91 |
| 724 | 40 | 33.74 | Director only + Position +10% — hold ret_high_60d_news | Director only + Position +10% | high | 60 | news | 4 | 100.0 | 8.74 | 9.13 | 34.96 | 3.28 | 2.66 | 4.54 | 12.15 |
| 725 | 40 | 33.74 | Director only + Position +10% — hold ret_high_90d_news | Director only + Position +10% | high | 90 | news | 4 | 100.0 | 8.74 | 9.13 | 34.96 | 3.28 | 2.66 | 4.54 | 12.15 |
| 726 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_mean_5d_news | CEO only + Value ≥100k | mean | 5 | news | 2 | 100.0 | 8.73 | 8.73 | 17.46 | 5.35 | 1.63 | 4.95 | 12.51 |
| 727 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_mean_5d_news | Price > MA50 + CEO/CFO | mean | 5 | news | 2 | 100.0 | 8.73 | 8.73 | 17.46 | 5.35 | 1.63 | 4.95 | 12.51 |
| 728 | 32 | 44.63 | Position +10% — hold ret_high_5d_news | Position +10% | high | 5 | news | 6 | 100.0 | 8.71 | 5.94 | 52.28 | 8.23 | 1.06 | 1.26 | 23.65 |
| 729 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_high_3d_open | CEO/CFO + Value ≥100k | high | 3 | open | 3 | 100.0 | 8.69 | 5.98 | 26.06 | 7.05 | 1.23 | 3.39 | 16.69 |
| 730 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_high_3d_open | Large cap (≥750M) CEO/CFO | high | 3 | open | 3 | 100.0 | 8.69 | 5.98 | 26.06 | 7.05 | 1.23 | 3.39 | 16.69 |
| 731 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_high_3d_open | Large cap (≥1B) CEO/CFO | high | 3 | open | 3 | 100.0 | 8.69 | 5.98 | 26.06 | 7.05 | 1.23 | 3.39 | 16.69 |
| 732 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_high_1d_news | Large cap (≥3B) CEO/CFO | high | 1 | news | 1 | 100.0 | 8.66 | 8.66 | 8.66 | nan | nan | 8.66 | 8.66 |
| 733 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_high_1d_news | Large cap (≥5B) CEO/CFO | high | 1 | news | 1 | 100.0 | 8.66 | 8.66 | 8.66 | nan | nan | 8.66 | 8.66 |
| 734 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_high_1d_news | Large cap (≥10B) CEO/CFO | high | 1 | news | 1 | 100.0 | 8.66 | 8.66 | 8.66 | nan | nan | 8.66 | 8.66 |
| 735 | 4 | 82.51 | CEO + Director (combo) — hold ret_high_1d_open | CEO + Director (combo) | high | 1 | open | 1 | 100.0 | 8.65 | 8.65 | 8.65 | nan | nan | 8.65 | 8.65 |
| 736 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_high_1d_open | Small cap (≤1B) CEO/CFO | high | 1 | open | 1 | 100.0 | 8.65 | 8.65 | 8.65 | nan | nan | 8.65 | 8.65 |
| 737 | 4 | 82.51 | CEO + Director (combo) — hold ret_high_2d_open | CEO + Director (combo) | high | 2 | open | 1 | 100.0 | 8.65 | 8.65 | 8.65 | nan | nan | 8.65 | 8.65 |
| 738 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_high_2d_open | Small cap (≤1B) CEO/CFO | high | 2 | open | 1 | 100.0 | 8.65 | 8.65 | 8.65 | nan | nan | 8.65 | 8.65 |
| 739 | 32 | 44.63 | Position +10% — hold ret_high_5d_open | Position +10% | high | 5 | open | 6 | 100.0 | 8.65 | 6.33 | 51.93 | 7.24 | 1.2 | 1.49 | 21.91 |
| 740 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_mean_30d_open | Mid cap (1B–10B) CEO/CFO | mean | 30 | open | 2 | 100.0 | 8.64 | 8.64 | 17.28 | 4.71 | 1.83 | 5.31 | 11.97 |
| 741 | 38 | 34.53 | Price < MA50 — hold ret_high_10d_open | Price < MA50 | high | 10 | open | 5 | 100.0 | 8.54 | 8.08 | 42.68 | 4.82 | 1.77 | 3.55 | 15.19 |
| 742 | 36 | 36.54 | Director only (no C-level) — hold ret_high_30d_news | Director only (no C-level) | high | 30 | news | 6 | 100.0 | 8.53 | 7.54 | 51.16 | 4.8 | 1.78 | 3.32 | 16.06 |
| 743 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_mean_14d_open | Mid cap (1B–10B) CEO/CFO | mean | 14 | open | 2 | 100.0 | 8.52 | 8.52 | 17.04 | 6.18 | 1.38 | 4.15 | 12.89 |
| 744 | 28 | 48.48 | Tutti — hold ret_high_7d_open | Tutti | high | 7 | open | 10 | 100.0 | 8.51 | 7.58 | 85.06 | 6.24 | 1.36 | 0.48 | 23.43 |
| 745 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_high_1d_open | CEO only + Value ≥500k | high | 1 | open | 1 | 100.0 | 8.48 | 8.48 | 8.48 | nan | nan | 8.48 | 8.48 |
| 746 | 1 | 100.0 | CEO only + Position +10% — hold ret_high_1d_open | CEO only + Position +10% | high | 1 | open | 1 | 100.0 | 8.48 | 8.48 | 8.48 | nan | nan | 8.48 | 8.48 |
| 747 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_high_1d_open | Near 52w high + CEO/CFO | high | 1 | open | 1 | 100.0 | 8.48 | 8.48 | 8.48 | nan | nan | 8.48 | 8.48 |
| 748 | 4 | 82.51 | CEO + Director (combo) — hold ret_mean_14d_open | CEO + Director (combo) | mean | 14 | open | 1 | 100.0 | 8.42 | 8.42 | 8.42 | nan | nan | 8.42 | 8.42 |
| 749 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_mean_14d_open | Small cap (≤1B) CEO/CFO | mean | 14 | open | 1 | 100.0 | 8.42 | 8.42 | 8.42 | nan | nan | 8.42 | 8.42 |
| 750 | 4 | 82.51 | CEO + Director (combo) — hold ret_high_3d_news | CEO + Director (combo) | high | 3 | news | 1 | 100.0 | 8.38 | 8.38 | 8.38 | nan | nan | 8.38 | 8.38 |
| 751 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_high_3d_news | Small cap (≤1B) CEO/CFO | high | 3 | news | 1 | 100.0 | 8.38 | 8.38 | 8.38 | nan | nan | 8.38 | 8.38 |
| 752 | 4 | 82.51 | CEO + Director (combo) — hold ret_high_5d_news | CEO + Director (combo) | high | 5 | news | 1 | 100.0 | 8.38 | 8.38 | 8.38 | nan | nan | 8.38 | 8.38 |
| 753 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_high_5d_news | Small cap (≤1B) CEO/CFO | high | 5 | news | 1 | 100.0 | 8.38 | 8.38 | 8.38 | nan | nan | 8.38 | 8.38 |
| 754 | 40 | 33.74 | Director only + Position +10% — hold ret_high_60d_open | Director only + Position +10% | high | 60 | open | 4 | 100.0 | 8.37 | 8.82 | 33.49 | 3.15 | 2.65 | 4.54 | 11.32 |
| 755 | 40 | 33.74 | Director only + Position +10% — hold ret_high_90d_open | Director only + Position +10% | high | 90 | open | 4 | 100.0 | 8.37 | 8.82 | 33.49 | 3.15 | 2.65 | 4.54 | 11.32 |
| 756 | 37 | 35.58 | Director only + Value ≥100k — hold ret_high_14d_news | Director only + Value ≥100k | high | 14 | news | 3 | 100.0 | 8.25 | 7.96 | 24.74 | 3.77 | 2.19 | 4.63 | 12.15 |
| 757 | 37 | 35.58 | Director only + Value ≥100k — hold ret_high_30d_open | Director only + Value ≥100k | high | 30 | open | 3 | 100.0 | 8.23 | 7.07 | 24.69 | 2.7 | 3.04 | 6.3 | 11.32 |
| 758 | 15 | 62.43 | Price > MA50 — hold ret_high_5d_open | Price > MA50 | high | 5 | open | 5 | 100.0 | 8.22 | 6.17 | 41.08 | 8.05 | 1.02 | 0.48 | 21.91 |
| 759 | 6 | 77.62 | CEO only — hold ret_mean_10d_news | CEO only | mean | 10 | news | 3 | 100.0 | 8.17 | 5.96 | 24.52 | 5.73 | 1.43 | 3.88 | 14.68 |
| 760 | 15 | 62.43 | Price > MA50 — hold ret_high_3d_news | Price > MA50 | high | 3 | news | 5 | 100.0 | 8.15 | 6.17 | 40.74 | 6.32 | 1.29 | 1.27 | 18.36 |
| 761 | 36 | 36.54 | Director only (no C-level) — hold ret_high_30d_open | Director only (no C-level) | high | 30 | open | 6 | 100.0 | 8.14 | 6.69 | 48.84 | 4.72 | 1.72 | 3.55 | 16.06 |
| 762 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_high_5d_news | Far 52w high + Value ≥100k | high | 5 | news | 3 | 100.0 | 8.13 | 8.89 | 24.38 | 4.45 | 1.82 | 3.34 | 12.15 |
| 763 | 35 | 40.48 | Value ≥500k — hold ret_high_3d_news | Value ≥500k | high | 3 | news | 4 | 100.0 | 8.09 | 6.71 | 32.37 | 8.65 | 0.94 | 0.59 | 18.36 |
| 764 | 49 | 32.78 | CFO only — hold ret_high_7d_open | CFO only | high | 7 | open | 1 | 100.0 | 8.08 | 8.08 | 8.08 | nan | nan | 8.08 | 8.08 |
| 765 | 48 | 32.78 | CFO + Director (combo) — hold ret_high_7d_open | CFO + Director (combo) | high | 7 | open | 1 | 100.0 | 8.08 | 8.08 | 8.08 | nan | nan | 8.08 | 8.08 |
| 766 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_high_7d_open | CFO only + Value ≥50k | high | 7 | open | 1 | 100.0 | 8.08 | 8.08 | 8.08 | nan | nan | 8.08 | 8.08 |
| 767 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_high_7d_open | CFO only + Value ≥100k | high | 7 | open | 1 | 100.0 | 8.08 | 8.08 | 8.08 | nan | nan | 8.08 | 8.08 |
| 768 | 47 | 32.78 | CFO only + Position +10% — hold ret_high_7d_open | CFO only + Position +10% | high | 7 | open | 1 | 100.0 | 8.08 | 8.08 | 8.08 | nan | nan | 8.08 | 8.08 |
| 769 | 46 | 32.78 | CFO only + Position +20% — hold ret_high_7d_open | CFO only + Position +20% | high | 7 | open | 1 | 100.0 | 8.08 | 8.08 | 8.08 | nan | nan | 8.08 | 8.08 |
| 770 | 44 | 32.78 | RSI oversold (<30) — hold ret_high_7d_open | RSI oversold (<30) | high | 7 | open | 1 | 100.0 | 8.08 | 8.08 | 8.08 | nan | nan | 8.08 | 8.08 |
| 771 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_high_7d_open | RSI oversold + CEO/CFO | high | 7 | open | 1 | 100.0 | 8.08 | 8.08 | 8.08 | nan | nan | 8.08 | 8.08 |
| 772 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_high_7d_open | RSI oversold + Value ≥100k | high | 7 | open | 1 | 100.0 | 8.08 | 8.08 | 8.08 | nan | nan | 8.08 | 8.08 |
| 773 | 49 | 32.78 | CFO only — hold ret_high_10d_open | CFO only | high | 10 | open | 1 | 100.0 | 8.08 | 8.08 | 8.08 | nan | nan | 8.08 | 8.08 |
| 774 | 48 | 32.78 | CFO + Director (combo) — hold ret_high_10d_open | CFO + Director (combo) | high | 10 | open | 1 | 100.0 | 8.08 | 8.08 | 8.08 | nan | nan | 8.08 | 8.08 |
| 775 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_high_10d_open | CFO only + Value ≥50k | high | 10 | open | 1 | 100.0 | 8.08 | 8.08 | 8.08 | nan | nan | 8.08 | 8.08 |
| 776 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_high_10d_open | CFO only + Value ≥100k | high | 10 | open | 1 | 100.0 | 8.08 | 8.08 | 8.08 | nan | nan | 8.08 | 8.08 |
| 777 | 47 | 32.78 | CFO only + Position +10% — hold ret_high_10d_open | CFO only + Position +10% | high | 10 | open | 1 | 100.0 | 8.08 | 8.08 | 8.08 | nan | nan | 8.08 | 8.08 |
| 778 | 46 | 32.78 | CFO only + Position +20% — hold ret_high_10d_open | CFO only + Position +20% | high | 10 | open | 1 | 100.0 | 8.08 | 8.08 | 8.08 | nan | nan | 8.08 | 8.08 |
| 779 | 44 | 32.78 | RSI oversold (<30) — hold ret_high_10d_open | RSI oversold (<30) | high | 10 | open | 1 | 100.0 | 8.08 | 8.08 | 8.08 | nan | nan | 8.08 | 8.08 |
| 780 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_high_10d_open | RSI oversold + CEO/CFO | high | 10 | open | 1 | 100.0 | 8.08 | 8.08 | 8.08 | nan | nan | 8.08 | 8.08 |
| 781 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_high_10d_open | RSI oversold + Value ≥100k | high | 10 | open | 1 | 100.0 | 8.08 | 8.08 | 8.08 | nan | nan | 8.08 | 8.08 |
| 782 | 6 | 77.62 | CEO only — hold ret_mean_7d_news | CEO only | mean | 7 | news | 3 | 100.0 | 8.01 | 5.89 | 24.02 | 5.26 | 1.52 | 4.14 | 13.99 |
| 783 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_mean_30d_news | Mid cap (1B–10B) CEO/CFO | mean | 30 | news | 2 | 100.0 | 8.01 | 8.01 | 16.02 | 7.86 | 1.02 | 2.45 | 13.57 |
| 784 | 14 | 65.45 | Price > MA200 — hold ret_high_3d_news | Price > MA200 | high | 3 | news | 4 | 100.0 | 7.98 | 6.15 | 31.94 | 7.29 | 1.1 | 1.27 | 18.36 |
| 785 | 35 | 40.48 | Value ≥500k — hold ret_high_3d_open | Value ≥500k | high | 3 | open | 4 | 100.0 | 7.97 | 7.36 | 31.88 | 7.4 | 1.08 | 0.48 | 16.69 |
| 786 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_high_2d_open | Mid cap (1B–10B) CEO/CFO | high | 2 | open | 2 | 100.0 | 7.96 | 7.96 | 15.93 | 7.7 | 1.03 | 2.52 | 13.41 |
| 787 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_mean_3d_open | CEO only + Value ≥500k | mean | 3 | open | 1 | 100.0 | 7.93 | 7.93 | 7.93 | nan | nan | 7.93 | 7.93 |
| 788 | 1 | 100.0 | CEO only + Position +10% — hold ret_mean_3d_open | CEO only + Position +10% | mean | 3 | open | 1 | 100.0 | 7.93 | 7.93 | 7.93 | nan | nan | 7.93 | 7.93 |
| 789 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_mean_3d_open | Near 52w high + CEO/CFO | mean | 3 | open | 1 | 100.0 | 7.93 | 7.93 | 7.93 | nan | nan | 7.93 | 7.93 |
| 790 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_high_10d_news | Multiple buys (n≥2) | high | 10 | news | 3 | 100.0 | 7.93 | 5.15 | 23.79 | 5.35 | 1.48 | 4.54 | 14.1 |
| 791 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_mean_14d_news | Mid cap (1B–10B) CEO/CFO | mean | 14 | news | 2 | 100.0 | 7.9 | 7.91 | 15.81 | 9.31 | 0.85 | 1.32 | 14.49 |
| 792 | 30 | 48.32 | Value ≥100k — hold ret_high_3d_news | Value ≥100k | high | 3 | news | 6 | 100.0 | 7.88 | 7.47 | 47.31 | 6.76 | 1.17 | 0.59 | 18.36 |
| 793 | 31 | 47.75 | Value ≥50k — hold ret_high_5d_news | Value ≥50k | high | 5 | news | 9 | 100.0 | 7.87 | 7.34 | 70.82 | 6.96 | 1.13 | 1.26 | 23.65 |
| 794 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_high_5d_open | Far 52w high + Value ≥100k | high | 5 | open | 3 | 100.0 | 7.87 | 6.22 | 23.61 | 2.99 | 2.63 | 6.07 | 11.32 |
| 795 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_high_7d_open | Multiple buys (n≥2) | high | 7 | open | 3 | 100.0 | 7.86 | 8.08 | 23.58 | 3.22 | 2.44 | 4.54 | 10.96 |
| 796 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_high_2d_news | CEO/CFO + Value ≥100k | high | 2 | news | 3 | 66.7 | 7.85 | 8.8 | 23.56 | 7.68 | 1.02 | -0.26 | 15.02 |
| 797 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_high_2d_news | Large cap (≥750M) CEO/CFO | high | 2 | news | 3 | 66.7 | 7.85 | 8.8 | 23.56 | 7.68 | 1.02 | -0.26 | 15.02 |
| 798 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_high_2d_news | Large cap (≥1B) CEO/CFO | high | 2 | news | 3 | 66.7 | 7.85 | 8.8 | 23.56 | 7.68 | 1.02 | -0.26 | 15.02 |
| 799 | 38 | 34.53 | Price < MA50 — hold ret_high_10d_news | Price < MA50 | high | 10 | news | 5 | 100.0 | 7.85 | 5.15 | 39.26 | 4.91 | 1.6 | 3.32 | 14.1 |
| 800 | 21 | 53.67 | Qty ≥5k shares — hold ret_high_3d_news | Qty ≥5k shares | high | 3 | news | 6 | 100.0 | 7.82 | 7.26 | 46.89 | 6.76 | 1.16 | 0.59 | 18.36 |
| 801 | 20 | 53.67 | Qty ≥10k shares — hold ret_high_3d_news | Qty ≥10k shares | high | 3 | news | 6 | 100.0 | 7.82 | 7.26 | 46.89 | 6.76 | 1.16 | 0.59 | 18.36 |
| 802 | 10 | 66.41 | CEO/CFO — hold ret_high_2d_news | CEO/CFO | high | 2 | news | 4 | 75.0 | 7.8 | 8.21 | 31.18 | 6.27 | 1.24 | -0.26 | 15.02 |
| 803 | 11 | 66.41 | Officer/President — hold ret_high_2d_news | Officer/President | high | 2 | news | 4 | 75.0 | 7.8 | 8.21 | 31.18 | 6.27 | 1.24 | -0.26 | 15.02 |
| 804 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_high_2d_news | Large cap (≥250M) CEO/CFO | high | 2 | news | 4 | 75.0 | 7.8 | 8.21 | 31.18 | 6.27 | 1.24 | -0.26 | 15.02 |
| 805 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_high_2d_news | Large cap (≥500M) CEO/CFO | high | 2 | news | 4 | 75.0 | 7.8 | 8.21 | 31.18 | 6.27 | 1.24 | -0.26 | 15.02 |
| 806 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_mean_7d_open | CEO only + Value ≥100k | mean | 7 | open | 2 | 100.0 | 7.77 | 7.77 | 15.54 | 6.53 | 1.19 | 3.15 | 12.39 |
| 807 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_mean_7d_open | Price > MA50 + CEO/CFO | mean | 7 | open | 2 | 100.0 | 7.77 | 7.77 | 15.54 | 6.53 | 1.19 | 3.15 | 12.39 |
| 808 | 21 | 53.67 | Qty ≥5k shares — hold ret_high_3d_open | Qty ≥5k shares | high | 3 | open | 6 | 100.0 | 7.76 | 7.34 | 46.56 | 5.89 | 1.32 | 0.48 | 16.69 |
| 809 | 20 | 53.67 | Qty ≥10k shares — hold ret_high_3d_open | Qty ≥10k shares | high | 3 | open | 6 | 100.0 | 7.76 | 7.34 | 46.56 | 5.89 | 1.32 | 0.48 | 16.69 |
| 810 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_mean_10d_open | Mid cap (1B–10B) CEO/CFO | mean | 10 | open | 2 | 100.0 | 7.74 | 7.75 | 15.49 | 7.53 | 1.03 | 2.42 | 13.07 |
| 811 | 28 | 48.48 | Tutti — hold ret_high_5d_news | Tutti | high | 5 | news | 10 | 100.0 | 7.7 | 6.75 | 76.99 | 6.59 | 1.17 | 1.26 | 23.65 |
| 812 | 38 | 34.53 | Price < MA50 — hold ret_high_7d_open | Price < MA50 | high | 7 | open | 5 | 100.0 | 7.69 | 8.08 | 38.45 | 3.57 | 2.15 | 3.55 | 11.32 |
| 813 | 6 | 77.62 | CEO only — hold ret_high_1d_open | CEO only | high | 1 | open | 3 | 100.0 | 7.66 | 8.48 | 22.97 | 1.58 | 4.86 | 5.84 | 8.65 |
| 814 | 51 | 20.1 | Position +30% — hold ret_high_7d_open | Position +30% | high | 7 | open | 3 | 100.0 | 7.65 | 8.08 | 22.95 | 3.9 | 1.96 | 3.55 | 11.32 |
| 815 | 37 | 35.58 | Director only + Value ≥100k — hold ret_high_10d_news | Director only + Value ≥100k | high | 10 | news | 3 | 100.0 | 7.65 | 7.96 | 22.94 | 4.67 | 1.64 | 2.83 | 12.15 |
| 816 | 51 | 20.1 | Position +30% — hold ret_high_10d_open | Position +30% | high | 10 | open | 3 | 100.0 | 7.65 | 8.08 | 22.95 | 3.9 | 1.96 | 3.55 | 11.32 |
| 817 | 10 | 66.41 | CEO/CFO — hold ret_high_2d_open | CEO/CFO | high | 2 | open | 4 | 100.0 | 7.64 | 7.32 | 30.56 | 4.59 | 1.66 | 2.52 | 13.41 |
| 818 | 11 | 66.41 | Officer/President — hold ret_high_2d_open | Officer/President | high | 2 | open | 4 | 100.0 | 7.64 | 7.32 | 30.56 | 4.59 | 1.66 | 2.52 | 13.41 |
| 819 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_high_2d_open | Large cap (≥250M) CEO/CFO | high | 2 | open | 4 | 100.0 | 7.64 | 7.32 | 30.56 | 4.59 | 1.66 | 2.52 | 13.41 |
| 820 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_high_2d_open | Large cap (≥500M) CEO/CFO | high | 2 | open | 4 | 100.0 | 7.64 | 7.32 | 30.56 | 4.59 | 1.66 | 2.52 | 13.41 |
| 821 | 4 | 82.51 | CEO + Director (combo) — hold ret_high_1d_news | CEO + Director (combo) | high | 1 | news | 1 | 100.0 | 7.62 | 7.62 | 7.62 | nan | nan | 7.62 | 7.62 |
| 822 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_high_1d_news | Small cap (≤1B) CEO/CFO | high | 1 | news | 1 | 100.0 | 7.62 | 7.62 | 7.62 | nan | nan | 7.62 | 7.62 |
| 823 | 4 | 82.51 | CEO + Director (combo) — hold ret_high_2d_news | CEO + Director (combo) | high | 2 | news | 1 | 100.0 | 7.62 | 7.62 | 7.62 | nan | nan | 7.62 | 7.62 |
| 824 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_high_2d_news | Small cap (≤1B) CEO/CFO | high | 2 | news | 1 | 100.0 | 7.62 | 7.62 | 7.62 | nan | nan | 7.62 | 7.62 |
| 825 | 31 | 47.75 | Value ≥50k — hold ret_high_5d_open | Value ≥50k | high | 5 | open | 9 | 100.0 | 7.54 | 6.22 | 67.9 | 6.37 | 1.18 | 0.48 | 21.91 |
| 826 | 22 | 53.36 | RSI overbought (>70) — hold ret_high_30d_news | RSI overbought (>70) | high | 30 | news | 2 | 100.0 | 7.54 | 7.54 | 15.09 | 0.59 | 12.86 | 7.13 | 7.96 |
| 827 | 39 | 34.48 | Position +20% — hold ret_high_7d_open | Position +20% | high | 7 | open | 4 | 100.0 | 7.5 | 7.58 | 30.02 | 3.2 | 2.35 | 3.55 | 11.32 |
| 828 | 39 | 34.48 | Position +20% — hold ret_high_10d_open | Position +20% | high | 10 | open | 4 | 100.0 | 7.5 | 7.58 | 30.02 | 3.2 | 2.35 | 3.55 | 11.32 |
| 829 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_mean_14d_news | CEO only + Value ≥100k | mean | 14 | news | 2 | 100.0 | 7.5 | 7.5 | 14.99 | 9.89 | 0.76 | 0.5 | 14.49 |
| 830 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_mean_14d_news | Price > MA50 + CEO/CFO | mean | 14 | news | 2 | 100.0 | 7.5 | 7.5 | 14.99 | 9.89 | 0.76 | 0.5 | 14.49 |
| 831 | 6 | 77.62 | CEO only — hold ret_mean_14d_news | CEO only | mean | 14 | news | 3 | 100.0 | 7.46 | 7.39 | 22.38 | 7.0 | 1.07 | 0.5 | 14.49 |
| 832 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_mean_2d_news | CEO only + Value ≥500k | mean | 2 | news | 1 | 100.0 | 7.43 | 7.43 | 7.43 | nan | nan | 7.43 | 7.43 |
| 833 | 1 | 100.0 | CEO only + Position +10% — hold ret_mean_2d_news | CEO only + Position +10% | mean | 2 | news | 1 | 100.0 | 7.43 | 7.43 | 7.43 | nan | nan | 7.43 | 7.43 |
| 834 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_mean_2d_news | Near 52w high + CEO/CFO | mean | 2 | news | 1 | 100.0 | 7.43 | 7.43 | 7.43 | nan | nan | 7.43 | 7.43 |
| 835 | 36 | 36.54 | Director only (no C-level) — hold ret_high_14d_news | Director only (no C-level) | high | 14 | news | 6 | 100.0 | 7.42 | 6.29 | 44.54 | 3.9 | 1.9 | 3.32 | 12.15 |
| 836 | 28 | 48.48 | Tutti — hold ret_high_5d_open | Tutti | high | 5 | open | 10 | 100.0 | 7.41 | 6.2 | 74.07 | 6.02 | 1.23 | 0.48 | 21.91 |
| 837 | 15 | 62.43 | Price > MA50 — hold ret_high_2d_news | Price > MA50 | high | 2 | news | 5 | 100.0 | 7.4 | 6.17 | 37.01 | 5.05 | 1.47 | 1.27 | 15.02 |
| 838 | 37 | 35.58 | Director only + Value ≥100k — hold ret_high_14d_open | Director only + Value ≥100k | high | 14 | open | 3 | 100.0 | 7.4 | 7.07 | 22.21 | 3.76 | 1.97 | 3.82 | 11.32 |
| 839 | 4 | 82.51 | CEO + Director (combo) — hold ret_mean_14d_news | CEO + Director (combo) | mean | 14 | news | 1 | 100.0 | 7.39 | 7.39 | 7.39 | nan | nan | 7.39 | 7.39 |
| 840 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_mean_14d_news | Small cap (≤1B) CEO/CFO | mean | 14 | news | 1 | 100.0 | 7.39 | 7.39 | 7.39 | nan | nan | 7.39 | 7.39 |
| 841 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_high_2d_news | Mid cap (1B–10B) CEO/CFO | high | 2 | news | 2 | 50.0 | 7.38 | 7.38 | 14.76 | 10.8 | 0.68 | -0.26 | 15.02 |
| 842 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_high_2d_open | CEO/CFO + Value ≥100k | high | 2 | open | 3 | 100.0 | 7.3 | 5.98 | 21.91 | 5.56 | 1.31 | 2.52 | 13.41 |
| 843 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_high_2d_open | Large cap (≥750M) CEO/CFO | high | 2 | open | 3 | 100.0 | 7.3 | 5.98 | 21.91 | 5.56 | 1.31 | 2.52 | 13.41 |
| 844 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_high_2d_open | Large cap (≥1B) CEO/CFO | high | 2 | open | 3 | 100.0 | 7.3 | 5.98 | 21.91 | 5.56 | 1.31 | 2.52 | 13.41 |
| 845 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_mean_7d_open | Mid cap (1B–10B) CEO/CFO | mean | 7 | open | 2 | 100.0 | 7.24 | 7.24 | 14.48 | 7.28 | 0.99 | 2.09 | 12.39 |
| 846 | 33 | 41.81 | Director — hold ret_high_10d_open | Director | high | 10 | open | 8 | 100.0 | 7.24 | 6.62 | 57.95 | 4.31 | 1.68 | 2.03 | 15.19 |
| 847 | 30 | 48.32 | Value ≥100k — hold ret_high_3d_open | Value ≥100k | high | 3 | open | 6 | 100.0 | 7.19 | 5.62 | 43.12 | 5.86 | 1.23 | 0.48 | 16.69 |
| 848 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_high_3d_news | Far 52w high + Value ≥100k | high | 3 | news | 3 | 100.0 | 7.18 | 8.8 | 21.54 | 5.95 | 1.21 | 0.59 | 12.15 |
| 849 | 6 | 77.62 | CEO only — hold ret_mean_30d_news | CEO only | mean | 30 | news | 3 | 66.7 | 7.18 | 9.36 | 21.54 | 7.71 | 0.93 | -1.39 | 13.57 |
| 850 | 32 | 44.63 | Position +10% — hold ret_high_3d_news | Position +10% | high | 3 | news | 6 | 100.0 | 7.17 | 5.34 | 43.04 | 6.87 | 1.04 | 0.59 | 18.36 |
| 851 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_high_1d_open | CEO only + Value ≥100k | high | 1 | open | 2 | 100.0 | 7.16 | 7.16 | 14.32 | 1.87 | 3.84 | 5.84 | 8.48 |
| 852 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_high_1d_open | Price > MA50 + CEO/CFO | high | 1 | open | 2 | 100.0 | 7.16 | 7.16 | 14.32 | 1.87 | 3.84 | 5.84 | 8.48 |
| 853 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_mean_10d_news | Mid cap (1B–10B) CEO/CFO | mean | 10 | news | 2 | 50.0 | 7.16 | 7.16 | 14.32 | 10.63 | 0.67 | -0.36 | 14.68 |
| 854 | 14 | 65.45 | Price > MA200 — hold ret_high_3d_open | Price > MA200 | high | 3 | open | 4 | 100.0 | 7.15 | 5.71 | 28.6 | 6.83 | 1.05 | 0.48 | 16.69 |
| 855 | 39 | 34.48 | Position +20% — hold ret_high_7d_news | Position +20% | high | 7 | news | 4 | 100.0 | 7.14 | 6.55 | 28.58 | 3.84 | 1.86 | 3.32 | 12.15 |
| 856 | 39 | 34.48 | Position +20% — hold ret_high_10d_news | Position +20% | high | 10 | news | 4 | 100.0 | 7.14 | 6.55 | 28.58 | 3.84 | 1.86 | 3.32 | 12.15 |
| 857 | 37 | 35.58 | Director only + Value ≥100k — hold ret_high_7d_news | Director only + Value ≥100k | high | 7 | news | 3 | 100.0 | 7.13 | 7.96 | 21.38 | 5.49 | 1.3 | 1.27 | 12.15 |
| 858 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_mean_10d_open | CEO only + Value ≥100k | mean | 10 | open | 2 | 100.0 | 7.13 | 7.13 | 14.26 | 8.4 | 0.85 | 1.19 | 13.07 |
| 859 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_mean_10d_open | Price > MA50 + CEO/CFO | mean | 10 | open | 2 | 100.0 | 7.13 | 7.13 | 14.26 | 8.4 | 0.85 | 1.19 | 13.07 |
| 860 | 30 | 48.32 | Value ≥100k — hold ret_high_2d_news | Value ≥100k | high | 2 | news | 6 | 83.3 | 7.12 | 7.28 | 42.73 | 6.02 | 1.18 | -0.26 | 15.02 |
| 861 | 32 | 44.63 | Position +10% — hold ret_high_3d_open | Position +10% | high | 3 | open | 6 | 100.0 | 7.11 | 4.9 | 42.69 | 5.74 | 1.24 | 1.49 | 16.69 |
| 862 | 6 | 77.62 | CEO only — hold ret_mean_10d_open | CEO only | mean | 10 | open | 3 | 100.0 | 7.08 | 6.98 | 21.24 | 5.94 | 1.19 | 1.19 | 13.07 |
| 863 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_mean_3d_news | CEO only + Value ≥100k | mean | 3 | news | 2 | 100.0 | 7.06 | 7.05 | 14.11 | 3.42 | 2.07 | 4.64 | 9.47 |
| 864 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_mean_3d_news | Price > MA50 + CEO/CFO | mean | 3 | news | 2 | 100.0 | 7.06 | 7.05 | 14.11 | 3.42 | 2.07 | 4.64 | 9.47 |
| 865 | 14 | 65.45 | Price > MA200 — hold ret_high_2d_news | Price > MA200 | high | 2 | news | 4 | 100.0 | 7.05 | 5.96 | 28.21 | 5.76 | 1.23 | 1.27 | 15.02 |
| 866 | 35 | 40.48 | Value ≥500k — hold ret_high_2d_news | Value ≥500k | high | 2 | news | 4 | 75.0 | 7.04 | 6.71 | 28.18 | 7.67 | 0.92 | -0.26 | 15.02 |
| 867 | 36 | 36.54 | Director only (no C-level) — hold ret_high_14d_open | Director only (no C-level) | high | 14 | open | 6 | 100.0 | 7.04 | 5.8 | 42.24 | 3.77 | 1.87 | 3.55 | 11.94 |
| 868 | 33 | 41.81 | Director — hold ret_high_10d_news | Director | high | 10 | news | 8 | 100.0 | 7.03 | 5.66 | 56.22 | 4.12 | 1.7 | 2.83 | 14.1 |
| 869 | 38 | 34.53 | Price < MA50 — hold ret_high_7d_news | Price < MA50 | high | 7 | news | 5 | 100.0 | 7.01 | 5.15 | 35.06 | 3.81 | 1.84 | 3.32 | 12.15 |
| 870 | 40 | 33.74 | Director only + Position +10% — hold ret_high_7d_news | Director only + Position +10% | high | 7 | news | 4 | 100.0 | 6.99 | 6.25 | 27.97 | 3.96 | 1.77 | 3.32 | 12.15 |
| 871 | 40 | 33.74 | Director only + Position +10% — hold ret_high_10d_news | Director only + Position +10% | high | 10 | news | 4 | 100.0 | 6.99 | 6.25 | 27.97 | 3.96 | 1.77 | 3.32 | 12.15 |
| 872 | 40 | 33.74 | Director only + Position +10% — hold ret_high_14d_news | Director only + Position +10% | high | 14 | news | 4 | 100.0 | 6.99 | 6.25 | 27.97 | 3.96 | 1.77 | 3.32 | 12.15 |
| 873 | 40 | 33.74 | Director only + Position +10% — hold ret_high_30d_news | Director only + Position +10% | high | 30 | news | 4 | 100.0 | 6.99 | 6.25 | 27.97 | 3.96 | 1.77 | 3.32 | 12.15 |
| 874 | 4 | 82.51 | CEO + Director (combo) — hold ret_mean_10d_open | CEO + Director (combo) | mean | 10 | open | 1 | 100.0 | 6.98 | 6.98 | 6.98 | nan | nan | 6.98 | 6.98 |
| 875 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_mean_10d_open | Small cap (≤1B) CEO/CFO | mean | 10 | open | 1 | 100.0 | 6.98 | 6.98 | 6.98 | nan | nan | 6.98 | 6.98 |
| 876 | 35 | 40.48 | Value ≥500k — hold ret_high_2d_open | Value ≥500k | high | 2 | open | 4 | 100.0 | 6.93 | 6.92 | 27.73 | 6.39 | 1.09 | 0.48 | 13.41 |
| 877 | 21 | 53.67 | Qty ≥5k shares — hold ret_high_2d_news | Qty ≥5k shares | high | 2 | news | 6 | 83.3 | 6.92 | 6.69 | 41.55 | 5.97 | 1.16 | -0.26 | 15.02 |
| 878 | 20 | 53.67 | Qty ≥10k shares — hold ret_high_2d_news | Qty ≥10k shares | high | 2 | news | 6 | 83.3 | 6.92 | 6.69 | 41.55 | 5.97 | 1.16 | -0.26 | 15.02 |
| 879 | 15 | 62.43 | Price > MA50 — hold ret_high_3d_open | Price > MA50 | high | 3 | open | 5 | 100.0 | 6.92 | 5.98 | 34.58 | 5.94 | 1.16 | 0.48 | 16.69 |
| 880 | 37 | 35.58 | Director only + Value ≥100k — hold ret_high_5d_news | Director only + Value ≥100k | high | 5 | news | 3 | 100.0 | 6.92 | 7.34 | 20.76 | 5.45 | 1.27 | 1.27 | 12.15 |
| 881 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_high_2d_news | Far 52w high + Value ≥100k | high | 2 | news | 3 | 66.7 | 6.9 | 8.8 | 20.69 | 6.42 | 1.07 | -0.26 | 12.15 |
| 882 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_high_3d_open | Far 52w high + Value ≥100k | high | 3 | open | 3 | 100.0 | 6.9 | 5.98 | 20.69 | 4.04 | 1.71 | 3.39 | 11.32 |
| 883 | 6 | 77.62 | CEO only — hold ret_mean_5d_news | CEO only | mean | 5 | news | 3 | 100.0 | 6.9 | 4.95 | 20.7 | 4.93 | 1.4 | 3.24 | 12.51 |
| 884 | 6 | 77.62 | CEO only — hold ret_mean_7d_open | CEO only | mean | 7 | open | 3 | 100.0 | 6.89 | 5.14 | 20.68 | 4.86 | 1.42 | 3.15 | 12.39 |
| 885 | 21 | 53.67 | Qty ≥5k shares — hold ret_high_2d_open | Qty ≥5k shares | high | 2 | open | 6 | 100.0 | 6.88 | 6.76 | 41.25 | 5.09 | 1.35 | 0.48 | 13.41 |
| 886 | 20 | 53.67 | Qty ≥10k shares — hold ret_high_2d_open | Qty ≥10k shares | high | 2 | open | 6 | 100.0 | 6.88 | 6.76 | 41.25 | 5.09 | 1.35 | 0.48 | 13.41 |
| 887 | 51 | 20.1 | Position +30% — hold ret_high_7d_news | Position +30% | high | 7 | news | 3 | 100.0 | 6.87 | 5.15 | 20.62 | 4.66 | 1.47 | 3.32 | 12.15 |
| 888 | 51 | 20.1 | Position +30% — hold ret_high_10d_news | Position +30% | high | 10 | news | 3 | 100.0 | 6.87 | 5.15 | 20.62 | 4.66 | 1.47 | 3.32 | 12.15 |
| 889 | 31 | 47.75 | Value ≥50k — hold ret_high_3d_news | Value ≥50k | high | 3 | news | 9 | 100.0 | 6.83 | 6.14 | 61.49 | 5.85 | 1.17 | 0.59 | 18.36 |
| 890 | 37 | 35.58 | Director only + Value ≥100k — hold ret_high_10d_open | Director only + Value ≥100k | high | 10 | open | 3 | 100.0 | 6.81 | 7.07 | 20.42 | 4.65 | 1.46 | 2.03 | 11.32 |
| 891 | 28 | 48.48 | Tutti — hold ret_high_3d_news | Tutti | high | 3 | news | 10 | 100.0 | 6.77 | 6.15 | 67.66 | 5.52 | 1.23 | 0.59 | 18.36 |
| 892 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_high_5d_open | Multiple buys (n≥2) | high | 5 | open | 3 | 100.0 | 6.73 | 6.22 | 20.18 | 2.48 | 2.71 | 4.54 | 9.42 |
| 893 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_mean_90d_open | Multiple buys (n≥2) | mean | 90 | open | 3 | 66.7 | 6.72 | 0.6 | 20.17 | 12.34 | 0.54 | -1.36 | 20.93 |
| 894 | 22 | 53.36 | RSI overbought (>70) — hold ret_high_30d_open | RSI overbought (>70) | high | 30 | open | 2 | 100.0 | 6.68 | 6.69 | 13.37 | 0.54 | 12.28 | 6.3 | 7.07 |
| 895 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_mean_7d_news | Mid cap (1B–10B) CEO/CFO | mean | 7 | news | 2 | 50.0 | 6.66 | 6.66 | 13.31 | 10.37 | 0.64 | -0.68 | 13.99 |
| 896 | 40 | 33.74 | Director only + Position +10% — hold ret_high_7d_open | Director only + Position +10% | high | 7 | open | 4 | 100.0 | 6.62 | 5.8 | 26.48 | 3.47 | 1.91 | 3.55 | 11.32 |
| 897 | 40 | 33.74 | Director only + Position +10% — hold ret_high_10d_open | Director only + Position +10% | high | 10 | open | 4 | 100.0 | 6.62 | 5.8 | 26.48 | 3.47 | 1.91 | 3.55 | 11.32 |
| 898 | 40 | 33.74 | Director only + Position +10% — hold ret_high_14d_open | Director only + Position +10% | high | 14 | open | 4 | 100.0 | 6.62 | 5.8 | 26.48 | 3.47 | 1.91 | 3.55 | 11.32 |
| 899 | 40 | 33.74 | Director only + Position +10% — hold ret_high_30d_open | Director only + Position +10% | high | 30 | open | 4 | 100.0 | 6.62 | 5.8 | 26.48 | 3.47 | 1.91 | 3.55 | 11.32 |
| 900 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_high_2d_open | Far 52w high + Value ≥100k | high | 2 | open | 3 | 100.0 | 6.61 | 5.98 | 19.82 | 4.43 | 1.49 | 2.52 | 11.32 |
| 901 | 38 | 34.53 | Price < MA50 — hold ret_high_5d_open | Price < MA50 | high | 5 | open | 5 | 100.0 | 6.6 | 6.22 | 32.99 | 3.9 | 1.69 | 1.49 | 11.32 |
| 902 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_high_3d_news | Mid cap (1B–10B) Value ≥100k | high | 3 | news | 4 | 100.0 | 6.59 | 3.71 | 26.36 | 8.23 | 0.8 | 0.59 | 18.36 |
| 903 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_mean_5d_open | CEO only + Value ≥100k | mean | 5 | open | 2 | 100.0 | 6.58 | 6.58 | 13.16 | 6.15 | 1.07 | 2.23 | 10.93 |
| 904 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_mean_5d_open | Price > MA50 + CEO/CFO | mean | 5 | open | 2 | 100.0 | 6.58 | 6.58 | 13.16 | 6.15 | 1.07 | 2.23 | 10.93 |
| 905 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_mean_60d_open | Multiple buys (n≥2) | mean | 60 | open | 3 | 66.7 | 6.58 | 3.7 | 19.75 | 9.37 | 0.7 | -1.01 | 17.06 |
| 906 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_high_7d_news | Multiple buys (n≥2) | high | 7 | news | 3 | 100.0 | 6.53 | 5.15 | 19.59 | 2.93 | 2.23 | 4.54 | 9.9 |
| 907 | 37 | 35.58 | Director only + Value ≥100k — hold ret_high_3d_news | Director only + Value ≥100k | high | 3 | news | 3 | 100.0 | 6.52 | 6.14 | 19.56 | 5.45 | 1.2 | 1.27 | 12.15 |
| 908 | 33 | 41.81 | Director — hold ret_high_7d_open | Director | high | 7 | open | 8 | 100.0 | 6.52 | 6.62 | 52.17 | 3.68 | 1.77 | 0.48 | 11.32 |
| 909 | 31 | 47.75 | Value ≥50k — hold ret_high_3d_open | Value ≥50k | high | 3 | open | 9 | 100.0 | 6.51 | 5.26 | 58.57 | 5.15 | 1.26 | 0.48 | 16.69 |
| 910 | 28 | 48.48 | Tutti — hold ret_high_3d_open | Tutti | high | 3 | open | 10 | 100.0 | 6.47 | 5.62 | 64.74 | 4.86 | 1.33 | 0.48 | 16.69 |
| 911 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_high_3d_open | Mid cap (1B–10B) Value ≥100k | high | 3 | open | 4 | 100.0 | 6.46 | 4.33 | 25.82 | 7.1 | 0.91 | 0.48 | 16.69 |
| 912 | 30 | 48.32 | Value ≥100k — hold ret_high_2d_open | Value ≥100k | high | 2 | open | 6 | 100.0 | 6.43 | 5.43 | 38.58 | 5.02 | 1.28 | 0.48 | 13.41 |
| 913 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_mean_7d_news | CEO/CFO + Value ≥100k | mean | 7 | news | 3 | 66.7 | 6.4 | 5.89 | 19.2 | 7.35 | 0.87 | -0.68 | 13.99 |
| 914 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_mean_7d_news | Large cap (≥750M) CEO/CFO | mean | 7 | news | 3 | 66.7 | 6.4 | 5.89 | 19.2 | 7.35 | 0.87 | -0.68 | 13.99 |
| 915 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_mean_7d_news | Large cap (≥1B) CEO/CFO | mean | 7 | news | 3 | 66.7 | 6.4 | 5.89 | 19.2 | 7.35 | 0.87 | -0.68 | 13.99 |
| 916 | 6 | 77.62 | CEO only — hold ret_mean_14d_open | CEO only | mean | 14 | open | 3 | 66.7 | 6.4 | 8.42 | 19.21 | 7.7 | 0.83 | -2.1 | 12.89 |
| 917 | 37 | 35.58 | Director only + Value ≥100k — hold ret_high_2d_news | Director only + Value ≥100k | high | 2 | news | 3 | 100.0 | 6.39 | 5.75 | 19.17 | 5.47 | 1.17 | 1.27 | 12.15 |
| 918 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_mean_2d_news | CEO only + Value ≥100k | mean | 2 | news | 2 | 100.0 | 6.39 | 6.39 | 12.78 | 1.47 | 4.34 | 5.35 | 7.43 |
| 919 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_mean_2d_news | Price > MA50 + CEO/CFO | mean | 2 | news | 2 | 100.0 | 6.39 | 6.39 | 12.78 | 1.47 | 4.34 | 5.35 | 7.43 |
| 920 | 26 | 50.0 | Qty ≥50k shares — hold ret_mean_2d_news | Qty ≥50k shares | mean | 2 | news | 2 | 100.0 | 6.38 | 6.38 | 12.76 | 1.48 | 4.3 | 5.33 | 7.43 |
| 921 | 27 | 50.0 | Value ≥1M — hold ret_mean_2d_news | Value ≥1M | mean | 2 | news | 2 | 100.0 | 6.38 | 6.38 | 12.76 | 1.48 | 4.3 | 5.33 | 7.43 |
| 922 | 39 | 34.48 | Position +20% — hold ret_high_5d_open | Position +20% | high | 5 | open | 4 | 100.0 | 6.37 | 6.33 | 25.48 | 4.01 | 1.59 | 1.49 | 11.32 |
| 923 | 51 | 20.1 | Position +30% — hold ret_high_5d_open | Position +30% | high | 5 | open | 3 | 100.0 | 6.34 | 6.22 | 19.03 | 4.92 | 1.29 | 1.49 | 11.32 |
| 924 | 40 | 33.74 | Director only + Position +10% — hold ret_high_5d_news | Director only + Position +10% | high | 5 | news | 4 | 100.0 | 6.32 | 5.94 | 25.29 | 4.61 | 1.37 | 1.26 | 12.15 |
| 925 | 33 | 41.81 | Director — hold ret_high_7d_news | Director | high | 7 | news | 8 | 100.0 | 6.31 | 5.66 | 50.46 | 3.56 | 1.77 | 1.27 | 12.15 |
| 926 | 22 | 53.36 | RSI overbought (>70) — hold ret_high_14d_news | RSI overbought (>70) | high | 14 | news | 2 | 100.0 | 6.3 | 6.29 | 12.59 | 2.35 | 2.67 | 4.63 | 7.96 |
| 927 | 37 | 35.58 | Director only + Value ≥100k — hold ret_high_7d_open | Director only + Value ≥100k | high | 7 | open | 3 | 100.0 | 6.29 | 7.07 | 18.87 | 5.46 | 1.15 | 0.48 | 11.32 |
| 928 | 32 | 44.63 | Position +10% — hold ret_high_2d_news | Position +10% | high | 2 | news | 6 | 83.3 | 6.23 | 4.69 | 37.37 | 6.13 | 1.02 | -0.26 | 15.02 |
| 929 | 14 | 65.45 | Price > MA200 — hold ret_high_2d_open | Price > MA200 | high | 2 | open | 4 | 100.0 | 6.23 | 5.52 | 24.93 | 5.37 | 1.16 | 0.48 | 13.41 |
| 930 | 26 | 50.0 | Qty ≥50k shares — hold ret_mean_3d_news | Qty ≥50k shares | mean | 3 | news | 2 | 100.0 | 6.22 | 6.23 | 12.45 | 4.59 | 1.36 | 2.98 | 9.47 |
| 931 | 27 | 50.0 | Value ≥1M — hold ret_mean_3d_news | Value ≥1M | mean | 3 | news | 2 | 100.0 | 6.22 | 6.23 | 12.45 | 4.59 | 1.36 | 2.98 | 9.47 |
| 932 | 49 | 32.78 | CFO only — hold ret_high_5d_open | CFO only | high | 5 | open | 1 | 100.0 | 6.22 | 6.22 | 6.22 | nan | nan | 6.22 | 6.22 |
| 933 | 48 | 32.78 | CFO + Director (combo) — hold ret_high_5d_open | CFO + Director (combo) | high | 5 | open | 1 | 100.0 | 6.22 | 6.22 | 6.22 | nan | nan | 6.22 | 6.22 |
| 934 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_high_5d_open | CFO only + Value ≥50k | high | 5 | open | 1 | 100.0 | 6.22 | 6.22 | 6.22 | nan | nan | 6.22 | 6.22 |
| 935 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_high_5d_open | CFO only + Value ≥100k | high | 5 | open | 1 | 100.0 | 6.22 | 6.22 | 6.22 | nan | nan | 6.22 | 6.22 |
| 936 | 47 | 32.78 | CFO only + Position +10% — hold ret_high_5d_open | CFO only + Position +10% | high | 5 | open | 1 | 100.0 | 6.22 | 6.22 | 6.22 | nan | nan | 6.22 | 6.22 |
| 937 | 46 | 32.78 | CFO only + Position +20% — hold ret_high_5d_open | CFO only + Position +20% | high | 5 | open | 1 | 100.0 | 6.22 | 6.22 | 6.22 | nan | nan | 6.22 | 6.22 |
| 938 | 44 | 32.78 | RSI oversold (<30) — hold ret_high_5d_open | RSI oversold (<30) | high | 5 | open | 1 | 100.0 | 6.22 | 6.22 | 6.22 | nan | nan | 6.22 | 6.22 |
| 939 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_high_5d_open | RSI oversold + CEO/CFO | high | 5 | open | 1 | 100.0 | 6.22 | 6.22 | 6.22 | nan | nan | 6.22 | 6.22 |
| 940 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_high_5d_open | RSI oversold + Value ≥100k | high | 5 | open | 1 | 100.0 | 6.22 | 6.22 | 6.22 | nan | nan | 6.22 | 6.22 |
| 941 | 32 | 44.63 | Position +10% — hold ret_high_2d_open | Position +10% | high | 2 | open | 6 | 100.0 | 6.18 | 4.25 | 37.05 | 4.98 | 1.24 | 1.3 | 13.41 |
| 942 | 15 | 62.43 | Price > MA50 — hold ret_high_2d_open | Price > MA50 | high | 2 | open | 5 | 100.0 | 6.18 | 5.98 | 30.91 | 4.65 | 1.33 | 0.48 | 13.41 |
| 943 | 36 | 36.54 | Director only (no C-level) — hold ret_high_10d_news | Director only (no C-level) | high | 10 | news | 6 | 100.0 | 6.16 | 5.36 | 36.97 | 3.49 | 1.77 | 2.83 | 12.15 |
| 944 | 6 | 77.62 | CEO only — hold ret_mean_30d_open | CEO only | mean | 30 | open | 3 | 66.7 | 6.15 | 10.42 | 18.44 | 8.78 | 0.7 | -3.95 | 11.97 |
| 945 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_high_5d_open | Large cap (≥2B) CEO/CFO | high | 5 | open | 2 | 100.0 | 6.14 | 6.14 | 12.29 | 0.11 | 57.94 | 6.07 | 6.22 |
| 946 | 28 | 48.48 | Tutti — hold ret_high_2d_news | Tutti | high | 2 | news | 10 | 90.0 | 6.12 | 5.96 | 61.23 | 4.96 | 1.24 | -0.26 | 15.02 |
| 947 | 31 | 47.75 | Value ≥50k — hold ret_high_2d_news | Value ≥50k | high | 2 | news | 9 | 88.9 | 6.12 | 5.75 | 55.06 | 5.26 | 1.16 | -0.26 | 15.02 |
| 948 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_high_5d_news | Large cap (≥2B) CEO/CFO | high | 5 | news | 2 | 100.0 | 6.12 | 6.12 | 12.23 | 3.92 | 1.56 | 3.34 | 8.89 |
| 949 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_high_1d_news | Far 52w high + Value ≥100k | high | 1 | news | 3 | 66.7 | 6.11 | 8.66 | 18.33 | 7.64 | 0.8 | -2.48 | 12.15 |
| 950 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_mean_30d_news | CEO only + Value ≥100k | mean | 30 | news | 2 | 50.0 | 6.09 | 6.09 | 12.18 | 10.58 | 0.58 | -1.39 | 13.57 |
| 951 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_mean_30d_news | Price > MA50 + CEO/CFO | mean | 30 | news | 2 | 50.0 | 6.09 | 6.09 | 12.18 | 10.58 | 0.58 | -1.39 | 13.57 |
| 952 | 37 | 35.58 | Director only + Value ≥100k — hold ret_high_5d_open | Director only + Value ≥100k | high | 5 | open | 3 | 100.0 | 6.08 | 6.45 | 18.25 | 5.43 | 1.12 | 0.48 | 11.32 |
| 953 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_high_5d_open | Large cap (≥3B) CEO/CFO | high | 5 | open | 1 | 100.0 | 6.07 | 6.07 | 6.07 | nan | nan | 6.07 | 6.07 |
| 954 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_high_5d_open | Large cap (≥5B) CEO/CFO | high | 5 | open | 1 | 100.0 | 6.07 | 6.07 | 6.07 | nan | nan | 6.07 | 6.07 |
| 955 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_high_5d_open | Large cap (≥10B) CEO/CFO | high | 5 | open | 1 | 100.0 | 6.07 | 6.07 | 6.07 | nan | nan | 6.07 | 6.07 |
| 956 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_mean_10d_news | CEO/CFO + Value ≥100k | mean | 10 | news | 3 | 66.7 | 6.07 | 3.88 | 18.2 | 7.75 | 0.78 | -0.36 | 14.68 |
| 957 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_mean_10d_news | Large cap (≥750M) CEO/CFO | mean | 10 | news | 3 | 66.7 | 6.07 | 3.88 | 18.2 | 7.75 | 0.78 | -0.36 | 14.68 |
| 958 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_mean_10d_news | Large cap (≥1B) CEO/CFO | mean | 10 | news | 3 | 66.7 | 6.07 | 3.88 | 18.2 | 7.75 | 0.78 | -0.36 | 14.68 |
| 959 | 10 | 66.41 | CEO/CFO — hold ret_mean_10d_news | CEO/CFO | mean | 10 | news | 4 | 75.0 | 6.04 | 4.92 | 24.16 | 6.33 | 0.95 | -0.36 | 14.68 |
| 960 | 11 | 66.41 | Officer/President — hold ret_mean_10d_news | Officer/President | mean | 10 | news | 4 | 75.0 | 6.04 | 4.92 | 24.16 | 6.33 | 0.95 | -0.36 | 14.68 |
| 961 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_mean_10d_news | Large cap (≥250M) CEO/CFO | mean | 10 | news | 4 | 75.0 | 6.04 | 4.92 | 24.16 | 6.33 | 0.95 | -0.36 | 14.68 |
| 962 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_mean_10d_news | Large cap (≥500M) CEO/CFO | mean | 10 | news | 4 | 75.0 | 6.04 | 4.92 | 24.16 | 6.33 | 0.95 | -0.36 | 14.68 |
| 963 | 38 | 34.53 | Price < MA50 — hold ret_high_3d_open | Price < MA50 | high | 3 | open | 5 | 100.0 | 6.03 | 4.54 | 30.16 | 4.16 | 1.45 | 1.49 | 11.32 |
| 964 | 40 | 33.74 | Director only + Position +10% — hold ret_high_3d_news | Director only + Position +10% | high | 3 | news | 4 | 100.0 | 6.02 | 5.34 | 24.09 | 4.56 | 1.32 | 1.26 | 12.15 |
| 965 | 39 | 34.48 | Position +20% — hold ret_high_5d_news | Position +20% | high | 5 | news | 4 | 100.0 | 6.02 | 5.34 | 24.09 | 4.8 | 1.25 | 1.26 | 12.15 |
| 966 | 10 | 66.41 | CEO/CFO — hold ret_mean_30d_news | CEO/CFO | mean | 30 | news | 4 | 75.0 | 6.0 | 5.9 | 23.99 | 6.73 | 0.89 | -1.39 | 13.57 |
| 967 | 11 | 66.41 | Officer/President — hold ret_mean_30d_news | Officer/President | mean | 30 | news | 4 | 75.0 | 6.0 | 5.9 | 23.99 | 6.73 | 0.89 | -1.39 | 13.57 |
| 968 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_mean_30d_news | Large cap (≥250M) CEO/CFO | mean | 30 | news | 4 | 75.0 | 6.0 | 5.9 | 23.99 | 6.73 | 0.89 | -1.39 | 13.57 |
| 969 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_mean_30d_news | Large cap (≥500M) CEO/CFO | mean | 30 | news | 4 | 75.0 | 6.0 | 5.9 | 23.99 | 6.73 | 0.89 | -1.39 | 13.57 |
| 970 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_high_2d_open | Large cap (≥3B) CEO/CFO | high | 2 | open | 1 | 100.0 | 5.98 | 5.98 | 5.98 | nan | nan | 5.98 | 5.98 |
| 971 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_high_2d_open | Large cap (≥5B) CEO/CFO | high | 2 | open | 1 | 100.0 | 5.98 | 5.98 | 5.98 | nan | nan | 5.98 | 5.98 |
| 972 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_high_2d_open | Large cap (≥10B) CEO/CFO | high | 2 | open | 1 | 100.0 | 5.98 | 5.98 | 5.98 | nan | nan | 5.98 | 5.98 |
| 973 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_high_3d_open | Large cap (≥3B) CEO/CFO | high | 3 | open | 1 | 100.0 | 5.98 | 5.98 | 5.98 | nan | nan | 5.98 | 5.98 |
| 974 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_high_3d_open | Large cap (≥5B) CEO/CFO | high | 3 | open | 1 | 100.0 | 5.98 | 5.98 | 5.98 | nan | nan | 5.98 | 5.98 |
| 975 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_high_3d_open | Large cap (≥10B) CEO/CFO | high | 3 | open | 1 | 100.0 | 5.98 | 5.98 | 5.98 | nan | nan | 5.98 | 5.98 |
| 976 | 10 | 66.41 | CEO/CFO — hold ret_high_1d_news | CEO/CFO | high | 1 | news | 4 | 75.0 | 5.96 | 8.14 | 23.82 | 5.71 | 1.04 | -2.48 | 10.02 |
| 977 | 11 | 66.41 | Officer/President — hold ret_high_1d_news | Officer/President | high | 1 | news | 4 | 75.0 | 5.96 | 8.14 | 23.82 | 5.71 | 1.04 | -2.48 | 10.02 |
| 978 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_high_1d_news | Large cap (≥250M) CEO/CFO | high | 1 | news | 4 | 75.0 | 5.96 | 8.14 | 23.82 | 5.71 | 1.04 | -2.48 | 10.02 |
| 979 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_high_1d_news | Large cap (≥500M) CEO/CFO | high | 1 | news | 4 | 75.0 | 5.96 | 8.14 | 23.82 | 5.71 | 1.04 | -2.48 | 10.02 |
| 980 | 4 | 82.51 | CEO + Director (combo) — hold ret_mean_10d_news | CEO + Director (combo) | mean | 10 | news | 1 | 100.0 | 5.96 | 5.96 | 5.96 | nan | nan | 5.96 | 5.96 |
| 981 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_mean_10d_news | Small cap (≤1B) CEO/CFO | mean | 10 | news | 1 | 100.0 | 5.96 | 5.96 | 5.96 | nan | nan | 5.96 | 5.96 |
| 982 | 40 | 33.74 | Director only + Position +10% — hold ret_high_5d_open | Director only + Position +10% | high | 5 | open | 4 | 100.0 | 5.95 | 5.5 | 23.8 | 4.12 | 1.44 | 1.49 | 11.32 |
| 983 | 10 | 66.41 | CEO/CFO — hold ret_mean_30d_open | CEO/CFO | mean | 30 | open | 4 | 75.0 | 5.94 | 7.87 | 23.75 | 7.18 | 0.83 | -3.95 | 11.97 |
| 984 | 11 | 66.41 | Officer/President — hold ret_mean_30d_open | Officer/President | mean | 30 | open | 4 | 75.0 | 5.94 | 7.87 | 23.75 | 7.18 | 0.83 | -3.95 | 11.97 |
| 985 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_mean_30d_open | Large cap (≥250M) CEO/CFO | mean | 30 | open | 4 | 75.0 | 5.94 | 7.87 | 23.75 | 7.18 | 0.83 | -3.95 | 11.97 |
| 986 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_mean_30d_open | Large cap (≥500M) CEO/CFO | mean | 30 | open | 4 | 75.0 | 5.94 | 7.87 | 23.75 | 7.18 | 0.83 | -3.95 | 11.97 |
| 987 | 53 | 0.0 | Qty ≥100k shares — hold ret_mean_1d_news | Qty ≥100k shares | mean | 1 | news | 1 | 100.0 | 5.93 | 5.93 | 5.93 | nan | nan | 5.93 | 5.93 |
| 988 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_mean_1d_news | Small cap (≤1B) Value ≥100k | mean | 1 | news | 1 | 100.0 | 5.93 | 5.93 | 5.93 | nan | nan | 5.93 | 5.93 |
| 989 | 38 | 34.53 | Price < MA50 — hold ret_high_5d_news | Price < MA50 | high | 5 | news | 5 | 100.0 | 5.93 | 4.54 | 29.67 | 4.33 | 1.37 | 1.26 | 12.15 |
| 990 | 14 | 65.45 | Price > MA200 — hold ret_mean_30d_news | Price > MA200 | mean | 30 | news | 4 | 100.0 | 5.93 | 4.01 | 23.72 | 5.17 | 1.15 | 2.13 | 13.57 |
| 991 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_mean_2d_open | CEO only + Value ≥500k | mean | 2 | open | 1 | 100.0 | 5.92 | 5.92 | 5.92 | nan | nan | 5.92 | 5.92 |
| 992 | 1 | 100.0 | CEO only + Position +10% — hold ret_mean_2d_open | CEO only + Position +10% | mean | 2 | open | 1 | 100.0 | 5.92 | 5.92 | 5.92 | nan | nan | 5.92 | 5.92 |
| 993 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_mean_2d_open | Near 52w high + CEO/CFO | mean | 2 | open | 1 | 100.0 | 5.92 | 5.92 | 5.92 | nan | nan | 5.92 | 5.92 |
| 994 | 10 | 66.41 | CEO/CFO — hold ret_mean_10d_open | CEO/CFO | mean | 10 | open | 4 | 100.0 | 5.92 | 4.7 | 23.66 | 5.38 | 1.1 | 1.19 | 13.07 |
| 995 | 11 | 66.41 | Officer/President — hold ret_mean_10d_open | Officer/President | mean | 10 | open | 4 | 100.0 | 5.92 | 4.7 | 23.66 | 5.38 | 1.1 | 1.19 | 13.07 |
| 996 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_mean_10d_open | Large cap (≥250M) CEO/CFO | mean | 10 | open | 4 | 100.0 | 5.92 | 4.7 | 23.66 | 5.38 | 1.1 | 1.19 | 13.07 |
| 997 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_mean_10d_open | Large cap (≥500M) CEO/CFO | mean | 10 | open | 4 | 100.0 | 5.92 | 4.7 | 23.66 | 5.38 | 1.1 | 1.19 | 13.07 |
| 998 | 10 | 66.41 | CEO/CFO — hold ret_mean_14d_news | CEO/CFO | mean | 14 | news | 4 | 100.0 | 5.92 | 4.35 | 23.7 | 6.48 | 0.91 | 0.5 | 14.49 |
| 999 | 11 | 66.41 | Officer/President — hold ret_mean_14d_news | Officer/President | mean | 14 | news | 4 | 100.0 | 5.92 | 4.35 | 23.7 | 6.48 | 0.91 | 0.5 | 14.49 |
| 1000 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_mean_14d_news | Large cap (≥250M) CEO/CFO | mean | 14 | news | 4 | 100.0 | 5.92 | 4.35 | 23.7 | 6.48 | 0.91 | 0.5 | 14.49 |
| 1001 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_mean_14d_news | Large cap (≥500M) CEO/CFO | mean | 14 | news | 4 | 100.0 | 5.92 | 4.35 | 23.7 | 6.48 | 0.91 | 0.5 | 14.49 |
| 1002 | 36 | 36.54 | Director only (no C-level) — hold ret_high_7d_news | Director only (no C-level) | high | 7 | news | 6 | 100.0 | 5.9 | 5.36 | 35.41 | 3.83 | 1.54 | 1.27 | 12.15 |
| 1003 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_mean_7d_news | Large cap (≥3B) CEO/CFO | mean | 7 | news | 1 | 100.0 | 5.89 | 5.89 | 5.89 | nan | nan | 5.89 | 5.89 |
| 1004 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_mean_7d_news | Large cap (≥5B) CEO/CFO | mean | 7 | news | 1 | 100.0 | 5.89 | 5.89 | 5.89 | nan | nan | 5.89 | 5.89 |
| 1005 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_mean_7d_news | Large cap (≥10B) CEO/CFO | mean | 7 | news | 1 | 100.0 | 5.89 | 5.89 | 5.89 | nan | nan | 5.89 | 5.89 |
| 1006 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_mean_7d_open | CEO/CFO + Value ≥100k | mean | 7 | open | 3 | 100.0 | 5.88 | 3.15 | 17.63 | 5.67 | 1.04 | 2.09 | 12.39 |
| 1007 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_mean_7d_open | Large cap (≥750M) CEO/CFO | mean | 7 | open | 3 | 100.0 | 5.88 | 3.15 | 17.63 | 5.67 | 1.04 | 2.09 | 12.39 |
| 1008 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_mean_7d_open | Large cap (≥1B) CEO/CFO | mean | 7 | open | 3 | 100.0 | 5.88 | 3.15 | 17.63 | 5.67 | 1.04 | 2.09 | 12.39 |
| 1009 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_mean_5d_open | Mid cap (1B–10B) CEO/CFO | mean | 5 | open | 2 | 100.0 | 5.86 | 5.85 | 11.71 | 7.18 | 0.82 | 0.78 | 10.93 |
| 1010 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_high_1d_open | Large cap (≥3B) CEO/CFO | high | 1 | open | 1 | 100.0 | 5.84 | 5.84 | 5.84 | nan | nan | 5.84 | 5.84 |
| 1011 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_high_1d_open | Large cap (≥5B) CEO/CFO | high | 1 | open | 1 | 100.0 | 5.84 | 5.84 | 5.84 | nan | nan | 5.84 | 5.84 |
| 1012 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_high_1d_open | Large cap (≥10B) CEO/CFO | high | 1 | open | 1 | 100.0 | 5.84 | 5.84 | 5.84 | nan | nan | 5.84 | 5.84 |
| 1013 | 10 | 66.41 | CEO/CFO — hold ret_mean_7d_news | CEO/CFO | mean | 7 | news | 4 | 75.0 | 5.84 | 5.01 | 23.34 | 6.11 | 0.96 | -0.68 | 13.99 |
| 1014 | 11 | 66.41 | Officer/President — hold ret_mean_7d_news | Officer/President | mean | 7 | news | 4 | 75.0 | 5.84 | 5.01 | 23.34 | 6.11 | 0.96 | -0.68 | 13.99 |
| 1015 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_mean_7d_news | Large cap (≥250M) CEO/CFO | mean | 7 | news | 4 | 75.0 | 5.84 | 5.01 | 23.34 | 6.11 | 0.96 | -0.68 | 13.99 |
| 1016 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_mean_7d_news | Large cap (≥500M) CEO/CFO | mean | 7 | news | 4 | 75.0 | 5.84 | 5.01 | 23.34 | 6.11 | 0.96 | -0.68 | 13.99 |
| 1017 | 10 | 66.41 | CEO/CFO — hold ret_mean_14d_open | CEO/CFO | mean | 14 | open | 4 | 75.0 | 5.84 | 6.29 | 23.36 | 6.38 | 0.91 | -2.1 | 12.89 |
| 1018 | 11 | 66.41 | Officer/President — hold ret_mean_14d_open | Officer/President | mean | 14 | open | 4 | 75.0 | 5.84 | 6.29 | 23.36 | 6.38 | 0.91 | -2.1 | 12.89 |
| 1019 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_mean_14d_open | Large cap (≥250M) CEO/CFO | mean | 14 | open | 4 | 75.0 | 5.84 | 6.29 | 23.36 | 6.38 | 0.91 | -2.1 | 12.89 |
| 1020 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_mean_14d_open | Large cap (≥500M) CEO/CFO | mean | 14 | open | 4 | 75.0 | 5.84 | 6.29 | 23.36 | 6.38 | 0.91 | -2.1 | 12.89 |
| 1021 | 28 | 48.48 | Tutti — hold ret_high_2d_open | Tutti | high | 2 | open | 10 | 100.0 | 5.83 | 5.43 | 58.33 | 4.24 | 1.38 | 0.48 | 13.41 |
| 1022 | 10 | 66.41 | CEO/CFO — hold ret_high_1d_open | CEO/CFO | high | 1 | open | 4 | 100.0 | 5.81 | 7.16 | 23.22 | 3.92 | 1.48 | 0.25 | 8.65 |
| 1023 | 11 | 66.41 | Officer/President — hold ret_high_1d_open | Officer/President | high | 1 | open | 4 | 100.0 | 5.81 | 7.16 | 23.22 | 3.92 | 1.48 | 0.25 | 8.65 |
| 1024 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_high_1d_open | Large cap (≥250M) CEO/CFO | high | 1 | open | 4 | 100.0 | 5.81 | 7.16 | 23.22 | 3.92 | 1.48 | 0.25 | 8.65 |
| 1025 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_high_1d_open | Large cap (≥500M) CEO/CFO | high | 1 | open | 4 | 100.0 | 5.81 | 7.16 | 23.22 | 3.92 | 1.48 | 0.25 | 8.65 |
| 1026 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_high_1d_open | Far 52w high + Value ≥100k | high | 1 | open | 3 | 100.0 | 5.8 | 5.84 | 17.41 | 5.54 | 1.05 | 0.25 | 11.32 |
| 1027 | 31 | 47.75 | Value ≥50k — hold ret_high_2d_open | Value ≥50k | high | 2 | open | 9 | 100.0 | 5.8 | 4.87 | 52.16 | 4.49 | 1.29 | 0.48 | 13.41 |
| 1028 | 6 | 77.62 | CEO only — hold ret_mean_5d_open | CEO only | mean | 5 | open | 3 | 100.0 | 5.8 | 4.23 | 17.39 | 4.56 | 1.27 | 2.23 | 10.93 |
| 1029 | 6 | 77.62 | CEO only — hold ret_mean_3d_news | CEO only | mean | 3 | news | 3 | 100.0 | 5.79 | 4.64 | 17.38 | 3.26 | 1.78 | 3.27 | 9.47 |
| 1030 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_high_3d_open | Multiple buys (n≥2) | high | 3 | open | 3 | 100.0 | 5.78 | 4.54 | 17.35 | 3.2 | 1.81 | 3.39 | 9.42 |
| 1031 | 36 | 36.54 | Director only (no C-level) — hold ret_high_10d_open | Director only (no C-level) | high | 10 | open | 6 | 100.0 | 5.78 | 5.36 | 34.68 | 3.26 | 1.77 | 2.03 | 11.32 |
| 1032 | 33 | 41.81 | Director — hold ret_high_5d_open | Director | high | 5 | open | 8 | 100.0 | 5.76 | 6.2 | 46.09 | 3.64 | 1.58 | 0.48 | 11.32 |
| 1033 | 37 | 35.58 | Director only + Value ≥100k — hold ret_high_3d_open | Director only + Value ≥100k | high | 3 | open | 3 | 100.0 | 5.69 | 5.26 | 17.06 | 5.43 | 1.05 | 0.48 | 11.32 |
| 1034 | 10 | 66.41 | CEO/CFO — hold ret_mean_7d_open | CEO/CFO | mean | 7 | open | 4 | 100.0 | 5.69 | 4.14 | 22.77 | 4.64 | 1.23 | 2.09 | 12.39 |
| 1035 | 11 | 66.41 | Officer/President — hold ret_mean_7d_open | Officer/President | mean | 7 | open | 4 | 100.0 | 5.69 | 4.14 | 22.77 | 4.64 | 1.23 | 2.09 | 12.39 |
| 1036 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_mean_7d_open | Large cap (≥250M) CEO/CFO | mean | 7 | open | 4 | 100.0 | 5.69 | 4.14 | 22.77 | 4.64 | 1.23 | 2.09 | 12.39 |
| 1037 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_mean_7d_open | Large cap (≥500M) CEO/CFO | mean | 7 | open | 4 | 100.0 | 5.69 | 4.14 | 22.77 | 4.64 | 1.23 | 2.09 | 12.39 |
| 1038 | 40 | 33.74 | Director only + Position +10% — hold ret_high_2d_news | Director only + Position +10% | high | 2 | news | 4 | 100.0 | 5.65 | 4.69 | 22.61 | 4.73 | 1.19 | 1.08 | 12.15 |
| 1039 | 40 | 33.74 | Director only + Position +10% — hold ret_high_3d_open | Director only + Position +10% | high | 3 | open | 4 | 100.0 | 5.65 | 4.9 | 22.61 | 4.12 | 1.37 | 1.49 | 11.32 |
| 1040 | 51 | 20.1 | Position +30% — hold ret_high_5d_news | Position +30% | high | 5 | news | 3 | 100.0 | 5.58 | 3.34 | 16.75 | 5.78 | 0.97 | 1.26 | 12.15 |
| 1041 | 26 | 50.0 | Qty ≥50k shares — hold ret_mean_5d_news | Qty ≥50k shares | mean | 5 | news | 2 | 50.0 | 5.58 | 5.58 | 11.16 | 9.8 | 0.57 | -1.35 | 12.51 |
| 1042 | 27 | 50.0 | Value ≥1M — hold ret_mean_5d_news | Value ≥1M | mean | 5 | news | 2 | 50.0 | 5.58 | 5.58 | 11.16 | 9.8 | 0.57 | -1.35 | 12.51 |
| 1043 | 37 | 35.58 | Director only + Value ≥100k — hold ret_high_2d_open | Director only + Value ≥100k | high | 2 | open | 3 | 100.0 | 5.56 | 4.87 | 16.67 | 5.45 | 1.02 | 0.48 | 11.32 |
| 1044 | 33 | 41.81 | Director — hold ret_high_5d_news | Director | high | 5 | news | 8 | 100.0 | 5.56 | 5.36 | 44.45 | 3.74 | 1.49 | 1.26 | 12.15 |
| 1045 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_mean_10d_open | CEO/CFO + Value ≥100k | mean | 10 | open | 3 | 100.0 | 5.56 | 2.42 | 16.68 | 6.53 | 0.85 | 1.19 | 13.07 |
| 1046 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_mean_10d_open | Large cap (≥750M) CEO/CFO | mean | 10 | open | 3 | 100.0 | 5.56 | 2.42 | 16.68 | 6.53 | 0.85 | 1.19 | 13.07 |
| 1047 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_mean_10d_open | Large cap (≥1B) CEO/CFO | mean | 10 | open | 3 | 100.0 | 5.56 | 2.42 | 16.68 | 6.53 | 0.85 | 1.19 | 13.07 |
| 1048 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_mean_30d_news | Mid cap (1B–10B) Value ≥100k | mean | 30 | news | 4 | 100.0 | 5.53 | 3.21 | 22.11 | 5.42 | 1.02 | 2.13 | 13.57 |
| 1049 | 36 | 36.54 | Director only (no C-level) — hold ret_high_7d_open | Director only (no C-level) | high | 7 | open | 6 | 100.0 | 5.52 | 5.36 | 33.13 | 3.65 | 1.51 | 0.48 | 11.32 |
| 1050 | 26 | 50.0 | Qty ≥50k shares — hold ret_mean_1d_news | Qty ≥50k shares | mean | 1 | news | 2 | 100.0 | 5.49 | 5.49 | 10.98 | 0.62 | 8.82 | 5.05 | 5.93 |
| 1051 | 27 | 50.0 | Value ≥1M — hold ret_mean_1d_news | Value ≥1M | mean | 1 | news | 2 | 100.0 | 5.49 | 5.49 | 10.98 | 0.62 | 8.82 | 5.05 | 5.93 |
| 1052 | 38 | 34.53 | Price < MA50 — hold ret_high_2d_open | Price < MA50 | high | 2 | open | 5 | 100.0 | 5.48 | 3.63 | 27.42 | 4.3 | 1.28 | 1.3 | 11.32 |
| 1053 | 6 | 77.62 | CEO only — hold ret_mean_60d_news | CEO only | mean | 60 | news | 3 | 66.7 | 5.48 | 4.46 | 16.44 | 10.0 | 0.55 | -3.97 | 15.95 |
| 1054 | 36 | 36.54 | Director only (no C-level) — hold ret_high_5d_news | Director only (no C-level) | high | 5 | news | 6 | 100.0 | 5.45 | 5.36 | 32.73 | 4.12 | 1.32 | 1.26 | 12.15 |
| 1055 | 37 | 35.58 | Director only + Value ≥100k — hold ret_high_1d_news | Director only + Value ≥100k | high | 1 | news | 3 | 100.0 | 5.44 | 2.89 | 16.31 | 5.87 | 0.93 | 1.27 | 12.15 |
| 1056 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_high_2d_news | Mid cap (1B–10B) Value ≥100k | high | 2 | news | 4 | 75.0 | 5.44 | 3.51 | 21.78 | 6.87 | 0.79 | -0.26 | 15.02 |
| 1057 | 22 | 53.36 | RSI overbought (>70) — hold ret_high_14d_open | RSI overbought (>70) | high | 14 | open | 2 | 100.0 | 5.44 | 5.45 | 10.89 | 2.3 | 2.37 | 3.82 | 7.07 |
| 1058 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_mean_14d_news | CEO/CFO + Value ≥100k | mean | 14 | news | 3 | 100.0 | 5.44 | 1.32 | 16.31 | 7.85 | 0.69 | 0.5 | 14.49 |
| 1059 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_mean_14d_news | Large cap (≥750M) CEO/CFO | mean | 14 | news | 3 | 100.0 | 5.44 | 1.32 | 16.31 | 7.85 | 0.69 | 0.5 | 14.49 |
| 1060 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_mean_14d_news | Large cap (≥1B) CEO/CFO | mean | 14 | news | 3 | 100.0 | 5.44 | 1.32 | 16.31 | 7.85 | 0.69 | 0.5 | 14.49 |
| 1061 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_mean_90d_news | Multiple buys (n≥2) | mean | 90 | news | 3 | 33.3 | 5.43 | -1.36 | 16.29 | 12.43 | 0.44 | -2.13 | 19.78 |
| 1062 | 30 | 48.32 | Value ≥100k — hold ret_high_1d_news | Value ≥100k | high | 1 | news | 6 | 83.3 | 5.42 | 5.78 | 32.51 | 5.71 | 0.95 | -2.48 | 12.15 |
| 1063 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_high_5d_news | Multiple buys (n≥2) | high | 5 | news | 3 | 100.0 | 5.42 | 4.54 | 16.26 | 2.63 | 2.06 | 3.34 | 8.38 |
| 1064 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_mean_30d_open | Mid cap (1B–10B) Value ≥100k | mean | 30 | open | 4 | 100.0 | 5.42 | 4.2 | 21.7 | 4.66 | 1.16 | 1.33 | 11.97 |
| 1065 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_high_1d_news | CEO/CFO + Value ≥100k | high | 1 | news | 3 | 66.7 | 5.4 | 8.66 | 16.2 | 6.86 | 0.79 | -2.48 | 10.02 |
| 1066 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_high_1d_news | Large cap (≥750M) CEO/CFO | high | 1 | news | 3 | 66.7 | 5.4 | 8.66 | 16.2 | 6.86 | 0.79 | -2.48 | 10.02 |
| 1067 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_high_1d_news | Large cap (≥1B) CEO/CFO | high | 1 | news | 3 | 66.7 | 5.4 | 8.66 | 16.2 | 6.86 | 0.79 | -2.48 | 10.02 |
| 1068 | 51 | 20.1 | Position +30% — hold ret_high_3d_open | Position +30% | high | 3 | open | 3 | 100.0 | 5.4 | 3.39 | 16.2 | 5.21 | 1.04 | 1.49 | 11.32 |
| 1069 | 22 | 53.36 | RSI overbought (>70) — hold ret_high_10d_news | RSI overbought (>70) | high | 10 | news | 2 | 100.0 | 5.4 | 5.39 | 10.79 | 3.63 | 1.49 | 2.83 | 7.96 |
| 1070 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_mean_14d_open | CEO only + Value ≥100k | mean | 14 | open | 2 | 50.0 | 5.4 | 5.4 | 10.79 | 10.6 | 0.51 | -2.1 | 12.89 |
| 1071 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_mean_14d_open | Price > MA50 + CEO/CFO | mean | 14 | open | 2 | 50.0 | 5.4 | 5.4 | 10.79 | 10.6 | 0.51 | -2.1 | 12.89 |
| 1072 | 38 | 34.53 | Price < MA50 — hold ret_high_3d_news | Price < MA50 | high | 3 | news | 5 | 100.0 | 5.38 | 4.54 | 26.92 | 4.89 | 1.1 | 0.59 | 12.15 |
| 1073 | 39 | 34.48 | Position +20% — hold ret_high_3d_open | Position +20% | high | 3 | open | 4 | 100.0 | 5.36 | 4.33 | 21.46 | 4.26 | 1.26 | 1.49 | 11.32 |
| 1074 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_mean_2d_news | Large cap (≥3B) CEO/CFO | mean | 2 | news | 1 | 100.0 | 5.35 | 5.35 | 5.35 | nan | nan | 5.35 | 5.35 |
| 1075 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_mean_2d_news | Large cap (≥5B) CEO/CFO | mean | 2 | news | 1 | 100.0 | 5.35 | 5.35 | 5.35 | nan | nan | 5.35 | 5.35 |
| 1076 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_mean_2d_news | Large cap (≥10B) CEO/CFO | mean | 2 | news | 1 | 100.0 | 5.35 | 5.35 | 5.35 | nan | nan | 5.35 | 5.35 |
| 1077 | 53 | 0.0 | Qty ≥100k shares — hold ret_mean_2d_news | Qty ≥100k shares | mean | 2 | news | 1 | 100.0 | 5.33 | 5.33 | 5.33 | nan | nan | 5.33 | 5.33 |
| 1078 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_mean_2d_news | Small cap (≤1B) Value ≥100k | mean | 2 | news | 1 | 100.0 | 5.33 | 5.33 | 5.33 | nan | nan | 5.33 | 5.33 |
| 1079 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_high_2d_open | Mid cap (1B–10B) Value ≥100k | high | 2 | open | 4 | 100.0 | 5.32 | 3.7 | 21.28 | 5.68 | 0.94 | 0.48 | 13.41 |
| 1080 | 49 | 32.78 | CFO only — hold ret_mean_30d_open | CFO only | mean | 30 | open | 1 | 100.0 | 5.31 | 5.31 | 5.31 | nan | nan | 5.31 | 5.31 |
| 1081 | 48 | 32.78 | CFO + Director (combo) — hold ret_mean_30d_open | CFO + Director (combo) | mean | 30 | open | 1 | 100.0 | 5.31 | 5.31 | 5.31 | nan | nan | 5.31 | 5.31 |
| 1082 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_mean_30d_open | CFO only + Value ≥50k | mean | 30 | open | 1 | 100.0 | 5.31 | 5.31 | 5.31 | nan | nan | 5.31 | 5.31 |
| 1083 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_mean_30d_open | CFO only + Value ≥100k | mean | 30 | open | 1 | 100.0 | 5.31 | 5.31 | 5.31 | nan | nan | 5.31 | 5.31 |
| 1084 | 47 | 32.78 | CFO only + Position +10% — hold ret_mean_30d_open | CFO only + Position +10% | mean | 30 | open | 1 | 100.0 | 5.31 | 5.31 | 5.31 | nan | nan | 5.31 | 5.31 |
| 1085 | 46 | 32.78 | CFO only + Position +20% — hold ret_mean_30d_open | CFO only + Position +20% | mean | 30 | open | 1 | 100.0 | 5.31 | 5.31 | 5.31 | nan | nan | 5.31 | 5.31 |
| 1086 | 44 | 32.78 | RSI oversold (<30) — hold ret_mean_30d_open | RSI oversold (<30) | mean | 30 | open | 1 | 100.0 | 5.31 | 5.31 | 5.31 | nan | nan | 5.31 | 5.31 |
| 1087 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_mean_30d_open | RSI oversold + CEO/CFO | mean | 30 | open | 1 | 100.0 | 5.31 | 5.31 | 5.31 | nan | nan | 5.31 | 5.31 |
| 1088 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_mean_30d_open | RSI oversold + Value ≥100k | mean | 30 | open | 1 | 100.0 | 5.31 | 5.31 | 5.31 | nan | nan | 5.31 | 5.31 |
| 1089 | 6 | 77.62 | CEO only — hold ret_mean_2d_news | CEO only | mean | 2 | news | 3 | 100.0 | 5.3 | 5.35 | 15.91 | 2.15 | 2.47 | 3.13 | 7.43 |
| 1090 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_mean_1d_news | Large cap (≥3B) CEO/CFO | mean | 1 | news | 1 | 100.0 | 5.28 | 5.28 | 5.28 | nan | nan | 5.28 | 5.28 |
| 1091 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_mean_1d_news | Large cap (≥5B) CEO/CFO | mean | 1 | news | 1 | 100.0 | 5.28 | 5.28 | 5.28 | nan | nan | 5.28 | 5.28 |
| 1092 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_mean_1d_news | Large cap (≥10B) CEO/CFO | mean | 1 | news | 1 | 100.0 | 5.28 | 5.28 | 5.28 | nan | nan | 5.28 | 5.28 |
| 1093 | 40 | 33.74 | Director only + Position +10% — hold ret_high_2d_open | Director only + Position +10% | high | 2 | open | 4 | 100.0 | 5.28 | 4.25 | 21.12 | 4.29 | 1.23 | 1.3 | 11.32 |
| 1094 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_mean_5d_news | Mid cap (1B–10B) CEO/CFO | mean | 5 | news | 2 | 50.0 | 5.28 | 5.28 | 10.55 | 10.23 | 0.52 | -1.96 | 12.51 |
| 1095 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_mean_60d_news | Multiple buys (n≥2) | mean | 60 | news | 3 | 66.7 | 5.28 | 0.89 | 15.83 | 9.29 | 0.57 | -1.01 | 15.95 |
| 1096 | 33 | 41.81 | Director — hold ret_high_3d_open | Director | high | 3 | open | 8 | 100.0 | 5.26 | 4.9 | 42.07 | 3.7 | 1.42 | 0.48 | 11.32 |
| 1097 | 36 | 36.54 | Director only (no C-level) — hold ret_high_3d_news | Director only (no C-level) | high | 3 | news | 6 | 100.0 | 5.26 | 5.34 | 31.53 | 4.04 | 1.3 | 1.26 | 12.15 |
| 1098 | 21 | 53.67 | Qty ≥5k shares — hold ret_high_1d_news | Qty ≥5k shares | high | 1 | news | 6 | 83.3 | 5.24 | 5.25 | 31.47 | 5.61 | 0.94 | -2.48 | 12.15 |
| 1099 | 20 | 53.67 | Qty ≥10k shares — hold ret_high_1d_news | Qty ≥10k shares | high | 1 | news | 6 | 83.3 | 5.24 | 5.25 | 31.47 | 5.61 | 0.94 | -2.48 | 12.15 |
| 1100 | 35 | 40.48 | Value ≥500k — hold ret_high_1d_news | Value ≥500k | high | 1 | news | 4 | 75.0 | 5.24 | 5.64 | 20.96 | 6.98 | 0.75 | -2.48 | 12.15 |
| 1101 | 26 | 50.0 | Qty ≥50k shares — hold ret_mean_2d_open | Qty ≥50k shares | mean | 2 | open | 2 | 100.0 | 5.24 | 5.24 | 10.48 | 0.96 | 5.45 | 4.56 | 5.92 |
| 1102 | 27 | 50.0 | Value ≥1M — hold ret_mean_2d_open | Value ≥1M | mean | 2 | open | 2 | 100.0 | 5.24 | 5.24 | 10.48 | 0.96 | 5.45 | 4.56 | 5.92 |
| 1103 | 21 | 53.67 | Qty ≥5k shares — hold ret_high_1d_open | Qty ≥5k shares | high | 1 | open | 6 | 100.0 | 5.2 | 5.26 | 31.22 | 4.83 | 1.08 | 0.25 | 11.32 |
| 1104 | 20 | 53.67 | Qty ≥10k shares — hold ret_high_1d_open | Qty ≥10k shares | high | 1 | open | 6 | 100.0 | 5.2 | 5.26 | 31.22 | 4.83 | 1.08 | 0.25 | 11.32 |
| 1105 | 14 | 65.45 | Price > MA200 — hold ret_mean_14d_news | Price > MA200 | mean | 14 | news | 4 | 100.0 | 5.2 | 2.85 | 20.81 | 6.35 | 0.82 | 0.62 | 14.49 |
| 1106 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_mean_5d_news | CEO/CFO + Value ≥100k | mean | 5 | news | 3 | 66.7 | 5.17 | 4.95 | 15.5 | 7.24 | 0.71 | -1.96 | 12.51 |
| 1107 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_mean_5d_news | Large cap (≥750M) CEO/CFO | mean | 5 | news | 3 | 66.7 | 5.17 | 4.95 | 15.5 | 7.24 | 0.71 | -1.96 | 12.51 |
| 1108 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_mean_5d_news | Large cap (≥1B) CEO/CFO | mean | 5 | news | 3 | 66.7 | 5.17 | 4.95 | 15.5 | 7.24 | 0.71 | -1.96 | 12.51 |
| 1109 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_mean_1d_news | CEO only + Value ≥100k | mean | 1 | news | 2 | 100.0 | 5.16 | 5.17 | 10.33 | 0.16 | 31.76 | 5.05 | 5.28 |
| 1110 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_mean_1d_news | Price > MA50 + CEO/CFO | mean | 1 | news | 2 | 100.0 | 5.16 | 5.17 | 10.33 | 0.16 | 31.76 | 5.05 | 5.28 |
| 1111 | 53 | 0.0 | Qty ≥100k shares — hold ret_mean_1d_open | Qty ≥100k shares | mean | 1 | open | 1 | 100.0 | 5.15 | 5.15 | 5.15 | nan | nan | 5.15 | 5.15 |
| 1112 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_mean_1d_open | Small cap (≤1B) Value ≥100k | mean | 1 | open | 1 | 100.0 | 5.15 | 5.15 | 5.15 | nan | nan | 5.15 | 5.15 |
| 1113 | 49 | 32.78 | CFO only — hold ret_high_7d_news | CFO only | high | 7 | news | 1 | 100.0 | 5.15 | 5.15 | 5.15 | nan | nan | 5.15 | 5.15 |
| 1114 | 48 | 32.78 | CFO + Director (combo) — hold ret_high_7d_news | CFO + Director (combo) | high | 7 | news | 1 | 100.0 | 5.15 | 5.15 | 5.15 | nan | nan | 5.15 | 5.15 |
| 1115 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_high_7d_news | CFO only + Value ≥50k | high | 7 | news | 1 | 100.0 | 5.15 | 5.15 | 5.15 | nan | nan | 5.15 | 5.15 |
| 1116 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_high_7d_news | CFO only + Value ≥100k | high | 7 | news | 1 | 100.0 | 5.15 | 5.15 | 5.15 | nan | nan | 5.15 | 5.15 |
| 1117 | 47 | 32.78 | CFO only + Position +10% — hold ret_high_7d_news | CFO only + Position +10% | high | 7 | news | 1 | 100.0 | 5.15 | 5.15 | 5.15 | nan | nan | 5.15 | 5.15 |
| 1118 | 46 | 32.78 | CFO only + Position +20% — hold ret_high_7d_news | CFO only + Position +20% | high | 7 | news | 1 | 100.0 | 5.15 | 5.15 | 5.15 | nan | nan | 5.15 | 5.15 |
| 1119 | 44 | 32.78 | RSI oversold (<30) — hold ret_high_7d_news | RSI oversold (<30) | high | 7 | news | 1 | 100.0 | 5.15 | 5.15 | 5.15 | nan | nan | 5.15 | 5.15 |
| 1120 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_high_7d_news | RSI oversold + CEO/CFO | high | 7 | news | 1 | 100.0 | 5.15 | 5.15 | 5.15 | nan | nan | 5.15 | 5.15 |
| 1121 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_high_7d_news | RSI oversold + Value ≥100k | high | 7 | news | 1 | 100.0 | 5.15 | 5.15 | 5.15 | nan | nan | 5.15 | 5.15 |
| 1122 | 49 | 32.78 | CFO only — hold ret_high_10d_news | CFO only | high | 10 | news | 1 | 100.0 | 5.15 | 5.15 | 5.15 | nan | nan | 5.15 | 5.15 |
| 1123 | 48 | 32.78 | CFO + Director (combo) — hold ret_high_10d_news | CFO + Director (combo) | high | 10 | news | 1 | 100.0 | 5.15 | 5.15 | 5.15 | nan | nan | 5.15 | 5.15 |
| 1124 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_high_10d_news | CFO only + Value ≥50k | high | 10 | news | 1 | 100.0 | 5.15 | 5.15 | 5.15 | nan | nan | 5.15 | 5.15 |
| 1125 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_high_10d_news | CFO only + Value ≥100k | high | 10 | news | 1 | 100.0 | 5.15 | 5.15 | 5.15 | nan | nan | 5.15 | 5.15 |
| 1126 | 47 | 32.78 | CFO only + Position +10% — hold ret_high_10d_news | CFO only + Position +10% | high | 10 | news | 1 | 100.0 | 5.15 | 5.15 | 5.15 | nan | nan | 5.15 | 5.15 |
| 1127 | 46 | 32.78 | CFO only + Position +20% — hold ret_high_10d_news | CFO only + Position +20% | high | 10 | news | 1 | 100.0 | 5.15 | 5.15 | 5.15 | nan | nan | 5.15 | 5.15 |
| 1128 | 44 | 32.78 | RSI oversold (<30) — hold ret_high_10d_news | RSI oversold (<30) | high | 10 | news | 1 | 100.0 | 5.15 | 5.15 | 5.15 | nan | nan | 5.15 | 5.15 |
| 1129 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_high_10d_news | RSI oversold + CEO/CFO | high | 10 | news | 1 | 100.0 | 5.15 | 5.15 | 5.15 | nan | nan | 5.15 | 5.15 |
| 1130 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_high_10d_news | RSI oversold + Value ≥100k | high | 10 | news | 1 | 100.0 | 5.15 | 5.15 | 5.15 | nan | nan | 5.15 | 5.15 |
| 1131 | 15 | 62.43 | Price > MA50 — hold ret_high_1d_news | Price > MA50 | high | 1 | news | 5 | 100.0 | 5.14 | 2.89 | 25.69 | 3.92 | 1.31 | 1.27 | 10.02 |
| 1132 | 4 | 82.51 | CEO + Director (combo) — hold ret_mean_7d_open | CEO + Director (combo) | mean | 7 | open | 1 | 100.0 | 5.14 | 5.14 | 5.14 | nan | nan | 5.14 | 5.14 |
| 1133 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_mean_7d_open | Small cap (≤1B) CEO/CFO | mean | 7 | open | 1 | 100.0 | 5.14 | 5.14 | 5.14 | nan | nan | 5.14 | 5.14 |
| 1134 | 35 | 40.48 | Value ≥500k — hold ret_high_1d_open | Value ≥500k | high | 1 | open | 4 | 100.0 | 5.13 | 4.48 | 20.53 | 5.63 | 0.91 | 0.25 | 11.32 |
| 1135 | 6 | 77.62 | CEO only — hold ret_mean_90d_news | CEO only | mean | 90 | news | 3 | 33.3 | 5.12 | -1.27 | 15.36 | 12.73 | 0.4 | -3.15 | 19.78 |
| 1136 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_mean_14d_news | Mid cap (1B–10B) Value ≥100k | mean | 14 | news | 4 | 100.0 | 5.11 | 2.67 | 20.44 | 6.42 | 0.8 | 0.62 | 14.49 |
| 1137 | 14 | 65.45 | Price > MA200 — hold ret_mean_30d_open | Price > MA200 | mean | 30 | open | 4 | 100.0 | 5.11 | 3.57 | 20.45 | 4.71 | 1.09 | 1.33 | 11.97 |
| 1138 | 26 | 50.0 | Qty ≥50k shares — hold ret_mean_3d_open | Qty ≥50k shares | mean | 3 | open | 2 | 100.0 | 5.08 | 5.08 | 10.15 | 4.04 | 1.26 | 2.22 | 7.93 |
| 1139 | 27 | 50.0 | Value ≥1M — hold ret_mean_3d_open | Value ≥1M | mean | 3 | open | 2 | 100.0 | 5.08 | 5.08 | 10.15 | 4.04 | 1.26 | 2.22 | 7.93 |
| 1140 | 36 | 36.54 | Director only (no C-level) — hold ret_high_5d_open | Director only (no C-level) | high | 5 | open | 6 | 100.0 | 5.08 | 5.36 | 30.45 | 3.91 | 1.3 | 0.48 | 11.32 |
| 1141 | 33 | 41.81 | Director — hold ret_high_3d_news | Director | high | 3 | news | 8 | 100.0 | 5.06 | 5.34 | 40.5 | 4.01 | 1.26 | 0.59 | 12.15 |
| 1142 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_mean_1d_news | CEO only + Value ≥500k | mean | 1 | news | 1 | 100.0 | 5.05 | 5.05 | 5.05 | nan | nan | 5.05 | 5.05 |
| 1143 | 1 | 100.0 | CEO only + Position +10% — hold ret_mean_1d_news | CEO only + Position +10% | mean | 1 | news | 1 | 100.0 | 5.05 | 5.05 | 5.05 | nan | nan | 5.05 | 5.05 |
| 1144 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_mean_1d_news | Near 52w high + CEO/CFO | mean | 1 | news | 1 | 100.0 | 5.05 | 5.05 | 5.05 | nan | nan | 5.05 | 5.05 |
| 1145 | 51 | 20.1 | Position +30% — hold ret_high_2d_open | Position +30% | high | 2 | open | 3 | 100.0 | 5.05 | 2.52 | 15.14 | 5.47 | 0.92 | 1.3 | 11.32 |
| 1146 | 39 | 34.48 | Position +20% — hold ret_high_3d_news | Position +20% | high | 3 | news | 4 | 100.0 | 5.04 | 3.7 | 20.14 | 5.35 | 0.94 | 0.59 | 12.15 |
| 1147 | 38 | 34.53 | Price < MA50 — hold ret_high_1d_open | Price < MA50 | high | 1 | open | 5 | 100.0 | 5.03 | 3.63 | 25.15 | 4.78 | 1.05 | 0.25 | 11.32 |
| 1148 | 36 | 36.54 | Director only (no C-level) — hold ret_high_2d_news | Director only (no C-level) | high | 2 | news | 6 | 100.0 | 5.01 | 4.69 | 30.05 | 4.1 | 1.22 | 1.08 | 12.15 |
| 1149 | 39 | 34.48 | Position +20% — hold ret_high_2d_open | Position +20% | high | 2 | open | 4 | 100.0 | 5.0 | 3.7 | 20.01 | 4.46 | 1.12 | 1.3 | 11.32 |
| 1150 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_mean_14d_open | Mid cap (1B–10B) Value ≥100k | mean | 14 | open | 4 | 75.0 | 5.0 | 3.65 | 20.02 | 5.57 | 0.9 | -0.16 | 12.89 |
| 1151 | 31 | 47.75 | Value ≥50k — hold ret_high_1d_news | Value ≥50k | high | 1 | news | 9 | 88.9 | 4.98 | 3.63 | 44.84 | 4.85 | 1.03 | -2.48 | 12.15 |
| 1152 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_mean_14d_open | CEO/CFO + Value ≥100k | mean | 14 | open | 3 | 66.7 | 4.98 | 4.15 | 14.94 | 7.53 | 0.66 | -2.1 | 12.89 |
| 1153 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_mean_14d_open | Large cap (≥750M) CEO/CFO | mean | 14 | open | 3 | 66.7 | 4.98 | 4.15 | 14.94 | 7.53 | 0.66 | -2.1 | 12.89 |
| 1154 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_mean_14d_open | Large cap (≥1B) CEO/CFO | mean | 14 | open | 3 | 66.7 | 4.98 | 4.15 | 14.94 | 7.53 | 0.66 | -2.1 | 12.89 |
| 1155 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_mean_5d_news | Large cap (≥3B) CEO/CFO | mean | 5 | news | 1 | 100.0 | 4.95 | 4.95 | 4.95 | nan | nan | 4.95 | 4.95 |
| 1156 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_mean_5d_news | Large cap (≥5B) CEO/CFO | mean | 5 | news | 1 | 100.0 | 4.95 | 4.95 | 4.95 | nan | nan | 4.95 | 4.95 |
| 1157 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_mean_5d_news | Large cap (≥10B) CEO/CFO | mean | 5 | news | 1 | 100.0 | 4.95 | 4.95 | 4.95 | nan | nan | 4.95 | 4.95 |
| 1158 | 40 | 33.74 | Director only + Position +10% — hold ret_high_1d_news | Director only + Position +10% | high | 1 | news | 4 | 100.0 | 4.94 | 3.26 | 19.75 | 4.93 | 1.0 | 1.08 | 12.15 |
| 1159 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_high_2d_open | Multiple buys (n≥2) | high | 2 | open | 3 | 100.0 | 4.93 | 3.63 | 14.8 | 3.27 | 1.51 | 2.52 | 8.65 |
| 1160 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_mean_3d_open | CEO only + Value ≥100k | mean | 3 | open | 2 | 100.0 | 4.93 | 4.93 | 9.86 | 4.24 | 1.16 | 1.93 | 7.93 |
| 1161 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_mean_3d_open | Price > MA50 + CEO/CFO | mean | 3 | open | 2 | 100.0 | 4.93 | 4.93 | 9.86 | 4.24 | 1.16 | 1.93 | 7.93 |
| 1162 | 36 | 36.54 | Director only (no C-level) — hold ret_high_3d_open | Director only (no C-level) | high | 3 | open | 6 | 100.0 | 4.88 | 4.9 | 29.26 | 3.85 | 1.27 | 0.48 | 11.32 |
| 1163 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_mean_30d_news | CEO/CFO + Value ≥100k | mean | 30 | news | 3 | 66.7 | 4.88 | 2.45 | 14.63 | 7.77 | 0.63 | -1.39 | 13.57 |
| 1164 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_mean_30d_news | Large cap (≥750M) CEO/CFO | mean | 30 | news | 3 | 66.7 | 4.88 | 2.45 | 14.63 | 7.77 | 0.63 | -1.39 | 13.57 |
| 1165 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_mean_30d_news | Large cap (≥1B) CEO/CFO | mean | 30 | news | 3 | 66.7 | 4.88 | 2.45 | 14.63 | 7.77 | 0.63 | -1.39 | 13.57 |
| 1166 | 33 | 41.81 | Director — hold ret_high_2d_open | Director | high | 2 | open | 8 | 100.0 | 4.87 | 4.25 | 38.94 | 3.72 | 1.31 | 0.48 | 11.32 |
| 1167 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_high_1d_open | CEO/CFO + Value ≥100k | high | 1 | open | 3 | 100.0 | 4.86 | 5.84 | 14.57 | 4.2 | 1.16 | 0.25 | 8.48 |
| 1168 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_high_1d_open | Large cap (≥750M) CEO/CFO | high | 1 | open | 3 | 100.0 | 4.86 | 5.84 | 14.57 | 4.2 | 1.16 | 0.25 | 8.48 |
| 1169 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_high_1d_open | Large cap (≥1B) CEO/CFO | high | 1 | open | 3 | 100.0 | 4.86 | 5.84 | 14.57 | 4.2 | 1.16 | 0.25 | 8.48 |
| 1170 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_mean_30d_open | Multiple buys (n≥2) | mean | 30 | open | 3 | 66.7 | 4.85 | 5.31 | 14.56 | 5.81 | 0.84 | -1.17 | 10.42 |
| 1171 | 38 | 34.53 | Price < MA50 — hold ret_high_2d_news | Price < MA50 | high | 2 | news | 5 | 80.0 | 4.84 | 3.63 | 24.22 | 5.07 | 0.96 | -0.26 | 12.15 |
| 1172 | 28 | 48.48 | Tutti — hold ret_high_1d_news | Tutti | high | 1 | news | 10 | 90.0 | 4.77 | 3.26 | 47.69 | 4.62 | 1.03 | -2.48 | 12.15 |
| 1173 | 30 | 48.32 | Value ≥100k — hold ret_high_1d_open | Value ≥100k | high | 1 | open | 6 | 100.0 | 4.74 | 3.94 | 28.41 | 4.56 | 1.04 | 0.25 | 11.32 |
| 1174 | 6 | 77.62 | CEO only — hold ret_mean_3d_open | CEO only | mean | 3 | open | 3 | 100.0 | 4.71 | 4.27 | 14.13 | 3.02 | 1.56 | 1.93 | 7.93 |
| 1175 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_high_3d_news | Large cap (≥2B) CEO/CFO | high | 3 | news | 2 | 100.0 | 4.7 | 4.7 | 9.39 | 5.81 | 0.81 | 0.59 | 8.8 |
| 1176 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_high_3d_open | Large cap (≥2B) CEO/CFO | high | 3 | open | 2 | 100.0 | 4.69 | 4.69 | 9.37 | 1.83 | 2.56 | 3.39 | 5.98 |
| 1177 | 10 | 66.41 | CEO/CFO — hold ret_mean_5d_news | CEO/CFO | mean | 5 | news | 4 | 75.0 | 4.69 | 4.1 | 18.74 | 5.99 | 0.78 | -1.96 | 12.51 |
| 1178 | 11 | 66.41 | Officer/President — hold ret_mean_5d_news | Officer/President | mean | 5 | news | 4 | 75.0 | 4.69 | 4.1 | 18.74 | 5.99 | 0.78 | -1.96 | 12.51 |
| 1179 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_mean_5d_news | Large cap (≥250M) CEO/CFO | mean | 5 | news | 4 | 75.0 | 4.69 | 4.1 | 18.74 | 5.99 | 0.78 | -1.96 | 12.51 |
| 1180 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_mean_5d_news | Large cap (≥500M) CEO/CFO | mean | 5 | news | 4 | 75.0 | 4.69 | 4.1 | 18.74 | 5.99 | 0.78 | -1.96 | 12.51 |
| 1181 | 33 | 41.81 | Director — hold ret_high_2d_news | Director | high | 2 | news | 8 | 87.5 | 4.68 | 4.69 | 37.41 | 4.1 | 1.14 | -0.26 | 12.15 |
| 1182 | 39 | 34.48 | Position +20% — hold ret_high_2d_news | Position +20% | high | 2 | news | 4 | 75.0 | 4.68 | 3.42 | 18.72 | 5.61 | 0.83 | -0.26 | 12.15 |
| 1183 | 31 | 47.75 | Value ≥50k — hold ret_high_1d_open | Value ≥50k | high | 1 | open | 9 | 100.0 | 4.67 | 3.63 | 41.99 | 4.07 | 1.15 | 0.25 | 11.32 |
| 1184 | 51 | 20.1 | Position +30% — hold ret_high_3d_news | Position +30% | high | 3 | news | 3 | 100.0 | 4.67 | 1.26 | 14.0 | 6.49 | 0.72 | 0.59 | 12.15 |
| 1185 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_mean_10d_news | Mid cap (1B–10B) Value ≥100k | mean | 10 | news | 4 | 50.0 | 4.66 | 2.16 | 18.65 | 7.05 | 0.66 | -0.36 | 14.68 |
| 1186 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_mean_5d_open | CEO/CFO + Value ≥100k | mean | 5 | open | 3 | 100.0 | 4.65 | 2.23 | 13.94 | 5.49 | 0.85 | 0.78 | 10.93 |
| 1187 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_mean_5d_open | Large cap (≥750M) CEO/CFO | mean | 5 | open | 3 | 100.0 | 4.65 | 2.23 | 13.94 | 5.49 | 0.85 | 0.78 | 10.93 |
| 1188 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_mean_5d_open | Large cap (≥1B) CEO/CFO | mean | 5 | open | 3 | 100.0 | 4.65 | 2.23 | 13.94 | 5.49 | 0.85 | 0.78 | 10.93 |
| 1189 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_mean_3d_news | Large cap (≥3B) CEO/CFO | mean | 3 | news | 1 | 100.0 | 4.64 | 4.64 | 4.64 | nan | nan | 4.64 | 4.64 |
| 1190 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_mean_3d_news | Large cap (≥5B) CEO/CFO | mean | 3 | news | 1 | 100.0 | 4.64 | 4.64 | 4.64 | nan | nan | 4.64 | 4.64 |
| 1191 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_mean_3d_news | Large cap (≥10B) CEO/CFO | mean | 3 | news | 1 | 100.0 | 4.64 | 4.64 | 4.64 | nan | nan | 4.64 | 4.64 |
| 1192 | 36 | 36.54 | Director only (no C-level) — hold ret_high_2d_open | Director only (no C-level) | high | 2 | open | 6 | 100.0 | 4.63 | 4.25 | 27.77 | 3.91 | 1.18 | 0.48 | 11.32 |
| 1193 | 22 | 53.36 | RSI overbought (>70) — hold ret_high_7d_news | RSI overbought (>70) | high | 7 | news | 2 | 100.0 | 4.62 | 4.62 | 9.23 | 4.73 | 0.98 | 1.27 | 7.96 |
| 1194 | 37 | 35.58 | Director only + Value ≥100k — hold ret_high_1d_open | Director only + Value ≥100k | high | 1 | open | 3 | 100.0 | 4.61 | 2.04 | 13.84 | 5.86 | 0.79 | 0.48 | 11.32 |
| 1195 | 14 | 65.45 | Price > MA200 — hold ret_mean_10d_news | Price > MA200 | mean | 10 | news | 4 | 50.0 | 4.61 | 2.16 | 18.45 | 7.1 | 0.65 | -0.56 | 14.68 |
| 1196 | 15 | 62.43 | Price > MA50 — hold ret_mean_7d_news | Price > MA50 | mean | 7 | news | 5 | 60.0 | 4.6 | 4.75 | 23.02 | 6.09 | 0.76 | -0.81 | 13.99 |
| 1197 | 40 | 33.74 | Director only + Position +10% — hold ret_high_1d_open | Director only + Position +10% | high | 1 | open | 4 | 100.0 | 4.57 | 2.83 | 18.29 | 4.6 | 0.99 | 1.3 | 11.32 |
| 1198 | 53 | 0.0 | Qty ≥100k shares — hold ret_mean_2d_open | Qty ≥100k shares | mean | 2 | open | 1 | 100.0 | 4.56 | 4.56 | 4.56 | nan | nan | 4.56 | 4.56 |
| 1199 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_mean_2d_open | Small cap (≤1B) Value ≥100k | mean | 2 | open | 1 | 100.0 | 4.56 | 4.56 | 4.56 | nan | nan | 4.56 | 4.56 |
| 1200 | 32 | 44.63 | Position +10% — hold ret_high_1d_news | Position +10% | high | 1 | news | 6 | 83.3 | 4.55 | 3.26 | 27.29 | 5.53 | 0.82 | -2.48 | 12.15 |
| 1201 | 22 | 53.36 | RSI overbought (>70) — hold ret_high_10d_open | RSI overbought (>70) | high | 10 | open | 2 | 100.0 | 4.55 | 4.55 | 9.1 | 3.56 | 1.28 | 2.03 | 7.07 |
| 1202 | 10 | 66.41 | CEO/CFO — hold ret_mean_5d_open | CEO/CFO | mean | 5 | open | 4 | 100.0 | 4.54 | 3.23 | 18.17 | 4.49 | 1.01 | 0.78 | 10.93 |
| 1203 | 11 | 66.41 | Officer/President — hold ret_mean_5d_open | Officer/President | mean | 5 | open | 4 | 100.0 | 4.54 | 3.23 | 18.17 | 4.49 | 1.01 | 0.78 | 10.93 |
| 1204 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_mean_5d_open | Large cap (≥250M) CEO/CFO | mean | 5 | open | 4 | 100.0 | 4.54 | 3.23 | 18.17 | 4.49 | 1.01 | 0.78 | 10.93 |
| 1205 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_mean_5d_open | Large cap (≥500M) CEO/CFO | mean | 5 | open | 4 | 100.0 | 4.54 | 3.23 | 18.17 | 4.49 | 1.01 | 0.78 | 10.93 |
| 1206 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_mean_10d_open | Mid cap (1B–10B) Value ≥100k | mean | 10 | open | 4 | 75.0 | 4.54 | 3.04 | 18.17 | 6.01 | 0.76 | -0.97 | 13.07 |
| 1207 | 6 | 77.62 | CEO only — hold ret_mean_60d_open | CEO only | mean | 60 | open | 3 | 66.7 | 4.53 | 2.99 | 13.59 | 11.84 | 0.38 | -6.46 | 17.06 |
| 1208 | 32 | 44.63 | Position +10% — hold ret_high_1d_open | Position +10% | high | 1 | open | 6 | 100.0 | 4.5 | 2.83 | 27.02 | 4.42 | 1.02 | 0.25 | 11.32 |
| 1209 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_high_3d_news | Multiple buys (n≥2) | high | 3 | news | 3 | 100.0 | 4.5 | 4.54 | 13.51 | 3.9 | 1.16 | 0.59 | 8.38 |
| 1210 | 28 | 48.48 | Tutti — hold ret_high_1d_open | Tutti | high | 1 | open | 10 | 100.0 | 4.48 | 3.24 | 44.84 | 3.88 | 1.16 | 0.25 | 11.32 |
| 1211 | 15 | 62.43 | Price > MA50 — hold ret_mean_10d_news | Price > MA50 | mean | 10 | news | 5 | 60.0 | 4.47 | 3.88 | 22.33 | 6.16 | 0.73 | -0.56 | 14.68 |
| 1212 | 15 | 62.43 | Price > MA50 — hold ret_mean_30d_news | Price > MA50 | mean | 30 | news | 5 | 80.0 | 4.47 | 3.96 | 22.33 | 5.55 | 0.81 | -1.39 | 13.57 |
| 1213 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_mean_60d_news | CEO only + Value ≥500k | mean | 60 | news | 1 | 100.0 | 4.46 | 4.46 | 4.46 | nan | nan | 4.46 | 4.46 |
| 1214 | 1 | 100.0 | CEO only + Position +10% — hold ret_mean_60d_news | CEO only + Position +10% | mean | 60 | news | 1 | 100.0 | 4.46 | 4.46 | 4.46 | nan | nan | 4.46 | 4.46 |
| 1215 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_mean_60d_news | Near 52w high + CEO/CFO | mean | 60 | news | 1 | 100.0 | 4.46 | 4.46 | 4.46 | nan | nan | 4.46 | 4.46 |
| 1216 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_mean_30d_open | CEO/CFO + Value ≥100k | mean | 30 | open | 3 | 66.7 | 4.44 | 5.31 | 13.33 | 8.0 | 0.56 | -3.95 | 11.97 |
| 1217 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_mean_30d_open | Large cap (≥750M) CEO/CFO | mean | 30 | open | 3 | 66.7 | 4.44 | 5.31 | 13.33 | 8.0 | 0.56 | -3.95 | 11.97 |
| 1218 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_mean_30d_open | Large cap (≥1B) CEO/CFO | mean | 30 | open | 3 | 66.7 | 4.44 | 5.31 | 13.33 | 8.0 | 0.56 | -3.95 | 11.97 |
| 1219 | 26 | 50.0 | Qty ≥50k shares — hold ret_mean_5d_open | Qty ≥50k shares | mean | 5 | open | 2 | 50.0 | 4.43 | 4.43 | 8.86 | 9.19 | 0.48 | -2.07 | 10.93 |
| 1220 | 27 | 50.0 | Value ≥1M — hold ret_mean_5d_open | Value ≥1M | mean | 5 | open | 2 | 50.0 | 4.43 | 4.43 | 8.86 | 9.19 | 0.48 | -2.07 | 10.93 |
| 1221 | 38 | 34.53 | Price < MA50 — hold ret_high_1d_news | Price < MA50 | high | 1 | news | 5 | 80.0 | 4.4 | 3.63 | 22.0 | 5.69 | 0.77 | -2.48 | 12.15 |
| 1222 | 14 | 65.45 | Price > MA200 — hold ret_mean_14d_open | Price > MA200 | mean | 14 | open | 4 | 75.0 | 4.39 | 2.42 | 17.56 | 5.83 | 0.75 | -0.16 | 12.89 |
| 1223 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_high_1d_open | Mid cap (1B–10B) CEO/CFO | high | 1 | open | 2 | 100.0 | 4.36 | 4.37 | 8.73 | 5.82 | 0.75 | 0.25 | 8.48 |
| 1224 | 26 | 50.0 | Qty ≥50k shares — hold ret_mean_1d_open | Qty ≥50k shares | mean | 1 | open | 2 | 100.0 | 4.36 | 4.36 | 8.72 | 1.12 | 3.9 | 3.57 | 5.15 |
| 1225 | 27 | 50.0 | Value ≥1M — hold ret_mean_1d_open | Value ≥1M | mean | 1 | open | 2 | 100.0 | 4.36 | 4.36 | 8.72 | 1.12 | 3.9 | 3.57 | 5.15 |
| 1226 | 10 | 66.41 | CEO/CFO — hold ret_mean_60d_news | CEO/CFO | mean | 60 | news | 4 | 75.0 | 4.33 | 2.67 | 17.33 | 8.48 | 0.51 | -3.97 | 15.95 |
| 1227 | 11 | 66.41 | Officer/President — hold ret_mean_60d_news | Officer/President | mean | 60 | news | 4 | 75.0 | 4.33 | 2.67 | 17.33 | 8.48 | 0.51 | -3.97 | 15.95 |
| 1228 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_mean_60d_news | Large cap (≥250M) CEO/CFO | mean | 60 | news | 4 | 75.0 | 4.33 | 2.67 | 17.33 | 8.48 | 0.51 | -3.97 | 15.95 |
| 1229 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_mean_60d_news | Large cap (≥500M) CEO/CFO | mean | 60 | news | 4 | 75.0 | 4.33 | 2.67 | 17.33 | 8.48 | 0.51 | -3.97 | 15.95 |
| 1230 | 51 | 20.1 | Position +30% — hold ret_high_2d_news | Position +30% | high | 2 | news | 3 | 66.7 | 4.32 | 1.08 | 12.97 | 6.81 | 0.63 | -0.26 | 12.15 |
| 1231 | 10 | 66.41 | CEO/CFO — hold ret_mean_60d_open | CEO/CFO | mean | 60 | open | 4 | 75.0 | 4.32 | 3.35 | 17.29 | 9.67 | 0.45 | -6.46 | 17.06 |
| 1232 | 11 | 66.41 | Officer/President — hold ret_mean_60d_open | Officer/President | mean | 60 | open | 4 | 75.0 | 4.32 | 3.35 | 17.29 | 9.67 | 0.45 | -6.46 | 17.06 |
| 1233 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_mean_60d_open | Large cap (≥250M) CEO/CFO | mean | 60 | open | 4 | 75.0 | 4.32 | 3.35 | 17.29 | 9.67 | 0.45 | -6.46 | 17.06 |
| 1234 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_mean_60d_open | Large cap (≥500M) CEO/CFO | mean | 60 | open | 4 | 75.0 | 4.32 | 3.35 | 17.29 | 9.67 | 0.45 | -6.46 | 17.06 |
| 1235 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_mean_7d_news | Mid cap (1B–10B) Value ≥100k | mean | 7 | news | 4 | 50.0 | 4.31 | 2.04 | 17.25 | 6.95 | 0.62 | -0.81 | 13.99 |
| 1236 | 22 | 53.36 | RSI overbought (>70) — hold ret_high_5d_news | RSI overbought (>70) | high | 5 | news | 2 | 100.0 | 4.3 | 4.3 | 8.61 | 4.29 | 1.0 | 1.27 | 7.34 |
| 1237 | 51 | 20.1 | Position +30% — hold ret_high_1d_open | Position +30% | high | 1 | open | 3 | 100.0 | 4.29 | 1.3 | 12.87 | 6.11 | 0.7 | 0.25 | 11.32 |
| 1238 | 14 | 65.45 | Price > MA200 — hold ret_mean_7d_news | Price > MA200 | mean | 7 | news | 4 | 50.0 | 4.28 | 1.98 | 17.13 | 6.98 | 0.61 | -0.81 | 13.99 |
| 1239 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_high_2d_news | Large cap (≥2B) CEO/CFO | high | 2 | news | 2 | 50.0 | 4.27 | 4.27 | 8.54 | 6.41 | 0.67 | -0.26 | 8.8 |
| 1240 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_mean_2d_open | CEO only + Value ≥100k | mean | 2 | open | 2 | 100.0 | 4.27 | 4.27 | 8.54 | 2.33 | 1.83 | 2.62 | 5.92 |
| 1241 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_mean_2d_open | Price > MA50 + CEO/CFO | mean | 2 | open | 2 | 100.0 | 4.27 | 4.27 | 8.54 | 2.33 | 1.83 | 2.62 | 5.92 |
| 1242 | 4 | 82.51 | CEO + Director (combo) — hold ret_mean_3d_open | CEO + Director (combo) | mean | 3 | open | 1 | 100.0 | 4.27 | 4.27 | 4.27 | nan | nan | 4.27 | 4.27 |
| 1243 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_mean_3d_open | Small cap (≤1B) CEO/CFO | mean | 3 | open | 1 | 100.0 | 4.27 | 4.27 | 4.27 | nan | nan | 4.27 | 4.27 |
| 1244 | 14 | 65.45 | Price > MA200 — hold ret_high_1d_news | Price > MA200 | high | 1 | news | 4 | 100.0 | 4.26 | 2.87 | 17.03 | 3.92 | 1.09 | 1.27 | 10.02 |
| 1245 | 15 | 62.43 | Price > MA50 — hold ret_mean_14d_news | Price > MA50 | mean | 14 | news | 5 | 100.0 | 4.26 | 1.69 | 21.31 | 5.89 | 0.72 | 0.5 | 14.49 |
| 1246 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_high_2d_open | Large cap (≥2B) CEO/CFO | high | 2 | open | 2 | 100.0 | 4.25 | 4.25 | 8.5 | 2.45 | 1.74 | 2.52 | 5.98 |
| 1247 | 4 | 82.51 | CEO + Director (combo) — hold ret_mean_5d_open | CEO + Director (combo) | mean | 5 | open | 1 | 100.0 | 4.23 | 4.23 | 4.23 | nan | nan | 4.23 | 4.23 |
| 1248 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_mean_5d_open | Small cap (≤1B) CEO/CFO | mean | 5 | open | 1 | 100.0 | 4.23 | 4.23 | 4.23 | nan | nan | 4.23 | 4.23 |
| 1249 | 6 | 77.62 | CEO only — hold ret_mean_2d_open | CEO only | mean | 2 | open | 3 | 100.0 | 4.22 | 4.12 | 12.66 | 1.65 | 2.55 | 2.62 | 5.92 |
| 1250 | 6 | 77.62 | CEO only — hold ret_mean_90d_open | CEO only | mean | 90 | open | 3 | 33.3 | 4.21 | -2.66 | 12.62 | 14.56 | 0.29 | -5.65 | 20.93 |
| 1251 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_mean_7d_open | Mid cap (1B–10B) Value ≥100k | mean | 7 | open | 4 | 75.0 | 4.2 | 2.98 | 16.78 | 5.92 | 0.71 | -1.58 | 12.39 |
| 1252 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_high_1d_open | Multiple buys (n≥2) | high | 1 | open | 3 | 100.0 | 4.18 | 3.63 | 12.53 | 4.23 | 0.99 | 0.25 | 8.65 |
| 1253 | 26 | 50.0 | Qty ≥50k shares — hold ret_mean_7d_news | Qty ≥50k shares | mean | 7 | news | 2 | 50.0 | 4.16 | 4.17 | 8.33 | 13.89 | 0.3 | -5.66 | 13.99 |
| 1254 | 27 | 50.0 | Value ≥1M — hold ret_mean_7d_news | Value ≥1M | mean | 7 | news | 2 | 50.0 | 4.16 | 4.17 | 8.33 | 13.89 | 0.3 | -5.66 | 13.99 |
| 1255 | 49 | 32.78 | CFO only — hold ret_mean_14d_open | CFO only | mean | 14 | open | 1 | 100.0 | 4.15 | 4.15 | 4.15 | nan | nan | 4.15 | 4.15 |
| 1256 | 48 | 32.78 | CFO + Director (combo) — hold ret_mean_14d_open | CFO + Director (combo) | mean | 14 | open | 1 | 100.0 | 4.15 | 4.15 | 4.15 | nan | nan | 4.15 | 4.15 |
| 1257 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_mean_14d_open | CFO only + Value ≥50k | mean | 14 | open | 1 | 100.0 | 4.15 | 4.15 | 4.15 | nan | nan | 4.15 | 4.15 |
| 1258 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_mean_14d_open | CFO only + Value ≥100k | mean | 14 | open | 1 | 100.0 | 4.15 | 4.15 | 4.15 | nan | nan | 4.15 | 4.15 |
| 1259 | 47 | 32.78 | CFO only + Position +10% — hold ret_mean_14d_open | CFO only + Position +10% | mean | 14 | open | 1 | 100.0 | 4.15 | 4.15 | 4.15 | nan | nan | 4.15 | 4.15 |
| 1260 | 46 | 32.78 | CFO only + Position +20% — hold ret_mean_14d_open | CFO only + Position +20% | mean | 14 | open | 1 | 100.0 | 4.15 | 4.15 | 4.15 | nan | nan | 4.15 | 4.15 |
| 1261 | 44 | 32.78 | RSI oversold (<30) — hold ret_mean_14d_open | RSI oversold (<30) | mean | 14 | open | 1 | 100.0 | 4.15 | 4.15 | 4.15 | nan | nan | 4.15 | 4.15 |
| 1262 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_mean_14d_open | RSI oversold + CEO/CFO | mean | 14 | open | 1 | 100.0 | 4.15 | 4.15 | 4.15 | nan | nan | 4.15 | 4.15 |
| 1263 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_mean_14d_open | RSI oversold + Value ≥100k | mean | 14 | open | 1 | 100.0 | 4.15 | 4.15 | 4.15 | nan | nan | 4.15 | 4.15 |
| 1264 | 4 | 82.51 | CEO + Director (combo) — hold ret_mean_7d_news | CEO + Director (combo) | mean | 7 | news | 1 | 100.0 | 4.14 | 4.14 | 4.14 | nan | nan | 4.14 | 4.14 |
| 1265 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_mean_7d_news | Small cap (≤1B) CEO/CFO | mean | 7 | news | 1 | 100.0 | 4.14 | 4.14 | 4.14 | nan | nan | 4.14 | 4.14 |
| 1266 | 4 | 82.51 | CEO + Director (combo) — hold ret_mean_2d_open | CEO + Director (combo) | mean | 2 | open | 1 | 100.0 | 4.12 | 4.12 | 4.12 | nan | nan | 4.12 | 4.12 |
| 1267 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_mean_2d_open | Small cap (≤1B) CEO/CFO | mean | 2 | open | 1 | 100.0 | 4.12 | 4.12 | 4.12 | nan | nan | 4.12 | 4.12 |
| 1268 | 6 | 77.62 | CEO only — hold ret_mean_1d_news | CEO only | mean | 1 | news | 3 | 100.0 | 4.11 | 5.05 | 12.33 | 1.83 | 2.24 | 2.0 | 5.28 |
| 1269 | 15 | 62.43 | Price > MA50 — hold ret_mean_5d_news | Price > MA50 | mean | 5 | news | 5 | 80.0 | 4.08 | 4.01 | 20.42 | 5.36 | 0.76 | -1.09 | 12.51 |
| 1270 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_mean_14d_open | Multiple buys (n≥2) | mean | 14 | open | 3 | 66.7 | 4.04 | 4.15 | 12.13 | 4.43 | 0.91 | -0.44 | 8.42 |
| 1271 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_mean_30d_open | CEO only + Value ≥100k | mean | 30 | open | 2 | 50.0 | 4.01 | 4.01 | 8.02 | 11.26 | 0.36 | -3.95 | 11.97 |
| 1272 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_mean_30d_open | Price > MA50 + CEO/CFO | mean | 30 | open | 2 | 50.0 | 4.01 | 4.01 | 8.02 | 11.26 | 0.36 | -3.95 | 11.97 |
| 1273 | 36 | 36.54 | Director only (no C-level) — hold ret_high_1d_news | Director only (no C-level) | high | 1 | news | 6 | 100.0 | 3.98 | 2.87 | 23.87 | 4.13 | 0.96 | 1.08 | 12.15 |
| 1274 | 15 | 62.43 | Price > MA50 — hold ret_high_1d_open | Price > MA50 | high | 1 | open | 5 | 100.0 | 3.94 | 2.85 | 19.69 | 3.2 | 1.23 | 0.48 | 8.48 |
| 1275 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_mean_3d_open | Mid cap (1B–10B) CEO/CFO | mean | 3 | open | 2 | 50.0 | 3.94 | 3.94 | 7.89 | 5.64 | 0.7 | -0.04 | 7.93 |
| 1276 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_mean_10d_news | Large cap (≥3B) CEO/CFO | mean | 10 | news | 1 | 100.0 | 3.88 | 3.88 | 3.88 | nan | nan | 3.88 | 3.88 |
| 1277 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_mean_10d_news | Large cap (≥5B) CEO/CFO | mean | 10 | news | 1 | 100.0 | 3.88 | 3.88 | 3.88 | nan | nan | 3.88 | 3.88 |
| 1278 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_mean_10d_news | Large cap (≥10B) CEO/CFO | mean | 10 | news | 1 | 100.0 | 3.88 | 3.88 | 3.88 | nan | nan | 3.88 | 3.88 |
| 1279 | 14 | 65.45 | Price > MA200 — hold ret_mean_5d_news | Price > MA200 | mean | 5 | news | 4 | 75.0 | 3.87 | 2.02 | 15.47 | 6.16 | 0.63 | -1.09 | 12.51 |
| 1280 | 22 | 53.36 | RSI overbought (>70) — hold ret_mean_90d_news | RSI overbought (>70) | mean | 90 | news | 2 | 100.0 | 3.84 | 3.83 | 7.67 | 5.35 | 0.72 | 0.05 | 7.62 |
| 1281 | 33 | 41.81 | Director — hold ret_high_1d_open | Director | high | 1 | open | 8 | 100.0 | 3.82 | 2.45 | 30.52 | 4.04 | 0.95 | 0.25 | 11.32 |
| 1282 | 14 | 65.45 | Price > MA200 — hold ret_mean_10d_open | Price > MA200 | mean | 10 | open | 4 | 50.0 | 3.8 | 1.54 | 15.19 | 6.52 | 0.58 | -0.97 | 13.07 |
| 1283 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_mean_3d_news | CEO/CFO + Value ≥100k | mean | 3 | news | 3 | 66.7 | 3.78 | 4.64 | 11.35 | 6.16 | 0.61 | -2.76 | 9.47 |
| 1284 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_mean_3d_news | Large cap (≥750M) CEO/CFO | mean | 3 | news | 3 | 66.7 | 3.78 | 4.64 | 11.35 | 6.16 | 0.61 | -2.76 | 9.47 |
| 1285 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_mean_3d_news | Large cap (≥1B) CEO/CFO | mean | 3 | news | 3 | 66.7 | 3.78 | 4.64 | 11.35 | 6.16 | 0.61 | -2.76 | 9.47 |
| 1286 | 22 | 53.36 | RSI overbought (>70) — hold ret_high_7d_open | RSI overbought (>70) | high | 7 | open | 2 | 100.0 | 3.78 | 3.78 | 7.55 | 4.66 | 0.81 | 0.48 | 7.07 |
| 1287 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_high_1d_news | Mid cap (1B–10B) CEO/CFO | high | 1 | news | 2 | 50.0 | 3.77 | 3.77 | 7.54 | 8.84 | 0.43 | -2.48 | 10.02 |
| 1288 | 39 | 34.48 | Position +20% — hold ret_high_1d_open | Position +20% | high | 1 | open | 4 | 100.0 | 3.73 | 1.67 | 14.91 | 5.11 | 0.73 | 0.25 | 11.32 |
| 1289 | 22 | 53.36 | RSI overbought (>70) — hold ret_mean_60d_news | RSI overbought (>70) | mean | 60 | news | 2 | 100.0 | 3.72 | 3.73 | 7.45 | 2.1 | 1.77 | 2.24 | 5.21 |
| 1290 | 22 | 53.36 | RSI overbought (>70) — hold ret_high_3d_news | RSI overbought (>70) | high | 3 | news | 2 | 100.0 | 3.7 | 3.71 | 7.41 | 3.44 | 1.08 | 1.27 | 6.14 |
| 1291 | 49 | 32.78 | CFO only — hold ret_mean_60d_open | CFO only | mean | 60 | open | 1 | 100.0 | 3.7 | 3.7 | 3.7 | nan | nan | 3.7 | 3.7 |
| 1292 | 48 | 32.78 | CFO + Director (combo) — hold ret_mean_60d_open | CFO + Director (combo) | mean | 60 | open | 1 | 100.0 | 3.7 | 3.7 | 3.7 | nan | nan | 3.7 | 3.7 |
| 1293 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_mean_60d_open | CFO only + Value ≥50k | mean | 60 | open | 1 | 100.0 | 3.7 | 3.7 | 3.7 | nan | nan | 3.7 | 3.7 |
| 1294 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_mean_60d_open | CFO only + Value ≥100k | mean | 60 | open | 1 | 100.0 | 3.7 | 3.7 | 3.7 | nan | nan | 3.7 | 3.7 |
| 1295 | 47 | 32.78 | CFO only + Position +10% — hold ret_mean_60d_open | CFO only + Position +10% | mean | 60 | open | 1 | 100.0 | 3.7 | 3.7 | 3.7 | nan | nan | 3.7 | 3.7 |
| 1296 | 46 | 32.78 | CFO only + Position +20% — hold ret_mean_60d_open | CFO only + Position +20% | mean | 60 | open | 1 | 100.0 | 3.7 | 3.7 | 3.7 | nan | nan | 3.7 | 3.7 |
| 1297 | 44 | 32.78 | RSI oversold (<30) — hold ret_mean_60d_open | RSI oversold (<30) | mean | 60 | open | 1 | 100.0 | 3.7 | 3.7 | 3.7 | nan | nan | 3.7 | 3.7 |
| 1298 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_mean_60d_open | RSI oversold + CEO/CFO | mean | 60 | open | 1 | 100.0 | 3.7 | 3.7 | 3.7 | nan | nan | 3.7 | 3.7 |
| 1299 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_mean_60d_open | RSI oversold + Value ≥100k | mean | 60 | open | 1 | 100.0 | 3.7 | 3.7 | 3.7 | nan | nan | 3.7 | 3.7 |
| 1300 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_high_2d_news | Multiple buys (n≥2) | high | 2 | news | 3 | 66.7 | 3.66 | 3.63 | 10.99 | 3.94 | 0.93 | -0.26 | 7.62 |
| 1301 | 10 | 66.41 | CEO/CFO — hold ret_mean_3d_news | CEO/CFO | mean | 3 | news | 4 | 75.0 | 3.66 | 3.96 | 14.62 | 5.04 | 0.73 | -2.76 | 9.47 |
| 1302 | 11 | 66.41 | Officer/President — hold ret_mean_3d_news | Officer/President | mean | 3 | news | 4 | 75.0 | 3.66 | 3.96 | 14.62 | 5.04 | 0.73 | -2.76 | 9.47 |
| 1303 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_mean_3d_news | Large cap (≥250M) CEO/CFO | mean | 3 | news | 4 | 75.0 | 3.66 | 3.96 | 14.62 | 5.04 | 0.73 | -2.76 | 9.47 |
| 1304 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_mean_3d_news | Large cap (≥500M) CEO/CFO | mean | 3 | news | 4 | 75.0 | 3.66 | 3.96 | 14.62 | 5.04 | 0.73 | -2.76 | 9.47 |
| 1305 | 14 | 65.45 | Price > MA200 — hold ret_mean_60d_news | Price > MA200 | mean | 60 | news | 4 | 100.0 | 3.64 | 3.54 | 14.54 | 1.43 | 2.55 | 2.24 | 5.21 |
| 1306 | 33 | 41.81 | Director — hold ret_high_1d_news | Director | high | 1 | news | 8 | 87.5 | 3.63 | 2.87 | 29.01 | 4.46 | 0.81 | -2.48 | 12.15 |
| 1307 | 36 | 36.54 | Director only (no C-level) — hold ret_high_1d_open | Director only (no C-level) | high | 1 | open | 6 | 100.0 | 3.6 | 2.45 | 21.62 | 3.94 | 0.91 | 0.48 | 11.32 |
| 1308 | 51 | 20.1 | Position +30% — hold ret_high_1d_news | Position +30% | high | 1 | news | 3 | 66.7 | 3.58 | 1.08 | 10.75 | 7.63 | 0.47 | -2.48 | 12.15 |
| 1309 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_mean_1d_open | CEO only + Value ≥500k | mean | 1 | open | 1 | 100.0 | 3.57 | 3.57 | 3.57 | nan | nan | 3.57 | 3.57 |
| 1310 | 1 | 100.0 | CEO only + Position +10% — hold ret_mean_1d_open | CEO only + Position +10% | mean | 1 | open | 1 | 100.0 | 3.57 | 3.57 | 3.57 | nan | nan | 3.57 | 3.57 |
| 1311 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_mean_1d_open | Near 52w high + CEO/CFO | mean | 1 | open | 1 | 100.0 | 3.57 | 3.57 | 3.57 | nan | nan | 3.57 | 3.57 |
| 1312 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_mean_30d_news | Multiple buys (n≥2) | mean | 30 | news | 3 | 66.7 | 3.55 | 2.45 | 10.64 | 5.35 | 0.66 | -1.17 | 9.36 |
| 1313 | 10 | 66.41 | CEO/CFO — hold ret_mean_3d_open | CEO/CFO | mean | 3 | open | 4 | 75.0 | 3.52 | 3.1 | 14.09 | 3.43 | 1.03 | -0.04 | 7.93 |
| 1314 | 11 | 66.41 | Officer/President — hold ret_mean_3d_open | Officer/President | mean | 3 | open | 4 | 75.0 | 3.52 | 3.1 | 14.09 | 3.43 | 1.03 | -0.04 | 7.93 |
| 1315 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_mean_3d_open | Large cap (≥250M) CEO/CFO | mean | 3 | open | 4 | 75.0 | 3.52 | 3.1 | 14.09 | 3.43 | 1.03 | -0.04 | 7.93 |
| 1316 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_mean_3d_open | Large cap (≥500M) CEO/CFO | mean | 3 | open | 4 | 75.0 | 3.52 | 3.1 | 14.09 | 3.43 | 1.03 | -0.04 | 7.93 |
| 1317 | 22 | 53.36 | RSI overbought (>70) — hold ret_high_2d_news | RSI overbought (>70) | high | 2 | news | 2 | 100.0 | 3.51 | 3.51 | 7.02 | 3.17 | 1.11 | 1.27 | 5.75 |
| 1318 | 14 | 65.45 | Price > MA200 — hold ret_mean_7d_open | Price > MA200 | mean | 7 | open | 4 | 50.0 | 3.47 | 1.54 | 13.89 | 6.42 | 0.54 | -1.58 | 12.39 |
| 1319 | 14 | 65.45 | Price > MA200 — hold ret_high_1d_open | Price > MA200 | high | 1 | open | 4 | 100.0 | 3.46 | 2.45 | 13.85 | 3.49 | 0.99 | 0.48 | 8.48 |
| 1320 | 22 | 53.36 | RSI overbought (>70) — hold ret_high_5d_open | RSI overbought (>70) | high | 5 | open | 2 | 100.0 | 3.46 | 3.46 | 6.93 | 4.22 | 0.82 | 0.48 | 6.45 |
| 1321 | 15 | 62.43 | Price > MA50 — hold ret_mean_3d_news | Price > MA50 | mean | 3 | news | 5 | 80.0 | 3.43 | 3.22 | 17.16 | 4.05 | 0.85 | -1.26 | 9.47 |
| 1322 | 39 | 34.48 | Position +20% — hold ret_high_1d_news | Position +20% | high | 1 | news | 4 | 75.0 | 3.41 | 1.99 | 13.64 | 6.24 | 0.55 | -2.48 | 12.15 |
| 1323 | 15 | 62.43 | Price > MA50 — hold ret_mean_7d_open | Price > MA50 | mean | 7 | open | 5 | 60.0 | 3.41 | 3.15 | 17.04 | 5.56 | 0.61 | -1.58 | 12.39 |
| 1324 | 49 | 32.78 | CFO only — hold ret_high_3d_open | CFO only | high | 3 | open | 1 | 100.0 | 3.39 | 3.39 | 3.39 | nan | nan | 3.39 | 3.39 |
| 1325 | 48 | 32.78 | CFO + Director (combo) — hold ret_high_3d_open | CFO + Director (combo) | high | 3 | open | 1 | 100.0 | 3.39 | 3.39 | 3.39 | nan | nan | 3.39 | 3.39 |
| 1326 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_high_3d_open | CFO only + Value ≥50k | high | 3 | open | 1 | 100.0 | 3.39 | 3.39 | 3.39 | nan | nan | 3.39 | 3.39 |
| 1327 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_high_3d_open | CFO only + Value ≥100k | high | 3 | open | 1 | 100.0 | 3.39 | 3.39 | 3.39 | nan | nan | 3.39 | 3.39 |
| 1328 | 47 | 32.78 | CFO only + Position +10% — hold ret_high_3d_open | CFO only + Position +10% | high | 3 | open | 1 | 100.0 | 3.39 | 3.39 | 3.39 | nan | nan | 3.39 | 3.39 |
| 1329 | 46 | 32.78 | CFO only + Position +20% — hold ret_high_3d_open | CFO only + Position +20% | high | 3 | open | 1 | 100.0 | 3.39 | 3.39 | 3.39 | nan | nan | 3.39 | 3.39 |
| 1330 | 44 | 32.78 | RSI oversold (<30) — hold ret_high_3d_open | RSI oversold (<30) | high | 3 | open | 1 | 100.0 | 3.39 | 3.39 | 3.39 | nan | nan | 3.39 | 3.39 |
| 1331 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_high_3d_open | RSI oversold + CEO/CFO | high | 3 | open | 1 | 100.0 | 3.39 | 3.39 | 3.39 | nan | nan | 3.39 | 3.39 |
| 1332 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_high_3d_open | RSI oversold + Value ≥100k | high | 3 | open | 1 | 100.0 | 3.39 | 3.39 | 3.39 | nan | nan | 3.39 | 3.39 |
| 1333 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_mean_5d_news | Mid cap (1B–10B) Value ≥100k | mean | 5 | news | 4 | 50.0 | 3.37 | 1.46 | 13.47 | 6.64 | 0.51 | -1.96 | 12.51 |
| 1334 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_mean_3d_news | Mid cap (1B–10B) CEO/CFO | mean | 3 | news | 2 | 50.0 | 3.36 | 3.36 | 6.71 | 8.65 | 0.39 | -2.76 | 9.47 |
| 1335 | 49 | 32.78 | CFO only — hold ret_high_5d_news | CFO only | high | 5 | news | 1 | 100.0 | 3.34 | 3.34 | 3.34 | nan | nan | 3.34 | 3.34 |
| 1336 | 48 | 32.78 | CFO + Director (combo) — hold ret_high_5d_news | CFO + Director (combo) | high | 5 | news | 1 | 100.0 | 3.34 | 3.34 | 3.34 | nan | nan | 3.34 | 3.34 |
| 1337 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_high_5d_news | CFO only + Value ≥50k | high | 5 | news | 1 | 100.0 | 3.34 | 3.34 | 3.34 | nan | nan | 3.34 | 3.34 |
| 1338 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_high_5d_news | CFO only + Value ≥100k | high | 5 | news | 1 | 100.0 | 3.34 | 3.34 | 3.34 | nan | nan | 3.34 | 3.34 |
| 1339 | 47 | 32.78 | CFO only + Position +10% — hold ret_high_5d_news | CFO only + Position +10% | high | 5 | news | 1 | 100.0 | 3.34 | 3.34 | 3.34 | nan | nan | 3.34 | 3.34 |
| 1340 | 46 | 32.78 | CFO only + Position +20% — hold ret_high_5d_news | CFO only + Position +20% | high | 5 | news | 1 | 100.0 | 3.34 | 3.34 | 3.34 | nan | nan | 3.34 | 3.34 |
| 1341 | 44 | 32.78 | RSI oversold (<30) — hold ret_high_5d_news | RSI oversold (<30) | high | 5 | news | 1 | 100.0 | 3.34 | 3.34 | 3.34 | nan | nan | 3.34 | 3.34 |
| 1342 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_high_5d_news | RSI oversold + CEO/CFO | high | 5 | news | 1 | 100.0 | 3.34 | 3.34 | 3.34 | nan | nan | 3.34 | 3.34 |
| 1343 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_high_5d_news | RSI oversold + Value ≥100k | high | 5 | news | 1 | 100.0 | 3.34 | 3.34 | 3.34 | nan | nan | 3.34 | 3.34 |
| 1344 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_mean_60d_open | Mid cap (1B–10B) CEO/CFO | mean | 60 | open | 2 | 100.0 | 3.34 | 3.35 | 6.69 | 0.5 | 6.66 | 2.99 | 3.7 |
| 1345 | 10 | 66.41 | CEO/CFO — hold ret_mean_90d_news | CEO/CFO | mean | 90 | news | 4 | 25.0 | 3.31 | -1.7 | 13.23 | 11.01 | 0.3 | -3.15 | 19.78 |
| 1346 | 11 | 66.41 | Officer/President — hold ret_mean_90d_news | Officer/President | mean | 90 | news | 4 | 25.0 | 3.31 | -1.7 | 13.23 | 11.01 | 0.3 | -3.15 | 19.78 |
| 1347 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_mean_90d_news | Large cap (≥250M) CEO/CFO | mean | 90 | news | 4 | 25.0 | 3.31 | -1.7 | 13.23 | 11.01 | 0.3 | -3.15 | 19.78 |
| 1348 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_mean_90d_news | Large cap (≥500M) CEO/CFO | mean | 90 | news | 4 | 25.0 | 3.31 | -1.7 | 13.23 | 11.01 | 0.3 | -3.15 | 19.78 |
| 1349 | 15 | 62.43 | Price > MA50 — hold ret_mean_30d_open | Price > MA50 | mean | 30 | open | 5 | 80.0 | 3.3 | 3.09 | 16.5 | 5.75 | 0.57 | -3.95 | 11.97 |
| 1350 | 10 | 66.41 | CEO/CFO — hold ret_mean_90d_open | CEO/CFO | mean | 90 | open | 4 | 50.0 | 3.3 | -1.03 | 13.22 | 12.02 | 0.27 | -5.65 | 20.93 |
| 1351 | 11 | 66.41 | Officer/President — hold ret_mean_90d_open | Officer/President | mean | 90 | open | 4 | 50.0 | 3.3 | -1.03 | 13.22 | 12.02 | 0.27 | -5.65 | 20.93 |
| 1352 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_mean_90d_open | Large cap (≥250M) CEO/CFO | mean | 90 | open | 4 | 50.0 | 3.3 | -1.03 | 13.22 | 12.02 | 0.27 | -5.65 | 20.93 |
| 1353 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_mean_90d_open | Large cap (≥500M) CEO/CFO | mean | 90 | open | 4 | 50.0 | 3.3 | -1.03 | 13.22 | 12.02 | 0.27 | -5.65 | 20.93 |
| 1354 | 15 | 62.43 | Price > MA50 — hold ret_mean_10d_open | Price > MA50 | mean | 10 | open | 5 | 60.0 | 3.28 | 1.19 | 16.38 | 5.77 | 0.57 | -0.97 | 13.07 |
| 1355 | 4 | 82.51 | CEO + Director (combo) — hold ret_mean_3d_news | CEO + Director (combo) | mean | 3 | news | 1 | 100.0 | 3.27 | 3.27 | 3.27 | nan | nan | 3.27 | 3.27 |
| 1356 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_mean_3d_open | CEO/CFO + Value ≥100k | mean | 3 | open | 3 | 66.7 | 3.27 | 1.93 | 9.82 | 4.15 | 0.79 | -0.04 | 7.93 |
| 1357 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_mean_3d_news | Small cap (≤1B) CEO/CFO | mean | 3 | news | 1 | 100.0 | 3.27 | 3.27 | 3.27 | nan | nan | 3.27 | 3.27 |
| 1358 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_mean_3d_open | Large cap (≥750M) CEO/CFO | mean | 3 | open | 3 | 66.7 | 3.27 | 1.93 | 9.82 | 4.15 | 0.79 | -0.04 | 7.93 |
| 1359 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_mean_3d_open | Large cap (≥1B) CEO/CFO | mean | 3 | open | 3 | 66.7 | 3.27 | 1.93 | 9.82 | 4.15 | 0.79 | -0.04 | 7.93 |
| 1360 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_mean_5d_open | Mid cap (1B–10B) Value ≥100k | mean | 5 | open | 4 | 75.0 | 3.25 | 1.96 | 13.0 | 5.51 | 0.59 | -1.86 | 10.93 |
| 1361 | 4 | 82.51 | CEO + Director (combo) — hold ret_mean_5d_news | CEO + Director (combo) | mean | 5 | news | 1 | 100.0 | 3.24 | 3.24 | 3.24 | nan | nan | 3.24 | 3.24 |
| 1362 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_mean_5d_news | Small cap (≤1B) CEO/CFO | mean | 5 | news | 1 | 100.0 | 3.24 | 3.24 | 3.24 | nan | nan | 3.24 | 3.24 |
| 1363 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_mean_2d_news | CEO/CFO + Value ≥100k | mean | 2 | news | 3 | 66.7 | 3.23 | 5.35 | 9.69 | 5.57 | 0.58 | -3.09 | 7.43 |
| 1364 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_mean_2d_news | Large cap (≥750M) CEO/CFO | mean | 2 | news | 3 | 66.7 | 3.23 | 5.35 | 9.69 | 5.57 | 0.58 | -3.09 | 7.43 |
| 1365 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_mean_2d_news | Large cap (≥1B) CEO/CFO | mean | 2 | news | 3 | 66.7 | 3.23 | 5.35 | 9.69 | 5.57 | 0.58 | -3.09 | 7.43 |
| 1366 | 10 | 66.41 | CEO/CFO — hold ret_mean_2d_news | CEO/CFO | mean | 2 | news | 4 | 75.0 | 3.2 | 4.24 | 12.82 | 4.55 | 0.7 | -3.09 | 7.43 |
| 1367 | 11 | 66.41 | Officer/President — hold ret_mean_2d_news | Officer/President | mean | 2 | news | 4 | 75.0 | 3.2 | 4.24 | 12.82 | 4.55 | 0.7 | -3.09 | 7.43 |
| 1368 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_mean_2d_news | Large cap (≥250M) CEO/CFO | mean | 2 | news | 4 | 75.0 | 3.2 | 4.24 | 12.82 | 4.55 | 0.7 | -3.09 | 7.43 |
| 1369 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_mean_2d_news | Large cap (≥500M) CEO/CFO | mean | 2 | news | 4 | 75.0 | 3.2 | 4.24 | 12.82 | 4.55 | 0.7 | -3.09 | 7.43 |
| 1370 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_mean_10d_open | Multiple buys (n≥2) | mean | 10 | open | 3 | 100.0 | 3.2 | 2.42 | 9.59 | 3.46 | 0.92 | 0.19 | 6.98 |
| 1371 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_mean_60d_news | Mid cap (1B–10B) Value ≥100k | mean | 60 | news | 4 | 100.0 | 3.2 | 3.35 | 12.8 | 1.99 | 1.61 | 0.89 | 5.21 |
| 1372 | 15 | 62.43 | Price > MA50 — hold ret_mean_2d_news | Price > MA50 | mean | 2 | news | 5 | 80.0 | 3.17 | 2.67 | 15.85 | 3.37 | 0.94 | -1.31 | 7.43 |
| 1373 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_mean_7d_open | Large cap (≥3B) CEO/CFO | mean | 7 | open | 1 | 100.0 | 3.15 | 3.15 | 3.15 | nan | nan | 3.15 | 3.15 |
| 1374 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_mean_7d_open | Large cap (≥5B) CEO/CFO | mean | 7 | open | 1 | 100.0 | 3.15 | 3.15 | 3.15 | nan | nan | 3.15 | 3.15 |
| 1375 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_mean_7d_open | Large cap (≥10B) CEO/CFO | mean | 7 | open | 1 | 100.0 | 3.15 | 3.15 | 3.15 | nan | nan | 3.15 | 3.15 |
| 1376 | 4 | 82.51 | CEO + Director (combo) — hold ret_mean_2d_news | CEO + Director (combo) | mean | 2 | news | 1 | 100.0 | 3.13 | 3.13 | 3.13 | nan | nan | 3.13 | 3.13 |
| 1377 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_mean_2d_news | Small cap (≤1B) CEO/CFO | mean | 2 | news | 1 | 100.0 | 3.13 | 3.13 | 3.13 | nan | nan | 3.13 | 3.13 |
| 1378 | 14 | 65.45 | Price > MA200 — hold ret_mean_3d_news | Price > MA200 | mean | 3 | news | 4 | 75.0 | 3.13 | 2.16 | 12.52 | 4.61 | 0.68 | -1.26 | 9.47 |
| 1379 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_mean_60d_open | Mid cap (1B–10B) Value ≥100k | mean | 60 | open | 4 | 100.0 | 3.12 | 3.35 | 12.47 | 1.29 | 2.42 | 1.39 | 4.39 |
| 1380 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_high_1d_news | Large cap (≥2B) CEO/CFO | high | 1 | news | 2 | 50.0 | 3.09 | 3.09 | 6.18 | 7.88 | 0.39 | -2.48 | 8.66 |
| 1381 | 15 | 62.43 | Price > MA50 — hold ret_mean_14d_open | Price > MA50 | mean | 14 | open | 5 | 60.0 | 3.09 | 1.69 | 15.46 | 5.82 | 0.53 | -2.1 | 12.89 |
| 1382 | 10 | 66.41 | CEO/CFO — hold ret_mean_2d_open | CEO/CFO | mean | 2 | open | 4 | 75.0 | 3.07 | 3.37 | 12.28 | 2.67 | 1.15 | -0.38 | 5.92 |
| 1383 | 11 | 66.41 | Officer/President — hold ret_mean_2d_open | Officer/President | mean | 2 | open | 4 | 75.0 | 3.07 | 3.37 | 12.28 | 2.67 | 1.15 | -0.38 | 5.92 |
| 1384 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_mean_2d_open | Large cap (≥250M) CEO/CFO | mean | 2 | open | 4 | 75.0 | 3.07 | 3.37 | 12.28 | 2.67 | 1.15 | -0.38 | 5.92 |
| 1385 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_mean_2d_open | Large cap (≥500M) CEO/CFO | mean | 2 | open | 4 | 75.0 | 3.07 | 3.37 | 12.28 | 2.67 | 1.15 | -0.38 | 5.92 |
| 1386 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_mean_1d_open | CEO only + Value ≥100k | mean | 1 | open | 2 | 100.0 | 3.06 | 3.06 | 6.12 | 0.72 | 4.24 | 2.55 | 3.57 |
| 1387 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_mean_1d_open | Price > MA50 + CEO/CFO | mean | 1 | open | 2 | 100.0 | 3.06 | 3.06 | 6.12 | 0.72 | 4.24 | 2.55 | 3.57 |
| 1388 | 14 | 65.45 | Price > MA200 — hold ret_mean_5d_open | Price > MA200 | mean | 5 | open | 4 | 75.0 | 3.06 | 1.59 | 12.26 | 5.64 | 0.54 | -1.86 | 10.93 |
| 1389 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_high_1d_open | Large cap (≥2B) CEO/CFO | high | 1 | open | 2 | 100.0 | 3.04 | 3.04 | 6.09 | 3.95 | 0.77 | 0.25 | 5.84 |
| 1390 | 22 | 53.36 | RSI overbought (>70) — hold ret_mean_30d_news | RSI overbought (>70) | mean | 30 | news | 2 | 100.0 | 3.04 | 3.04 | 6.09 | 1.29 | 2.35 | 2.13 | 3.96 |
| 1391 | 6 | 77.62 | CEO only — hold ret_mean_1d_open | CEO only | mean | 1 | open | 3 | 100.0 | 3.03 | 2.98 | 9.1 | 0.51 | 5.92 | 2.55 | 3.57 |
| 1392 | 26 | 50.0 | Qty ≥50k shares — hold ret_mean_7d_open | Qty ≥50k shares | mean | 7 | open | 2 | 50.0 | 3.02 | 3.02 | 6.04 | 13.25 | 0.23 | -6.35 | 12.39 |
| 1393 | 27 | 50.0 | Value ≥1M — hold ret_mean_7d_open | Value ≥1M | mean | 7 | open | 2 | 50.0 | 3.02 | 3.02 | 6.04 | 13.25 | 0.23 | -6.35 | 12.39 |
| 1394 | 22 | 53.36 | RSI overbought (>70) — hold ret_mean_90d_open | RSI overbought (>70) | mean | 90 | open | 2 | 50.0 | 3.0 | 3.0 | 6.0 | 5.35 | 0.56 | -0.78 | 6.78 |
| 1395 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_mean_60d_open | CEO only + Value ≥500k | mean | 60 | open | 1 | 100.0 | 2.99 | 2.99 | 2.99 | nan | nan | 2.99 | 2.99 |
| 1396 | 1 | 100.0 | CEO only + Position +10% — hold ret_mean_60d_open | CEO only + Position +10% | mean | 60 | open | 1 | 100.0 | 2.99 | 2.99 | 2.99 | nan | nan | 2.99 | 2.99 |
| 1397 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_mean_60d_open | Near 52w high + CEO/CFO | mean | 60 | open | 1 | 100.0 | 2.99 | 2.99 | 2.99 | nan | nan | 2.99 | 2.99 |
| 1398 | 4 | 82.51 | CEO + Director (combo) — hold ret_mean_1d_open | CEO + Director (combo) | mean | 1 | open | 1 | 100.0 | 2.98 | 2.98 | 2.98 | nan | nan | 2.98 | 2.98 |
| 1399 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_mean_1d_open | Small cap (≤1B) CEO/CFO | mean | 1 | open | 1 | 100.0 | 2.98 | 2.98 | 2.98 | nan | nan | 2.98 | 2.98 |
| 1400 | 53 | 0.0 | Qty ≥100k shares — hold ret_mean_3d_news | Qty ≥100k shares | mean | 3 | news | 1 | 100.0 | 2.98 | 2.98 | 2.98 | nan | nan | 2.98 | 2.98 |
| 1401 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_mean_3d_news | Small cap (≤1B) Value ≥100k | mean | 3 | news | 1 | 100.0 | 2.98 | 2.98 | 2.98 | nan | nan | 2.98 | 2.98 |
| 1402 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_high_1d_news | Multiple buys (n≥2) | high | 1 | news | 3 | 66.7 | 2.92 | 3.63 | 8.77 | 5.09 | 0.57 | -2.48 | 7.62 |
| 1403 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_high_1d_news | Mid cap (1B–10B) Value ≥100k | high | 1 | news | 4 | 75.0 | 2.92 | 2.08 | 11.7 | 5.24 | 0.56 | -2.48 | 10.02 |
| 1404 | 30 | 48.32 | Value ≥100k — hold ret_mean_7d_news | Value ≥100k | mean | 7 | news | 6 | 50.0 | 2.91 | 2.04 | 17.48 | 6.86 | 0.42 | -5.66 | 13.99 |
| 1405 | 15 | 62.43 | Price > MA50 — hold ret_mean_5d_open | Price > MA50 | mean | 5 | open | 5 | 80.0 | 2.9 | 2.23 | 14.49 | 4.89 | 0.59 | -1.86 | 10.93 |
| 1406 | 22 | 53.36 | RSI overbought (>70) — hold ret_mean_60d_open | RSI overbought (>70) | mean | 60 | open | 2 | 100.0 | 2.89 | 2.89 | 5.78 | 2.12 | 1.36 | 1.39 | 4.39 |
| 1407 | 22 | 53.36 | RSI overbought (>70) — hold ret_high_3d_open | RSI overbought (>70) | high | 3 | open | 2 | 100.0 | 2.87 | 2.87 | 5.74 | 3.38 | 0.85 | 0.48 | 5.26 |
| 1408 | 14 | 65.45 | Price > MA200 — hold ret_mean_60d_open | Price > MA200 | mean | 60 | open | 4 | 100.0 | 2.85 | 2.81 | 11.4 | 1.23 | 2.31 | 1.39 | 4.39 |
| 1409 | 30 | 48.32 | Value ≥100k — hold ret_mean_5d_news | Value ≥100k | mean | 5 | news | 6 | 50.0 | 2.84 | 1.46 | 17.07 | 5.57 | 0.51 | -1.96 | 12.51 |
| 1410 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_high_1d_open | Mid cap (1B–10B) Value ≥100k | high | 1 | open | 4 | 100.0 | 2.81 | 1.26 | 11.25 | 3.86 | 0.73 | 0.25 | 8.48 |
| 1411 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_mean_2d_open | Mid cap (1B–10B) CEO/CFO | mean | 2 | open | 2 | 50.0 | 2.77 | 2.77 | 5.54 | 4.45 | 0.62 | -0.38 | 5.92 |
| 1412 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_mean_14d_news | Multiple buys (n≥2) | mean | 14 | news | 3 | 66.7 | 2.76 | 1.32 | 8.27 | 4.11 | 0.67 | -0.44 | 7.39 |
| 1413 | 30 | 48.32 | Value ≥100k — hold ret_mean_2d_news | Value ≥100k | mean | 2 | news | 6 | 66.7 | 2.73 | 4.0 | 16.38 | 4.15 | 0.66 | -3.09 | 7.43 |
| 1414 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_mean_2d_open | CEO/CFO + Value ≥100k | mean | 2 | open | 3 | 66.7 | 2.72 | 2.62 | 8.16 | 3.15 | 0.86 | -0.38 | 5.92 |
| 1415 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_mean_2d_open | Large cap (≥750M) CEO/CFO | mean | 2 | open | 3 | 66.7 | 2.72 | 2.62 | 8.16 | 3.15 | 0.86 | -0.38 | 5.92 |
| 1416 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_mean_2d_open | Large cap (≥1B) CEO/CFO | mean | 2 | open | 3 | 66.7 | 2.72 | 2.62 | 8.16 | 3.15 | 0.86 | -0.38 | 5.92 |
| 1417 | 30 | 48.32 | Value ≥100k — hold ret_mean_3d_news | Value ≥100k | mean | 3 | news | 6 | 66.7 | 2.72 | 3.1 | 16.29 | 4.37 | 0.62 | -2.76 | 9.47 |
| 1418 | 22 | 53.36 | RSI overbought (>70) — hold ret_high_2d_open | RSI overbought (>70) | high | 2 | open | 2 | 100.0 | 2.68 | 2.67 | 5.35 | 3.1 | 0.86 | 0.48 | 4.87 |
| 1419 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_mean_60d_news | Mid cap (1B–10B) CEO/CFO | mean | 60 | news | 2 | 100.0 | 2.68 | 2.67 | 5.35 | 2.52 | 1.06 | 0.89 | 4.46 |
| 1420 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_mean_2d_open | Large cap (≥3B) CEO/CFO | mean | 2 | open | 1 | 100.0 | 2.62 | 2.62 | 2.62 | nan | nan | 2.62 | 2.62 |
| 1421 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_mean_2d_open | Large cap (≥5B) CEO/CFO | mean | 2 | open | 1 | 100.0 | 2.62 | 2.62 | 2.62 | nan | nan | 2.62 | 2.62 |
| 1422 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_mean_2d_open | Large cap (≥10B) CEO/CFO | mean | 2 | open | 1 | 100.0 | 2.62 | 2.62 | 2.62 | nan | nan | 2.62 | 2.62 |
| 1423 | 14 | 65.45 | Price > MA200 — hold ret_mean_2d_news | Price > MA200 | mean | 2 | news | 4 | 75.0 | 2.62 | 2.19 | 10.5 | 3.62 | 0.72 | -1.31 | 7.43 |
| 1424 | 21 | 53.67 | Qty ≥5k shares — hold ret_mean_7d_news | Qty ≥5k shares | mean | 7 | news | 6 | 50.0 | 2.62 | 1.73 | 15.73 | 6.74 | 0.39 | -5.66 | 13.99 |
| 1425 | 20 | 53.67 | Qty ≥10k shares — hold ret_mean_7d_news | Qty ≥10k shares | mean | 7 | news | 6 | 50.0 | 2.62 | 1.73 | 15.73 | 6.74 | 0.39 | -5.66 | 13.99 |
| 1426 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_mean_7d_open | Large cap (≥2B) CEO/CFO | mean | 7 | open | 2 | 100.0 | 2.62 | 2.62 | 5.24 | 0.75 | 3.5 | 2.09 | 3.15 |
| 1427 | 21 | 53.67 | Qty ≥5k shares — hold ret_mean_7d_open | Qty ≥5k shares | mean | 7 | open | 6 | 66.7 | 2.6 | 2.98 | 15.57 | 6.35 | 0.41 | -6.35 | 12.39 |
| 1428 | 20 | 53.67 | Qty ≥10k shares — hold ret_mean_7d_open | Qty ≥10k shares | mean | 7 | open | 6 | 66.7 | 2.6 | 2.98 | 15.57 | 6.35 | 0.41 | -6.35 | 12.39 |
| 1429 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_mean_7d_news | Large cap (≥2B) CEO/CFO | mean | 7 | news | 2 | 50.0 | 2.6 | 2.6 | 5.21 | 4.65 | 0.56 | -0.68 | 5.89 |
| 1430 | 21 | 53.67 | Qty ≥5k shares — hold ret_mean_5d_news | Qty ≥5k shares | mean | 5 | news | 6 | 50.0 | 2.56 | 1.08 | 15.36 | 5.49 | 0.47 | -1.96 | 12.51 |
| 1431 | 20 | 53.67 | Qty ≥10k shares — hold ret_mean_5d_news | Qty ≥10k shares | mean | 5 | news | 6 | 50.0 | 2.56 | 1.08 | 15.36 | 5.49 | 0.47 | -1.96 | 12.51 |
| 1432 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_mean_1d_open | Large cap (≥3B) CEO/CFO | mean | 1 | open | 1 | 100.0 | 2.55 | 2.55 | 2.55 | nan | nan | 2.55 | 2.55 |
| 1433 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_mean_1d_open | Large cap (≥5B) CEO/CFO | mean | 1 | open | 1 | 100.0 | 2.55 | 2.55 | 2.55 | nan | nan | 2.55 | 2.55 |
| 1434 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_mean_1d_open | Large cap (≥10B) CEO/CFO | mean | 1 | open | 1 | 100.0 | 2.55 | 2.55 | 2.55 | nan | nan | 2.55 | 2.55 |
| 1435 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_mean_1d_news | Far 52w high + Value ≥100k | mean | 1 | news | 3 | 66.7 | 2.54 | 5.28 | 7.61 | 5.32 | 0.48 | -3.6 | 5.93 |
| 1436 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_mean_2d_news | Far 52w high + Value ≥100k | mean | 2 | news | 3 | 66.7 | 2.53 | 5.33 | 7.59 | 4.87 | 0.52 | -3.09 | 5.35 |
| 1437 | 21 | 53.67 | Qty ≥5k shares — hold ret_mean_5d_open | Qty ≥5k shares | mean | 5 | open | 6 | 66.7 | 2.53 | 1.96 | 15.16 | 4.84 | 0.52 | -2.07 | 10.93 |
| 1438 | 20 | 53.67 | Qty ≥10k shares — hold ret_mean_5d_open | Qty ≥10k shares | mean | 5 | open | 6 | 66.7 | 2.53 | 1.96 | 15.16 | 4.84 | 0.52 | -2.07 | 10.93 |
| 1439 | 49 | 32.78 | CFO only — hold ret_high_2d_open | CFO only | high | 2 | open | 1 | 100.0 | 2.52 | 2.52 | 2.52 | nan | nan | 2.52 | 2.52 |
| 1440 | 48 | 32.78 | CFO + Director (combo) — hold ret_high_2d_open | CFO + Director (combo) | high | 2 | open | 1 | 100.0 | 2.52 | 2.52 | 2.52 | nan | nan | 2.52 | 2.52 |
| 1441 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_high_2d_open | CFO only + Value ≥50k | high | 2 | open | 1 | 100.0 | 2.52 | 2.52 | 2.52 | nan | nan | 2.52 | 2.52 |
| 1442 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_high_2d_open | CFO only + Value ≥100k | high | 2 | open | 1 | 100.0 | 2.52 | 2.52 | 2.52 | nan | nan | 2.52 | 2.52 |
| 1443 | 47 | 32.78 | CFO only + Position +10% — hold ret_high_2d_open | CFO only + Position +10% | high | 2 | open | 1 | 100.0 | 2.52 | 2.52 | 2.52 | nan | nan | 2.52 | 2.52 |
| 1444 | 46 | 32.78 | CFO only + Position +20% — hold ret_high_2d_open | CFO only + Position +20% | high | 2 | open | 1 | 100.0 | 2.52 | 2.52 | 2.52 | nan | nan | 2.52 | 2.52 |
| 1445 | 44 | 32.78 | RSI oversold (<30) — hold ret_high_2d_open | RSI oversold (<30) | high | 2 | open | 1 | 100.0 | 2.52 | 2.52 | 2.52 | nan | nan | 2.52 | 2.52 |
| 1446 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_high_2d_open | RSI oversold + CEO/CFO | high | 2 | open | 1 | 100.0 | 2.52 | 2.52 | 2.52 | nan | nan | 2.52 | 2.52 |
| 1447 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_high_2d_open | RSI oversold + Value ≥100k | high | 2 | open | 1 | 100.0 | 2.52 | 2.52 | 2.52 | nan | nan | 2.52 | 2.52 |
| 1448 | 21 | 53.67 | Qty ≥5k shares — hold ret_mean_3d_news | Qty ≥5k shares | mean | 3 | news | 6 | 66.7 | 2.49 | 3.1 | 14.92 | 4.28 | 0.58 | -2.76 | 9.47 |
| 1449 | 20 | 53.67 | Qty ≥10k shares — hold ret_mean_3d_news | Qty ≥10k shares | mean | 3 | news | 6 | 66.7 | 2.49 | 3.1 | 14.92 | 4.28 | 0.58 | -2.76 | 9.47 |
| 1450 | 21 | 53.67 | Qty ≥5k shares — hold ret_mean_3d_open | Qty ≥5k shares | mean | 3 | open | 6 | 66.7 | 2.45 | 2.29 | 14.72 | 3.45 | 0.71 | -2.03 | 7.93 |
| 1451 | 20 | 53.67 | Qty ≥10k shares — hold ret_mean_3d_open | Qty ≥10k shares | mean | 3 | open | 6 | 66.7 | 2.45 | 2.29 | 14.72 | 3.45 | 0.71 | -2.03 | 7.93 |
| 1452 | 49 | 32.78 | CFO only — hold ret_mean_30d_news | CFO only | mean | 30 | news | 1 | 100.0 | 2.45 | 2.45 | 2.45 | nan | nan | 2.45 | 2.45 |
| 1453 | 48 | 32.78 | CFO + Director (combo) — hold ret_mean_30d_news | CFO + Director (combo) | mean | 30 | news | 1 | 100.0 | 2.45 | 2.45 | 2.45 | nan | nan | 2.45 | 2.45 |
| 1454 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_mean_30d_news | CFO only + Value ≥50k | mean | 30 | news | 1 | 100.0 | 2.45 | 2.45 | 2.45 | nan | nan | 2.45 | 2.45 |
| 1455 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_mean_30d_news | CFO only + Value ≥100k | mean | 30 | news | 1 | 100.0 | 2.45 | 2.45 | 2.45 | nan | nan | 2.45 | 2.45 |
| 1456 | 47 | 32.78 | CFO only + Position +10% — hold ret_mean_30d_news | CFO only + Position +10% | mean | 30 | news | 1 | 100.0 | 2.45 | 2.45 | 2.45 | nan | nan | 2.45 | 2.45 |
| 1457 | 46 | 32.78 | CFO only + Position +20% — hold ret_mean_30d_news | CFO only + Position +20% | mean | 30 | news | 1 | 100.0 | 2.45 | 2.45 | 2.45 | nan | nan | 2.45 | 2.45 |
| 1458 | 44 | 32.78 | RSI oversold (<30) — hold ret_mean_30d_news | RSI oversold (<30) | mean | 30 | news | 1 | 100.0 | 2.45 | 2.45 | 2.45 | nan | nan | 2.45 | 2.45 |
| 1459 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_mean_30d_news | RSI oversold + CEO/CFO | mean | 30 | news | 1 | 100.0 | 2.45 | 2.45 | 2.45 | nan | nan | 2.45 | 2.45 |
| 1460 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_mean_30d_news | RSI oversold + Value ≥100k | mean | 30 | news | 1 | 100.0 | 2.45 | 2.45 | 2.45 | nan | nan | 2.45 | 2.45 |
| 1461 | 15 | 62.43 | Price > MA50 — hold ret_mean_1d_news | Price > MA50 | mean | 1 | news | 5 | 80.0 | 2.43 | 1.89 | 12.13 | 2.8 | 0.87 | -1.41 | 5.28 |
| 1462 | 49 | 32.78 | CFO only — hold ret_mean_10d_open | CFO only | mean | 10 | open | 1 | 100.0 | 2.42 | 2.42 | 2.42 | nan | nan | 2.42 | 2.42 |
| 1463 | 48 | 32.78 | CFO + Director (combo) — hold ret_mean_10d_open | CFO + Director (combo) | mean | 10 | open | 1 | 100.0 | 2.42 | 2.42 | 2.42 | nan | nan | 2.42 | 2.42 |
| 1464 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_mean_10d_open | CFO only + Value ≥50k | mean | 10 | open | 1 | 100.0 | 2.42 | 2.42 | 2.42 | nan | nan | 2.42 | 2.42 |
| 1465 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_mean_10d_open | CFO only + Value ≥100k | mean | 10 | open | 1 | 100.0 | 2.42 | 2.42 | 2.42 | nan | nan | 2.42 | 2.42 |
| 1466 | 47 | 32.78 | CFO only + Position +10% — hold ret_mean_10d_open | CFO only + Position +10% | mean | 10 | open | 1 | 100.0 | 2.42 | 2.42 | 2.42 | nan | nan | 2.42 | 2.42 |
| 1467 | 46 | 32.78 | CFO only + Position +20% — hold ret_mean_10d_open | CFO only + Position +20% | mean | 10 | open | 1 | 100.0 | 2.42 | 2.42 | 2.42 | nan | nan | 2.42 | 2.42 |
| 1468 | 44 | 32.78 | RSI oversold (<30) — hold ret_mean_10d_open | RSI oversold (<30) | mean | 10 | open | 1 | 100.0 | 2.42 | 2.42 | 2.42 | nan | nan | 2.42 | 2.42 |
| 1469 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_mean_10d_open | RSI oversold + CEO/CFO | mean | 10 | open | 1 | 100.0 | 2.42 | 2.42 | 2.42 | nan | nan | 2.42 | 2.42 |
| 1470 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_mean_10d_open | RSI oversold + Value ≥100k | mean | 10 | open | 1 | 100.0 | 2.42 | 2.42 | 2.42 | nan | nan | 2.42 | 2.42 |
| 1471 | 21 | 53.67 | Qty ≥5k shares — hold ret_mean_2d_news | Qty ≥5k shares | mean | 2 | news | 6 | 66.7 | 2.36 | 2.9 | 14.16 | 3.96 | 0.6 | -3.09 | 7.43 |
| 1472 | 20 | 53.67 | Qty ≥10k shares — hold ret_mean_2d_news | Qty ≥10k shares | mean | 2 | news | 6 | 66.7 | 2.36 | 2.9 | 14.16 | 3.96 | 0.6 | -3.09 | 7.43 |
| 1473 | 31 | 47.75 | Value ≥50k — hold ret_mean_7d_news | Value ≥50k | mean | 7 | news | 9 | 44.4 | 2.36 | -0.15 | 21.21 | 5.63 | 0.42 | -5.66 | 13.99 |
| 1474 | 14 | 65.45 | Price > MA200 — hold ret_mean_3d_open | Price > MA200 | mean | 3 | open | 4 | 75.0 | 2.34 | 1.73 | 9.36 | 4.16 | 0.56 | -2.03 | 7.93 |
| 1475 | 21 | 53.67 | Qty ≥5k shares — hold ret_mean_2d_open | Qty ≥5k shares | mean | 2 | open | 6 | 66.7 | 2.32 | 2.96 | 13.95 | 3.1 | 0.75 | -2.08 | 5.92 |
| 1476 | 20 | 53.67 | Qty ≥10k shares — hold ret_mean_2d_open | Qty ≥10k shares | mean | 2 | open | 6 | 66.7 | 2.32 | 2.96 | 13.95 | 3.1 | 0.75 | -2.08 | 5.92 |
| 1477 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_mean_7d_open | Multiple buys (n≥2) | mean | 7 | open | 3 | 66.7 | 2.32 | 2.09 | 6.97 | 2.71 | 0.86 | -0.26 | 5.14 |
| 1478 | 22 | 53.36 | RSI overbought (>70) — hold ret_mean_14d_news | RSI overbought (>70) | mean | 14 | news | 2 | 100.0 | 2.32 | 2.31 | 4.63 | 2.4 | 0.97 | 0.62 | 4.01 |
| 1479 | 32 | 44.63 | Position +10% — hold ret_mean_3d_news | Position +10% | mean | 3 | news | 6 | 66.7 | 2.28 | 2.1 | 13.68 | 4.17 | 0.55 | -2.76 | 9.47 |
| 1480 | 31 | 47.75 | Value ≥50k — hold ret_mean_2d_news | Value ≥50k | mean | 2 | news | 9 | 66.7 | 2.27 | 2.67 | 20.4 | 3.47 | 0.65 | -3.09 | 7.43 |
| 1481 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_mean_2d_open | Far 52w high + Value ≥100k | mean | 2 | open | 3 | 66.7 | 2.27 | 2.62 | 6.8 | 2.49 | 0.91 | -0.38 | 4.56 |
| 1482 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_mean_1d_open | Far 52w high + Value ≥100k | mean | 1 | open | 3 | 66.7 | 2.26 | 2.55 | 6.79 | 3.04 | 0.74 | -0.91 | 5.15 |
| 1483 | 31 | 47.75 | Value ≥50k — hold ret_mean_3d_news | Value ≥50k | mean | 3 | news | 9 | 66.7 | 2.26 | 2.98 | 20.33 | 3.64 | 0.62 | -2.76 | 9.47 |
| 1484 | 15 | 62.43 | Price > MA50 — hold ret_mean_3d_open | Price > MA50 | mean | 3 | open | 5 | 80.0 | 2.26 | 1.93 | 11.29 | 3.61 | 0.63 | -2.03 | 7.93 |
| 1485 | 30 | 48.32 | Value ≥100k — hold ret_mean_7d_open | Value ≥100k | mean | 7 | open | 6 | 66.7 | 2.26 | 2.62 | 13.58 | 6.24 | 0.36 | -6.35 | 12.39 |
| 1486 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_mean_1d_news | CEO/CFO + Value ≥100k | mean | 1 | news | 3 | 66.7 | 2.24 | 5.05 | 6.73 | 5.06 | 0.44 | -3.6 | 5.28 |
| 1487 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_mean_1d_news | Large cap (≥750M) CEO/CFO | mean | 1 | news | 3 | 66.7 | 2.24 | 5.05 | 6.73 | 5.06 | 0.44 | -3.6 | 5.28 |
| 1488 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_mean_1d_news | Large cap (≥1B) CEO/CFO | mean | 1 | news | 3 | 66.7 | 2.24 | 5.05 | 6.73 | 5.06 | 0.44 | -3.6 | 5.28 |
| 1489 | 32 | 44.63 | Position +10% — hold ret_mean_3d_open | Position +10% | mean | 3 | open | 6 | 66.7 | 2.24 | 1.73 | 13.47 | 2.99 | 0.75 | -0.24 | 7.93 |
| 1490 | 37 | 35.58 | Director only + Value ≥100k — hold ret_mean_2d_news | Director only + Value ≥100k | mean | 2 | news | 3 | 66.7 | 2.23 | 2.67 | 6.69 | 3.34 | 0.67 | -1.31 | 5.33 |
| 1491 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_mean_5d_open | Large cap (≥3B) CEO/CFO | mean | 5 | open | 1 | 100.0 | 2.23 | 2.23 | 2.23 | nan | nan | 2.23 | 2.23 |
| 1492 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_mean_5d_open | Large cap (≥5B) CEO/CFO | mean | 5 | open | 1 | 100.0 | 2.23 | 2.23 | 2.23 | nan | nan | 2.23 | 2.23 |
| 1493 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_mean_5d_open | Large cap (≥10B) CEO/CFO | mean | 5 | open | 1 | 100.0 | 2.23 | 2.23 | 2.23 | nan | nan | 2.23 | 2.23 |
| 1494 | 40 | 33.74 | Director only + Position +10% — hold ret_mean_2d_news | Director only + Position +10% | mean | 2 | news | 4 | 75.0 | 2.22 | 2.04 | 8.89 | 2.45 | 0.91 | -0.53 | 5.33 |
| 1495 | 53 | 0.0 | Qty ≥100k shares — hold ret_mean_3d_open | Qty ≥100k shares | mean | 3 | open | 1 | 100.0 | 2.22 | 2.22 | 2.22 | nan | nan | 2.22 | 2.22 |
| 1496 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_mean_3d_open | Small cap (≤1B) Value ≥100k | mean | 3 | open | 1 | 100.0 | 2.22 | 2.22 | 2.22 | nan | nan | 2.22 | 2.22 |
| 1497 | 28 | 48.48 | Tutti — hold ret_mean_2d_news | Tutti | mean | 2 | news | 10 | 70.0 | 2.21 | 2.19 | 22.11 | 3.28 | 0.67 | -3.09 | 7.43 |
| 1498 | 22 | 53.36 | RSI overbought (>70) — hold ret_mean_30d_open | RSI overbought (>70) | mean | 30 | open | 2 | 100.0 | 2.21 | 2.21 | 4.42 | 1.24 | 1.78 | 1.33 | 3.09 |
| 1499 | 32 | 44.63 | Position +10% — hold ret_mean_2d_news | Position +10% | mean | 2 | news | 6 | 66.7 | 2.2 | 2.04 | 13.23 | 3.83 | 0.58 | -3.09 | 7.43 |
| 1500 | 30 | 48.32 | Value ≥100k — hold ret_mean_1d_news | Value ≥100k | mean | 1 | news | 6 | 66.7 | 2.19 | 3.47 | 13.14 | 3.96 | 0.55 | -3.6 | 5.93 |
| 1501 | 30 | 48.32 | Value ≥100k — hold ret_mean_5d_open | Value ≥100k | mean | 5 | open | 6 | 66.7 | 2.19 | 1.5 | 13.16 | 4.77 | 0.46 | -2.07 | 10.93 |
| 1502 | 10 | 66.41 | CEO/CFO — hold ret_mean_1d_news | CEO/CFO | mean | 1 | news | 4 | 75.0 | 2.18 | 3.52 | 8.73 | 4.13 | 0.53 | -3.6 | 5.28 |
| 1503 | 11 | 66.41 | Officer/President — hold ret_mean_1d_news | Officer/President | mean | 1 | news | 4 | 75.0 | 2.18 | 3.52 | 8.73 | 4.13 | 0.53 | -3.6 | 5.28 |
| 1504 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_mean_1d_news | Large cap (≥250M) CEO/CFO | mean | 1 | news | 4 | 75.0 | 2.18 | 3.52 | 8.73 | 4.13 | 0.53 | -3.6 | 5.28 |
| 1505 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_mean_1d_news | Large cap (≥500M) CEO/CFO | mean | 1 | news | 4 | 75.0 | 2.18 | 3.52 | 8.73 | 4.13 | 0.53 | -3.6 | 5.28 |
| 1506 | 31 | 47.75 | Value ≥50k — hold ret_mean_5d_news | Value ≥50k | mean | 5 | news | 9 | 44.4 | 2.18 | -0.22 | 19.62 | 4.64 | 0.47 | -1.96 | 12.51 |
| 1507 | 32 | 44.63 | Position +10% — hold ret_mean_2d_open | Position +10% | mean | 2 | open | 6 | 66.7 | 2.17 | 1.61 | 13.02 | 2.57 | 0.84 | -0.38 | 5.92 |
| 1508 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_mean_2d_news | Mid cap (1B–10B) CEO/CFO | mean | 2 | news | 2 | 50.0 | 2.17 | 2.17 | 4.34 | 7.44 | 0.29 | -3.09 | 7.43 |
| 1509 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_mean_3d_news | Mid cap (1B–10B) Value ≥100k | mean | 3 | news | 4 | 50.0 | 2.17 | 0.98 | 8.67 | 5.49 | 0.39 | -2.76 | 9.47 |
| 1510 | 22 | 53.36 | RSI overbought (>70) — hold ret_mean_10d_news | RSI overbought (>70) | mean | 10 | news | 2 | 50.0 | 2.16 | 2.16 | 4.33 | 3.33 | 0.65 | -0.19 | 4.52 |
| 1511 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_low_1d_news | Large cap (≥3B) CEO/CFO | low | 1 | news | 1 | 100.0 | 2.15 | 2.15 | 2.15 | nan | nan | 2.15 | 2.15 |
| 1512 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_low_1d_news | Large cap (≥5B) CEO/CFO | low | 1 | news | 1 | 100.0 | 2.15 | 2.15 | 2.15 | nan | nan | 2.15 | 2.15 |
| 1513 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_low_1d_news | Large cap (≥10B) CEO/CFO | low | 1 | news | 1 | 100.0 | 2.15 | 2.15 | 2.15 | nan | nan | 2.15 | 2.15 |
| 1514 | 37 | 35.58 | Director only + Value ≥100k — hold ret_mean_1d_news | Director only + Value ≥100k | mean | 1 | news | 3 | 66.7 | 2.14 | 1.89 | 6.41 | 3.68 | 0.58 | -1.41 | 5.93 |
| 1515 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_low_2d_news | Large cap (≥3B) CEO/CFO | low | 2 | news | 1 | 100.0 | 2.14 | 2.14 | 2.14 | nan | nan | 2.14 | 2.14 |
| 1516 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_low_2d_news | Large cap (≥5B) CEO/CFO | low | 2 | news | 1 | 100.0 | 2.14 | 2.14 | 2.14 | nan | nan | 2.14 | 2.14 |
| 1517 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_low_2d_news | Large cap (≥10B) CEO/CFO | low | 2 | news | 1 | 100.0 | 2.14 | 2.14 | 2.14 | nan | nan | 2.14 | 2.14 |
| 1518 | 28 | 48.48 | Tutti — hold ret_mean_3d_news | Tutti | mean | 3 | news | 10 | 70.0 | 2.14 | 2.1 | 21.42 | 3.45 | 0.62 | -2.76 | 9.47 |
| 1519 | 35 | 40.48 | Value ≥500k — hold ret_mean_3d_news | Value ≥500k | mean | 3 | news | 4 | 50.0 | 2.11 | 0.86 | 8.43 | 5.48 | 0.38 | -2.76 | 9.47 |
| 1520 | 15 | 62.43 | Price > MA50 — hold ret_mean_60d_news | Price > MA50 | mean | 60 | news | 5 | 80.0 | 2.11 | 2.63 | 10.57 | 3.62 | 0.58 | -3.97 | 5.21 |
| 1521 | 35 | 40.48 | Value ≥500k — hold ret_mean_2d_news | Value ≥500k | mean | 2 | news | 4 | 50.0 | 2.09 | 2.01 | 8.36 | 5.08 | 0.41 | -3.09 | 7.43 |
| 1522 | 32 | 44.63 | Position +10% — hold ret_mean_5d_news | Position +10% | mean | 5 | news | 6 | 33.3 | 2.09 | -0.34 | 12.52 | 5.52 | 0.38 | -1.96 | 12.51 |
| 1523 | 49 | 32.78 | CFO only — hold ret_mean_7d_open | CFO only | mean | 7 | open | 1 | 100.0 | 2.09 | 2.09 | 2.09 | nan | nan | 2.09 | 2.09 |
| 1524 | 48 | 32.78 | CFO + Director (combo) — hold ret_mean_7d_open | CFO + Director (combo) | mean | 7 | open | 1 | 100.0 | 2.09 | 2.09 | 2.09 | nan | nan | 2.09 | 2.09 |
| 1525 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_mean_7d_open | CFO only + Value ≥50k | mean | 7 | open | 1 | 100.0 | 2.09 | 2.09 | 2.09 | nan | nan | 2.09 | 2.09 |
| 1526 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_mean_7d_open | CFO only + Value ≥100k | mean | 7 | open | 1 | 100.0 | 2.09 | 2.09 | 2.09 | nan | nan | 2.09 | 2.09 |
| 1527 | 47 | 32.78 | CFO only + Position +10% — hold ret_mean_7d_open | CFO only + Position +10% | mean | 7 | open | 1 | 100.0 | 2.09 | 2.09 | 2.09 | nan | nan | 2.09 | 2.09 |
| 1528 | 46 | 32.78 | CFO only + Position +20% — hold ret_mean_7d_open | CFO only + Position +20% | mean | 7 | open | 1 | 100.0 | 2.09 | 2.09 | 2.09 | nan | nan | 2.09 | 2.09 |
| 1529 | 44 | 32.78 | RSI oversold (<30) — hold ret_mean_7d_open | RSI oversold (<30) | mean | 7 | open | 1 | 100.0 | 2.09 | 2.09 | 2.09 | nan | nan | 2.09 | 2.09 |
| 1530 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_mean_7d_open | RSI oversold + CEO/CFO | mean | 7 | open | 1 | 100.0 | 2.09 | 2.09 | 2.09 | nan | nan | 2.09 | 2.09 |
| 1531 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_mean_7d_open | RSI oversold + Value ≥100k | mean | 7 | open | 1 | 100.0 | 2.09 | 2.09 | 2.09 | nan | nan | 2.09 | 2.09 |
| 1532 | 22 | 53.36 | RSI overbought (>70) — hold ret_high_1d_news | RSI overbought (>70) | high | 1 | news | 2 | 100.0 | 2.08 | 2.08 | 4.16 | 1.15 | 1.82 | 1.27 | 2.89 |
| 1533 | 30 | 48.32 | Value ≥100k — hold ret_mean_2d_open | Value ≥100k | mean | 2 | open | 6 | 66.7 | 2.07 | 2.21 | 12.45 | 2.99 | 0.69 | -2.08 | 5.92 |
| 1534 | 21 | 53.67 | Qty ≥5k shares — hold ret_mean_10d_news | Qty ≥5k shares | mean | 10 | news | 6 | 50.0 | 2.07 | 2.16 | 12.4 | 8.89 | 0.23 | -12.21 | 14.68 |
| 1535 | 20 | 53.67 | Qty ≥10k shares — hold ret_mean_10d_news | Qty ≥10k shares | mean | 10 | news | 6 | 50.0 | 2.07 | 2.16 | 12.4 | 8.89 | 0.23 | -12.21 | 14.68 |
| 1536 | 30 | 48.32 | Value ≥100k — hold ret_mean_3d_open | Value ≥100k | mean | 3 | open | 6 | 66.7 | 2.06 | 2.08 | 12.38 | 3.34 | 0.62 | -2.03 | 7.93 |
| 1537 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_mean_3d_open | Mid cap (1B–10B) Value ≥100k | mean | 3 | open | 4 | 50.0 | 2.06 | 1.17 | 8.23 | 4.31 | 0.48 | -2.03 | 7.93 |
| 1538 | 31 | 47.75 | Value ≥50k — hold ret_mean_7d_open | Value ≥50k | mean | 7 | open | 9 | 66.7 | 2.06 | 2.09 | 18.53 | 5.17 | 0.4 | -6.35 | 12.39 |
| 1539 | 10 | 66.41 | CEO/CFO — hold ret_mean_1d_open | CEO/CFO | mean | 1 | open | 4 | 75.0 | 2.05 | 2.76 | 8.19 | 2.02 | 1.02 | -0.91 | 3.57 |
| 1540 | 11 | 66.41 | Officer/President — hold ret_mean_1d_open | Officer/President | mean | 1 | open | 4 | 75.0 | 2.05 | 2.76 | 8.19 | 2.02 | 1.02 | -0.91 | 3.57 |
| 1541 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_mean_1d_open | Large cap (≥250M) CEO/CFO | mean | 1 | open | 4 | 75.0 | 2.05 | 2.76 | 8.19 | 2.02 | 1.02 | -0.91 | 3.57 |
| 1542 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_mean_1d_open | Large cap (≥500M) CEO/CFO | mean | 1 | open | 4 | 75.0 | 2.05 | 2.76 | 8.19 | 2.02 | 1.02 | -0.91 | 3.57 |
| 1543 | 32 | 44.63 | Position +10% — hold ret_mean_5d_open | Position +10% | mean | 5 | open | 6 | 50.0 | 2.05 | 0.28 | 12.32 | 4.67 | 0.44 | -2.07 | 10.93 |
| 1544 | 21 | 53.67 | Qty ≥5k shares — hold ret_mean_10d_open | Qty ≥5k shares | mean | 10 | open | 6 | 66.7 | 2.05 | 3.04 | 12.3 | 8.71 | 0.24 | -12.85 | 13.07 |
| 1545 | 20 | 53.67 | Qty ≥10k shares — hold ret_mean_10d_open | Qty ≥10k shares | mean | 10 | open | 6 | 66.7 | 2.05 | 3.04 | 12.3 | 8.71 | 0.24 | -12.85 | 13.07 |
| 1546 | 28 | 48.48 | Tutti — hold ret_mean_7d_news | Tutti | mean | 7 | news | 10 | 40.0 | 2.04 | -0.21 | 20.41 | 5.4 | 0.38 | -5.66 | 13.99 |
| 1547 | 35 | 40.48 | Value ≥500k — hold ret_mean_5d_news | Value ≥500k | mean | 5 | news | 4 | 25.0 | 2.03 | -1.22 | 8.11 | 7.0 | 0.29 | -1.96 | 12.51 |
| 1548 | 40 | 33.74 | Director only + Position +10% — hold ret_mean_1d_news | Director only + Position +10% | mean | 1 | news | 4 | 75.0 | 2.02 | 1.42 | 8.1 | 2.81 | 0.72 | -0.66 | 5.93 |
| 1549 | 35 | 40.48 | Value ≥500k — hold ret_mean_3d_open | Value ≥500k | mean | 3 | open | 4 | 50.0 | 2.02 | 1.09 | 8.08 | 4.31 | 0.47 | -2.03 | 7.93 |
| 1550 | 21 | 53.67 | Qty ≥5k shares — hold ret_mean_30d_open | Qty ≥5k shares | mean | 30 | open | 6 | 83.3 | 2.02 | 4.2 | 12.13 | 11.55 | 0.18 | -19.99 | 11.97 |
| 1551 | 20 | 53.67 | Qty ≥10k shares — hold ret_mean_30d_open | Qty ≥10k shares | mean | 30 | open | 6 | 83.3 | 2.02 | 4.2 | 12.13 | 11.55 | 0.18 | -19.99 | 11.97 |
| 1552 | 21 | 53.67 | Qty ≥5k shares — hold ret_mean_30d_news | Qty ≥5k shares | mean | 30 | news | 6 | 83.3 | 2.01 | 3.21 | 12.07 | 11.4 | 0.18 | -19.4 | 13.57 |
| 1553 | 20 | 53.67 | Qty ≥10k shares — hold ret_mean_30d_news | Qty ≥10k shares | mean | 30 | news | 6 | 83.3 | 2.01 | 3.21 | 12.07 | 11.4 | 0.18 | -19.4 | 13.57 |
| 1554 | 4 | 82.51 | CEO + Director (combo) — hold ret_mean_1d_news | CEO + Director (combo) | mean | 1 | news | 1 | 100.0 | 2.0 | 2.0 | 2.0 | nan | nan | 2.0 | 2.0 |
| 1555 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_mean_1d_news | Small cap (≤1B) CEO/CFO | mean | 1 | news | 1 | 100.0 | 2.0 | 2.0 | 2.0 | nan | nan | 2.0 | 2.0 |
| 1556 | 35 | 40.48 | Value ≥500k — hold ret_mean_2d_open | Value ≥500k | mean | 2 | open | 4 | 50.0 | 2.0 | 2.09 | 8.02 | 3.84 | 0.52 | -2.08 | 5.92 |
| 1557 | 15 | 62.43 | Price > MA50 — hold ret_mean_2d_open | Price > MA50 | mean | 2 | open | 5 | 80.0 | 2.0 | 1.81 | 9.98 | 2.85 | 0.7 | -2.08 | 5.92 |
| 1558 | 32 | 44.63 | Position +10% — hold ret_mean_7d_news | Position +10% | mean | 7 | news | 6 | 33.3 | 2.0 | -0.21 | 11.99 | 6.74 | 0.3 | -5.66 | 13.99 |
| 1559 | 28 | 48.48 | Tutti — hold ret_mean_5d_news | Tutti | mean | 5 | news | 10 | 50.0 | 1.97 | -0.09 | 19.66 | 4.42 | 0.44 | -1.96 | 12.51 |
| 1560 | 32 | 44.63 | Position +10% — hold ret_mean_7d_open | Position +10% | mean | 7 | open | 6 | 66.7 | 1.97 | 1.08 | 11.82 | 6.17 | 0.32 | -6.35 | 12.39 |
| 1561 | 22 | 53.36 | RSI overbought (>70) — hold ret_mean_7d_news | RSI overbought (>70) | mean | 7 | news | 2 | 50.0 | 1.97 | 1.97 | 3.94 | 3.93 | 0.5 | -0.81 | 4.75 |
| 1562 | 31 | 47.75 | Value ≥50k — hold ret_mean_2d_open | Value ≥50k | mean | 2 | open | 9 | 66.7 | 1.96 | 1.81 | 17.68 | 2.62 | 0.75 | -2.08 | 5.92 |
| 1563 | 31 | 47.75 | Value ≥50k — hold ret_mean_3d_open | Value ≥50k | mean | 3 | open | 9 | 66.7 | 1.96 | 1.93 | 17.64 | 2.88 | 0.68 | -2.03 | 7.93 |
| 1564 | 28 | 48.48 | Tutti — hold ret_mean_2d_open | Tutti | mean | 2 | open | 10 | 70.0 | 1.94 | 1.76 | 19.39 | 2.47 | 0.79 | -2.08 | 5.92 |
| 1565 | 35 | 40.48 | Value ≥500k — hold ret_mean_5d_open | Value ≥500k | mean | 5 | open | 4 | 50.0 | 1.94 | -0.54 | 7.78 | 6.13 | 0.32 | -2.07 | 10.93 |
| 1566 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_mean_3d_open | Large cap (≥3B) CEO/CFO | mean | 3 | open | 1 | 100.0 | 1.93 | 1.93 | 1.93 | nan | nan | 1.93 | 1.93 |
| 1567 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_mean_3d_open | Large cap (≥5B) CEO/CFO | mean | 3 | open | 1 | 100.0 | 1.93 | 1.93 | 1.93 | nan | nan | 1.93 | 1.93 |
| 1568 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_mean_3d_open | Large cap (≥10B) CEO/CFO | mean | 3 | open | 1 | 100.0 | 1.93 | 1.93 | 1.93 | nan | nan | 1.93 | 1.93 |
| 1569 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_mean_10d_news | Multiple buys (n≥2) | mean | 10 | news | 3 | 66.7 | 1.93 | 0.19 | 5.79 | 3.5 | 0.55 | -0.36 | 5.96 |
| 1570 | 14 | 65.45 | Price > MA200 — hold ret_mean_90d_news | Price > MA200 | mean | 90 | news | 4 | 75.0 | 1.9 | 0.63 | 7.61 | 3.94 | 0.48 | -1.27 | 7.62 |
| 1571 | 38 | 34.53 | Price < MA50 — hold ret_mean_2d_open | Price < MA50 | mean | 2 | open | 5 | 60.0 | 1.88 | 1.42 | 9.41 | 2.36 | 0.8 | -0.38 | 4.56 |
| 1572 | 31 | 47.75 | Value ≥50k — hold ret_mean_5d_open | Value ≥50k | mean | 5 | open | 9 | 55.6 | 1.88 | 0.78 | 16.92 | 4.01 | 0.47 | -2.07 | 10.93 |
| 1573 | 40 | 33.74 | Director only + Position +10% — hold ret_mean_2d_open | Director only + Position +10% | mean | 2 | open | 4 | 75.0 | 1.87 | 1.61 | 7.48 | 2.02 | 0.93 | -0.31 | 4.56 |
| 1574 | 28 | 48.48 | Tutti — hold ret_mean_3d_open | Tutti | mean | 3 | open | 10 | 70.0 | 1.87 | 1.58 | 18.73 | 2.73 | 0.69 | -2.03 | 7.93 |
| 1575 | 31 | 47.75 | Value ≥50k — hold ret_mean_10d_news | Value ≥50k | mean | 10 | news | 9 | 66.7 | 1.85 | 0.19 | 16.65 | 7.12 | 0.26 | -12.21 | 14.68 |
| 1576 | 14 | 65.45 | Price > MA200 — hold ret_mean_2d_open | Price > MA200 | mean | 2 | open | 4 | 75.0 | 1.84 | 1.76 | 7.36 | 3.27 | 0.56 | -2.08 | 5.92 |
| 1577 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_mean_3d_open | Multiple buys (n≥2) | mean | 3 | open | 3 | 66.7 | 1.82 | 1.23 | 5.46 | 2.21 | 0.82 | -0.04 | 4.27 |
| 1578 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_mean_10d_open | Large cap (≥2B) CEO/CFO | mean | 10 | open | 2 | 100.0 | 1.8 | 1.8 | 3.61 | 0.87 | 2.08 | 1.19 | 2.42 |
| 1579 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_low_1d_news | CEO only + Value ≥100k | low | 1 | news | 2 | 100.0 | 1.79 | 1.79 | 3.58 | 0.51 | 3.52 | 1.43 | 2.15 |
| 1580 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_low_1d_news | Price > MA50 + CEO/CFO | low | 1 | news | 2 | 100.0 | 1.79 | 1.79 | 3.58 | 0.51 | 3.52 | 1.43 | 2.15 |
| 1581 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_low_2d_news | CEO only + Value ≥100k | low | 2 | news | 2 | 100.0 | 1.78 | 1.79 | 3.57 | 0.5 | 3.56 | 1.43 | 2.14 |
| 1582 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_low_2d_news | Price > MA50 + CEO/CFO | low | 2 | news | 2 | 100.0 | 1.78 | 1.79 | 3.57 | 0.5 | 3.56 | 1.43 | 2.14 |
| 1583 | 28 | 48.48 | Tutti — hold ret_mean_7d_open | Tutti | mean | 7 | open | 10 | 60.0 | 1.77 | 1.08 | 17.73 | 4.96 | 0.36 | -6.35 | 12.39 |
| 1584 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_mean_10d_news | Large cap (≥2B) CEO/CFO | mean | 10 | news | 2 | 50.0 | 1.76 | 1.76 | 3.52 | 3.0 | 0.59 | -0.36 | 3.88 |
| 1585 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_mean_1d_open | CEO/CFO + Value ≥100k | mean | 1 | open | 3 | 66.7 | 1.74 | 2.55 | 5.21 | 2.35 | 0.74 | -0.91 | 3.57 |
| 1586 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_mean_1d_open | Large cap (≥750M) CEO/CFO | mean | 1 | open | 3 | 66.7 | 1.74 | 2.55 | 5.21 | 2.35 | 0.74 | -0.91 | 3.57 |
| 1587 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_mean_1d_open | Large cap (≥1B) CEO/CFO | mean | 1 | open | 3 | 66.7 | 1.74 | 2.55 | 5.21 | 2.35 | 0.74 | -0.91 | 3.57 |
| 1588 | 40 | 33.74 | Director only + Position +10% — hold ret_mean_3d_news | Director only + Position +10% | mean | 3 | news | 4 | 75.0 | 1.74 | 2.1 | 6.97 | 1.72 | 1.02 | -0.46 | 3.22 |
| 1589 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_mean_2d_open | Multiple buys (n≥2) | mean | 2 | open | 3 | 66.7 | 1.72 | 1.42 | 5.16 | 2.26 | 0.76 | -0.38 | 4.12 |
| 1590 | 30 | 48.32 | Value ≥100k — hold ret_mean_10d_news | Value ≥100k | mean | 10 | news | 6 | 50.0 | 1.72 | 1.84 | 10.32 | 8.75 | 0.2 | -12.21 | 14.68 |
| 1591 | 31 | 47.75 | Value ≥50k — hold ret_mean_1d_news | Value ≥50k | mean | 1 | news | 9 | 66.7 | 1.71 | 1.89 | 15.42 | 3.28 | 0.52 | -3.6 | 5.93 |
| 1592 | 14 | 65.45 | Price > MA200 — hold ret_mean_1d_news | Price > MA200 | mean | 1 | news | 4 | 75.0 | 1.71 | 1.6 | 6.85 | 2.65 | 0.65 | -1.41 | 5.05 |
| 1593 | 35 | 40.48 | Value ≥500k — hold ret_mean_7d_news | Value ≥500k | mean | 7 | news | 4 | 25.0 | 1.71 | -0.75 | 6.84 | 8.51 | 0.2 | -5.66 | 13.99 |
| 1594 | 28 | 48.48 | Tutti — hold ret_mean_5d_open | Tutti | mean | 5 | open | 10 | 60.0 | 1.7 | 0.41 | 16.96 | 3.83 | 0.44 | -2.07 | 10.93 |
| 1595 | 40 | 33.74 | Director only + Position +10% — hold ret_mean_1d_open | Director only + Position +10% | mean | 1 | open | 4 | 75.0 | 1.68 | 0.99 | 6.7 | 2.41 | 0.69 | -0.44 | 5.15 |
| 1596 | 28 | 48.48 | Tutti — hold ret_mean_1d_news | Tutti | mean | 1 | news | 10 | 70.0 | 1.67 | 1.6 | 16.74 | 3.09 | 0.54 | -3.6 | 5.93 |
| 1597 | 37 | 35.58 | Director only + Value ≥100k — hold ret_mean_3d_news | Director only + Value ≥100k | mean | 3 | news | 3 | 66.7 | 1.65 | 2.98 | 4.94 | 2.52 | 0.65 | -1.26 | 3.22 |
| 1598 | 21 | 53.67 | Qty ≥5k shares — hold ret_mean_1d_news | Qty ≥5k shares | mean | 1 | news | 6 | 66.7 | 1.64 | 1.94 | 9.86 | 3.66 | 0.45 | -3.6 | 5.93 |
| 1599 | 20 | 53.67 | Qty ≥10k shares — hold ret_mean_1d_news | Qty ≥10k shares | mean | 1 | news | 6 | 66.7 | 1.64 | 1.94 | 9.86 | 3.66 | 0.45 | -3.6 | 5.93 |
| 1600 | 35 | 40.48 | Value ≥500k — hold ret_mean_7d_open | Value ≥500k | mean | 7 | open | 4 | 50.0 | 1.64 | 0.25 | 6.55 | 7.96 | 0.21 | -6.35 | 12.39 |
| 1601 | 21 | 53.67 | Qty ≥5k shares — hold ret_mean_14d_open | Qty ≥5k shares | mean | 14 | open | 6 | 66.7 | 1.63 | 3.65 | 9.8 | 10.91 | 0.15 | -18.64 | 12.89 |
| 1602 | 21 | 53.67 | Qty ≥5k shares — hold ret_mean_14d_news | Qty ≥5k shares | mean | 14 | news | 6 | 83.3 | 1.63 | 2.67 | 9.8 | 10.88 | 0.15 | -18.03 | 14.49 |
| 1603 | 20 | 53.67 | Qty ≥10k shares — hold ret_mean_14d_open | Qty ≥10k shares | mean | 14 | open | 6 | 66.7 | 1.63 | 3.65 | 9.8 | 10.91 | 0.15 | -18.64 | 12.89 |
| 1604 | 20 | 53.67 | Qty ≥10k shares — hold ret_mean_14d_news | Qty ≥10k shares | mean | 14 | news | 6 | 83.3 | 1.63 | 2.67 | 9.8 | 10.88 | 0.15 | -18.03 | 14.49 |
| 1605 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_mean_3d_news | Far 52w high + Value ≥100k | mean | 3 | news | 3 | 66.7 | 1.62 | 2.98 | 4.86 | 3.88 | 0.42 | -2.76 | 4.64 |
| 1606 | 21 | 53.67 | Qty ≥5k shares — hold ret_mean_1d_open | Qty ≥5k shares | mean | 1 | open | 6 | 66.7 | 1.61 | 2.02 | 9.66 | 2.8 | 0.57 | -2.18 | 5.15 |
| 1607 | 20 | 53.67 | Qty ≥10k shares — hold ret_mean_1d_open | Qty ≥10k shares | mean | 1 | open | 6 | 66.7 | 1.61 | 2.02 | 9.66 | 2.8 | 0.57 | -2.18 | 5.15 |
| 1608 | 28 | 48.48 | Tutti — hold ret_mean_10d_news | Tutti | mean | 10 | news | 10 | 60.0 | 1.61 | 0.18 | 16.09 | 6.75 | 0.24 | -12.21 | 14.68 |
| 1609 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_mean_5d_open | Multiple buys (n≥2) | mean | 5 | open | 3 | 66.7 | 1.6 | 0.78 | 4.79 | 2.33 | 0.68 | -0.22 | 4.23 |
| 1610 | 32 | 44.63 | Position +10% — hold ret_mean_1d_news | Position +10% | mean | 1 | news | 6 | 66.7 | 1.59 | 1.42 | 9.55 | 3.56 | 0.45 | -3.6 | 5.93 |
| 1611 | 32 | 44.63 | Position +10% — hold ret_mean_1d_open | Position +10% | mean | 1 | open | 6 | 66.7 | 1.56 | 0.99 | 9.36 | 2.35 | 0.66 | -0.91 | 5.15 |
| 1612 | 31 | 47.75 | Value ≥50k — hold ret_mean_10d_open | Value ≥50k | mean | 10 | open | 9 | 77.8 | 1.56 | 1.19 | 14.08 | 6.93 | 0.23 | -12.85 | 13.07 |
| 1613 | 36 | 36.54 | Director only (no C-level) — hold ret_mean_2d_news | Director only (no C-level) | mean | 2 | news | 6 | 66.7 | 1.55 | 1.56 | 9.29 | 2.37 | 0.65 | -1.31 | 5.33 |
| 1614 | 30 | 48.32 | Value ≥100k — hold ret_mean_1d_open | Value ≥100k | mean | 1 | open | 6 | 66.7 | 1.54 | 1.8 | 9.23 | 2.77 | 0.56 | -2.18 | 5.15 |
| 1615 | 38 | 34.53 | Price < MA50 — hold ret_mean_1d_open | Price < MA50 | mean | 1 | open | 5 | 60.0 | 1.54 | 0.94 | 7.72 | 2.52 | 0.61 | -0.91 | 5.15 |
| 1616 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_mean_5d_open | Large cap (≥2B) CEO/CFO | mean | 5 | open | 2 | 100.0 | 1.5 | 1.5 | 3.01 | 1.03 | 1.47 | 0.78 | 2.23 |
| 1617 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_mean_5d_news | Large cap (≥2B) CEO/CFO | mean | 5 | news | 2 | 50.0 | 1.5 | 1.5 | 2.99 | 4.89 | 0.31 | -1.96 | 4.95 |
| 1618 | 35 | 40.48 | Value ≥500k — hold ret_mean_1d_news | Value ≥500k | mean | 1 | news | 4 | 50.0 | 1.49 | 1.82 | 5.97 | 4.72 | 0.32 | -3.6 | 5.93 |
| 1619 | 38 | 34.53 | Price < MA50 — hold ret_mean_3d_open | Price < MA50 | mean | 3 | open | 5 | 60.0 | 1.49 | 1.23 | 7.44 | 1.85 | 0.81 | -0.24 | 4.27 |
| 1620 | 22 | 53.36 | RSI overbought (>70) — hold ret_mean_14d_open | RSI overbought (>70) | mean | 14 | open | 2 | 50.0 | 1.49 | 1.49 | 2.98 | 2.33 | 0.64 | -0.16 | 3.14 |
| 1621 | 22 | 53.36 | RSI overbought (>70) — hold ret_mean_5d_news | RSI overbought (>70) | mean | 5 | news | 2 | 50.0 | 1.46 | 1.46 | 2.92 | 3.61 | 0.4 | -1.09 | 4.01 |
| 1622 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_low_1d_news | CEO only + Value ≥500k | low | 1 | news | 1 | 100.0 | 1.43 | 1.43 | 1.43 | nan | nan | 1.43 | 1.43 |
| 1623 | 1 | 100.0 | CEO only + Position +10% — hold ret_low_1d_news | CEO only + Position +10% | low | 1 | news | 1 | 100.0 | 1.43 | 1.43 | 1.43 | nan | nan | 1.43 | 1.43 |
| 1624 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_low_1d_news | Near 52w high + CEO/CFO | low | 1 | news | 1 | 100.0 | 1.43 | 1.43 | 1.43 | nan | nan | 1.43 | 1.43 |
| 1625 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_low_2d_news | CEO only + Value ≥500k | low | 2 | news | 1 | 100.0 | 1.43 | 1.43 | 1.43 | nan | nan | 1.43 | 1.43 |
| 1626 | 1 | 100.0 | CEO only + Position +10% — hold ret_low_2d_news | CEO only + Position +10% | low | 2 | news | 1 | 100.0 | 1.43 | 1.43 | 1.43 | nan | nan | 1.43 | 1.43 |
| 1627 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_low_2d_news | Near 52w high + CEO/CFO | low | 2 | news | 1 | 100.0 | 1.43 | 1.43 | 1.43 | nan | nan | 1.43 | 1.43 |
| 1628 | 37 | 35.58 | Director only + Value ≥100k — hold ret_mean_2d_open | Director only + Value ≥100k | mean | 2 | open | 3 | 66.7 | 1.43 | 1.81 | 4.29 | 3.34 | 0.43 | -2.08 | 4.56 |
| 1629 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_low_3d_news | CEO only + Value ≥500k | low | 3 | news | 1 | 100.0 | 1.43 | 1.43 | 1.43 | nan | nan | 1.43 | 1.43 |
| 1630 | 1 | 100.0 | CEO only + Position +10% — hold ret_low_3d_news | CEO only + Position +10% | low | 3 | news | 1 | 100.0 | 1.43 | 1.43 | 1.43 | nan | nan | 1.43 | 1.43 |
| 1631 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_low_3d_news | Near 52w high + CEO/CFO | low | 3 | news | 1 | 100.0 | 1.43 | 1.43 | 1.43 | nan | nan | 1.43 | 1.43 |
| 1632 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_low_5d_news | CEO only + Value ≥500k | low | 5 | news | 1 | 100.0 | 1.43 | 1.43 | 1.43 | nan | nan | 1.43 | 1.43 |
| 1633 | 1 | 100.0 | CEO only + Position +10% — hold ret_low_5d_news | CEO only + Position +10% | low | 5 | news | 1 | 100.0 | 1.43 | 1.43 | 1.43 | nan | nan | 1.43 | 1.43 |
| 1634 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_low_5d_news | Near 52w high + CEO/CFO | low | 5 | news | 1 | 100.0 | 1.43 | 1.43 | 1.43 | nan | nan | 1.43 | 1.43 |
| 1635 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_low_7d_news | CEO only + Value ≥500k | low | 7 | news | 1 | 100.0 | 1.43 | 1.43 | 1.43 | nan | nan | 1.43 | 1.43 |
| 1636 | 1 | 100.0 | CEO only + Position +10% — hold ret_low_7d_news | CEO only + Position +10% | low | 7 | news | 1 | 100.0 | 1.43 | 1.43 | 1.43 | nan | nan | 1.43 | 1.43 |
| 1637 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_low_7d_news | Near 52w high + CEO/CFO | low | 7 | news | 1 | 100.0 | 1.43 | 1.43 | 1.43 | nan | nan | 1.43 | 1.43 |
| 1638 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_low_10d_news | CEO only + Value ≥500k | low | 10 | news | 1 | 100.0 | 1.43 | 1.43 | 1.43 | nan | nan | 1.43 | 1.43 |
| 1639 | 1 | 100.0 | CEO only + Position +10% — hold ret_low_10d_news | CEO only + Position +10% | low | 10 | news | 1 | 100.0 | 1.43 | 1.43 | 1.43 | nan | nan | 1.43 | 1.43 |
| 1640 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_low_10d_news | Near 52w high + CEO/CFO | low | 10 | news | 1 | 100.0 | 1.43 | 1.43 | 1.43 | nan | nan | 1.43 | 1.43 |
| 1641 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_low_14d_news | CEO only + Value ≥500k | low | 14 | news | 1 | 100.0 | 1.43 | 1.43 | 1.43 | nan | nan | 1.43 | 1.43 |
| 1642 | 1 | 100.0 | CEO only + Position +10% — hold ret_low_14d_news | CEO only + Position +10% | low | 14 | news | 1 | 100.0 | 1.43 | 1.43 | 1.43 | nan | nan | 1.43 | 1.43 |
| 1643 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_low_14d_news | Near 52w high + CEO/CFO | low | 14 | news | 1 | 100.0 | 1.43 | 1.43 | 1.43 | nan | nan | 1.43 | 1.43 |
| 1644 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_low_30d_news | CEO only + Value ≥500k | low | 30 | news | 1 | 100.0 | 1.43 | 1.43 | 1.43 | nan | nan | 1.43 | 1.43 |
| 1645 | 1 | 100.0 | CEO only + Position +10% — hold ret_low_30d_news | CEO only + Position +10% | low | 30 | news | 1 | 100.0 | 1.43 | 1.43 | 1.43 | nan | nan | 1.43 | 1.43 |
| 1646 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_low_30d_news | Near 52w high + CEO/CFO | low | 30 | news | 1 | 100.0 | 1.43 | 1.43 | 1.43 | nan | nan | 1.43 | 1.43 |
| 1647 | 39 | 34.48 | Position +20% — hold ret_mean_2d_open | Position +20% | mean | 2 | open | 4 | 50.0 | 1.42 | 0.75 | 5.68 | 2.33 | 0.61 | -0.38 | 4.56 |
| 1648 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_mean_2d_news | Mid cap (1B–10B) Value ≥100k | mean | 2 | news | 4 | 50.0 | 1.42 | 0.68 | 5.7 | 4.67 | 0.31 | -3.09 | 7.43 |
| 1649 | 31 | 47.75 | Value ≥50k — hold ret_mean_1d_open | Value ≥50k | mean | 1 | open | 9 | 66.7 | 1.41 | 1.05 | 12.71 | 2.36 | 0.6 | -2.18 | 5.15 |
| 1650 | 35 | 40.48 | Value ≥500k — hold ret_mean_1d_open | Value ≥500k | mean | 1 | open | 4 | 50.0 | 1.41 | 1.33 | 5.63 | 3.51 | 0.4 | -2.18 | 5.15 |
| 1651 | 28 | 48.48 | Tutti — hold ret_mean_1d_open | Tutti | mean | 1 | open | 10 | 70.0 | 1.4 | 1.19 | 14.03 | 2.22 | 0.63 | -2.18 | 5.15 |
| 1652 | 40 | 33.74 | Director only + Position +10% — hold ret_mean_3d_open | Director only + Position +10% | mean | 3 | open | 4 | 75.0 | 1.4 | 1.73 | 5.58 | 1.2 | 1.16 | -0.24 | 2.37 |
| 1653 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_mean_3d_open | Far 52w high + Value ≥100k | mean | 3 | open | 3 | 66.7 | 1.37 | 1.93 | 4.11 | 1.23 | 1.11 | -0.04 | 2.22 |
| 1654 | 33 | 41.81 | Director — hold ret_mean_2d_open | Director | mean | 2 | open | 8 | 62.5 | 1.36 | 1.56 | 10.85 | 2.26 | 0.6 | -2.08 | 4.56 |
| 1655 | 28 | 48.48 | Tutti — hold ret_mean_10d_open | Tutti | mean | 10 | open | 10 | 70.0 | 1.35 | 0.79 | 13.52 | 6.57 | 0.21 | -12.85 | 13.07 |
| 1656 | 36 | 36.54 | Director only (no C-level) — hold ret_mean_1d_news | Director only (no C-level) | mean | 1 | news | 6 | 66.7 | 1.34 | 1.13 | 8.01 | 2.57 | 0.52 | -1.41 | 5.93 |
| 1657 | 37 | 35.58 | Director only + Value ≥100k — hold ret_mean_1d_open | Director only + Value ≥100k | mean | 1 | open | 3 | 66.7 | 1.34 | 1.05 | 4.02 | 3.67 | 0.36 | -2.18 | 5.15 |
| 1658 | 22 | 53.36 | RSI overbought (>70) — hold ret_mean_10d_open | RSI overbought (>70) | mean | 10 | open | 2 | 50.0 | 1.34 | 1.34 | 2.68 | 3.27 | 0.41 | -0.97 | 3.65 |
| 1659 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_mean_1d_open | Mid cap (1B–10B) CEO/CFO | mean | 1 | open | 2 | 50.0 | 1.33 | 1.33 | 2.66 | 3.17 | 0.42 | -0.91 | 3.57 |
| 1660 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_mean_2d_open | Mid cap (1B–10B) Value ≥100k | mean | 2 | open | 4 | 50.0 | 1.32 | 0.72 | 5.27 | 3.46 | 0.38 | -2.08 | 5.92 |
| 1661 | 49 | 32.78 | CFO only — hold ret_mean_14d_news | CFO only | mean | 14 | news | 1 | 100.0 | 1.32 | 1.32 | 1.32 | nan | nan | 1.32 | 1.32 |
| 1662 | 48 | 32.78 | CFO + Director (combo) — hold ret_mean_14d_news | CFO + Director (combo) | mean | 14 | news | 1 | 100.0 | 1.32 | 1.32 | 1.32 | nan | nan | 1.32 | 1.32 |
| 1663 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_mean_14d_news | CFO only + Value ≥50k | mean | 14 | news | 1 | 100.0 | 1.32 | 1.32 | 1.32 | nan | nan | 1.32 | 1.32 |
| 1664 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_mean_14d_news | CFO only + Value ≥100k | mean | 14 | news | 1 | 100.0 | 1.32 | 1.32 | 1.32 | nan | nan | 1.32 | 1.32 |
| 1665 | 47 | 32.78 | CFO only + Position +10% — hold ret_mean_14d_news | CFO only + Position +10% | mean | 14 | news | 1 | 100.0 | 1.32 | 1.32 | 1.32 | nan | nan | 1.32 | 1.32 |
| 1666 | 46 | 32.78 | CFO only + Position +20% — hold ret_mean_14d_news | CFO only + Position +20% | mean | 14 | news | 1 | 100.0 | 1.32 | 1.32 | 1.32 | nan | nan | 1.32 | 1.32 |
| 1667 | 44 | 32.78 | RSI oversold (<30) — hold ret_mean_14d_news | RSI oversold (<30) | mean | 14 | news | 1 | 100.0 | 1.32 | 1.32 | 1.32 | nan | nan | 1.32 | 1.32 |
| 1668 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_mean_14d_news | RSI oversold + CEO/CFO | mean | 14 | news | 1 | 100.0 | 1.32 | 1.32 | 1.32 | nan | nan | 1.32 | 1.32 |
| 1669 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_mean_14d_news | RSI oversold + Value ≥100k | mean | 14 | news | 1 | 100.0 | 1.32 | 1.32 | 1.32 | nan | nan | 1.32 | 1.32 |
| 1670 | 51 | 20.1 | Position +30% — hold ret_mean_2d_open | Position +30% | mean | 2 | open | 3 | 33.3 | 1.29 | -0.31 | 3.87 | 2.83 | 0.46 | -0.38 | 4.56 |
| 1671 | 51 | 20.1 | Position +30% — hold ret_mean_1d_open | Position +30% | mean | 1 | open | 3 | 33.3 | 1.27 | -0.44 | 3.8 | 3.37 | 0.38 | -0.91 | 5.15 |
| 1672 | 22 | 53.36 | RSI overbought (>70) — hold ret_high_1d_open | RSI overbought (>70) | high | 1 | open | 2 | 100.0 | 1.26 | 1.26 | 2.52 | 1.1 | 1.14 | 0.48 | 2.04 |
| 1673 | 15 | 62.43 | Price > MA50 — hold ret_mean_1d_open | Price > MA50 | mean | 1 | open | 5 | 80.0 | 1.26 | 1.32 | 6.31 | 2.17 | 0.58 | -2.18 | 3.57 |
| 1674 | 38 | 34.53 | Price < MA50 — hold ret_mean_2d_news | Price < MA50 | mean | 2 | news | 5 | 60.0 | 1.25 | 1.42 | 6.26 | 3.25 | 0.39 | -3.09 | 5.33 |
| 1675 | 28 | 48.48 | Tutti — hold ret_mean_30d_news | Tutti | mean | 30 | news | 10 | 60.0 | 1.25 | 2.29 | 12.48 | 8.69 | 0.14 | -19.4 | 13.57 |
| 1676 | 26 | 50.0 | Qty ≥50k shares — hold ret_mean_10d_news | Qty ≥50k shares | mean | 10 | news | 2 | 50.0 | 1.23 | 1.23 | 2.47 | 19.01 | 0.06 | -12.21 | 14.68 |
| 1677 | 27 | 50.0 | Value ≥1M — hold ret_mean_10d_news | Value ≥1M | mean | 10 | news | 2 | 50.0 | 1.23 | 1.23 | 2.47 | 19.01 | 0.06 | -12.21 | 14.68 |
| 1678 | 39 | 34.48 | Position +20% — hold ret_mean_1d_open | Position +20% | mean | 1 | open | 4 | 50.0 | 1.21 | 0.31 | 4.85 | 2.75 | 0.44 | -0.91 | 5.15 |
| 1679 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_mean_10d_open | Large cap (≥3B) CEO/CFO | mean | 10 | open | 1 | 100.0 | 1.19 | 1.19 | 1.19 | nan | nan | 1.19 | 1.19 |
| 1680 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_mean_10d_open | Large cap (≥5B) CEO/CFO | mean | 10 | open | 1 | 100.0 | 1.19 | 1.19 | 1.19 | nan | nan | 1.19 | 1.19 |
| 1681 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_mean_10d_open | Large cap (≥10B) CEO/CFO | mean | 10 | open | 1 | 100.0 | 1.19 | 1.19 | 1.19 | nan | nan | 1.19 | 1.19 |
| 1682 | 36 | 36.54 | Director only (no C-level) — hold ret_mean_2d_open | Director only (no C-level) | mean | 2 | open | 6 | 66.7 | 1.18 | 1.56 | 7.11 | 2.24 | 0.53 | -2.08 | 4.56 |
| 1683 | 33 | 41.81 | Director — hold ret_mean_2d_news | Director | mean | 2 | news | 8 | 62.5 | 1.17 | 1.56 | 9.33 | 2.7 | 0.43 | -3.09 | 5.33 |
| 1684 | 32 | 44.63 | Position +10% — hold ret_mean_10d_news | Position +10% | mean | 10 | news | 6 | 66.7 | 1.17 | 0.18 | 7.0 | 8.68 | 0.13 | -12.21 | 14.68 |
| 1685 | 22 | 53.36 | RSI overbought (>70) — hold ret_mean_7d_open | RSI overbought (>70) | mean | 7 | open | 2 | 50.0 | 1.15 | 1.15 | 2.3 | 3.86 | 0.3 | -1.58 | 3.88 |
| 1686 | 32 | 44.63 | Position +10% — hold ret_mean_10d_open | Position +10% | mean | 10 | open | 6 | 83.3 | 1.15 | 1.41 | 6.88 | 8.34 | 0.14 | -12.85 | 13.07 |
| 1687 | 14 | 65.45 | Price > MA200 — hold ret_mean_90d_open | Price > MA200 | mean | 90 | open | 4 | 50.0 | 1.14 | 0.21 | 4.55 | 4.08 | 0.28 | -2.66 | 6.78 |
| 1688 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_mean_2d_news | Large cap (≥2B) CEO/CFO | mean | 2 | news | 2 | 50.0 | 1.13 | 1.13 | 2.26 | 5.97 | 0.19 | -3.09 | 5.35 |
| 1689 | 36 | 36.54 | Director only (no C-level) — hold ret_mean_3d_news | Director only (no C-level) | mean | 3 | news | 6 | 66.7 | 1.13 | 1.16 | 6.8 | 1.79 | 0.63 | -1.26 | 3.22 |
| 1690 | 28 | 48.48 | Tutti — hold ret_mean_14d_news | Tutti | mean | 14 | news | 10 | 70.0 | 1.13 | 0.97 | 11.32 | 8.15 | 0.14 | -18.03 | 14.49 |
| 1691 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_mean_2d_open | Large cap (≥2B) CEO/CFO | mean | 2 | open | 2 | 50.0 | 1.12 | 1.12 | 2.24 | 2.12 | 0.53 | -0.38 | 2.62 |
| 1692 | 33 | 41.81 | Director — hold ret_mean_3d_open | Director | mean | 3 | open | 8 | 62.5 | 1.11 | 1.16 | 8.87 | 1.92 | 0.58 | -2.03 | 4.27 |
| 1693 | 39 | 34.48 | Position +20% — hold ret_mean_2d_news | Position +20% | mean | 2 | news | 4 | 50.0 | 1.1 | 1.07 | 4.38 | 3.68 | 0.3 | -3.09 | 5.33 |
| 1694 | 30 | 48.32 | Value ≥100k — hold ret_mean_10d_open | Value ≥100k | mean | 10 | open | 6 | 66.7 | 1.09 | 1.8 | 6.51 | 8.37 | 0.13 | -12.85 | 13.07 |
| 1695 | 39 | 34.48 | Position +20% — hold ret_mean_3d_open | Position +20% | mean | 3 | open | 4 | 50.0 | 1.08 | 1.09 | 4.31 | 1.41 | 0.76 | -0.24 | 2.37 |
| 1696 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_mean_7d_news | Multiple buys (n≥2) | mean | 7 | news | 3 | 33.3 | 1.07 | -0.26 | 3.2 | 2.67 | 0.4 | -0.68 | 4.14 |
| 1697 | 31 | 47.75 | Value ≥50k — hold ret_mean_14d_news | Value ≥50k | mean | 14 | news | 9 | 66.7 | 1.07 | 0.62 | 9.63 | 8.65 | 0.12 | -18.03 | 14.49 |
| 1698 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_mean_90d_news | Mid cap (1B–10B) Value ≥100k | mean | 90 | news | 4 | 50.0 | 1.07 | -0.61 | 4.27 | 4.46 | 0.24 | -2.13 | 7.62 |
| 1699 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_mean_14d_open | Large cap (≥2B) CEO/CFO | mean | 14 | open | 2 | 50.0 | 1.03 | 1.03 | 2.05 | 4.42 | 0.23 | -2.1 | 4.15 |
| 1700 | 28 | 48.48 | Tutti — hold ret_mean_30d_open | Tutti | mean | 30 | open | 10 | 60.0 | 1.02 | 2.21 | 10.2 | 8.91 | 0.11 | -19.99 | 11.97 |
| 1701 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_mean_1d_open | Multiple buys (n≥2) | mean | 1 | open | 3 | 66.7 | 1.0 | 0.94 | 3.01 | 1.95 | 0.52 | -0.91 | 2.98 |
| 1702 | 33 | 41.81 | Director — hold ret_mean_1d_open | Director | mean | 1 | open | 8 | 62.5 | 0.99 | 0.99 | 7.91 | 2.3 | 0.43 | -2.18 | 5.15 |
| 1703 | 15 | 62.43 | Price > MA50 — hold ret_mean_60d_open | Price > MA50 | mean | 60 | open | 5 | 80.0 | 0.99 | 2.63 | 4.94 | 4.3 | 0.23 | -6.46 | 4.39 |
| 1704 | 22 | 53.36 | RSI overbought (>70) — hold ret_mean_3d_news | RSI overbought (>70) | mean | 3 | news | 2 | 50.0 | 0.98 | 0.98 | 1.96 | 3.17 | 0.31 | -1.26 | 3.22 |
| 1705 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_mean_90d_open | Mid cap (1B–10B) Value ≥100k | mean | 90 | open | 4 | 50.0 | 0.98 | -0.09 | 3.94 | 4.09 | 0.24 | -2.66 | 6.78 |
| 1706 | 36 | 36.54 | Director only (no C-level) — hold ret_mean_1d_open | Director only (no C-level) | mean | 1 | open | 6 | 66.7 | 0.97 | 0.99 | 5.84 | 2.43 | 0.4 | -2.18 | 5.15 |
| 1707 | 14 | 65.45 | Price > MA200 — hold ret_mean_1d_open | Price > MA200 | mean | 1 | open | 4 | 75.0 | 0.94 | 1.19 | 3.76 | 2.37 | 0.4 | -2.18 | 3.57 |
| 1708 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_mean_3d_open | Large cap (≥2B) CEO/CFO | mean | 3 | open | 2 | 50.0 | 0.94 | 0.94 | 1.89 | 1.39 | 0.68 | -0.04 | 1.93 |
| 1709 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_mean_3d_news | Large cap (≥2B) CEO/CFO | mean | 3 | news | 2 | 50.0 | 0.94 | 0.94 | 1.88 | 5.23 | 0.18 | -2.76 | 4.64 |
| 1710 | 31 | 47.75 | Value ≥50k — hold ret_mean_30d_news | Value ≥50k | mean | 30 | news | 9 | 55.6 | 0.94 | 2.13 | 8.42 | 9.16 | 0.1 | -19.4 | 13.57 |
| 1711 | 38 | 34.53 | Price < MA50 — hold ret_mean_1d_news | Price < MA50 | mean | 1 | news | 5 | 60.0 | 0.92 | 0.94 | 4.61 | 3.51 | 0.26 | -3.6 | 5.93 |
| 1712 | 33 | 41.81 | Director — hold ret_mean_3d_news | Director | mean | 3 | news | 8 | 62.5 | 0.91 | 1.16 | 7.31 | 2.25 | 0.41 | -2.76 | 3.27 |
| 1713 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_mean_14d_news | Large cap (≥2B) CEO/CFO | mean | 14 | news | 2 | 100.0 | 0.91 | 0.91 | 1.82 | 0.58 | 1.57 | 0.5 | 1.32 |
| 1714 | 39 | 34.48 | Position +20% — hold ret_mean_1d_news | Position +20% | mean | 1 | news | 4 | 50.0 | 0.89 | 0.61 | 3.56 | 4.04 | 0.22 | -3.6 | 5.93 |
| 1715 | 28 | 48.48 | Tutti — hold ret_mean_14d_open | Tutti | mean | 14 | open | 10 | 50.0 | 0.89 | 0.84 | 8.94 | 8.24 | 0.11 | -18.64 | 12.89 |
| 1716 | 49 | 32.78 | CFO only — hold ret_mean_60d_news | CFO only | mean | 60 | news | 1 | 100.0 | 0.89 | 0.89 | 0.89 | nan | nan | 0.89 | 0.89 |
| 1717 | 48 | 32.78 | CFO + Director (combo) — hold ret_mean_60d_news | CFO + Director (combo) | mean | 60 | news | 1 | 100.0 | 0.89 | 0.89 | 0.89 | nan | nan | 0.89 | 0.89 |
| 1718 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_mean_60d_news | CFO only + Value ≥50k | mean | 60 | news | 1 | 100.0 | 0.89 | 0.89 | 0.89 | nan | nan | 0.89 | 0.89 |
| 1719 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_mean_60d_news | CFO only + Value ≥100k | mean | 60 | news | 1 | 100.0 | 0.89 | 0.89 | 0.89 | nan | nan | 0.89 | 0.89 |
| 1720 | 47 | 32.78 | CFO only + Position +10% — hold ret_mean_60d_news | CFO only + Position +10% | mean | 60 | news | 1 | 100.0 | 0.89 | 0.89 | 0.89 | nan | nan | 0.89 | 0.89 |
| 1721 | 46 | 32.78 | CFO only + Position +20% — hold ret_mean_60d_news | CFO only + Position +20% | mean | 60 | news | 1 | 100.0 | 0.89 | 0.89 | 0.89 | nan | nan | 0.89 | 0.89 |
| 1722 | 44 | 32.78 | RSI oversold (<30) — hold ret_mean_60d_news | RSI oversold (<30) | mean | 60 | news | 1 | 100.0 | 0.89 | 0.89 | 0.89 | nan | nan | 0.89 | 0.89 |
| 1723 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_mean_60d_news | RSI oversold + CEO/CFO | mean | 60 | news | 1 | 100.0 | 0.89 | 0.89 | 0.89 | nan | nan | 0.89 | 0.89 |
| 1724 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_mean_60d_news | RSI oversold + Value ≥100k | mean | 60 | news | 1 | 100.0 | 0.89 | 0.89 | 0.89 | nan | nan | 0.89 | 0.89 |
| 1725 | 15 | 62.43 | Price > MA50 — hold ret_mean_90d_news | Price > MA50 | mean | 90 | news | 5 | 60.0 | 0.89 | 0.05 | 4.46 | 4.1 | 0.22 | -3.15 | 7.62 |
| 1726 | 37 | 35.58 | Director only + Value ≥100k — hold ret_mean_3d_open | Director only + Value ≥100k | mean | 3 | open | 3 | 66.7 | 0.85 | 2.22 | 2.56 | 2.5 | 0.34 | -2.03 | 2.37 |
| 1727 | 38 | 34.53 | Price < MA50 — hold ret_mean_3d_news | Price < MA50 | mean | 3 | news | 5 | 60.0 | 0.85 | 1.23 | 4.26 | 2.51 | 0.34 | -2.76 | 3.27 |
| 1728 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_mean_1d_news | Large cap (≥2B) CEO/CFO | mean | 1 | news | 2 | 50.0 | 0.84 | 0.84 | 1.68 | 6.28 | 0.13 | -3.6 | 5.28 |
| 1729 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_mean_1d_open | Large cap (≥2B) CEO/CFO | mean | 1 | open | 2 | 50.0 | 0.82 | 0.82 | 1.64 | 2.45 | 0.34 | -0.91 | 2.55 |
| 1730 | 31 | 47.75 | Value ≥50k — hold ret_mean_14d_open | Value ≥50k | mean | 14 | open | 9 | 44.4 | 0.81 | -0.01 | 7.25 | 8.73 | 0.09 | -18.64 | 12.89 |
| 1731 | 33 | 41.81 | Director — hold ret_mean_1d_news | Director | mean | 1 | news | 8 | 62.5 | 0.8 | 1.13 | 6.41 | 2.82 | 0.28 | -3.6 | 5.93 |
| 1732 | 49 | 32.78 | CFO only — hold ret_mean_5d_open | CFO only | mean | 5 | open | 1 | 100.0 | 0.78 | 0.78 | 0.78 | nan | nan | 0.78 | 0.78 |
| 1733 | 48 | 32.78 | CFO + Director (combo) — hold ret_mean_5d_open | CFO + Director (combo) | mean | 5 | open | 1 | 100.0 | 0.78 | 0.78 | 0.78 | nan | nan | 0.78 | 0.78 |
| 1734 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_mean_5d_open | CFO only + Value ≥50k | mean | 5 | open | 1 | 100.0 | 0.78 | 0.78 | 0.78 | nan | nan | 0.78 | 0.78 |
| 1735 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_mean_5d_open | CFO only + Value ≥100k | mean | 5 | open | 1 | 100.0 | 0.78 | 0.78 | 0.78 | nan | nan | 0.78 | 0.78 |
| 1736 | 47 | 32.78 | CFO only + Position +10% — hold ret_mean_5d_open | CFO only + Position +10% | mean | 5 | open | 1 | 100.0 | 0.78 | 0.78 | 0.78 | nan | nan | 0.78 | 0.78 |
| 1737 | 46 | 32.78 | CFO only + Position +20% — hold ret_mean_5d_open | CFO only + Position +20% | mean | 5 | open | 1 | 100.0 | 0.78 | 0.78 | 0.78 | nan | nan | 0.78 | 0.78 |
| 1738 | 44 | 32.78 | RSI oversold (<30) — hold ret_mean_5d_open | RSI oversold (<30) | mean | 5 | open | 1 | 100.0 | 0.78 | 0.78 | 0.78 | nan | nan | 0.78 | 0.78 |
| 1739 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_mean_5d_open | RSI oversold + CEO/CFO | mean | 5 | open | 1 | 100.0 | 0.78 | 0.78 | 0.78 | nan | nan | 0.78 | 0.78 |
| 1740 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_mean_5d_open | RSI oversold + Value ≥100k | mean | 5 | open | 1 | 100.0 | 0.78 | 0.78 | 0.78 | nan | nan | 0.78 | 0.78 |
| 1741 | 36 | 36.54 | Director only (no C-level) — hold ret_mean_3d_open | Director only (no C-level) | mean | 3 | open | 6 | 66.7 | 0.77 | 1.16 | 4.64 | 1.66 | 0.46 | -2.03 | 2.37 |
| 1742 | 39 | 34.48 | Position +20% — hold ret_mean_3d_news | Position +20% | mean | 3 | news | 4 | 50.0 | 0.75 | 1.26 | 2.98 | 2.88 | 0.26 | -2.76 | 3.22 |
| 1743 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_mean_1d_news | Mid cap (1B–10B) CEO/CFO | mean | 1 | news | 2 | 50.0 | 0.72 | 0.72 | 1.45 | 6.12 | 0.12 | -3.6 | 5.05 |
| 1744 | 22 | 53.36 | RSI overbought (>70) — hold ret_mean_2d_news | RSI overbought (>70) | mean | 2 | news | 2 | 50.0 | 0.68 | 0.68 | 1.36 | 2.81 | 0.24 | -1.31 | 2.67 |
| 1745 | 31 | 47.75 | Value ≥50k — hold ret_mean_30d_open | Value ≥50k | mean | 30 | open | 9 | 55.6 | 0.68 | 1.33 | 6.14 | 9.38 | 0.07 | -19.99 | 11.97 |
| 1746 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_mean_30d_open | Large cap (≥2B) CEO/CFO | mean | 30 | open | 2 | 50.0 | 0.68 | 0.68 | 1.36 | 6.55 | 0.1 | -3.95 | 5.31 |
| 1747 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_low_3d_news | CEO only + Value ≥100k | low | 3 | news | 2 | 50.0 | 0.66 | 0.66 | 1.32 | 1.09 | 0.61 | -0.11 | 1.43 |
| 1748 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_low_3d_news | Price > MA50 + CEO/CFO | low | 3 | news | 2 | 50.0 | 0.66 | 0.66 | 1.32 | 1.09 | 0.61 | -0.11 | 1.43 |
| 1749 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_low_5d_news | CEO only + Value ≥100k | low | 5 | news | 2 | 50.0 | 0.66 | 0.66 | 1.32 | 1.09 | 0.61 | -0.11 | 1.43 |
| 1750 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_low_5d_news | Price > MA50 + CEO/CFO | low | 5 | news | 2 | 50.0 | 0.66 | 0.66 | 1.32 | 1.09 | 0.61 | -0.11 | 1.43 |
| 1751 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_low_7d_news | CEO only + Value ≥100k | low | 7 | news | 2 | 50.0 | 0.66 | 0.66 | 1.32 | 1.09 | 0.61 | -0.11 | 1.43 |
| 1752 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_low_7d_news | Price > MA50 + CEO/CFO | low | 7 | news | 2 | 50.0 | 0.66 | 0.66 | 1.32 | 1.09 | 0.61 | -0.11 | 1.43 |
| 1753 | 51 | 20.1 | Position +30% — hold ret_mean_3d_open | Position +30% | mean | 3 | open | 3 | 33.3 | 0.65 | -0.04 | 1.94 | 1.37 | 0.47 | -0.24 | 2.22 |
| 1754 | 22 | 53.36 | RSI overbought (>70) — hold ret_mean_5d_open | RSI overbought (>70) | mean | 5 | open | 2 | 50.0 | 0.64 | 0.64 | 1.29 | 3.54 | 0.18 | -1.86 | 3.15 |
| 1755 | 49 | 32.78 | CFO only — hold ret_mean_90d_open | CFO only | mean | 90 | open | 1 | 100.0 | 0.6 | 0.6 | 0.6 | nan | nan | 0.6 | 0.6 |
| 1756 | 48 | 32.78 | CFO + Director (combo) — hold ret_mean_90d_open | CFO + Director (combo) | mean | 90 | open | 1 | 100.0 | 0.6 | 0.6 | 0.6 | nan | nan | 0.6 | 0.6 |
| 1757 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_mean_90d_open | CFO only + Value ≥50k | mean | 90 | open | 1 | 100.0 | 0.6 | 0.6 | 0.6 | nan | nan | 0.6 | 0.6 |
| 1758 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_mean_90d_open | CFO only + Value ≥100k | mean | 90 | open | 1 | 100.0 | 0.6 | 0.6 | 0.6 | nan | nan | 0.6 | 0.6 |
| 1759 | 47 | 32.78 | CFO only + Position +10% — hold ret_mean_90d_open | CFO only + Position +10% | mean | 90 | open | 1 | 100.0 | 0.6 | 0.6 | 0.6 | nan | nan | 0.6 | 0.6 |
| 1760 | 46 | 32.78 | CFO only + Position +20% — hold ret_mean_90d_open | CFO only + Position +20% | mean | 90 | open | 1 | 100.0 | 0.6 | 0.6 | 0.6 | nan | nan | 0.6 | 0.6 |
| 1761 | 44 | 32.78 | RSI oversold (<30) — hold ret_mean_90d_open | RSI oversold (<30) | mean | 90 | open | 1 | 100.0 | 0.6 | 0.6 | 0.6 | nan | nan | 0.6 | 0.6 |
| 1762 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_mean_90d_open | RSI oversold + CEO/CFO | mean | 90 | open | 1 | 100.0 | 0.6 | 0.6 | 0.6 | nan | nan | 0.6 | 0.6 |
| 1763 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_mean_90d_open | RSI oversold + Value ≥100k | mean | 90 | open | 1 | 100.0 | 0.6 | 0.6 | 0.6 | nan | nan | 0.6 | 0.6 |
| 1764 | 49 | 32.78 | CFO only — hold ret_high_3d_news | CFO only | high | 3 | news | 1 | 100.0 | 0.59 | 0.59 | 0.59 | nan | nan | 0.59 | 0.59 |
| 1765 | 48 | 32.78 | CFO + Director (combo) — hold ret_high_3d_news | CFO + Director (combo) | high | 3 | news | 1 | 100.0 | 0.59 | 0.59 | 0.59 | nan | nan | 0.59 | 0.59 |
| 1766 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_high_3d_news | CFO only + Value ≥50k | high | 3 | news | 1 | 100.0 | 0.59 | 0.59 | 0.59 | nan | nan | 0.59 | 0.59 |
| 1767 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_high_3d_news | CFO only + Value ≥100k | high | 3 | news | 1 | 100.0 | 0.59 | 0.59 | 0.59 | nan | nan | 0.59 | 0.59 |
| 1768 | 47 | 32.78 | CFO only + Position +10% — hold ret_high_3d_news | CFO only + Position +10% | high | 3 | news | 1 | 100.0 | 0.59 | 0.59 | 0.59 | nan | nan | 0.59 | 0.59 |
| 1769 | 46 | 32.78 | CFO only + Position +20% — hold ret_high_3d_news | CFO only + Position +20% | high | 3 | news | 1 | 100.0 | 0.59 | 0.59 | 0.59 | nan | nan | 0.59 | 0.59 |
| 1770 | 44 | 32.78 | RSI oversold (<30) — hold ret_high_3d_news | RSI oversold (<30) | high | 3 | news | 1 | 100.0 | 0.59 | 0.59 | 0.59 | nan | nan | 0.59 | 0.59 |
| 1771 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_high_3d_news | RSI oversold + CEO/CFO | high | 3 | news | 1 | 100.0 | 0.59 | 0.59 | 0.59 | nan | nan | 0.59 | 0.59 |
| 1772 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_high_3d_news | RSI oversold + Value ≥100k | high | 3 | news | 1 | 100.0 | 0.59 | 0.59 | 0.59 | nan | nan | 0.59 | 0.59 |
| 1773 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_mean_3d_news | Multiple buys (n≥2) | mean | 3 | news | 3 | 66.7 | 0.58 | 1.23 | 1.74 | 3.07 | 0.19 | -2.76 | 3.27 |
| 1774 | 51 | 20.1 | Position +30% — hold ret_mean_2d_news | Position +30% | mean | 2 | news | 3 | 33.3 | 0.57 | -0.53 | 1.71 | 4.32 | 0.13 | -3.09 | 5.33 |
| 1775 | 26 | 50.0 | Qty ≥50k shares — hold ret_low_1d_news | Qty ≥50k shares | low | 1 | news | 2 | 50.0 | 0.56 | 0.56 | 1.13 | 1.22 | 0.46 | -0.3 | 1.43 |
| 1776 | 27 | 50.0 | Value ≥1M — hold ret_low_1d_news | Value ≥1M | low | 1 | news | 2 | 50.0 | 0.56 | 0.56 | 1.13 | 1.22 | 0.46 | -0.3 | 1.43 |
| 1777 | 51 | 20.1 | Position +30% — hold ret_mean_1d_news | Position +30% | mean | 1 | news | 3 | 33.3 | 0.56 | -0.66 | 1.67 | 4.88 | 0.11 | -3.6 | 5.93 |
| 1778 | 26 | 50.0 | Qty ≥50k shares — hold ret_low_2d_news | Qty ≥50k shares | low | 2 | news | 2 | 50.0 | 0.56 | 0.56 | 1.13 | 1.22 | 0.46 | -0.3 | 1.43 |
| 1779 | 27 | 50.0 | Value ≥1M — hold ret_low_2d_news | Value ≥1M | low | 2 | news | 2 | 50.0 | 0.56 | 0.56 | 1.13 | 1.22 | 0.46 | -0.3 | 1.43 |
| 1780 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_mean_5d_news | Far 52w high + Value ≥100k | mean | 5 | news | 3 | 33.3 | 0.55 | -1.35 | 1.64 | 3.83 | 0.14 | -1.96 | 4.95 |
| 1781 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_mean_30d_news | Large cap (≥2B) CEO/CFO | mean | 30 | news | 2 | 50.0 | 0.53 | 0.53 | 1.06 | 2.72 | 0.2 | -1.39 | 2.45 |
| 1782 | 37 | 35.58 | Director only + Value ≥100k — hold ret_mean_5d_news | Director only + Value ≥100k | mean | 5 | news | 3 | 33.3 | 0.52 | -1.09 | 1.57 | 3.02 | 0.17 | -1.35 | 4.01 |
| 1783 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_mean_14d_news | Large cap (≥3B) CEO/CFO | mean | 14 | news | 1 | 100.0 | 0.5 | 0.5 | 0.5 | nan | nan | 0.5 | 0.5 |
| 1784 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_mean_14d_news | Large cap (≥5B) CEO/CFO | mean | 14 | news | 1 | 100.0 | 0.5 | 0.5 | 0.5 | nan | nan | 0.5 | 0.5 |
| 1785 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_mean_14d_news | Large cap (≥10B) CEO/CFO | mean | 14 | news | 1 | 100.0 | 0.5 | 0.5 | 0.5 | nan | nan | 0.5 | 0.5 |
| 1786 | 6 | 77.62 | CEO only — hold ret_low_1d_news | CEO only | low | 1 | news | 3 | 66.7 | 0.49 | 1.43 | 1.48 | 2.27 | 0.22 | -2.1 | 2.15 |
| 1787 | 6 | 77.62 | CEO only — hold ret_low_2d_news | CEO only | low | 2 | news | 3 | 66.7 | 0.49 | 1.43 | 1.47 | 2.27 | 0.22 | -2.1 | 2.14 |
| 1788 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_mean_2d_news | Multiple buys (n≥2) | mean | 2 | news | 3 | 66.7 | 0.49 | 1.42 | 1.46 | 3.21 | 0.15 | -3.09 | 3.13 |
| 1789 | 40 | 33.74 | Director only + Position +10% — hold ret_mean_5d_news | Director only + Position +10% | mean | 5 | news | 4 | 25.0 | 0.49 | -0.34 | 1.97 | 2.39 | 0.21 | -1.35 | 4.01 |
| 1790 | 38 | 34.53 | Price < MA50 — hold ret_mean_5d_open | Price < MA50 | mean | 5 | open | 5 | 40.0 | 0.49 | -0.22 | 2.47 | 2.33 | 0.21 | -2.07 | 4.23 |
| 1791 | 30 | 48.32 | Value ≥100k — hold ret_mean_14d_news | Value ≥100k | mean | 14 | news | 6 | 83.3 | 0.49 | 0.97 | 2.91 | 10.51 | 0.05 | -18.03 | 14.49 |
| 1792 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_mean_1d_news | Mid cap (1B–10B) Value ≥100k | mean | 1 | news | 4 | 50.0 | 0.48 | 0.24 | 1.93 | 3.79 | 0.13 | -3.6 | 5.05 |
| 1793 | 33 | 41.81 | Director — hold ret_mean_5d_open | Director | mean | 5 | open | 8 | 50.0 | 0.48 | -0.09 | 3.8 | 2.22 | 0.21 | -2.07 | 4.23 |
| 1794 | 35 | 40.48 | Value ≥500k — hold ret_mean_10d_news | Value ≥500k | mean | 10 | news | 4 | 25.0 | 0.48 | -0.28 | 1.92 | 11.01 | 0.04 | -12.21 | 14.68 |
| 1795 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_mean_60d_news | CEO/CFO + Value ≥100k | mean | 60 | news | 3 | 66.7 | 0.46 | 0.89 | 1.38 | 4.23 | 0.11 | -3.97 | 4.46 |
| 1796 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_mean_60d_news | Large cap (≥750M) CEO/CFO | mean | 60 | news | 3 | 66.7 | 0.46 | 0.89 | 1.38 | 4.23 | 0.11 | -3.97 | 4.46 |
| 1797 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_mean_60d_news | Large cap (≥1B) CEO/CFO | mean | 60 | news | 3 | 66.7 | 0.46 | 0.89 | 1.38 | 4.23 | 0.11 | -3.97 | 4.46 |
| 1798 | 35 | 40.48 | Value ≥500k — hold ret_mean_10d_open | Value ≥500k | mean | 10 | open | 4 | 50.0 | 0.42 | 0.72 | 1.67 | 10.68 | 0.04 | -12.85 | 13.07 |
| 1799 | 39 | 34.48 | Position +20% — hold ret_mean_5d_open | Position +20% | mean | 5 | open | 4 | 50.0 | 0.4 | 0.27 | 1.61 | 2.18 | 0.18 | -2.07 | 3.15 |
| 1800 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_mean_1d_open | Mid cap (1B–10B) Value ≥100k | mean | 1 | open | 4 | 50.0 | 0.38 | 0.07 | 1.53 | 2.51 | 0.15 | -2.18 | 3.57 |
| 1801 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_mean_5d_news | Multiple buys (n≥2) | mean | 5 | news | 3 | 33.3 | 0.35 | -0.22 | 1.06 | 2.65 | 0.13 | -1.96 | 3.24 |
| 1802 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_mean_5d_open | Far 52w high + Value ≥100k | mean | 5 | open | 3 | 66.7 | 0.31 | 0.78 | 0.94 | 2.19 | 0.14 | -2.07 | 2.23 |
| 1803 | 33 | 41.81 | Director — hold ret_mean_5d_news | Director | mean | 5 | news | 8 | 37.5 | 0.28 | -0.34 | 2.2 | 2.17 | 0.13 | -1.96 | 4.01 |
| 1804 | 33 | 41.81 | Director — hold ret_mean_7d_open | Director | mean | 7 | open | 8 | 50.0 | 0.27 | -0.1 | 2.19 | 3.56 | 0.08 | -6.35 | 5.14 |
| 1805 | 33 | 41.81 | Director — hold ret_mean_30d_open | Director | mean | 30 | open | 8 | 62.5 | 0.27 | 2.21 | 2.18 | 8.99 | 0.03 | -19.99 | 10.42 |
| 1806 | 49 | 32.78 | CFO only — hold ret_high_1d_open | CFO only | high | 1 | open | 1 | 100.0 | 0.25 | 0.25 | 0.25 | nan | nan | 0.25 | 0.25 |
| 1807 | 48 | 32.78 | CFO + Director (combo) — hold ret_high_1d_open | CFO + Director (combo) | high | 1 | open | 1 | 100.0 | 0.25 | 0.25 | 0.25 | nan | nan | 0.25 | 0.25 |
| 1808 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_high_1d_open | CFO only + Value ≥50k | high | 1 | open | 1 | 100.0 | 0.25 | 0.25 | 0.25 | nan | nan | 0.25 | 0.25 |
| 1809 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_high_1d_open | CFO only + Value ≥100k | high | 1 | open | 1 | 100.0 | 0.25 | 0.25 | 0.25 | nan | nan | 0.25 | 0.25 |
| 1810 | 47 | 32.78 | CFO only + Position +10% — hold ret_high_1d_open | CFO only + Position +10% | high | 1 | open | 1 | 100.0 | 0.25 | 0.25 | 0.25 | nan | nan | 0.25 | 0.25 |
| 1811 | 46 | 32.78 | CFO only + Position +20% — hold ret_high_1d_open | CFO only + Position +20% | high | 1 | open | 1 | 100.0 | 0.25 | 0.25 | 0.25 | nan | nan | 0.25 | 0.25 |
| 1812 | 44 | 32.78 | RSI oversold (<30) — hold ret_high_1d_open | RSI oversold (<30) | high | 1 | open | 1 | 100.0 | 0.25 | 0.25 | 0.25 | nan | nan | 0.25 | 0.25 |
| 1813 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_high_1d_open | RSI oversold + CEO/CFO | high | 1 | open | 1 | 100.0 | 0.25 | 0.25 | 0.25 | nan | nan | 0.25 | 0.25 |
| 1814 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_high_1d_open | RSI oversold + Value ≥100k | high | 1 | open | 1 | 100.0 | 0.25 | 0.25 | 0.25 | nan | nan | 0.25 | 0.25 |
| 1815 | 22 | 53.36 | RSI overbought (>70) — hold ret_mean_1d_news | RSI overbought (>70) | mean | 1 | news | 2 | 50.0 | 0.24 | 0.24 | 0.48 | 2.33 | 0.1 | -1.41 | 1.89 |
| 1816 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_mean_60d_news | CEO only + Value ≥100k | mean | 60 | news | 2 | 50.0 | 0.24 | 0.24 | 0.49 | 5.96 | 0.04 | -3.97 | 4.46 |
| 1817 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_mean_60d_news | Price > MA50 + CEO/CFO | mean | 60 | news | 2 | 50.0 | 0.24 | 0.24 | 0.49 | 5.96 | 0.04 | -3.97 | 4.46 |
| 1818 | 30 | 48.32 | Value ≥100k — hold ret_mean_30d_news | Value ≥100k | mean | 30 | news | 6 | 66.7 | 0.22 | 2.29 | 1.32 | 10.85 | 0.02 | -19.4 | 13.57 |
| 1819 | 32 | 44.63 | Position +10% — hold ret_mean_14d_news | Position +10% | mean | 14 | news | 6 | 50.0 | 0.19 | 0.55 | 1.12 | 10.52 | 0.02 | -18.03 | 14.49 |
| 1820 | 32 | 44.63 | Position +10% — hold ret_mean_14d_open | Position +10% | mean | 14 | open | 6 | 50.0 | 0.18 | 1.57 | 1.09 | 10.4 | 0.02 | -18.64 | 12.89 |
| 1821 | 22 | 53.36 | RSI overbought (>70) — hold ret_mean_3d_open | RSI overbought (>70) | mean | 3 | open | 2 | 50.0 | 0.17 | 0.17 | 0.34 | 3.11 | 0.05 | -2.03 | 2.37 |
| 1822 | 36 | 36.54 | Director only (no C-level) — hold ret_mean_5d_news | Director only (no C-level) | mean | 5 | news | 6 | 33.3 | 0.15 | -0.34 | 0.92 | 1.96 | 0.08 | -1.35 | 4.01 |
| 1823 | 40 | 33.74 | Director only + Position +10% — hold ret_mean_5d_open | Director only + Position +10% | mean | 5 | open | 4 | 25.0 | 0.15 | -0.23 | 0.61 | 2.18 | 0.07 | -2.07 | 3.15 |
| 1824 | 38 | 34.53 | Price < MA50 — hold ret_mean_7d_open | Price < MA50 | mean | 7 | open | 5 | 60.0 | 0.14 | 0.07 | 0.69 | 4.22 | 0.03 | -6.35 | 5.14 |
| 1825 | 33 | 41.81 | Director — hold ret_mean_90d_open | Director | mean | 90 | open | 8 | 62.5 | 0.13 | 0.45 | 1.02 | 13.09 | 0.01 | -26.66 | 20.93 |
| 1826 | 26 | 50.0 | Qty ≥50k shares — hold ret_mean_10d_open | Qty ≥50k shares | mean | 10 | open | 2 | 50.0 | 0.11 | 0.11 | 0.22 | 18.33 | 0.01 | -12.85 | 13.07 |
| 1827 | 27 | 50.0 | Value ≥1M — hold ret_mean_10d_open | Value ≥1M | mean | 10 | open | 2 | 50.0 | 0.11 | 0.11 | 0.22 | 18.33 | 0.01 | -12.85 | 13.07 |
| 1828 | 21 | 53.67 | Qty ≥5k shares — hold ret_mean_60d_open | Qty ≥5k shares | mean | 60 | open | 6 | 83.3 | 0.1 | 3.35 | 0.61 | 15.3 | 0.01 | -28.92 | 17.06 |
| 1829 | 20 | 53.67 | Qty ≥10k shares — hold ret_mean_60d_open | Qty ≥10k shares | mean | 60 | open | 6 | 83.3 | 0.1 | 3.35 | 0.61 | 15.3 | 0.01 | -28.92 | 17.06 |
| 1830 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_mean_60d_open | CEO/CFO + Value ≥100k | mean | 60 | open | 3 | 66.7 | 0.08 | 2.99 | 0.23 | 5.67 | 0.01 | -6.46 | 3.7 |
| 1831 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_mean_60d_open | Large cap (≥750M) CEO/CFO | mean | 60 | open | 3 | 66.7 | 0.08 | 2.99 | 0.23 | 5.67 | 0.01 | -6.46 | 3.7 |
| 1832 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_mean_60d_open | Large cap (≥1B) CEO/CFO | mean | 60 | open | 3 | 66.7 | 0.08 | 2.99 | 0.23 | 5.67 | 0.01 | -6.46 | 3.7 |
| 1833 | 33 | 41.81 | Director — hold ret_mean_7d_news | Director | mean | 7 | news | 8 | 25.0 | 0.07 | -0.47 | 0.53 | 3.24 | 0.02 | -5.66 | 4.75 |
| 1834 | 39 | 34.48 | Position +20% — hold ret_mean_5d_news | Position +20% | mean | 5 | news | 4 | 25.0 | 0.06 | -0.91 | 0.23 | 2.71 | 0.02 | -1.96 | 4.01 |
| 1835 | 21 | 53.67 | Qty ≥5k shares — hold ret_mean_60d_news | Qty ≥5k shares | mean | 60 | news | 6 | 83.3 | 0.06 | 3.35 | 0.36 | 14.92 | 0.0 | -28.39 | 15.95 |
| 1836 | 20 | 53.67 | Qty ≥10k shares — hold ret_mean_60d_news | Qty ≥10k shares | mean | 60 | news | 6 | 83.3 | 0.06 | 3.35 | 0.36 | 14.92 | 0.0 | -28.39 | 15.95 |
| 1837 | 33 | 41.81 | Director — hold ret_mean_30d_news | Director | mean | 30 | news | 8 | 62.5 | 0.04 | 2.29 | 0.3 | 8.53 | 0.0 | -19.4 | 9.36 |
| 1838 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_low_1d_open | CEO only + Value ≥500k | low | 1 | open | 1 | 0.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0.0 | 0.0 |
| 1839 | 1 | 100.0 | CEO only + Position +10% — hold ret_low_1d_open | CEO only + Position +10% | low | 1 | open | 1 | 0.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0.0 | 0.0 |
| 1840 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_low_1d_open | Near 52w high + CEO/CFO | low | 1 | open | 1 | 0.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0.0 | 0.0 |
| 1841 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_low_2d_open | CEO only + Value ≥500k | low | 2 | open | 1 | 0.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0.0 | 0.0 |
| 1842 | 1 | 100.0 | CEO only + Position +10% — hold ret_low_2d_open | CEO only + Position +10% | low | 2 | open | 1 | 0.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0.0 | 0.0 |
| 1843 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_low_2d_open | Near 52w high + CEO/CFO | low | 2 | open | 1 | 0.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0.0 | 0.0 |
| 1844 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_low_3d_open | CEO only + Value ≥500k | low | 3 | open | 1 | 0.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0.0 | 0.0 |
| 1845 | 1 | 100.0 | CEO only + Position +10% — hold ret_low_3d_open | CEO only + Position +10% | low | 3 | open | 1 | 0.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0.0 | 0.0 |
| 1846 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_low_3d_open | Near 52w high + CEO/CFO | low | 3 | open | 1 | 0.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0.0 | 0.0 |
| 1847 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_low_5d_open | CEO only + Value ≥500k | low | 5 | open | 1 | 0.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0.0 | 0.0 |
| 1848 | 1 | 100.0 | CEO only + Position +10% — hold ret_low_5d_open | CEO only + Position +10% | low | 5 | open | 1 | 0.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0.0 | 0.0 |
| 1849 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_low_5d_open | Near 52w high + CEO/CFO | low | 5 | open | 1 | 0.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0.0 | 0.0 |
| 1850 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_low_7d_open | CEO only + Value ≥500k | low | 7 | open | 1 | 0.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0.0 | 0.0 |
| 1851 | 1 | 100.0 | CEO only + Position +10% — hold ret_low_7d_open | CEO only + Position +10% | low | 7 | open | 1 | 0.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0.0 | 0.0 |
| 1852 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_low_7d_open | Near 52w high + CEO/CFO | low | 7 | open | 1 | 0.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0.0 | 0.0 |
| 1853 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_low_10d_open | CEO only + Value ≥500k | low | 10 | open | 1 | 0.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0.0 | 0.0 |
| 1854 | 1 | 100.0 | CEO only + Position +10% — hold ret_low_10d_open | CEO only + Position +10% | low | 10 | open | 1 | 0.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0.0 | 0.0 |
| 1855 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_low_10d_open | Near 52w high + CEO/CFO | low | 10 | open | 1 | 0.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0.0 | 0.0 |
| 1856 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_low_14d_open | CEO only + Value ≥500k | low | 14 | open | 1 | 0.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0.0 | 0.0 |
| 1857 | 1 | 100.0 | CEO only + Position +10% — hold ret_low_14d_open | CEO only + Position +10% | low | 14 | open | 1 | 0.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0.0 | 0.0 |
| 1858 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_low_14d_open | Near 52w high + CEO/CFO | low | 14 | open | 1 | 0.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0.0 | 0.0 |
| 1859 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_low_30d_open | CEO only + Value ≥500k | low | 30 | open | 1 | 0.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0.0 | 0.0 |
| 1860 | 1 | 100.0 | CEO only + Position +10% — hold ret_low_30d_open | CEO only + Position +10% | low | 30 | open | 1 | 0.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0.0 | 0.0 |
| 1861 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_low_30d_open | Near 52w high + CEO/CFO | low | 30 | open | 1 | 0.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0.0 | 0.0 |
| 1862 | 49 | 32.78 | CFO only — hold ret_mean_3d_open | CFO only | mean | 3 | open | 1 | 0.0 | -0.04 | -0.04 | -0.04 | nan | nan | -0.04 | -0.04 |
| 1863 | 48 | 32.78 | CFO + Director (combo) — hold ret_mean_3d_open | CFO + Director (combo) | mean | 3 | open | 1 | 0.0 | -0.04 | -0.04 | -0.04 | nan | nan | -0.04 | -0.04 |
| 1864 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_mean_3d_open | CFO only + Value ≥50k | mean | 3 | open | 1 | 0.0 | -0.04 | -0.04 | -0.04 | nan | nan | -0.04 | -0.04 |
| 1865 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_mean_3d_open | CFO only + Value ≥100k | mean | 3 | open | 1 | 0.0 | -0.04 | -0.04 | -0.04 | nan | nan | -0.04 | -0.04 |
| 1866 | 47 | 32.78 | CFO only + Position +10% — hold ret_mean_3d_open | CFO only + Position +10% | mean | 3 | open | 1 | 0.0 | -0.04 | -0.04 | -0.04 | nan | nan | -0.04 | -0.04 |
| 1867 | 46 | 32.78 | CFO only + Position +20% — hold ret_mean_3d_open | CFO only + Position +20% | mean | 3 | open | 1 | 0.0 | -0.04 | -0.04 | -0.04 | nan | nan | -0.04 | -0.04 |
| 1868 | 44 | 32.78 | RSI oversold (<30) — hold ret_mean_3d_open | RSI oversold (<30) | mean | 3 | open | 1 | 0.0 | -0.04 | -0.04 | -0.04 | nan | nan | -0.04 | -0.04 |
| 1869 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_mean_3d_open | RSI oversold + CEO/CFO | mean | 3 | open | 1 | 0.0 | -0.04 | -0.04 | -0.04 | nan | nan | -0.04 | -0.04 |
| 1870 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_mean_3d_open | RSI oversold + Value ≥100k | mean | 3 | open | 1 | 0.0 | -0.04 | -0.04 | -0.04 | nan | nan | -0.04 | -0.04 |
| 1871 | 33 | 41.81 | Director — hold ret_mean_60d_open | Director | mean | 60 | open | 8 | 75.0 | -0.04 | 2.01 | -0.33 | 12.93 | -0.0 | -28.92 | 17.06 |
| 1872 | 51 | 20.1 | Position +30% — hold ret_mean_3d_news | Position +30% | mean | 3 | news | 3 | 33.3 | -0.08 | -0.46 | -0.24 | 2.89 | -0.03 | -2.76 | 2.98 |
| 1873 | 39 | 34.48 | Position +20% — hold ret_mean_7d_open | Position +20% | mean | 7 | open | 4 | 75.0 | -0.08 | 1.08 | -0.31 | 4.46 | -0.02 | -6.35 | 3.88 |
| 1874 | 33 | 41.81 | Director — hold ret_mean_10d_open | Director | mean | 10 | open | 8 | 62.5 | -0.09 | 0.3 | -0.74 | 5.79 | -0.02 | -12.85 | 6.98 |
| 1875 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_low_3d_news | Large cap (≥3B) CEO/CFO | low | 3 | news | 1 | 0.0 | -0.11 | -0.11 | -0.11 | nan | nan | -0.11 | -0.11 |
| 1876 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_low_3d_news | Large cap (≥5B) CEO/CFO | low | 3 | news | 1 | 0.0 | -0.11 | -0.11 | -0.11 | nan | nan | -0.11 | -0.11 |
| 1877 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_low_3d_news | Large cap (≥10B) CEO/CFO | low | 3 | news | 1 | 0.0 | -0.11 | -0.11 | -0.11 | nan | nan | -0.11 | -0.11 |
| 1878 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_low_5d_news | Large cap (≥3B) CEO/CFO | low | 5 | news | 1 | 0.0 | -0.11 | -0.11 | -0.11 | nan | nan | -0.11 | -0.11 |
| 1879 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_low_5d_news | Large cap (≥5B) CEO/CFO | low | 5 | news | 1 | 0.0 | -0.11 | -0.11 | -0.11 | nan | nan | -0.11 | -0.11 |
| 1880 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_low_5d_news | Large cap (≥10B) CEO/CFO | low | 5 | news | 1 | 0.0 | -0.11 | -0.11 | -0.11 | nan | nan | -0.11 | -0.11 |
| 1881 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_low_7d_news | Large cap (≥3B) CEO/CFO | low | 7 | news | 1 | 0.0 | -0.11 | -0.11 | -0.11 | nan | nan | -0.11 | -0.11 |
| 1882 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_low_7d_news | Large cap (≥5B) CEO/CFO | low | 7 | news | 1 | 0.0 | -0.11 | -0.11 | -0.11 | nan | nan | -0.11 | -0.11 |
| 1883 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_low_7d_news | Large cap (≥10B) CEO/CFO | low | 7 | news | 1 | 0.0 | -0.11 | -0.11 | -0.11 | nan | nan | -0.11 | -0.11 |
| 1884 | 33 | 41.81 | Director — hold ret_mean_90d_news | Director | mean | 90 | news | 8 | 62.5 | -0.11 | 0.06 | -0.88 | 12.76 | -0.01 | -26.12 | 19.78 |
| 1885 | 30 | 48.32 | Value ≥100k — hold ret_mean_14d_open | Value ≥100k | mean | 14 | open | 6 | 50.0 | -0.12 | 1.49 | -0.72 | 10.44 | -0.01 | -18.64 | 12.89 |
| 1886 | 22 | 53.36 | RSI overbought (>70) — hold ret_mean_2d_open | RSI overbought (>70) | mean | 2 | open | 2 | 50.0 | -0.14 | -0.14 | -0.27 | 2.75 | -0.05 | -2.08 | 1.81 |
| 1887 | 38 | 34.53 | Price < MA50 — hold ret_mean_5d_news | Price < MA50 | mean | 5 | news | 5 | 20.0 | -0.15 | -0.47 | -0.76 | 2.02 | -0.08 | -1.96 | 3.24 |
| 1888 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_mean_7d_news | Far 52w high + Value ≥100k | mean | 7 | news | 3 | 33.3 | -0.15 | -0.68 | -0.45 | 5.79 | -0.03 | -5.66 | 5.89 |
| 1889 | 15 | 62.43 | Price > MA50 — hold ret_low_1d_news | Price > MA50 | low | 1 | news | 5 | 60.0 | -0.17 | 0.84 | -0.84 | 2.37 | -0.07 | -3.47 | 2.15 |
| 1890 | 15 | 62.43 | Price > MA50 — hold ret_low_2d_news | Price > MA50 | low | 2 | news | 5 | 60.0 | -0.17 | 0.84 | -0.85 | 2.37 | -0.07 | -3.47 | 2.14 |
| 1891 | 28 | 48.48 | Tutti — hold ret_mean_60d_news | Tutti | mean | 60 | news | 10 | 70.0 | -0.18 | 1.57 | -1.78 | 11.24 | -0.02 | -28.39 | 15.95 |
| 1892 | 36 | 36.54 | Director only (no C-level) — hold ret_mean_5d_open | Director only (no C-level) | mean | 5 | open | 6 | 33.3 | -0.2 | -0.23 | -1.21 | 1.87 | -0.11 | -2.07 | 3.15 |
| 1893 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_mean_1d_news | Multiple buys (n≥2) | mean | 1 | news | 3 | 66.7 | -0.22 | 0.94 | -0.66 | 2.97 | -0.07 | -3.6 | 2.0 |
| 1894 | 15 | 62.43 | Price > MA50 — hold ret_mean_90d_open | Price > MA50 | mean | 90 | open | 5 | 40.0 | -0.22 | -0.78 | -1.1 | 4.66 | -0.05 | -5.65 | 6.78 |
| 1895 | 33 | 41.81 | Director — hold ret_mean_14d_open | Director | mean | 14 | open | 8 | 50.0 | -0.23 | 0.84 | -1.85 | 8.0 | -0.03 | -18.64 | 8.42 |
| 1896 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_low_1d_open | CEO only + Value ≥100k | low | 1 | open | 2 | 0.0 | -0.25 | -0.25 | -0.5 | 0.35 | -0.71 | -0.5 | 0.0 |
| 1897 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_low_1d_open | Price > MA50 + CEO/CFO | low | 1 | open | 2 | 0.0 | -0.25 | -0.25 | -0.5 | 0.35 | -0.71 | -0.5 | 0.0 |
| 1898 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_low_2d_open | CEO only + Value ≥100k | low | 2 | open | 2 | 0.0 | -0.25 | -0.25 | -0.5 | 0.35 | -0.71 | -0.5 | 0.0 |
| 1899 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_low_2d_open | Price > MA50 + CEO/CFO | low | 2 | open | 2 | 0.0 | -0.25 | -0.25 | -0.5 | 0.35 | -0.71 | -0.5 | 0.0 |
| 1900 | 49 | 32.78 | CFO only — hold ret_high_2d_news | CFO only | high | 2 | news | 1 | 0.0 | -0.26 | -0.26 | -0.26 | nan | nan | -0.26 | -0.26 |
| 1901 | 48 | 32.78 | CFO + Director (combo) — hold ret_high_2d_news | CFO + Director (combo) | high | 2 | news | 1 | 0.0 | -0.26 | -0.26 | -0.26 | nan | nan | -0.26 | -0.26 |
| 1902 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_high_2d_news | CFO only + Value ≥50k | high | 2 | news | 1 | 0.0 | -0.26 | -0.26 | -0.26 | nan | nan | -0.26 | -0.26 |
| 1903 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_high_2d_news | CFO only + Value ≥100k | high | 2 | news | 1 | 0.0 | -0.26 | -0.26 | -0.26 | nan | nan | -0.26 | -0.26 |
| 1904 | 47 | 32.78 | CFO only + Position +10% — hold ret_high_2d_news | CFO only + Position +10% | high | 2 | news | 1 | 0.0 | -0.26 | -0.26 | -0.26 | nan | nan | -0.26 | -0.26 |
| 1905 | 46 | 32.78 | CFO only + Position +20% — hold ret_high_2d_news | CFO only + Position +20% | high | 2 | news | 1 | 0.0 | -0.26 | -0.26 | -0.26 | nan | nan | -0.26 | -0.26 |
| 1906 | 44 | 32.78 | RSI oversold (<30) — hold ret_high_2d_news | RSI oversold (<30) | high | 2 | news | 1 | 0.0 | -0.26 | -0.26 | -0.26 | nan | nan | -0.26 | -0.26 |
| 1907 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_high_2d_news | RSI oversold + CEO/CFO | high | 2 | news | 1 | 0.0 | -0.26 | -0.26 | -0.26 | nan | nan | -0.26 | -0.26 |
| 1908 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_high_2d_news | RSI oversold + Value ≥100k | high | 2 | news | 1 | 0.0 | -0.26 | -0.26 | -0.26 | nan | nan | -0.26 | -0.26 |
| 1909 | 6 | 77.62 | CEO only — hold ret_low_3d_news | CEO only | low | 3 | news | 3 | 33.3 | -0.26 | -0.11 | -0.78 | 1.77 | -0.15 | -2.1 | 1.43 |
| 1910 | 6 | 77.62 | CEO only — hold ret_low_5d_news | CEO only | low | 5 | news | 3 | 33.3 | -0.26 | -0.11 | -0.78 | 1.77 | -0.15 | -2.1 | 1.43 |
| 1911 | 37 | 35.58 | Director only + Value ≥100k — hold ret_mean_5d_open | Director only + Value ≥100k | mean | 5 | open | 3 | 33.3 | -0.26 | -1.86 | -0.78 | 2.96 | -0.09 | -2.07 | 3.15 |
| 1912 | 6 | 77.62 | CEO only — hold ret_low_7d_news | CEO only | low | 7 | news | 3 | 33.3 | -0.26 | -0.11 | -0.78 | 1.77 | -0.15 | -2.1 | 1.43 |
| 1913 | 32 | 44.63 | Position +10% — hold ret_mean_30d_open | Position +10% | mean | 30 | open | 6 | 50.0 | -0.28 | 1.11 | -1.66 | 10.79 | -0.03 | -19.99 | 11.97 |
| 1914 | 32 | 44.63 | Position +10% — hold ret_mean_30d_news | Position +10% | mean | 30 | news | 6 | 50.0 | -0.28 | 0.68 | -1.68 | 10.81 | -0.03 | -19.4 | 13.57 |
| 1915 | 33 | 41.81 | Director — hold ret_mean_60d_news | Director | mean | 60 | news | 8 | 75.0 | -0.28 | 1.57 | -2.27 | 12.54 | -0.02 | -28.39 | 15.95 |
| 1916 | 53 | 0.0 | Qty ≥100k shares — hold ret_low_1d_news | Qty ≥100k shares | low | 1 | news | 1 | 0.0 | -0.3 | -0.3 | -0.3 | nan | nan | -0.3 | -0.3 |
| 1917 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_low_1d_news | Small cap (≤1B) Value ≥100k | low | 1 | news | 1 | 0.0 | -0.3 | -0.3 | -0.3 | nan | nan | -0.3 | -0.3 |
| 1918 | 53 | 0.0 | Qty ≥100k shares — hold ret_low_2d_news | Qty ≥100k shares | low | 2 | news | 1 | 0.0 | -0.3 | -0.3 | -0.3 | nan | nan | -0.3 | -0.3 |
| 1919 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_low_2d_news | Small cap (≤1B) Value ≥100k | low | 2 | news | 1 | 0.0 | -0.3 | -0.3 | -0.3 | nan | nan | -0.3 | -0.3 |
| 1920 | 21 | 53.67 | Qty ≥5k shares — hold ret_mean_90d_open | Qty ≥5k shares | mean | 90 | open | 6 | 50.0 | -0.3 | -0.09 | -1.79 | 15.51 | -0.02 | -26.66 | 20.93 |
| 1921 | 20 | 53.67 | Qty ≥10k shares — hold ret_mean_90d_open | Qty ≥10k shares | mean | 90 | open | 6 | 50.0 | -0.3 | -0.09 | -1.79 | 15.51 | -0.02 | -26.66 | 20.93 |
| 1922 | 33 | 41.81 | Director — hold ret_mean_10d_news | Director | mean | 10 | news | 8 | 50.0 | -0.31 | -0.01 | -2.47 | 5.41 | -0.06 | -12.21 | 5.96 |
| 1923 | 35 | 40.48 | Value ≥500k — hold ret_mean_30d_news | Value ≥500k | mean | 30 | news | 4 | 75.0 | -0.31 | 2.29 | -1.25 | 13.79 | -0.02 | -19.4 | 13.57 |
| 1924 | 40 | 33.74 | Director only + Position +10% — hold ret_mean_7d_news | Director only + Position +10% | mean | 7 | news | 4 | 25.0 | -0.33 | -0.21 | -1.32 | 4.25 | -0.08 | -5.66 | 4.75 |
| 1925 | 35 | 40.48 | Value ≥500k — hold ret_mean_30d_open | Value ≥500k | mean | 30 | open | 4 | 75.0 | -0.34 | 3.32 | -1.38 | 13.81 | -0.02 | -19.99 | 11.97 |
| 1926 | 21 | 53.67 | Qty ≥5k shares — hold ret_mean_90d_news | Qty ≥5k shares | mean | 90 | news | 6 | 50.0 | -0.34 | -0.61 | -2.07 | 15.08 | -0.02 | -26.12 | 19.78 |
| 1927 | 20 | 53.67 | Qty ≥10k shares — hold ret_mean_90d_news | Qty ≥10k shares | mean | 90 | news | 6 | 50.0 | -0.34 | -0.61 | -2.07 | 15.08 | -0.02 | -26.12 | 19.78 |
| 1928 | 49 | 32.78 | CFO only — hold ret_mean_10d_news | CFO only | mean | 10 | news | 1 | 0.0 | -0.36 | -0.36 | -0.36 | nan | nan | -0.36 | -0.36 |
| 1929 | 48 | 32.78 | CFO + Director (combo) — hold ret_mean_10d_news | CFO + Director (combo) | mean | 10 | news | 1 | 0.0 | -0.36 | -0.36 | -0.36 | nan | nan | -0.36 | -0.36 |
| 1930 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_mean_10d_news | CFO only + Value ≥50k | mean | 10 | news | 1 | 0.0 | -0.36 | -0.36 | -0.36 | nan | nan | -0.36 | -0.36 |
| 1931 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_mean_10d_news | CFO only + Value ≥100k | mean | 10 | news | 1 | 0.0 | -0.36 | -0.36 | -0.36 | nan | nan | -0.36 | -0.36 |
| 1932 | 47 | 32.78 | CFO only + Position +10% — hold ret_mean_10d_news | CFO only + Position +10% | mean | 10 | news | 1 | 0.0 | -0.36 | -0.36 | -0.36 | nan | nan | -0.36 | -0.36 |
| 1933 | 46 | 32.78 | CFO only + Position +20% — hold ret_mean_10d_news | CFO only + Position +20% | mean | 10 | news | 1 | 0.0 | -0.36 | -0.36 | -0.36 | nan | nan | -0.36 | -0.36 |
| 1934 | 44 | 32.78 | RSI oversold (<30) — hold ret_mean_10d_news | RSI oversold (<30) | mean | 10 | news | 1 | 0.0 | -0.36 | -0.36 | -0.36 | nan | nan | -0.36 | -0.36 |
| 1935 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_mean_10d_news | RSI oversold + CEO/CFO | mean | 10 | news | 1 | 0.0 | -0.36 | -0.36 | -0.36 | nan | nan | -0.36 | -0.36 |
| 1936 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_mean_10d_news | RSI oversold + Value ≥100k | mean | 10 | news | 1 | 0.0 | -0.36 | -0.36 | -0.36 | nan | nan | -0.36 | -0.36 |
| 1937 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_mean_7d_open | Far 52w high + Value ≥100k | mean | 7 | open | 3 | 66.7 | -0.37 | 2.09 | -1.11 | 5.21 | -0.07 | -6.35 | 3.15 |
| 1938 | 30 | 48.32 | Value ≥100k — hold ret_mean_30d_open | Value ≥100k | mean | 30 | open | 6 | 66.7 | -0.37 | 2.21 | -2.24 | 10.93 | -0.03 | -19.99 | 11.97 |
| 1939 | 49 | 32.78 | CFO only — hold ret_mean_2d_open | CFO only | mean | 2 | open | 1 | 0.0 | -0.38 | -0.38 | -0.38 | nan | nan | -0.38 | -0.38 |
| 1940 | 48 | 32.78 | CFO + Director (combo) — hold ret_mean_2d_open | CFO + Director (combo) | mean | 2 | open | 1 | 0.0 | -0.38 | -0.38 | -0.38 | nan | nan | -0.38 | -0.38 |
| 1941 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_mean_2d_open | CFO only + Value ≥50k | mean | 2 | open | 1 | 0.0 | -0.38 | -0.38 | -0.38 | nan | nan | -0.38 | -0.38 |
| 1942 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_mean_2d_open | CFO only + Value ≥100k | mean | 2 | open | 1 | 0.0 | -0.38 | -0.38 | -0.38 | nan | nan | -0.38 | -0.38 |
| 1943 | 47 | 32.78 | CFO only + Position +10% — hold ret_mean_2d_open | CFO only + Position +10% | mean | 2 | open | 1 | 0.0 | -0.38 | -0.38 | -0.38 | nan | nan | -0.38 | -0.38 |
| 1944 | 46 | 32.78 | CFO only + Position +20% — hold ret_mean_2d_open | CFO only + Position +20% | mean | 2 | open | 1 | 0.0 | -0.38 | -0.38 | -0.38 | nan | nan | -0.38 | -0.38 |
| 1945 | 44 | 32.78 | RSI oversold (<30) — hold ret_mean_2d_open | RSI oversold (<30) | mean | 2 | open | 1 | 0.0 | -0.38 | -0.38 | -0.38 | nan | nan | -0.38 | -0.38 |
| 1946 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_mean_2d_open | RSI oversold + CEO/CFO | mean | 2 | open | 1 | 0.0 | -0.38 | -0.38 | -0.38 | nan | nan | -0.38 | -0.38 |
| 1947 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_mean_2d_open | RSI oversold + Value ≥100k | mean | 2 | open | 1 | 0.0 | -0.38 | -0.38 | -0.38 | nan | nan | -0.38 | -0.38 |
| 1948 | 28 | 48.48 | Tutti — hold ret_mean_60d_open | Tutti | mean | 60 | open | 10 | 70.0 | -0.38 | 2.01 | -3.8 | 11.64 | -0.03 | -28.92 | 17.06 |
| 1949 | 35 | 40.48 | Value ≥500k — hold ret_mean_14d_news | Value ≥500k | mean | 14 | news | 4 | 75.0 | -0.4 | 0.97 | -1.6 | 13.37 | -0.03 | -18.03 | 14.49 |
| 1950 | 39 | 34.48 | Position +20% — hold ret_mean_7d_news | Position +20% | mean | 7 | news | 4 | 25.0 | -0.43 | -0.42 | -1.74 | 4.26 | -0.1 | -5.66 | 4.75 |
| 1951 | 35 | 40.48 | Value ≥500k — hold ret_mean_14d_open | Value ≥500k | mean | 14 | open | 4 | 50.0 | -0.44 | 2.0 | -1.76 | 13.29 | -0.03 | -18.64 | 12.89 |
| 1952 | 33 | 41.81 | Director — hold ret_mean_14d_news | Director | mean | 14 | news | 8 | 62.5 | -0.46 | 0.97 | -3.67 | 7.55 | -0.06 | -18.03 | 7.39 |
| 1953 | 36 | 36.54 | Director only (no C-level) — hold ret_mean_7d_news | Director only (no C-level) | mean | 7 | news | 6 | 16.7 | -0.49 | -0.53 | -2.93 | 3.3 | -0.15 | -5.66 | 4.75 |
| 1954 | 31 | 47.75 | Value ≥50k — hold ret_mean_60d_news | Value ≥50k | mean | 60 | news | 9 | 66.7 | -0.49 | 0.89 | -4.41 | 11.87 | -0.04 | -28.39 | 15.95 |
| 1955 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_low_1d_open | Large cap (≥3B) CEO/CFO | low | 1 | open | 1 | 0.0 | -0.5 | -0.5 | -0.5 | nan | nan | -0.5 | -0.5 |
| 1956 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_low_1d_open | Large cap (≥5B) CEO/CFO | low | 1 | open | 1 | 0.0 | -0.5 | -0.5 | -0.5 | nan | nan | -0.5 | -0.5 |
| 1957 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_low_1d_open | Large cap (≥10B) CEO/CFO | low | 1 | open | 1 | 0.0 | -0.5 | -0.5 | -0.5 | nan | nan | -0.5 | -0.5 |
| 1958 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_low_2d_open | Large cap (≥3B) CEO/CFO | low | 2 | open | 1 | 0.0 | -0.5 | -0.5 | -0.5 | nan | nan | -0.5 | -0.5 |
| 1959 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_low_2d_open | Large cap (≥5B) CEO/CFO | low | 2 | open | 1 | 0.0 | -0.5 | -0.5 | -0.5 | nan | nan | -0.5 | -0.5 |
| 1960 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_low_2d_open | Large cap (≥10B) CEO/CFO | low | 2 | open | 1 | 0.0 | -0.5 | -0.5 | -0.5 | nan | nan | -0.5 | -0.5 |
| 1961 | 51 | 20.1 | Position +30% — hold ret_mean_5d_open | Position +30% | mean | 5 | open | 3 | 33.3 | -0.51 | -0.25 | -1.54 | 1.44 | -0.36 | -2.07 | 0.78 |
| 1962 | 26 | 50.0 | Qty ≥50k shares — hold ret_low_1d_open | Qty ≥50k shares | low | 1 | open | 2 | 0.0 | -0.52 | -0.52 | -1.03 | 0.73 | -0.71 | -1.03 | 0.0 |
| 1963 | 27 | 50.0 | Value ≥1M — hold ret_low_1d_open | Value ≥1M | low | 1 | open | 2 | 0.0 | -0.52 | -0.52 | -1.03 | 0.73 | -0.71 | -1.03 | 0.0 |
| 1964 | 26 | 50.0 | Qty ≥50k shares — hold ret_low_2d_open | Qty ≥50k shares | low | 2 | open | 2 | 0.0 | -0.52 | -0.52 | -1.03 | 0.73 | -0.71 | -1.03 | 0.0 |
| 1965 | 27 | 50.0 | Value ≥1M — hold ret_low_2d_open | Value ≥1M | low | 2 | open | 2 | 0.0 | -0.52 | -0.52 | -1.03 | 0.73 | -0.71 | -1.03 | 0.0 |
| 1966 | 38 | 34.53 | Price < MA50 — hold ret_mean_7d_news | Price < MA50 | mean | 7 | news | 5 | 20.0 | -0.52 | -0.26 | -2.61 | 3.48 | -0.15 | -5.66 | 4.14 |
| 1967 | 28 | 48.48 | Tutti — hold ret_mean_90d_news | Tutti | mean | 90 | news | 10 | 50.0 | -0.53 | -0.61 | -5.3 | 11.29 | -0.05 | -26.12 | 19.78 |
| 1968 | 6 | 77.62 | CEO only — hold ret_low_1d_open | CEO only | low | 1 | open | 3 | 0.0 | -0.55 | -0.5 | -1.65 | 0.58 | -0.95 | -1.15 | 0.0 |
| 1969 | 6 | 77.62 | CEO only — hold ret_low_2d_open | CEO only | low | 2 | open | 3 | 0.0 | -0.55 | -0.5 | -1.65 | 0.58 | -0.95 | -1.15 | 0.0 |
| 1970 | 22 | 53.36 | RSI overbought (>70) — hold ret_mean_1d_open | RSI overbought (>70) | mean | 1 | open | 2 | 50.0 | -0.57 | -0.57 | -1.13 | 2.28 | -0.25 | -2.18 | 1.05 |
| 1971 | 37 | 35.58 | Director only + Value ≥100k — hold ret_mean_7d_news | Director only + Value ≥100k | mean | 7 | news | 3 | 33.3 | -0.57 | -0.81 | -1.72 | 5.21 | -0.11 | -5.66 | 4.75 |
| 1972 | 38 | 34.53 | Price < MA50 — hold ret_mean_10d_open | Price < MA50 | mean | 10 | open | 5 | 80.0 | -0.57 | 0.4 | -2.86 | 7.39 | -0.08 | -12.85 | 6.98 |
| 1973 | 40 | 33.74 | Director only + Position +10% — hold ret_mean_7d_open | Director only + Position +10% | mean | 7 | open | 4 | 50.0 | -0.66 | -0.1 | -2.66 | 4.23 | -0.16 | -6.35 | 3.88 |
| 1974 | 49 | 32.78 | CFO only — hold ret_mean_7d_news | CFO only | mean | 7 | news | 1 | 0.0 | -0.68 | -0.68 | -0.68 | nan | nan | -0.68 | -0.68 |
| 1975 | 48 | 32.78 | CFO + Director (combo) — hold ret_mean_7d_news | CFO + Director (combo) | mean | 7 | news | 1 | 0.0 | -0.68 | -0.68 | -0.68 | nan | nan | -0.68 | -0.68 |
| 1976 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_mean_7d_news | CFO only + Value ≥50k | mean | 7 | news | 1 | 0.0 | -0.68 | -0.68 | -0.68 | nan | nan | -0.68 | -0.68 |
| 1977 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_mean_7d_news | CFO only + Value ≥100k | mean | 7 | news | 1 | 0.0 | -0.68 | -0.68 | -0.68 | nan | nan | -0.68 | -0.68 |
| 1978 | 47 | 32.78 | CFO only + Position +10% — hold ret_mean_7d_news | CFO only + Position +10% | mean | 7 | news | 1 | 0.0 | -0.68 | -0.68 | -0.68 | nan | nan | -0.68 | -0.68 |
| 1979 | 46 | 32.78 | CFO only + Position +20% — hold ret_mean_7d_news | CFO only + Position +20% | mean | 7 | news | 1 | 0.0 | -0.68 | -0.68 | -0.68 | nan | nan | -0.68 | -0.68 |
| 1980 | 44 | 32.78 | RSI oversold (<30) — hold ret_mean_7d_news | RSI oversold (<30) | mean | 7 | news | 1 | 0.0 | -0.68 | -0.68 | -0.68 | nan | nan | -0.68 | -0.68 |
| 1981 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_mean_7d_news | RSI oversold + CEO/CFO | mean | 7 | news | 1 | 0.0 | -0.68 | -0.68 | -0.68 | nan | nan | -0.68 | -0.68 |
| 1982 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_mean_7d_news | RSI oversold + Value ≥100k | mean | 7 | news | 1 | 0.0 | -0.68 | -0.68 | -0.68 | nan | nan | -0.68 | -0.68 |
| 1983 | 15 | 62.43 | Price > MA50 — hold ret_low_3d_news | Price > MA50 | low | 3 | news | 5 | 40.0 | -0.69 | -0.11 | -3.43 | 2.06 | -0.33 | -3.47 | 1.43 |
| 1984 | 31 | 47.75 | Value ≥50k — hold ret_mean_60d_open | Value ≥50k | mean | 60 | open | 9 | 66.7 | -0.71 | 1.39 | -6.43 | 12.3 | -0.06 | -28.92 | 17.06 |
| 1985 | 31 | 47.75 | Value ≥50k — hold ret_mean_90d_news | Value ≥50k | mean | 90 | news | 9 | 44.4 | -0.72 | -1.27 | -6.51 | 11.96 | -0.06 | -26.12 | 19.78 |
| 1986 | 28 | 48.48 | Tutti — hold ret_mean_90d_open | Tutti | mean | 90 | open | 10 | 50.0 | -0.73 | -0.24 | -7.29 | 11.7 | -0.06 | -26.66 | 20.93 |
| 1987 | 14 | 65.45 | Price > MA200 — hold ret_low_1d_news | Price > MA200 | low | 1 | news | 4 | 50.0 | -0.75 | -0.48 | -2.99 | 2.29 | -0.33 | -3.47 | 1.43 |
| 1988 | 14 | 65.45 | Price > MA200 — hold ret_low_2d_news | Price > MA200 | low | 2 | news | 4 | 50.0 | -0.75 | -0.48 | -2.99 | 2.29 | -0.33 | -3.47 | 1.43 |
| 1989 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_low_1d_news | CEO/CFO + Value ≥100k | low | 1 | news | 3 | 66.7 | -0.77 | 1.43 | -2.32 | 4.45 | -0.17 | -5.9 | 2.15 |
| 1990 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_low_1d_news | Large cap (≥750M) CEO/CFO | low | 1 | news | 3 | 66.7 | -0.77 | 1.43 | -2.32 | 4.45 | -0.17 | -5.9 | 2.15 |
| 1991 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_low_1d_news | Large cap (≥1B) CEO/CFO | low | 1 | news | 3 | 66.7 | -0.77 | 1.43 | -2.32 | 4.45 | -0.17 | -5.9 | 2.15 |
| 1992 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_low_2d_news | CEO/CFO + Value ≥100k | low | 2 | news | 3 | 66.7 | -0.78 | 1.43 | -2.33 | 4.45 | -0.17 | -5.9 | 2.14 |
| 1993 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_low_2d_news | Large cap (≥750M) CEO/CFO | low | 2 | news | 3 | 66.7 | -0.78 | 1.43 | -2.33 | 4.45 | -0.17 | -5.9 | 2.14 |
| 1994 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_low_2d_news | Large cap (≥1B) CEO/CFO | low | 2 | news | 3 | 66.7 | -0.78 | 1.43 | -2.33 | 4.45 | -0.17 | -5.9 | 2.14 |
| 1995 | 14 | 65.45 | Price > MA200 — hold ret_low_3d_news | Price > MA200 | low | 3 | news | 4 | 50.0 | -0.83 | -0.64 | -3.32 | 2.35 | -0.35 | -3.47 | 1.43 |
| 1996 | 36 | 36.54 | Director only (no C-level) — hold ret_mean_7d_open | Director only (no C-level) | mean | 7 | open | 6 | 33.3 | -0.84 | -0.53 | -5.04 | 3.3 | -0.25 | -6.35 | 3.88 |
| 1997 | 30 | 48.32 | Value ≥100k — hold ret_low_1d_news | Value ≥100k | low | 1 | news | 6 | 50.0 | -0.88 | 0.27 | -5.25 | 3.15 | -0.28 | -5.9 | 2.15 |
| 1998 | 30 | 48.32 | Value ≥100k — hold ret_low_2d_news | Value ≥100k | low | 2 | news | 6 | 50.0 | -0.88 | 0.27 | -5.26 | 3.15 | -0.28 | -5.9 | 2.14 |
| 1999 | 49 | 32.78 | CFO only — hold ret_mean_1d_open | CFO only | mean | 1 | open | 1 | 0.0 | -0.91 | -0.91 | -0.91 | nan | nan | -0.91 | -0.91 |
| 2000 | 48 | 32.78 | CFO + Director (combo) — hold ret_mean_1d_open | CFO + Director (combo) | mean | 1 | open | 1 | 0.0 | -0.91 | -0.91 | -0.91 | nan | nan | -0.91 | -0.91 |
| 2001 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_mean_1d_open | CFO only + Value ≥50k | mean | 1 | open | 1 | 0.0 | -0.91 | -0.91 | -0.91 | nan | nan | -0.91 | -0.91 |
| 2002 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_mean_1d_open | CFO only + Value ≥100k | mean | 1 | open | 1 | 0.0 | -0.91 | -0.91 | -0.91 | nan | nan | -0.91 | -0.91 |
| 2003 | 47 | 32.78 | CFO only + Position +10% — hold ret_mean_1d_open | CFO only + Position +10% | mean | 1 | open | 1 | 0.0 | -0.91 | -0.91 | -0.91 | nan | nan | -0.91 | -0.91 |
| 2004 | 46 | 32.78 | CFO only + Position +20% — hold ret_mean_1d_open | CFO only + Position +20% | mean | 1 | open | 1 | 0.0 | -0.91 | -0.91 | -0.91 | nan | nan | -0.91 | -0.91 |
| 2005 | 44 | 32.78 | RSI oversold (<30) — hold ret_mean_1d_open | RSI oversold (<30) | mean | 1 | open | 1 | 0.0 | -0.91 | -0.91 | -0.91 | nan | nan | -0.91 | -0.91 |
| 2006 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_mean_1d_open | RSI oversold + CEO/CFO | mean | 1 | open | 1 | 0.0 | -0.91 | -0.91 | -0.91 | nan | nan | -0.91 | -0.91 |
| 2007 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_mean_1d_open | RSI oversold + Value ≥100k | mean | 1 | open | 1 | 0.0 | -0.91 | -0.91 | -0.91 | nan | nan | -0.91 | -0.91 |
| 2008 | 31 | 47.75 | Value ≥50k — hold ret_mean_90d_open | Value ≥50k | mean | 90 | open | 9 | 44.4 | -0.94 | -0.78 | -8.5 | 12.39 | -0.08 | -26.66 | 20.93 |
| 2009 | 40 | 33.74 | Director only + Position +10% — hold ret_low_1d_news | Director only + Position +10% | low | 1 | news | 4 | 25.0 | -0.97 | -1.12 | -3.89 | 1.52 | -0.64 | -2.49 | 0.84 |
| 2010 | 40 | 33.74 | Director only + Position +10% — hold ret_low_2d_news | Director only + Position +10% | low | 2 | news | 4 | 25.0 | -0.97 | -1.12 | -3.89 | 1.52 | -0.64 | -2.49 | 0.84 |
| 2011 | 37 | 35.58 | Director only + Value ≥100k — hold ret_low_1d_news | Director only + Value ≥100k | low | 1 | news | 3 | 33.3 | -0.98 | -0.3 | -2.93 | 2.23 | -0.44 | -3.47 | 0.84 |
| 2012 | 37 | 35.58 | Director only + Value ≥100k — hold ret_low_2d_news | Director only + Value ≥100k | low | 2 | news | 3 | 33.3 | -0.98 | -0.3 | -2.93 | 2.23 | -0.44 | -3.47 | 0.84 |
| 2013 | 53 | 0.0 | Qty ≥100k shares — hold ret_low_1d_open | Qty ≥100k shares | low | 1 | open | 1 | 0.0 | -1.03 | -1.03 | -1.03 | nan | nan | -1.03 | -1.03 |
| 2014 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_low_1d_open | Small cap (≤1B) Value ≥100k | low | 1 | open | 1 | 0.0 | -1.03 | -1.03 | -1.03 | nan | nan | -1.03 | -1.03 |
| 2015 | 53 | 0.0 | Qty ≥100k shares — hold ret_low_2d_open | Qty ≥100k shares | low | 2 | open | 1 | 0.0 | -1.03 | -1.03 | -1.03 | nan | nan | -1.03 | -1.03 |
| 2016 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_low_2d_open | Small cap (≤1B) Value ≥100k | low | 2 | open | 1 | 0.0 | -1.03 | -1.03 | -1.03 | nan | nan | -1.03 | -1.03 |
| 2017 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_mean_90d_open | Mid cap (1B–10B) CEO/CFO | mean | 90 | open | 2 | 50.0 | -1.03 | -1.03 | -2.06 | 2.31 | -0.45 | -2.66 | 0.6 |
| 2018 | 10 | 66.41 | CEO/CFO — hold ret_low_1d_news | CEO/CFO | low | 1 | news | 4 | 50.0 | -1.1 | -0.34 | -4.42 | 3.7 | -0.3 | -5.9 | 2.15 |
| 2019 | 11 | 66.41 | Officer/President — hold ret_low_1d_news | Officer/President | low | 1 | news | 4 | 50.0 | -1.1 | -0.34 | -4.42 | 3.7 | -0.3 | -5.9 | 2.15 |
| 2020 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_low_1d_news | Large cap (≥250M) CEO/CFO | low | 1 | news | 4 | 50.0 | -1.1 | -0.34 | -4.42 | 3.7 | -0.3 | -5.9 | 2.15 |
| 2021 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_low_1d_news | Large cap (≥500M) CEO/CFO | low | 1 | news | 4 | 50.0 | -1.1 | -0.34 | -4.42 | 3.7 | -0.3 | -5.9 | 2.15 |
| 2022 | 10 | 66.41 | CEO/CFO — hold ret_low_2d_news | CEO/CFO | low | 2 | news | 4 | 50.0 | -1.11 | -0.34 | -4.43 | 3.69 | -0.3 | -5.9 | 2.14 |
| 2023 | 11 | 66.41 | Officer/President — hold ret_low_2d_news | Officer/President | low | 2 | news | 4 | 50.0 | -1.11 | -0.34 | -4.43 | 3.69 | -0.3 | -5.9 | 2.14 |
| 2024 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_low_2d_news | Large cap (≥250M) CEO/CFO | low | 2 | news | 4 | 50.0 | -1.11 | -0.34 | -4.43 | 3.69 | -0.3 | -5.9 | 2.14 |
| 2025 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_low_2d_news | Large cap (≥500M) CEO/CFO | low | 2 | news | 4 | 50.0 | -1.11 | -0.34 | -4.43 | 3.69 | -0.3 | -5.9 | 2.14 |
| 2026 | 4 | 82.51 | CEO + Director (combo) — hold ret_low_1d_open | CEO + Director (combo) | low | 1 | open | 1 | 0.0 | -1.15 | -1.15 | -1.15 | nan | nan | -1.15 | -1.15 |
| 2027 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_low_1d_open | Small cap (≤1B) CEO/CFO | low | 1 | open | 1 | 0.0 | -1.15 | -1.15 | -1.15 | nan | nan | -1.15 | -1.15 |
| 2028 | 4 | 82.51 | CEO + Director (combo) — hold ret_low_2d_open | CEO + Director (combo) | low | 2 | open | 1 | 0.0 | -1.15 | -1.15 | -1.15 | nan | nan | -1.15 | -1.15 |
| 2029 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_low_2d_open | Small cap (≤1B) CEO/CFO | low | 2 | open | 1 | 0.0 | -1.15 | -1.15 | -1.15 | nan | nan | -1.15 | -1.15 |
| 2030 | 4 | 82.51 | CEO + Director (combo) — hold ret_low_3d_open | CEO + Director (combo) | low | 3 | open | 1 | 0.0 | -1.15 | -1.15 | -1.15 | nan | nan | -1.15 | -1.15 |
| 2031 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_low_3d_open | Small cap (≤1B) CEO/CFO | low | 3 | open | 1 | 0.0 | -1.15 | -1.15 | -1.15 | nan | nan | -1.15 | -1.15 |
| 2032 | 4 | 82.51 | CEO + Director (combo) — hold ret_low_5d_open | CEO + Director (combo) | low | 5 | open | 1 | 0.0 | -1.15 | -1.15 | -1.15 | nan | nan | -1.15 | -1.15 |
| 2033 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_low_5d_open | Small cap (≤1B) CEO/CFO | low | 5 | open | 1 | 0.0 | -1.15 | -1.15 | -1.15 | nan | nan | -1.15 | -1.15 |
| 2034 | 4 | 82.51 | CEO + Director (combo) — hold ret_low_7d_open | CEO + Director (combo) | low | 7 | open | 1 | 0.0 | -1.15 | -1.15 | -1.15 | nan | nan | -1.15 | -1.15 |
| 2035 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_low_7d_open | Small cap (≤1B) CEO/CFO | low | 7 | open | 1 | 0.0 | -1.15 | -1.15 | -1.15 | nan | nan | -1.15 | -1.15 |
| 2036 | 4 | 82.51 | CEO + Director (combo) — hold ret_low_10d_open | CEO + Director (combo) | low | 10 | open | 1 | 0.0 | -1.15 | -1.15 | -1.15 | nan | nan | -1.15 | -1.15 |
| 2037 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_low_10d_open | Small cap (≤1B) CEO/CFO | low | 10 | open | 1 | 0.0 | -1.15 | -1.15 | -1.15 | nan | nan | -1.15 | -1.15 |
| 2038 | 4 | 82.51 | CEO + Director (combo) — hold ret_low_14d_open | CEO + Director (combo) | low | 14 | open | 1 | 0.0 | -1.15 | -1.15 | -1.15 | nan | nan | -1.15 | -1.15 |
| 2039 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_low_14d_open | Small cap (≤1B) CEO/CFO | low | 14 | open | 1 | 0.0 | -1.15 | -1.15 | -1.15 | nan | nan | -1.15 | -1.15 |
| 2040 | 4 | 82.51 | CEO + Director (combo) — hold ret_low_30d_open | CEO + Director (combo) | low | 30 | open | 1 | 0.0 | -1.15 | -1.15 | -1.15 | nan | nan | -1.15 | -1.15 |
| 2041 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_low_30d_open | Small cap (≤1B) CEO/CFO | low | 30 | open | 1 | 0.0 | -1.15 | -1.15 | -1.15 | nan | nan | -1.15 | -1.15 |
| 2042 | 4 | 82.51 | CEO + Director (combo) — hold ret_low_60d_open | CEO + Director (combo) | low | 60 | open | 1 | 0.0 | -1.15 | -1.15 | -1.15 | nan | nan | -1.15 | -1.15 |
| 2043 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_low_60d_open | Small cap (≤1B) CEO/CFO | low | 60 | open | 1 | 0.0 | -1.15 | -1.15 | -1.15 | nan | nan | -1.15 | -1.15 |
| 2044 | 4 | 82.51 | CEO + Director (combo) — hold ret_low_90d_open | CEO + Director (combo) | low | 90 | open | 1 | 0.0 | -1.15 | -1.15 | -1.15 | nan | nan | -1.15 | -1.15 |
| 2045 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_low_90d_open | Small cap (≤1B) CEO/CFO | low | 90 | open | 1 | 0.0 | -1.15 | -1.15 | -1.15 | nan | nan | -1.15 | -1.15 |
| 2046 | 10 | 66.41 | CEO/CFO — hold ret_low_1d_open | CEO/CFO | low | 1 | open | 4 | 0.0 | -1.23 | -0.82 | -4.93 | 1.44 | -0.85 | -3.28 | 0.0 |
| 2047 | 11 | 66.41 | Officer/President — hold ret_low_1d_open | Officer/President | low | 1 | open | 4 | 0.0 | -1.23 | -0.82 | -4.93 | 1.44 | -0.85 | -3.28 | 0.0 |
| 2048 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_low_1d_open | Large cap (≥250M) CEO/CFO | low | 1 | open | 4 | 0.0 | -1.23 | -0.82 | -4.93 | 1.44 | -0.85 | -3.28 | 0.0 |
| 2049 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_low_1d_open | Large cap (≥500M) CEO/CFO | low | 1 | open | 4 | 0.0 | -1.23 | -0.82 | -4.93 | 1.44 | -0.85 | -3.28 | 0.0 |
| 2050 | 10 | 66.41 | CEO/CFO — hold ret_low_2d_open | CEO/CFO | low | 2 | open | 4 | 0.0 | -1.23 | -0.82 | -4.93 | 1.44 | -0.85 | -3.28 | 0.0 |
| 2051 | 11 | 66.41 | Officer/President — hold ret_low_2d_open | Officer/President | low | 2 | open | 4 | 0.0 | -1.23 | -0.82 | -4.93 | 1.44 | -0.85 | -3.28 | 0.0 |
| 2052 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_low_2d_open | Large cap (≥250M) CEO/CFO | low | 2 | open | 4 | 0.0 | -1.23 | -0.82 | -4.93 | 1.44 | -0.85 | -3.28 | 0.0 |
| 2053 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_low_2d_open | Large cap (≥500M) CEO/CFO | low | 2 | open | 4 | 0.0 | -1.23 | -0.82 | -4.93 | 1.44 | -0.85 | -3.28 | 0.0 |
| 2054 | 38 | 34.53 | Price < MA50 — hold ret_mean_90d_open | Price < MA50 | mean | 90 | open | 5 | 60.0 | -1.24 | 0.3 | -6.19 | 16.91 | -0.07 | -26.66 | 20.93 |
| 2055 | 38 | 34.53 | Price < MA50 — hold ret_mean_10d_news | Price < MA50 | mean | 10 | news | 5 | 60.0 | -1.25 | 0.18 | -6.24 | 6.65 | -0.19 | -12.21 | 5.96 |
| 2056 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_low_1d_open | CEO/CFO + Value ≥100k | low | 1 | open | 3 | 0.0 | -1.26 | -0.5 | -3.78 | 1.77 | -0.71 | -3.28 | 0.0 |
| 2057 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_low_1d_open | Large cap (≥750M) CEO/CFO | low | 1 | open | 3 | 0.0 | -1.26 | -0.5 | -3.78 | 1.77 | -0.71 | -3.28 | 0.0 |
| 2058 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_low_1d_open | Large cap (≥1B) CEO/CFO | low | 1 | open | 3 | 0.0 | -1.26 | -0.5 | -3.78 | 1.77 | -0.71 | -3.28 | 0.0 |
| 2059 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_low_2d_open | CEO/CFO + Value ≥100k | low | 2 | open | 3 | 0.0 | -1.26 | -0.5 | -3.78 | 1.77 | -0.71 | -3.28 | 0.0 |
| 2060 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_low_2d_open | Large cap (≥750M) CEO/CFO | low | 2 | open | 3 | 0.0 | -1.26 | -0.5 | -3.78 | 1.77 | -0.71 | -3.28 | 0.0 |
| 2061 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_low_2d_open | Large cap (≥1B) CEO/CFO | low | 2 | open | 3 | 0.0 | -1.26 | -0.5 | -3.78 | 1.77 | -0.71 | -3.28 | 0.0 |
| 2062 | 51 | 20.1 | Position +30% — hold ret_mean_5d_news | Position +30% | mean | 5 | news | 3 | 0.0 | -1.26 | -1.35 | -3.78 | 0.75 | -1.68 | -1.96 | -0.47 |
| 2063 | 38 | 34.53 | Price < MA50 — hold ret_mean_30d_open | Price < MA50 | mean | 30 | open | 5 | 40.0 | -1.26 | -0.87 | -6.3 | 11.52 | -0.11 | -19.99 | 10.42 |
| 2064 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_mean_90d_news | CEO only + Value ≥500k | mean | 90 | news | 1 | 0.0 | -1.27 | -1.27 | -1.27 | nan | nan | -1.27 | -1.27 |
| 2065 | 1 | 100.0 | CEO only + Position +10% — hold ret_mean_90d_news | CEO only + Position +10% | mean | 90 | news | 1 | 0.0 | -1.27 | -1.27 | -1.27 | nan | nan | -1.27 | -1.27 |
| 2066 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_mean_90d_news | Near 52w high + CEO/CFO | mean | 90 | news | 1 | 0.0 | -1.27 | -1.27 | -1.27 | nan | nan | -1.27 | -1.27 |
| 2067 | 6 | 77.62 | CEO only — hold ret_low_3d_open | CEO only | low | 3 | open | 3 | 0.0 | -1.28 | -1.15 | -3.85 | 1.35 | -0.95 | -2.7 | 0.0 |
| 2068 | 6 | 77.62 | CEO only — hold ret_low_5d_open | CEO only | low | 5 | open | 3 | 0.0 | -1.28 | -1.15 | -3.85 | 1.35 | -0.95 | -2.7 | 0.0 |
| 2069 | 6 | 77.62 | CEO only — hold ret_low_7d_open | CEO only | low | 7 | open | 3 | 0.0 | -1.28 | -1.15 | -3.85 | 1.35 | -0.95 | -2.7 | 0.0 |
| 2070 | 15 | 62.43 | Price > MA50 — hold ret_low_1d_open | Price > MA50 | low | 1 | open | 5 | 0.0 | -1.3 | -0.5 | -6.51 | 1.79 | -0.73 | -4.22 | 0.0 |
| 2071 | 15 | 62.43 | Price > MA50 — hold ret_low_2d_open | Price > MA50 | low | 2 | open | 5 | 0.0 | -1.3 | -0.5 | -6.51 | 1.79 | -0.73 | -4.22 | 0.0 |
| 2072 | 38 | 34.53 | Price < MA50 — hold ret_mean_14d_open | Price < MA50 | mean | 14 | open | 5 | 40.0 | -1.3 | -0.01 | -6.52 | 10.34 | -0.13 | -18.64 | 8.42 |
| 2073 | 40 | 33.74 | Director only + Position +10% — hold ret_low_1d_open | Director only + Position +10% | low | 1 | open | 4 | 0.0 | -1.31 | -1.48 | -5.24 | 1.02 | -1.29 | -2.27 | 0.0 |
| 2074 | 31 | 47.75 | Value ≥50k — hold ret_low_1d_news | Value ≥50k | low | 1 | news | 9 | 33.3 | -1.31 | -1.94 | -11.78 | 2.58 | -0.51 | -5.9 | 2.15 |
| 2075 | 40 | 33.74 | Director only + Position +10% — hold ret_low_2d_open | Director only + Position +10% | low | 2 | open | 4 | 0.0 | -1.31 | -1.48 | -5.24 | 1.02 | -1.29 | -2.27 | 0.0 |
| 2076 | 31 | 47.75 | Value ≥50k — hold ret_low_2d_news | Value ≥50k | low | 2 | news | 9 | 33.3 | -1.31 | -1.94 | -11.79 | 2.58 | -0.51 | -5.9 | 2.14 |
| 2077 | 22 | 53.36 | RSI overbought (>70) — hold ret_low_1d_news | RSI overbought (>70) | low | 1 | news | 2 | 50.0 | -1.32 | -1.32 | -2.63 | 3.05 | -0.43 | -3.47 | 0.84 |
| 2078 | 22 | 53.36 | RSI overbought (>70) — hold ret_low_2d_news | RSI overbought (>70) | low | 2 | news | 2 | 50.0 | -1.32 | -1.32 | -2.63 | 3.05 | -0.43 | -3.47 | 0.84 |
| 2079 | 22 | 53.36 | RSI overbought (>70) — hold ret_low_3d_news | RSI overbought (>70) | low | 3 | news | 2 | 50.0 | -1.32 | -1.32 | -2.63 | 3.05 | -0.43 | -3.47 | 0.84 |
| 2080 | 22 | 53.36 | RSI overbought (>70) — hold ret_low_5d_news | RSI overbought (>70) | low | 5 | news | 2 | 50.0 | -1.32 | -1.32 | -2.63 | 3.05 | -0.43 | -3.47 | 0.84 |
| 2081 | 22 | 53.36 | RSI overbought (>70) — hold ret_low_7d_news | RSI overbought (>70) | low | 7 | news | 2 | 50.0 | -1.32 | -1.32 | -2.63 | 3.05 | -0.43 | -3.47 | 0.84 |
| 2082 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_low_1d_news | Far 52w high + Value ≥100k | low | 1 | news | 3 | 33.3 | -1.35 | -0.3 | -4.05 | 4.13 | -0.33 | -5.9 | 2.15 |
| 2083 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_low_2d_news | Far 52w high + Value ≥100k | low | 2 | news | 3 | 33.3 | -1.35 | -0.3 | -4.06 | 4.12 | -0.33 | -5.9 | 2.14 |
| 2084 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_low_3d_open | CEO only + Value ≥100k | low | 3 | open | 2 | 0.0 | -1.35 | -1.35 | -2.7 | 1.91 | -0.71 | -2.7 | 0.0 |
| 2085 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_low_3d_open | Price > MA50 + CEO/CFO | low | 3 | open | 2 | 0.0 | -1.35 | -1.35 | -2.7 | 1.91 | -0.71 | -2.7 | 0.0 |
| 2086 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_low_5d_open | CEO only + Value ≥100k | low | 5 | open | 2 | 0.0 | -1.35 | -1.35 | -2.7 | 1.91 | -0.71 | -2.7 | 0.0 |
| 2087 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_low_5d_open | Price > MA50 + CEO/CFO | low | 5 | open | 2 | 0.0 | -1.35 | -1.35 | -2.7 | 1.91 | -0.71 | -2.7 | 0.0 |
| 2088 | 53 | 0.0 | Qty ≥100k shares — hold ret_mean_5d_news | Qty ≥100k shares | mean | 5 | news | 1 | 0.0 | -1.35 | -1.35 | -1.35 | nan | nan | -1.35 | -1.35 |
| 2089 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_mean_5d_news | Small cap (≤1B) Value ≥100k | mean | 5 | news | 1 | 0.0 | -1.35 | -1.35 | -1.35 | nan | nan | -1.35 | -1.35 |
| 2090 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_low_7d_open | CEO only + Value ≥100k | low | 7 | open | 2 | 0.0 | -1.35 | -1.35 | -2.7 | 1.91 | -0.71 | -2.7 | 0.0 |
| 2091 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_low_7d_open | Price > MA50 + CEO/CFO | low | 7 | open | 2 | 0.0 | -1.35 | -1.35 | -2.7 | 1.91 | -0.71 | -2.7 | 0.0 |
| 2092 | 37 | 35.58 | Director only + Value ≥100k — hold ret_mean_7d_open | Director only + Value ≥100k | mean | 7 | open | 3 | 33.3 | -1.35 | -1.58 | -4.05 | 5.12 | -0.26 | -6.35 | 3.88 |
| 2093 | 36 | 36.54 | Director only (no C-level) — hold ret_mean_10d_news | Director only (no C-level) | mean | 10 | news | 6 | 50.0 | -1.35 | -0.01 | -8.07 | 5.64 | -0.24 | -12.21 | 4.52 |
| 2094 | 28 | 48.48 | Tutti — hold ret_low_1d_news | Tutti | low | 1 | news | 10 | 30.0 | -1.36 | -1.86 | -13.57 | 2.44 | -0.56 | -5.9 | 2.15 |
| 2095 | 28 | 48.48 | Tutti — hold ret_low_2d_news | Tutti | low | 2 | news | 10 | 30.0 | -1.36 | -1.86 | -13.58 | 2.44 | -0.56 | -5.9 | 2.14 |
| 2096 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_mean_60d_open | Large cap (≥2B) CEO/CFO | mean | 60 | open | 2 | 50.0 | -1.38 | -1.38 | -2.76 | 7.18 | -0.19 | -6.46 | 3.7 |
| 2097 | 32 | 44.63 | Position +10% — hold ret_low_1d_news | Position +10% | low | 1 | news | 6 | 33.3 | -1.39 | -1.12 | -8.36 | 2.68 | -0.52 | -5.9 | 1.43 |
| 2098 | 32 | 44.63 | Position +10% — hold ret_low_2d_news | Position +10% | low | 2 | news | 6 | 33.3 | -1.39 | -1.12 | -8.36 | 2.68 | -0.52 | -5.9 | 1.43 |
| 2099 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_mean_30d_news | Large cap (≥3B) CEO/CFO | mean | 30 | news | 1 | 0.0 | -1.39 | -1.39 | -1.39 | nan | nan | -1.39 | -1.39 |
| 2100 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_mean_30d_news | Large cap (≥5B) CEO/CFO | mean | 30 | news | 1 | 0.0 | -1.39 | -1.39 | -1.39 | nan | nan | -1.39 | -1.39 |
| 2101 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_mean_30d_news | Large cap (≥10B) CEO/CFO | mean | 30 | news | 1 | 0.0 | -1.39 | -1.39 | -1.39 | nan | nan | -1.39 | -1.39 |
| 2102 | 51 | 20.1 | Position +30% — hold ret_mean_7d_open | Position +30% | mean | 7 | open | 3 | 66.7 | -1.4 | 0.07 | -4.19 | 4.41 | -0.32 | -6.35 | 2.09 |
| 2103 | 32 | 44.63 | Position +10% — hold ret_low_1d_open | Position +10% | low | 1 | open | 6 | 0.0 | -1.42 | -1.48 | -8.52 | 1.31 | -1.08 | -3.28 | 0.0 |
| 2104 | 32 | 44.63 | Position +10% — hold ret_low_2d_open | Position +10% | low | 2 | open | 6 | 0.0 | -1.42 | -1.48 | -8.52 | 1.31 | -1.08 | -3.28 | 0.0 |
| 2105 | 15 | 62.43 | Price > MA50 — hold ret_low_5d_news | Price > MA50 | low | 5 | news | 5 | 40.0 | -1.48 | -0.11 | -7.41 | 3.2 | -0.46 | -6.1 | 1.43 |
| 2106 | 30 | 48.32 | Value ≥100k — hold ret_low_1d_open | Value ≥100k | low | 1 | open | 6 | 0.0 | -1.5 | -0.77 | -9.03 | 1.8 | -0.83 | -4.22 | 0.0 |
| 2107 | 14 | 65.45 | Price > MA200 — hold ret_low_1d_open | Price > MA200 | low | 1 | open | 4 | 0.0 | -1.5 | -0.9 | -6.01 | 2.0 | -0.75 | -4.22 | 0.0 |
| 2108 | 30 | 48.32 | Value ≥100k — hold ret_low_2d_open | Value ≥100k | low | 2 | open | 6 | 0.0 | -1.5 | -0.77 | -9.03 | 1.8 | -0.83 | -4.22 | 0.0 |
| 2109 | 14 | 65.45 | Price > MA200 — hold ret_low_2d_open | Price > MA200 | low | 2 | open | 4 | 0.0 | -1.5 | -0.9 | -6.01 | 2.0 | -0.75 | -4.22 | 0.0 |
| 2110 | 36 | 36.54 | Director only (no C-level) — hold ret_low_1d_news | Director only (no C-level) | low | 1 | news | 6 | 16.7 | -1.53 | -1.86 | -9.15 | 1.55 | -0.98 | -3.47 | 0.84 |
| 2111 | 36 | 36.54 | Director only (no C-level) — hold ret_low_2d_news | Director only (no C-level) | low | 2 | news | 6 | 16.7 | -1.53 | -1.86 | -9.15 | 1.55 | -0.98 | -3.47 | 0.84 |
| 2112 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_low_3d_news | CEO/CFO + Value ≥100k | low | 3 | news | 3 | 33.3 | -1.53 | -0.11 | -4.58 | 3.86 | -0.4 | -5.9 | 1.43 |
| 2113 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_low_3d_news | Large cap (≥750M) CEO/CFO | low | 3 | news | 3 | 33.3 | -1.53 | -0.11 | -4.58 | 3.86 | -0.4 | -5.9 | 1.43 |
| 2114 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_low_3d_news | Large cap (≥1B) CEO/CFO | low | 3 | news | 3 | 33.3 | -1.53 | -0.11 | -4.58 | 3.86 | -0.4 | -5.9 | 1.43 |
| 2115 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_low_5d_news | CEO/CFO + Value ≥100k | low | 5 | news | 3 | 33.3 | -1.53 | -0.11 | -4.58 | 3.86 | -0.4 | -5.9 | 1.43 |
| 2116 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_low_5d_news | Large cap (≥750M) CEO/CFO | low | 5 | news | 3 | 33.3 | -1.53 | -0.11 | -4.58 | 3.86 | -0.4 | -5.9 | 1.43 |
| 2117 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_low_5d_news | Large cap (≥1B) CEO/CFO | low | 5 | news | 3 | 33.3 | -1.53 | -0.11 | -4.58 | 3.86 | -0.4 | -5.9 | 1.43 |
| 2118 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_low_7d_news | CEO/CFO + Value ≥100k | low | 7 | news | 3 | 33.3 | -1.53 | -0.11 | -4.58 | 3.86 | -0.4 | -5.9 | 1.43 |
| 2119 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_low_7d_news | Large cap (≥750M) CEO/CFO | low | 7 | news | 3 | 33.3 | -1.53 | -0.11 | -4.58 | 3.86 | -0.4 | -5.9 | 1.43 |
| 2120 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_low_7d_news | Large cap (≥1B) CEO/CFO | low | 7 | news | 3 | 33.3 | -1.53 | -0.11 | -4.58 | 3.86 | -0.4 | -5.9 | 1.43 |
| 2121 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_mean_60d_news | Large cap (≥2B) CEO/CFO | mean | 60 | news | 2 | 50.0 | -1.54 | -1.54 | -3.08 | 3.44 | -0.45 | -3.97 | 0.89 |
| 2122 | 21 | 53.67 | Qty ≥5k shares — hold ret_low_1d_news | Qty ≥5k shares | low | 1 | news | 6 | 33.3 | -1.58 | -1.2 | -9.5 | 2.79 | -0.57 | -5.9 | 1.43 |
| 2123 | 20 | 53.67 | Qty ≥10k shares — hold ret_low_1d_news | Qty ≥10k shares | low | 1 | news | 6 | 33.3 | -1.58 | -1.2 | -9.5 | 2.79 | -0.57 | -5.9 | 1.43 |
| 2124 | 21 | 53.67 | Qty ≥5k shares — hold ret_low_2d_news | Qty ≥5k shares | low | 2 | news | 6 | 33.3 | -1.58 | -1.2 | -9.5 | 2.79 | -0.57 | -5.9 | 1.43 |
| 2125 | 20 | 53.67 | Qty ≥10k shares — hold ret_low_2d_news | Qty ≥10k shares | low | 2 | news | 6 | 33.3 | -1.58 | -1.2 | -9.5 | 2.79 | -0.57 | -5.9 | 1.43 |
| 2126 | 14 | 65.45 | Price > MA200 — hold ret_low_3d_open | Price > MA200 | low | 3 | open | 4 | 0.0 | -1.58 | -1.06 | -6.34 | 2.02 | -0.78 | -4.22 | 0.0 |
| 2127 | 15 | 62.43 | Price > MA50 — hold ret_low_7d_news | Price > MA50 | low | 7 | news | 5 | 40.0 | -1.58 | -0.11 | -7.88 | 3.37 | -0.47 | -6.57 | 1.43 |
| 2128 | 39 | 34.48 | Position +20% — hold ret_mean_10d_open | Position +20% | mean | 10 | open | 4 | 75.0 | -1.59 | 1.41 | -6.38 | 7.62 | -0.21 | -12.85 | 3.65 |
| 2129 | 31 | 47.75 | Value ≥50k — hold ret_low_1d_open | Value ≥50k | low | 1 | open | 9 | 0.0 | -1.6 | -1.15 | -14.39 | 1.46 | -1.09 | -4.22 | 0.0 |
| 2130 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_low_1d_open | Far 52w high + Value ≥100k | low | 1 | open | 3 | 0.0 | -1.6 | -1.03 | -4.81 | 1.48 | -1.09 | -3.28 | -0.5 |
| 2131 | 31 | 47.75 | Value ≥50k — hold ret_low_2d_open | Value ≥50k | low | 2 | open | 9 | 0.0 | -1.6 | -1.15 | -14.39 | 1.46 | -1.09 | -4.22 | 0.0 |
| 2132 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_low_2d_open | Far 52w high + Value ≥100k | low | 2 | open | 3 | 0.0 | -1.6 | -1.03 | -4.81 | 1.48 | -1.09 | -3.28 | -0.5 |
| 2133 | 21 | 53.67 | Qty ≥5k shares — hold ret_low_1d_open | Qty ≥5k shares | low | 1 | open | 6 | 0.0 | -1.61 | -1.09 | -9.68 | 1.75 | -0.92 | -4.22 | 0.0 |
| 2134 | 20 | 53.67 | Qty ≥10k shares — hold ret_low_1d_open | Qty ≥10k shares | low | 1 | open | 6 | 0.0 | -1.61 | -1.09 | -9.68 | 1.75 | -0.92 | -4.22 | 0.0 |
| 2135 | 21 | 53.67 | Qty ≥5k shares — hold ret_low_2d_open | Qty ≥5k shares | low | 2 | open | 6 | 0.0 | -1.61 | -1.09 | -9.68 | 1.75 | -0.92 | -4.22 | 0.0 |
| 2136 | 20 | 53.67 | Qty ≥10k shares — hold ret_low_2d_open | Qty ≥10k shares | low | 2 | open | 6 | 0.0 | -1.61 | -1.09 | -9.68 | 1.75 | -0.92 | -4.22 | 0.0 |
| 2137 | 28 | 48.48 | Tutti — hold ret_low_1d_open | Tutti | low | 1 | open | 10 | 0.0 | -1.62 | -1.47 | -16.18 | 1.38 | -1.17 | -4.22 | 0.0 |
| 2138 | 28 | 48.48 | Tutti — hold ret_low_2d_open | Tutti | low | 2 | open | 10 | 0.0 | -1.62 | -1.47 | -16.18 | 1.38 | -1.17 | -4.22 | 0.0 |
| 2139 | 39 | 34.48 | Position +20% — hold ret_low_1d_open | Position +20% | low | 1 | open | 4 | 0.0 | -1.64 | -1.65 | -6.58 | 1.43 | -1.15 | -3.28 | 0.0 |
| 2140 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_low_1d_open | Mid cap (1B–10B) CEO/CFO | low | 1 | open | 2 | 0.0 | -1.64 | -1.64 | -3.28 | 2.32 | -0.71 | -3.28 | 0.0 |
| 2141 | 39 | 34.48 | Position +20% — hold ret_low_2d_open | Position +20% | low | 2 | open | 4 | 0.0 | -1.64 | -1.65 | -6.58 | 1.43 | -1.15 | -3.28 | 0.0 |
| 2142 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_low_2d_open | Mid cap (1B–10B) CEO/CFO | low | 2 | open | 2 | 0.0 | -1.64 | -1.64 | -3.28 | 2.32 | -0.71 | -3.28 | 0.0 |
| 2143 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_low_3d_open | Mid cap (1B–10B) CEO/CFO | low | 3 | open | 2 | 0.0 | -1.64 | -1.64 | -3.28 | 2.32 | -0.71 | -3.28 | 0.0 |
| 2144 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_low_5d_open | Mid cap (1B–10B) CEO/CFO | low | 5 | open | 2 | 0.0 | -1.64 | -1.64 | -3.28 | 2.32 | -0.71 | -3.28 | 0.0 |
| 2145 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_low_7d_open | Mid cap (1B–10B) CEO/CFO | low | 7 | open | 2 | 0.0 | -1.64 | -1.64 | -3.28 | 2.32 | -0.71 | -3.28 | 0.0 |
| 2146 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_low_10d_open | Mid cap (1B–10B) CEO/CFO | low | 10 | open | 2 | 0.0 | -1.64 | -1.64 | -3.28 | 2.32 | -0.71 | -3.28 | 0.0 |
| 2147 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_low_14d_open | Mid cap (1B–10B) CEO/CFO | low | 14 | open | 2 | 0.0 | -1.64 | -1.64 | -3.28 | 2.32 | -0.71 | -3.28 | 0.0 |
| 2148 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_low_30d_open | Mid cap (1B–10B) CEO/CFO | low | 30 | open | 2 | 0.0 | -1.64 | -1.64 | -3.28 | 2.32 | -0.71 | -3.28 | 0.0 |
| 2149 | 10 | 66.41 | CEO/CFO — hold ret_low_3d_news | CEO/CFO | low | 3 | news | 4 | 25.0 | -1.67 | -1.1 | -6.68 | 3.17 | -0.53 | -5.9 | 1.43 |
| 2150 | 11 | 66.41 | Officer/President — hold ret_low_3d_news | Officer/President | low | 3 | news | 4 | 25.0 | -1.67 | -1.1 | -6.68 | 3.17 | -0.53 | -5.9 | 1.43 |
| 2151 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_low_3d_news | Large cap (≥250M) CEO/CFO | low | 3 | news | 4 | 25.0 | -1.67 | -1.1 | -6.68 | 3.17 | -0.53 | -5.9 | 1.43 |
| 2152 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_low_3d_news | Large cap (≥500M) CEO/CFO | low | 3 | news | 4 | 25.0 | -1.67 | -1.1 | -6.68 | 3.17 | -0.53 | -5.9 | 1.43 |
| 2153 | 10 | 66.41 | CEO/CFO — hold ret_low_5d_news | CEO/CFO | low | 5 | news | 4 | 25.0 | -1.67 | -1.1 | -6.68 | 3.17 | -0.53 | -5.9 | 1.43 |
| 2154 | 11 | 66.41 | Officer/President — hold ret_low_5d_news | Officer/President | low | 5 | news | 4 | 25.0 | -1.67 | -1.1 | -6.68 | 3.17 | -0.53 | -5.9 | 1.43 |
| 2155 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_low_5d_news | Large cap (≥250M) CEO/CFO | low | 5 | news | 4 | 25.0 | -1.67 | -1.1 | -6.68 | 3.17 | -0.53 | -5.9 | 1.43 |
| 2156 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_low_5d_news | Large cap (≥500M) CEO/CFO | low | 5 | news | 4 | 25.0 | -1.67 | -1.1 | -6.68 | 3.17 | -0.53 | -5.9 | 1.43 |
| 2157 | 10 | 66.41 | CEO/CFO — hold ret_low_7d_news | CEO/CFO | low | 7 | news | 4 | 25.0 | -1.67 | -1.1 | -6.68 | 3.17 | -0.53 | -5.9 | 1.43 |
| 2158 | 11 | 66.41 | Officer/President — hold ret_low_7d_news | Officer/President | low | 7 | news | 4 | 25.0 | -1.67 | -1.1 | -6.68 | 3.17 | -0.53 | -5.9 | 1.43 |
| 2159 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_low_7d_news | Large cap (≥250M) CEO/CFO | low | 7 | news | 4 | 25.0 | -1.67 | -1.1 | -6.68 | 3.17 | -0.53 | -5.9 | 1.43 |
| 2160 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_low_7d_news | Large cap (≥500M) CEO/CFO | low | 7 | news | 4 | 25.0 | -1.67 | -1.1 | -6.68 | 3.17 | -0.53 | -5.9 | 1.43 |
| 2161 | 36 | 36.54 | Director only (no C-level) — hold ret_mean_10d_open | Director only (no C-level) | mean | 10 | open | 6 | 50.0 | -1.69 | -0.19 | -10.14 | 5.71 | -0.3 | -12.85 | 3.65 |
| 2162 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_mean_90d_news | Mid cap (1B–10B) CEO/CFO | mean | 90 | news | 2 | 0.0 | -1.7 | -1.7 | -3.4 | 0.61 | -2.8 | -2.13 | -1.27 |
| 2163 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_mean_60d_open | CEO only + Value ≥100k | mean | 60 | open | 2 | 50.0 | -1.74 | -1.73 | -3.47 | 6.68 | -0.26 | -6.46 | 2.99 |
| 2164 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_mean_60d_open | Price > MA50 + CEO/CFO | mean | 60 | open | 2 | 50.0 | -1.74 | -1.73 | -3.47 | 6.68 | -0.26 | -6.46 | 2.99 |
| 2165 | 37 | 35.58 | Director only + Value ≥100k — hold ret_low_1d_open | Director only + Value ≥100k | low | 1 | open | 3 | 0.0 | -1.75 | -1.03 | -5.25 | 2.2 | -0.8 | -4.22 | 0.0 |
| 2166 | 37 | 35.58 | Director only + Value ≥100k — hold ret_low_2d_open | Director only + Value ≥100k | low | 2 | open | 3 | 0.0 | -1.75 | -1.03 | -5.25 | 2.2 | -0.8 | -4.22 | 0.0 |
| 2167 | 38 | 34.53 | Price < MA50 — hold ret_mean_60d_open | Price < MA50 | mean | 60 | open | 5 | 60.0 | -1.75 | 0.43 | -8.74 | 16.79 | -0.1 | -28.92 | 17.06 |
| 2168 | 22 | 53.36 | RSI overbought (>70) — hold ret_low_10d_news | RSI overbought (>70) | low | 10 | news | 2 | 0.0 | -1.76 | -1.76 | -3.51 | 2.43 | -0.72 | -3.47 | -0.04 |
| 2169 | 22 | 53.36 | RSI overbought (>70) — hold ret_low_14d_news | RSI overbought (>70) | low | 14 | news | 2 | 0.0 | -1.76 | -1.76 | -3.51 | 2.43 | -0.72 | -3.47 | -0.04 |
| 2170 | 22 | 53.36 | RSI overbought (>70) — hold ret_low_30d_news | RSI overbought (>70) | low | 30 | news | 2 | 0.0 | -1.76 | -1.76 | -3.51 | 2.43 | -0.72 | -3.47 | -0.04 |
| 2171 | 26 | 50.0 | Qty ≥50k shares — hold ret_mean_14d_news | Qty ≥50k shares | mean | 14 | news | 2 | 50.0 | -1.77 | -1.77 | -3.54 | 23.0 | -0.08 | -18.03 | 14.49 |
| 2172 | 27 | 50.0 | Value ≥1M — hold ret_mean_14d_news | Value ≥1M | mean | 14 | news | 2 | 50.0 | -1.77 | -1.77 | -3.54 | 23.0 | -0.08 | -18.03 | 14.49 |
| 2173 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_low_1d_news | Mid cap (1B–10B) Value ≥100k | low | 1 | news | 4 | 50.0 | -1.78 | -1.32 | -7.1 | 3.51 | -0.51 | -5.9 | 1.43 |
| 2174 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_low_2d_news | Mid cap (1B–10B) Value ≥100k | low | 2 | news | 4 | 50.0 | -1.78 | -1.32 | -7.1 | 3.51 | -0.51 | -5.9 | 1.43 |
| 2175 | 10 | 66.41 | CEO/CFO — hold ret_low_3d_open | CEO/CFO | low | 3 | open | 4 | 0.0 | -1.78 | -1.93 | -7.13 | 1.49 | -1.2 | -3.28 | 0.0 |
| 2176 | 11 | 66.41 | Officer/President — hold ret_low_3d_open | Officer/President | low | 3 | open | 4 | 0.0 | -1.78 | -1.93 | -7.13 | 1.49 | -1.2 | -3.28 | 0.0 |
| 2177 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_low_3d_open | Large cap (≥250M) CEO/CFO | low | 3 | open | 4 | 0.0 | -1.78 | -1.93 | -7.13 | 1.49 | -1.2 | -3.28 | 0.0 |
| 2178 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_low_3d_open | Large cap (≥500M) CEO/CFO | low | 3 | open | 4 | 0.0 | -1.78 | -1.93 | -7.13 | 1.49 | -1.2 | -3.28 | 0.0 |
| 2179 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_low_3d_news | Mid cap (1B–10B) Value ≥100k | low | 3 | news | 4 | 50.0 | -1.78 | -1.32 | -7.1 | 3.51 | -0.51 | -5.9 | 1.43 |
| 2180 | 10 | 66.41 | CEO/CFO — hold ret_low_5d_open | CEO/CFO | low | 5 | open | 4 | 0.0 | -1.78 | -1.93 | -7.13 | 1.49 | -1.2 | -3.28 | 0.0 |
| 2181 | 11 | 66.41 | Officer/President — hold ret_low_5d_open | Officer/President | low | 5 | open | 4 | 0.0 | -1.78 | -1.93 | -7.13 | 1.49 | -1.2 | -3.28 | 0.0 |
| 2182 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_low_5d_open | Large cap (≥250M) CEO/CFO | low | 5 | open | 4 | 0.0 | -1.78 | -1.93 | -7.13 | 1.49 | -1.2 | -3.28 | 0.0 |
| 2183 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_low_5d_open | Large cap (≥500M) CEO/CFO | low | 5 | open | 4 | 0.0 | -1.78 | -1.93 | -7.13 | 1.49 | -1.2 | -3.28 | 0.0 |
| 2184 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_low_5d_news | Mid cap (1B–10B) Value ≥100k | low | 5 | news | 4 | 50.0 | -1.78 | -1.32 | -7.1 | 3.51 | -0.51 | -5.9 | 1.43 |
| 2185 | 10 | 66.41 | CEO/CFO — hold ret_low_7d_open | CEO/CFO | low | 7 | open | 4 | 0.0 | -1.78 | -1.93 | -7.13 | 1.49 | -1.2 | -3.28 | 0.0 |
| 2186 | 11 | 66.41 | Officer/President — hold ret_low_7d_open | Officer/President | low | 7 | open | 4 | 0.0 | -1.78 | -1.93 | -7.13 | 1.49 | -1.2 | -3.28 | 0.0 |
| 2187 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_low_7d_open | Large cap (≥250M) CEO/CFO | low | 7 | open | 4 | 0.0 | -1.78 | -1.93 | -7.13 | 1.49 | -1.2 | -3.28 | 0.0 |
| 2188 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_low_7d_open | Large cap (≥500M) CEO/CFO | low | 7 | open | 4 | 0.0 | -1.78 | -1.93 | -7.13 | 1.49 | -1.2 | -3.28 | 0.0 |
| 2189 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_low_7d_news | Mid cap (1B–10B) Value ≥100k | low | 7 | news | 4 | 50.0 | -1.78 | -1.32 | -7.1 | 3.51 | -0.51 | -5.9 | 1.43 |
| 2190 | 15 | 62.43 | Price > MA50 — hold ret_low_3d_open | Price > MA50 | low | 3 | open | 5 | 0.0 | -1.81 | -2.12 | -9.04 | 1.82 | -0.99 | -4.22 | 0.0 |
| 2191 | 14 | 65.45 | Price > MA200 — hold ret_low_5d_news | Price > MA200 | low | 5 | news | 4 | 50.0 | -1.82 | -1.32 | -7.3 | 3.59 | -0.51 | -6.1 | 1.43 |
| 2192 | 40 | 33.74 | Director only + Position +10% — hold ret_mean_10d_news | Director only + Position +10% | mean | 10 | news | 4 | 75.0 | -1.83 | 0.18 | -7.32 | 7.22 | -0.25 | -12.21 | 4.52 |
| 2193 | 36 | 36.54 | Director only (no C-level) — hold ret_low_1d_open | Director only (no C-level) | low | 1 | open | 6 | 0.0 | -1.87 | -1.86 | -11.25 | 1.41 | -1.33 | -4.22 | 0.0 |
| 2194 | 36 | 36.54 | Director only (no C-level) — hold ret_low_2d_open | Director only (no C-level) | low | 2 | open | 6 | 0.0 | -1.87 | -1.86 | -11.25 | 1.41 | -1.33 | -4.22 | 0.0 |
| 2195 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_low_1d_news | Large cap (≥2B) CEO/CFO | low | 1 | news | 2 | 50.0 | -1.88 | -1.88 | -3.75 | 5.69 | -0.33 | -5.9 | 2.15 |
| 2196 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_low_1d_open | Mid cap (1B–10B) Value ≥100k | low | 1 | open | 4 | 0.0 | -1.88 | -1.64 | -7.5 | 2.2 | -0.85 | -4.22 | 0.0 |
| 2197 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_low_2d_news | Large cap (≥2B) CEO/CFO | low | 2 | news | 2 | 50.0 | -1.88 | -1.88 | -3.76 | 5.69 | -0.33 | -5.9 | 2.14 |
| 2198 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_low_2d_open | Mid cap (1B–10B) Value ≥100k | low | 2 | open | 4 | 0.0 | -1.88 | -1.64 | -7.5 | 2.2 | -0.85 | -4.22 | 0.0 |
| 2199 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_low_3d_open | Mid cap (1B–10B) Value ≥100k | low | 3 | open | 4 | 0.0 | -1.88 | -1.64 | -7.5 | 2.2 | -0.85 | -4.22 | 0.0 |
| 2200 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_low_5d_open | Mid cap (1B–10B) Value ≥100k | low | 5 | open | 4 | 0.0 | -1.88 | -1.64 | -7.5 | 2.2 | -0.85 | -4.22 | 0.0 |
| 2201 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_low_7d_open | Mid cap (1B–10B) Value ≥100k | low | 7 | open | 4 | 0.0 | -1.88 | -1.64 | -7.5 | 2.2 | -0.85 | -4.22 | 0.0 |
| 2202 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_low_1d_open | Large cap (≥2B) CEO/CFO | low | 1 | open | 2 | 0.0 | -1.89 | -1.89 | -3.78 | 1.97 | -0.96 | -3.28 | -0.5 |
| 2203 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_low_2d_open | Large cap (≥2B) CEO/CFO | low | 2 | open | 2 | 0.0 | -1.89 | -1.89 | -3.78 | 1.97 | -0.96 | -3.28 | -0.5 |
| 2204 | 36 | 36.54 | Director only (no C-level) — hold ret_mean_30d_news | Director only (no C-level) | mean | 30 | news | 6 | 50.0 | -1.92 | 0.52 | -11.51 | 8.87 | -0.22 | -19.4 | 4.06 |
| 2205 | 38 | 34.53 | Price < MA50 — hold ret_low_1d_open | Price < MA50 | low | 1 | open | 5 | 0.0 | -1.93 | -1.94 | -9.67 | 0.92 | -2.11 | -3.28 | -1.03 |
| 2206 | 38 | 34.53 | Price < MA50 — hold ret_low_2d_open | Price < MA50 | low | 2 | open | 5 | 0.0 | -1.93 | -1.94 | -9.67 | 0.92 | -2.11 | -3.28 | -1.03 |
| 2207 | 14 | 65.45 | Price > MA200 — hold ret_low_7d_news | Price > MA200 | low | 7 | news | 4 | 50.0 | -1.94 | -1.32 | -7.77 | 3.78 | -0.51 | -6.57 | 1.43 |
| 2208 | 38 | 34.53 | Price < MA50 — hold ret_mean_90d_news | Price < MA50 | mean | 90 | news | 5 | 40.0 | -1.95 | -1.36 | -9.76 | 16.29 | -0.12 | -26.12 | 19.78 |
| 2209 | 33 | 41.81 | Director — hold ret_low_1d_open | Director | low | 1 | open | 8 | 0.0 | -1.96 | -1.86 | -15.68 | 1.33 | -1.48 | -4.22 | 0.0 |
| 2210 | 39 | 34.48 | Position +20% — hold ret_low_1d_news | Position +20% | low | 1 | news | 4 | 25.0 | -1.96 | -1.4 | -7.85 | 2.97 | -0.66 | -5.9 | 0.84 |
| 2211 | 33 | 41.81 | Director — hold ret_low_2d_open | Director | low | 2 | open | 8 | 0.0 | -1.96 | -1.86 | -15.68 | 1.33 | -1.48 | -4.22 | 0.0 |
| 2212 | 39 | 34.48 | Position +20% — hold ret_low_2d_news | Position +20% | low | 2 | news | 4 | 25.0 | -1.96 | -1.4 | -7.85 | 2.97 | -0.66 | -5.9 | 0.84 |
| 2213 | 49 | 32.78 | CFO only — hold ret_mean_5d_news | CFO only | mean | 5 | news | 1 | 0.0 | -1.96 | -1.96 | -1.96 | nan | nan | -1.96 | -1.96 |
| 2214 | 48 | 32.78 | CFO + Director (combo) — hold ret_mean_5d_news | CFO + Director (combo) | mean | 5 | news | 1 | 0.0 | -1.96 | -1.96 | -1.96 | nan | nan | -1.96 | -1.96 |
| 2215 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_mean_5d_news | CFO only + Value ≥50k | mean | 5 | news | 1 | 0.0 | -1.96 | -1.96 | -1.96 | nan | nan | -1.96 | -1.96 |
| 2216 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_mean_5d_news | CFO only + Value ≥100k | mean | 5 | news | 1 | 0.0 | -1.96 | -1.96 | -1.96 | nan | nan | -1.96 | -1.96 |
| 2217 | 47 | 32.78 | CFO only + Position +10% — hold ret_mean_5d_news | CFO only + Position +10% | mean | 5 | news | 1 | 0.0 | -1.96 | -1.96 | -1.96 | nan | nan | -1.96 | -1.96 |
| 2218 | 46 | 32.78 | CFO only + Position +20% — hold ret_mean_5d_news | CFO only + Position +20% | mean | 5 | news | 1 | 0.0 | -1.96 | -1.96 | -1.96 | nan | nan | -1.96 | -1.96 |
| 2219 | 44 | 32.78 | RSI oversold (<30) — hold ret_mean_5d_news | RSI oversold (<30) | mean | 5 | news | 1 | 0.0 | -1.96 | -1.96 | -1.96 | nan | nan | -1.96 | -1.96 |
| 2220 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_mean_5d_news | RSI oversold + CEO/CFO | mean | 5 | news | 1 | 0.0 | -1.96 | -1.96 | -1.96 | nan | nan | -1.96 | -1.96 |
| 2221 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_mean_5d_news | RSI oversold + Value ≥100k | mean | 5 | news | 1 | 0.0 | -1.96 | -1.96 | -1.96 | nan | nan | -1.96 | -1.96 |
| 2222 | 39 | 34.48 | Position +20% — hold ret_mean_10d_news | Position +20% | mean | 10 | news | 4 | 50.0 | -1.97 | -0.09 | -7.87 | 7.17 | -0.27 | -12.21 | 4.52 |
| 2223 | 38 | 34.53 | Price < MA50 — hold ret_mean_30d_news | Price < MA50 | mean | 30 | news | 5 | 40.0 | -1.97 | -1.09 | -9.85 | 10.64 | -0.19 | -19.4 | 9.36 |
| 2224 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_low_3d_open | CEO/CFO + Value ≥100k | low | 3 | open | 3 | 0.0 | -1.99 | -2.7 | -5.98 | 1.75 | -1.14 | -3.28 | 0.0 |
| 2225 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_low_3d_open | Large cap (≥750M) CEO/CFO | low | 3 | open | 3 | 0.0 | -1.99 | -2.7 | -5.98 | 1.75 | -1.14 | -3.28 | 0.0 |
| 2226 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_low_3d_open | Large cap (≥1B) CEO/CFO | low | 3 | open | 3 | 0.0 | -1.99 | -2.7 | -5.98 | 1.75 | -1.14 | -3.28 | 0.0 |
| 2227 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_low_5d_open | CEO/CFO + Value ≥100k | low | 5 | open | 3 | 0.0 | -1.99 | -2.7 | -5.98 | 1.75 | -1.14 | -3.28 | 0.0 |
| 2228 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_low_5d_open | Large cap (≥750M) CEO/CFO | low | 5 | open | 3 | 0.0 | -1.99 | -2.7 | -5.98 | 1.75 | -1.14 | -3.28 | 0.0 |
| 2229 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_low_5d_open | Large cap (≥1B) CEO/CFO | low | 5 | open | 3 | 0.0 | -1.99 | -2.7 | -5.98 | 1.75 | -1.14 | -3.28 | 0.0 |
| 2230 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_low_7d_open | CEO/CFO + Value ≥100k | low | 7 | open | 3 | 0.0 | -1.99 | -2.7 | -5.98 | 1.75 | -1.14 | -3.28 | 0.0 |
| 2231 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_low_7d_open | Large cap (≥750M) CEO/CFO | low | 7 | open | 3 | 0.0 | -1.99 | -2.7 | -5.98 | 1.75 | -1.14 | -3.28 | 0.0 |
| 2232 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_low_7d_open | Large cap (≥1B) CEO/CFO | low | 7 | open | 3 | 0.0 | -1.99 | -2.7 | -5.98 | 1.75 | -1.14 | -3.28 | 0.0 |
| 2233 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_low_10d_news | Mid cap (1B–10B) Value ≥100k | low | 10 | news | 4 | 25.0 | -2.0 | -1.76 | -7.98 | 3.32 | -0.6 | -5.9 | 1.43 |
| 2234 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_low_14d_news | Mid cap (1B–10B) Value ≥100k | low | 14 | news | 4 | 25.0 | -2.0 | -1.76 | -7.98 | 3.32 | -0.6 | -5.9 | 1.43 |
| 2235 | 38 | 34.53 | Price < MA50 — hold ret_mean_14d_news | Price < MA50 | mean | 14 | news | 5 | 40.0 | -2.0 | -0.23 | -9.99 | 9.51 | -0.21 | -18.03 | 7.39 |
| 2236 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_low_30d_news | Mid cap (1B–10B) Value ≥100k | low | 30 | news | 4 | 25.0 | -2.0 | -1.76 | -7.98 | 3.32 | -0.6 | -5.9 | 1.43 |
| 2237 | 35 | 40.48 | Value ≥500k — hold ret_low_1d_news | Value ≥500k | low | 1 | news | 4 | 25.0 | -2.06 | -1.89 | -8.24 | 3.27 | -0.63 | -5.9 | 1.43 |
| 2238 | 35 | 40.48 | Value ≥500k — hold ret_low_2d_news | Value ≥500k | low | 2 | news | 4 | 25.0 | -2.06 | -1.89 | -8.24 | 3.27 | -0.63 | -5.9 | 1.43 |
| 2239 | 36 | 36.54 | Director only (no C-level) — hold ret_mean_14d_news | Director only (no C-level) | mean | 14 | news | 6 | 50.0 | -2.06 | 0.2 | -12.38 | 7.99 | -0.26 | -18.03 | 4.01 |
| 2240 | 53 | 0.0 | Qty ≥100k shares — hold ret_mean_5d_open | Qty ≥100k shares | mean | 5 | open | 1 | 0.0 | -2.07 | -2.07 | -2.07 | nan | nan | -2.07 | -2.07 |
| 2241 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_mean_5d_open | Small cap (≤1B) Value ≥100k | mean | 5 | open | 1 | 0.0 | -2.07 | -2.07 | -2.07 | nan | nan | -2.07 | -2.07 |
| 2242 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_low_10d_open | Mid cap (1B–10B) Value ≥100k | low | 10 | open | 4 | 0.0 | -2.09 | -2.07 | -8.37 | 1.98 | -1.05 | -4.22 | 0.0 |
| 2243 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_low_14d_open | Mid cap (1B–10B) Value ≥100k | low | 14 | open | 4 | 0.0 | -2.09 | -2.07 | -8.37 | 1.98 | -1.05 | -4.22 | 0.0 |
| 2244 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_low_30d_open | Mid cap (1B–10B) Value ≥100k | low | 30 | open | 4 | 0.0 | -2.09 | -2.07 | -8.37 | 1.98 | -1.05 | -4.22 | 0.0 |
| 2245 | 4 | 82.51 | CEO + Director (combo) — hold ret_low_1d_news | CEO + Director (combo) | low | 1 | news | 1 | 0.0 | -2.1 | -2.1 | -2.1 | nan | nan | -2.1 | -2.1 |
| 2246 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_low_1d_news | Small cap (≤1B) CEO/CFO | low | 1 | news | 1 | 0.0 | -2.1 | -2.1 | -2.1 | nan | nan | -2.1 | -2.1 |
| 2247 | 4 | 82.51 | CEO + Director (combo) — hold ret_low_2d_news | CEO + Director (combo) | low | 2 | news | 1 | 0.0 | -2.1 | -2.1 | -2.1 | nan | nan | -2.1 | -2.1 |
| 2248 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_low_2d_news | Small cap (≤1B) CEO/CFO | low | 2 | news | 1 | 0.0 | -2.1 | -2.1 | -2.1 | nan | nan | -2.1 | -2.1 |
| 2249 | 4 | 82.51 | CEO + Director (combo) — hold ret_low_3d_news | CEO + Director (combo) | low | 3 | news | 1 | 0.0 | -2.1 | -2.1 | -2.1 | nan | nan | -2.1 | -2.1 |
| 2250 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_low_3d_news | Small cap (≤1B) CEO/CFO | low | 3 | news | 1 | 0.0 | -2.1 | -2.1 | -2.1 | nan | nan | -2.1 | -2.1 |
| 2251 | 4 | 82.51 | CEO + Director (combo) — hold ret_low_5d_news | CEO + Director (combo) | low | 5 | news | 1 | 0.0 | -2.1 | -2.1 | -2.1 | nan | nan | -2.1 | -2.1 |
| 2252 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_low_5d_news | Small cap (≤1B) CEO/CFO | low | 5 | news | 1 | 0.0 | -2.1 | -2.1 | -2.1 | nan | nan | -2.1 | -2.1 |
| 2253 | 4 | 82.51 | CEO + Director (combo) — hold ret_low_7d_news | CEO + Director (combo) | low | 7 | news | 1 | 0.0 | -2.1 | -2.1 | -2.1 | nan | nan | -2.1 | -2.1 |
| 2254 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_low_7d_news | Small cap (≤1B) CEO/CFO | low | 7 | news | 1 | 0.0 | -2.1 | -2.1 | -2.1 | nan | nan | -2.1 | -2.1 |
| 2255 | 4 | 82.51 | CEO + Director (combo) — hold ret_low_10d_news | CEO + Director (combo) | low | 10 | news | 1 | 0.0 | -2.1 | -2.1 | -2.1 | nan | nan | -2.1 | -2.1 |
| 2256 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_low_10d_news | Small cap (≤1B) CEO/CFO | low | 10 | news | 1 | 0.0 | -2.1 | -2.1 | -2.1 | nan | nan | -2.1 | -2.1 |
| 2257 | 4 | 82.51 | CEO + Director (combo) — hold ret_low_14d_news | CEO + Director (combo) | low | 14 | news | 1 | 0.0 | -2.1 | -2.1 | -2.1 | nan | nan | -2.1 | -2.1 |
| 2258 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_low_14d_news | Small cap (≤1B) CEO/CFO | low | 14 | news | 1 | 0.0 | -2.1 | -2.1 | -2.1 | nan | nan | -2.1 | -2.1 |
| 2259 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_mean_14d_open | Large cap (≥3B) CEO/CFO | mean | 14 | open | 1 | 0.0 | -2.1 | -2.1 | -2.1 | nan | nan | -2.1 | -2.1 |
| 2260 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_mean_14d_open | Large cap (≥5B) CEO/CFO | mean | 14 | open | 1 | 0.0 | -2.1 | -2.1 | -2.1 | nan | nan | -2.1 | -2.1 |
| 2261 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_mean_14d_open | Large cap (≥10B) CEO/CFO | mean | 14 | open | 1 | 0.0 | -2.1 | -2.1 | -2.1 | nan | nan | -2.1 | -2.1 |
| 2262 | 4 | 82.51 | CEO + Director (combo) — hold ret_low_30d_news | CEO + Director (combo) | low | 30 | news | 1 | 0.0 | -2.1 | -2.1 | -2.1 | nan | nan | -2.1 | -2.1 |
| 2263 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_low_30d_news | Small cap (≤1B) CEO/CFO | low | 30 | news | 1 | 0.0 | -2.1 | -2.1 | -2.1 | nan | nan | -2.1 | -2.1 |
| 2264 | 4 | 82.51 | CEO + Director (combo) — hold ret_low_60d_news | CEO + Director (combo) | low | 60 | news | 1 | 0.0 | -2.1 | -2.1 | -2.1 | nan | nan | -2.1 | -2.1 |
| 2265 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_low_60d_news | Small cap (≤1B) CEO/CFO | low | 60 | news | 1 | 0.0 | -2.1 | -2.1 | -2.1 | nan | nan | -2.1 | -2.1 |
| 2266 | 4 | 82.51 | CEO + Director (combo) — hold ret_low_90d_news | CEO + Director (combo) | low | 90 | news | 1 | 0.0 | -2.1 | -2.1 | -2.1 | nan | nan | -2.1 | -2.1 |
| 2267 | 5 | 82.51 | Small cap (≤1B) CEO/CFO — hold ret_low_90d_news | Small cap (≤1B) CEO/CFO | low | 90 | news | 1 | 0.0 | -2.1 | -2.1 | -2.1 | nan | nan | -2.1 | -2.1 |
| 2268 | 22 | 53.36 | RSI overbought (>70) — hold ret_low_1d_open | RSI overbought (>70) | low | 1 | open | 2 | 0.0 | -2.11 | -2.11 | -4.22 | 2.98 | -0.71 | -4.22 | 0.0 |
| 2269 | 22 | 53.36 | RSI overbought (>70) — hold ret_low_2d_open | RSI overbought (>70) | low | 2 | open | 2 | 0.0 | -2.11 | -2.11 | -4.22 | 2.98 | -0.71 | -4.22 | 0.0 |
| 2270 | 22 | 53.36 | RSI overbought (>70) — hold ret_low_3d_open | RSI overbought (>70) | low | 3 | open | 2 | 0.0 | -2.11 | -2.11 | -4.22 | 2.98 | -0.71 | -4.22 | 0.0 |
| 2271 | 22 | 53.36 | RSI overbought (>70) — hold ret_low_5d_open | RSI overbought (>70) | low | 5 | open | 2 | 0.0 | -2.11 | -2.11 | -4.22 | 2.98 | -0.71 | -4.22 | 0.0 |
| 2272 | 22 | 53.36 | RSI overbought (>70) — hold ret_low_7d_open | RSI overbought (>70) | low | 7 | open | 2 | 0.0 | -2.11 | -2.11 | -4.22 | 2.98 | -0.71 | -4.22 | 0.0 |
| 2273 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_low_1d_open | Multiple buys (n≥2) | low | 1 | open | 3 | 0.0 | -2.12 | -1.94 | -6.37 | 1.08 | -1.97 | -3.28 | -1.15 |
| 2274 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_low_2d_open | Multiple buys (n≥2) | low | 2 | open | 3 | 0.0 | -2.12 | -1.94 | -6.37 | 1.08 | -1.97 | -3.28 | -1.15 |
| 2275 | 35 | 40.48 | Value ≥500k — hold ret_low_1d_open | Value ≥500k | low | 1 | open | 4 | 0.0 | -2.13 | -2.15 | -8.53 | 1.95 | -1.09 | -4.22 | 0.0 |
| 2276 | 35 | 40.48 | Value ≥500k — hold ret_low_2d_open | Value ≥500k | low | 2 | open | 4 | 0.0 | -2.13 | -2.15 | -8.53 | 1.95 | -1.09 | -4.22 | 0.0 |
| 2277 | 49 | 32.78 | CFO only — hold ret_mean_90d_news | CFO only | mean | 90 | news | 1 | 0.0 | -2.13 | -2.13 | -2.13 | nan | nan | -2.13 | -2.13 |
| 2278 | 48 | 32.78 | CFO + Director (combo) — hold ret_mean_90d_news | CFO + Director (combo) | mean | 90 | news | 1 | 0.0 | -2.13 | -2.13 | -2.13 | nan | nan | -2.13 | -2.13 |
| 2279 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_mean_90d_news | CFO only + Value ≥50k | mean | 90 | news | 1 | 0.0 | -2.13 | -2.13 | -2.13 | nan | nan | -2.13 | -2.13 |
| 2280 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_mean_90d_news | CFO only + Value ≥100k | mean | 90 | news | 1 | 0.0 | -2.13 | -2.13 | -2.13 | nan | nan | -2.13 | -2.13 |
| 2281 | 47 | 32.78 | CFO only + Position +10% — hold ret_mean_90d_news | CFO only + Position +10% | mean | 90 | news | 1 | 0.0 | -2.13 | -2.13 | -2.13 | nan | nan | -2.13 | -2.13 |
| 2282 | 46 | 32.78 | CFO only + Position +20% — hold ret_mean_90d_news | CFO only + Position +20% | mean | 90 | news | 1 | 0.0 | -2.13 | -2.13 | -2.13 | nan | nan | -2.13 | -2.13 |
| 2283 | 44 | 32.78 | RSI oversold (<30) — hold ret_mean_90d_news | RSI oversold (<30) | mean | 90 | news | 1 | 0.0 | -2.13 | -2.13 | -2.13 | nan | nan | -2.13 | -2.13 |
| 2284 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_mean_90d_news | RSI oversold + CEO/CFO | mean | 90 | news | 1 | 0.0 | -2.13 | -2.13 | -2.13 | nan | nan | -2.13 | -2.13 |
| 2285 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_mean_90d_news | RSI oversold + Value ≥100k | mean | 90 | news | 1 | 0.0 | -2.13 | -2.13 | -2.13 | nan | nan | -2.13 | -2.13 |
| 2286 | 33 | 41.81 | Director — hold ret_low_1d_news | Director | low | 1 | news | 8 | 12.5 | -2.14 | -2.02 | -17.15 | 2.02 | -1.06 | -5.9 | 0.84 |
| 2287 | 33 | 41.81 | Director — hold ret_low_2d_news | Director | low | 2 | news | 8 | 12.5 | -2.14 | -2.02 | -17.15 | 2.02 | -1.06 | -5.9 | 0.84 |
| 2288 | 40 | 33.74 | Director only + Position +10% — hold ret_mean_10d_open | Director only + Position +10% | mean | 10 | open | 4 | 75.0 | -2.15 | 0.3 | -8.61 | 7.31 | -0.29 | -12.85 | 3.65 |
| 2289 | 51 | 20.1 | Position +30% — hold ret_mean_7d_news | Position +30% | mean | 7 | news | 3 | 0.0 | -2.16 | -0.68 | -6.49 | 3.04 | -0.71 | -5.66 | -0.15 |
| 2290 | 14 | 65.45 | Price > MA200 — hold ret_low_10d_news | Price > MA200 | low | 10 | news | 4 | 25.0 | -2.16 | -1.76 | -8.65 | 3.58 | -0.6 | -6.57 | 1.43 |
| 2291 | 14 | 65.45 | Price > MA200 — hold ret_low_14d_news | Price > MA200 | low | 14 | news | 4 | 25.0 | -2.16 | -1.76 | -8.65 | 3.58 | -0.6 | -6.57 | 1.43 |
| 2292 | 14 | 65.45 | Price > MA200 — hold ret_low_30d_news | Price > MA200 | low | 30 | news | 4 | 25.0 | -2.16 | -1.76 | -8.65 | 3.58 | -0.6 | -6.57 | 1.43 |
| 2293 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_mean_90d_news | CEO/CFO + Value ≥100k | mean | 90 | news | 3 | 0.0 | -2.18 | -2.13 | -6.55 | 0.94 | -2.32 | -3.15 | -1.27 |
| 2294 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_mean_90d_news | Large cap (≥750M) CEO/CFO | mean | 90 | news | 3 | 0.0 | -2.18 | -2.13 | -6.55 | 0.94 | -2.32 | -3.15 | -1.27 |
| 2295 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_mean_90d_news | Large cap (≥1B) CEO/CFO | mean | 90 | news | 3 | 0.0 | -2.18 | -2.13 | -6.55 | 0.94 | -2.32 | -3.15 | -1.27 |
| 2296 | 51 | 20.1 | Position +30% — hold ret_low_1d_open | Position +30% | low | 1 | open | 3 | 0.0 | -2.19 | -2.27 | -6.58 | 1.13 | -1.95 | -3.28 | -1.03 |
| 2297 | 51 | 20.1 | Position +30% — hold ret_low_2d_open | Position +30% | low | 2 | open | 3 | 0.0 | -2.19 | -2.27 | -6.58 | 1.13 | -1.95 | -3.28 | -1.03 |
| 2298 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_mean_90d_news | CEO only + Value ≥100k | mean | 90 | news | 2 | 0.0 | -2.21 | -2.21 | -4.42 | 1.33 | -1.66 | -3.15 | -1.27 |
| 2299 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_mean_90d_news | Price > MA50 + CEO/CFO | mean | 90 | news | 2 | 0.0 | -2.21 | -2.21 | -4.42 | 1.33 | -1.66 | -3.15 | -1.27 |
| 2300 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_low_1d_news | Mid cap (1B–10B) CEO/CFO | low | 1 | news | 2 | 50.0 | -2.24 | -2.24 | -4.47 | 5.18 | -0.43 | -5.9 | 1.43 |
| 2301 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_low_2d_news | Mid cap (1B–10B) CEO/CFO | low | 2 | news | 2 | 50.0 | -2.24 | -2.24 | -4.47 | 5.18 | -0.43 | -5.9 | 1.43 |
| 2302 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_low_3d_news | Mid cap (1B–10B) CEO/CFO | low | 3 | news | 2 | 50.0 | -2.24 | -2.24 | -4.47 | 5.18 | -0.43 | -5.9 | 1.43 |
| 2303 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_low_5d_news | Mid cap (1B–10B) CEO/CFO | low | 5 | news | 2 | 50.0 | -2.24 | -2.24 | -4.47 | 5.18 | -0.43 | -5.9 | 1.43 |
| 2304 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_low_7d_news | Mid cap (1B–10B) CEO/CFO | low | 7 | news | 2 | 50.0 | -2.24 | -2.24 | -4.47 | 5.18 | -0.43 | -5.9 | 1.43 |
| 2305 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_low_10d_news | Mid cap (1B–10B) CEO/CFO | low | 10 | news | 2 | 50.0 | -2.24 | -2.24 | -4.47 | 5.18 | -0.43 | -5.9 | 1.43 |
| 2306 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_low_14d_news | Mid cap (1B–10B) CEO/CFO | low | 14 | news | 2 | 50.0 | -2.24 | -2.24 | -4.47 | 5.18 | -0.43 | -5.9 | 1.43 |
| 2307 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_low_30d_news | Mid cap (1B–10B) CEO/CFO | low | 30 | news | 2 | 50.0 | -2.24 | -2.24 | -4.47 | 5.18 | -0.43 | -5.9 | 1.43 |
| 2308 | 36 | 36.54 | Director only (no C-level) — hold ret_mean_30d_open | Director only (no C-level) | mean | 30 | open | 6 | 50.0 | -2.26 | 0.23 | -13.55 | 8.93 | -0.25 | -19.99 | 4.06 |
| 2309 | 36 | 36.54 | Director only (no C-level) — hold ret_mean_14d_open | Director only (no C-level) | mean | 14 | open | 6 | 33.3 | -2.4 | -0.09 | -14.42 | 8.07 | -0.3 | -18.64 | 3.14 |
| 2310 | 38 | 34.53 | Price < MA50 — hold ret_mean_60d_news | Price < MA50 | mean | 60 | news | 5 | 60.0 | -2.47 | 0.21 | -12.35 | 16.06 | -0.15 | -28.39 | 15.95 |
| 2311 | 49 | 32.78 | CFO only — hold ret_high_1d_news | CFO only | high | 1 | news | 1 | 0.0 | -2.48 | -2.48 | -2.48 | nan | nan | -2.48 | -2.48 |
| 2312 | 48 | 32.78 | CFO + Director (combo) — hold ret_high_1d_news | CFO + Director (combo) | high | 1 | news | 1 | 0.0 | -2.48 | -2.48 | -2.48 | nan | nan | -2.48 | -2.48 |
| 2313 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_high_1d_news | CFO only + Value ≥50k | high | 1 | news | 1 | 0.0 | -2.48 | -2.48 | -2.48 | nan | nan | -2.48 | -2.48 |
| 2314 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_high_1d_news | CFO only + Value ≥100k | high | 1 | news | 1 | 0.0 | -2.48 | -2.48 | -2.48 | nan | nan | -2.48 | -2.48 |
| 2315 | 47 | 32.78 | CFO only + Position +10% — hold ret_high_1d_news | CFO only + Position +10% | high | 1 | news | 1 | 0.0 | -2.48 | -2.48 | -2.48 | nan | nan | -2.48 | -2.48 |
| 2316 | 46 | 32.78 | CFO only + Position +20% — hold ret_high_1d_news | CFO only + Position +20% | high | 1 | news | 1 | 0.0 | -2.48 | -2.48 | -2.48 | nan | nan | -2.48 | -2.48 |
| 2317 | 44 | 32.78 | RSI oversold (<30) — hold ret_high_1d_news | RSI oversold (<30) | high | 1 | news | 1 | 0.0 | -2.48 | -2.48 | -2.48 | nan | nan | -2.48 | -2.48 |
| 2318 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_high_1d_news | RSI oversold + CEO/CFO | high | 1 | news | 1 | 0.0 | -2.48 | -2.48 | -2.48 | nan | nan | -2.48 | -2.48 |
| 2319 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_high_1d_news | RSI oversold + Value ≥100k | high | 1 | news | 1 | 0.0 | -2.48 | -2.48 | -2.48 | nan | nan | -2.48 | -2.48 |
| 2320 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_mean_90d_open | Large cap (≥2B) CEO/CFO | mean | 90 | open | 2 | 50.0 | -2.53 | -2.53 | -5.05 | 4.42 | -0.57 | -5.65 | 0.6 |
| 2321 | 22 | 53.36 | RSI overbought (>70) — hold ret_low_10d_open | RSI overbought (>70) | low | 10 | open | 2 | 0.0 | -2.54 | -2.54 | -5.09 | 2.37 | -1.07 | -4.22 | -0.87 |
| 2322 | 22 | 53.36 | RSI overbought (>70) — hold ret_low_14d_open | RSI overbought (>70) | low | 14 | open | 2 | 0.0 | -2.54 | -2.54 | -5.09 | 2.37 | -1.07 | -4.22 | -0.87 |
| 2323 | 22 | 53.36 | RSI overbought (>70) — hold ret_low_30d_open | RSI overbought (>70) | low | 30 | open | 2 | 0.0 | -2.54 | -2.54 | -5.09 | 2.37 | -1.07 | -4.22 | -0.87 |
| 2324 | 38 | 34.53 | Price < MA50 — hold ret_low_1d_news | Price < MA50 | low | 1 | news | 5 | 0.0 | -2.55 | -2.1 | -12.73 | 2.05 | -1.24 | -5.9 | -0.3 |
| 2325 | 38 | 34.53 | Price < MA50 — hold ret_low_2d_news | Price < MA50 | low | 2 | news | 5 | 0.0 | -2.55 | -2.1 | -12.73 | 2.05 | -1.24 | -5.9 | -0.3 |
| 2326 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_mean_90d_open | CEO/CFO + Value ≥100k | mean | 90 | open | 3 | 33.3 | -2.57 | -2.66 | -7.71 | 3.13 | -0.82 | -5.65 | 0.6 |
| 2327 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_mean_90d_open | Large cap (≥750M) CEO/CFO | mean | 90 | open | 3 | 33.3 | -2.57 | -2.66 | -7.71 | 3.13 | -0.82 | -5.65 | 0.6 |
| 2328 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_mean_90d_open | Large cap (≥1B) CEO/CFO | mean | 90 | open | 3 | 33.3 | -2.57 | -2.66 | -7.71 | 3.13 | -0.82 | -5.65 | 0.6 |
| 2329 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_low_3d_open | Multiple buys (n≥2) | low | 3 | open | 3 | 0.0 | -2.58 | -3.28 | -7.73 | 1.24 | -2.09 | -3.3 | -1.15 |
| 2330 | 14 | 65.45 | Price > MA200 — hold ret_low_5d_open | Price > MA200 | low | 5 | open | 4 | 0.0 | -2.58 | -2.11 | -10.32 | 3.08 | -0.84 | -6.1 | 0.0 |
| 2331 | 15 | 62.43 | Price > MA50 — hold ret_low_5d_open | Price > MA50 | low | 5 | open | 5 | 0.0 | -2.6 | -2.7 | -13.02 | 2.66 | -0.98 | -6.1 | 0.0 |
| 2332 | 28 | 48.48 | Tutti — hold ret_low_3d_news | Tutti | low | 3 | news | 10 | 20.0 | -2.63 | -2.31 | -26.26 | 3.13 | -0.84 | -9.04 | 1.43 |
| 2333 | 37 | 35.58 | Director only + Value ≥100k — hold ret_mean_10d_news | Director only + Value ≥100k | mean | 10 | news | 3 | 33.3 | -2.63 | -0.19 | -7.88 | 8.63 | -0.3 | -12.21 | 4.52 |
| 2334 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_mean_90d_news | Large cap (≥2B) CEO/CFO | mean | 90 | news | 2 | 0.0 | -2.64 | -2.64 | -5.28 | 0.72 | -3.66 | -3.15 | -2.13 |
| 2335 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_mean_90d_open | CEO only + Value ≥500k | mean | 90 | open | 1 | 0.0 | -2.66 | -2.66 | -2.66 | nan | nan | -2.66 | -2.66 |
| 2336 | 1 | 100.0 | CEO only + Position +10% — hold ret_mean_90d_open | CEO only + Position +10% | mean | 90 | open | 1 | 0.0 | -2.66 | -2.66 | -2.66 | nan | nan | -2.66 | -2.66 |
| 2337 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_mean_90d_open | Near 52w high + CEO/CFO | mean | 90 | open | 1 | 0.0 | -2.66 | -2.66 | -2.66 | nan | nan | -2.66 | -2.66 |
| 2338 | 31 | 47.75 | Value ≥50k — hold ret_low_3d_news | Value ≥50k | low | 3 | news | 9 | 22.2 | -2.68 | -2.49 | -24.14 | 3.32 | -0.81 | -9.04 | 1.43 |
| 2339 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_low_3d_open | Large cap (≥3B) CEO/CFO | low | 3 | open | 1 | 0.0 | -2.7 | -2.7 | -2.7 | nan | nan | -2.7 | -2.7 |
| 2340 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_low_3d_open | Large cap (≥5B) CEO/CFO | low | 3 | open | 1 | 0.0 | -2.7 | -2.7 | -2.7 | nan | nan | -2.7 | -2.7 |
| 2341 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_low_3d_open | Large cap (≥10B) CEO/CFO | low | 3 | open | 1 | 0.0 | -2.7 | -2.7 | -2.7 | nan | nan | -2.7 | -2.7 |
| 2342 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_low_5d_open | Large cap (≥3B) CEO/CFO | low | 5 | open | 1 | 0.0 | -2.7 | -2.7 | -2.7 | nan | nan | -2.7 | -2.7 |
| 2343 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_low_5d_open | Large cap (≥5B) CEO/CFO | low | 5 | open | 1 | 0.0 | -2.7 | -2.7 | -2.7 | nan | nan | -2.7 | -2.7 |
| 2344 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_low_5d_open | Large cap (≥10B) CEO/CFO | low | 5 | open | 1 | 0.0 | -2.7 | -2.7 | -2.7 | nan | nan | -2.7 | -2.7 |
| 2345 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_low_7d_open | Large cap (≥3B) CEO/CFO | low | 7 | open | 1 | 0.0 | -2.7 | -2.7 | -2.7 | nan | nan | -2.7 | -2.7 |
| 2346 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_low_7d_open | Large cap (≥5B) CEO/CFO | low | 7 | open | 1 | 0.0 | -2.7 | -2.7 | -2.7 | nan | nan | -2.7 | -2.7 |
| 2347 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_low_7d_open | Large cap (≥10B) CEO/CFO | low | 7 | open | 1 | 0.0 | -2.7 | -2.7 | -2.7 | nan | nan | -2.7 | -2.7 |
| 2348 | 15 | 62.43 | Price > MA50 — hold ret_low_7d_open | Price > MA50 | low | 7 | open | 5 | 0.0 | -2.7 | -2.7 | -13.49 | 2.82 | -0.96 | -6.57 | 0.0 |
| 2349 | 14 | 65.45 | Price > MA200 — hold ret_low_7d_open | Price > MA200 | low | 7 | open | 4 | 0.0 | -2.7 | -2.11 | -10.79 | 3.26 | -0.83 | -6.57 | 0.0 |
| 2350 | 30 | 48.32 | Value ≥100k — hold ret_low_3d_news | Value ≥100k | low | 3 | news | 6 | 33.3 | -2.71 | -1.79 | -16.25 | 4.18 | -0.65 | -9.04 | 1.43 |
| 2351 | 49 | 32.78 | CFO only — hold ret_mean_3d_news | CFO only | mean | 3 | news | 1 | 0.0 | -2.76 | -2.76 | -2.76 | nan | nan | -2.76 | -2.76 |
| 2352 | 48 | 32.78 | CFO + Director (combo) — hold ret_mean_3d_news | CFO + Director (combo) | mean | 3 | news | 1 | 0.0 | -2.76 | -2.76 | -2.76 | nan | nan | -2.76 | -2.76 |
| 2353 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_mean_3d_news | CFO only + Value ≥50k | mean | 3 | news | 1 | 0.0 | -2.76 | -2.76 | -2.76 | nan | nan | -2.76 | -2.76 |
| 2354 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_mean_3d_news | CFO only + Value ≥100k | mean | 3 | news | 1 | 0.0 | -2.76 | -2.76 | -2.76 | nan | nan | -2.76 | -2.76 |
| 2355 | 47 | 32.78 | CFO only + Position +10% — hold ret_mean_3d_news | CFO only + Position +10% | mean | 3 | news | 1 | 0.0 | -2.76 | -2.76 | -2.76 | nan | nan | -2.76 | -2.76 |
| 2356 | 46 | 32.78 | CFO only + Position +20% — hold ret_mean_3d_news | CFO only + Position +20% | mean | 3 | news | 1 | 0.0 | -2.76 | -2.76 | -2.76 | nan | nan | -2.76 | -2.76 |
| 2357 | 44 | 32.78 | RSI oversold (<30) — hold ret_mean_3d_news | RSI oversold (<30) | mean | 3 | news | 1 | 0.0 | -2.76 | -2.76 | -2.76 | nan | nan | -2.76 | -2.76 |
| 2358 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_mean_3d_news | RSI oversold + CEO/CFO | mean | 3 | news | 1 | 0.0 | -2.76 | -2.76 | -2.76 | nan | nan | -2.76 | -2.76 |
| 2359 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_mean_3d_news | RSI oversold + Value ≥100k | mean | 3 | news | 1 | 0.0 | -2.76 | -2.76 | -2.76 | nan | nan | -2.76 | -2.76 |
| 2360 | 39 | 34.48 | Position +20% — hold ret_mean_14d_open | Position +20% | mean | 14 | open | 4 | 50.0 | -2.84 | 1.57 | -11.36 | 10.68 | -0.27 | -18.64 | 4.15 |
| 2361 | 28 | 48.48 | Tutti — hold ret_low_3d_open | Tutti | low | 3 | open | 10 | 0.0 | -2.88 | -2.49 | -28.75 | 2.78 | -1.04 | -9.71 | 0.0 |
| 2362 | 26 | 50.0 | Qty ≥50k shares — hold ret_mean_14d_open | Qty ≥50k shares | mean | 14 | open | 2 | 50.0 | -2.88 | -2.88 | -5.75 | 22.3 | -0.13 | -18.64 | 12.89 |
| 2363 | 27 | 50.0 | Value ≥1M — hold ret_mean_14d_open | Value ≥1M | mean | 14 | open | 2 | 50.0 | -2.88 | -2.88 | -5.75 | 22.3 | -0.13 | -18.64 | 12.89 |
| 2364 | 51 | 20.1 | Position +30% — hold ret_low_1d_news | Position +30% | low | 1 | news | 3 | 0.0 | -2.9 | -2.49 | -8.69 | 2.82 | -1.03 | -5.9 | -0.3 |
| 2365 | 51 | 20.1 | Position +30% — hold ret_low_2d_news | Position +30% | low | 2 | news | 3 | 0.0 | -2.9 | -2.49 | -8.69 | 2.82 | -1.03 | -5.9 | -0.3 |
| 2366 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_mean_10d_news | Far 52w high + Value ≥100k | mean | 10 | news | 3 | 33.3 | -2.9 | -0.36 | -8.69 | 8.34 | -0.35 | -12.21 | 3.88 |
| 2367 | 26 | 50.0 | Qty ≥50k shares — hold ret_mean_30d_news | Qty ≥50k shares | mean | 30 | news | 2 | 50.0 | -2.91 | -2.91 | -5.83 | 23.31 | -0.13 | -19.4 | 13.57 |
| 2368 | 27 | 50.0 | Value ≥1M — hold ret_mean_30d_news | Value ≥1M | mean | 30 | news | 2 | 50.0 | -2.91 | -2.91 | -5.83 | 23.31 | -0.13 | -19.4 | 13.57 |
| 2369 | 14 | 65.45 | Price > MA200 — hold ret_low_10d_open | Price > MA200 | low | 10 | open | 4 | 0.0 | -2.92 | -2.54 | -11.66 | 3.04 | -0.96 | -6.57 | 0.0 |
| 2370 | 14 | 65.45 | Price > MA200 — hold ret_low_14d_open | Price > MA200 | low | 14 | open | 4 | 0.0 | -2.92 | -2.54 | -11.66 | 3.04 | -0.96 | -6.57 | 0.0 |
| 2371 | 14 | 65.45 | Price > MA200 — hold ret_low_30d_open | Price > MA200 | low | 30 | open | 4 | 0.0 | -2.92 | -2.54 | -11.66 | 3.04 | -0.96 | -6.57 | 0.0 |
| 2372 | 31 | 47.75 | Value ≥50k — hold ret_low_3d_open | Value ≥50k | low | 3 | open | 9 | 0.0 | -2.96 | -2.7 | -26.63 | 2.93 | -1.01 | -9.71 | 0.0 |
| 2373 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_low_3d_open | Large cap (≥2B) CEO/CFO | low | 3 | open | 2 | 0.0 | -2.99 | -2.99 | -5.98 | 0.41 | -7.29 | -3.28 | -2.7 |
| 2374 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_low_5d_open | Large cap (≥2B) CEO/CFO | low | 5 | open | 2 | 0.0 | -2.99 | -2.99 | -5.98 | 0.41 | -7.29 | -3.28 | -2.7 |
| 2375 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_low_7d_open | Large cap (≥2B) CEO/CFO | low | 7 | open | 2 | 0.0 | -2.99 | -2.99 | -5.98 | 0.41 | -7.29 | -3.28 | -2.7 |
| 2376 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_low_3d_news | Large cap (≥2B) CEO/CFO | low | 3 | news | 2 | 0.0 | -3.01 | -3.01 | -6.01 | 4.09 | -0.73 | -5.9 | -0.11 |
| 2377 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_low_5d_news | Large cap (≥2B) CEO/CFO | low | 5 | news | 2 | 0.0 | -3.01 | -3.01 | -6.01 | 4.09 | -0.73 | -5.9 | -0.11 |
| 2378 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_low_7d_news | Large cap (≥2B) CEO/CFO | low | 7 | news | 2 | 0.0 | -3.01 | -3.01 | -6.01 | 4.09 | -0.73 | -5.9 | -0.11 |
| 2379 | 21 | 53.67 | Qty ≥5k shares — hold ret_low_3d_news | Qty ≥5k shares | low | 3 | news | 6 | 33.3 | -3.04 | -2.79 | -18.24 | 4.01 | -0.76 | -9.04 | 1.43 |
| 2380 | 20 | 53.67 | Qty ≥10k shares — hold ret_low_3d_news | Qty ≥10k shares | low | 3 | news | 6 | 33.3 | -3.04 | -2.79 | -18.24 | 4.01 | -0.76 | -9.04 | 1.43 |
| 2381 | 21 | 53.67 | Qty ≥5k shares — hold ret_low_3d_open | Qty ≥5k shares | low | 3 | open | 6 | 0.0 | -3.06 | -2.21 | -18.36 | 3.69 | -0.83 | -9.71 | 0.0 |
| 2382 | 20 | 53.67 | Qty ≥10k shares — hold ret_low_3d_open | Qty ≥10k shares | low | 3 | open | 6 | 0.0 | -3.06 | -2.21 | -18.36 | 3.69 | -0.83 | -9.71 | 0.0 |
| 2383 | 32 | 44.63 | Position +10% — hold ret_low_3d_news | Position +10% | low | 3 | news | 6 | 33.3 | -3.08 | -2.9 | -18.46 | 3.99 | -0.77 | -9.04 | 1.43 |
| 2384 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_mean_10d_open | Far 52w high + Value ≥100k | mean | 10 | open | 3 | 66.7 | -3.08 | 1.19 | -9.24 | 8.48 | -0.36 | -12.85 | 2.42 |
| 2385 | 49 | 32.78 | CFO only — hold ret_mean_2d_news | CFO only | mean | 2 | news | 1 | 0.0 | -3.09 | -3.09 | -3.09 | nan | nan | -3.09 | -3.09 |
| 2386 | 48 | 32.78 | CFO + Director (combo) — hold ret_mean_2d_news | CFO + Director (combo) | mean | 2 | news | 1 | 0.0 | -3.09 | -3.09 | -3.09 | nan | nan | -3.09 | -3.09 |
| 2387 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_mean_2d_news | CFO only + Value ≥50k | mean | 2 | news | 1 | 0.0 | -3.09 | -3.09 | -3.09 | nan | nan | -3.09 | -3.09 |
| 2388 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_mean_2d_news | CFO only + Value ≥100k | mean | 2 | news | 1 | 0.0 | -3.09 | -3.09 | -3.09 | nan | nan | -3.09 | -3.09 |
| 2389 | 47 | 32.78 | CFO only + Position +10% — hold ret_mean_2d_news | CFO only + Position +10% | mean | 2 | news | 1 | 0.0 | -3.09 | -3.09 | -3.09 | nan | nan | -3.09 | -3.09 |
| 2390 | 46 | 32.78 | CFO only + Position +20% — hold ret_mean_2d_news | CFO only + Position +20% | mean | 2 | news | 1 | 0.0 | -3.09 | -3.09 | -3.09 | nan | nan | -3.09 | -3.09 |
| 2391 | 44 | 32.78 | RSI oversold (<30) — hold ret_mean_2d_news | RSI oversold (<30) | mean | 2 | news | 1 | 0.0 | -3.09 | -3.09 | -3.09 | nan | nan | -3.09 | -3.09 |
| 2392 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_mean_2d_news | RSI oversold + CEO/CFO | mean | 2 | news | 1 | 0.0 | -3.09 | -3.09 | -3.09 | nan | nan | -3.09 | -3.09 |
| 2393 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_mean_2d_news | RSI oversold + Value ≥100k | mean | 2 | news | 1 | 0.0 | -3.09 | -3.09 | -3.09 | nan | nan | -3.09 | -3.09 |
| 2394 | 32 | 44.63 | Position +10% — hold ret_low_3d_open | Position +10% | low | 3 | open | 6 | 0.0 | -3.09 | -2.77 | -18.56 | 3.57 | -0.87 | -9.71 | 0.0 |
| 2395 | 36 | 36.54 | Director only (no C-level) — hold ret_mean_90d_news | Director only (no C-level) | mean | 90 | news | 6 | 66.7 | -3.09 | 0.06 | -18.53 | 11.72 | -0.26 | -26.12 | 7.62 |
| 2396 | 39 | 34.48 | Position +20% — hold ret_mean_30d_open | Position +20% | mean | 30 | open | 4 | 50.0 | -3.12 | 1.11 | -12.46 | 11.54 | -0.27 | -19.99 | 5.31 |
| 2397 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_mean_90d_news | Large cap (≥3B) CEO/CFO | mean | 90 | news | 1 | 0.0 | -3.15 | -3.15 | -3.15 | nan | nan | -3.15 | -3.15 |
| 2398 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_mean_90d_news | Large cap (≥5B) CEO/CFO | mean | 90 | news | 1 | 0.0 | -3.15 | -3.15 | -3.15 | nan | nan | -3.15 | -3.15 |
| 2399 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_mean_90d_news | Large cap (≥10B) CEO/CFO | mean | 90 | news | 1 | 0.0 | -3.15 | -3.15 | -3.15 | nan | nan | -3.15 | -3.15 |
| 2400 | 36 | 36.54 | Director only (no C-level) — hold ret_mean_60d_news | Director only (no C-level) | mean | 60 | news | 6 | 66.7 | -3.18 | 1.23 | -19.11 | 12.53 | -0.25 | -28.39 | 5.21 |
| 2401 | 39 | 34.48 | Position +20% — hold ret_mean_14d_news | Position +20% | mean | 14 | news | 4 | 50.0 | -3.23 | 0.55 | -12.93 | 10.02 | -0.32 | -18.03 | 4.01 |
| 2402 | 33 | 41.81 | Director — hold ret_low_3d_open | Director | low | 3 | open | 8 | 0.0 | -3.26 | -2.77 | -26.05 | 2.92 | -1.11 | -9.71 | 0.0 |
| 2403 | 36 | 36.54 | Director only (no C-level) — hold ret_low_3d_news | Director only (no C-level) | low | 3 | news | 6 | 16.7 | -3.26 | -2.9 | -19.58 | 3.23 | -1.01 | -9.04 | 0.84 |
| 2404 | 30 | 48.32 | Value ≥100k — hold ret_mean_60d_news | Value ≥100k | mean | 60 | news | 6 | 66.7 | -3.26 | 1.57 | -19.56 | 12.73 | -0.26 | -28.39 | 5.21 |
| 2405 | 49 | 32.78 | CFO only — hold ret_low_1d_open | CFO only | low | 1 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2406 | 48 | 32.78 | CFO + Director (combo) — hold ret_low_1d_open | CFO + Director (combo) | low | 1 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2407 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_low_1d_open | CFO only + Value ≥50k | low | 1 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2408 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_low_1d_open | CFO only + Value ≥100k | low | 1 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2409 | 47 | 32.78 | CFO only + Position +10% — hold ret_low_1d_open | CFO only + Position +10% | low | 1 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2410 | 46 | 32.78 | CFO only + Position +20% — hold ret_low_1d_open | CFO only + Position +20% | low | 1 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2411 | 44 | 32.78 | RSI oversold (<30) — hold ret_low_1d_open | RSI oversold (<30) | low | 1 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2412 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_low_1d_open | RSI oversold + CEO/CFO | low | 1 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2413 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_low_1d_open | RSI oversold + Value ≥100k | low | 1 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2414 | 49 | 32.78 | CFO only — hold ret_low_2d_open | CFO only | low | 2 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2415 | 48 | 32.78 | CFO + Director (combo) — hold ret_low_2d_open | CFO + Director (combo) | low | 2 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2416 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_low_2d_open | CFO only + Value ≥50k | low | 2 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2417 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_low_2d_open | CFO only + Value ≥100k | low | 2 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2418 | 47 | 32.78 | CFO only + Position +10% — hold ret_low_2d_open | CFO only + Position +10% | low | 2 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2419 | 46 | 32.78 | CFO only + Position +20% — hold ret_low_2d_open | CFO only + Position +20% | low | 2 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2420 | 44 | 32.78 | RSI oversold (<30) — hold ret_low_2d_open | RSI oversold (<30) | low | 2 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2421 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_low_2d_open | RSI oversold + CEO/CFO | low | 2 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2422 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_low_2d_open | RSI oversold + Value ≥100k | low | 2 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2423 | 49 | 32.78 | CFO only — hold ret_low_3d_open | CFO only | low | 3 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2424 | 48 | 32.78 | CFO + Director (combo) — hold ret_low_3d_open | CFO + Director (combo) | low | 3 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2425 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_low_3d_open | CFO only + Value ≥50k | low | 3 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2426 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_low_3d_open | CFO only + Value ≥100k | low | 3 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2427 | 47 | 32.78 | CFO only + Position +10% — hold ret_low_3d_open | CFO only + Position +10% | low | 3 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2428 | 46 | 32.78 | CFO only + Position +20% — hold ret_low_3d_open | CFO only + Position +20% | low | 3 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2429 | 44 | 32.78 | RSI oversold (<30) — hold ret_low_3d_open | RSI oversold (<30) | low | 3 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2430 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_low_3d_open | RSI oversold + CEO/CFO | low | 3 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2431 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_low_3d_open | RSI oversold + Value ≥100k | low | 3 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2432 | 49 | 32.78 | CFO only — hold ret_low_5d_open | CFO only | low | 5 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2433 | 48 | 32.78 | CFO + Director (combo) — hold ret_low_5d_open | CFO + Director (combo) | low | 5 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2434 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_low_5d_open | CFO only + Value ≥50k | low | 5 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2435 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_low_5d_open | CFO only + Value ≥100k | low | 5 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2436 | 47 | 32.78 | CFO only + Position +10% — hold ret_low_5d_open | CFO only + Position +10% | low | 5 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2437 | 46 | 32.78 | CFO only + Position +20% — hold ret_low_5d_open | CFO only + Position +20% | low | 5 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2438 | 44 | 32.78 | RSI oversold (<30) — hold ret_low_5d_open | RSI oversold (<30) | low | 5 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2439 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_low_5d_open | RSI oversold + CEO/CFO | low | 5 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2440 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_low_5d_open | RSI oversold + Value ≥100k | low | 5 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2441 | 49 | 32.78 | CFO only — hold ret_low_7d_open | CFO only | low | 7 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2442 | 48 | 32.78 | CFO + Director (combo) — hold ret_low_7d_open | CFO + Director (combo) | low | 7 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2443 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_low_7d_open | CFO only + Value ≥50k | low | 7 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2444 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_low_7d_open | CFO only + Value ≥100k | low | 7 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2445 | 47 | 32.78 | CFO only + Position +10% — hold ret_low_7d_open | CFO only + Position +10% | low | 7 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2446 | 46 | 32.78 | CFO only + Position +20% — hold ret_low_7d_open | CFO only + Position +20% | low | 7 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2447 | 44 | 32.78 | RSI oversold (<30) — hold ret_low_7d_open | RSI oversold (<30) | low | 7 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2448 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_low_7d_open | RSI oversold + CEO/CFO | low | 7 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2449 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_low_7d_open | RSI oversold + Value ≥100k | low | 7 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2450 | 49 | 32.78 | CFO only — hold ret_low_10d_open | CFO only | low | 10 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2451 | 48 | 32.78 | CFO + Director (combo) — hold ret_low_10d_open | CFO + Director (combo) | low | 10 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2452 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_low_10d_open | CFO only + Value ≥50k | low | 10 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2453 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_low_10d_open | CFO only + Value ≥100k | low | 10 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2454 | 47 | 32.78 | CFO only + Position +10% — hold ret_low_10d_open | CFO only + Position +10% | low | 10 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2455 | 46 | 32.78 | CFO only + Position +20% — hold ret_low_10d_open | CFO only + Position +20% | low | 10 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2456 | 44 | 32.78 | RSI oversold (<30) — hold ret_low_10d_open | RSI oversold (<30) | low | 10 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2457 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_low_10d_open | RSI oversold + CEO/CFO | low | 10 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2458 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_low_10d_open | RSI oversold + Value ≥100k | low | 10 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2459 | 49 | 32.78 | CFO only — hold ret_low_14d_open | CFO only | low | 14 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2460 | 48 | 32.78 | CFO + Director (combo) — hold ret_low_14d_open | CFO + Director (combo) | low | 14 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2461 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_low_14d_open | CFO only + Value ≥50k | low | 14 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2462 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_low_14d_open | CFO only + Value ≥100k | low | 14 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2463 | 47 | 32.78 | CFO only + Position +10% — hold ret_low_14d_open | CFO only + Position +10% | low | 14 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2464 | 46 | 32.78 | CFO only + Position +20% — hold ret_low_14d_open | CFO only + Position +20% | low | 14 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2465 | 44 | 32.78 | RSI oversold (<30) — hold ret_low_14d_open | RSI oversold (<30) | low | 14 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2466 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_low_14d_open | RSI oversold + CEO/CFO | low | 14 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2467 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_low_14d_open | RSI oversold + Value ≥100k | low | 14 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2468 | 49 | 32.78 | CFO only — hold ret_low_30d_open | CFO only | low | 30 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2469 | 48 | 32.78 | CFO + Director (combo) — hold ret_low_30d_open | CFO + Director (combo) | low | 30 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2470 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_low_30d_open | CFO only + Value ≥50k | low | 30 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2471 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_low_30d_open | CFO only + Value ≥100k | low | 30 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2472 | 47 | 32.78 | CFO only + Position +10% — hold ret_low_30d_open | CFO only + Position +10% | low | 30 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2473 | 46 | 32.78 | CFO only + Position +20% — hold ret_low_30d_open | CFO only + Position +20% | low | 30 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2474 | 44 | 32.78 | RSI oversold (<30) — hold ret_low_30d_open | RSI oversold (<30) | low | 30 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2475 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_low_30d_open | RSI oversold + CEO/CFO | low | 30 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2476 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_low_30d_open | RSI oversold + Value ≥100k | low | 30 | open | 1 | 0.0 | -3.28 | -3.28 | -3.28 | nan | nan | -3.28 | -3.28 |
| 2477 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_low_1d_news | Multiple buys (n≥2) | low | 1 | news | 3 | 0.0 | -3.31 | -2.1 | -9.94 | 2.24 | -1.48 | -5.9 | -1.94 |
| 2478 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_low_2d_news | Multiple buys (n≥2) | low | 2 | news | 3 | 0.0 | -3.31 | -2.1 | -9.94 | 2.24 | -1.48 | -5.9 | -1.94 |
| 2479 | 30 | 48.32 | Value ≥100k — hold ret_low_3d_open | Value ≥100k | low | 3 | open | 6 | 0.0 | -3.32 | -2.99 | -19.91 | 3.58 | -0.93 | -9.71 | 0.0 |
| 2480 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_low_5d_open | Multiple buys (n≥2) | low | 5 | open | 3 | 0.0 | -3.32 | -3.28 | -9.96 | 2.19 | -1.52 | -5.53 | -1.15 |
| 2481 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_low_7d_open | Multiple buys (n≥2) | low | 7 | open | 3 | 0.0 | -3.32 | -3.28 | -9.96 | 2.19 | -1.52 | -5.53 | -1.15 |
| 2482 | 6 | 77.62 | CEO only — hold ret_low_10d_news | CEO only | low | 10 | news | 3 | 33.3 | -3.32 | -2.1 | -9.95 | 5.46 | -0.61 | -9.28 | 1.43 |
| 2483 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_low_10d_open | Multiple buys (n≥2) | low | 10 | open | 3 | 0.0 | -3.32 | -3.28 | -9.96 | 2.19 | -1.52 | -5.53 | -1.15 |
| 2484 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_low_14d_open | Multiple buys (n≥2) | low | 14 | open | 3 | 0.0 | -3.32 | -3.28 | -9.96 | 2.19 | -1.52 | -5.53 | -1.15 |
| 2485 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_low_30d_open | Multiple buys (n≥2) | low | 30 | open | 3 | 0.0 | -3.32 | -3.28 | -9.96 | 2.19 | -1.52 | -5.53 | -1.15 |
| 2486 | 51 | 20.1 | Position +30% — hold ret_mean_10d_open | Position +30% | mean | 10 | open | 3 | 66.7 | -3.34 | 0.4 | -10.03 | 8.29 | -0.4 | -12.85 | 2.42 |
| 2487 | 37 | 35.58 | Director only + Value ≥100k — hold ret_mean_10d_open | Director only + Value ≥100k | mean | 10 | open | 3 | 33.3 | -3.39 | -0.97 | -10.17 | 8.51 | -0.4 | -12.85 | 3.65 |
| 2488 | 36 | 36.54 | Director only (no C-level) — hold ret_mean_90d_open | Director only (no C-level) | mean | 90 | open | 6 | 50.0 | -3.42 | -0.24 | -20.51 | 11.75 | -0.29 | -26.66 | 6.78 |
| 2489 | 33 | 41.81 | Director — hold ret_low_3d_news | Director | low | 3 | news | 8 | 12.5 | -3.45 | -2.9 | -27.58 | 2.93 | -1.18 | -9.04 | 0.84 |
| 2490 | 40 | 33.74 | Director only + Position +10% — hold ret_low_3d_news | Director only + Position +10% | low | 3 | news | 4 | 25.0 | -3.5 | -2.9 | -13.99 | 4.11 | -0.85 | -9.04 | 0.84 |
| 2491 | 39 | 34.48 | Position +20% — hold ret_mean_30d_news | Position +20% | mean | 30 | news | 4 | 50.0 | -3.52 | 0.68 | -14.08 | 10.8 | -0.33 | -19.4 | 3.96 |
| 2492 | 36 | 36.54 | Director only (no C-level) — hold ret_mean_60d_open | Director only (no C-level) | mean | 60 | open | 6 | 66.7 | -3.52 | 0.91 | -21.09 | 12.58 | -0.28 | -28.92 | 4.39 |
| 2493 | 22 | 53.36 | RSI overbought (>70) — hold ret_low_60d_news | RSI overbought (>70) | low | 60 | news | 2 | 0.0 | -3.54 | -3.54 | -7.08 | 0.1 | -35.76 | -3.61 | -3.47 |
| 2494 | 32 | 44.63 | Position +10% — hold ret_mean_60d_open | Position +10% | mean | 60 | open | 6 | 66.7 | -3.57 | 0.91 | -21.42 | 12.54 | -0.28 | -28.92 | 3.7 |
| 2495 | 15 | 62.43 | Price > MA50 — hold ret_low_10d_news | Price > MA50 | low | 10 | news | 5 | 20.0 | -3.59 | -3.47 | -17.93 | 4.45 | -0.81 | -9.28 | 1.43 |
| 2496 | 49 | 32.78 | CFO only — hold ret_mean_1d_news | CFO only | mean | 1 | news | 1 | 0.0 | -3.6 | -3.6 | -3.6 | nan | nan | -3.6 | -3.6 |
| 2497 | 48 | 32.78 | CFO + Director (combo) — hold ret_mean_1d_news | CFO + Director (combo) | mean | 1 | news | 1 | 0.0 | -3.6 | -3.6 | -3.6 | nan | nan | -3.6 | -3.6 |
| 2498 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_mean_1d_news | CFO only + Value ≥50k | mean | 1 | news | 1 | 0.0 | -3.6 | -3.6 | -3.6 | nan | nan | -3.6 | -3.6 |
| 2499 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_mean_1d_news | CFO only + Value ≥100k | mean | 1 | news | 1 | 0.0 | -3.6 | -3.6 | -3.6 | nan | nan | -3.6 | -3.6 |
| 2500 | 47 | 32.78 | CFO only + Position +10% — hold ret_mean_1d_news | CFO only + Position +10% | mean | 1 | news | 1 | 0.0 | -3.6 | -3.6 | -3.6 | nan | nan | -3.6 | -3.6 |
| 2501 | 46 | 32.78 | CFO only + Position +20% — hold ret_mean_1d_news | CFO only + Position +20% | mean | 1 | news | 1 | 0.0 | -3.6 | -3.6 | -3.6 | nan | nan | -3.6 | -3.6 |
| 2502 | 44 | 32.78 | RSI oversold (<30) — hold ret_mean_1d_news | RSI oversold (<30) | mean | 1 | news | 1 | 0.0 | -3.6 | -3.6 | -3.6 | nan | nan | -3.6 | -3.6 |
| 2503 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_mean_1d_news | RSI oversold + CEO/CFO | mean | 1 | news | 1 | 0.0 | -3.6 | -3.6 | -3.6 | nan | nan | -3.6 | -3.6 |
| 2504 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_mean_1d_news | RSI oversold + Value ≥100k | mean | 1 | news | 1 | 0.0 | -3.6 | -3.6 | -3.6 | nan | nan | -3.6 | -3.6 |
| 2505 | 36 | 36.54 | Director only (no C-level) — hold ret_low_3d_open | Director only (no C-level) | low | 3 | open | 6 | 0.0 | -3.6 | -2.79 | -21.62 | 3.31 | -1.09 | -9.71 | 0.0 |
| 2506 | 32 | 44.63 | Position +10% — hold ret_mean_60d_news | Position +10% | mean | 60 | news | 6 | 66.7 | -3.6 | 0.55 | -21.6 | 12.29 | -0.29 | -28.39 | 4.46 |
| 2507 | 40 | 33.74 | Director only + Position +10% — hold ret_mean_14d_news | Director only + Position +10% | mean | 14 | news | 4 | 25.0 | -3.67 | -0.34 | -14.69 | 9.79 | -0.38 | -18.03 | 4.01 |
| 2508 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_low_3d_news | Multiple buys (n≥2) | low | 3 | news | 3 | 0.0 | -3.77 | -3.3 | -11.3 | 1.94 | -1.94 | -5.9 | -2.1 |
| 2509 | 31 | 47.75 | Value ≥50k — hold ret_low_5d_news | Value ≥50k | low | 5 | news | 9 | 22.2 | -3.78 | -2.49 | -34.0 | 5.48 | -0.69 | -16.67 | 1.43 |
| 2510 | 26 | 50.0 | Qty ≥50k shares — hold ret_low_3d_news | Qty ≥50k shares | low | 3 | news | 2 | 50.0 | -3.8 | -3.8 | -7.61 | 7.4 | -0.51 | -9.04 | 1.43 |
| 2511 | 27 | 50.0 | Value ≥1M — hold ret_low_3d_news | Value ≥1M | low | 3 | news | 2 | 50.0 | -3.8 | -3.8 | -7.61 | 7.4 | -0.51 | -9.04 | 1.43 |
| 2512 | 39 | 34.48 | Position +20% — hold ret_low_3d_open | Position +20% | low | 3 | open | 4 | 0.0 | -3.82 | -2.77 | -15.26 | 4.16 | -0.92 | -9.71 | 0.0 |
| 2513 | 40 | 33.74 | Director only + Position +10% — hold ret_low_3d_open | Director only + Position +10% | low | 3 | open | 4 | 0.0 | -3.82 | -2.79 | -15.28 | 4.16 | -0.92 | -9.71 | 0.0 |
| 2514 | 30 | 48.32 | Value ≥100k — hold ret_mean_60d_open | Value ≥100k | mean | 60 | open | 6 | 66.7 | -3.82 | 2.19 | -22.91 | 12.92 | -0.3 | -28.92 | 4.39 |
| 2515 | 37 | 35.58 | Director only + Value ≥100k — hold ret_low_3d_news | Director only + Value ≥100k | low | 3 | news | 3 | 33.3 | -3.89 | -3.47 | -11.67 | 4.95 | -0.79 | -9.04 | 0.84 |
| 2516 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_low_10d_news | CEO only + Value ≥100k | low | 10 | news | 2 | 50.0 | -3.92 | -3.92 | -7.85 | 7.57 | -0.52 | -9.28 | 1.43 |
| 2517 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_low_10d_news | Price > MA50 + CEO/CFO | low | 10 | news | 2 | 50.0 | -3.92 | -3.92 | -7.85 | 7.57 | -0.52 | -9.28 | 1.43 |
| 2518 | 38 | 34.53 | Price < MA50 — hold ret_low_3d_open | Price < MA50 | low | 3 | open | 5 | 0.0 | -3.94 | -3.28 | -19.71 | 3.34 | -1.18 | -9.71 | -1.15 |
| 2519 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_mean_30d_open | Large cap (≥3B) CEO/CFO | mean | 30 | open | 1 | 0.0 | -3.95 | -3.95 | -3.95 | nan | nan | -3.95 | -3.95 |
| 2520 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_mean_30d_open | Large cap (≥5B) CEO/CFO | mean | 30 | open | 1 | 0.0 | -3.95 | -3.95 | -3.95 | nan | nan | -3.95 | -3.95 |
| 2521 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_mean_30d_open | Large cap (≥10B) CEO/CFO | mean | 30 | open | 1 | 0.0 | -3.95 | -3.95 | -3.95 | nan | nan | -3.95 | -3.95 |
| 2522 | 10 | 66.41 | CEO/CFO — hold ret_low_10d_news | CEO/CFO | low | 10 | news | 4 | 25.0 | -3.96 | -4.0 | -15.85 | 4.64 | -0.85 | -9.28 | 1.43 |
| 2523 | 11 | 66.41 | Officer/President — hold ret_low_10d_news | Officer/President | low | 10 | news | 4 | 25.0 | -3.96 | -4.0 | -15.85 | 4.64 | -0.85 | -9.28 | 1.43 |
| 2524 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_low_10d_news | Large cap (≥250M) CEO/CFO | low | 10 | news | 4 | 25.0 | -3.96 | -4.0 | -15.85 | 4.64 | -0.85 | -9.28 | 1.43 |
| 2525 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_low_10d_news | Large cap (≥500M) CEO/CFO | low | 10 | news | 4 | 25.0 | -3.96 | -4.0 | -15.85 | 4.64 | -0.85 | -9.28 | 1.43 |
| 2526 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_mean_60d_news | Large cap (≥3B) CEO/CFO | mean | 60 | news | 1 | 0.0 | -3.97 | -3.97 | -3.97 | nan | nan | -3.97 | -3.97 |
| 2527 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_mean_60d_news | Large cap (≥5B) CEO/CFO | mean | 60 | news | 1 | 0.0 | -3.97 | -3.97 | -3.97 | nan | nan | -3.97 | -3.97 |
| 2528 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_mean_60d_news | Large cap (≥10B) CEO/CFO | mean | 60 | news | 1 | 0.0 | -3.97 | -3.97 | -3.97 | nan | nan | -3.97 | -3.97 |
| 2529 | 30 | 48.32 | Value ≥100k — hold ret_low_5d_news | Value ≥100k | low | 5 | news | 6 | 33.3 | -3.98 | -1.79 | -23.88 | 6.82 | -0.58 | -16.67 | 1.43 |
| 2530 | 40 | 33.74 | Director only + Position +10% — hold ret_mean_14d_open | Director only + Position +10% | mean | 14 | open | 4 | 25.0 | -3.99 | -0.23 | -15.95 | 9.9 | -0.4 | -18.64 | 3.14 |
| 2531 | 28 | 48.48 | Tutti — hold ret_low_5d_news | Tutti | low | 5 | news | 10 | 20.0 | -4.01 | -2.98 | -40.1 | 5.22 | -0.77 | -16.67 | 1.43 |
| 2532 | 26 | 50.0 | Qty ≥50k shares — hold ret_mean_30d_open | Qty ≥50k shares | mean | 30 | open | 2 | 50.0 | -4.01 | -4.01 | -8.02 | 22.6 | -0.18 | -19.99 | 11.97 |
| 2533 | 27 | 50.0 | Value ≥1M — hold ret_mean_30d_open | Value ≥1M | mean | 30 | open | 2 | 50.0 | -4.01 | -4.01 | -8.02 | 22.6 | -0.18 | -19.99 | 11.97 |
| 2534 | 10 | 66.41 | CEO/CFO — hold ret_low_10d_open | CEO/CFO | low | 10 | open | 4 | 0.0 | -4.02 | -2.21 | -16.06 | 5.26 | -0.76 | -11.63 | 0.0 |
| 2535 | 11 | 66.41 | Officer/President — hold ret_low_10d_open | Officer/President | low | 10 | open | 4 | 0.0 | -4.02 | -2.21 | -16.06 | 5.26 | -0.76 | -11.63 | 0.0 |
| 2536 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_low_10d_open | Large cap (≥250M) CEO/CFO | low | 10 | open | 4 | 0.0 | -4.02 | -2.21 | -16.06 | 5.26 | -0.76 | -11.63 | 0.0 |
| 2537 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_low_10d_open | Large cap (≥500M) CEO/CFO | low | 10 | open | 4 | 0.0 | -4.02 | -2.21 | -16.06 | 5.26 | -0.76 | -11.63 | 0.0 |
| 2538 | 31 | 47.75 | Value ≥50k — hold ret_low_5d_open | Value ≥50k | low | 5 | open | 9 | 0.0 | -4.05 | -2.7 | -36.43 | 5.29 | -0.76 | -17.28 | 0.0 |
| 2539 | 15 | 62.43 | Price > MA50 — hold ret_low_14d_news | Price > MA50 | low | 14 | news | 5 | 20.0 | -4.05 | -3.47 | -20.27 | 5.25 | -0.77 | -11.62 | 1.43 |
| 2540 | 15 | 62.43 | Price > MA50 — hold ret_low_30d_news | Price > MA50 | low | 30 | news | 5 | 20.0 | -4.05 | -3.47 | -20.27 | 5.25 | -0.77 | -11.62 | 1.43 |
| 2541 | 6 | 77.62 | CEO only — hold ret_low_14d_news | CEO only | low | 14 | news | 3 | 33.3 | -4.1 | -2.1 | -12.29 | 6.75 | -0.61 | -11.62 | 1.43 |
| 2542 | 6 | 77.62 | CEO only — hold ret_low_30d_news | CEO only | low | 30 | news | 3 | 33.3 | -4.1 | -2.1 | -12.29 | 6.75 | -0.61 | -11.62 | 1.43 |
| 2543 | 51 | 20.1 | Position +30% — hold ret_mean_10d_news | Position +30% | mean | 10 | news | 3 | 33.3 | -4.13 | -0.36 | -12.39 | 7.0 | -0.59 | -12.21 | 0.18 |
| 2544 | 39 | 34.48 | Position +20% — hold ret_low_3d_news | Position +20% | low | 3 | news | 4 | 25.0 | -4.15 | -4.2 | -16.59 | 4.27 | -0.97 | -9.04 | 0.84 |
| 2545 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_mean_90d_open | CEO only + Value ≥100k | mean | 90 | open | 2 | 0.0 | -4.16 | -4.16 | -8.31 | 2.11 | -1.97 | -5.65 | -2.66 |
| 2546 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_mean_90d_open | Price > MA50 + CEO/CFO | mean | 90 | open | 2 | 0.0 | -4.16 | -4.16 | -8.31 | 2.11 | -1.97 | -5.65 | -2.66 |
| 2547 | 30 | 48.32 | Value ≥100k — hold ret_mean_90d_news | Value ≥100k | mean | 90 | news | 6 | 33.3 | -4.17 | -1.7 | -25.0 | 11.42 | -0.36 | -26.12 | 7.62 |
| 2548 | 35 | 40.48 | Value ≥500k — hold ret_low_3d_news | Value ≥500k | low | 3 | news | 4 | 25.0 | -4.24 | -4.69 | -16.98 | 4.42 | -0.96 | -9.04 | 1.43 |
| 2549 | 28 | 48.48 | Tutti — hold ret_low_5d_open | Tutti | low | 5 | open | 10 | 0.0 | -4.25 | -2.99 | -42.53 | 5.03 | -0.85 | -17.28 | 0.0 |
| 2550 | 6 | 77.62 | CEO only — hold ret_low_10d_open | CEO only | low | 10 | open | 3 | 0.0 | -4.26 | -1.15 | -12.78 | 6.41 | -0.66 | -11.63 | 0.0 |
| 2551 | 35 | 40.48 | Value ≥500k — hold ret_low_3d_open | Value ≥500k | low | 3 | open | 4 | 0.0 | -4.3 | -3.75 | -17.21 | 4.03 | -1.07 | -9.71 | 0.0 |
| 2552 | 21 | 53.67 | Qty ≥5k shares — hold ret_low_5d_news | Qty ≥5k shares | low | 5 | news | 6 | 33.3 | -4.31 | -2.79 | -25.87 | 6.64 | -0.65 | -16.67 | 1.43 |
| 2553 | 20 | 53.67 | Qty ≥10k shares — hold ret_low_5d_news | Qty ≥10k shares | low | 5 | news | 6 | 33.3 | -4.31 | -2.79 | -25.87 | 6.64 | -0.65 | -16.67 | 1.43 |
| 2554 | 21 | 53.67 | Qty ≥5k shares — hold ret_low_5d_open | Qty ≥5k shares | low | 5 | open | 6 | 0.0 | -4.32 | -2.21 | -25.93 | 6.58 | -0.66 | -17.28 | 0.0 |
| 2555 | 20 | 53.67 | Qty ≥10k shares — hold ret_low_5d_open | Qty ≥10k shares | low | 5 | open | 6 | 0.0 | -4.32 | -2.21 | -25.93 | 6.58 | -0.66 | -17.28 | 0.0 |
| 2556 | 22 | 53.36 | RSI overbought (>70) — hold ret_low_60d_open | RSI overbought (>70) | low | 60 | open | 2 | 0.0 | -4.32 | -4.32 | -8.64 | 0.14 | -30.55 | -4.42 | -4.22 |
| 2557 | 40 | 33.74 | Director only + Position +10% — hold ret_mean_30d_news | Director only + Position +10% | mean | 30 | news | 4 | 25.0 | -4.42 | -1.13 | -17.7 | 10.27 | -0.43 | -19.4 | 3.96 |
| 2558 | 31 | 47.75 | Value ≥50k — hold ret_low_7d_news | Value ≥50k | low | 7 | news | 9 | 22.2 | -4.43 | -2.49 | -39.85 | 7.26 | -0.61 | -22.52 | 1.43 |
| 2559 | 37 | 35.58 | Director only + Value ≥100k — hold ret_mean_30d_news | Director only + Value ≥100k | mean | 30 | news | 3 | 66.7 | -4.44 | 2.13 | -13.31 | 12.99 | -0.34 | -19.4 | 3.96 |
| 2560 | 35 | 40.48 | Value ≥500k — hold ret_mean_60d_open | Value ≥500k | mean | 60 | open | 4 | 75.0 | -4.46 | 3.35 | -17.84 | 16.32 | -0.27 | -28.92 | 4.39 |
| 2561 | 35 | 40.48 | Value ≥500k — hold ret_mean_60d_news | Value ≥500k | mean | 60 | news | 4 | 75.0 | -4.46 | 2.67 | -17.83 | 16.07 | -0.28 | -28.39 | 5.21 |
| 2562 | 37 | 35.58 | Director only + Value ≥100k — hold ret_mean_14d_news | Director only + Value ≥100k | mean | 14 | news | 3 | 66.7 | -4.47 | 0.62 | -13.4 | 11.87 | -0.38 | -18.03 | 4.01 |
| 2563 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_low_5d_news | Multiple buys (n≥2) | low | 5 | news | 3 | 0.0 | -4.51 | -5.53 | -13.53 | 2.1 | -2.15 | -5.9 | -2.1 |
| 2564 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_low_7d_news | Multiple buys (n≥2) | low | 7 | news | 3 | 0.0 | -4.51 | -5.53 | -13.53 | 2.1 | -2.15 | -5.9 | -2.1 |
| 2565 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_low_10d_news | Multiple buys (n≥2) | low | 10 | news | 3 | 0.0 | -4.51 | -5.53 | -13.53 | 2.1 | -2.15 | -5.9 | -2.1 |
| 2566 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_low_14d_news | Multiple buys (n≥2) | low | 14 | news | 3 | 0.0 | -4.51 | -5.53 | -13.53 | 2.1 | -2.15 | -5.9 | -2.1 |
| 2567 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_low_30d_news | Multiple buys (n≥2) | low | 30 | news | 3 | 0.0 | -4.51 | -5.53 | -13.53 | 2.1 | -2.15 | -5.9 | -2.1 |
| 2568 | 10 | 66.41 | CEO/CFO — hold ret_low_14d_news | CEO/CFO | low | 14 | news | 4 | 25.0 | -4.55 | -4.0 | -18.19 | 5.58 | -0.81 | -11.62 | 1.43 |
| 2569 | 11 | 66.41 | Officer/President — hold ret_low_14d_news | Officer/President | low | 14 | news | 4 | 25.0 | -4.55 | -4.0 | -18.19 | 5.58 | -0.81 | -11.62 | 1.43 |
| 2570 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_low_14d_news | Large cap (≥250M) CEO/CFO | low | 14 | news | 4 | 25.0 | -4.55 | -4.0 | -18.19 | 5.58 | -0.81 | -11.62 | 1.43 |
| 2571 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_low_14d_news | Large cap (≥500M) CEO/CFO | low | 14 | news | 4 | 25.0 | -4.55 | -4.0 | -18.19 | 5.58 | -0.81 | -11.62 | 1.43 |
| 2572 | 10 | 66.41 | CEO/CFO — hold ret_low_30d_news | CEO/CFO | low | 30 | news | 4 | 25.0 | -4.55 | -4.0 | -18.19 | 5.58 | -0.81 | -11.62 | 1.43 |
| 2573 | 11 | 66.41 | Officer/President — hold ret_low_30d_news | Officer/President | low | 30 | news | 4 | 25.0 | -4.55 | -4.0 | -18.19 | 5.58 | -0.81 | -11.62 | 1.43 |
| 2574 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_low_30d_news | Large cap (≥250M) CEO/CFO | low | 30 | news | 4 | 25.0 | -4.55 | -4.0 | -18.19 | 5.58 | -0.81 | -11.62 | 1.43 |
| 2575 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_low_30d_news | Large cap (≥500M) CEO/CFO | low | 30 | news | 4 | 25.0 | -4.55 | -4.0 | -18.19 | 5.58 | -0.81 | -11.62 | 1.43 |
| 2576 | 38 | 34.53 | Price < MA50 — hold ret_low_3d_news | Price < MA50 | low | 3 | news | 5 | 0.0 | -4.57 | -3.3 | -22.83 | 2.91 | -1.57 | -9.04 | -2.1 |
| 2577 | 30 | 48.32 | Value ≥100k — hold ret_low_5d_open | Value ≥100k | low | 5 | open | 6 | 0.0 | -4.58 | -2.99 | -27.48 | 6.46 | -0.71 | -17.28 | 0.0 |
| 2578 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_low_10d_news | CEO/CFO + Value ≥100k | low | 10 | news | 3 | 33.3 | -4.58 | -5.9 | -13.75 | 5.48 | -0.84 | -9.28 | 1.43 |
| 2579 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_low_10d_news | Large cap (≥750M) CEO/CFO | low | 10 | news | 3 | 33.3 | -4.58 | -5.9 | -13.75 | 5.48 | -0.84 | -9.28 | 1.43 |
| 2580 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_low_10d_news | Large cap (≥1B) CEO/CFO | low | 10 | news | 3 | 33.3 | -4.58 | -5.9 | -13.75 | 5.48 | -0.84 | -9.28 | 1.43 |
| 2581 | 10 | 66.41 | CEO/CFO — hold ret_low_14d_open | CEO/CFO | low | 14 | open | 4 | 0.0 | -4.58 | -2.21 | -18.34 | 6.36 | -0.72 | -13.91 | 0.0 |
| 2582 | 11 | 66.41 | Officer/President — hold ret_low_14d_open | Officer/President | low | 14 | open | 4 | 0.0 | -4.58 | -2.21 | -18.34 | 6.36 | -0.72 | -13.91 | 0.0 |
| 2583 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_low_14d_open | Large cap (≥250M) CEO/CFO | low | 14 | open | 4 | 0.0 | -4.58 | -2.21 | -18.34 | 6.36 | -0.72 | -13.91 | 0.0 |
| 2584 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_low_14d_open | Large cap (≥500M) CEO/CFO | low | 14 | open | 4 | 0.0 | -4.58 | -2.21 | -18.34 | 6.36 | -0.72 | -13.91 | 0.0 |
| 2585 | 10 | 66.41 | CEO/CFO — hold ret_low_30d_open | CEO/CFO | low | 30 | open | 4 | 0.0 | -4.58 | -2.21 | -18.34 | 6.36 | -0.72 | -13.91 | 0.0 |
| 2586 | 11 | 66.41 | Officer/President — hold ret_low_30d_open | Officer/President | low | 30 | open | 4 | 0.0 | -4.58 | -2.21 | -18.34 | 6.36 | -0.72 | -13.91 | 0.0 |
| 2587 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_low_30d_open | Large cap (≥250M) CEO/CFO | low | 30 | open | 4 | 0.0 | -4.58 | -2.21 | -18.34 | 6.36 | -0.72 | -13.91 | 0.0 |
| 2588 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_low_30d_open | Large cap (≥500M) CEO/CFO | low | 30 | open | 4 | 0.0 | -4.58 | -2.21 | -18.34 | 6.36 | -0.72 | -13.91 | 0.0 |
| 2589 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_low_60d_open | Multiple buys (n≥2) | low | 60 | open | 3 | 0.0 | -4.58 | -5.53 | -13.75 | 3.07 | -1.49 | -7.07 | -1.15 |
| 2590 | 37 | 35.58 | Director only + Value ≥100k — hold ret_low_3d_open | Director only + Value ≥100k | low | 3 | open | 3 | 0.0 | -4.64 | -4.22 | -13.93 | 4.87 | -0.95 | -9.71 | 0.0 |
| 2591 | 28 | 48.48 | Tutti — hold ret_low_7d_news | Tutti | low | 7 | news | 10 | 20.0 | -4.64 | -2.98 | -46.42 | 6.88 | -0.68 | -22.52 | 1.43 |
| 2592 | 15 | 62.43 | Price > MA50 — hold ret_low_10d_open | Price > MA50 | low | 10 | open | 5 | 0.0 | -4.66 | -4.22 | -23.29 | 4.7 | -0.99 | -11.63 | 0.0 |
| 2593 | 31 | 47.75 | Value ≥50k — hold ret_low_7d_open | Value ≥50k | low | 7 | open | 9 | 0.0 | -4.69 | -2.7 | -42.24 | 7.14 | -0.66 | -23.09 | 0.0 |
| 2594 | 32 | 44.63 | Position +10% — hold ret_low_5d_news | Position +10% | low | 5 | news | 6 | 33.3 | -4.72 | -4.01 | -28.32 | 6.61 | -0.71 | -16.67 | 1.43 |
| 2595 | 32 | 44.63 | Position +10% — hold ret_low_5d_open | Position +10% | low | 5 | open | 6 | 0.0 | -4.73 | -2.77 | -28.36 | 6.5 | -0.73 | -17.28 | 0.0 |
| 2596 | 40 | 33.74 | Director only + Position +10% — hold ret_mean_30d_open | Director only + Position +10% | mean | 30 | open | 4 | 25.0 | -4.73 | -1.02 | -18.94 | 10.35 | -0.46 | -19.99 | 3.09 |
| 2597 | 30 | 48.32 | Value ≥100k — hold ret_mean_90d_open | Value ≥100k | mean | 90 | open | 6 | 33.3 | -4.73 | -1.72 | -28.37 | 11.51 | -0.41 | -26.66 | 6.78 |
| 2598 | 51 | 20.1 | Position +30% — hold ret_mean_14d_open | Position +30% | mean | 14 | open | 3 | 33.3 | -4.83 | -0.01 | -14.5 | 12.14 | -0.4 | -18.64 | 4.15 |
| 2599 | 26 | 50.0 | Qty ≥50k shares — hold ret_low_3d_open | Qty ≥50k shares | low | 3 | open | 2 | 0.0 | -4.86 | -4.86 | -9.71 | 6.87 | -0.71 | -9.71 | 0.0 |
| 2600 | 27 | 50.0 | Value ≥1M — hold ret_low_3d_open | Value ≥1M | low | 3 | open | 2 | 0.0 | -4.86 | -4.86 | -9.71 | 6.87 | -0.71 | -9.71 | 0.0 |
| 2601 | 28 | 48.48 | Tutti — hold ret_low_7d_open | Tutti | low | 7 | open | 10 | 0.0 | -4.88 | -2.99 | -48.81 | 6.76 | -0.72 | -23.09 | 0.0 |
| 2602 | 30 | 48.32 | Value ≥100k — hold ret_low_7d_news | Value ≥100k | low | 7 | news | 6 | 33.3 | -4.96 | -1.79 | -29.73 | 9.05 | -0.55 | -22.52 | 1.43 |
| 2603 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_low_10d_open | CEO/CFO + Value ≥100k | low | 10 | open | 3 | 0.0 | -4.97 | -3.28 | -14.91 | 6.0 | -0.83 | -11.63 | 0.0 |
| 2604 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_low_10d_open | Large cap (≥750M) CEO/CFO | low | 10 | open | 3 | 0.0 | -4.97 | -3.28 | -14.91 | 6.0 | -0.83 | -11.63 | 0.0 |
| 2605 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_low_10d_open | Large cap (≥1B) CEO/CFO | low | 10 | open | 3 | 0.0 | -4.97 | -3.28 | -14.91 | 6.0 | -0.83 | -11.63 | 0.0 |
| 2606 | 33 | 41.81 | Director — hold ret_low_5d_open | Director | low | 5 | open | 8 | 0.0 | -4.98 | -3.75 | -39.83 | 5.39 | -0.92 | -17.28 | 0.0 |
| 2607 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_low_3d_news | Far 52w high + Value ≥100k | low | 3 | news | 3 | 0.0 | -5.02 | -5.9 | -15.05 | 4.53 | -1.11 | -9.04 | -0.11 |
| 2608 | 6 | 77.62 | CEO only — hold ret_low_14d_open | CEO only | low | 14 | open | 3 | 0.0 | -5.02 | -1.15 | -15.06 | 7.72 | -0.65 | -13.91 | 0.0 |
| 2609 | 6 | 77.62 | CEO only — hold ret_low_30d_open | CEO only | low | 30 | open | 3 | 0.0 | -5.02 | -1.15 | -15.06 | 7.72 | -0.65 | -13.91 | 0.0 |
| 2610 | 51 | 20.1 | Position +30% — hold ret_low_3d_open | Position +30% | low | 3 | open | 3 | 0.0 | -5.09 | -3.28 | -15.26 | 4.04 | -1.26 | -9.71 | -2.27 |
| 2611 | 32 | 44.63 | Position +10% — hold ret_mean_90d_open | Position +10% | mean | 90 | open | 6 | 33.3 | -5.09 | -1.07 | -30.56 | 10.63 | -0.48 | -26.66 | 0.6 |
| 2612 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_low_14d_news | CEO only + Value ≥100k | low | 14 | news | 2 | 50.0 | -5.1 | -5.09 | -10.19 | 9.23 | -0.55 | -11.62 | 1.43 |
| 2613 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_low_14d_news | Price > MA50 + CEO/CFO | low | 14 | news | 2 | 50.0 | -5.1 | -5.09 | -10.19 | 9.23 | -0.55 | -11.62 | 1.43 |
| 2614 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_low_30d_news | CEO only + Value ≥100k | low | 30 | news | 2 | 50.0 | -5.1 | -5.09 | -10.19 | 9.23 | -0.55 | -11.62 | 1.43 |
| 2615 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_low_30d_news | Price > MA50 + CEO/CFO | low | 30 | news | 2 | 50.0 | -5.1 | -5.09 | -10.19 | 9.23 | -0.55 | -11.62 | 1.43 |
| 2616 | 15 | 62.43 | Price > MA50 — hold ret_low_14d_open | Price > MA50 | low | 14 | open | 5 | 0.0 | -5.11 | -4.22 | -25.57 | 5.58 | -0.92 | -13.91 | 0.0 |
| 2617 | 15 | 62.43 | Price > MA50 — hold ret_low_30d_open | Price > MA50 | low | 30 | open | 5 | 0.0 | -5.11 | -4.22 | -25.57 | 5.58 | -0.92 | -13.91 | 0.0 |
| 2618 | 32 | 44.63 | Position +10% — hold ret_mean_90d_news | Position +10% | mean | 90 | news | 6 | 33.3 | -5.13 | -1.31 | -30.76 | 10.32 | -0.5 | -26.12 | 0.07 |
| 2619 | 33 | 41.81 | Director — hold ret_low_5d_news | Director | low | 5 | news | 8 | 12.5 | -5.18 | -4.5 | -41.42 | 5.2 | -1.0 | -16.67 | 0.84 |
| 2620 | 51 | 20.1 | Position +30% — hold ret_mean_30d_open | Position +30% | mean | 30 | open | 3 | 33.3 | -5.18 | -0.87 | -15.55 | 13.19 | -0.39 | -19.99 | 5.31 |
| 2621 | 37 | 35.58 | Director only + Value ≥100k — hold ret_mean_30d_open | Director only + Value ≥100k | mean | 30 | open | 3 | 66.7 | -5.19 | 1.33 | -15.57 | 12.85 | -0.4 | -19.99 | 3.09 |
| 2622 | 37 | 35.58 | Director only + Value ≥100k — hold ret_mean_14d_open | Director only + Value ≥100k | mean | 14 | open | 3 | 33.3 | -5.22 | -0.16 | -15.66 | 11.74 | -0.44 | -18.64 | 3.14 |
| 2623 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_low_3d_open | Far 52w high + Value ≥100k | low | 3 | open | 3 | 0.0 | -5.23 | -3.28 | -15.69 | 3.89 | -1.34 | -9.71 | -2.7 |
| 2624 | 21 | 53.67 | Qty ≥5k shares — hold ret_low_7d_open | Qty ≥5k shares | low | 7 | open | 6 | 0.0 | -5.29 | -2.21 | -31.74 | 8.89 | -0.6 | -23.09 | 0.0 |
| 2625 | 21 | 53.67 | Qty ≥5k shares — hold ret_low_7d_news | Qty ≥5k shares | low | 7 | news | 6 | 33.3 | -5.29 | -2.79 | -31.72 | 8.87 | -0.6 | -22.52 | 1.43 |
| 2626 | 20 | 53.67 | Qty ≥10k shares — hold ret_low_7d_open | Qty ≥10k shares | low | 7 | open | 6 | 0.0 | -5.29 | -2.21 | -31.74 | 8.89 | -0.6 | -23.09 | 0.0 |
| 2627 | 20 | 53.67 | Qty ≥10k shares — hold ret_low_7d_news | Qty ≥10k shares | low | 7 | news | 6 | 33.3 | -5.29 | -2.79 | -31.72 | 8.87 | -0.6 | -22.52 | 1.43 |
| 2628 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_low_14d_news | CEO/CFO + Value ≥100k | low | 14 | news | 3 | 33.3 | -5.36 | -5.9 | -16.09 | 6.54 | -0.82 | -11.62 | 1.43 |
| 2629 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_low_14d_news | Large cap (≥750M) CEO/CFO | low | 14 | news | 3 | 33.3 | -5.36 | -5.9 | -16.09 | 6.54 | -0.82 | -11.62 | 1.43 |
| 2630 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_low_14d_news | Large cap (≥1B) CEO/CFO | low | 14 | news | 3 | 33.3 | -5.36 | -5.9 | -16.09 | 6.54 | -0.82 | -11.62 | 1.43 |
| 2631 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_low_30d_news | CEO/CFO + Value ≥100k | low | 30 | news | 3 | 33.3 | -5.36 | -5.9 | -16.09 | 6.54 | -0.82 | -11.62 | 1.43 |
| 2632 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_low_30d_news | Large cap (≥750M) CEO/CFO | low | 30 | news | 3 | 33.3 | -5.36 | -5.9 | -16.09 | 6.54 | -0.82 | -11.62 | 1.43 |
| 2633 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_low_30d_news | Large cap (≥1B) CEO/CFO | low | 30 | news | 3 | 33.3 | -5.36 | -5.9 | -16.09 | 6.54 | -0.82 | -11.62 | 1.43 |
| 2634 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_mean_14d_news | Far 52w high + Value ≥100k | mean | 14 | news | 3 | 66.7 | -5.4 | 0.5 | -16.21 | 10.94 | -0.49 | -18.03 | 1.32 |
| 2635 | 35 | 40.48 | Value ≥500k — hold ret_mean_90d_open | Value ≥500k | mean | 90 | open | 4 | 50.0 | -5.48 | -1.03 | -21.94 | 14.65 | -0.37 | -26.66 | 6.78 |
| 2636 | 35 | 40.48 | Value ≥500k — hold ret_mean_90d_news | Value ≥500k | mean | 90 | news | 4 | 25.0 | -5.48 | -1.7 | -21.9 | 14.45 | -0.38 | -26.12 | 7.62 |
| 2637 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_mean_14d_open | Far 52w high + Value ≥100k | mean | 14 | open | 3 | 33.3 | -5.53 | -2.1 | -16.59 | 11.78 | -0.47 | -18.64 | 4.15 |
| 2638 | 30 | 48.32 | Value ≥100k — hold ret_low_7d_open | Value ≥100k | low | 7 | open | 6 | 0.0 | -5.55 | -2.99 | -33.29 | 8.77 | -0.63 | -23.09 | 0.0 |
| 2639 | 36 | 36.54 | Director only (no C-level) — hold ret_low_5d_news | Director only (no C-level) | low | 5 | news | 6 | 16.7 | -5.57 | -4.5 | -33.42 | 5.97 | -0.93 | -16.67 | 0.84 |
| 2640 | 51 | 20.1 | Position +30% — hold ret_mean_14d_news | Position +30% | mean | 14 | news | 3 | 33.3 | -5.65 | -0.23 | -16.94 | 10.75 | -0.53 | -18.03 | 1.32 |
| 2641 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_mean_90d_open | Large cap (≥3B) CEO/CFO | mean | 90 | open | 1 | 0.0 | -5.65 | -5.65 | -5.65 | nan | nan | -5.65 | -5.65 |
| 2642 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_mean_90d_open | Large cap (≥5B) CEO/CFO | mean | 90 | open | 1 | 0.0 | -5.65 | -5.65 | -5.65 | nan | nan | -5.65 | -5.65 |
| 2643 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_mean_90d_open | Large cap (≥10B) CEO/CFO | mean | 90 | open | 1 | 0.0 | -5.65 | -5.65 | -5.65 | nan | nan | -5.65 | -5.65 |
| 2644 | 53 | 0.0 | Qty ≥100k shares — hold ret_mean_7d_news | Qty ≥100k shares | mean | 7 | news | 1 | 0.0 | -5.66 | -5.66 | -5.66 | nan | nan | -5.66 | -5.66 |
| 2645 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_mean_7d_news | Small cap (≤1B) Value ≥100k | mean | 7 | news | 1 | 0.0 | -5.66 | -5.66 | -5.66 | nan | nan | -5.66 | -5.66 |
| 2646 | 32 | 44.63 | Position +10% — hold ret_low_7d_open | Position +10% | low | 7 | open | 6 | 0.0 | -5.7 | -2.77 | -34.17 | 8.78 | -0.65 | -23.09 | 0.0 |
| 2647 | 32 | 44.63 | Position +10% — hold ret_low_7d_news | Position +10% | low | 7 | news | 6 | 33.3 | -5.7 | -4.01 | -34.17 | 8.8 | -0.65 | -22.52 | 1.43 |
| 2648 | 39 | 34.48 | Position +20% — hold ret_low_5d_open | Position +20% | low | 5 | open | 4 | 0.0 | -5.71 | -2.77 | -22.83 | 7.84 | -0.73 | -17.28 | 0.0 |
| 2649 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_low_14d_open | CEO/CFO + Value ≥100k | low | 14 | open | 3 | 0.0 | -5.73 | -3.28 | -17.19 | 7.27 | -0.79 | -13.91 | 0.0 |
| 2650 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_low_14d_open | Large cap (≥750M) CEO/CFO | low | 14 | open | 3 | 0.0 | -5.73 | -3.28 | -17.19 | 7.27 | -0.79 | -13.91 | 0.0 |
| 2651 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_low_14d_open | Large cap (≥1B) CEO/CFO | low | 14 | open | 3 | 0.0 | -5.73 | -3.28 | -17.19 | 7.27 | -0.79 | -13.91 | 0.0 |
| 2652 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_low_30d_open | CEO/CFO + Value ≥100k | low | 30 | open | 3 | 0.0 | -5.73 | -3.28 | -17.19 | 7.27 | -0.79 | -13.91 | 0.0 |
| 2653 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_low_30d_open | Large cap (≥750M) CEO/CFO | low | 30 | open | 3 | 0.0 | -5.73 | -3.28 | -17.19 | 7.27 | -0.79 | -13.91 | 0.0 |
| 2654 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_low_30d_open | Large cap (≥1B) CEO/CFO | low | 30 | open | 3 | 0.0 | -5.73 | -3.28 | -17.19 | 7.27 | -0.79 | -13.91 | 0.0 |
| 2655 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_low_60d_news | Multiple buys (n≥2) | low | 60 | news | 3 | 0.0 | -5.74 | -5.53 | -17.22 | 3.75 | -1.53 | -9.59 | -2.1 |
| 2656 | 33 | 41.81 | Director — hold ret_low_7d_open | Director | low | 7 | open | 8 | 0.0 | -5.76 | -3.75 | -46.11 | 7.33 | -0.79 | -23.09 | 0.0 |
| 2657 | 51 | 20.1 | Position +30% — hold ret_low_3d_news | Position +30% | low | 3 | news | 3 | 0.0 | -5.81 | -5.9 | -17.43 | 3.28 | -1.77 | -9.04 | -2.49 |
| 2658 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_low_10d_open | CEO only + Value ≥100k | low | 10 | open | 2 | 0.0 | -5.82 | -5.82 | -11.63 | 8.22 | -0.71 | -11.63 | 0.0 |
| 2659 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_low_10d_open | Price > MA50 + CEO/CFO | low | 10 | open | 2 | 0.0 | -5.82 | -5.82 | -11.63 | 8.22 | -0.71 | -11.63 | 0.0 |
| 2660 | 39 | 34.48 | Position +20% — hold ret_mean_60d_open | Position +20% | mean | 60 | open | 4 | 75.0 | -5.85 | 0.91 | -23.4 | 15.44 | -0.38 | -28.92 | 3.7 |
| 2661 | 49 | 32.78 | CFO only — hold ret_low_1d_news | CFO only | low | 1 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2662 | 48 | 32.78 | CFO + Director (combo) — hold ret_low_1d_news | CFO + Director (combo) | low | 1 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2663 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_low_1d_news | CFO only + Value ≥50k | low | 1 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2664 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_low_1d_news | CFO only + Value ≥100k | low | 1 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2665 | 47 | 32.78 | CFO only + Position +10% — hold ret_low_1d_news | CFO only + Position +10% | low | 1 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2666 | 46 | 32.78 | CFO only + Position +20% — hold ret_low_1d_news | CFO only + Position +20% | low | 1 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2667 | 44 | 32.78 | RSI oversold (<30) — hold ret_low_1d_news | RSI oversold (<30) | low | 1 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2668 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_low_1d_news | RSI oversold + CEO/CFO | low | 1 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2669 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_low_1d_news | RSI oversold + Value ≥100k | low | 1 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2670 | 49 | 32.78 | CFO only — hold ret_low_2d_news | CFO only | low | 2 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2671 | 48 | 32.78 | CFO + Director (combo) — hold ret_low_2d_news | CFO + Director (combo) | low | 2 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2672 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_low_2d_news | CFO only + Value ≥50k | low | 2 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2673 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_low_2d_news | CFO only + Value ≥100k | low | 2 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2674 | 47 | 32.78 | CFO only + Position +10% — hold ret_low_2d_news | CFO only + Position +10% | low | 2 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2675 | 46 | 32.78 | CFO only + Position +20% — hold ret_low_2d_news | CFO only + Position +20% | low | 2 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2676 | 44 | 32.78 | RSI oversold (<30) — hold ret_low_2d_news | RSI oversold (<30) | low | 2 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2677 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_low_2d_news | RSI oversold + CEO/CFO | low | 2 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2678 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_low_2d_news | RSI oversold + Value ≥100k | low | 2 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2679 | 49 | 32.78 | CFO only — hold ret_low_3d_news | CFO only | low | 3 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2680 | 48 | 32.78 | CFO + Director (combo) — hold ret_low_3d_news | CFO + Director (combo) | low | 3 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2681 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_low_3d_news | CFO only + Value ≥50k | low | 3 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2682 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_low_3d_news | CFO only + Value ≥100k | low | 3 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2683 | 47 | 32.78 | CFO only + Position +10% — hold ret_low_3d_news | CFO only + Position +10% | low | 3 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2684 | 46 | 32.78 | CFO only + Position +20% — hold ret_low_3d_news | CFO only + Position +20% | low | 3 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2685 | 44 | 32.78 | RSI oversold (<30) — hold ret_low_3d_news | RSI oversold (<30) | low | 3 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2686 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_low_3d_news | RSI oversold + CEO/CFO | low | 3 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2687 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_low_3d_news | RSI oversold + Value ≥100k | low | 3 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2688 | 49 | 32.78 | CFO only — hold ret_low_5d_news | CFO only | low | 5 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2689 | 36 | 36.54 | Director only (no C-level) — hold ret_low_5d_open | Director only (no C-level) | low | 5 | open | 6 | 0.0 | -5.9 | -4.88 | -35.4 | 6.01 | -0.98 | -17.28 | 0.0 |
| 2690 | 48 | 32.78 | CFO + Director (combo) — hold ret_low_5d_news | CFO + Director (combo) | low | 5 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2691 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_low_5d_news | CFO only + Value ≥50k | low | 5 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2692 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_low_5d_news | CFO only + Value ≥100k | low | 5 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2693 | 47 | 32.78 | CFO only + Position +10% — hold ret_low_5d_news | CFO only + Position +10% | low | 5 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2694 | 46 | 32.78 | CFO only + Position +20% — hold ret_low_5d_news | CFO only + Position +20% | low | 5 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2695 | 44 | 32.78 | RSI oversold (<30) — hold ret_low_5d_news | RSI oversold (<30) | low | 5 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2696 | 38 | 34.53 | Price < MA50 — hold ret_low_5d_open | Price < MA50 | low | 5 | open | 5 | 0.0 | -5.9 | -3.28 | -29.51 | 6.56 | -0.9 | -17.28 | -1.15 |
| 2697 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_low_5d_news | RSI oversold + CEO/CFO | low | 5 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2698 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_low_5d_news | RSI oversold + Value ≥100k | low | 5 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2699 | 49 | 32.78 | CFO only — hold ret_low_7d_news | CFO only | low | 7 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2700 | 48 | 32.78 | CFO + Director (combo) — hold ret_low_7d_news | CFO + Director (combo) | low | 7 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2701 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_low_7d_news | CFO only + Value ≥50k | low | 7 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2702 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_low_7d_news | CFO only + Value ≥100k | low | 7 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2703 | 47 | 32.78 | CFO only + Position +10% — hold ret_low_7d_news | CFO only + Position +10% | low | 7 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2704 | 46 | 32.78 | CFO only + Position +20% — hold ret_low_7d_news | CFO only + Position +20% | low | 7 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2705 | 44 | 32.78 | RSI oversold (<30) — hold ret_low_7d_news | RSI oversold (<30) | low | 7 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2706 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_low_7d_news | RSI oversold + CEO/CFO | low | 7 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2707 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_low_7d_news | RSI oversold + Value ≥100k | low | 7 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2708 | 49 | 32.78 | CFO only — hold ret_low_10d_news | CFO only | low | 10 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2709 | 48 | 32.78 | CFO + Director (combo) — hold ret_low_10d_news | CFO + Director (combo) | low | 10 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2710 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_low_10d_news | CFO only + Value ≥50k | low | 10 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2711 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_low_10d_news | CFO only + Value ≥100k | low | 10 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2712 | 47 | 32.78 | CFO only + Position +10% — hold ret_low_10d_news | CFO only + Position +10% | low | 10 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2713 | 46 | 32.78 | CFO only + Position +20% — hold ret_low_10d_news | CFO only + Position +20% | low | 10 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2714 | 44 | 32.78 | RSI oversold (<30) — hold ret_low_10d_news | RSI oversold (<30) | low | 10 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2715 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_low_10d_news | RSI oversold + CEO/CFO | low | 10 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2716 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_low_10d_news | RSI oversold + Value ≥100k | low | 10 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2717 | 49 | 32.78 | CFO only — hold ret_low_14d_news | CFO only | low | 14 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2718 | 48 | 32.78 | CFO + Director (combo) — hold ret_low_14d_news | CFO + Director (combo) | low | 14 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2719 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_low_14d_news | CFO only + Value ≥50k | low | 14 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2720 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_low_14d_news | CFO only + Value ≥100k | low | 14 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2721 | 47 | 32.78 | CFO only + Position +10% — hold ret_low_14d_news | CFO only + Position +10% | low | 14 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2722 | 46 | 32.78 | CFO only + Position +20% — hold ret_low_14d_news | CFO only + Position +20% | low | 14 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2723 | 44 | 32.78 | RSI oversold (<30) — hold ret_low_14d_news | RSI oversold (<30) | low | 14 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2724 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_low_14d_news | RSI oversold + CEO/CFO | low | 14 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2725 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_low_14d_news | RSI oversold + Value ≥100k | low | 14 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2726 | 49 | 32.78 | CFO only — hold ret_low_30d_news | CFO only | low | 30 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2727 | 48 | 32.78 | CFO + Director (combo) — hold ret_low_30d_news | CFO + Director (combo) | low | 30 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2728 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_low_30d_news | CFO only + Value ≥50k | low | 30 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2729 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_low_30d_news | CFO only + Value ≥100k | low | 30 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2730 | 47 | 32.78 | CFO only + Position +10% — hold ret_low_30d_news | CFO only + Position +10% | low | 30 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2731 | 46 | 32.78 | CFO only + Position +20% — hold ret_low_30d_news | CFO only + Position +20% | low | 30 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2732 | 44 | 32.78 | RSI oversold (<30) — hold ret_low_30d_news | RSI oversold (<30) | low | 30 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2733 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_low_30d_news | RSI oversold + CEO/CFO | low | 30 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2734 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_low_30d_news | RSI oversold + Value ≥100k | low | 30 | news | 1 | 0.0 | -5.9 | -5.9 | -5.9 | nan | nan | -5.9 | -5.9 |
| 2735 | 40 | 33.74 | Director only + Position +10% — hold ret_low_5d_news | Director only + Position +10% | low | 5 | news | 4 | 25.0 | -5.96 | -4.01 | -23.85 | 7.6 | -0.78 | -16.67 | 0.84 |
| 2736 | 33 | 41.81 | Director — hold ret_low_7d_news | Director | low | 7 | news | 8 | 12.5 | -5.97 | -4.5 | -47.74 | 7.11 | -0.84 | -22.52 | 0.84 |
| 2737 | 51 | 20.1 | Position +30% — hold ret_mean_30d_news | Position +30% | mean | 30 | news | 3 | 33.3 | -6.01 | -1.09 | -18.04 | 11.73 | -0.51 | -19.4 | 2.45 |
| 2738 | 39 | 34.48 | Position +20% — hold ret_low_5d_news | Position +20% | low | 5 | news | 4 | 25.0 | -6.06 | -4.2 | -24.22 | 7.59 | -0.8 | -16.67 | 0.84 |
| 2739 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_mean_30d_news | Far 52w high + Value ≥100k | mean | 30 | news | 3 | 33.3 | -6.11 | -1.39 | -18.34 | 11.67 | -0.52 | -19.4 | 2.45 |
| 2740 | 35 | 40.48 | Value ≥500k — hold ret_low_5d_news | Value ≥500k | low | 5 | news | 4 | 25.0 | -6.15 | -4.69 | -24.61 | 7.65 | -0.8 | -16.67 | 1.43 |
| 2741 | 37 | 35.58 | Director only + Value ≥100k — hold ret_mean_90d_news | Director only + Value ≥100k | mean | 90 | news | 3 | 66.7 | -6.15 | 0.05 | -18.45 | 17.7 | -0.35 | -26.12 | 7.62 |
| 2742 | 35 | 40.48 | Value ≥500k — hold ret_low_5d_open | Value ≥500k | low | 5 | open | 4 | 0.0 | -6.2 | -3.75 | -24.78 | 7.61 | -0.81 | -17.28 | 0.0 |
| 2743 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_mean_30d_open | Far 52w high + Value ≥100k | mean | 30 | open | 3 | 33.3 | -6.21 | -3.95 | -18.63 | 12.8 | -0.49 | -19.99 | 5.31 |
| 2744 | 39 | 34.48 | Position +20% — hold ret_mean_60d_news | Position +20% | mean | 60 | news | 4 | 75.0 | -6.26 | 0.55 | -25.05 | 14.78 | -0.42 | -28.39 | 2.24 |
| 2745 | 40 | 33.74 | Director only + Position +10% — hold ret_low_5d_open | Director only + Position +10% | low | 5 | open | 4 | 0.0 | -6.27 | -3.9 | -25.08 | 7.68 | -0.82 | -17.28 | 0.0 |
| 2746 | 53 | 0.0 | Qty ≥100k shares — hold ret_mean_7d_open | Qty ≥100k shares | mean | 7 | open | 1 | 0.0 | -6.35 | -6.35 | -6.35 | nan | nan | -6.35 | -6.35 |
| 2747 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_mean_7d_open | Small cap (≤1B) Value ≥100k | mean | 7 | open | 1 | 0.0 | -6.35 | -6.35 | -6.35 | nan | nan | -6.35 | -6.35 |
| 2748 | 37 | 35.58 | Director only + Value ≥100k — hold ret_low_5d_news | Director only + Value ≥100k | low | 5 | news | 3 | 33.3 | -6.43 | -3.47 | -19.3 | 9.12 | -0.71 | -16.67 | 0.84 |
| 2749 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_mean_60d_open | Large cap (≥3B) CEO/CFO | mean | 60 | open | 1 | 0.0 | -6.46 | -6.46 | -6.46 | nan | nan | -6.46 | -6.46 |
| 2750 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_mean_60d_open | Large cap (≥5B) CEO/CFO | mean | 60 | open | 1 | 0.0 | -6.46 | -6.46 | -6.46 | nan | nan | -6.46 | -6.46 |
| 2751 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_mean_60d_open | Large cap (≥10B) CEO/CFO | mean | 60 | open | 1 | 0.0 | -6.46 | -6.46 | -6.46 | nan | nan | -6.46 | -6.46 |
| 2752 | 38 | 34.53 | Price < MA50 — hold ret_low_5d_news | Price < MA50 | low | 5 | news | 5 | 0.0 | -6.54 | -5.53 | -32.69 | 5.92 | -1.1 | -16.67 | -2.1 |
| 2753 | 22 | 53.36 | RSI overbought (>70) — hold ret_low_90d_news | RSI overbought (>70) | low | 90 | news | 2 | 0.0 | -6.57 | -6.57 | -13.14 | 4.38 | -1.5 | -9.67 | -3.47 |
| 2754 | 36 | 36.54 | Director only (no C-level) — hold ret_low_7d_news | Director only (no C-level) | low | 7 | news | 6 | 16.7 | -6.62 | -4.5 | -39.74 | 8.21 | -0.81 | -22.52 | 0.84 |
| 2755 | 39 | 34.48 | Position +20% — hold ret_mean_90d_open | Position +20% | mean | 90 | open | 4 | 50.0 | -6.64 | -0.24 | -26.54 | 13.36 | -0.5 | -26.66 | 0.6 |
| 2756 | 40 | 33.74 | Director only + Position +10% — hold ret_mean_60d_news | Director only + Position +10% | mean | 60 | news | 4 | 50.0 | -6.74 | -0.4 | -26.95 | 14.5 | -0.46 | -28.39 | 2.24 |
| 2757 | 40 | 33.74 | Director only + Position +10% — hold ret_mean_90d_news | Director only + Position +10% | mean | 90 | news | 4 | 50.0 | -6.84 | -0.66 | -27.36 | 12.87 | -0.53 | -26.12 | 0.07 |
| 2758 | 37 | 35.58 | Director only + Value ≥100k — hold ret_mean_90d_open | Director only + Value ≥100k | mean | 90 | open | 3 | 33.3 | -6.89 | -0.78 | -20.66 | 17.54 | -0.39 | -26.66 | 6.78 |
| 2759 | 36 | 36.54 | Director only (no C-level) — hold ret_low_7d_open | Director only (no C-level) | low | 7 | open | 6 | 0.0 | -6.95 | -4.88 | -41.68 | 8.25 | -0.84 | -23.09 | 0.0 |
| 2760 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_low_14d_open | CEO only + Value ≥100k | low | 14 | open | 2 | 0.0 | -6.96 | -6.96 | -13.91 | 9.84 | -0.71 | -13.91 | 0.0 |
| 2761 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_low_14d_open | Price > MA50 + CEO/CFO | low | 14 | open | 2 | 0.0 | -6.96 | -6.96 | -13.91 | 9.84 | -0.71 | -13.91 | 0.0 |
| 2762 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_low_30d_open | CEO only + Value ≥100k | low | 30 | open | 2 | 0.0 | -6.96 | -6.96 | -13.91 | 9.84 | -0.71 | -13.91 | 0.0 |
| 2763 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_low_30d_open | Price > MA50 + CEO/CFO | low | 30 | open | 2 | 0.0 | -6.96 | -6.96 | -13.91 | 9.84 | -0.71 | -13.91 | 0.0 |
| 2764 | 37 | 35.58 | Director only + Value ≥100k — hold ret_mean_60d_news | Director only + Value ≥100k | mean | 60 | news | 3 | 66.7 | -6.98 | 2.24 | -20.94 | 18.6 | -0.38 | -28.39 | 5.21 |
| 2765 | 40 | 33.74 | Director only + Position +10% — hold ret_mean_60d_open | Director only + Position +10% | mean | 60 | open | 4 | 50.0 | -7.03 | -0.29 | -28.11 | 14.63 | -0.48 | -28.92 | 1.39 |
| 2766 | 39 | 34.48 | Position +20% — hold ret_mean_90d_news | Position +20% | mean | 90 | news | 4 | 50.0 | -7.03 | -1.04 | -28.13 | 12.77 | -0.55 | -26.12 | 0.07 |
| 2767 | 38 | 34.53 | Price < MA50 — hold ret_low_7d_open | Price < MA50 | low | 7 | open | 5 | 0.0 | -7.06 | -3.28 | -35.32 | 9.1 | -0.78 | -23.09 | -1.15 |
| 2768 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_low_90d_open | Multiple buys (n≥2) | low | 90 | open | 3 | 0.0 | -7.06 | -5.53 | -21.18 | 6.81 | -1.04 | -14.5 | -1.15 |
| 2769 | 49 | 32.78 | CFO only — hold ret_low_60d_open | CFO only | low | 60 | open | 1 | 0.0 | -7.07 | -7.07 | -7.07 | nan | nan | -7.07 | -7.07 |
| 2770 | 48 | 32.78 | CFO + Director (combo) — hold ret_low_60d_open | CFO + Director (combo) | low | 60 | open | 1 | 0.0 | -7.07 | -7.07 | -7.07 | nan | nan | -7.07 | -7.07 |
| 2771 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_low_60d_open | CFO only + Value ≥50k | low | 60 | open | 1 | 0.0 | -7.07 | -7.07 | -7.07 | nan | nan | -7.07 | -7.07 |
| 2772 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_low_60d_open | CFO only + Value ≥100k | low | 60 | open | 1 | 0.0 | -7.07 | -7.07 | -7.07 | nan | nan | -7.07 | -7.07 |
| 2773 | 47 | 32.78 | CFO only + Position +10% — hold ret_low_60d_open | CFO only + Position +10% | low | 60 | open | 1 | 0.0 | -7.07 | -7.07 | -7.07 | nan | nan | -7.07 | -7.07 |
| 2774 | 46 | 32.78 | CFO only + Position +20% — hold ret_low_60d_open | CFO only + Position +20% | low | 60 | open | 1 | 0.0 | -7.07 | -7.07 | -7.07 | nan | nan | -7.07 | -7.07 |
| 2775 | 44 | 32.78 | RSI oversold (<30) — hold ret_low_60d_open | RSI oversold (<30) | low | 60 | open | 1 | 0.0 | -7.07 | -7.07 | -7.07 | nan | nan | -7.07 | -7.07 |
| 2776 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_low_60d_open | RSI oversold + CEO/CFO | low | 60 | open | 1 | 0.0 | -7.07 | -7.07 | -7.07 | nan | nan | -7.07 | -7.07 |
| 2777 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_low_60d_open | RSI oversold + Value ≥100k | low | 60 | open | 1 | 0.0 | -7.07 | -7.07 | -7.07 | nan | nan | -7.07 | -7.07 |
| 2778 | 40 | 33.74 | Director only + Position +10% — hold ret_mean_90d_open | Director only + Position +10% | mean | 90 | open | 4 | 25.0 | -7.12 | -1.07 | -28.5 | 13.04 | -0.55 | -26.66 | 0.3 |
| 2779 | 39 | 34.48 | Position +20% — hold ret_low_7d_open | Position +20% | low | 7 | open | 4 | 0.0 | -7.16 | -2.77 | -28.64 | 10.71 | -0.67 | -23.09 | 0.0 |
| 2780 | 37 | 35.58 | Director only + Value ≥100k — hold ret_low_5d_open | Director only + Value ≥100k | low | 5 | open | 3 | 0.0 | -7.17 | -4.22 | -21.5 | 9.01 | -0.8 | -17.28 | 0.0 |
| 2781 | 14 | 65.45 | Price > MA200 — hold ret_low_60d_news | Price > MA200 | low | 60 | news | 4 | 0.0 | -7.23 | -5.09 | -28.92 | 5.55 | -1.3 | -15.27 | -3.47 |
| 2782 | 22 | 53.36 | RSI overbought (>70) — hold ret_low_90d_open | RSI overbought (>70) | low | 90 | open | 2 | 0.0 | -7.32 | -7.32 | -14.64 | 4.38 | -1.67 | -10.42 | -4.22 |
| 2783 | 40 | 33.74 | Director only + Position +10% — hold ret_low_7d_news | Director only + Position +10% | low | 7 | news | 4 | 25.0 | -7.42 | -4.01 | -29.7 | 10.39 | -0.71 | -22.52 | 0.84 |
| 2784 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_low_10d_open | Large cap (≥2B) CEO/CFO | low | 10 | open | 2 | 0.0 | -7.46 | -7.46 | -14.91 | 5.9 | -1.26 | -11.63 | -3.28 |
| 2785 | 39 | 34.48 | Position +20% — hold ret_low_7d_news | Position +20% | low | 7 | news | 4 | 25.0 | -7.52 | -4.2 | -30.07 | 10.37 | -0.72 | -22.52 | 0.84 |
| 2786 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_low_5d_news | Far 52w high + Value ≥100k | low | 5 | news | 3 | 0.0 | -7.56 | -5.9 | -22.68 | 8.4 | -0.9 | -16.67 | -0.11 |
| 2787 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_low_10d_news | Large cap (≥2B) CEO/CFO | low | 10 | news | 2 | 0.0 | -7.59 | -7.59 | -15.18 | 2.39 | -3.18 | -9.28 | -5.9 |
| 2788 | 51 | 20.1 | Position +30% — hold ret_low_5d_open | Position +30% | low | 5 | open | 3 | 0.0 | -7.61 | -3.28 | -22.83 | 8.39 | -0.91 | -17.28 | -2.27 |
| 2789 | 26 | 50.0 | Qty ≥50k shares — hold ret_low_5d_news | Qty ≥50k shares | low | 5 | news | 2 | 50.0 | -7.62 | -7.62 | -15.24 | 12.8 | -0.6 | -16.67 | 1.43 |
| 2790 | 27 | 50.0 | Value ≥1M — hold ret_low_5d_news | Value ≥1M | low | 5 | news | 2 | 50.0 | -7.62 | -7.62 | -15.24 | 12.8 | -0.6 | -16.67 | 1.43 |
| 2791 | 35 | 40.48 | Value ≥500k — hold ret_low_7d_news | Value ≥500k | low | 7 | news | 4 | 25.0 | -7.62 | -4.69 | -30.46 | 10.39 | -0.73 | -22.52 | 1.43 |
| 2792 | 35 | 40.48 | Value ≥500k — hold ret_low_7d_open | Value ≥500k | low | 7 | open | 4 | 0.0 | -7.65 | -3.75 | -30.59 | 10.45 | -0.73 | -23.09 | 0.0 |
| 2793 | 38 | 34.53 | Price < MA50 — hold ret_low_7d_news | Price < MA50 | low | 7 | news | 5 | 0.0 | -7.71 | -5.53 | -38.54 | 8.46 | -0.91 | -22.52 | -2.1 |
| 2794 | 37 | 35.58 | Director only + Value ≥100k — hold ret_mean_60d_open | Director only + Value ≥100k | mean | 60 | open | 3 | 66.7 | -7.71 | 1.39 | -23.14 | 18.43 | -0.42 | -28.92 | 4.39 |
| 2795 | 40 | 33.74 | Director only + Position +10% — hold ret_low_7d_open | Director only + Position +10% | low | 7 | open | 4 | 0.0 | -7.72 | -3.9 | -30.89 | 10.49 | -0.74 | -23.09 | 0.0 |
| 2796 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_low_5d_open | Far 52w high + Value ≥100k | low | 5 | open | 3 | 0.0 | -7.75 | -3.28 | -23.26 | 8.26 | -0.94 | -17.28 | -2.7 |
| 2797 | 28 | 48.48 | Tutti — hold ret_low_10d_news | Tutti | low | 10 | news | 10 | 10.0 | -7.76 | -4.5 | -77.65 | 13.02 | -0.6 | -43.7 | 1.43 |
| 2798 | 31 | 47.75 | Value ≥50k — hold ret_low_10d_news | Value ≥50k | low | 10 | news | 9 | 11.1 | -7.9 | -3.47 | -71.08 | 13.8 | -0.57 | -43.7 | 1.43 |
| 2799 | 14 | 65.45 | Price > MA200 — hold ret_low_60d_open | Price > MA200 | low | 60 | open | 4 | 0.0 | -7.92 | -5.5 | -31.67 | 5.79 | -1.37 | -16.46 | -4.22 |
| 2800 | 28 | 48.48 | Tutti — hold ret_low_10d_open | Tutti | low | 10 | open | 10 | 0.0 | -7.96 | -3.75 | -79.64 | 13.15 | -0.61 | -44.12 | 0.0 |
| 2801 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_low_60d_news | Mid cap (1B–10B) Value ≥100k | low | 60 | news | 4 | 0.0 | -7.98 | -6.6 | -31.94 | 5.63 | -1.42 | -15.27 | -3.47 |
| 2802 | 28 | 48.48 | Tutti — hold ret_low_14d_news | Tutti | low | 14 | news | 10 | 10.0 | -8.01 | -4.5 | -80.06 | 13.07 | -0.61 | -43.7 | 1.43 |
| 2803 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_low_60d_open | Mid cap (1B–10B) Value ≥100k | low | 60 | open | 4 | 0.0 | -8.04 | -5.75 | -32.17 | 5.76 | -1.4 | -16.46 | -4.22 |
| 2804 | 31 | 47.75 | Value ≥50k — hold ret_low_10d_open | Value ≥50k | low | 10 | open | 9 | 0.0 | -8.12 | -3.28 | -73.07 | 13.94 | -0.58 | -44.12 | 0.0 |
| 2805 | 29 | 48.39 | Multiple buys (n≥2) — hold ret_low_90d_news | Multiple buys (n≥2) | low | 90 | news | 3 | 0.0 | -8.15 | -5.53 | -24.45 | 7.7 | -1.06 | -16.82 | -2.1 |
| 2806 | 31 | 47.75 | Value ≥50k — hold ret_low_14d_news | Value ≥50k | low | 14 | news | 9 | 11.1 | -8.17 | -3.47 | -73.49 | 13.85 | -0.59 | -43.7 | 1.43 |
| 2807 | 28 | 48.48 | Tutti — hold ret_low_14d_open | Tutti | low | 14 | open | 10 | 0.0 | -8.2 | -3.75 | -81.99 | 13.24 | -0.62 | -44.12 | 0.0 |
| 2808 | 51 | 20.1 | Position +30% — hold ret_mean_60d_open | Position +30% | mean | 60 | open | 3 | 66.7 | -8.26 | 0.43 | -24.79 | 17.96 | -0.46 | -28.92 | 3.7 |
| 2809 | 28 | 48.48 | Tutti — hold ret_low_30d_news | Tutti | low | 30 | news | 10 | 10.0 | -8.3 | -5.5 | -82.96 | 12.97 | -0.64 | -43.7 | 1.43 |
| 2810 | 51 | 20.1 | Position +30% — hold ret_low_5d_news | Position +30% | low | 5 | news | 3 | 0.0 | -8.35 | -5.9 | -25.06 | 7.4 | -1.13 | -16.67 | -2.49 |
| 2811 | 37 | 35.58 | Director only + Value ≥100k — hold ret_low_7d_news | Director only + Value ≥100k | low | 7 | news | 3 | 33.3 | -8.38 | -3.47 | -25.15 | 12.43 | -0.67 | -22.52 | 0.84 |
| 2812 | 31 | 47.75 | Value ≥50k — hold ret_low_14d_open | Value ≥50k | low | 14 | open | 9 | 0.0 | -8.38 | -3.28 | -75.42 | 14.03 | -0.6 | -44.12 | 0.0 |
| 2813 | 28 | 48.48 | Tutti — hold ret_low_30d_open | Tutti | low | 30 | open | 10 | 0.0 | -8.49 | -4.73 | -84.9 | 13.13 | -0.65 | -44.12 | 0.0 |
| 2814 | 31 | 47.75 | Value ≥50k — hold ret_low_30d_news | Value ≥50k | low | 30 | news | 9 | 11.1 | -8.49 | -5.46 | -76.39 | 13.74 | -0.62 | -43.7 | 1.43 |
| 2815 | 33 | 41.81 | Director — hold ret_low_10d_open | Director | low | 10 | open | 8 | 0.0 | -8.5 | -3.75 | -68.01 | 14.53 | -0.59 | -44.12 | -0.87 |
| 2816 | 33 | 41.81 | Director — hold ret_low_14d_open | Director | low | 14 | open | 8 | 0.0 | -8.51 | -3.75 | -68.08 | 14.53 | -0.59 | -44.12 | -0.87 |
| 2817 | 51 | 20.1 | Position +30% — hold ret_mean_90d_open | Position +30% | mean | 90 | open | 3 | 66.7 | -8.59 | 0.3 | -25.76 | 15.65 | -0.55 | -26.66 | 0.6 |
| 2818 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_low_14d_open | Large cap (≥2B) CEO/CFO | low | 14 | open | 2 | 0.0 | -8.6 | -8.6 | -17.19 | 7.52 | -1.14 | -13.91 | -3.28 |
| 2819 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_low_30d_open | Large cap (≥2B) CEO/CFO | low | 30 | open | 2 | 0.0 | -8.6 | -8.6 | -17.19 | 7.52 | -1.14 | -13.91 | -3.28 |
| 2820 | 26 | 50.0 | Qty ≥50k shares — hold ret_low_5d_open | Qty ≥50k shares | low | 5 | open | 2 | 0.0 | -8.64 | -8.64 | -17.28 | 12.22 | -0.71 | -17.28 | 0.0 |
| 2821 | 27 | 50.0 | Value ≥1M — hold ret_low_5d_open | Value ≥1M | low | 5 | open | 2 | 0.0 | -8.64 | -8.64 | -17.28 | 12.22 | -0.71 | -17.28 | 0.0 |
| 2822 | 31 | 47.75 | Value ≥50k — hold ret_low_30d_open | Value ≥50k | low | 30 | open | 9 | 0.0 | -8.7 | -4.22 | -78.33 | 13.91 | -0.63 | -44.12 | 0.0 |
| 2823 | 33 | 41.81 | Director — hold ret_low_10d_news | Director | low | 10 | news | 8 | 0.0 | -8.73 | -4.5 | -69.8 | 14.3 | -0.61 | -43.7 | -0.04 |
| 2824 | 33 | 41.81 | Director — hold ret_low_14d_news | Director | low | 14 | news | 8 | 0.0 | -8.73 | -4.5 | -69.87 | 14.3 | -0.61 | -43.7 | -0.04 |
| 2825 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_low_14d_news | Large cap (≥2B) CEO/CFO | low | 14 | news | 2 | 0.0 | -8.76 | -8.76 | -17.52 | 4.04 | -2.17 | -11.62 | -5.9 |
| 2826 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_low_30d_news | Large cap (≥2B) CEO/CFO | low | 30 | news | 2 | 0.0 | -8.76 | -8.76 | -17.52 | 4.04 | -2.17 | -11.62 | -5.9 |
| 2827 | 33 | 41.81 | Director — hold ret_low_30d_open | Director | low | 30 | open | 8 | 0.0 | -8.87 | -4.73 | -70.99 | 14.39 | -0.62 | -44.12 | -0.87 |
| 2828 | 21 | 53.67 | Qty ≥5k shares — hold ret_low_10d_open | Qty ≥5k shares | low | 10 | open | 6 | 0.0 | -8.94 | -2.21 | -53.64 | 17.31 | -0.52 | -44.12 | 0.0 |
| 2829 | 20 | 53.67 | Qty ≥10k shares — hold ret_low_10d_open | Qty ≥10k shares | low | 10 | open | 6 | 0.0 | -8.94 | -2.21 | -53.64 | 17.31 | -0.52 | -44.12 | 0.0 |
| 2830 | 21 | 53.67 | Qty ≥5k shares — hold ret_low_14d_open | Qty ≥5k shares | low | 14 | open | 6 | 0.0 | -8.94 | -2.21 | -53.64 | 17.31 | -0.52 | -44.12 | 0.0 |
| 2831 | 20 | 53.67 | Qty ≥10k shares — hold ret_low_14d_open | Qty ≥10k shares | low | 14 | open | 6 | 0.0 | -8.94 | -2.21 | -53.64 | 17.31 | -0.52 | -44.12 | 0.0 |
| 2832 | 21 | 53.67 | Qty ≥5k shares — hold ret_low_30d_open | Qty ≥5k shares | low | 30 | open | 6 | 0.0 | -8.94 | -2.21 | -53.64 | 17.31 | -0.52 | -44.12 | 0.0 |
| 2833 | 20 | 53.67 | Qty ≥10k shares — hold ret_low_30d_open | Qty ≥10k shares | low | 30 | open | 6 | 0.0 | -8.94 | -2.21 | -53.64 | 17.31 | -0.52 | -44.12 | 0.0 |
| 2834 | 21 | 53.67 | Qty ≥5k shares — hold ret_low_10d_news | Qty ≥5k shares | low | 10 | news | 6 | 16.7 | -8.96 | -2.79 | -53.78 | 17.21 | -0.52 | -43.7 | 1.43 |
| 2835 | 20 | 53.67 | Qty ≥10k shares — hold ret_low_10d_news | Qty ≥10k shares | low | 10 | news | 6 | 16.7 | -8.96 | -2.79 | -53.78 | 17.21 | -0.52 | -43.7 | 1.43 |
| 2836 | 21 | 53.67 | Qty ≥5k shares — hold ret_low_14d_news | Qty ≥5k shares | low | 14 | news | 6 | 16.7 | -8.96 | -2.79 | -53.78 | 17.21 | -0.52 | -43.7 | 1.43 |
| 2837 | 20 | 53.67 | Qty ≥10k shares — hold ret_low_14d_news | Qty ≥10k shares | low | 14 | news | 6 | 16.7 | -8.96 | -2.79 | -53.78 | 17.21 | -0.52 | -43.7 | 1.43 |
| 2838 | 21 | 53.67 | Qty ≥5k shares — hold ret_low_30d_news | Qty ≥5k shares | low | 30 | news | 6 | 16.7 | -8.96 | -2.79 | -53.78 | 17.21 | -0.52 | -43.7 | 1.43 |
| 2839 | 20 | 53.67 | Qty ≥10k shares — hold ret_low_30d_news | Qty ≥10k shares | low | 30 | news | 6 | 16.7 | -8.96 | -2.79 | -53.78 | 17.21 | -0.52 | -43.7 | 1.43 |
| 2840 | 53 | 0.0 | Qty ≥100k shares — hold ret_low_3d_news | Qty ≥100k shares | low | 3 | news | 1 | 0.0 | -9.04 | -9.04 | -9.04 | nan | nan | -9.04 | -9.04 |
| 2841 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_low_3d_news | Small cap (≤1B) Value ≥100k | low | 3 | news | 1 | 0.0 | -9.04 | -9.04 | -9.04 | nan | nan | -9.04 | -9.04 |
| 2842 | 37 | 35.58 | Director only + Value ≥100k — hold ret_low_7d_open | Director only + Value ≥100k | low | 7 | open | 3 | 0.0 | -9.1 | -4.22 | -27.31 | 12.3 | -0.74 | -23.09 | 0.0 |
| 2843 | 33 | 41.81 | Director — hold ret_low_30d_news | Director | low | 30 | news | 8 | 0.0 | -9.1 | -5.5 | -72.77 | 14.16 | -0.64 | -43.7 | -0.04 |
| 2844 | 51 | 20.1 | Position +30% — hold ret_mean_60d_news | Position +30% | mean | 60 | news | 3 | 66.7 | -9.1 | 0.21 | -27.29 | 16.71 | -0.54 | -28.39 | 0.89 |
| 2845 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_low_10d_news | Large cap (≥3B) CEO/CFO | low | 10 | news | 1 | 0.0 | -9.28 | -9.28 | -9.28 | nan | nan | -9.28 | -9.28 |
| 2846 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_low_10d_news | Large cap (≥5B) CEO/CFO | low | 10 | news | 1 | 0.0 | -9.28 | -9.28 | -9.28 | nan | nan | -9.28 | -9.28 |
| 2847 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_low_10d_news | Large cap (≥10B) CEO/CFO | low | 10 | news | 1 | 0.0 | -9.28 | -9.28 | -9.28 | nan | nan | -9.28 | -9.28 |
| 2848 | 32 | 44.63 | Position +10% — hold ret_low_10d_open | Position +10% | low | 10 | open | 6 | 0.0 | -9.34 | -2.77 | -56.07 | 17.15 | -0.55 | -44.12 | 0.0 |
| 2849 | 32 | 44.63 | Position +10% — hold ret_low_14d_open | Position +10% | low | 14 | open | 6 | 0.0 | -9.36 | -2.81 | -56.14 | 17.14 | -0.55 | -44.12 | 0.0 |
| 2850 | 32 | 44.63 | Position +10% — hold ret_low_10d_news | Position +10% | low | 10 | news | 6 | 16.7 | -9.37 | -4.01 | -56.23 | 17.07 | -0.55 | -43.7 | 1.43 |
| 2851 | 32 | 44.63 | Position +10% — hold ret_low_14d_news | Position +10% | low | 14 | news | 6 | 16.7 | -9.38 | -4.04 | -56.3 | 17.06 | -0.55 | -43.7 | 1.43 |
| 2852 | 51 | 20.1 | Position +30% — hold ret_mean_90d_news | Position +30% | mean | 90 | news | 3 | 33.3 | -9.39 | -2.13 | -28.18 | 14.53 | -0.65 | -26.12 | 0.07 |
| 2853 | 15 | 62.43 | Price > MA50 — hold ret_low_60d_news | Price > MA50 | low | 60 | news | 5 | 0.0 | -9.45 | -6.57 | -47.25 | 6.91 | -1.37 | -18.33 | -3.47 |
| 2854 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_low_7d_news | Far 52w high + Value ≥100k | low | 7 | news | 3 | 0.0 | -9.51 | -5.9 | -28.53 | 11.63 | -0.82 | -22.52 | -0.11 |
| 2855 | 51 | 20.1 | Position +30% — hold ret_low_7d_open | Position +30% | low | 7 | open | 3 | 0.0 | -9.55 | -3.28 | -28.64 | 11.74 | -0.81 | -23.09 | -2.27 |
| 2856 | 49 | 32.78 | CFO only — hold ret_low_60d_news | CFO only | low | 60 | news | 1 | 0.0 | -9.59 | -9.59 | -9.59 | nan | nan | -9.59 | -9.59 |
| 2857 | 48 | 32.78 | CFO + Director (combo) — hold ret_low_60d_news | CFO + Director (combo) | low | 60 | news | 1 | 0.0 | -9.59 | -9.59 | -9.59 | nan | nan | -9.59 | -9.59 |
| 2858 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_low_60d_news | CFO only + Value ≥50k | low | 60 | news | 1 | 0.0 | -9.59 | -9.59 | -9.59 | nan | nan | -9.59 | -9.59 |
| 2859 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_low_60d_news | CFO only + Value ≥100k | low | 60 | news | 1 | 0.0 | -9.59 | -9.59 | -9.59 | nan | nan | -9.59 | -9.59 |
| 2860 | 47 | 32.78 | CFO only + Position +10% — hold ret_low_60d_news | CFO only + Position +10% | low | 60 | news | 1 | 0.0 | -9.59 | -9.59 | -9.59 | nan | nan | -9.59 | -9.59 |
| 2861 | 46 | 32.78 | CFO only + Position +20% — hold ret_low_60d_news | CFO only + Position +20% | low | 60 | news | 1 | 0.0 | -9.59 | -9.59 | -9.59 | nan | nan | -9.59 | -9.59 |
| 2862 | 44 | 32.78 | RSI oversold (<30) — hold ret_low_60d_news | RSI oversold (<30) | low | 60 | news | 1 | 0.0 | -9.59 | -9.59 | -9.59 | nan | nan | -9.59 | -9.59 |
| 2863 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_low_60d_news | RSI oversold + CEO/CFO | low | 60 | news | 1 | 0.0 | -9.59 | -9.59 | -9.59 | nan | nan | -9.59 | -9.59 |
| 2864 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_low_60d_news | RSI oversold + Value ≥100k | low | 60 | news | 1 | 0.0 | -9.59 | -9.59 | -9.59 | nan | nan | -9.59 | -9.59 |
| 2865 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_low_7d_open | Far 52w high + Value ≥100k | low | 7 | open | 3 | 0.0 | -9.69 | -3.28 | -29.07 | 11.61 | -0.83 | -23.09 | -2.7 |
| 2866 | 53 | 0.0 | Qty ≥100k shares — hold ret_low_3d_open | Qty ≥100k shares | low | 3 | open | 1 | 0.0 | -9.71 | -9.71 | -9.71 | nan | nan | -9.71 | -9.71 |
| 2867 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_low_3d_open | Small cap (≤1B) Value ≥100k | low | 3 | open | 1 | 0.0 | -9.71 | -9.71 | -9.71 | nan | nan | -9.71 | -9.71 |
| 2868 | 32 | 44.63 | Position +10% — hold ret_low_30d_open | Position +10% | low | 30 | open | 6 | 0.0 | -9.84 | -4.26 | -59.05 | 16.94 | -0.58 | -44.12 | 0.0 |
| 2869 | 32 | 44.63 | Position +10% — hold ret_low_30d_news | Position +10% | low | 30 | news | 6 | 16.7 | -9.87 | -5.5 | -59.2 | 16.87 | -0.58 | -43.7 | 1.43 |
| 2870 | 30 | 48.32 | Value ≥100k — hold ret_low_10d_news | Value ≥100k | low | 10 | news | 6 | 16.7 | -10.16 | -4.69 | -60.96 | 16.88 | -0.6 | -43.7 | 1.43 |
| 2871 | 51 | 20.1 | Position +30% — hold ret_low_7d_news | Position +30% | low | 7 | news | 3 | 0.0 | -10.3 | -5.9 | -30.91 | 10.72 | -0.96 | -22.52 | -2.49 |
| 2872 | 36 | 36.54 | Director only (no C-level) — hold ret_low_10d_news | Director only (no C-level) | low | 10 | news | 6 | 0.0 | -10.3 | -4.5 | -61.8 | 16.52 | -0.62 | -43.7 | -0.04 |
| 2873 | 36 | 36.54 | Director only (no C-level) — hold ret_low_14d_news | Director only (no C-level) | low | 14 | news | 6 | 0.0 | -10.31 | -4.5 | -61.87 | 16.52 | -0.62 | -43.7 | -0.04 |
| 2874 | 15 | 62.43 | Price > MA50 — hold ret_low_60d_open | Price > MA50 | low | 60 | open | 5 | 0.0 | -10.42 | -6.57 | -52.12 | 7.52 | -1.39 | -20.45 | -4.22 |
| 2875 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_mean_90d_news | Far 52w high + Value ≥100k | mean | 90 | news | 3 | 0.0 | -10.47 | -3.15 | -31.4 | 13.57 | -0.77 | -26.12 | -2.13 |
| 2876 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_mean_60d_news | Far 52w high + Value ≥100k | mean | 60 | news | 3 | 33.3 | -10.49 | -3.97 | -31.47 | 15.69 | -0.67 | -28.39 | 0.89 |
| 2877 | 26 | 50.0 | Qty ≥50k shares — hold ret_low_7d_news | Qty ≥50k shares | low | 7 | news | 2 | 50.0 | -10.54 | -10.54 | -21.09 | 16.94 | -0.62 | -22.52 | 1.43 |
| 2878 | 27 | 50.0 | Value ≥1M — hold ret_low_7d_news | Value ≥1M | low | 7 | news | 2 | 50.0 | -10.54 | -10.54 | -21.09 | 16.94 | -0.62 | -22.52 | 1.43 |
| 2879 | 30 | 48.32 | Value ≥100k — hold ret_low_14d_news | Value ≥100k | low | 14 | news | 6 | 16.7 | -10.55 | -4.69 | -63.3 | 16.89 | -0.62 | -43.7 | 1.43 |
| 2880 | 30 | 48.32 | Value ≥100k — hold ret_low_30d_news | Value ≥100k | low | 30 | news | 6 | 16.7 | -10.55 | -4.69 | -63.3 | 16.89 | -0.62 | -43.7 | 1.43 |
| 2881 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_mean_60d_open | Far 52w high + Value ≥100k | mean | 60 | open | 3 | 33.3 | -10.56 | -6.46 | -31.68 | 16.69 | -0.63 | -28.92 | 3.7 |
| 2882 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_mean_90d_open | Far 52w high + Value ≥100k | mean | 90 | open | 3 | 33.3 | -10.57 | -5.65 | -31.71 | 14.28 | -0.74 | -26.66 | 0.6 |
| 2883 | 36 | 36.54 | Director only (no C-level) — hold ret_low_10d_open | Director only (no C-level) | low | 10 | open | 6 | 0.0 | -10.6 | -4.88 | -63.58 | 16.55 | -0.64 | -44.12 | -0.87 |
| 2884 | 36 | 36.54 | Director only (no C-level) — hold ret_low_14d_open | Director only (no C-level) | low | 14 | open | 6 | 0.0 | -10.61 | -4.88 | -63.65 | 16.55 | -0.64 | -44.12 | -0.87 |
| 2885 | 30 | 48.32 | Value ≥100k — hold ret_low_10d_open | Value ≥100k | low | 10 | open | 6 | 0.0 | -10.69 | -3.75 | -64.12 | 16.89 | -0.63 | -44.12 | 0.0 |
| 2886 | 36 | 36.54 | Director only (no C-level) — hold ret_low_30d_news | Director only (no C-level) | low | 30 | news | 6 | 0.0 | -10.8 | -5.5 | -64.77 | 16.29 | -0.66 | -43.7 | -0.04 |
| 2887 | 33 | 41.81 | Director — hold ret_low_60d_open | Director | low | 60 | open | 8 | 0.0 | -10.94 | -6.05 | -87.5 | 16.1 | -0.68 | -50.44 | -1.15 |
| 2888 | 30 | 48.32 | Value ≥100k — hold ret_low_14d_open | Value ≥100k | low | 14 | open | 6 | 0.0 | -11.07 | -3.75 | -66.4 | 16.94 | -0.65 | -44.12 | 0.0 |
| 2889 | 30 | 48.32 | Value ≥100k — hold ret_low_30d_open | Value ≥100k | low | 30 | open | 6 | 0.0 | -11.07 | -3.75 | -66.4 | 16.94 | -0.65 | -44.12 | 0.0 |
| 2890 | 36 | 36.54 | Director only (no C-level) — hold ret_low_30d_open | Director only (no C-level) | low | 30 | open | 6 | 0.0 | -11.09 | -5.39 | -66.56 | 16.3 | -0.68 | -44.12 | -0.87 |
| 2891 | 33 | 41.81 | Director — hold ret_low_60d_news | Director | low | 60 | news | 8 | 0.0 | -11.16 | -6.05 | -89.24 | 15.93 | -0.7 | -50.07 | -2.1 |
| 2892 | 14 | 65.45 | Price > MA200 — hold ret_low_90d_news | Price > MA200 | low | 90 | news | 4 | 0.0 | -11.19 | -9.41 | -44.76 | 8.02 | -1.39 | -22.46 | -3.47 |
| 2893 | 38 | 34.53 | Price < MA50 — hold ret_low_10d_open | Price < MA50 | low | 10 | open | 5 | 0.0 | -11.27 | -3.28 | -56.35 | 18.43 | -0.61 | -44.12 | -1.15 |
| 2894 | 38 | 34.53 | Price < MA50 — hold ret_low_14d_open | Price < MA50 | low | 14 | open | 5 | 0.0 | -11.28 | -3.28 | -56.42 | 18.43 | -0.61 | -44.12 | -1.15 |
| 2895 | 10 | 66.41 | CEO/CFO — hold ret_low_60d_open | CEO/CFO | low | 60 | open | 4 | 0.0 | -11.28 | -11.77 | -45.13 | 8.78 | -1.29 | -20.45 | -1.15 |
| 2896 | 11 | 66.41 | Officer/President — hold ret_low_60d_open | Officer/President | low | 60 | open | 4 | 0.0 | -11.28 | -11.77 | -45.13 | 8.78 | -1.29 | -20.45 | -1.15 |
| 2897 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_low_60d_open | Large cap (≥250M) CEO/CFO | low | 60 | open | 4 | 0.0 | -11.28 | -11.77 | -45.13 | 8.78 | -1.29 | -20.45 | -1.15 |
| 2898 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_low_60d_open | Large cap (≥500M) CEO/CFO | low | 60 | open | 4 | 0.0 | -11.28 | -11.77 | -45.13 | 8.78 | -1.29 | -20.45 | -1.15 |
| 2899 | 10 | 66.41 | CEO/CFO — hold ret_low_60d_news | CEO/CFO | low | 60 | news | 4 | 0.0 | -11.32 | -12.43 | -45.29 | 7.14 | -1.59 | -18.33 | -2.1 |
| 2900 | 11 | 66.41 | Officer/President — hold ret_low_60d_news | Officer/President | low | 60 | news | 4 | 0.0 | -11.32 | -12.43 | -45.29 | 7.14 | -1.59 | -18.33 | -2.1 |
| 2901 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_low_60d_news | Large cap (≥250M) CEO/CFO | low | 60 | news | 4 | 0.0 | -11.32 | -12.43 | -45.29 | 7.14 | -1.59 | -18.33 | -2.1 |
| 2902 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_low_60d_news | Large cap (≥500M) CEO/CFO | low | 60 | news | 4 | 0.0 | -11.32 | -12.43 | -45.29 | 7.14 | -1.59 | -18.33 | -2.1 |
| 2903 | 26 | 50.0 | Qty ≥50k shares — hold ret_low_7d_open | Qty ≥50k shares | low | 7 | open | 2 | 0.0 | -11.54 | -11.54 | -23.09 | 16.33 | -0.71 | -23.09 | 0.0 |
| 2904 | 27 | 50.0 | Value ≥1M — hold ret_low_7d_open | Value ≥1M | low | 7 | open | 2 | 0.0 | -11.54 | -11.54 | -23.09 | 16.33 | -0.71 | -23.09 | 0.0 |
| 2905 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_low_14d_news | Large cap (≥3B) CEO/CFO | low | 14 | news | 1 | 0.0 | -11.62 | -11.62 | -11.62 | nan | nan | -11.62 | -11.62 |
| 2906 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_low_14d_news | Large cap (≥5B) CEO/CFO | low | 14 | news | 1 | 0.0 | -11.62 | -11.62 | -11.62 | nan | nan | -11.62 | -11.62 |
| 2907 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_low_14d_news | Large cap (≥10B) CEO/CFO | low | 14 | news | 1 | 0.0 | -11.62 | -11.62 | -11.62 | nan | nan | -11.62 | -11.62 |
| 2908 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_low_30d_news | Large cap (≥3B) CEO/CFO | low | 30 | news | 1 | 0.0 | -11.62 | -11.62 | -11.62 | nan | nan | -11.62 | -11.62 |
| 2909 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_low_30d_news | Large cap (≥5B) CEO/CFO | low | 30 | news | 1 | 0.0 | -11.62 | -11.62 | -11.62 | nan | nan | -11.62 | -11.62 |
| 2910 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_low_30d_news | Large cap (≥10B) CEO/CFO | low | 30 | news | 1 | 0.0 | -11.62 | -11.62 | -11.62 | nan | nan | -11.62 | -11.62 |
| 2911 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_low_10d_open | Large cap (≥3B) CEO/CFO | low | 10 | open | 1 | 0.0 | -11.63 | -11.63 | -11.63 | nan | nan | -11.63 | -11.63 |
| 2912 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_low_10d_open | Large cap (≥5B) CEO/CFO | low | 10 | open | 1 | 0.0 | -11.63 | -11.63 | -11.63 | nan | nan | -11.63 | -11.63 |
| 2913 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_low_10d_open | Large cap (≥10B) CEO/CFO | low | 10 | open | 1 | 0.0 | -11.63 | -11.63 | -11.63 | nan | nan | -11.63 | -11.63 |
| 2914 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_low_60d_open | Mid cap (1B–10B) CEO/CFO | low | 60 | open | 2 | 0.0 | -11.76 | -11.77 | -23.53 | 6.64 | -1.77 | -16.46 | -7.07 |
| 2915 | 14 | 65.45 | Price > MA200 — hold ret_low_90d_open | Price > MA200 | low | 90 | open | 4 | 0.0 | -11.84 | -9.79 | -47.35 | 8.25 | -1.43 | -23.55 | -4.22 |
| 2916 | 38 | 34.53 | Price < MA50 — hold ret_low_30d_open | Price < MA50 | low | 30 | open | 5 | 0.0 | -11.87 | -5.25 | -59.33 | 18.12 | -0.65 | -44.12 | -1.15 |
| 2917 | 6 | 77.62 | CEO only — hold ret_low_60d_news | CEO only | low | 60 | news | 3 | 0.0 | -11.9 | -15.27 | -35.7 | 8.62 | -1.38 | -18.33 | -2.1 |
| 2918 | 38 | 34.53 | Price < MA50 — hold ret_low_10d_news | Price < MA50 | low | 10 | news | 5 | 0.0 | -11.94 | -5.53 | -59.72 | 17.84 | -0.67 | -43.7 | -2.1 |
| 2919 | 38 | 34.53 | Price < MA50 — hold ret_low_14d_news | Price < MA50 | low | 14 | news | 5 | 0.0 | -11.96 | -5.53 | -59.79 | 17.83 | -0.67 | -43.7 | -2.1 |
| 2920 | 26 | 50.0 | Qty ≥50k shares — hold ret_mean_60d_news | Qty ≥50k shares | mean | 60 | news | 2 | 50.0 | -11.96 | -11.96 | -23.93 | 23.23 | -0.52 | -28.39 | 4.46 |
| 2921 | 27 | 50.0 | Value ≥1M — hold ret_mean_60d_news | Value ≥1M | mean | 60 | news | 2 | 50.0 | -11.96 | -11.96 | -23.93 | 23.23 | -0.52 | -28.39 | 4.46 |
| 2922 | 53 | 0.0 | Qty ≥100k shares — hold ret_mean_10d_news | Qty ≥100k shares | mean | 10 | news | 1 | 0.0 | -12.21 | -12.21 | -12.21 | nan | nan | -12.21 | -12.21 |
| 2923 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_mean_10d_news | Small cap (≤1B) Value ≥100k | mean | 10 | news | 1 | 0.0 | -12.21 | -12.21 | -12.21 | nan | nan | -12.21 | -12.21 |
| 2924 | 28 | 48.48 | Tutti — hold ret_low_60d_news | Tutti | low | 60 | news | 10 | 0.0 | -12.28 | -7.44 | -122.84 | 14.26 | -0.86 | -50.07 | -2.1 |
| 2925 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_low_60d_news | Mid cap (1B–10B) CEO/CFO | low | 60 | news | 2 | 0.0 | -12.43 | -12.43 | -24.86 | 4.02 | -3.09 | -15.27 | -9.59 |
| 2926 | 28 | 48.48 | Tutti — hold ret_low_60d_open | Tutti | low | 60 | open | 10 | 0.0 | -12.44 | -6.82 | -124.41 | 14.58 | -0.85 | -50.44 | -1.15 |
| 2927 | 38 | 34.53 | Price < MA50 — hold ret_low_30d_news | Price < MA50 | low | 30 | news | 5 | 0.0 | -12.54 | -5.53 | -62.69 | 17.49 | -0.72 | -43.7 | -2.1 |
| 2928 | 39 | 34.48 | Position +20% — hold ret_low_10d_open | Position +20% | low | 10 | open | 4 | 0.0 | -12.64 | -2.77 | -50.54 | 21.01 | -0.6 | -44.12 | -0.87 |
| 2929 | 39 | 34.48 | Position +20% — hold ret_low_14d_open | Position +20% | low | 14 | open | 4 | 0.0 | -12.65 | -2.81 | -50.61 | 21.0 | -0.6 | -44.12 | -0.87 |
| 2930 | 6 | 77.62 | CEO only — hold ret_low_60d_open | CEO only | low | 60 | open | 3 | 0.0 | -12.69 | -16.46 | -38.06 | 10.19 | -1.25 | -20.45 | -1.15 |
| 2931 | 53 | 0.0 | Qty ≥100k shares — hold ret_mean_10d_open | Qty ≥100k shares | mean | 10 | open | 1 | 0.0 | -12.85 | -12.85 | -12.85 | nan | nan | -12.85 | -12.85 |
| 2932 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_mean_10d_open | Small cap (≤1B) Value ≥100k | mean | 10 | open | 1 | 0.0 | -12.85 | -12.85 | -12.85 | nan | nan | -12.85 | -12.85 |
| 2933 | 35 | 40.48 | Value ≥500k — hold ret_low_10d_open | Value ≥500k | low | 10 | open | 4 | 0.0 | -12.9 | -3.75 | -51.62 | 20.89 | -0.62 | -44.12 | 0.0 |
| 2934 | 35 | 40.48 | Value ≥500k — hold ret_low_14d_open | Value ≥500k | low | 14 | open | 4 | 0.0 | -12.9 | -3.75 | -51.62 | 20.89 | -0.62 | -44.12 | 0.0 |
| 2935 | 35 | 40.48 | Value ≥500k — hold ret_low_30d_open | Value ≥500k | low | 30 | open | 4 | 0.0 | -12.9 | -3.75 | -51.62 | 20.89 | -0.62 | -44.12 | 0.0 |
| 2936 | 35 | 40.48 | Value ≥500k — hold ret_low_10d_news | Value ≥500k | low | 10 | news | 4 | 25.0 | -12.91 | -4.69 | -51.64 | 20.75 | -0.62 | -43.7 | 1.43 |
| 2937 | 35 | 40.48 | Value ≥500k — hold ret_low_14d_news | Value ≥500k | low | 14 | news | 4 | 25.0 | -12.91 | -4.69 | -51.64 | 20.75 | -0.62 | -43.7 | 1.43 |
| 2938 | 35 | 40.48 | Value ≥500k — hold ret_low_30d_news | Value ≥500k | low | 30 | news | 4 | 25.0 | -12.91 | -4.69 | -51.64 | 20.75 | -0.62 | -43.7 | 1.43 |
| 2939 | 36 | 36.54 | Director only (no C-level) — hold ret_low_60d_news | Director only (no C-level) | low | 60 | news | 6 | 0.0 | -12.92 | -6.05 | -77.55 | 18.29 | -0.71 | -50.07 | -3.47 |
| 2940 | 31 | 47.75 | Value ≥50k — hold ret_low_60d_news | Value ≥50k | low | 60 | news | 9 | 0.0 | -12.92 | -8.3 | -116.27 | 14.98 | -0.86 | -50.07 | -2.1 |
| 2941 | 40 | 33.74 | Director only + Position +10% — hold ret_low_10d_news | Director only + Position +10% | low | 10 | news | 4 | 0.0 | -12.94 | -4.01 | -51.76 | 20.63 | -0.63 | -43.7 | -0.04 |
| 2942 | 33 | 41.81 | Director — hold ret_low_90d_open | Director | low | 90 | open | 8 | 0.0 | -12.94 | -8.63 | -103.52 | 15.69 | -0.82 | -50.44 | -1.15 |
| 2943 | 40 | 33.74 | Director only + Position +10% — hold ret_low_14d_news | Director only + Position +10% | low | 14 | news | 4 | 0.0 | -12.96 | -4.04 | -51.83 | 20.62 | -0.63 | -43.7 | -0.04 |
| 2944 | 26 | 50.0 | Qty ≥50k shares — hold ret_mean_60d_open | Qty ≥50k shares | mean | 60 | open | 2 | 50.0 | -12.96 | -12.96 | -25.93 | 22.56 | -0.57 | -28.92 | 2.99 |
| 2945 | 27 | 50.0 | Value ≥1M — hold ret_mean_60d_open | Value ≥1M | mean | 60 | open | 2 | 50.0 | -12.96 | -12.96 | -25.93 | 22.56 | -0.57 | -28.92 | 2.99 |
| 2946 | 39 | 34.48 | Position +20% — hold ret_low_10d_news | Position +20% | low | 10 | news | 4 | 0.0 | -13.03 | -4.2 | -52.13 | 20.59 | -0.63 | -43.7 | -0.04 |
| 2947 | 39 | 34.48 | Position +20% — hold ret_low_14d_news | Position +20% | low | 14 | news | 4 | 0.0 | -13.05 | -4.23 | -52.2 | 20.57 | -0.63 | -43.7 | -0.04 |
| 2948 | 31 | 47.75 | Value ≥50k — hold ret_low_60d_open | Value ≥50k | low | 60 | open | 9 | 0.0 | -13.09 | -7.07 | -117.84 | 15.31 | -0.86 | -50.44 | -1.15 |
| 2949 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_low_90d_news | Mid cap (1B–10B) Value ≥100k | low | 90 | news | 4 | 0.0 | -13.1 | -13.25 | -52.42 | 8.29 | -1.58 | -22.46 | -3.47 |
| 2950 | 33 | 41.81 | Director — hold ret_low_90d_news | Director | low | 90 | news | 8 | 0.0 | -13.14 | -8.73 | -105.12 | 15.59 | -0.84 | -50.07 | -2.1 |
| 2951 | 15 | 62.43 | Price > MA50 — hold ret_low_90d_news | Price > MA50 | low | 90 | news | 5 | 0.0 | -13.15 | -9.67 | -65.74 | 8.21 | -1.6 | -22.46 | -3.47 |
| 2952 | 19 | 59.88 | Mid cap (1B–10B) Value ≥100k — hold ret_low_90d_open | Mid cap (1B–10B) Value ≥100k | low | 90 | open | 4 | 0.0 | -13.17 | -12.46 | -52.69 | 8.11 | -1.62 | -23.55 | -4.22 |
| 2953 | 40 | 33.74 | Director only + Position +10% — hold ret_low_10d_open | Director only + Position +10% | low | 10 | open | 4 | 0.0 | -13.2 | -3.9 | -52.79 | 20.71 | -0.64 | -44.12 | -0.87 |
| 2954 | 36 | 36.54 | Director only (no C-level) — hold ret_low_60d_open | Director only (no C-level) | low | 60 | open | 6 | 0.0 | -13.21 | -6.05 | -79.28 | 18.29 | -0.72 | -50.44 | -4.22 |
| 2955 | 40 | 33.74 | Director only + Position +10% — hold ret_low_14d_open | Director only + Position +10% | low | 14 | open | 4 | 0.0 | -13.22 | -3.94 | -52.86 | 20.69 | -0.64 | -44.12 | -0.87 |
| 2956 | 39 | 34.48 | Position +20% — hold ret_low_30d_open | Position +20% | low | 30 | open | 4 | 0.0 | -13.38 | -4.26 | -53.52 | 20.57 | -0.65 | -44.12 | -0.87 |
| 2957 | 40 | 33.74 | Director only + Position +10% — hold ret_low_30d_news | Director only + Position +10% | low | 30 | news | 4 | 0.0 | -13.68 | -5.5 | -54.73 | 20.18 | -0.68 | -43.7 | -0.04 |
| 2958 | 26 | 50.0 | Qty ≥50k shares — hold ret_mean_90d_news | Qty ≥50k shares | mean | 90 | news | 2 | 0.0 | -13.7 | -13.7 | -27.39 | 17.57 | -0.78 | -26.12 | -1.27 |
| 2959 | 27 | 50.0 | Value ≥1M — hold ret_mean_90d_news | Value ≥1M | mean | 90 | news | 2 | 0.0 | -13.7 | -13.7 | -27.39 | 17.57 | -0.78 | -26.12 | -1.27 |
| 2960 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_low_60d_open | Large cap (≥2B) CEO/CFO | low | 60 | open | 2 | 0.0 | -13.76 | -13.76 | -27.52 | 9.46 | -1.45 | -20.45 | -7.07 |
| 2961 | 39 | 34.48 | Position +20% — hold ret_low_30d_news | Position +20% | low | 30 | news | 4 | 0.0 | -13.78 | -5.68 | -55.1 | 20.13 | -0.68 | -43.7 | -0.04 |
| 2962 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_low_14d_open | Large cap (≥3B) CEO/CFO | low | 14 | open | 1 | 0.0 | -13.91 | -13.91 | -13.91 | nan | nan | -13.91 | -13.91 |
| 2963 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_low_14d_open | Large cap (≥5B) CEO/CFO | low | 14 | open | 1 | 0.0 | -13.91 | -13.91 | -13.91 | nan | nan | -13.91 | -13.91 |
| 2964 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_low_14d_open | Large cap (≥10B) CEO/CFO | low | 14 | open | 1 | 0.0 | -13.91 | -13.91 | -13.91 | nan | nan | -13.91 | -13.91 |
| 2965 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_low_30d_open | Large cap (≥3B) CEO/CFO | low | 30 | open | 1 | 0.0 | -13.91 | -13.91 | -13.91 | nan | nan | -13.91 | -13.91 |
| 2966 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_low_30d_open | Large cap (≥5B) CEO/CFO | low | 30 | open | 1 | 0.0 | -13.91 | -13.91 | -13.91 | nan | nan | -13.91 | -13.91 |
| 2967 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_low_30d_open | Large cap (≥10B) CEO/CFO | low | 30 | open | 1 | 0.0 | -13.91 | -13.91 | -13.91 | nan | nan | -13.91 | -13.91 |
| 2968 | 40 | 33.74 | Director only + Position +10% — hold ret_low_30d_open | Director only + Position +10% | low | 30 | open | 4 | 0.0 | -13.94 | -5.39 | -55.77 | 20.23 | -0.69 | -44.12 | -0.87 |
| 2969 | 21 | 53.67 | Qty ≥5k shares — hold ret_low_60d_open | Qty ≥5k shares | low | 60 | open | 6 | 0.0 | -13.96 | -5.75 | -83.76 | 18.63 | -0.75 | -50.44 | -1.15 |
| 2970 | 20 | 53.67 | Qty ≥10k shares — hold ret_low_60d_open | Qty ≥10k shares | low | 60 | open | 6 | 0.0 | -13.96 | -5.75 | -83.76 | 18.63 | -0.75 | -50.44 | -1.15 |
| 2971 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_low_60d_news | Large cap (≥2B) CEO/CFO | low | 60 | news | 2 | 0.0 | -13.96 | -13.96 | -27.92 | 6.18 | -2.26 | -18.33 | -9.59 |
| 2972 | 21 | 53.67 | Qty ≥5k shares — hold ret_low_60d_news | Qty ≥5k shares | low | 60 | news | 6 | 0.0 | -14.02 | -6.6 | -84.11 | 18.34 | -0.76 | -50.07 | -2.1 |
| 2973 | 20 | 53.67 | Qty ≥10k shares — hold ret_low_60d_news | Qty ≥10k shares | low | 60 | news | 6 | 0.0 | -14.02 | -6.6 | -84.11 | 18.34 | -0.76 | -50.07 | -2.1 |
| 2974 | 15 | 62.43 | Price > MA50 — hold ret_low_90d_open | Price > MA50 | low | 90 | open | 5 | 0.0 | -14.08 | -10.42 | -70.38 | 8.73 | -1.61 | -23.55 | -4.22 |
| 2975 | 36 | 36.54 | Director only (no C-level) — hold ret_low_90d_news | Director only (no C-level) | low | 90 | news | 6 | 0.0 | -14.37 | -8.73 | -86.2 | 17.65 | -0.81 | -50.07 | -3.47 |
| 2976 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_low_60d_news | CEO/CFO + Value ≥100k | low | 60 | news | 3 | 0.0 | -14.4 | -15.27 | -43.19 | 4.43 | -3.25 | -18.33 | -9.59 |
| 2977 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_low_60d_news | Large cap (≥750M) CEO/CFO | low | 60 | news | 3 | 0.0 | -14.4 | -15.27 | -43.19 | 4.43 | -3.25 | -18.33 | -9.59 |
| 2978 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_low_60d_news | Large cap (≥1B) CEO/CFO | low | 60 | news | 3 | 0.0 | -14.4 | -15.27 | -43.19 | 4.43 | -3.25 | -18.33 | -9.59 |
| 2979 | 38 | 34.53 | Price < MA50 — hold ret_low_60d_open | Price < MA50 | low | 60 | open | 5 | 0.0 | -14.46 | -7.07 | -72.29 | 20.29 | -0.71 | -50.44 | -1.15 |
| 2980 | 49 | 32.78 | CFO only — hold ret_low_90d_open | CFO only | low | 90 | open | 1 | 0.0 | -14.5 | -14.5 | -14.5 | nan | nan | -14.5 | -14.5 |
| 2981 | 48 | 32.78 | CFO + Director (combo) — hold ret_low_90d_open | CFO + Director (combo) | low | 90 | open | 1 | 0.0 | -14.5 | -14.5 | -14.5 | nan | nan | -14.5 | -14.5 |
| 2982 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_low_90d_open | CFO only + Value ≥50k | low | 90 | open | 1 | 0.0 | -14.5 | -14.5 | -14.5 | nan | nan | -14.5 | -14.5 |
| 2983 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_low_90d_open | CFO only + Value ≥100k | low | 90 | open | 1 | 0.0 | -14.5 | -14.5 | -14.5 | nan | nan | -14.5 | -14.5 |
| 2984 | 47 | 32.78 | CFO only + Position +10% — hold ret_low_90d_open | CFO only + Position +10% | low | 90 | open | 1 | 0.0 | -14.5 | -14.5 | -14.5 | nan | nan | -14.5 | -14.5 |
| 2985 | 46 | 32.78 | CFO only + Position +20% — hold ret_low_90d_open | CFO only + Position +20% | low | 90 | open | 1 | 0.0 | -14.5 | -14.5 | -14.5 | nan | nan | -14.5 | -14.5 |
| 2986 | 44 | 32.78 | RSI oversold (<30) — hold ret_low_90d_open | RSI oversold (<30) | low | 90 | open | 1 | 0.0 | -14.5 | -14.5 | -14.5 | nan | nan | -14.5 | -14.5 |
| 2987 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_low_90d_open | RSI oversold + CEO/CFO | low | 90 | open | 1 | 0.0 | -14.5 | -14.5 | -14.5 | nan | nan | -14.5 | -14.5 |
| 2988 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_low_90d_open | RSI oversold + Value ≥100k | low | 90 | open | 1 | 0.0 | -14.5 | -14.5 | -14.5 | nan | nan | -14.5 | -14.5 |
| 2989 | 36 | 36.54 | Director only (no C-level) — hold ret_low_90d_open | Director only (no C-level) | low | 90 | open | 6 | 0.0 | -14.65 | -8.63 | -87.87 | 17.69 | -0.83 | -50.44 | -4.22 |
| 2990 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_low_60d_open | CEO/CFO + Value ≥100k | low | 60 | open | 3 | 0.0 | -14.66 | -16.46 | -43.98 | 6.87 | -2.13 | -20.45 | -7.07 |
| 2991 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_low_60d_open | Large cap (≥750M) CEO/CFO | low | 60 | open | 3 | 0.0 | -14.66 | -16.46 | -43.98 | 6.87 | -2.13 | -20.45 | -7.07 |
| 2992 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_low_60d_open | Large cap (≥1B) CEO/CFO | low | 60 | open | 3 | 0.0 | -14.66 | -16.46 | -43.98 | 6.87 | -2.13 | -20.45 | -7.07 |
| 2993 | 26 | 50.0 | Qty ≥50k shares — hold ret_mean_90d_open | Qty ≥50k shares | mean | 90 | open | 2 | 0.0 | -14.66 | -14.66 | -29.32 | 16.97 | -0.86 | -26.66 | -2.66 |
| 2994 | 27 | 50.0 | Value ≥1M — hold ret_mean_90d_open | Value ≥1M | mean | 90 | open | 2 | 0.0 | -14.66 | -14.66 | -29.32 | 16.97 | -0.86 | -26.66 | -2.66 |
| 2995 | 28 | 48.48 | Tutti — hold ret_low_90d_news | Tutti | low | 90 | news | 10 | 0.0 | -14.86 | -9.41 | -148.56 | 14.22 | -1.04 | -50.07 | -2.1 |
| 2996 | 28 | 48.48 | Tutti — hold ret_low_90d_open | Tutti | low | 90 | open | 10 | 0.0 | -15.01 | -9.79 | -150.1 | 14.51 | -1.03 | -50.44 | -1.15 |
| 2997 | 38 | 34.53 | Price < MA50 — hold ret_low_60d_news | Price < MA50 | low | 60 | news | 5 | 0.0 | -15.12 | -8.3 | -75.59 | 19.75 | -0.77 | -50.07 | -2.1 |
| 2998 | 6 | 77.62 | CEO only — hold ret_low_90d_news | CEO only | low | 90 | news | 3 | 0.0 | -15.18 | -20.98 | -45.54 | 11.35 | -1.34 | -22.46 | -2.1 |
| 2999 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_low_60d_news | CEO only + Value ≥500k | low | 60 | news | 1 | 0.0 | -15.27 | -15.27 | -15.27 | nan | nan | -15.27 | -15.27 |
| 3000 | 1 | 100.0 | CEO only + Position +10% — hold ret_low_60d_news | CEO only + Position +10% | low | 60 | news | 1 | 0.0 | -15.27 | -15.27 | -15.27 | nan | nan | -15.27 | -15.27 |
| 3001 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_low_60d_news | Near 52w high + CEO/CFO | low | 60 | news | 1 | 0.0 | -15.27 | -15.27 | -15.27 | nan | nan | -15.27 | -15.27 |
| 3002 | 32 | 44.63 | Position +10% — hold ret_low_60d_open | Position +10% | low | 60 | open | 6 | 0.0 | -15.34 | -7.58 | -92.02 | 17.72 | -0.87 | -50.44 | -4.42 |
| 3003 | 32 | 44.63 | Position +10% — hold ret_low_60d_news | Position +10% | low | 60 | news | 6 | 0.0 | -15.4 | -8.95 | -92.37 | 17.45 | -0.88 | -50.07 | -3.61 |
| 3004 | 31 | 47.75 | Value ≥50k — hold ret_low_90d_news | Value ≥50k | low | 90 | news | 9 | 0.0 | -15.49 | -9.67 | -139.4 | 14.94 | -1.04 | -50.07 | -2.1 |
| 3005 | 10 | 66.41 | CEO/CFO — hold ret_low_90d_open | CEO/CFO | low | 90 | open | 4 | 0.0 | -15.56 | -18.77 | -62.23 | 10.46 | -1.49 | -23.55 | -1.15 |
| 3006 | 11 | 66.41 | Officer/President — hold ret_low_90d_open | Officer/President | low | 90 | open | 4 | 0.0 | -15.56 | -18.77 | -62.23 | 10.46 | -1.49 | -23.55 | -1.15 |
| 3007 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_low_90d_open | Large cap (≥250M) CEO/CFO | low | 90 | open | 4 | 0.0 | -15.56 | -18.77 | -62.23 | 10.46 | -1.49 | -23.55 | -1.15 |
| 3008 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_low_90d_open | Large cap (≥500M) CEO/CFO | low | 90 | open | 4 | 0.0 | -15.56 | -18.77 | -62.23 | 10.46 | -1.49 | -23.55 | -1.15 |
| 3009 | 10 | 66.41 | CEO/CFO — hold ret_low_90d_news | CEO/CFO | low | 90 | news | 4 | 0.0 | -15.59 | -18.9 | -62.36 | 9.3 | -1.68 | -22.46 | -2.1 |
| 3010 | 11 | 66.41 | Officer/President — hold ret_low_90d_news | Officer/President | low | 90 | news | 4 | 0.0 | -15.59 | -18.9 | -62.36 | 9.3 | -1.68 | -22.46 | -2.1 |
| 3011 | 9 | 66.41 | Large cap (≥250M) CEO/CFO — hold ret_low_90d_news | Large cap (≥250M) CEO/CFO | low | 90 | news | 4 | 0.0 | -15.59 | -18.9 | -62.36 | 9.3 | -1.68 | -22.46 | -2.1 |
| 3012 | 12 | 66.41 | Large cap (≥500M) CEO/CFO — hold ret_low_90d_news | Large cap (≥500M) CEO/CFO | low | 90 | news | 4 | 0.0 | -15.59 | -18.9 | -62.36 | 9.3 | -1.68 | -22.46 | -2.1 |
| 3013 | 31 | 47.75 | Value ≥50k — hold ret_low_90d_open | Value ≥50k | low | 90 | open | 9 | 0.0 | -15.66 | -10.42 | -140.94 | 15.23 | -1.03 | -50.44 | -1.15 |
| 3014 | 37 | 35.58 | Director only + Value ≥100k — hold ret_low_10d_news | Director only + Value ≥100k | low | 10 | news | 3 | 0.0 | -15.74 | -3.47 | -47.21 | 24.28 | -0.65 | -43.7 | -0.04 |
| 3015 | 37 | 35.58 | Director only + Value ≥100k — hold ret_low_14d_news | Director only + Value ≥100k | low | 14 | news | 3 | 0.0 | -15.74 | -3.47 | -47.21 | 24.28 | -0.65 | -43.7 | -0.04 |
| 3016 | 37 | 35.58 | Director only + Value ≥100k — hold ret_low_30d_news | Director only + Value ≥100k | low | 30 | news | 3 | 0.0 | -15.74 | -3.47 | -47.21 | 24.28 | -0.65 | -43.7 | -0.04 |
| 3017 | 6 | 77.62 | CEO only — hold ret_low_90d_open | CEO only | low | 90 | open | 3 | 0.0 | -15.91 | -23.03 | -47.73 | 12.79 | -1.24 | -23.55 | -1.15 |
| 3018 | 38 | 34.53 | Price < MA50 — hold ret_low_90d_open | Price < MA50 | low | 90 | open | 5 | 0.0 | -15.94 | -8.1 | -79.72 | 19.88 | -0.8 | -50.44 | -1.15 |
| 3019 | 37 | 35.58 | Director only + Value ≥100k — hold ret_low_10d_open | Director only + Value ≥100k | low | 10 | open | 3 | 0.0 | -16.4 | -4.22 | -49.21 | 24.06 | -0.68 | -44.12 | -0.87 |
| 3020 | 37 | 35.58 | Director only + Value ≥100k — hold ret_low_14d_open | Director only + Value ≥100k | low | 14 | open | 3 | 0.0 | -16.4 | -4.22 | -49.21 | 24.06 | -0.68 | -44.12 | -0.87 |
| 3021 | 37 | 35.58 | Director only + Value ≥100k — hold ret_low_30d_open | Director only + Value ≥100k | low | 30 | open | 3 | 0.0 | -16.4 | -4.22 | -49.21 | 24.06 | -0.68 | -44.12 | -0.87 |
| 3022 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_low_60d_open | CEO only + Value ≥500k | low | 60 | open | 1 | 0.0 | -16.46 | -16.46 | -16.46 | nan | nan | -16.46 | -16.46 |
| 3023 | 1 | 100.0 | CEO only + Position +10% — hold ret_low_60d_open | CEO only + Position +10% | low | 60 | open | 1 | 0.0 | -16.46 | -16.46 | -16.46 | nan | nan | -16.46 | -16.46 |
| 3024 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_low_60d_open | Near 52w high + CEO/CFO | low | 60 | open | 1 | 0.0 | -16.46 | -16.46 | -16.46 | nan | nan | -16.46 | -16.46 |
| 3025 | 51 | 20.1 | Position +30% — hold ret_low_10d_open | Position +30% | low | 10 | open | 3 | 0.0 | -16.56 | -3.28 | -49.67 | 23.88 | -0.69 | -44.12 | -2.27 |
| 3026 | 38 | 34.53 | Price < MA50 — hold ret_low_90d_news | Price < MA50 | low | 90 | news | 5 | 0.0 | -16.56 | -8.3 | -82.82 | 19.51 | -0.85 | -50.07 | -2.1 |
| 3027 | 51 | 20.1 | Position +30% — hold ret_low_14d_open | Position +30% | low | 14 | open | 3 | 0.0 | -16.58 | -3.28 | -49.74 | 23.85 | -0.7 | -44.12 | -2.34 |
| 3028 | 53 | 0.0 | Qty ≥100k shares — hold ret_low_5d_news | Qty ≥100k shares | low | 5 | news | 1 | 0.0 | -16.67 | -16.67 | -16.67 | nan | nan | -16.67 | -16.67 |
| 3029 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_low_5d_news | Small cap (≤1B) Value ≥100k | low | 5 | news | 1 | 0.0 | -16.67 | -16.67 | -16.67 | nan | nan | -16.67 | -16.67 |
| 3030 | 30 | 48.32 | Value ≥100k — hold ret_low_60d_news | Value ≥100k | low | 60 | news | 6 | 0.0 | -16.72 | -12.43 | -100.34 | 17.41 | -0.96 | -50.07 | -3.47 |
| 3031 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_low_60d_news | CEO only + Value ≥100k | low | 60 | news | 2 | 0.0 | -16.8 | -16.8 | -33.6 | 2.16 | -7.76 | -18.33 | -15.27 |
| 3032 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_low_60d_news | Price > MA50 + CEO/CFO | low | 60 | news | 2 | 0.0 | -16.8 | -16.8 | -33.6 | 2.16 | -7.76 | -18.33 | -15.27 |
| 3033 | 49 | 32.78 | CFO only — hold ret_low_90d_news | CFO only | low | 90 | news | 1 | 0.0 | -16.82 | -16.82 | -16.82 | nan | nan | -16.82 | -16.82 |
| 3034 | 48 | 32.78 | CFO + Director (combo) — hold ret_low_90d_news | CFO + Director (combo) | low | 90 | news | 1 | 0.0 | -16.82 | -16.82 | -16.82 | nan | nan | -16.82 | -16.82 |
| 3035 | 41 | 32.78 | CFO only + Value ≥50k — hold ret_low_90d_news | CFO only + Value ≥50k | low | 90 | news | 1 | 0.0 | -16.82 | -16.82 | -16.82 | nan | nan | -16.82 | -16.82 |
| 3036 | 45 | 32.78 | CFO only + Value ≥100k — hold ret_low_90d_news | CFO only + Value ≥100k | low | 90 | news | 1 | 0.0 | -16.82 | -16.82 | -16.82 | nan | nan | -16.82 | -16.82 |
| 3037 | 47 | 32.78 | CFO only + Position +10% — hold ret_low_90d_news | CFO only + Position +10% | low | 90 | news | 1 | 0.0 | -16.82 | -16.82 | -16.82 | nan | nan | -16.82 | -16.82 |
| 3038 | 46 | 32.78 | CFO only + Position +20% — hold ret_low_90d_news | CFO only + Position +20% | low | 90 | news | 1 | 0.0 | -16.82 | -16.82 | -16.82 | nan | nan | -16.82 | -16.82 |
| 3039 | 44 | 32.78 | RSI oversold (<30) — hold ret_low_90d_news | RSI oversold (<30) | low | 90 | news | 1 | 0.0 | -16.82 | -16.82 | -16.82 | nan | nan | -16.82 | -16.82 |
| 3040 | 43 | 32.78 | RSI oversold + CEO/CFO — hold ret_low_90d_news | RSI oversold + CEO/CFO | low | 90 | news | 1 | 0.0 | -16.82 | -16.82 | -16.82 | nan | nan | -16.82 | -16.82 |
| 3041 | 42 | 32.78 | RSI oversold + Value ≥100k — hold ret_low_90d_news | RSI oversold + Value ≥100k | low | 90 | news | 1 | 0.0 | -16.82 | -16.82 | -16.82 | nan | nan | -16.82 | -16.82 |
| 3042 | 40 | 33.74 | Director only + Position +10% — hold ret_low_60d_news | Director only + Position +10% | low | 60 | news | 4 | 0.0 | -16.88 | -6.92 | -67.51 | 22.21 | -0.76 | -50.07 | -3.61 |
| 3043 | 40 | 33.74 | Director only + Position +10% — hold ret_low_60d_open | Director only + Position +10% | low | 60 | open | 4 | 0.0 | -17.12 | -6.81 | -68.49 | 22.27 | -0.77 | -50.44 | -4.42 |
| 3044 | 30 | 48.32 | Value ≥100k — hold ret_low_60d_open | Value ≥100k | low | 60 | open | 6 | 0.0 | -17.18 | -11.77 | -103.06 | 17.61 | -0.98 | -50.44 | -4.22 |
| 3045 | 53 | 0.0 | Qty ≥100k shares — hold ret_low_5d_open | Qty ≥100k shares | low | 5 | open | 1 | 0.0 | -17.28 | -17.28 | -17.28 | nan | nan | -17.28 | -17.28 |
| 3046 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_low_5d_open | Small cap (≤1B) Value ≥100k | low | 5 | open | 1 | 0.0 | -17.28 | -17.28 | -17.28 | nan | nan | -17.28 | -17.28 |
| 3047 | 51 | 20.1 | Position +30% — hold ret_low_10d_news | Position +30% | low | 10 | news | 3 | 0.0 | -17.36 | -5.9 | -52.09 | 22.87 | -0.76 | -43.7 | -2.49 |
| 3048 | 21 | 53.67 | Qty ≥5k shares — hold ret_low_90d_open | Qty ≥5k shares | low | 90 | open | 6 | 0.0 | -17.38 | -12.46 | -104.28 | 18.02 | -0.96 | -50.44 | -1.15 |
| 3049 | 20 | 53.67 | Qty ≥10k shares — hold ret_low_90d_open | Qty ≥10k shares | low | 90 | open | 6 | 0.0 | -17.38 | -12.46 | -104.28 | 18.02 | -0.96 | -50.44 | -1.15 |
| 3050 | 51 | 20.1 | Position +30% — hold ret_low_14d_news | Position +30% | low | 14 | news | 3 | 0.0 | -17.39 | -5.9 | -52.16 | 22.85 | -0.76 | -43.7 | -2.56 |
| 3051 | 21 | 53.67 | Qty ≥5k shares — hold ret_low_90d_news | Qty ≥5k shares | low | 90 | news | 6 | 0.0 | -17.43 | -13.25 | -104.59 | 17.78 | -0.98 | -50.07 | -2.1 |
| 3052 | 20 | 53.67 | Qty ≥10k shares — hold ret_low_90d_news | Qty ≥10k shares | low | 90 | news | 6 | 0.0 | -17.43 | -13.25 | -104.59 | 17.78 | -0.98 | -50.07 | -2.1 |
| 3053 | 39 | 34.48 | Position +20% — hold ret_low_60d_open | Position +20% | low | 60 | open | 4 | 0.0 | -17.51 | -7.58 | -70.03 | 22.01 | -0.8 | -50.44 | -4.42 |
| 3054 | 51 | 20.1 | Position +30% — hold ret_low_30d_open | Position +30% | low | 30 | open | 3 | 0.0 | -17.55 | -5.25 | -52.65 | 23.03 | -0.76 | -44.12 | -3.28 |
| 3055 | 39 | 34.48 | Position +20% — hold ret_low_60d_news | Position +20% | low | 60 | news | 4 | 0.0 | -17.89 | -8.95 | -71.57 | 21.61 | -0.83 | -50.07 | -3.61 |
| 3056 | 53 | 0.0 | Qty ≥100k shares — hold ret_mean_14d_news | Qty ≥100k shares | mean | 14 | news | 1 | 0.0 | -18.03 | -18.03 | -18.03 | nan | nan | -18.03 | -18.03 |
| 3057 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_mean_14d_news | Small cap (≤1B) Value ≥100k | mean | 14 | news | 1 | 0.0 | -18.03 | -18.03 | -18.03 | nan | nan | -18.03 | -18.03 |
| 3058 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_low_60d_news | Large cap (≥3B) CEO/CFO | low | 60 | news | 1 | 0.0 | -18.33 | -18.33 | -18.33 | nan | nan | -18.33 | -18.33 |
| 3059 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_low_60d_news | Large cap (≥5B) CEO/CFO | low | 60 | news | 1 | 0.0 | -18.33 | -18.33 | -18.33 | nan | nan | -18.33 | -18.33 |
| 3060 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_low_60d_news | Large cap (≥10B) CEO/CFO | low | 60 | news | 1 | 0.0 | -18.33 | -18.33 | -18.33 | nan | nan | -18.33 | -18.33 |
| 3061 | 51 | 20.1 | Position +30% — hold ret_low_30d_news | Position +30% | low | 30 | news | 3 | 0.0 | -18.35 | -5.9 | -55.06 | 21.95 | -0.84 | -43.7 | -5.46 |
| 3062 | 40 | 33.74 | Director only + Position +10% — hold ret_low_90d_news | Director only + Position +10% | low | 90 | news | 4 | 0.0 | -18.39 | -8.98 | -73.57 | 21.19 | -0.87 | -50.07 | -5.53 |
| 3063 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_low_60d_open | CEO only + Value ≥100k | low | 60 | open | 2 | 0.0 | -18.45 | -18.45 | -36.91 | 2.82 | -6.54 | -20.45 | -16.46 |
| 3064 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_low_60d_open | Price > MA50 + CEO/CFO | low | 60 | open | 2 | 0.0 | -18.45 | -18.45 | -36.91 | 2.82 | -6.54 | -20.45 | -16.46 |
| 3065 | 40 | 33.74 | Director only + Position +10% — hold ret_low_90d_open | Director only + Position +10% | low | 90 | open | 4 | 0.0 | -18.62 | -9.26 | -74.49 | 21.31 | -0.87 | -50.44 | -5.53 |
| 3066 | 53 | 0.0 | Qty ≥100k shares — hold ret_mean_14d_open | Qty ≥100k shares | mean | 14 | open | 1 | 0.0 | -18.64 | -18.64 | -18.64 | nan | nan | -18.64 | -18.64 |
| 3067 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_mean_14d_open | Small cap (≤1B) Value ≥100k | mean | 14 | open | 1 | 0.0 | -18.64 | -18.64 | -18.64 | nan | nan | -18.64 | -18.64 |
| 3068 | 32 | 44.63 | Position +10% — hold ret_low_90d_open | Position +10% | low | 90 | open | 6 | 0.0 | -18.76 | -12.46 | -112.54 | 16.75 | -1.12 | -50.44 | -5.53 |
| 3069 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_low_90d_open | Large cap (≥2B) CEO/CFO | low | 90 | open | 2 | 0.0 | -18.76 | -18.77 | -37.53 | 6.03 | -3.11 | -23.03 | -14.5 |
| 3070 | 32 | 44.63 | Position +10% — hold ret_low_90d_news | Position +10% | low | 90 | news | 6 | 0.0 | -18.81 | -13.25 | -112.85 | 16.52 | -1.14 | -50.07 | -5.53 |
| 3071 | 34 | 41.56 | Large cap (≥2B) CEO/CFO — hold ret_low_90d_news | Large cap (≥2B) CEO/CFO | low | 90 | news | 2 | 0.0 | -18.9 | -18.9 | -37.8 | 2.94 | -6.43 | -20.98 | -16.82 |
| 3072 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_low_90d_open | Mid cap (1B–10B) CEO/CFO | low | 90 | open | 2 | 0.0 | -19.02 | -19.02 | -38.05 | 6.4 | -2.97 | -23.55 | -14.5 |
| 3073 | 37 | 35.58 | Director only + Value ≥100k — hold ret_low_60d_news | Director only + Value ≥100k | low | 60 | news | 3 | 0.0 | -19.05 | -3.61 | -57.15 | 26.86 | -0.71 | -50.07 | -3.47 |
| 3074 | 53 | 0.0 | Qty ≥100k shares — hold ret_mean_30d_news | Qty ≥100k shares | mean | 30 | news | 1 | 0.0 | -19.4 | -19.4 | -19.4 | nan | nan | -19.4 | -19.4 |
| 3075 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_mean_30d_news | Small cap (≤1B) Value ≥100k | mean | 30 | news | 1 | 0.0 | -19.4 | -19.4 | -19.4 | nan | nan | -19.4 | -19.4 |
| 3076 | 35 | 40.48 | Value ≥500k — hold ret_low_60d_open | Value ≥500k | low | 60 | open | 4 | 0.0 | -19.55 | -11.77 | -78.19 | 21.25 | -0.92 | -50.44 | -4.22 |
| 3077 | 35 | 40.48 | Value ≥500k — hold ret_low_60d_news | Value ≥500k | low | 60 | news | 4 | 0.0 | -19.6 | -12.43 | -78.4 | 20.88 | -0.94 | -50.07 | -3.47 |
| 3078 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_low_10d_news | Far 52w high + Value ≥100k | low | 10 | news | 3 | 0.0 | -19.63 | -9.28 | -58.88 | 20.92 | -0.94 | -43.7 | -5.9 |
| 3079 | 13 | 66.39 | Mid cap (1B–10B) CEO/CFO — hold ret_low_90d_news | Mid cap (1B–10B) CEO/CFO | low | 90 | news | 2 | 0.0 | -19.64 | -19.64 | -39.28 | 3.99 | -4.92 | -22.46 | -16.82 |
| 3080 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_low_10d_open | Far 52w high + Value ≥100k | low | 10 | open | 3 | 0.0 | -19.68 | -11.63 | -59.03 | 21.58 | -0.91 | -44.12 | -3.28 |
| 3081 | 37 | 35.58 | Director only + Value ≥100k — hold ret_low_60d_open | Director only + Value ≥100k | low | 60 | open | 3 | 0.0 | -19.69 | -4.42 | -59.08 | 26.63 | -0.74 | -50.44 | -4.22 |
| 3082 | 53 | 0.0 | Qty ≥100k shares — hold ret_mean_30d_open | Qty ≥100k shares | mean | 30 | open | 1 | 0.0 | -19.99 | -19.99 | -19.99 | nan | nan | -19.99 | -19.99 |
| 3083 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_mean_30d_open | Small cap (≤1B) Value ≥100k | mean | 30 | open | 1 | 0.0 | -19.99 | -19.99 | -19.99 | nan | nan | -19.99 | -19.99 |
| 3084 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_low_90d_news | CEO/CFO + Value ≥100k | low | 90 | news | 3 | 0.0 | -20.09 | -20.98 | -60.26 | 2.92 | -6.87 | -22.46 | -16.82 |
| 3085 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_low_90d_news | Large cap (≥750M) CEO/CFO | low | 90 | news | 3 | 0.0 | -20.09 | -20.98 | -60.26 | 2.92 | -6.87 | -22.46 | -16.82 |
| 3086 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_low_90d_news | Large cap (≥1B) CEO/CFO | low | 90 | news | 3 | 0.0 | -20.09 | -20.98 | -60.26 | 2.92 | -6.87 | -22.46 | -16.82 |
| 3087 | 18 | 61.05 | CEO/CFO + Value ≥100k — hold ret_low_90d_open | CEO/CFO + Value ≥100k | low | 90 | open | 3 | 0.0 | -20.36 | -23.03 | -61.08 | 5.08 | -4.01 | -23.55 | -14.5 |
| 3088 | 16 | 61.05 | Large cap (≥750M) CEO/CFO — hold ret_low_90d_open | Large cap (≥750M) CEO/CFO | low | 90 | open | 3 | 0.0 | -20.36 | -23.03 | -61.08 | 5.08 | -4.01 | -23.55 | -14.5 |
| 3089 | 17 | 61.05 | Large cap (≥1B) CEO/CFO — hold ret_low_90d_open | Large cap (≥1B) CEO/CFO | low | 90 | open | 3 | 0.0 | -20.36 | -23.03 | -61.08 | 5.08 | -4.01 | -23.55 | -14.5 |
| 3090 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_low_14d_news | Far 52w high + Value ≥100k | low | 14 | news | 3 | 0.0 | -20.41 | -11.62 | -61.22 | 20.37 | -1.0 | -43.7 | -5.9 |
| 3091 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_low_30d_news | Far 52w high + Value ≥100k | low | 30 | news | 3 | 0.0 | -20.41 | -11.62 | -61.22 | 20.37 | -1.0 | -43.7 | -5.9 |
| 3092 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_low_14d_open | Far 52w high + Value ≥100k | low | 14 | open | 3 | 0.0 | -20.44 | -13.91 | -61.31 | 21.19 | -0.96 | -44.12 | -3.28 |
| 3093 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_low_30d_open | Far 52w high + Value ≥100k | low | 30 | open | 3 | 0.0 | -20.44 | -13.91 | -61.31 | 21.19 | -0.96 | -44.12 | -3.28 |
| 3094 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_low_60d_open | Large cap (≥3B) CEO/CFO | low | 60 | open | 1 | 0.0 | -20.45 | -20.45 | -20.45 | nan | nan | -20.45 | -20.45 |
| 3095 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_low_60d_open | Large cap (≥5B) CEO/CFO | low | 60 | open | 1 | 0.0 | -20.45 | -20.45 | -20.45 | nan | nan | -20.45 | -20.45 |
| 3096 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_low_60d_open | Large cap (≥10B) CEO/CFO | low | 60 | open | 1 | 0.0 | -20.45 | -20.45 | -20.45 | nan | nan | -20.45 | -20.45 |
| 3097 | 30 | 48.32 | Value ≥100k — hold ret_low_90d_news | Value ≥100k | low | 90 | news | 6 | 0.0 | -20.58 | -18.9 | -123.47 | 16.12 | -1.28 | -50.07 | -3.47 |
| 3098 | 39 | 34.48 | Position +20% — hold ret_low_90d_open | Position +20% | low | 90 | open | 4 | 0.0 | -20.86 | -12.46 | -83.46 | 19.89 | -1.05 | -50.44 | -8.1 |
| 3099 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_low_90d_news | Large cap (≥3B) CEO/CFO | low | 90 | news | 1 | 0.0 | -20.98 | -20.98 | -20.98 | nan | nan | -20.98 | -20.98 |
| 3100 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_low_90d_news | Large cap (≥5B) CEO/CFO | low | 90 | news | 1 | 0.0 | -20.98 | -20.98 | -20.98 | nan | nan | -20.98 | -20.98 |
| 3101 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_low_90d_news | Large cap (≥10B) CEO/CFO | low | 90 | news | 1 | 0.0 | -20.98 | -20.98 | -20.98 | nan | nan | -20.98 | -20.98 |
| 3102 | 30 | 48.32 | Value ≥100k — hold ret_low_90d_open | Value ≥100k | low | 90 | open | 6 | 0.0 | -21.03 | -18.77 | -126.16 | 16.21 | -1.3 | -50.44 | -4.22 |
| 3103 | 37 | 35.58 | Director only + Value ≥100k — hold ret_low_90d_news | Director only + Value ≥100k | low | 90 | news | 3 | 0.0 | -21.07 | -9.67 | -63.21 | 25.31 | -0.83 | -50.07 | -3.47 |
| 3104 | 26 | 50.0 | Qty ≥50k shares — hold ret_low_10d_news | Qty ≥50k shares | low | 10 | news | 2 | 50.0 | -21.14 | -21.14 | -42.27 | 31.91 | -0.66 | -43.7 | 1.43 |
| 3105 | 27 | 50.0 | Value ≥1M — hold ret_low_10d_news | Value ≥1M | low | 10 | news | 2 | 50.0 | -21.14 | -21.14 | -42.27 | 31.91 | -0.66 | -43.7 | 1.43 |
| 3106 | 26 | 50.0 | Qty ≥50k shares — hold ret_low_14d_news | Qty ≥50k shares | low | 14 | news | 2 | 50.0 | -21.14 | -21.14 | -42.27 | 31.91 | -0.66 | -43.7 | 1.43 |
| 3107 | 27 | 50.0 | Value ≥1M — hold ret_low_14d_news | Value ≥1M | low | 14 | news | 2 | 50.0 | -21.14 | -21.14 | -42.27 | 31.91 | -0.66 | -43.7 | 1.43 |
| 3108 | 26 | 50.0 | Qty ≥50k shares — hold ret_low_30d_news | Qty ≥50k shares | low | 30 | news | 2 | 50.0 | -21.14 | -21.14 | -42.27 | 31.91 | -0.66 | -43.7 | 1.43 |
| 3109 | 27 | 50.0 | Value ≥1M — hold ret_low_30d_news | Value ≥1M | low | 30 | news | 2 | 50.0 | -21.14 | -21.14 | -42.27 | 31.91 | -0.66 | -43.7 | 1.43 |
| 3110 | 39 | 34.48 | Position +20% — hold ret_low_90d_news | Position +20% | low | 90 | news | 4 | 0.0 | -21.22 | -13.25 | -84.86 | 19.6 | -1.08 | -50.07 | -8.3 |
| 3111 | 37 | 35.58 | Director only + Value ≥100k — hold ret_low_90d_open | Director only + Value ≥100k | low | 90 | open | 3 | 0.0 | -21.69 | -10.42 | -65.08 | 25.09 | -0.86 | -50.44 | -4.22 |
| 3112 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_low_90d_news | CEO only + Value ≥100k | low | 90 | news | 2 | 0.0 | -21.72 | -21.72 | -43.44 | 1.05 | -20.75 | -22.46 | -20.98 |
| 3113 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_low_90d_news | Price > MA50 + CEO/CFO | low | 90 | news | 2 | 0.0 | -21.72 | -21.72 | -43.44 | 1.05 | -20.75 | -22.46 | -20.98 |
| 3114 | 51 | 20.1 | Position +30% — hold ret_low_60d_open | Position +30% | low | 60 | open | 3 | 0.0 | -21.87 | -8.1 | -65.61 | 24.75 | -0.88 | -50.44 | -7.07 |
| 3115 | 26 | 50.0 | Qty ≥50k shares — hold ret_low_10d_open | Qty ≥50k shares | low | 10 | open | 2 | 0.0 | -22.06 | -22.06 | -44.12 | 31.2 | -0.71 | -44.12 | 0.0 |
| 3116 | 27 | 50.0 | Value ≥1M — hold ret_low_10d_open | Value ≥1M | low | 10 | open | 2 | 0.0 | -22.06 | -22.06 | -44.12 | 31.2 | -0.71 | -44.12 | 0.0 |
| 3117 | 26 | 50.0 | Qty ≥50k shares — hold ret_low_14d_open | Qty ≥50k shares | low | 14 | open | 2 | 0.0 | -22.06 | -22.06 | -44.12 | 31.2 | -0.71 | -44.12 | 0.0 |
| 3118 | 27 | 50.0 | Value ≥1M — hold ret_low_14d_open | Value ≥1M | low | 14 | open | 2 | 0.0 | -22.06 | -22.06 | -44.12 | 31.2 | -0.71 | -44.12 | 0.0 |
| 3119 | 26 | 50.0 | Qty ≥50k shares — hold ret_low_30d_open | Qty ≥50k shares | low | 30 | open | 2 | 0.0 | -22.06 | -22.06 | -44.12 | 31.2 | -0.71 | -44.12 | 0.0 |
| 3120 | 27 | 50.0 | Value ≥1M — hold ret_low_30d_open | Value ≥1M | low | 30 | open | 2 | 0.0 | -22.06 | -22.06 | -44.12 | 31.2 | -0.71 | -44.12 | 0.0 |
| 3121 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_low_90d_news | CEO only + Value ≥500k | low | 90 | news | 1 | 0.0 | -22.46 | -22.46 | -22.46 | nan | nan | -22.46 | -22.46 |
| 3122 | 1 | 100.0 | CEO only + Position +10% — hold ret_low_90d_news | CEO only + Position +10% | low | 90 | news | 1 | 0.0 | -22.46 | -22.46 | -22.46 | nan | nan | -22.46 | -22.46 |
| 3123 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_low_90d_news | Near 52w high + CEO/CFO | low | 90 | news | 1 | 0.0 | -22.46 | -22.46 | -22.46 | nan | nan | -22.46 | -22.46 |
| 3124 | 53 | 0.0 | Qty ≥100k shares — hold ret_low_7d_news | Qty ≥100k shares | low | 7 | news | 1 | 0.0 | -22.52 | -22.52 | -22.52 | nan | nan | -22.52 | -22.52 |
| 3125 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_low_7d_news | Small cap (≤1B) Value ≥100k | low | 7 | news | 1 | 0.0 | -22.52 | -22.52 | -22.52 | nan | nan | -22.52 | -22.52 |
| 3126 | 51 | 20.1 | Position +30% — hold ret_low_60d_news | Position +30% | low | 60 | news | 3 | 0.0 | -22.65 | -9.59 | -67.96 | 23.75 | -0.95 | -50.07 | -8.3 |
| 3127 | 25 | 50.35 | Large cap (≥3B) CEO/CFO — hold ret_low_90d_open | Large cap (≥3B) CEO/CFO | low | 90 | open | 1 | 0.0 | -23.03 | -23.03 | -23.03 | nan | nan | -23.03 | -23.03 |
| 3128 | 24 | 50.35 | Large cap (≥5B) CEO/CFO — hold ret_low_90d_open | Large cap (≥5B) CEO/CFO | low | 90 | open | 1 | 0.0 | -23.03 | -23.03 | -23.03 | nan | nan | -23.03 | -23.03 |
| 3129 | 23 | 50.35 | Large cap (≥10B) CEO/CFO — hold ret_low_90d_open | Large cap (≥10B) CEO/CFO | low | 90 | open | 1 | 0.0 | -23.03 | -23.03 | -23.03 | nan | nan | -23.03 | -23.03 |
| 3130 | 53 | 0.0 | Qty ≥100k shares — hold ret_low_7d_open | Qty ≥100k shares | low | 7 | open | 1 | 0.0 | -23.09 | -23.09 | -23.09 | nan | nan | -23.09 | -23.09 |
| 3131 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_low_7d_open | Small cap (≤1B) Value ≥100k | low | 7 | open | 1 | 0.0 | -23.09 | -23.09 | -23.09 | nan | nan | -23.09 | -23.09 |
| 3132 | 35 | 40.48 | Value ≥500k — hold ret_low_90d_open | Value ≥500k | low | 90 | open | 4 | 0.0 | -23.18 | -19.02 | -92.71 | 19.82 | -1.17 | -50.44 | -4.22 |
| 3133 | 35 | 40.48 | Value ≥500k — hold ret_low_90d_news | Value ≥500k | low | 90 | news | 4 | 0.0 | -23.2 | -19.64 | -92.82 | 19.6 | -1.18 | -50.07 | -3.47 |
| 3134 | 7 | 75.17 | CEO only + Value ≥100k — hold ret_low_90d_open | CEO only + Value ≥100k | low | 90 | open | 2 | 0.0 | -23.29 | -23.29 | -46.58 | 0.37 | -63.34 | -23.55 | -23.03 |
| 3135 | 8 | 75.17 | Price > MA50 + CEO/CFO — hold ret_low_90d_open | Price > MA50 + CEO/CFO | low | 90 | open | 2 | 0.0 | -23.29 | -23.29 | -46.58 | 0.37 | -63.34 | -23.55 | -23.03 |
| 3136 | 2 | 100.0 | CEO only + Value ≥500k — hold ret_low_90d_open | CEO only + Value ≥500k | low | 90 | open | 1 | 0.0 | -23.55 | -23.55 | -23.55 | nan | nan | -23.55 | -23.55 |
| 3137 | 1 | 100.0 | CEO only + Position +10% — hold ret_low_90d_open | CEO only + Position +10% | low | 90 | open | 1 | 0.0 | -23.55 | -23.55 | -23.55 | nan | nan | -23.55 | -23.55 |
| 3138 | 3 | 100.0 | Near 52w high + CEO/CFO — hold ret_low_90d_open | Near 52w high + CEO/CFO | low | 90 | open | 1 | 0.0 | -23.55 | -23.55 | -23.55 | nan | nan | -23.55 | -23.55 |
| 3139 | 51 | 20.1 | Position +30% — hold ret_low_90d_open | Position +30% | low | 90 | open | 3 | 0.0 | -24.35 | -14.5 | -73.04 | 22.82 | -1.07 | -50.44 | -8.1 |
| 3140 | 51 | 20.1 | Position +30% — hold ret_low_90d_news | Position +30% | low | 90 | news | 3 | 0.0 | -25.06 | -16.82 | -75.19 | 22.07 | -1.14 | -50.07 | -8.3 |
| 3141 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_low_60d_open | Far 52w high + Value ≥100k | low | 60 | open | 3 | 0.0 | -25.99 | -20.45 | -77.96 | 22.21 | -1.17 | -50.44 | -7.07 |
| 3142 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_low_60d_news | Far 52w high + Value ≥100k | low | 60 | news | 3 | 0.0 | -26.0 | -18.33 | -77.99 | 21.3 | -1.22 | -50.07 | -9.59 |
| 3143 | 53 | 0.0 | Qty ≥100k shares — hold ret_mean_90d_news | Qty ≥100k shares | mean | 90 | news | 1 | 0.0 | -26.12 | -26.12 | -26.12 | nan | nan | -26.12 | -26.12 |
| 3144 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_mean_90d_news | Small cap (≤1B) Value ≥100k | mean | 90 | news | 1 | 0.0 | -26.12 | -26.12 | -26.12 | nan | nan | -26.12 | -26.12 |
| 3145 | 53 | 0.0 | Qty ≥100k shares — hold ret_mean_90d_open | Qty ≥100k shares | mean | 90 | open | 1 | 0.0 | -26.66 | -26.66 | -26.66 | nan | nan | -26.66 | -26.66 |
| 3146 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_mean_90d_open | Small cap (≤1B) Value ≥100k | mean | 90 | open | 1 | 0.0 | -26.66 | -26.66 | -26.66 | nan | nan | -26.66 | -26.66 |
| 3147 | 53 | 0.0 | Qty ≥100k shares — hold ret_mean_60d_news | Qty ≥100k shares | mean | 60 | news | 1 | 0.0 | -28.39 | -28.39 | -28.39 | nan | nan | -28.39 | -28.39 |
| 3148 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_mean_60d_news | Small cap (≤1B) Value ≥100k | mean | 60 | news | 1 | 0.0 | -28.39 | -28.39 | -28.39 | nan | nan | -28.39 | -28.39 |
| 3149 | 53 | 0.0 | Qty ≥100k shares — hold ret_mean_60d_open | Qty ≥100k shares | mean | 60 | open | 1 | 0.0 | -28.92 | -28.92 | -28.92 | nan | nan | -28.92 | -28.92 |
| 3150 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_mean_60d_open | Small cap (≤1B) Value ≥100k | mean | 60 | open | 1 | 0.0 | -28.92 | -28.92 | -28.92 | nan | nan | -28.92 | -28.92 |
| 3151 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_low_90d_news | Far 52w high + Value ≥100k | low | 90 | news | 3 | 0.0 | -29.29 | -20.98 | -87.87 | 18.12 | -1.62 | -50.07 | -16.82 |
| 3152 | 50 | 27.71 | Far 52w high + Value ≥100k — hold ret_low_90d_open | Far 52w high + Value ≥100k | low | 90 | open | 3 | 0.0 | -29.32 | -23.03 | -87.97 | 18.78 | -1.56 | -50.44 | -14.5 |
| 3153 | 26 | 50.0 | Qty ≥50k shares — hold ret_low_60d_news | Qty ≥50k shares | low | 60 | news | 2 | 0.0 | -32.67 | -32.67 | -65.34 | 24.61 | -1.33 | -50.07 | -15.27 |
| 3154 | 27 | 50.0 | Value ≥1M — hold ret_low_60d_news | Value ≥1M | low | 60 | news | 2 | 0.0 | -32.67 | -32.67 | -65.34 | 24.61 | -1.33 | -50.07 | -15.27 |
| 3155 | 26 | 50.0 | Qty ≥50k shares — hold ret_low_60d_open | Qty ≥50k shares | low | 60 | open | 2 | 0.0 | -33.45 | -33.45 | -66.9 | 24.03 | -1.39 | -50.44 | -16.46 |
| 3156 | 27 | 50.0 | Value ≥1M — hold ret_low_60d_open | Value ≥1M | low | 60 | open | 2 | 0.0 | -33.45 | -33.45 | -66.9 | 24.03 | -1.39 | -50.44 | -16.46 |
| 3157 | 26 | 50.0 | Qty ≥50k shares — hold ret_low_90d_news | Qty ≥50k shares | low | 90 | news | 2 | 0.0 | -36.26 | -36.27 | -72.53 | 19.52 | -1.86 | -50.07 | -22.46 |
| 3158 | 27 | 50.0 | Value ≥1M — hold ret_low_90d_news | Value ≥1M | low | 90 | news | 2 | 0.0 | -36.26 | -36.27 | -72.53 | 19.52 | -1.86 | -50.07 | -22.46 |
| 3159 | 26 | 50.0 | Qty ≥50k shares — hold ret_low_90d_open | Qty ≥50k shares | low | 90 | open | 2 | 0.0 | -36.99 | -36.99 | -73.99 | 19.01 | -1.95 | -50.44 | -23.55 |
| 3160 | 27 | 50.0 | Value ≥1M — hold ret_low_90d_open | Value ≥1M | low | 90 | open | 2 | 0.0 | -36.99 | -36.99 | -73.99 | 19.01 | -1.95 | -50.44 | -23.55 |
| 3161 | 53 | 0.0 | Qty ≥100k shares — hold ret_low_10d_news | Qty ≥100k shares | low | 10 | news | 1 | 0.0 | -43.7 | -43.7 | -43.7 | nan | nan | -43.7 | -43.7 |
| 3162 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_low_10d_news | Small cap (≤1B) Value ≥100k | low | 10 | news | 1 | 0.0 | -43.7 | -43.7 | -43.7 | nan | nan | -43.7 | -43.7 |
| 3163 | 53 | 0.0 | Qty ≥100k shares — hold ret_low_14d_news | Qty ≥100k shares | low | 14 | news | 1 | 0.0 | -43.7 | -43.7 | -43.7 | nan | nan | -43.7 | -43.7 |
| 3164 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_low_14d_news | Small cap (≤1B) Value ≥100k | low | 14 | news | 1 | 0.0 | -43.7 | -43.7 | -43.7 | nan | nan | -43.7 | -43.7 |
| 3165 | 53 | 0.0 | Qty ≥100k shares — hold ret_low_30d_news | Qty ≥100k shares | low | 30 | news | 1 | 0.0 | -43.7 | -43.7 | -43.7 | nan | nan | -43.7 | -43.7 |
| 3166 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_low_30d_news | Small cap (≤1B) Value ≥100k | low | 30 | news | 1 | 0.0 | -43.7 | -43.7 | -43.7 | nan | nan | -43.7 | -43.7 |
| 3167 | 53 | 0.0 | Qty ≥100k shares — hold ret_low_10d_open | Qty ≥100k shares | low | 10 | open | 1 | 0.0 | -44.12 | -44.12 | -44.12 | nan | nan | -44.12 | -44.12 |
| 3168 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_low_10d_open | Small cap (≤1B) Value ≥100k | low | 10 | open | 1 | 0.0 | -44.12 | -44.12 | -44.12 | nan | nan | -44.12 | -44.12 |
| 3169 | 53 | 0.0 | Qty ≥100k shares — hold ret_low_14d_open | Qty ≥100k shares | low | 14 | open | 1 | 0.0 | -44.12 | -44.12 | -44.12 | nan | nan | -44.12 | -44.12 |
| 3170 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_low_14d_open | Small cap (≤1B) Value ≥100k | low | 14 | open | 1 | 0.0 | -44.12 | -44.12 | -44.12 | nan | nan | -44.12 | -44.12 |
| 3171 | 53 | 0.0 | Qty ≥100k shares — hold ret_low_30d_open | Qty ≥100k shares | low | 30 | open | 1 | 0.0 | -44.12 | -44.12 | -44.12 | nan | nan | -44.12 | -44.12 |
| 3172 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_low_30d_open | Small cap (≤1B) Value ≥100k | low | 30 | open | 1 | 0.0 | -44.12 | -44.12 | -44.12 | nan | nan | -44.12 | -44.12 |
| 3173 | 53 | 0.0 | Qty ≥100k shares — hold ret_low_60d_news | Qty ≥100k shares | low | 60 | news | 1 | 0.0 | -50.07 | -50.07 | -50.07 | nan | nan | -50.07 | -50.07 |
| 3174 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_low_60d_news | Small cap (≤1B) Value ≥100k | low | 60 | news | 1 | 0.0 | -50.07 | -50.07 | -50.07 | nan | nan | -50.07 | -50.07 |
| 3175 | 53 | 0.0 | Qty ≥100k shares — hold ret_low_90d_news | Qty ≥100k shares | low | 90 | news | 1 | 0.0 | -50.07 | -50.07 | -50.07 | nan | nan | -50.07 | -50.07 |
| 3176 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_low_90d_news | Small cap (≤1B) Value ≥100k | low | 90 | news | 1 | 0.0 | -50.07 | -50.07 | -50.07 | nan | nan | -50.07 | -50.07 |
| 3177 | 53 | 0.0 | Qty ≥100k shares — hold ret_low_60d_open | Qty ≥100k shares | low | 60 | open | 1 | 0.0 | -50.44 | -50.44 | -50.44 | nan | nan | -50.44 | -50.44 |
| 3178 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_low_60d_open | Small cap (≤1B) Value ≥100k | low | 60 | open | 1 | 0.0 | -50.44 | -50.44 | -50.44 | nan | nan | -50.44 | -50.44 |
| 3179 | 53 | 0.0 | Qty ≥100k shares — hold ret_low_90d_open | Qty ≥100k shares | low | 90 | open | 1 | 0.0 | -50.44 | -50.44 | -50.44 | nan | nan | -50.44 | -50.44 |
| 3180 | 52 | 0.0 | Small cap (≤1B) Value ≥100k — hold ret_low_90d_open | Small cap (≤1B) Value ≥100k | low | 90 | open | 1 | 0.0 | -50.44 | -50.44 | -50.44 | nan | nan | -50.44 | -50.44 |
| 3181 | 58 | nan | CEO + CFO (combo) — hold ret_high_1d_open | CEO + CFO (combo) | high | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3182 | 58 | nan | CEO + CFO (combo) — hold ret_high_1d_news | CEO + CFO (combo) | high | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3183 | 54 | nan | 10% Owner — hold ret_high_1d_open | 10% Owner | high | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3184 | 54 | nan | 10% Owner — hold ret_high_1d_news | 10% Owner | high | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3185 | 57 | nan | 10% Owner + Value ≥500k — hold ret_high_1d_open | 10% Owner + Value ≥500k | high | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3186 | 57 | nan | 10% Owner + Value ≥500k — hold ret_high_1d_news | 10% Owner + Value ≥500k | high | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3187 | 59 | nan | CEO only + Position +20% — hold ret_high_1d_open | CEO only + Position +20% | high | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3188 | 59 | nan | CEO only + Position +20% — hold ret_high_1d_news | CEO only + Position +20% | high | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3189 | 55 | nan | 10% Owner + Position +10% — hold ret_high_1d_open | 10% Owner + Position +10% | high | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3190 | 55 | nan | 10% Owner + Position +10% — hold ret_high_1d_news | 10% Owner + Position +10% | high | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3191 | 56 | nan | 10% Owner + Position +20% — hold ret_high_1d_open | 10% Owner + Position +20% | high | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3192 | 56 | nan | 10% Owner + Position +20% — hold ret_high_1d_news | 10% Owner + Position +20% | high | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3193 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_high_1d_open | CEO+CFO (combo) + Position +10% | high | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3194 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_high_1d_news | CEO+CFO (combo) + Position +10% | high | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3195 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_high_1d_open | CEO+CFO (combo) + Position +20% | high | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3196 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_high_1d_news | CEO+CFO (combo) + Position +20% | high | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3197 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_high_1d_open | Micro cap (≤50M) CEO/CFO | high | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3198 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_high_1d_news | Micro cap (≤50M) CEO/CFO | high | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3199 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_high_1d_open | Micro cap (≤100M) CEO/CFO | high | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3200 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_high_1d_news | Micro cap (≤100M) CEO/CFO | high | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3201 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_high_1d_open | Micro cap (≤250M) CEO/CFO | high | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3202 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_high_1d_news | Micro cap (≤250M) CEO/CFO | high | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3203 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_high_1d_open | Large cap (≥20B) CEO/CFO | high | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3204 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_high_1d_news | Large cap (≥20B) CEO/CFO | high | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3205 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_high_1d_open | Large cap (≥50B) CEO/CFO | high | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3206 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_high_1d_news | Large cap (≥50B) CEO/CFO | high | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3207 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_high_1d_open | Large cap (≥100B) CEO/CFO | high | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3208 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_high_1d_news | Large cap (≥100B) CEO/CFO | high | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3209 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_high_1d_open | Micro cap (≤50M) Value ≥100k | high | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3210 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_high_1d_news | Micro cap (≤50M) Value ≥100k | high | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3211 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_high_1d_open | Micro cap (≤100M) Value ≥100k | high | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3212 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_high_1d_news | Micro cap (≤100M) Value ≥100k | high | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3213 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_high_1d_open | Micro cap (≤250M) Value ≥100k | high | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3214 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_high_1d_news | Micro cap (≤250M) Value ≥100k | high | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3215 | 58 | nan | CEO + CFO (combo) — hold ret_low_1d_open | CEO + CFO (combo) | low | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3216 | 58 | nan | CEO + CFO (combo) — hold ret_low_1d_news | CEO + CFO (combo) | low | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3217 | 54 | nan | 10% Owner — hold ret_low_1d_open | 10% Owner | low | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3218 | 54 | nan | 10% Owner — hold ret_low_1d_news | 10% Owner | low | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3219 | 57 | nan | 10% Owner + Value ≥500k — hold ret_low_1d_open | 10% Owner + Value ≥500k | low | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3220 | 57 | nan | 10% Owner + Value ≥500k — hold ret_low_1d_news | 10% Owner + Value ≥500k | low | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3221 | 59 | nan | CEO only + Position +20% — hold ret_low_1d_open | CEO only + Position +20% | low | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3222 | 59 | nan | CEO only + Position +20% — hold ret_low_1d_news | CEO only + Position +20% | low | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3223 | 55 | nan | 10% Owner + Position +10% — hold ret_low_1d_open | 10% Owner + Position +10% | low | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3224 | 55 | nan | 10% Owner + Position +10% — hold ret_low_1d_news | 10% Owner + Position +10% | low | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3225 | 56 | nan | 10% Owner + Position +20% — hold ret_low_1d_open | 10% Owner + Position +20% | low | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3226 | 56 | nan | 10% Owner + Position +20% — hold ret_low_1d_news | 10% Owner + Position +20% | low | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3227 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_low_1d_open | CEO+CFO (combo) + Position +10% | low | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3228 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_low_1d_news | CEO+CFO (combo) + Position +10% | low | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3229 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_low_1d_open | CEO+CFO (combo) + Position +20% | low | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3230 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_low_1d_news | CEO+CFO (combo) + Position +20% | low | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3231 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_low_1d_open | Micro cap (≤50M) CEO/CFO | low | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3232 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_low_1d_news | Micro cap (≤50M) CEO/CFO | low | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3233 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_low_1d_open | Micro cap (≤100M) CEO/CFO | low | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3234 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_low_1d_news | Micro cap (≤100M) CEO/CFO | low | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3235 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_low_1d_open | Micro cap (≤250M) CEO/CFO | low | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3236 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_low_1d_news | Micro cap (≤250M) CEO/CFO | low | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3237 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_low_1d_open | Large cap (≥20B) CEO/CFO | low | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3238 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_low_1d_news | Large cap (≥20B) CEO/CFO | low | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3239 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_low_1d_open | Large cap (≥50B) CEO/CFO | low | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3240 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_low_1d_news | Large cap (≥50B) CEO/CFO | low | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3241 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_low_1d_open | Large cap (≥100B) CEO/CFO | low | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3242 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_low_1d_news | Large cap (≥100B) CEO/CFO | low | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3243 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_low_1d_open | Micro cap (≤50M) Value ≥100k | low | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3244 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_low_1d_news | Micro cap (≤50M) Value ≥100k | low | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3245 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_low_1d_open | Micro cap (≤100M) Value ≥100k | low | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3246 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_low_1d_news | Micro cap (≤100M) Value ≥100k | low | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3247 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_low_1d_open | Micro cap (≤250M) Value ≥100k | low | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3248 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_low_1d_news | Micro cap (≤250M) Value ≥100k | low | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3249 | 58 | nan | CEO + CFO (combo) — hold ret_mean_1d_open | CEO + CFO (combo) | mean | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3250 | 58 | nan | CEO + CFO (combo) — hold ret_mean_1d_news | CEO + CFO (combo) | mean | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3251 | 54 | nan | 10% Owner — hold ret_mean_1d_open | 10% Owner | mean | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3252 | 54 | nan | 10% Owner — hold ret_mean_1d_news | 10% Owner | mean | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3253 | 57 | nan | 10% Owner + Value ≥500k — hold ret_mean_1d_open | 10% Owner + Value ≥500k | mean | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3254 | 57 | nan | 10% Owner + Value ≥500k — hold ret_mean_1d_news | 10% Owner + Value ≥500k | mean | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3255 | 59 | nan | CEO only + Position +20% — hold ret_mean_1d_open | CEO only + Position +20% | mean | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3256 | 59 | nan | CEO only + Position +20% — hold ret_mean_1d_news | CEO only + Position +20% | mean | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3257 | 55 | nan | 10% Owner + Position +10% — hold ret_mean_1d_open | 10% Owner + Position +10% | mean | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3258 | 55 | nan | 10% Owner + Position +10% — hold ret_mean_1d_news | 10% Owner + Position +10% | mean | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3259 | 56 | nan | 10% Owner + Position +20% — hold ret_mean_1d_open | 10% Owner + Position +20% | mean | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3260 | 56 | nan | 10% Owner + Position +20% — hold ret_mean_1d_news | 10% Owner + Position +20% | mean | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3261 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_mean_1d_open | CEO+CFO (combo) + Position +10% | mean | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3262 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_mean_1d_news | CEO+CFO (combo) + Position +10% | mean | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3263 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_mean_1d_open | CEO+CFO (combo) + Position +20% | mean | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3264 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_mean_1d_news | CEO+CFO (combo) + Position +20% | mean | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3265 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_mean_1d_open | Micro cap (≤50M) CEO/CFO | mean | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3266 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_mean_1d_news | Micro cap (≤50M) CEO/CFO | mean | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3267 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_mean_1d_open | Micro cap (≤100M) CEO/CFO | mean | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3268 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_mean_1d_news | Micro cap (≤100M) CEO/CFO | mean | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3269 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_mean_1d_open | Micro cap (≤250M) CEO/CFO | mean | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3270 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_mean_1d_news | Micro cap (≤250M) CEO/CFO | mean | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3271 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_mean_1d_open | Large cap (≥20B) CEO/CFO | mean | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3272 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_mean_1d_news | Large cap (≥20B) CEO/CFO | mean | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3273 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_mean_1d_open | Large cap (≥50B) CEO/CFO | mean | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3274 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_mean_1d_news | Large cap (≥50B) CEO/CFO | mean | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3275 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_mean_1d_open | Large cap (≥100B) CEO/CFO | mean | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3276 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_mean_1d_news | Large cap (≥100B) CEO/CFO | mean | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3277 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_mean_1d_open | Micro cap (≤50M) Value ≥100k | mean | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3278 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_mean_1d_news | Micro cap (≤50M) Value ≥100k | mean | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3279 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_mean_1d_open | Micro cap (≤100M) Value ≥100k | mean | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3280 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_mean_1d_news | Micro cap (≤100M) Value ≥100k | mean | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3281 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_mean_1d_open | Micro cap (≤250M) Value ≥100k | mean | 1 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3282 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_mean_1d_news | Micro cap (≤250M) Value ≥100k | mean | 1 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3283 | 58 | nan | CEO + CFO (combo) — hold ret_high_2d_open | CEO + CFO (combo) | high | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3284 | 58 | nan | CEO + CFO (combo) — hold ret_high_2d_news | CEO + CFO (combo) | high | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3285 | 54 | nan | 10% Owner — hold ret_high_2d_open | 10% Owner | high | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3286 | 54 | nan | 10% Owner — hold ret_high_2d_news | 10% Owner | high | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3287 | 57 | nan | 10% Owner + Value ≥500k — hold ret_high_2d_open | 10% Owner + Value ≥500k | high | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3288 | 57 | nan | 10% Owner + Value ≥500k — hold ret_high_2d_news | 10% Owner + Value ≥500k | high | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3289 | 59 | nan | CEO only + Position +20% — hold ret_high_2d_open | CEO only + Position +20% | high | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3290 | 59 | nan | CEO only + Position +20% — hold ret_high_2d_news | CEO only + Position +20% | high | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3291 | 55 | nan | 10% Owner + Position +10% — hold ret_high_2d_open | 10% Owner + Position +10% | high | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3292 | 55 | nan | 10% Owner + Position +10% — hold ret_high_2d_news | 10% Owner + Position +10% | high | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3293 | 56 | nan | 10% Owner + Position +20% — hold ret_high_2d_open | 10% Owner + Position +20% | high | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3294 | 56 | nan | 10% Owner + Position +20% — hold ret_high_2d_news | 10% Owner + Position +20% | high | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3295 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_high_2d_open | CEO+CFO (combo) + Position +10% | high | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3296 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_high_2d_news | CEO+CFO (combo) + Position +10% | high | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3297 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_high_2d_open | CEO+CFO (combo) + Position +20% | high | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3298 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_high_2d_news | CEO+CFO (combo) + Position +20% | high | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3299 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_high_2d_open | Micro cap (≤50M) CEO/CFO | high | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3300 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_high_2d_news | Micro cap (≤50M) CEO/CFO | high | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3301 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_high_2d_open | Micro cap (≤100M) CEO/CFO | high | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3302 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_high_2d_news | Micro cap (≤100M) CEO/CFO | high | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3303 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_high_2d_open | Micro cap (≤250M) CEO/CFO | high | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3304 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_high_2d_news | Micro cap (≤250M) CEO/CFO | high | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3305 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_high_2d_open | Large cap (≥20B) CEO/CFO | high | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3306 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_high_2d_news | Large cap (≥20B) CEO/CFO | high | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3307 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_high_2d_open | Large cap (≥50B) CEO/CFO | high | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3308 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_high_2d_news | Large cap (≥50B) CEO/CFO | high | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3309 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_high_2d_open | Large cap (≥100B) CEO/CFO | high | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3310 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_high_2d_news | Large cap (≥100B) CEO/CFO | high | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3311 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_high_2d_open | Micro cap (≤50M) Value ≥100k | high | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3312 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_high_2d_news | Micro cap (≤50M) Value ≥100k | high | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3313 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_high_2d_open | Micro cap (≤100M) Value ≥100k | high | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3314 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_high_2d_news | Micro cap (≤100M) Value ≥100k | high | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3315 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_high_2d_open | Micro cap (≤250M) Value ≥100k | high | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3316 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_high_2d_news | Micro cap (≤250M) Value ≥100k | high | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3317 | 58 | nan | CEO + CFO (combo) — hold ret_low_2d_open | CEO + CFO (combo) | low | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3318 | 58 | nan | CEO + CFO (combo) — hold ret_low_2d_news | CEO + CFO (combo) | low | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3319 | 54 | nan | 10% Owner — hold ret_low_2d_open | 10% Owner | low | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3320 | 54 | nan | 10% Owner — hold ret_low_2d_news | 10% Owner | low | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3321 | 57 | nan | 10% Owner + Value ≥500k — hold ret_low_2d_open | 10% Owner + Value ≥500k | low | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3322 | 57 | nan | 10% Owner + Value ≥500k — hold ret_low_2d_news | 10% Owner + Value ≥500k | low | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3323 | 59 | nan | CEO only + Position +20% — hold ret_low_2d_open | CEO only + Position +20% | low | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3324 | 59 | nan | CEO only + Position +20% — hold ret_low_2d_news | CEO only + Position +20% | low | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3325 | 55 | nan | 10% Owner + Position +10% — hold ret_low_2d_open | 10% Owner + Position +10% | low | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3326 | 55 | nan | 10% Owner + Position +10% — hold ret_low_2d_news | 10% Owner + Position +10% | low | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3327 | 56 | nan | 10% Owner + Position +20% — hold ret_low_2d_open | 10% Owner + Position +20% | low | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3328 | 56 | nan | 10% Owner + Position +20% — hold ret_low_2d_news | 10% Owner + Position +20% | low | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3329 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_low_2d_open | CEO+CFO (combo) + Position +10% | low | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3330 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_low_2d_news | CEO+CFO (combo) + Position +10% | low | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3331 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_low_2d_open | CEO+CFO (combo) + Position +20% | low | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3332 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_low_2d_news | CEO+CFO (combo) + Position +20% | low | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3333 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_low_2d_open | Micro cap (≤50M) CEO/CFO | low | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3334 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_low_2d_news | Micro cap (≤50M) CEO/CFO | low | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3335 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_low_2d_open | Micro cap (≤100M) CEO/CFO | low | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3336 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_low_2d_news | Micro cap (≤100M) CEO/CFO | low | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3337 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_low_2d_open | Micro cap (≤250M) CEO/CFO | low | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3338 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_low_2d_news | Micro cap (≤250M) CEO/CFO | low | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3339 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_low_2d_open | Large cap (≥20B) CEO/CFO | low | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3340 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_low_2d_news | Large cap (≥20B) CEO/CFO | low | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3341 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_low_2d_open | Large cap (≥50B) CEO/CFO | low | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3342 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_low_2d_news | Large cap (≥50B) CEO/CFO | low | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3343 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_low_2d_open | Large cap (≥100B) CEO/CFO | low | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3344 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_low_2d_news | Large cap (≥100B) CEO/CFO | low | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3345 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_low_2d_open | Micro cap (≤50M) Value ≥100k | low | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3346 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_low_2d_news | Micro cap (≤50M) Value ≥100k | low | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3347 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_low_2d_open | Micro cap (≤100M) Value ≥100k | low | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3348 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_low_2d_news | Micro cap (≤100M) Value ≥100k | low | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3349 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_low_2d_open | Micro cap (≤250M) Value ≥100k | low | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3350 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_low_2d_news | Micro cap (≤250M) Value ≥100k | low | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3351 | 58 | nan | CEO + CFO (combo) — hold ret_mean_2d_open | CEO + CFO (combo) | mean | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3352 | 58 | nan | CEO + CFO (combo) — hold ret_mean_2d_news | CEO + CFO (combo) | mean | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3353 | 54 | nan | 10% Owner — hold ret_mean_2d_open | 10% Owner | mean | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3354 | 54 | nan | 10% Owner — hold ret_mean_2d_news | 10% Owner | mean | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3355 | 57 | nan | 10% Owner + Value ≥500k — hold ret_mean_2d_open | 10% Owner + Value ≥500k | mean | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3356 | 57 | nan | 10% Owner + Value ≥500k — hold ret_mean_2d_news | 10% Owner + Value ≥500k | mean | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3357 | 59 | nan | CEO only + Position +20% — hold ret_mean_2d_open | CEO only + Position +20% | mean | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3358 | 59 | nan | CEO only + Position +20% — hold ret_mean_2d_news | CEO only + Position +20% | mean | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3359 | 55 | nan | 10% Owner + Position +10% — hold ret_mean_2d_open | 10% Owner + Position +10% | mean | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3360 | 55 | nan | 10% Owner + Position +10% — hold ret_mean_2d_news | 10% Owner + Position +10% | mean | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3361 | 56 | nan | 10% Owner + Position +20% — hold ret_mean_2d_open | 10% Owner + Position +20% | mean | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3362 | 56 | nan | 10% Owner + Position +20% — hold ret_mean_2d_news | 10% Owner + Position +20% | mean | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3363 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_mean_2d_open | CEO+CFO (combo) + Position +10% | mean | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3364 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_mean_2d_news | CEO+CFO (combo) + Position +10% | mean | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3365 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_mean_2d_open | CEO+CFO (combo) + Position +20% | mean | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3366 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_mean_2d_news | CEO+CFO (combo) + Position +20% | mean | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3367 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_mean_2d_open | Micro cap (≤50M) CEO/CFO | mean | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3368 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_mean_2d_news | Micro cap (≤50M) CEO/CFO | mean | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3369 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_mean_2d_open | Micro cap (≤100M) CEO/CFO | mean | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3370 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_mean_2d_news | Micro cap (≤100M) CEO/CFO | mean | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3371 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_mean_2d_open | Micro cap (≤250M) CEO/CFO | mean | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3372 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_mean_2d_news | Micro cap (≤250M) CEO/CFO | mean | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3373 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_mean_2d_open | Large cap (≥20B) CEO/CFO | mean | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3374 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_mean_2d_news | Large cap (≥20B) CEO/CFO | mean | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3375 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_mean_2d_open | Large cap (≥50B) CEO/CFO | mean | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3376 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_mean_2d_news | Large cap (≥50B) CEO/CFO | mean | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3377 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_mean_2d_open | Large cap (≥100B) CEO/CFO | mean | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3378 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_mean_2d_news | Large cap (≥100B) CEO/CFO | mean | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3379 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_mean_2d_open | Micro cap (≤50M) Value ≥100k | mean | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3380 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_mean_2d_news | Micro cap (≤50M) Value ≥100k | mean | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3381 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_mean_2d_open | Micro cap (≤100M) Value ≥100k | mean | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3382 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_mean_2d_news | Micro cap (≤100M) Value ≥100k | mean | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3383 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_mean_2d_open | Micro cap (≤250M) Value ≥100k | mean | 2 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3384 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_mean_2d_news | Micro cap (≤250M) Value ≥100k | mean | 2 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3385 | 58 | nan | CEO + CFO (combo) — hold ret_high_3d_open | CEO + CFO (combo) | high | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3386 | 58 | nan | CEO + CFO (combo) — hold ret_high_3d_news | CEO + CFO (combo) | high | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3387 | 54 | nan | 10% Owner — hold ret_high_3d_open | 10% Owner | high | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3388 | 54 | nan | 10% Owner — hold ret_high_3d_news | 10% Owner | high | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3389 | 57 | nan | 10% Owner + Value ≥500k — hold ret_high_3d_open | 10% Owner + Value ≥500k | high | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3390 | 57 | nan | 10% Owner + Value ≥500k — hold ret_high_3d_news | 10% Owner + Value ≥500k | high | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3391 | 59 | nan | CEO only + Position +20% — hold ret_high_3d_open | CEO only + Position +20% | high | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3392 | 59 | nan | CEO only + Position +20% — hold ret_high_3d_news | CEO only + Position +20% | high | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3393 | 55 | nan | 10% Owner + Position +10% — hold ret_high_3d_open | 10% Owner + Position +10% | high | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3394 | 55 | nan | 10% Owner + Position +10% — hold ret_high_3d_news | 10% Owner + Position +10% | high | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3395 | 56 | nan | 10% Owner + Position +20% — hold ret_high_3d_open | 10% Owner + Position +20% | high | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3396 | 56 | nan | 10% Owner + Position +20% — hold ret_high_3d_news | 10% Owner + Position +20% | high | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3397 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_high_3d_open | CEO+CFO (combo) + Position +10% | high | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3398 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_high_3d_news | CEO+CFO (combo) + Position +10% | high | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3399 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_high_3d_open | CEO+CFO (combo) + Position +20% | high | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3400 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_high_3d_news | CEO+CFO (combo) + Position +20% | high | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3401 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_high_3d_open | Micro cap (≤50M) CEO/CFO | high | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3402 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_high_3d_news | Micro cap (≤50M) CEO/CFO | high | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3403 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_high_3d_open | Micro cap (≤100M) CEO/CFO | high | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3404 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_high_3d_news | Micro cap (≤100M) CEO/CFO | high | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3405 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_high_3d_open | Micro cap (≤250M) CEO/CFO | high | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3406 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_high_3d_news | Micro cap (≤250M) CEO/CFO | high | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3407 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_high_3d_open | Large cap (≥20B) CEO/CFO | high | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3408 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_high_3d_news | Large cap (≥20B) CEO/CFO | high | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3409 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_high_3d_open | Large cap (≥50B) CEO/CFO | high | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3410 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_high_3d_news | Large cap (≥50B) CEO/CFO | high | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3411 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_high_3d_open | Large cap (≥100B) CEO/CFO | high | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3412 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_high_3d_news | Large cap (≥100B) CEO/CFO | high | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3413 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_high_3d_open | Micro cap (≤50M) Value ≥100k | high | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3414 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_high_3d_news | Micro cap (≤50M) Value ≥100k | high | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3415 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_high_3d_open | Micro cap (≤100M) Value ≥100k | high | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3416 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_high_3d_news | Micro cap (≤100M) Value ≥100k | high | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3417 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_high_3d_open | Micro cap (≤250M) Value ≥100k | high | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3418 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_high_3d_news | Micro cap (≤250M) Value ≥100k | high | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3419 | 58 | nan | CEO + CFO (combo) — hold ret_low_3d_open | CEO + CFO (combo) | low | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3420 | 58 | nan | CEO + CFO (combo) — hold ret_low_3d_news | CEO + CFO (combo) | low | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3421 | 54 | nan | 10% Owner — hold ret_low_3d_open | 10% Owner | low | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3422 | 54 | nan | 10% Owner — hold ret_low_3d_news | 10% Owner | low | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3423 | 57 | nan | 10% Owner + Value ≥500k — hold ret_low_3d_open | 10% Owner + Value ≥500k | low | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3424 | 57 | nan | 10% Owner + Value ≥500k — hold ret_low_3d_news | 10% Owner + Value ≥500k | low | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3425 | 59 | nan | CEO only + Position +20% — hold ret_low_3d_open | CEO only + Position +20% | low | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3426 | 59 | nan | CEO only + Position +20% — hold ret_low_3d_news | CEO only + Position +20% | low | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3427 | 55 | nan | 10% Owner + Position +10% — hold ret_low_3d_open | 10% Owner + Position +10% | low | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3428 | 55 | nan | 10% Owner + Position +10% — hold ret_low_3d_news | 10% Owner + Position +10% | low | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3429 | 56 | nan | 10% Owner + Position +20% — hold ret_low_3d_open | 10% Owner + Position +20% | low | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3430 | 56 | nan | 10% Owner + Position +20% — hold ret_low_3d_news | 10% Owner + Position +20% | low | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3431 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_low_3d_open | CEO+CFO (combo) + Position +10% | low | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3432 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_low_3d_news | CEO+CFO (combo) + Position +10% | low | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3433 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_low_3d_open | CEO+CFO (combo) + Position +20% | low | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3434 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_low_3d_news | CEO+CFO (combo) + Position +20% | low | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3435 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_low_3d_open | Micro cap (≤50M) CEO/CFO | low | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3436 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_low_3d_news | Micro cap (≤50M) CEO/CFO | low | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3437 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_low_3d_open | Micro cap (≤100M) CEO/CFO | low | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3438 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_low_3d_news | Micro cap (≤100M) CEO/CFO | low | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3439 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_low_3d_open | Micro cap (≤250M) CEO/CFO | low | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3440 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_low_3d_news | Micro cap (≤250M) CEO/CFO | low | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3441 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_low_3d_open | Large cap (≥20B) CEO/CFO | low | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3442 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_low_3d_news | Large cap (≥20B) CEO/CFO | low | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3443 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_low_3d_open | Large cap (≥50B) CEO/CFO | low | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3444 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_low_3d_news | Large cap (≥50B) CEO/CFO | low | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3445 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_low_3d_open | Large cap (≥100B) CEO/CFO | low | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3446 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_low_3d_news | Large cap (≥100B) CEO/CFO | low | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3447 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_low_3d_open | Micro cap (≤50M) Value ≥100k | low | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3448 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_low_3d_news | Micro cap (≤50M) Value ≥100k | low | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3449 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_low_3d_open | Micro cap (≤100M) Value ≥100k | low | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3450 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_low_3d_news | Micro cap (≤100M) Value ≥100k | low | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3451 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_low_3d_open | Micro cap (≤250M) Value ≥100k | low | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3452 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_low_3d_news | Micro cap (≤250M) Value ≥100k | low | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3453 | 58 | nan | CEO + CFO (combo) — hold ret_mean_3d_open | CEO + CFO (combo) | mean | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3454 | 58 | nan | CEO + CFO (combo) — hold ret_mean_3d_news | CEO + CFO (combo) | mean | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3455 | 54 | nan | 10% Owner — hold ret_mean_3d_open | 10% Owner | mean | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3456 | 54 | nan | 10% Owner — hold ret_mean_3d_news | 10% Owner | mean | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3457 | 57 | nan | 10% Owner + Value ≥500k — hold ret_mean_3d_open | 10% Owner + Value ≥500k | mean | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3458 | 57 | nan | 10% Owner + Value ≥500k — hold ret_mean_3d_news | 10% Owner + Value ≥500k | mean | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3459 | 59 | nan | CEO only + Position +20% — hold ret_mean_3d_open | CEO only + Position +20% | mean | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3460 | 59 | nan | CEO only + Position +20% — hold ret_mean_3d_news | CEO only + Position +20% | mean | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3461 | 55 | nan | 10% Owner + Position +10% — hold ret_mean_3d_open | 10% Owner + Position +10% | mean | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3462 | 55 | nan | 10% Owner + Position +10% — hold ret_mean_3d_news | 10% Owner + Position +10% | mean | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3463 | 56 | nan | 10% Owner + Position +20% — hold ret_mean_3d_open | 10% Owner + Position +20% | mean | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3464 | 56 | nan | 10% Owner + Position +20% — hold ret_mean_3d_news | 10% Owner + Position +20% | mean | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3465 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_mean_3d_open | CEO+CFO (combo) + Position +10% | mean | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3466 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_mean_3d_news | CEO+CFO (combo) + Position +10% | mean | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3467 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_mean_3d_open | CEO+CFO (combo) + Position +20% | mean | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3468 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_mean_3d_news | CEO+CFO (combo) + Position +20% | mean | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3469 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_mean_3d_open | Micro cap (≤50M) CEO/CFO | mean | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3470 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_mean_3d_news | Micro cap (≤50M) CEO/CFO | mean | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3471 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_mean_3d_open | Micro cap (≤100M) CEO/CFO | mean | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3472 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_mean_3d_news | Micro cap (≤100M) CEO/CFO | mean | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3473 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_mean_3d_open | Micro cap (≤250M) CEO/CFO | mean | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3474 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_mean_3d_news | Micro cap (≤250M) CEO/CFO | mean | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3475 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_mean_3d_open | Large cap (≥20B) CEO/CFO | mean | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3476 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_mean_3d_news | Large cap (≥20B) CEO/CFO | mean | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3477 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_mean_3d_open | Large cap (≥50B) CEO/CFO | mean | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3478 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_mean_3d_news | Large cap (≥50B) CEO/CFO | mean | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3479 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_mean_3d_open | Large cap (≥100B) CEO/CFO | mean | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3480 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_mean_3d_news | Large cap (≥100B) CEO/CFO | mean | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3481 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_mean_3d_open | Micro cap (≤50M) Value ≥100k | mean | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3482 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_mean_3d_news | Micro cap (≤50M) Value ≥100k | mean | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3483 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_mean_3d_open | Micro cap (≤100M) Value ≥100k | mean | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3484 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_mean_3d_news | Micro cap (≤100M) Value ≥100k | mean | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3485 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_mean_3d_open | Micro cap (≤250M) Value ≥100k | mean | 3 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3486 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_mean_3d_news | Micro cap (≤250M) Value ≥100k | mean | 3 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3487 | 58 | nan | CEO + CFO (combo) — hold ret_high_5d_open | CEO + CFO (combo) | high | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3488 | 58 | nan | CEO + CFO (combo) — hold ret_high_5d_news | CEO + CFO (combo) | high | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3489 | 54 | nan | 10% Owner — hold ret_high_5d_open | 10% Owner | high | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3490 | 54 | nan | 10% Owner — hold ret_high_5d_news | 10% Owner | high | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3491 | 57 | nan | 10% Owner + Value ≥500k — hold ret_high_5d_open | 10% Owner + Value ≥500k | high | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3492 | 57 | nan | 10% Owner + Value ≥500k — hold ret_high_5d_news | 10% Owner + Value ≥500k | high | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3493 | 59 | nan | CEO only + Position +20% — hold ret_high_5d_open | CEO only + Position +20% | high | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3494 | 59 | nan | CEO only + Position +20% — hold ret_high_5d_news | CEO only + Position +20% | high | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3495 | 55 | nan | 10% Owner + Position +10% — hold ret_high_5d_open | 10% Owner + Position +10% | high | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3496 | 55 | nan | 10% Owner + Position +10% — hold ret_high_5d_news | 10% Owner + Position +10% | high | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3497 | 56 | nan | 10% Owner + Position +20% — hold ret_high_5d_open | 10% Owner + Position +20% | high | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3498 | 56 | nan | 10% Owner + Position +20% — hold ret_high_5d_news | 10% Owner + Position +20% | high | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3499 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_high_5d_open | CEO+CFO (combo) + Position +10% | high | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3500 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_high_5d_news | CEO+CFO (combo) + Position +10% | high | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3501 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_high_5d_open | CEO+CFO (combo) + Position +20% | high | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3502 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_high_5d_news | CEO+CFO (combo) + Position +20% | high | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3503 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_high_5d_open | Micro cap (≤50M) CEO/CFO | high | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3504 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_high_5d_news | Micro cap (≤50M) CEO/CFO | high | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3505 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_high_5d_open | Micro cap (≤100M) CEO/CFO | high | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3506 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_high_5d_news | Micro cap (≤100M) CEO/CFO | high | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3507 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_high_5d_open | Micro cap (≤250M) CEO/CFO | high | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3508 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_high_5d_news | Micro cap (≤250M) CEO/CFO | high | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3509 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_high_5d_open | Large cap (≥20B) CEO/CFO | high | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3510 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_high_5d_news | Large cap (≥20B) CEO/CFO | high | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3511 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_high_5d_open | Large cap (≥50B) CEO/CFO | high | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3512 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_high_5d_news | Large cap (≥50B) CEO/CFO | high | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3513 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_high_5d_open | Large cap (≥100B) CEO/CFO | high | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3514 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_high_5d_news | Large cap (≥100B) CEO/CFO | high | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3515 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_high_5d_open | Micro cap (≤50M) Value ≥100k | high | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3516 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_high_5d_news | Micro cap (≤50M) Value ≥100k | high | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3517 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_high_5d_open | Micro cap (≤100M) Value ≥100k | high | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3518 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_high_5d_news | Micro cap (≤100M) Value ≥100k | high | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3519 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_high_5d_open | Micro cap (≤250M) Value ≥100k | high | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3520 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_high_5d_news | Micro cap (≤250M) Value ≥100k | high | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3521 | 58 | nan | CEO + CFO (combo) — hold ret_low_5d_open | CEO + CFO (combo) | low | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3522 | 58 | nan | CEO + CFO (combo) — hold ret_low_5d_news | CEO + CFO (combo) | low | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3523 | 54 | nan | 10% Owner — hold ret_low_5d_open | 10% Owner | low | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3524 | 54 | nan | 10% Owner — hold ret_low_5d_news | 10% Owner | low | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3525 | 57 | nan | 10% Owner + Value ≥500k — hold ret_low_5d_open | 10% Owner + Value ≥500k | low | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3526 | 57 | nan | 10% Owner + Value ≥500k — hold ret_low_5d_news | 10% Owner + Value ≥500k | low | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3527 | 59 | nan | CEO only + Position +20% — hold ret_low_5d_open | CEO only + Position +20% | low | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3528 | 59 | nan | CEO only + Position +20% — hold ret_low_5d_news | CEO only + Position +20% | low | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3529 | 55 | nan | 10% Owner + Position +10% — hold ret_low_5d_open | 10% Owner + Position +10% | low | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3530 | 55 | nan | 10% Owner + Position +10% — hold ret_low_5d_news | 10% Owner + Position +10% | low | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3531 | 56 | nan | 10% Owner + Position +20% — hold ret_low_5d_open | 10% Owner + Position +20% | low | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3532 | 56 | nan | 10% Owner + Position +20% — hold ret_low_5d_news | 10% Owner + Position +20% | low | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3533 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_low_5d_open | CEO+CFO (combo) + Position +10% | low | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3534 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_low_5d_news | CEO+CFO (combo) + Position +10% | low | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3535 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_low_5d_open | CEO+CFO (combo) + Position +20% | low | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3536 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_low_5d_news | CEO+CFO (combo) + Position +20% | low | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3537 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_low_5d_open | Micro cap (≤50M) CEO/CFO | low | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3538 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_low_5d_news | Micro cap (≤50M) CEO/CFO | low | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3539 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_low_5d_open | Micro cap (≤100M) CEO/CFO | low | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3540 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_low_5d_news | Micro cap (≤100M) CEO/CFO | low | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3541 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_low_5d_open | Micro cap (≤250M) CEO/CFO | low | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3542 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_low_5d_news | Micro cap (≤250M) CEO/CFO | low | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3543 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_low_5d_open | Large cap (≥20B) CEO/CFO | low | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3544 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_low_5d_news | Large cap (≥20B) CEO/CFO | low | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3545 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_low_5d_open | Large cap (≥50B) CEO/CFO | low | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3546 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_low_5d_news | Large cap (≥50B) CEO/CFO | low | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3547 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_low_5d_open | Large cap (≥100B) CEO/CFO | low | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3548 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_low_5d_news | Large cap (≥100B) CEO/CFO | low | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3549 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_low_5d_open | Micro cap (≤50M) Value ≥100k | low | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3550 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_low_5d_news | Micro cap (≤50M) Value ≥100k | low | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3551 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_low_5d_open | Micro cap (≤100M) Value ≥100k | low | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3552 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_low_5d_news | Micro cap (≤100M) Value ≥100k | low | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3553 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_low_5d_open | Micro cap (≤250M) Value ≥100k | low | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3554 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_low_5d_news | Micro cap (≤250M) Value ≥100k | low | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3555 | 58 | nan | CEO + CFO (combo) — hold ret_mean_5d_open | CEO + CFO (combo) | mean | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3556 | 58 | nan | CEO + CFO (combo) — hold ret_mean_5d_news | CEO + CFO (combo) | mean | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3557 | 54 | nan | 10% Owner — hold ret_mean_5d_open | 10% Owner | mean | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3558 | 54 | nan | 10% Owner — hold ret_mean_5d_news | 10% Owner | mean | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3559 | 57 | nan | 10% Owner + Value ≥500k — hold ret_mean_5d_open | 10% Owner + Value ≥500k | mean | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3560 | 57 | nan | 10% Owner + Value ≥500k — hold ret_mean_5d_news | 10% Owner + Value ≥500k | mean | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3561 | 59 | nan | CEO only + Position +20% — hold ret_mean_5d_open | CEO only + Position +20% | mean | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3562 | 59 | nan | CEO only + Position +20% — hold ret_mean_5d_news | CEO only + Position +20% | mean | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3563 | 55 | nan | 10% Owner + Position +10% — hold ret_mean_5d_open | 10% Owner + Position +10% | mean | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3564 | 55 | nan | 10% Owner + Position +10% — hold ret_mean_5d_news | 10% Owner + Position +10% | mean | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3565 | 56 | nan | 10% Owner + Position +20% — hold ret_mean_5d_open | 10% Owner + Position +20% | mean | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3566 | 56 | nan | 10% Owner + Position +20% — hold ret_mean_5d_news | 10% Owner + Position +20% | mean | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3567 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_mean_5d_open | CEO+CFO (combo) + Position +10% | mean | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3568 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_mean_5d_news | CEO+CFO (combo) + Position +10% | mean | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3569 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_mean_5d_open | CEO+CFO (combo) + Position +20% | mean | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3570 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_mean_5d_news | CEO+CFO (combo) + Position +20% | mean | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3571 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_mean_5d_open | Micro cap (≤50M) CEO/CFO | mean | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3572 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_mean_5d_news | Micro cap (≤50M) CEO/CFO | mean | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3573 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_mean_5d_open | Micro cap (≤100M) CEO/CFO | mean | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3574 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_mean_5d_news | Micro cap (≤100M) CEO/CFO | mean | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3575 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_mean_5d_open | Micro cap (≤250M) CEO/CFO | mean | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3576 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_mean_5d_news | Micro cap (≤250M) CEO/CFO | mean | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3577 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_mean_5d_open | Large cap (≥20B) CEO/CFO | mean | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3578 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_mean_5d_news | Large cap (≥20B) CEO/CFO | mean | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3579 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_mean_5d_open | Large cap (≥50B) CEO/CFO | mean | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3580 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_mean_5d_news | Large cap (≥50B) CEO/CFO | mean | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3581 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_mean_5d_open | Large cap (≥100B) CEO/CFO | mean | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3582 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_mean_5d_news | Large cap (≥100B) CEO/CFO | mean | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3583 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_mean_5d_open | Micro cap (≤50M) Value ≥100k | mean | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3584 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_mean_5d_news | Micro cap (≤50M) Value ≥100k | mean | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3585 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_mean_5d_open | Micro cap (≤100M) Value ≥100k | mean | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3586 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_mean_5d_news | Micro cap (≤100M) Value ≥100k | mean | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3587 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_mean_5d_open | Micro cap (≤250M) Value ≥100k | mean | 5 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3588 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_mean_5d_news | Micro cap (≤250M) Value ≥100k | mean | 5 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3589 | 58 | nan | CEO + CFO (combo) — hold ret_high_7d_open | CEO + CFO (combo) | high | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3590 | 58 | nan | CEO + CFO (combo) — hold ret_high_7d_news | CEO + CFO (combo) | high | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3591 | 54 | nan | 10% Owner — hold ret_high_7d_open | 10% Owner | high | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3592 | 54 | nan | 10% Owner — hold ret_high_7d_news | 10% Owner | high | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3593 | 57 | nan | 10% Owner + Value ≥500k — hold ret_high_7d_open | 10% Owner + Value ≥500k | high | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3594 | 57 | nan | 10% Owner + Value ≥500k — hold ret_high_7d_news | 10% Owner + Value ≥500k | high | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3595 | 59 | nan | CEO only + Position +20% — hold ret_high_7d_open | CEO only + Position +20% | high | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3596 | 59 | nan | CEO only + Position +20% — hold ret_high_7d_news | CEO only + Position +20% | high | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3597 | 55 | nan | 10% Owner + Position +10% — hold ret_high_7d_open | 10% Owner + Position +10% | high | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3598 | 55 | nan | 10% Owner + Position +10% — hold ret_high_7d_news | 10% Owner + Position +10% | high | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3599 | 56 | nan | 10% Owner + Position +20% — hold ret_high_7d_open | 10% Owner + Position +20% | high | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3600 | 56 | nan | 10% Owner + Position +20% — hold ret_high_7d_news | 10% Owner + Position +20% | high | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3601 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_high_7d_open | CEO+CFO (combo) + Position +10% | high | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3602 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_high_7d_news | CEO+CFO (combo) + Position +10% | high | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3603 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_high_7d_open | CEO+CFO (combo) + Position +20% | high | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3604 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_high_7d_news | CEO+CFO (combo) + Position +20% | high | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3605 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_high_7d_open | Micro cap (≤50M) CEO/CFO | high | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3606 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_high_7d_news | Micro cap (≤50M) CEO/CFO | high | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3607 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_high_7d_open | Micro cap (≤100M) CEO/CFO | high | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3608 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_high_7d_news | Micro cap (≤100M) CEO/CFO | high | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3609 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_high_7d_open | Micro cap (≤250M) CEO/CFO | high | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3610 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_high_7d_news | Micro cap (≤250M) CEO/CFO | high | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3611 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_high_7d_open | Large cap (≥20B) CEO/CFO | high | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3612 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_high_7d_news | Large cap (≥20B) CEO/CFO | high | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3613 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_high_7d_open | Large cap (≥50B) CEO/CFO | high | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3614 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_high_7d_news | Large cap (≥50B) CEO/CFO | high | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3615 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_high_7d_open | Large cap (≥100B) CEO/CFO | high | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3616 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_high_7d_news | Large cap (≥100B) CEO/CFO | high | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3617 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_high_7d_open | Micro cap (≤50M) Value ≥100k | high | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3618 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_high_7d_news | Micro cap (≤50M) Value ≥100k | high | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3619 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_high_7d_open | Micro cap (≤100M) Value ≥100k | high | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3620 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_high_7d_news | Micro cap (≤100M) Value ≥100k | high | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3621 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_high_7d_open | Micro cap (≤250M) Value ≥100k | high | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3622 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_high_7d_news | Micro cap (≤250M) Value ≥100k | high | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3623 | 58 | nan | CEO + CFO (combo) — hold ret_low_7d_open | CEO + CFO (combo) | low | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3624 | 58 | nan | CEO + CFO (combo) — hold ret_low_7d_news | CEO + CFO (combo) | low | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3625 | 54 | nan | 10% Owner — hold ret_low_7d_open | 10% Owner | low | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3626 | 54 | nan | 10% Owner — hold ret_low_7d_news | 10% Owner | low | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3627 | 57 | nan | 10% Owner + Value ≥500k — hold ret_low_7d_open | 10% Owner + Value ≥500k | low | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3628 | 57 | nan | 10% Owner + Value ≥500k — hold ret_low_7d_news | 10% Owner + Value ≥500k | low | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3629 | 59 | nan | CEO only + Position +20% — hold ret_low_7d_open | CEO only + Position +20% | low | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3630 | 59 | nan | CEO only + Position +20% — hold ret_low_7d_news | CEO only + Position +20% | low | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3631 | 55 | nan | 10% Owner + Position +10% — hold ret_low_7d_open | 10% Owner + Position +10% | low | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3632 | 55 | nan | 10% Owner + Position +10% — hold ret_low_7d_news | 10% Owner + Position +10% | low | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3633 | 56 | nan | 10% Owner + Position +20% — hold ret_low_7d_open | 10% Owner + Position +20% | low | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3634 | 56 | nan | 10% Owner + Position +20% — hold ret_low_7d_news | 10% Owner + Position +20% | low | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3635 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_low_7d_open | CEO+CFO (combo) + Position +10% | low | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3636 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_low_7d_news | CEO+CFO (combo) + Position +10% | low | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3637 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_low_7d_open | CEO+CFO (combo) + Position +20% | low | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3638 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_low_7d_news | CEO+CFO (combo) + Position +20% | low | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3639 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_low_7d_open | Micro cap (≤50M) CEO/CFO | low | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3640 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_low_7d_news | Micro cap (≤50M) CEO/CFO | low | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3641 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_low_7d_open | Micro cap (≤100M) CEO/CFO | low | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3642 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_low_7d_news | Micro cap (≤100M) CEO/CFO | low | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3643 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_low_7d_open | Micro cap (≤250M) CEO/CFO | low | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3644 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_low_7d_news | Micro cap (≤250M) CEO/CFO | low | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3645 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_low_7d_open | Large cap (≥20B) CEO/CFO | low | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3646 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_low_7d_news | Large cap (≥20B) CEO/CFO | low | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3647 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_low_7d_open | Large cap (≥50B) CEO/CFO | low | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3648 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_low_7d_news | Large cap (≥50B) CEO/CFO | low | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3649 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_low_7d_open | Large cap (≥100B) CEO/CFO | low | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3650 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_low_7d_news | Large cap (≥100B) CEO/CFO | low | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3651 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_low_7d_open | Micro cap (≤50M) Value ≥100k | low | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3652 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_low_7d_news | Micro cap (≤50M) Value ≥100k | low | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3653 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_low_7d_open | Micro cap (≤100M) Value ≥100k | low | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3654 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_low_7d_news | Micro cap (≤100M) Value ≥100k | low | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3655 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_low_7d_open | Micro cap (≤250M) Value ≥100k | low | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3656 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_low_7d_news | Micro cap (≤250M) Value ≥100k | low | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3657 | 58 | nan | CEO + CFO (combo) — hold ret_mean_7d_open | CEO + CFO (combo) | mean | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3658 | 58 | nan | CEO + CFO (combo) — hold ret_mean_7d_news | CEO + CFO (combo) | mean | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3659 | 54 | nan | 10% Owner — hold ret_mean_7d_open | 10% Owner | mean | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3660 | 54 | nan | 10% Owner — hold ret_mean_7d_news | 10% Owner | mean | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3661 | 57 | nan | 10% Owner + Value ≥500k — hold ret_mean_7d_open | 10% Owner + Value ≥500k | mean | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3662 | 57 | nan | 10% Owner + Value ≥500k — hold ret_mean_7d_news | 10% Owner + Value ≥500k | mean | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3663 | 59 | nan | CEO only + Position +20% — hold ret_mean_7d_open | CEO only + Position +20% | mean | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3664 | 59 | nan | CEO only + Position +20% — hold ret_mean_7d_news | CEO only + Position +20% | mean | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3665 | 55 | nan | 10% Owner + Position +10% — hold ret_mean_7d_open | 10% Owner + Position +10% | mean | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3666 | 55 | nan | 10% Owner + Position +10% — hold ret_mean_7d_news | 10% Owner + Position +10% | mean | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3667 | 56 | nan | 10% Owner + Position +20% — hold ret_mean_7d_open | 10% Owner + Position +20% | mean | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3668 | 56 | nan | 10% Owner + Position +20% — hold ret_mean_7d_news | 10% Owner + Position +20% | mean | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3669 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_mean_7d_open | CEO+CFO (combo) + Position +10% | mean | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3670 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_mean_7d_news | CEO+CFO (combo) + Position +10% | mean | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3671 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_mean_7d_open | CEO+CFO (combo) + Position +20% | mean | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3672 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_mean_7d_news | CEO+CFO (combo) + Position +20% | mean | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3673 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_mean_7d_open | Micro cap (≤50M) CEO/CFO | mean | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3674 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_mean_7d_news | Micro cap (≤50M) CEO/CFO | mean | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3675 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_mean_7d_open | Micro cap (≤100M) CEO/CFO | mean | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3676 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_mean_7d_news | Micro cap (≤100M) CEO/CFO | mean | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3677 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_mean_7d_open | Micro cap (≤250M) CEO/CFO | mean | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3678 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_mean_7d_news | Micro cap (≤250M) CEO/CFO | mean | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3679 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_mean_7d_open | Large cap (≥20B) CEO/CFO | mean | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3680 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_mean_7d_news | Large cap (≥20B) CEO/CFO | mean | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3681 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_mean_7d_open | Large cap (≥50B) CEO/CFO | mean | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3682 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_mean_7d_news | Large cap (≥50B) CEO/CFO | mean | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3683 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_mean_7d_open | Large cap (≥100B) CEO/CFO | mean | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3684 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_mean_7d_news | Large cap (≥100B) CEO/CFO | mean | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3685 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_mean_7d_open | Micro cap (≤50M) Value ≥100k | mean | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3686 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_mean_7d_news | Micro cap (≤50M) Value ≥100k | mean | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3687 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_mean_7d_open | Micro cap (≤100M) Value ≥100k | mean | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3688 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_mean_7d_news | Micro cap (≤100M) Value ≥100k | mean | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3689 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_mean_7d_open | Micro cap (≤250M) Value ≥100k | mean | 7 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3690 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_mean_7d_news | Micro cap (≤250M) Value ≥100k | mean | 7 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3691 | 58 | nan | CEO + CFO (combo) — hold ret_high_10d_open | CEO + CFO (combo) | high | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3692 | 58 | nan | CEO + CFO (combo) — hold ret_high_10d_news | CEO + CFO (combo) | high | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3693 | 54 | nan | 10% Owner — hold ret_high_10d_open | 10% Owner | high | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3694 | 54 | nan | 10% Owner — hold ret_high_10d_news | 10% Owner | high | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3695 | 57 | nan | 10% Owner + Value ≥500k — hold ret_high_10d_open | 10% Owner + Value ≥500k | high | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3696 | 57 | nan | 10% Owner + Value ≥500k — hold ret_high_10d_news | 10% Owner + Value ≥500k | high | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3697 | 59 | nan | CEO only + Position +20% — hold ret_high_10d_open | CEO only + Position +20% | high | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3698 | 59 | nan | CEO only + Position +20% — hold ret_high_10d_news | CEO only + Position +20% | high | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3699 | 55 | nan | 10% Owner + Position +10% — hold ret_high_10d_open | 10% Owner + Position +10% | high | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3700 | 55 | nan | 10% Owner + Position +10% — hold ret_high_10d_news | 10% Owner + Position +10% | high | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3701 | 56 | nan | 10% Owner + Position +20% — hold ret_high_10d_open | 10% Owner + Position +20% | high | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3702 | 56 | nan | 10% Owner + Position +20% — hold ret_high_10d_news | 10% Owner + Position +20% | high | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3703 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_high_10d_open | CEO+CFO (combo) + Position +10% | high | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3704 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_high_10d_news | CEO+CFO (combo) + Position +10% | high | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3705 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_high_10d_open | CEO+CFO (combo) + Position +20% | high | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3706 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_high_10d_news | CEO+CFO (combo) + Position +20% | high | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3707 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_high_10d_open | Micro cap (≤50M) CEO/CFO | high | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3708 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_high_10d_news | Micro cap (≤50M) CEO/CFO | high | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3709 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_high_10d_open | Micro cap (≤100M) CEO/CFO | high | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3710 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_high_10d_news | Micro cap (≤100M) CEO/CFO | high | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3711 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_high_10d_open | Micro cap (≤250M) CEO/CFO | high | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3712 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_high_10d_news | Micro cap (≤250M) CEO/CFO | high | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3713 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_high_10d_open | Large cap (≥20B) CEO/CFO | high | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3714 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_high_10d_news | Large cap (≥20B) CEO/CFO | high | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3715 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_high_10d_open | Large cap (≥50B) CEO/CFO | high | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3716 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_high_10d_news | Large cap (≥50B) CEO/CFO | high | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3717 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_high_10d_open | Large cap (≥100B) CEO/CFO | high | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3718 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_high_10d_news | Large cap (≥100B) CEO/CFO | high | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3719 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_high_10d_open | Micro cap (≤50M) Value ≥100k | high | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3720 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_high_10d_news | Micro cap (≤50M) Value ≥100k | high | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3721 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_high_10d_open | Micro cap (≤100M) Value ≥100k | high | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3722 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_high_10d_news | Micro cap (≤100M) Value ≥100k | high | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3723 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_high_10d_open | Micro cap (≤250M) Value ≥100k | high | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3724 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_high_10d_news | Micro cap (≤250M) Value ≥100k | high | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3725 | 58 | nan | CEO + CFO (combo) — hold ret_low_10d_open | CEO + CFO (combo) | low | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3726 | 58 | nan | CEO + CFO (combo) — hold ret_low_10d_news | CEO + CFO (combo) | low | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3727 | 54 | nan | 10% Owner — hold ret_low_10d_open | 10% Owner | low | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3728 | 54 | nan | 10% Owner — hold ret_low_10d_news | 10% Owner | low | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3729 | 57 | nan | 10% Owner + Value ≥500k — hold ret_low_10d_open | 10% Owner + Value ≥500k | low | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3730 | 57 | nan | 10% Owner + Value ≥500k — hold ret_low_10d_news | 10% Owner + Value ≥500k | low | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3731 | 59 | nan | CEO only + Position +20% — hold ret_low_10d_open | CEO only + Position +20% | low | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3732 | 59 | nan | CEO only + Position +20% — hold ret_low_10d_news | CEO only + Position +20% | low | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3733 | 55 | nan | 10% Owner + Position +10% — hold ret_low_10d_open | 10% Owner + Position +10% | low | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3734 | 55 | nan | 10% Owner + Position +10% — hold ret_low_10d_news | 10% Owner + Position +10% | low | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3735 | 56 | nan | 10% Owner + Position +20% — hold ret_low_10d_open | 10% Owner + Position +20% | low | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3736 | 56 | nan | 10% Owner + Position +20% — hold ret_low_10d_news | 10% Owner + Position +20% | low | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3737 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_low_10d_open | CEO+CFO (combo) + Position +10% | low | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3738 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_low_10d_news | CEO+CFO (combo) + Position +10% | low | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3739 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_low_10d_open | CEO+CFO (combo) + Position +20% | low | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3740 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_low_10d_news | CEO+CFO (combo) + Position +20% | low | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3741 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_low_10d_open | Micro cap (≤50M) CEO/CFO | low | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3742 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_low_10d_news | Micro cap (≤50M) CEO/CFO | low | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3743 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_low_10d_open | Micro cap (≤100M) CEO/CFO | low | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3744 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_low_10d_news | Micro cap (≤100M) CEO/CFO | low | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3745 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_low_10d_open | Micro cap (≤250M) CEO/CFO | low | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3746 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_low_10d_news | Micro cap (≤250M) CEO/CFO | low | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3747 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_low_10d_open | Large cap (≥20B) CEO/CFO | low | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3748 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_low_10d_news | Large cap (≥20B) CEO/CFO | low | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3749 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_low_10d_open | Large cap (≥50B) CEO/CFO | low | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3750 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_low_10d_news | Large cap (≥50B) CEO/CFO | low | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3751 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_low_10d_open | Large cap (≥100B) CEO/CFO | low | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3752 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_low_10d_news | Large cap (≥100B) CEO/CFO | low | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3753 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_low_10d_open | Micro cap (≤50M) Value ≥100k | low | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3754 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_low_10d_news | Micro cap (≤50M) Value ≥100k | low | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3755 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_low_10d_open | Micro cap (≤100M) Value ≥100k | low | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3756 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_low_10d_news | Micro cap (≤100M) Value ≥100k | low | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3757 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_low_10d_open | Micro cap (≤250M) Value ≥100k | low | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3758 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_low_10d_news | Micro cap (≤250M) Value ≥100k | low | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3759 | 58 | nan | CEO + CFO (combo) — hold ret_mean_10d_open | CEO + CFO (combo) | mean | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3760 | 58 | nan | CEO + CFO (combo) — hold ret_mean_10d_news | CEO + CFO (combo) | mean | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3761 | 54 | nan | 10% Owner — hold ret_mean_10d_open | 10% Owner | mean | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3762 | 54 | nan | 10% Owner — hold ret_mean_10d_news | 10% Owner | mean | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3763 | 57 | nan | 10% Owner + Value ≥500k — hold ret_mean_10d_open | 10% Owner + Value ≥500k | mean | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3764 | 57 | nan | 10% Owner + Value ≥500k — hold ret_mean_10d_news | 10% Owner + Value ≥500k | mean | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3765 | 59 | nan | CEO only + Position +20% — hold ret_mean_10d_open | CEO only + Position +20% | mean | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3766 | 59 | nan | CEO only + Position +20% — hold ret_mean_10d_news | CEO only + Position +20% | mean | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3767 | 55 | nan | 10% Owner + Position +10% — hold ret_mean_10d_open | 10% Owner + Position +10% | mean | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3768 | 55 | nan | 10% Owner + Position +10% — hold ret_mean_10d_news | 10% Owner + Position +10% | mean | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3769 | 56 | nan | 10% Owner + Position +20% — hold ret_mean_10d_open | 10% Owner + Position +20% | mean | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3770 | 56 | nan | 10% Owner + Position +20% — hold ret_mean_10d_news | 10% Owner + Position +20% | mean | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3771 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_mean_10d_open | CEO+CFO (combo) + Position +10% | mean | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3772 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_mean_10d_news | CEO+CFO (combo) + Position +10% | mean | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3773 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_mean_10d_open | CEO+CFO (combo) + Position +20% | mean | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3774 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_mean_10d_news | CEO+CFO (combo) + Position +20% | mean | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3775 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_mean_10d_open | Micro cap (≤50M) CEO/CFO | mean | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3776 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_mean_10d_news | Micro cap (≤50M) CEO/CFO | mean | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3777 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_mean_10d_open | Micro cap (≤100M) CEO/CFO | mean | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3778 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_mean_10d_news | Micro cap (≤100M) CEO/CFO | mean | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3779 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_mean_10d_open | Micro cap (≤250M) CEO/CFO | mean | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3780 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_mean_10d_news | Micro cap (≤250M) CEO/CFO | mean | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3781 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_mean_10d_open | Large cap (≥20B) CEO/CFO | mean | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3782 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_mean_10d_news | Large cap (≥20B) CEO/CFO | mean | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3783 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_mean_10d_open | Large cap (≥50B) CEO/CFO | mean | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3784 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_mean_10d_news | Large cap (≥50B) CEO/CFO | mean | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3785 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_mean_10d_open | Large cap (≥100B) CEO/CFO | mean | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3786 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_mean_10d_news | Large cap (≥100B) CEO/CFO | mean | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3787 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_mean_10d_open | Micro cap (≤50M) Value ≥100k | mean | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3788 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_mean_10d_news | Micro cap (≤50M) Value ≥100k | mean | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3789 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_mean_10d_open | Micro cap (≤100M) Value ≥100k | mean | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3790 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_mean_10d_news | Micro cap (≤100M) Value ≥100k | mean | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3791 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_mean_10d_open | Micro cap (≤250M) Value ≥100k | mean | 10 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3792 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_mean_10d_news | Micro cap (≤250M) Value ≥100k | mean | 10 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3793 | 58 | nan | CEO + CFO (combo) — hold ret_high_14d_open | CEO + CFO (combo) | high | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3794 | 58 | nan | CEO + CFO (combo) — hold ret_high_14d_news | CEO + CFO (combo) | high | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3795 | 54 | nan | 10% Owner — hold ret_high_14d_open | 10% Owner | high | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3796 | 54 | nan | 10% Owner — hold ret_high_14d_news | 10% Owner | high | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3797 | 57 | nan | 10% Owner + Value ≥500k — hold ret_high_14d_open | 10% Owner + Value ≥500k | high | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3798 | 57 | nan | 10% Owner + Value ≥500k — hold ret_high_14d_news | 10% Owner + Value ≥500k | high | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3799 | 59 | nan | CEO only + Position +20% — hold ret_high_14d_open | CEO only + Position +20% | high | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3800 | 59 | nan | CEO only + Position +20% — hold ret_high_14d_news | CEO only + Position +20% | high | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3801 | 55 | nan | 10% Owner + Position +10% — hold ret_high_14d_open | 10% Owner + Position +10% | high | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3802 | 55 | nan | 10% Owner + Position +10% — hold ret_high_14d_news | 10% Owner + Position +10% | high | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3803 | 56 | nan | 10% Owner + Position +20% — hold ret_high_14d_open | 10% Owner + Position +20% | high | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3804 | 56 | nan | 10% Owner + Position +20% — hold ret_high_14d_news | 10% Owner + Position +20% | high | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3805 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_high_14d_open | CEO+CFO (combo) + Position +10% | high | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3806 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_high_14d_news | CEO+CFO (combo) + Position +10% | high | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3807 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_high_14d_open | CEO+CFO (combo) + Position +20% | high | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3808 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_high_14d_news | CEO+CFO (combo) + Position +20% | high | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3809 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_high_14d_open | Micro cap (≤50M) CEO/CFO | high | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3810 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_high_14d_news | Micro cap (≤50M) CEO/CFO | high | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3811 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_high_14d_open | Micro cap (≤100M) CEO/CFO | high | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3812 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_high_14d_news | Micro cap (≤100M) CEO/CFO | high | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3813 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_high_14d_open | Micro cap (≤250M) CEO/CFO | high | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3814 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_high_14d_news | Micro cap (≤250M) CEO/CFO | high | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3815 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_high_14d_open | Large cap (≥20B) CEO/CFO | high | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3816 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_high_14d_news | Large cap (≥20B) CEO/CFO | high | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3817 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_high_14d_open | Large cap (≥50B) CEO/CFO | high | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3818 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_high_14d_news | Large cap (≥50B) CEO/CFO | high | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3819 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_high_14d_open | Large cap (≥100B) CEO/CFO | high | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3820 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_high_14d_news | Large cap (≥100B) CEO/CFO | high | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3821 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_high_14d_open | Micro cap (≤50M) Value ≥100k | high | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3822 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_high_14d_news | Micro cap (≤50M) Value ≥100k | high | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3823 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_high_14d_open | Micro cap (≤100M) Value ≥100k | high | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3824 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_high_14d_news | Micro cap (≤100M) Value ≥100k | high | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3825 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_high_14d_open | Micro cap (≤250M) Value ≥100k | high | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3826 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_high_14d_news | Micro cap (≤250M) Value ≥100k | high | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3827 | 58 | nan | CEO + CFO (combo) — hold ret_low_14d_open | CEO + CFO (combo) | low | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3828 | 58 | nan | CEO + CFO (combo) — hold ret_low_14d_news | CEO + CFO (combo) | low | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3829 | 54 | nan | 10% Owner — hold ret_low_14d_open | 10% Owner | low | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3830 | 54 | nan | 10% Owner — hold ret_low_14d_news | 10% Owner | low | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3831 | 57 | nan | 10% Owner + Value ≥500k — hold ret_low_14d_open | 10% Owner + Value ≥500k | low | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3832 | 57 | nan | 10% Owner + Value ≥500k — hold ret_low_14d_news | 10% Owner + Value ≥500k | low | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3833 | 59 | nan | CEO only + Position +20% — hold ret_low_14d_open | CEO only + Position +20% | low | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3834 | 59 | nan | CEO only + Position +20% — hold ret_low_14d_news | CEO only + Position +20% | low | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3835 | 55 | nan | 10% Owner + Position +10% — hold ret_low_14d_open | 10% Owner + Position +10% | low | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3836 | 55 | nan | 10% Owner + Position +10% — hold ret_low_14d_news | 10% Owner + Position +10% | low | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3837 | 56 | nan | 10% Owner + Position +20% — hold ret_low_14d_open | 10% Owner + Position +20% | low | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3838 | 56 | nan | 10% Owner + Position +20% — hold ret_low_14d_news | 10% Owner + Position +20% | low | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3839 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_low_14d_open | CEO+CFO (combo) + Position +10% | low | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3840 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_low_14d_news | CEO+CFO (combo) + Position +10% | low | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3841 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_low_14d_open | CEO+CFO (combo) + Position +20% | low | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3842 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_low_14d_news | CEO+CFO (combo) + Position +20% | low | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3843 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_low_14d_open | Micro cap (≤50M) CEO/CFO | low | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3844 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_low_14d_news | Micro cap (≤50M) CEO/CFO | low | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3845 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_low_14d_open | Micro cap (≤100M) CEO/CFO | low | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3846 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_low_14d_news | Micro cap (≤100M) CEO/CFO | low | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3847 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_low_14d_open | Micro cap (≤250M) CEO/CFO | low | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3848 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_low_14d_news | Micro cap (≤250M) CEO/CFO | low | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3849 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_low_14d_open | Large cap (≥20B) CEO/CFO | low | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3850 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_low_14d_news | Large cap (≥20B) CEO/CFO | low | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3851 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_low_14d_open | Large cap (≥50B) CEO/CFO | low | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3852 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_low_14d_news | Large cap (≥50B) CEO/CFO | low | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3853 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_low_14d_open | Large cap (≥100B) CEO/CFO | low | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3854 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_low_14d_news | Large cap (≥100B) CEO/CFO | low | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3855 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_low_14d_open | Micro cap (≤50M) Value ≥100k | low | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3856 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_low_14d_news | Micro cap (≤50M) Value ≥100k | low | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3857 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_low_14d_open | Micro cap (≤100M) Value ≥100k | low | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3858 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_low_14d_news | Micro cap (≤100M) Value ≥100k | low | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3859 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_low_14d_open | Micro cap (≤250M) Value ≥100k | low | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3860 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_low_14d_news | Micro cap (≤250M) Value ≥100k | low | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3861 | 58 | nan | CEO + CFO (combo) — hold ret_mean_14d_open | CEO + CFO (combo) | mean | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3862 | 58 | nan | CEO + CFO (combo) — hold ret_mean_14d_news | CEO + CFO (combo) | mean | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3863 | 54 | nan | 10% Owner — hold ret_mean_14d_open | 10% Owner | mean | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3864 | 54 | nan | 10% Owner — hold ret_mean_14d_news | 10% Owner | mean | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3865 | 57 | nan | 10% Owner + Value ≥500k — hold ret_mean_14d_open | 10% Owner + Value ≥500k | mean | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3866 | 57 | nan | 10% Owner + Value ≥500k — hold ret_mean_14d_news | 10% Owner + Value ≥500k | mean | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3867 | 59 | nan | CEO only + Position +20% — hold ret_mean_14d_open | CEO only + Position +20% | mean | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3868 | 59 | nan | CEO only + Position +20% — hold ret_mean_14d_news | CEO only + Position +20% | mean | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3869 | 55 | nan | 10% Owner + Position +10% — hold ret_mean_14d_open | 10% Owner + Position +10% | mean | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3870 | 55 | nan | 10% Owner + Position +10% — hold ret_mean_14d_news | 10% Owner + Position +10% | mean | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3871 | 56 | nan | 10% Owner + Position +20% — hold ret_mean_14d_open | 10% Owner + Position +20% | mean | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3872 | 56 | nan | 10% Owner + Position +20% — hold ret_mean_14d_news | 10% Owner + Position +20% | mean | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3873 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_mean_14d_open | CEO+CFO (combo) + Position +10% | mean | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3874 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_mean_14d_news | CEO+CFO (combo) + Position +10% | mean | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3875 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_mean_14d_open | CEO+CFO (combo) + Position +20% | mean | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3876 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_mean_14d_news | CEO+CFO (combo) + Position +20% | mean | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3877 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_mean_14d_open | Micro cap (≤50M) CEO/CFO | mean | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3878 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_mean_14d_news | Micro cap (≤50M) CEO/CFO | mean | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3879 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_mean_14d_open | Micro cap (≤100M) CEO/CFO | mean | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3880 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_mean_14d_news | Micro cap (≤100M) CEO/CFO | mean | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3881 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_mean_14d_open | Micro cap (≤250M) CEO/CFO | mean | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3882 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_mean_14d_news | Micro cap (≤250M) CEO/CFO | mean | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3883 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_mean_14d_open | Large cap (≥20B) CEO/CFO | mean | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3884 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_mean_14d_news | Large cap (≥20B) CEO/CFO | mean | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3885 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_mean_14d_open | Large cap (≥50B) CEO/CFO | mean | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3886 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_mean_14d_news | Large cap (≥50B) CEO/CFO | mean | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3887 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_mean_14d_open | Large cap (≥100B) CEO/CFO | mean | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3888 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_mean_14d_news | Large cap (≥100B) CEO/CFO | mean | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3889 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_mean_14d_open | Micro cap (≤50M) Value ≥100k | mean | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3890 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_mean_14d_news | Micro cap (≤50M) Value ≥100k | mean | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3891 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_mean_14d_open | Micro cap (≤100M) Value ≥100k | mean | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3892 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_mean_14d_news | Micro cap (≤100M) Value ≥100k | mean | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3893 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_mean_14d_open | Micro cap (≤250M) Value ≥100k | mean | 14 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3894 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_mean_14d_news | Micro cap (≤250M) Value ≥100k | mean | 14 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3895 | 58 | nan | CEO + CFO (combo) — hold ret_high_30d_open | CEO + CFO (combo) | high | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3896 | 58 | nan | CEO + CFO (combo) — hold ret_high_30d_news | CEO + CFO (combo) | high | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3897 | 54 | nan | 10% Owner — hold ret_high_30d_open | 10% Owner | high | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3898 | 54 | nan | 10% Owner — hold ret_high_30d_news | 10% Owner | high | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3899 | 57 | nan | 10% Owner + Value ≥500k — hold ret_high_30d_open | 10% Owner + Value ≥500k | high | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3900 | 57 | nan | 10% Owner + Value ≥500k — hold ret_high_30d_news | 10% Owner + Value ≥500k | high | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3901 | 59 | nan | CEO only + Position +20% — hold ret_high_30d_open | CEO only + Position +20% | high | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3902 | 59 | nan | CEO only + Position +20% — hold ret_high_30d_news | CEO only + Position +20% | high | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3903 | 55 | nan | 10% Owner + Position +10% — hold ret_high_30d_open | 10% Owner + Position +10% | high | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3904 | 55 | nan | 10% Owner + Position +10% — hold ret_high_30d_news | 10% Owner + Position +10% | high | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3905 | 56 | nan | 10% Owner + Position +20% — hold ret_high_30d_open | 10% Owner + Position +20% | high | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3906 | 56 | nan | 10% Owner + Position +20% — hold ret_high_30d_news | 10% Owner + Position +20% | high | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3907 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_high_30d_open | CEO+CFO (combo) + Position +10% | high | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3908 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_high_30d_news | CEO+CFO (combo) + Position +10% | high | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3909 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_high_30d_open | CEO+CFO (combo) + Position +20% | high | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3910 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_high_30d_news | CEO+CFO (combo) + Position +20% | high | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3911 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_high_30d_open | Micro cap (≤50M) CEO/CFO | high | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3912 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_high_30d_news | Micro cap (≤50M) CEO/CFO | high | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3913 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_high_30d_open | Micro cap (≤100M) CEO/CFO | high | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3914 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_high_30d_news | Micro cap (≤100M) CEO/CFO | high | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3915 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_high_30d_open | Micro cap (≤250M) CEO/CFO | high | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3916 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_high_30d_news | Micro cap (≤250M) CEO/CFO | high | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3917 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_high_30d_open | Large cap (≥20B) CEO/CFO | high | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3918 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_high_30d_news | Large cap (≥20B) CEO/CFO | high | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3919 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_high_30d_open | Large cap (≥50B) CEO/CFO | high | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3920 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_high_30d_news | Large cap (≥50B) CEO/CFO | high | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3921 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_high_30d_open | Large cap (≥100B) CEO/CFO | high | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3922 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_high_30d_news | Large cap (≥100B) CEO/CFO | high | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3923 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_high_30d_open | Micro cap (≤50M) Value ≥100k | high | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3924 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_high_30d_news | Micro cap (≤50M) Value ≥100k | high | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3925 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_high_30d_open | Micro cap (≤100M) Value ≥100k | high | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3926 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_high_30d_news | Micro cap (≤100M) Value ≥100k | high | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3927 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_high_30d_open | Micro cap (≤250M) Value ≥100k | high | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3928 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_high_30d_news | Micro cap (≤250M) Value ≥100k | high | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3929 | 58 | nan | CEO + CFO (combo) — hold ret_low_30d_open | CEO + CFO (combo) | low | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3930 | 58 | nan | CEO + CFO (combo) — hold ret_low_30d_news | CEO + CFO (combo) | low | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3931 | 54 | nan | 10% Owner — hold ret_low_30d_open | 10% Owner | low | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3932 | 54 | nan | 10% Owner — hold ret_low_30d_news | 10% Owner | low | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3933 | 57 | nan | 10% Owner + Value ≥500k — hold ret_low_30d_open | 10% Owner + Value ≥500k | low | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3934 | 57 | nan | 10% Owner + Value ≥500k — hold ret_low_30d_news | 10% Owner + Value ≥500k | low | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3935 | 59 | nan | CEO only + Position +20% — hold ret_low_30d_open | CEO only + Position +20% | low | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3936 | 59 | nan | CEO only + Position +20% — hold ret_low_30d_news | CEO only + Position +20% | low | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3937 | 55 | nan | 10% Owner + Position +10% — hold ret_low_30d_open | 10% Owner + Position +10% | low | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3938 | 55 | nan | 10% Owner + Position +10% — hold ret_low_30d_news | 10% Owner + Position +10% | low | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3939 | 56 | nan | 10% Owner + Position +20% — hold ret_low_30d_open | 10% Owner + Position +20% | low | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3940 | 56 | nan | 10% Owner + Position +20% — hold ret_low_30d_news | 10% Owner + Position +20% | low | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3941 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_low_30d_open | CEO+CFO (combo) + Position +10% | low | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3942 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_low_30d_news | CEO+CFO (combo) + Position +10% | low | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3943 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_low_30d_open | CEO+CFO (combo) + Position +20% | low | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3944 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_low_30d_news | CEO+CFO (combo) + Position +20% | low | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3945 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_low_30d_open | Micro cap (≤50M) CEO/CFO | low | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3946 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_low_30d_news | Micro cap (≤50M) CEO/CFO | low | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3947 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_low_30d_open | Micro cap (≤100M) CEO/CFO | low | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3948 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_low_30d_news | Micro cap (≤100M) CEO/CFO | low | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3949 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_low_30d_open | Micro cap (≤250M) CEO/CFO | low | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3950 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_low_30d_news | Micro cap (≤250M) CEO/CFO | low | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3951 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_low_30d_open | Large cap (≥20B) CEO/CFO | low | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3952 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_low_30d_news | Large cap (≥20B) CEO/CFO | low | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3953 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_low_30d_open | Large cap (≥50B) CEO/CFO | low | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3954 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_low_30d_news | Large cap (≥50B) CEO/CFO | low | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3955 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_low_30d_open | Large cap (≥100B) CEO/CFO | low | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3956 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_low_30d_news | Large cap (≥100B) CEO/CFO | low | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3957 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_low_30d_open | Micro cap (≤50M) Value ≥100k | low | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3958 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_low_30d_news | Micro cap (≤50M) Value ≥100k | low | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3959 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_low_30d_open | Micro cap (≤100M) Value ≥100k | low | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3960 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_low_30d_news | Micro cap (≤100M) Value ≥100k | low | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3961 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_low_30d_open | Micro cap (≤250M) Value ≥100k | low | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3962 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_low_30d_news | Micro cap (≤250M) Value ≥100k | low | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3963 | 58 | nan | CEO + CFO (combo) — hold ret_mean_30d_open | CEO + CFO (combo) | mean | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3964 | 58 | nan | CEO + CFO (combo) — hold ret_mean_30d_news | CEO + CFO (combo) | mean | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3965 | 54 | nan | 10% Owner — hold ret_mean_30d_open | 10% Owner | mean | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3966 | 54 | nan | 10% Owner — hold ret_mean_30d_news | 10% Owner | mean | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3967 | 57 | nan | 10% Owner + Value ≥500k — hold ret_mean_30d_open | 10% Owner + Value ≥500k | mean | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3968 | 57 | nan | 10% Owner + Value ≥500k — hold ret_mean_30d_news | 10% Owner + Value ≥500k | mean | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3969 | 59 | nan | CEO only + Position +20% — hold ret_mean_30d_open | CEO only + Position +20% | mean | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3970 | 59 | nan | CEO only + Position +20% — hold ret_mean_30d_news | CEO only + Position +20% | mean | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3971 | 55 | nan | 10% Owner + Position +10% — hold ret_mean_30d_open | 10% Owner + Position +10% | mean | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3972 | 55 | nan | 10% Owner + Position +10% — hold ret_mean_30d_news | 10% Owner + Position +10% | mean | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3973 | 56 | nan | 10% Owner + Position +20% — hold ret_mean_30d_open | 10% Owner + Position +20% | mean | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3974 | 56 | nan | 10% Owner + Position +20% — hold ret_mean_30d_news | 10% Owner + Position +20% | mean | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3975 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_mean_30d_open | CEO+CFO (combo) + Position +10% | mean | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3976 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_mean_30d_news | CEO+CFO (combo) + Position +10% | mean | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3977 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_mean_30d_open | CEO+CFO (combo) + Position +20% | mean | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3978 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_mean_30d_news | CEO+CFO (combo) + Position +20% | mean | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3979 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_mean_30d_open | Micro cap (≤50M) CEO/CFO | mean | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3980 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_mean_30d_news | Micro cap (≤50M) CEO/CFO | mean | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3981 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_mean_30d_open | Micro cap (≤100M) CEO/CFO | mean | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3982 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_mean_30d_news | Micro cap (≤100M) CEO/CFO | mean | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3983 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_mean_30d_open | Micro cap (≤250M) CEO/CFO | mean | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3984 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_mean_30d_news | Micro cap (≤250M) CEO/CFO | mean | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3985 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_mean_30d_open | Large cap (≥20B) CEO/CFO | mean | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3986 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_mean_30d_news | Large cap (≥20B) CEO/CFO | mean | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3987 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_mean_30d_open | Large cap (≥50B) CEO/CFO | mean | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3988 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_mean_30d_news | Large cap (≥50B) CEO/CFO | mean | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3989 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_mean_30d_open | Large cap (≥100B) CEO/CFO | mean | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3990 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_mean_30d_news | Large cap (≥100B) CEO/CFO | mean | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3991 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_mean_30d_open | Micro cap (≤50M) Value ≥100k | mean | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3992 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_mean_30d_news | Micro cap (≤50M) Value ≥100k | mean | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3993 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_mean_30d_open | Micro cap (≤100M) Value ≥100k | mean | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3994 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_mean_30d_news | Micro cap (≤100M) Value ≥100k | mean | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3995 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_mean_30d_open | Micro cap (≤250M) Value ≥100k | mean | 30 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3996 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_mean_30d_news | Micro cap (≤250M) Value ≥100k | mean | 30 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3997 | 58 | nan | CEO + CFO (combo) — hold ret_high_60d_open | CEO + CFO (combo) | high | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3998 | 58 | nan | CEO + CFO (combo) — hold ret_high_60d_news | CEO + CFO (combo) | high | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 3999 | 54 | nan | 10% Owner — hold ret_high_60d_open | 10% Owner | high | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4000 | 54 | nan | 10% Owner — hold ret_high_60d_news | 10% Owner | high | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4001 | 57 | nan | 10% Owner + Value ≥500k — hold ret_high_60d_open | 10% Owner + Value ≥500k | high | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4002 | 57 | nan | 10% Owner + Value ≥500k — hold ret_high_60d_news | 10% Owner + Value ≥500k | high | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4003 | 59 | nan | CEO only + Position +20% — hold ret_high_60d_open | CEO only + Position +20% | high | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4004 | 59 | nan | CEO only + Position +20% — hold ret_high_60d_news | CEO only + Position +20% | high | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4005 | 55 | nan | 10% Owner + Position +10% — hold ret_high_60d_open | 10% Owner + Position +10% | high | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4006 | 55 | nan | 10% Owner + Position +10% — hold ret_high_60d_news | 10% Owner + Position +10% | high | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4007 | 56 | nan | 10% Owner + Position +20% — hold ret_high_60d_open | 10% Owner + Position +20% | high | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4008 | 56 | nan | 10% Owner + Position +20% — hold ret_high_60d_news | 10% Owner + Position +20% | high | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4009 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_high_60d_open | CEO+CFO (combo) + Position +10% | high | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4010 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_high_60d_news | CEO+CFO (combo) + Position +10% | high | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4011 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_high_60d_open | CEO+CFO (combo) + Position +20% | high | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4012 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_high_60d_news | CEO+CFO (combo) + Position +20% | high | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4013 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_high_60d_open | Micro cap (≤50M) CEO/CFO | high | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4014 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_high_60d_news | Micro cap (≤50M) CEO/CFO | high | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4015 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_high_60d_open | Micro cap (≤100M) CEO/CFO | high | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4016 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_high_60d_news | Micro cap (≤100M) CEO/CFO | high | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4017 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_high_60d_open | Micro cap (≤250M) CEO/CFO | high | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4018 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_high_60d_news | Micro cap (≤250M) CEO/CFO | high | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4019 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_high_60d_open | Large cap (≥20B) CEO/CFO | high | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4020 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_high_60d_news | Large cap (≥20B) CEO/CFO | high | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4021 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_high_60d_open | Large cap (≥50B) CEO/CFO | high | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4022 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_high_60d_news | Large cap (≥50B) CEO/CFO | high | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4023 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_high_60d_open | Large cap (≥100B) CEO/CFO | high | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4024 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_high_60d_news | Large cap (≥100B) CEO/CFO | high | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4025 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_high_60d_open | Micro cap (≤50M) Value ≥100k | high | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4026 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_high_60d_news | Micro cap (≤50M) Value ≥100k | high | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4027 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_high_60d_open | Micro cap (≤100M) Value ≥100k | high | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4028 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_high_60d_news | Micro cap (≤100M) Value ≥100k | high | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4029 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_high_60d_open | Micro cap (≤250M) Value ≥100k | high | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4030 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_high_60d_news | Micro cap (≤250M) Value ≥100k | high | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4031 | 58 | nan | CEO + CFO (combo) — hold ret_low_60d_open | CEO + CFO (combo) | low | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4032 | 58 | nan | CEO + CFO (combo) — hold ret_low_60d_news | CEO + CFO (combo) | low | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4033 | 54 | nan | 10% Owner — hold ret_low_60d_open | 10% Owner | low | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4034 | 54 | nan | 10% Owner — hold ret_low_60d_news | 10% Owner | low | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4035 | 57 | nan | 10% Owner + Value ≥500k — hold ret_low_60d_open | 10% Owner + Value ≥500k | low | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4036 | 57 | nan | 10% Owner + Value ≥500k — hold ret_low_60d_news | 10% Owner + Value ≥500k | low | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4037 | 59 | nan | CEO only + Position +20% — hold ret_low_60d_open | CEO only + Position +20% | low | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4038 | 59 | nan | CEO only + Position +20% — hold ret_low_60d_news | CEO only + Position +20% | low | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4039 | 55 | nan | 10% Owner + Position +10% — hold ret_low_60d_open | 10% Owner + Position +10% | low | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4040 | 55 | nan | 10% Owner + Position +10% — hold ret_low_60d_news | 10% Owner + Position +10% | low | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4041 | 56 | nan | 10% Owner + Position +20% — hold ret_low_60d_open | 10% Owner + Position +20% | low | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4042 | 56 | nan | 10% Owner + Position +20% — hold ret_low_60d_news | 10% Owner + Position +20% | low | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4043 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_low_60d_open | CEO+CFO (combo) + Position +10% | low | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4044 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_low_60d_news | CEO+CFO (combo) + Position +10% | low | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4045 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_low_60d_open | CEO+CFO (combo) + Position +20% | low | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4046 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_low_60d_news | CEO+CFO (combo) + Position +20% | low | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4047 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_low_60d_open | Micro cap (≤50M) CEO/CFO | low | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4048 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_low_60d_news | Micro cap (≤50M) CEO/CFO | low | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4049 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_low_60d_open | Micro cap (≤100M) CEO/CFO | low | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4050 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_low_60d_news | Micro cap (≤100M) CEO/CFO | low | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4051 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_low_60d_open | Micro cap (≤250M) CEO/CFO | low | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4052 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_low_60d_news | Micro cap (≤250M) CEO/CFO | low | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4053 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_low_60d_open | Large cap (≥20B) CEO/CFO | low | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4054 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_low_60d_news | Large cap (≥20B) CEO/CFO | low | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4055 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_low_60d_open | Large cap (≥50B) CEO/CFO | low | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4056 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_low_60d_news | Large cap (≥50B) CEO/CFO | low | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4057 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_low_60d_open | Large cap (≥100B) CEO/CFO | low | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4058 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_low_60d_news | Large cap (≥100B) CEO/CFO | low | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4059 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_low_60d_open | Micro cap (≤50M) Value ≥100k | low | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4060 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_low_60d_news | Micro cap (≤50M) Value ≥100k | low | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4061 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_low_60d_open | Micro cap (≤100M) Value ≥100k | low | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4062 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_low_60d_news | Micro cap (≤100M) Value ≥100k | low | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4063 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_low_60d_open | Micro cap (≤250M) Value ≥100k | low | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4064 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_low_60d_news | Micro cap (≤250M) Value ≥100k | low | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4065 | 58 | nan | CEO + CFO (combo) — hold ret_mean_60d_open | CEO + CFO (combo) | mean | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4066 | 58 | nan | CEO + CFO (combo) — hold ret_mean_60d_news | CEO + CFO (combo) | mean | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4067 | 54 | nan | 10% Owner — hold ret_mean_60d_open | 10% Owner | mean | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4068 | 54 | nan | 10% Owner — hold ret_mean_60d_news | 10% Owner | mean | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4069 | 57 | nan | 10% Owner + Value ≥500k — hold ret_mean_60d_open | 10% Owner + Value ≥500k | mean | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4070 | 57 | nan | 10% Owner + Value ≥500k — hold ret_mean_60d_news | 10% Owner + Value ≥500k | mean | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4071 | 59 | nan | CEO only + Position +20% — hold ret_mean_60d_open | CEO only + Position +20% | mean | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4072 | 59 | nan | CEO only + Position +20% — hold ret_mean_60d_news | CEO only + Position +20% | mean | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4073 | 55 | nan | 10% Owner + Position +10% — hold ret_mean_60d_open | 10% Owner + Position +10% | mean | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4074 | 55 | nan | 10% Owner + Position +10% — hold ret_mean_60d_news | 10% Owner + Position +10% | mean | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4075 | 56 | nan | 10% Owner + Position +20% — hold ret_mean_60d_open | 10% Owner + Position +20% | mean | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4076 | 56 | nan | 10% Owner + Position +20% — hold ret_mean_60d_news | 10% Owner + Position +20% | mean | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4077 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_mean_60d_open | CEO+CFO (combo) + Position +10% | mean | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4078 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_mean_60d_news | CEO+CFO (combo) + Position +10% | mean | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4079 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_mean_60d_open | CEO+CFO (combo) + Position +20% | mean | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4080 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_mean_60d_news | CEO+CFO (combo) + Position +20% | mean | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4081 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_mean_60d_open | Micro cap (≤50M) CEO/CFO | mean | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4082 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_mean_60d_news | Micro cap (≤50M) CEO/CFO | mean | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4083 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_mean_60d_open | Micro cap (≤100M) CEO/CFO | mean | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4084 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_mean_60d_news | Micro cap (≤100M) CEO/CFO | mean | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4085 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_mean_60d_open | Micro cap (≤250M) CEO/CFO | mean | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4086 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_mean_60d_news | Micro cap (≤250M) CEO/CFO | mean | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4087 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_mean_60d_open | Large cap (≥20B) CEO/CFO | mean | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4088 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_mean_60d_news | Large cap (≥20B) CEO/CFO | mean | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4089 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_mean_60d_open | Large cap (≥50B) CEO/CFO | mean | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4090 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_mean_60d_news | Large cap (≥50B) CEO/CFO | mean | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4091 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_mean_60d_open | Large cap (≥100B) CEO/CFO | mean | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4092 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_mean_60d_news | Large cap (≥100B) CEO/CFO | mean | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4093 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_mean_60d_open | Micro cap (≤50M) Value ≥100k | mean | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4094 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_mean_60d_news | Micro cap (≤50M) Value ≥100k | mean | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4095 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_mean_60d_open | Micro cap (≤100M) Value ≥100k | mean | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4096 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_mean_60d_news | Micro cap (≤100M) Value ≥100k | mean | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4097 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_mean_60d_open | Micro cap (≤250M) Value ≥100k | mean | 60 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4098 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_mean_60d_news | Micro cap (≤250M) Value ≥100k | mean | 60 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4099 | 58 | nan | CEO + CFO (combo) — hold ret_high_90d_open | CEO + CFO (combo) | high | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4100 | 58 | nan | CEO + CFO (combo) — hold ret_high_90d_news | CEO + CFO (combo) | high | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4101 | 54 | nan | 10% Owner — hold ret_high_90d_open | 10% Owner | high | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4102 | 54 | nan | 10% Owner — hold ret_high_90d_news | 10% Owner | high | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4103 | 57 | nan | 10% Owner + Value ≥500k — hold ret_high_90d_open | 10% Owner + Value ≥500k | high | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4104 | 57 | nan | 10% Owner + Value ≥500k — hold ret_high_90d_news | 10% Owner + Value ≥500k | high | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4105 | 59 | nan | CEO only + Position +20% — hold ret_high_90d_open | CEO only + Position +20% | high | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4106 | 59 | nan | CEO only + Position +20% — hold ret_high_90d_news | CEO only + Position +20% | high | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4107 | 55 | nan | 10% Owner + Position +10% — hold ret_high_90d_open | 10% Owner + Position +10% | high | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4108 | 55 | nan | 10% Owner + Position +10% — hold ret_high_90d_news | 10% Owner + Position +10% | high | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4109 | 56 | nan | 10% Owner + Position +20% — hold ret_high_90d_open | 10% Owner + Position +20% | high | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4110 | 56 | nan | 10% Owner + Position +20% — hold ret_high_90d_news | 10% Owner + Position +20% | high | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4111 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_high_90d_open | CEO+CFO (combo) + Position +10% | high | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4112 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_high_90d_news | CEO+CFO (combo) + Position +10% | high | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4113 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_high_90d_open | CEO+CFO (combo) + Position +20% | high | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4114 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_high_90d_news | CEO+CFO (combo) + Position +20% | high | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4115 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_high_90d_open | Micro cap (≤50M) CEO/CFO | high | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4116 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_high_90d_news | Micro cap (≤50M) CEO/CFO | high | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4117 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_high_90d_open | Micro cap (≤100M) CEO/CFO | high | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4118 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_high_90d_news | Micro cap (≤100M) CEO/CFO | high | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4119 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_high_90d_open | Micro cap (≤250M) CEO/CFO | high | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4120 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_high_90d_news | Micro cap (≤250M) CEO/CFO | high | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4121 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_high_90d_open | Large cap (≥20B) CEO/CFO | high | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4122 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_high_90d_news | Large cap (≥20B) CEO/CFO | high | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4123 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_high_90d_open | Large cap (≥50B) CEO/CFO | high | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4124 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_high_90d_news | Large cap (≥50B) CEO/CFO | high | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4125 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_high_90d_open | Large cap (≥100B) CEO/CFO | high | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4126 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_high_90d_news | Large cap (≥100B) CEO/CFO | high | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4127 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_high_90d_open | Micro cap (≤50M) Value ≥100k | high | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4128 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_high_90d_news | Micro cap (≤50M) Value ≥100k | high | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4129 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_high_90d_open | Micro cap (≤100M) Value ≥100k | high | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4130 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_high_90d_news | Micro cap (≤100M) Value ≥100k | high | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4131 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_high_90d_open | Micro cap (≤250M) Value ≥100k | high | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4132 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_high_90d_news | Micro cap (≤250M) Value ≥100k | high | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4133 | 58 | nan | CEO + CFO (combo) — hold ret_low_90d_open | CEO + CFO (combo) | low | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4134 | 58 | nan | CEO + CFO (combo) — hold ret_low_90d_news | CEO + CFO (combo) | low | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4135 | 54 | nan | 10% Owner — hold ret_low_90d_open | 10% Owner | low | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4136 | 54 | nan | 10% Owner — hold ret_low_90d_news | 10% Owner | low | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4137 | 57 | nan | 10% Owner + Value ≥500k — hold ret_low_90d_open | 10% Owner + Value ≥500k | low | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4138 | 57 | nan | 10% Owner + Value ≥500k — hold ret_low_90d_news | 10% Owner + Value ≥500k | low | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4139 | 59 | nan | CEO only + Position +20% — hold ret_low_90d_open | CEO only + Position +20% | low | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4140 | 59 | nan | CEO only + Position +20% — hold ret_low_90d_news | CEO only + Position +20% | low | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4141 | 55 | nan | 10% Owner + Position +10% — hold ret_low_90d_open | 10% Owner + Position +10% | low | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4142 | 55 | nan | 10% Owner + Position +10% — hold ret_low_90d_news | 10% Owner + Position +10% | low | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4143 | 56 | nan | 10% Owner + Position +20% — hold ret_low_90d_open | 10% Owner + Position +20% | low | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4144 | 56 | nan | 10% Owner + Position +20% — hold ret_low_90d_news | 10% Owner + Position +20% | low | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4145 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_low_90d_open | CEO+CFO (combo) + Position +10% | low | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4146 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_low_90d_news | CEO+CFO (combo) + Position +10% | low | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4147 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_low_90d_open | CEO+CFO (combo) + Position +20% | low | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4148 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_low_90d_news | CEO+CFO (combo) + Position +20% | low | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4149 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_low_90d_open | Micro cap (≤50M) CEO/CFO | low | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4150 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_low_90d_news | Micro cap (≤50M) CEO/CFO | low | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4151 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_low_90d_open | Micro cap (≤100M) CEO/CFO | low | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4152 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_low_90d_news | Micro cap (≤100M) CEO/CFO | low | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4153 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_low_90d_open | Micro cap (≤250M) CEO/CFO | low | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4154 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_low_90d_news | Micro cap (≤250M) CEO/CFO | low | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4155 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_low_90d_open | Large cap (≥20B) CEO/CFO | low | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4156 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_low_90d_news | Large cap (≥20B) CEO/CFO | low | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4157 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_low_90d_open | Large cap (≥50B) CEO/CFO | low | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4158 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_low_90d_news | Large cap (≥50B) CEO/CFO | low | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4159 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_low_90d_open | Large cap (≥100B) CEO/CFO | low | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4160 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_low_90d_news | Large cap (≥100B) CEO/CFO | low | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4161 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_low_90d_open | Micro cap (≤50M) Value ≥100k | low | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4162 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_low_90d_news | Micro cap (≤50M) Value ≥100k | low | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4163 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_low_90d_open | Micro cap (≤100M) Value ≥100k | low | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4164 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_low_90d_news | Micro cap (≤100M) Value ≥100k | low | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4165 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_low_90d_open | Micro cap (≤250M) Value ≥100k | low | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4166 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_low_90d_news | Micro cap (≤250M) Value ≥100k | low | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4167 | 58 | nan | CEO + CFO (combo) — hold ret_mean_90d_open | CEO + CFO (combo) | mean | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4168 | 58 | nan | CEO + CFO (combo) — hold ret_mean_90d_news | CEO + CFO (combo) | mean | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4169 | 54 | nan | 10% Owner — hold ret_mean_90d_open | 10% Owner | mean | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4170 | 54 | nan | 10% Owner — hold ret_mean_90d_news | 10% Owner | mean | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4171 | 57 | nan | 10% Owner + Value ≥500k — hold ret_mean_90d_open | 10% Owner + Value ≥500k | mean | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4172 | 57 | nan | 10% Owner + Value ≥500k — hold ret_mean_90d_news | 10% Owner + Value ≥500k | mean | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4173 | 59 | nan | CEO only + Position +20% — hold ret_mean_90d_open | CEO only + Position +20% | mean | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4174 | 59 | nan | CEO only + Position +20% — hold ret_mean_90d_news | CEO only + Position +20% | mean | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4175 | 55 | nan | 10% Owner + Position +10% — hold ret_mean_90d_open | 10% Owner + Position +10% | mean | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4176 | 55 | nan | 10% Owner + Position +10% — hold ret_mean_90d_news | 10% Owner + Position +10% | mean | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4177 | 56 | nan | 10% Owner + Position +20% — hold ret_mean_90d_open | 10% Owner + Position +20% | mean | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4178 | 56 | nan | 10% Owner + Position +20% — hold ret_mean_90d_news | 10% Owner + Position +20% | mean | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4179 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_mean_90d_open | CEO+CFO (combo) + Position +10% | mean | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4180 | 60 | nan | CEO+CFO (combo) + Position +10% — hold ret_mean_90d_news | CEO+CFO (combo) + Position +10% | mean | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4181 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_mean_90d_open | CEO+CFO (combo) + Position +20% | mean | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4182 | 61 | nan | CEO+CFO (combo) + Position +20% — hold ret_mean_90d_news | CEO+CFO (combo) + Position +20% | mean | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4183 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_mean_90d_open | Micro cap (≤50M) CEO/CFO | mean | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4184 | 69 | nan | Micro cap (≤50M) CEO/CFO — hold ret_mean_90d_news | Micro cap (≤50M) CEO/CFO | mean | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4185 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_mean_90d_open | Micro cap (≤100M) CEO/CFO | mean | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4186 | 65 | nan | Micro cap (≤100M) CEO/CFO — hold ret_mean_90d_news | Micro cap (≤100M) CEO/CFO | mean | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4187 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_mean_90d_open | Micro cap (≤250M) CEO/CFO | mean | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4188 | 67 | nan | Micro cap (≤250M) CEO/CFO — hold ret_mean_90d_news | Micro cap (≤250M) CEO/CFO | mean | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4189 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_mean_90d_open | Large cap (≥20B) CEO/CFO | mean | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4190 | 63 | nan | Large cap (≥20B) CEO/CFO — hold ret_mean_90d_news | Large cap (≥20B) CEO/CFO | mean | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4191 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_mean_90d_open | Large cap (≥50B) CEO/CFO | mean | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4192 | 64 | nan | Large cap (≥50B) CEO/CFO — hold ret_mean_90d_news | Large cap (≥50B) CEO/CFO | mean | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4193 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_mean_90d_open | Large cap (≥100B) CEO/CFO | mean | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4194 | 62 | nan | Large cap (≥100B) CEO/CFO — hold ret_mean_90d_news | Large cap (≥100B) CEO/CFO | mean | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4195 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_mean_90d_open | Micro cap (≤50M) Value ≥100k | mean | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4196 | 70 | nan | Micro cap (≤50M) Value ≥100k — hold ret_mean_90d_news | Micro cap (≤50M) Value ≥100k | mean | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4197 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_mean_90d_open | Micro cap (≤100M) Value ≥100k | mean | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4198 | 66 | nan | Micro cap (≤100M) Value ≥100k — hold ret_mean_90d_news | Micro cap (≤100M) Value ≥100k | mean | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4199 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_mean_90d_open | Micro cap (≤250M) Value ≥100k | mean | 90 | open | 0 | nan | nan | nan | nan | nan | nan | nan | nan |
| 4200 | 68 | nan | Micro cap (≤250M) Value ≥100k — hold ret_mean_90d_news | Micro cap (≤250M) Value ≥100k | mean | 90 | news | 0 | nan | nan | nan | nan | nan | nan | nan | nan |