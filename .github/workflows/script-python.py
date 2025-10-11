name: Ejecutar Script Python

on:
  push:
    branches: 
      - main
    
jobs:
  run-python:
    runs-on: ubuntu-latest
    
    steps:
    - name: Descargar code rwpositorio
      uses: action/checkout@v4
    steps:
    - name: Config Python
      uses: actions/setup-python@v5
      with: 
        python-version: '3.x'
        
    - name: Ejecutar Script
      run: python script.py