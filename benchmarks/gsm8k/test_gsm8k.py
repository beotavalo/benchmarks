import unittest
import json
from pathlib import Path

from benchmarks.gsm8k.gsm8k_benchmark import Gsm8kBenchmark


class TestGsm8kBenchmark(unittest.TestCase):
    def setUp(self):
        self.benchmark = Gsm8kBenchmark()

    def test_get_task_ids(self):
        task_ids = self.benchmark.get_task_ids()
        self.assertIsInstance(task_ids, list)
        self.assertGreater(len(task_ids), 0)

    def test_get_task(self):
        task_ids = self.benchmark.get_task_ids()
        if task_ids:
            task = self.benchmark.get_task(task_ids[0])
            self.assertEqual(task.benchmark, "Gsm8k")

    def test_evaluate(self):
        # This test will be more meaningful once the data is loaded.
        pass

    def test_full_dataset_evaluation(self):
        """
        Test evaluation over the full dataset to ensure all tasks can be
        processed and compared to ground truth.
        """
        task_ids = self.benchmark.get_task_ids()
        self.assertGreater(len(task_ids), 0, "No tasks found to evaluate.")

        for task_id in task_ids:
            task = self.benchmark.get_task(task_id)
            ground_truth = task.data.get("answer")

            # Simulate a correct answer
            result_correct = self.benchmark.evaluate(task_id, ground_truth)
            self.assertEqual(result_correct.score, 1.0)

            # Simulate an incorrect answer
            result_incorrect = self.benchmark.evaluate(task_id, "wrong answer")
            self.assertEqual(result_incorrect.score, 0.0)


if __name__ == "__main__":
    unittest.main()
