# genai-studio-api
FastAPI service for GenAI explanations

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

A production-ready API for generating simplified technical explanations using simulated AI processing. Built with FastAPI and designed for seamless integration with frontend applications.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **AI Explanation Generation**: Simulated LLM integration with configurable latency
- **Async Architecture**: Handle 1000+ concurrent requests efficiently
- **Input Validation**: Strict validation using Pydantic models
- **Production-Ready**: Docker support with multi-platform compatibility
- **Comprehensive Testing**: 100% endpoint coverage with pytest
- **Security**: CORS configured and proper error handling
- **Monitoring**: Health check endpoint with system status

## Installation

### Prerequisites
- Python 3.11+
- Docker 20.10+ (optional)
- Git 2.25+

### Local Setup
```bash
# Clone repository
git clone https://github.com/anbabb/genai-studio-api.git
cd genai-studio-api

# Create and activate virtual environment
python3.11 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt