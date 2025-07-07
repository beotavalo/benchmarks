import unittest
from benchmarks.stark_amazon.stark_amazon import StarkAmazonBenchmark


class TestStarkAmazonBenchmark(unittest.TestCase):
    def test_load_synthesized(self):
        benchmark = StarkAmazonBenchmark(subset="synthesized")
        task_ids = benchmark.get_task_ids()
        self.assertIsInstance(task_ids, list)
        self.assertGreater(len(task_ids), 0)
        self.assertTrue(all(t.startswith("synthesized") for t in task_ids))

    def test_load_human_generated(self):
        benchmark = StarkAmazonBenchmark(subset="human_generated")
        task_ids = benchmark.get_task_ids()
        self.assertIsInstance(task_ids, list)
        self.assertGreater(len(task_ids), 0)
        self.assertTrue(all(t.startswith("human_generated") for t in task_ids))

    def test_load_all(self):
        benchmark = StarkAmazonBenchmark(subset="all")
        task_ids = benchmark.get_task_ids()
        self.assertIsInstance(task_ids, list)
        self.assertGreater(len(task_ids), 0)
        self.assertTrue(any(t.startswith("synthesized") for t in task_ids))
        self.assertTrue(any(t.startswith("human_generated") for t in task_ids))

    def test_get_task(self):
        benchmark = StarkAmazonBenchmark()
        task_ids = benchmark.get_task_ids()
        self.assertGreater(len(task_ids), 0)
        task = benchmark.get_task(task_ids[0])
        self.assertEqual(task.benchmark, "StarkAmazon_all")
        self.assertIn("question", task.data)
        self.assertIn("answer", task.data)

    def test_evaluate(self):
        benchmark = StarkAmazonBenchmark(subset="human_generated")
        task_ids = benchmark.get_task_ids()
        self.assertGreater(len(task_ids), 0)
        task_id = task_ids[0]
        task = benchmark.get_task(task_id)
        correct_answer = task.data["answer"]

        # Test correct answer
        result = benchmark.evaluate(task_id, correct_answer)
        self.assertEqual(result.score, 1.0)

        # Test incorrect answer
        result = benchmark.evaluate(task_id, "some incorrect answer")
        self.assertEqual(result.score, 0.0)


if __name__ == "__main__":
    unittest.main()
