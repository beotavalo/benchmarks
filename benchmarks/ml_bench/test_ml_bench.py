
import unittest
from unittest.mock import patch, MagicMock

from benchmarks.ml_bench import MLBenchBenchmark


class TestMLBenchBenchmark(unittest.TestCase):
    @patch("benchmarks.ml_bench.ml_bench.load_dataset")
    def setUp(self, mock_load_dataset):
        # Mock the dataset loading
        mock_dataset = [
            {
                "instruction": "Train a model.",
                "github": "user/repo",
                "path": "train.py",
                "arguments": {},
                "oracle": "",
                "output": "python train.py",
                "type": "Bash Script",
            }
        ]
        mock_load_dataset.return_value = mock_dataset
        self.benchmark = MLBenchBenchmark()

    def test_get_task_ids(self):
        task_ids = self.benchmark.get_task_ids()
        self.assertIsInstance(task_ids, list)
        self.assertEqual(len(task_ids), 1)
        self.assertEqual(task_ids[0], "ml_bench_0")

    def test_get_task(self):
        task = self.benchmark.get_task("ml_bench_0")
        self.assertEqual(task.benchmark, "ML-Bench")
        self.assertEqual(task.prompt, "Train a model.")
        self.assertEqual(task.data["output"], "python train.py")

    def test_evaluate_correct(self):
        result = self.benchmark.evaluate("ml_bench_0", "python train.py")
        self.assertEqual(result.score, 1.0)
        self.assertEqual(result.score_explanation, "Correct answer")

    def test_evaluate_incorrect(self):
        result = self.benchmark.evaluate("ml_bench_0", "python test.py")
        self.assertEqual(result.score, 0.0)
        self.assertIn("Expected:", result.score_explanation)


if __name__ == "__main__":
    unittest.main()
