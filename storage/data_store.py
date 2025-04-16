import os
import json
import pandas as pd
import shutil

class DataStore:
    def __init__(self, base_path):
        self.base_path = base_path
        self.processed_path = os.path.join(base_path, 'processed')
        os.makedirs(self.processed_path, exist_ok=True)

    def save_dataframe(self, df, filename):
        file_path = os.path.join(self.processed_path, filename)
        df.to_csv(file_path, index=False)

    def load_dataframe(self, filename):
        file_path = os.path.join(self.processed_path, filename)
        return pd.read_csv(file_path)

    def save_json(self, data, filename):
        file_path = os.path.join(self.processed_path, filename)
        with open(file_path, 'w') as f:
            json.dump(data, f)

    def load_json(self, filename):
        file_path = os.path.join(self.processed_path, filename)
        with open(file_path, 'r') as f:
            return json.load(f)

    def clear_processed_data(self):
        if os.path.exists(self.processed_path):
            shutil.rmtree(self.processed_path)
        os.makedirs(self.processed_path, exist_ok=True)

    def archive_data(self, archive_name):
        archive_path = os.path.join(self.base_path, 'archives')
        os.makedirs(archive_path, exist_ok=True)

        shutil.make_archive(
            os.path.join(archive_path, archive_name),
            'zip',
            self.processed_path
        ) 