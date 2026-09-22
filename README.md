# MLP Baseline - Deep Learning NIDS Project

## Overview
This repository contains Sushant Shekhar Sinha's implementation of **Model 1: MLP baseline (classical / feedforward)** for our Deep Learning project[cite: 2].
The broader project investigates the robustness of Deep Learning architectures to joint adversarial-evasion and concept-drift attacks in Network Intrusion Detection Systems (NIDS)[cite: 2].

## Dataset
* **CSE-CIC-IDS2018**: Contains legitimate traffic and several attack types (DoS, DDoS, brute force, infiltration, botnet, web attack)[cite: 2].
* *Note: We are using the corrected release by Liu et al. to account for label-corruption issues (>50% zero-payload attempted attacks in minority classes)*[cite: 2].

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

*Dependencies: list will be updated in `requirements.txt`.*

## Data
Ensure the dataset is placed in the `data/` directory (which is git-ignored). The CSV must contain one label column and numeric flow features. By default, the label column is `Label`.

Data processing is tabular: each row represents an independent network flow. The model evaluates these flows individually without sequence grouping.

## Train
Training script: `train_mlp.py`

```bash
python train_mlp.py --csv data/cic_ids2018.csv --label-column Label
```

Useful command-line options include `--epochs`, `--batch-size`, `--learning-rate`, and `--output-dir`.

The script creates a stratified train/validation/test split, fits preprocessing on the training split only, trains the classical feedforward MLP, and writes the following to the ignored artifacts directory:

* `artifacts/mlp/best_model.pt`
* `artifacts/mlp/preprocessing.joblib`
* `artifacts/mlp/metrics.json`
* `artifacts/mlp/test_predictions.csv`
* `artifacts/mlp/confusion_matrix.csv`
