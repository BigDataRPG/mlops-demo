import argparse
import json
from pathlib import Path

import wandb


def load_prompt(prompt_path):
    with open(prompt_path) as f:
        return f.read()


def fake_llm(prompt):
    # Simulate LLM output for demo
    return {
        "class": "Mage",
        "tone": "Mysterious",
        "gear": "Staff, Robes",
        "backstory": "A scholar who uncovered forbidden secrets.",
    }


def recommend_character(preferences, prompt_path):
    prompt_template = load_prompt(prompt_path)
    prompt = prompt_template.replace("{preferences}", preferences)
    return fake_llm(prompt)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--inputs", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--eval-only", action="store_true")
    args = parser.parse_args()

    with open(args.inputs) as f:
        inputs = json.load(f)

    results = []
    for item in inputs:
        result = recommend_character(item["preferences"], args.prompt)
        results.append(result)

    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)

    # Log to W&B
    wandb.init(project="mlops-demo", job_type="generate")
    wandb.log({"prompt_path": args.prompt, "output_count": len(results)})


if __name__ == "__main__":
    main()
