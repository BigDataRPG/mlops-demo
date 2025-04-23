import argparse
import json


def evaluate(preds, refs):
    # Simple quality metric: count "Mage" recommendations
    mage_count = sum(1 for p in preds if p["class"] == "Mage")
    return {"mage_ratio": mage_count / len(preds)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pred", required=True)
    parser.add_argument("--ref", required=True)
    args = parser.parse_args()

    with open(args.pred) as f:
        preds = json.load(f)
    with open(args.ref) as f:
        refs = json.load(f)

    metrics = evaluate(preds, refs)
    with open("outputs/metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)


if __name__ == "__main__":
    main()
