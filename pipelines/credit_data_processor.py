import json
import os
from datetime import datetime

class CreditDataProcessor:
    def __init__(self, data_path):
        self.data_path = data_path

    def process_credit_report(self):
        try:
            with open(os.path.join(self.data_path, 'credit_report.json'), 'r') as f:
                credit_report = json.load(f)

            processed_data = {
                'credit_score': credit_report.get('credit_score', 0),
                'report_date': credit_report.get('report_date', datetime.now().isoformat()),
                'inquiries': credit_report.get('inquiries_last_6mo', 0),
                'derogatory_marks': credit_report.get('derogatory_marks', 0),
                'processed_at': datetime.now().isoformat()
            }

            accounts = credit_report.get('accounts', [])
            total_balance = sum(account.get('balance', 0) for account in accounts)
            total_limit = sum(account.get('limit', 0) for account in accounts)
            utilization = (total_balance / total_limit) * 100 if total_limit > 0 else 0

            processed_data.update({
                'total_balance': total_balance,
                'total_limit': total_limit,
                'utilization_rate': utilization
            })

            output_dir = os.path.join(self.data_path, 'processed')
            os.makedirs(output_dir, exist_ok=True)

            with open(os.path.join(output_dir, 'processed_credit.json'), 'w') as f:
                json.dump(processed_data, f)

            return True
        except Exception as e:
            print(f"Error processing credit report: {e}")
            return False 