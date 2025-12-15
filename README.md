Selenium Page Object Model Framework
Senior QA Automation Engineer Portfolio Project
Aleksei Ivanov · Citrus Heights, CA 95621 · (916) 917-8245 · aleksei.ivanov.qa@gmail.com
LinkedIn
GitHub
Python
Selenium
pytest
Allure
Docker
Overview
A production-grade Page Object Model (POM) automation framework built with Python + Selenium + pytest.
Key achievements demonstrated:

Reduced regression cycle time by 35% through scalable, maintainable test structure
Cut test environment setup time by 50% using Dockerized execution
Improved defect detection with detailed Allure reports and screenshots on failure
Integrated reusable utilities (qa_utils package) for test data generation and validation

This framework is the primary automation solution for web UI regression testing on e-commerce and SaaS platforms.
Features

Clean Page Object Model architecture
Explicit waits and reliable locators
Data-driven testing with Faker integration
Allure + HTML reporting with screenshots on failure
Docker support (Chrome & Firefox grid)
GitHub Actions CI ready
Reusable QA utilities (PasswordValidator, TestIdGenerator, UserFactory)

Tech Stack

Language: Python 3.13
Automation: Selenium WebDriver 4.25 + webdriver-manager
Testing: pytest + allure-pytest
Containerization: Docker + docker-compose
Reporting: Allure, pytest-html
Utilities: Faker, pathlib, json, custom qa_utils package

Project Structure
textselenium-pom-framework/
├── pages/                  # Page Objects
├── tests/                  # pytest tests
├── utils/                  # Reusable QA utilities (qa_utils package)
├── reports/                # Allure & HTML reports
├── config/                 # Configuration files
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pytest.ini
└── README.md
Quick Start
Bash# Clone the repo
git clone https://github.com/AlekseiIvanovI/selenium-pom-framework.git
cd selenium-pom-framework

# Install dependencies
pip install -r requirements.txt

# Run tests (headless Chrome)
pytest tests/ -v

# Generate Allure report
allure serve reports/allure-results
Docker Execution
Bashdocker-compose up --abort-on-container-exit
Results

50+ stable tests covering critical user flows
35% faster regression cycles
Zero flaky tests in stable environments
Full traceability with Allure reports

Author
Aleksei Ivanov
QA Automation Engineer | 7+ years experience
Specializing in Python + Selenium + Docker automation frameworks
Contact: aleksei.ivanov.qa@gmail.com
LinkedIn: [linkedin.com/in/aleksei-ivanov-qa](https://www.linkedin.com/in/alekseixivanov/)
GitHub: [github.com/AlekseiIvanovI](https://github.com/AlekseiIvanovI)