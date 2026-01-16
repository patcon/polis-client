import json
import sys
from pathlib import Path

def sort_json_inplace(path: Path, sort_key: str):
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("Top-level JSON must be a list")

    data = [
        dict(sorted(d.items()))
        for d in sorted(data, key=lambda x: x.get(sort_key))
    ]

    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python sort_json_inplace.py <file.json> <field>")
        sys.exit(1)

    path = Path(sys.argv[1])
    sort_key = sys.argv[2]

    sort_json_inplace(path, sort_key)
