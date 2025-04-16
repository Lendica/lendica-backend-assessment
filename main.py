import os
import argparse
from pipelines.orchestrator import Orchestrator

def main():
    parser = argparse.ArgumentParser(description='Run the underwriting pipeline')
    parser.add_argument('--data-path', type=str, default='./data',
                        help='Path to the data directory')
    args = parser.parse_args()

    orchestrator = Orchestrator(args.data_path)

    success = orchestrator.monitor_pipeline()

    if success:
        print("Pipeline completed successfully")
    else:
        print("Pipeline failed")

if __name__ == "__main__":
    main() 