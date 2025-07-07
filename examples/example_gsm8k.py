
"""Example usage of Gsm8kBenchmark."""

from benchmarks.gsm8k import Gsm8kBenchmark


def main():
    # Initialize benchmark
    benchmark = Gsm8kBenchmark()

    # Get task information
    task_ids = benchmark.get_task_ids()
    print(f"Total tasks: {len(task_ids)}")

    # Example with first task
    if task_ids:
        task_id = task_ids[0]
        task = benchmark.get_task(task_id)

        print(f"\nTask ID: {task_id}")
        print(f"Task data keys: {list(task.data.keys())}")
        print(f"Question: {task.data['question']}")

        # Example evaluation
        example_output = task.data['answer']
        result = benchmark.evaluate(task_id, example_output)

        print(f"\nEvaluation result:")
        print(f"Score: {result.score}")
        print(f"Explanation: {result.score_explanation}")


if __name__ == "__main__":
    main()

