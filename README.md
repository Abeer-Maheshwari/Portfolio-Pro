# Financial Advisor

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A **local AI Financial Advisor** that analyses images of complex financial graphs, charts, or website screenshots and provides insightful feedback/advice.

This project uses local vision-language models (ollama) that interpret the visual financial data, ensuring privacy and offline capability.

## Features

- Fully local processing: no API calls or internet required for inference
- Accepts image inputs (screenshots of graphs, financial websites, reports)
- Provides natural language feedback, explanations, and recommendations
- Local LVMs are provided by Ollama

## Requirements

- Python 3.8 or higher
- Sufficient GPU (recommended for faster inference) or CPU
- Dependencies include:
  - Ollama (for providing, installing and running the local LVMs)
  - A multimodal model supporting vision (`llava`, `bakllava`, or `moondream` | I used llava:13b)

## Installation and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Abeer-Maheshwari/Financial-Advisor.git
   cd Financial-Advisor
   ```
2. Install Ollama from ollama.com and pull a vision-capable model (llava:13b for better results, llava:7b for faster inference):
   ```bash
   ollama pull llava:13b
   ```
3. Install Python Dependencies:
   ```bash
   pip install ollama pillow
   ```
4. Run ollama locally first (keep cmd window open), then script in another window:
   ```bash
   ollama serve
   ```
   ```bash
   python FinancialAdvisor.py
   ```
The script will:
- Prompt you to provide an image link or drag-and-drop/upload
- Process the image using the local vision model
- Output detailed financial insights and advice

## Notes
- This is a privacy-focused, experimental project running entirely locally.
- Performance and accuracy depend on the chosen local vision-language model.
- For best results, use high-quality images and detailed/zoomed in screenshots.
