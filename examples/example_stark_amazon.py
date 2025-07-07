"""Example usage of StarkAmazonBenchmark."""

from benchmarks.stark_amazon.stark_amazon import StarkAmazonBenchmark


def main():
    """Example usage of StarkAmazonBenchmark."""
    print("Running Stark Amazon benchmark example...")

    # Initialize benchmark with a specific subset
    benchmark = StarkAmazonBenchmark(subset="human_generated")
    print(f"Initialized benchmark: {benchmark.name}")

    # Get task information
    task_ids = benchmark.get_task_ids()
    print(f"Total tasks in '{benchmark.subset}' subset: {len(task_ids)}")

    # Example with first task
    if task_ids:
        task_id = task_ids[0]
        task = benchmark.get_task(task_id)

        print(f"\nTask ID: {task_id}")
        print(f"Question: {task.data.get('question')}")
        print(f"Ground Truth Answer: {task.ground_truth}")

        # Example evaluation
        example_output = task.ground_truth  # Simulate a correct answer
        result = benchmark.evaluate(task_id, example_output)

        print(f"\nEvaluation result for a correct answer:")
        print(f"Score: {result.score}")
        print(f"Explanation: {result.score_explanation}")

        # Example evaluation with incorrect answer
        example_output_incorrect = "This is a wrong answer."
        result_incorrect = benchmark.evaluate(task_id, example_output_incorrect)
        print(f"\nEvaluation result for an incorrect answer:")
        print(f"Score: {result_incorrect.score}")
        print(f"Explanation: {result_incorrect.score_explanation}")

    else:
        print("No tasks found for this benchmark.")


if __name__ == "__main__":
    main()
