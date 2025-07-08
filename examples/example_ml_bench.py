"""Example usage of MLBenchBenchmark."""

from benchmarks.ml_bench import MLBenchBenchmark


def main():
    """
    Example of how to use the ML-Bench benchmark.
    """
    # Initialize benchmark
    benchmark = MLBenchBenchmark()

    # Get task information
    task_ids = benchmark.get_task_ids()
    print(f"Total tasks: {len(task_ids)}")

    # Example with first task
    if task_ids:
        task_id = task_ids[0]
        task = benchmark.get_task(task_id)

        print(f"\nTask ID: {task_id}")
        print(f"Task instruction: {task.prompt}")
        print(f"Expected output: {task.data['output']}")

        # Example evaluation
        example_output = task.data["output"]  # Using correct output for demonstration
        result = benchmark.evaluate(task_id, example_output)

        print(f"\nEvaluation result:")
        print(f"Score: {result.score}")
        print(f"Explanation: {result.score_explanation}")


if __name__ == "__main__":
    main()
