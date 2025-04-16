import os
from pipelines.bank_data_processor import BankDataProcessor
from pipelines.credit_data_processor import CreditDataProcessor
from analysis.risk_calculator import RiskCalculator
from storage.data_store import DataStore
from storage.reporting import ReportGenerator
import time

class Orchestrator:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data_store = DataStore(data_path)

    def run_pipeline(self):
        print("Starting underwriting pipeline...")

        print("Processing bank data...")
        bank_processor = BankDataProcessor(self.data_path)
        bank_result = bank_processor.process_transactions()

        print("Processing credit data...")
        credit_processor = CreditDataProcessor(self.data_path)
        credit_result = credit_processor.process_credit_report()

        print("Calculating risk score...")
        risk_calculator = RiskCalculator(self.data_path)
        risk_score, risk_category = risk_calculator.calculate_risk_score()

        print("Generating report...")
        report_generator = ReportGenerator(self.data_path)
        report_generator.generate_report()

        if bank_result and credit_result and risk_score:
            print(f"Pipeline completed successfully. Risk score: {risk_score}, Category: {risk_category}")
            return True
        else:
            print("Pipeline completed with errors.")
            return False

    def monitor_pipeline(self):
        start_time = time.time()
        result = self.run_pipeline()
        end_time = time.time()

        execution_time = end_time - start_time
        print(f"Pipeline execution time: {execution_time:.2f} seconds")

        if execution_time > 10:
            print("WARNING: Pipeline execution time exceeds threshold")

        return result 