
# Datasets

This project follows a clean data management approach.

Datasets are intentionally **excluded from version control** and are downloaded locally using **KaggleHub**.

---

## 🔐 Authentication

Authentication is handled globally via Kaggle CLI credentials:

- `~/.kaggle/kaggle.json`

No credentials or login logic are stored in this repository.

---

## ⬇️ Download Datasets

To download all required datasets locally, run:

```bash
python datasets/download.py