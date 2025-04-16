import json
import os
from datetime import datetime

class ReportGenerator:
    def __init__(self, data_path):
        self.data_path = data_path
        self.processed_path = os.path.join(data_path, 'processed')

    def generate_report(self):
        try:
            with open(os.path.join(self.processed_path, 'risk_assessment.json'), 'r') as f:
                risk_data = json.load(f)

            with open(os.path.join(self.processed_path, 'processed_credit.json'), 'r') as f:
                credit_data = json.load(f)

            with open(os.path.join(self.processed_path, 'metrics.json'), 'r') as f:
                bank_metrics = json.load(f)

            report = {
                'generated_at': datetime.now().isoformat(),
                'risk_score': risk_data['score'],
                'risk_category': risk_data['category'],
                'credit_score': credit_data['credit_score'],
                'total_deposits': bank_metrics['total_deposits'],
                'total_withdrawals': bank_metrics['total_withdrawals'],
                'transaction_count': bank_metrics['transaction_count']
            }

            with open(os.path.join(self.processed_path, 'final_report.json'), 'w') as f:
                json.dump(report, f)

            return True
        except Exception as e:
            print(f"Error generating report: {e}")
            return False 