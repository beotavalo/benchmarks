# ML-Bench Benchmark

## Overview
ML-Bench is a benchmark for evaluating Large Language Models (LLMs) and AI agents on repository-level machine learning tasks. It tests the ability of a model to generate correct command-line scripts for various ML tasks based on natural language instructions.

## Task Structure
Each task in ML-Bench consists of:
- `instruction`: A natural language request describing a machine learning task.
- `github` & `path`: The relevant GitHub repository and file path that provide the context for the task.
- `arguments`: A dictionary of specific parameters to be used.
- `oracle`: Documentation or example commands related to the task.
- `output`: The ground-truth command-line script that correctly performs the requested task.
- `type`: The type of the output, such as `Bash Script` or `Python Code`.

## Evaluation Metrics
The model's output is compared to the ground-truth `output` field. A score of 1.0 is awarded for an exact match (after stripping whitespace), and 0.0 otherwise.

## Usage Example
```python
from benchmarks.ml_bench import MLBenchBenchmark

benchmark = MLBenchBenchmark()
task_ids = benchmark.get_task_ids()
task = benchmark.get_task(task_ids[0])

# Get model output
model_output = "python train.py --learning_rate 0.01"

# Evaluate
result = benchmark.evaluate(task.task_id, model_output)
print(f"Score: {result.score}")
```

## Dataset Information
- **Source:** [super-dainiu/ml-bench on Hugging Face](https://huggingface.co/datasets/super-dainiu/ml-bench)
- **Number of tasks:** Over 10,000
- **Task types:** Command-line script generation for machine learning tasks.
