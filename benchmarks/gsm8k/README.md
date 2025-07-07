# GSM8K Benchmark

## Overview
This benchmark evaluates the performance of models on the GSM8K dataset, which consists of grade school math word problems.

## Task Structure
Each task in this benchmark is a math word problem. The goal is to provide the correct numerical answer.

## Evaluation Metrics
The evaluation is based on exact match of the numerical answer.

## Usage Example
```python
from benchmarks.gsm8k import Gsm8kBenchmark

benchmark = Gsm8kBenchmark()
task_ids = benchmark.get_task_ids()
task = benchmark.get_task(task_ids[0])

# Evaluate
result = benchmark.evaluate(task_ids[0], "model output")
print(f"Score: {result.score}")
```

## Dataset Information
- Number of tasks: 1319 (test set)
- Task types: Grade school math word problems
- Sources: https://huggingface.co/datasets/gsm8k
