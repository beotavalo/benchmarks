
import json
from datasets import load_dataset

def download_and_save_gsm8k():
    dataset = load_dataset("gsm8k", "main")
    test_data = dataset["test"]
    for i, example in enumerate(test_data):
        task_data = {
            "task_id": f"gsm8k_{i}",
            "question": example["question"],
            "answer": example["answer"].split("####")[1].strip()
        }
        with open(f"/workspaces/benchmarks/benchmarks/gsm8k/tasks/gsm8k_{i}.json", "w") as f:
            json.dump(task_data, f, indent=4)

if __name__ == "__main__":
    download_and_save_gsm8k()
