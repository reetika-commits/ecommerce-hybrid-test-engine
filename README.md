
# E-Commerce Hybrid Test Engine

An end-to-end test automation framework built with Python, Playwright Async API, and Pytest. The project explores API testing, UI automation, and hybrid API-UI testing through a modular architecture.

## Project Objectives

- Build reusable API and UI automation components.
- Implement independent and maintainable test cases.
- Explore authentication and session management.
- Combine API operations with UI-based verification.
- Apply clean code and separation of concerns.
- Integrate automated testing into CI/CD.

## Tech Stack

- Python
- Playwright (Async API)
- Pytest
- pytest-asyncio
- Git and GitHub

## Project Structure

```text
ecommerce-hybrid-test-engine/
├── api/
│   ├── auth_api.py
│   ├── product_api.py
│   └── cart_api.py
├── pages/
├── tests/
│   ├── api/
│   ├── ui/
│   └── hybrid/
├── utilities/
│   └── assertions.py
├── test_data/
├── reports/
├── screenshots/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Implemented Features

### API Testing

- Product listing retrieval.
- User authentication through the DemoBlaze login API.
- Dynamic authentication token extraction.
- Add products to cart.
- Retrieve cart contents.
- Delete individual cart entries.
- Validate HTTP response status and response data.
- Verify application state after cart operations.

### Framework Design

- Modular API classes.
- Reusable pytest fixtures.
- Session-scoped API context and authentication fixture.
- Centralized assertion utilities.
- Async test execution using Playwright and pytest-asyncio.

## Setup and Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd ecommerce-hybrid-test-engine
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browser binaries when required:

```bash
python -m playwright install
```

## Running Tests

Run the complete test suite:

```bash
python -m pytest -v
```

Run API tests:

```bash
python -m pytest tests/api -v
```

## Application Under Test

[DemoBlaze](https://www.demoblaze.com/)

## Roadmap

- [ ] Complete independent API test coverage.
- [ ] Improve test data management.
- [ ] Implement UI automation using Playwright Async API.
- [ ] Develop Page Object Model.
- [ ] Implement hybrid API-UI test scenarios.
- [ ] Add network monitoring and interception.
- [ ] Integrate logging and test reporting.
- [ ] Configure GitHub Actions for CI/CD.

## Learning Approach

This project is being developed incrementally, focusing on understanding framework architecture, asynchronous programming, test design, API behaviour, and maintainable automation practices.
