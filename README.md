# Crypto MCP Tool 🚀

A simple **Model Context Protocol (MCP)** server that fetches real-time cryptocurrency prices using the **CoinGecko API**. This project demonstrates how to build and expose tools via MCP with clean, lightweight Python code.

## 📂 Project Structure

```
.
├── .gitignore
├── .python-version
├── README.md
├── crypto.py        # MCP tool for fetching crypto prices
├── main.py          # Entry point (extend/launch server here)
├── pyproject.toml   # Project metadata & dependencies
└── uv.lock          # Lockfile for reproducible environments
```

## ⚡ Features

* Exposes a **`get_cryptocurrency_price`** MCP tool.
* Fetches **live prices** of cryptocurrencies (e.g., Bitcoin, Ethereum) in USD.
* Built on top of **FastMCP** for quick tool registration and execution.
* Uses the **CoinGecko API** for reliable and free crypto market data.

## 🔧 Usage

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the MCP server:

   ```bash
   python crypto.py
   ```

3. Call the tool (example):

   ```python
   from crypto import get_cryptocurrency_price
   print(get_cryptocurrency_price("bitcoin"))
   # -> The price of bitcoin is $XX,XXX USD.
   ```

## 🌐 API Reference

* [CoinGecko API – Simple Price](https://www.coingecko.com/en/api/documentation)


Do you want me to also add a **“Future Improvements”** section (like adding multiple currencies, historical data, etc.) so recruiters see it’s forward-looking?
