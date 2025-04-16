# Lending Underwriting Pipeline Assessment

This project contains a simplified underwriting pipeline for processing loan applications. The pipeline includes data ingestion, transformation, analysis, and reporting components.

## Project Structure

```
lending-assessment/
├── README.md
├── requirements.txt
├── data/
│   ├── bank_transactions.csv
│   ├── bank_accounts.csv
│   ├── credit_report.json
│   └── company_info.json
├── pipelines/
│   ├── __init__.py
│   ├── bank_data_processor.py
│   ├── credit_data_processor.py
│   └── orchestrator.py
├── analysis/
│   ├── __init__.py
│   ├── bank_analysis.py
│   ├── credit_analysis.py
│   └── risk_calculator.py
├── storage/
│   ├── __init__.py
│   ├── data_store.py
│   └── reporting.py
├── tests/
│   ├── __init__.py
│   ├── test_bank_processor.py
│   └── test_risk_calculator.py
└── main.py
```

## Setup

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Pipeline

To run the pipeline:

```bash
python main.py --data-path ./data
```

## Assessment Instructions

**Time Limit:** 90 minutes

**Task Overview:**

You've been given a simplified underwriting pipeline used to process loan applications. The current implementation has several issues with code quality, architecture, performance, and reliability. Your task is to:

1. **Analyze the codebase** and identify key problems
2. **Improve the code** by fixing critical issues
3. **Suggest architectural improvements** that would make the system more robust, scalable, and maintainable
4. **Document your changes** and rationale

**Specific Areas to Address:**

1. **Performance Issues:** Identify and fix inefficient code
2. **Error Handling:** Improve error handling and logging
3. **Architecture:** Suggest better approaches to data storage, processing, and reporting
4. **Code Quality:** Address code smells and improve maintainability

**Deliverables:**

1. Modified code with your improvements
2. A brief document (1-2 pages) explaining:
   - Key issues you identified
   - Solutions you implemented
   - Architectural improvements you would make if you had more time
   - Any trade-offs you considered

**Evaluation Criteria:**

- Thoroughness in identifying problems
- Quality of implemented solutions
- Systems thinking and architectural vision
- Code quality and maintainability
- Communication of technical concepts
