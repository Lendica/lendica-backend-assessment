import json
import os
import numpy as np
from datetime import datetime

class RiskCalculator:
    def __init__(self, data_path):
        self.data_path = data_path
        self.processed_path = os.path.join(data_path, 'processed')

    def calculate_risk_score(self):
        try:
            with open(os.path.join(self.processed_path, 'metrics.json'), 'r') as f:
                metrics = json.load(f)

            with open(os.path.join(self.data_path, 'credit_report.json'), 'r') as f:
                credit_report = json.load(f)

            with open(os.path.join(self.data_path, 'company_info.json'), 'r') as f:
                company_info = json.load(f)

            bank_risk = self._calculate_bank_risk(metrics)
            credit_risk = self._calculate_credit_risk(credit_report)
            business_risk = self._calculate_business_risk(company_info)

            final_score = (bank_risk * 0.4) + (credit_risk * 0.4) + (business_risk * 0.2)

            risk_category = 'high' if final_score > 70 else 'medium' if final_score > 40 else 'low'

            with open(os.path.join(self.processed_path, 'risk_assessment.json'), 'w') as f:
                json.dump({
                    'score': final_score,
                    'category': risk_category,
                    'components': {
                        'bank_risk': bank_risk,
                        'credit_risk': credit_risk,
                        'business_risk': business_risk
                    },
                    'calculated_at': datetime.now().isoformat()
                }, f)

            return final_score, risk_category
        except Exception as e:
            print(f"Error calculating risk score: {e}")
            return None, None

    def _calculate_bank_risk(self, metrics):
        if metrics['total_deposits'] <= 0:
            return 100  # Maximum risk if no deposits

        deposit_to_withdrawal_ratio = metrics['total_deposits'] / max(metrics['total_withdrawals'], 1)

        if deposit_to_withdrawal_ratio < 0.8:
            return 80
        elif deposit_to_withdrawal_ratio < 1.0:
            return 60
        elif deposit_to_withdrawal_ratio < 1.2:
            return 40
        else:
            return 20

    def _calculate_credit_risk(self, credit_report):
        score = credit_report.get('credit_score', 0)
        if score == 0:  # Missing data
            return 50  # Default to medium risk

        return 100 - (score / 8.5)

    def _calculate_business_risk(self, company_info):
        age_in_years = company_info.get('years_in_business', 0)
        industry = company_info.get('industry', 'unknown')

        if age_in_years < 1:
            base_risk = 80
        elif age_in_years < 3:
            base_risk = 60
        elif age_in_years < 5:
            base_risk = 40
        else:
            base_risk = 20

        industry_risk_map = {
            'technology': -10,
            'retail': 0,
            'manufacturing': 5,
            'restaurant': 15,
            'construction': 10,
            'unknown': 20
        }

        industry_modifier = industry_risk_map.get(industry, 0)
        final_risk = base_risk + industry_modifier

        return final_risk 