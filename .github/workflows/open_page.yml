name: Abrir página web con Selenium en Edge

on:
  push:
    branches:
      - main  # Cambiar por la rama principal de tu repositorio
  pull_request:
    branches:
      - main  # Cambiar por la rama principal de tu repositorio
  workflow_dispatch:

jobs:
  run-selenium:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install selenium

      - name: Download and setup Edge WebDriver
        run: |
          sudo apt-get update
          sudo apt-get install -y wget unzip
          wget https://msedgedriver.azureedge.net/114.0.1823.67/edgedriver_linux64.zip
          unzip edgedriver_linux64.zip
          sudo mv msedgedriver /usr/local/bin/msedgedriver
          sudo chmod +x /usr/local/bin/msedgedriver
          sudo apt-get install -y microsoft-edge-stable

      - name: Run Selenium script
        run: python open_page_edge.py
