import json


def load_json(file_path: str):
    print(f"loading data {file_path}")
    if file_path.endswith(".jsonl"):
        with open(file_path, "r", encoding="utf-8") as f:
            samples = [json.loads(line) for line in f]
            return samples
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            samples = json.load(f)
        return samples