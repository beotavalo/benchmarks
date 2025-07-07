# Stark Amazon Benchmark

## Overview
This benchmark evaluates the model's ability to answer questions based on the STaRK Amazon dataset.

## Task Structure
Each task consists of a question and a corresponding answer.

## Evaluation Metrics
The evaluation is based on the exact match between the model's output and the expected answer.

## Usage Example
```python
from benchmarks.stark_amazon import StarkAmazonBenchmark

benchmark = StarkAmazonBenchmark()
task_ids = benchmark.get_task_ids()
if task_ids:
    task = benchmark.get_task(task_ids[0])

    # Evaluate
    result = benchmark.evaluate(task_ids[0], "model output")
    print(f"Score: {result.score}")
```

## Dataset Information
- Number of tasks: 0 (placeholder)
- Task types: Question Answering
- Sources: STaRK Amazon Dataset
