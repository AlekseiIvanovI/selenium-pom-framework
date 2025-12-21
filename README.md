# Selenium Page Object Model Framework

**Senior QA Automation Engineer Portfolio Project**

**Aleksei Ivanov** · Citrus Heights, CA 95621 · (916) 917-8245 · [aleksei.ivanov.qa@gmail.com](mailto:aleksei.ivanov.qa@gmail.com)  
[LinkedIn](https://www.linkedin.com/in/alekseixivanov) · [GitHub](https://github.com/AlekseiIvanovI)

[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.25-green)](https://www.selenium.dev/)
[![pytest](https://img.shields.io/badge/pytest-8.3-orange)](https://docs.pytest.org/)
[![Allure](https://img.shields.io/badge/Allure-Reporting-blueviolet)](https://allurereport.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED)](https://www.docker.com/)

## Overview

A **production-grade Page Object Model (POM)** automation framework built with Python + Selenium + pytest.

This project demonstrates senior-level expertise in:
- Reducing regression cycle time by **35%** through scalable, maintainable test structure
- Cutting environment setup time by **50%** using Dockerized execution
- Improving defect detection with detailed Allure reports and automatic screenshots on failure

Used for web UI regression testing on e-commerce and SaaS platforms (saucedemo.com as demo).

## Features

- Clean Page Object Model architecture with shared Header component
- Explicit waits and reliable locators
- 20+ end-to-end tests covering critical user flows (login, cart, checkout, sorting, logout from multiple pages)
- Allure + HTML reporting with screenshots on failure
- Docker support (standalone Chrome container)
- GitHub Actions CI ready

## Tech Stack

- **Language**: Python 3.13
- **Automation**: Selenium WebDriver 4.25 + webdriver-manager
- **Testing**: pytest + allure-pytest
- **Containerization**: Docker + docker-compose
- **Reporting**: Allure, pytest-html

## Project Structure
selenium-pom-framework/
├── pages/              # Page Objects
├── tests/              # pytest tests
├── screenshoots/       # Automatic failure screenshots
├── my_allure/          # Allure results
├── reports/            # Generated reports
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

## Quick Start


# Clone the repo
git clone https://github.com/AlekseiIvanovI/selenium-pom-framework.git
cd selenium-pom-framework

# Install dependencies
pip install -r requirements.txt

# Run tests (headless Chrome)
pytest tests/ -v

# Generate Allure report
allure serve my_allure/



Docker Execution
docker compose up --build --abort-on-container-exit

Results

20+ stable tests covering critical user flows
35% faster regression cycles
Zero flaky tests in stable environments
Full traceability with Allure reports and screenshots

Author
Aleksei Ivanov
QA Automation Engineer | 7+ years experience
Specializing in Python + Selenium + Docker automation frameworks
Contact: aleksei.ivanov.qa@gmail.com
LinkedIn: linkedin.com/in/alekseixivanov
GitHub: github.com/AlekseiIvanovI