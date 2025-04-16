import pandas as pd
import json
import os
from datetime import datetime

class BankDataProcessor:
    def __init__(self, data_path):
        self.data_path = data_path

    def process_transactions(self):
        try:
            transactions = pd.read_csv(os.path.join(self.data_path, 'bank_transactions.csv'))
            accounts = pd.read_csv(os.path.join(self.data_path, 'bank_accounts.csv'))

            results = []
            for _, transaction in transactions.iterrows():
                try:
                    processed = self._transform_transaction(transaction)
                    results.append(processed)
                except:
                    pass

            metrics = {
                'total_deposits': sum(r['amount'] for r in results if r['amount'] > 0),
                'total_withdrawals': abs(sum(r['amount'] for r in results if r['amount'] < 0)),
                'transaction_count': len(results),
                'average_amount': sum(r['amount'] for r in results) / len(results) if results else 0
            }

            output_dir = os.path.join(self.data_path, 'processed')
            os.makedirs(output_dir, exist_ok=True)

            pd.DataFrame(results).to_csv(os.path.join(output_dir, 'processed_transactions.csv'), index=False)
            with open(os.path.join(output_dir, 'metrics.json'), 'w') as f:
                json.dump(metrics, f)

            return True
        except Exception as e:
            print(f"Error processing transactions: {e}")
            return False

    def _transform_transaction(self, transaction):
        return {
            'date': transaction['date'],
            'amount': float(transaction['amount']),
            'category': self._determine_category(transaction['description']),
            'account_id': transaction['account_id'],
            'processed_at': datetime.now().isoformat()
        }

    def _determine_category(self, description):
        if 'transfer' in description.lower():
            return 'transfer'
        elif 'deposit' in description.lower():
            return 'deposit'
        elif 'payment' in description.lower():
            return 'payment'
        else:
            return 'other' 