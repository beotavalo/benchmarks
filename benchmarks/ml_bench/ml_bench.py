
from pathlib import Path
from typing import Any, Dict

from datasets import load_dataset

from core.base_benchmark import BaseBenchmark
from core.models.task import EvaluationResult, Task


class MLBenchBenchmark(BaseBenchmark):
    """
    ML-Bench is a benchmark for evaluating LLMs and AI agents on repository-level
    machine learning tasks.
    """

    def __init__(self, data_dir: str | None = None, **kwargs):
        """
        Args:
            data_dir: The directory where the benchmark data is stored.
            **kwargs: Additional keyword arguments.
        """
        super().__init__(data_dir, **kwargs)
        self.tasks: Dict[str, Task] = self._load_tasks()

    @property
    def name(self) -> str:
        return "ML-Bench"

    def get_task_ids(self) -> list[str]:
        return list(self.tasks.keys())

    def get_task(self, task_id: str) -> Task:
        return self.tasks[task_id]

    def evaluate(self, task_id: str, output: Any) -> EvaluationResult:
        task = self.get_task(task_id)
        expected_output = task.data["output"]

        if str(output).strip() == str(expected_output).strip():
            return EvaluationResult(
                score=1.0, score_explanation="Correct answer"
            )
        else:
            return EvaluationResult(
                score=0.0,
                score_explanation=f"Expected: {expected_output}, Got: {output}",
            )

    def _load_tasks(self) -> Dict[str, Task]:
        tasks = {}
        dataset = load_dataset("super-dainiu/ml-bench", split="train")
        for i, item in enumerate(dataset):
            task_id = f"ml_bench_{i}"
            task_data = {
                "instruction": item["instruction"],
                "github": item["github"],
                "path": item["path"],
                "arguments": item["arguments"],
                "oracle": item["oracle"],
                "output": item["output"],
                "type": item["type"],
            }
            task = Task(
                task_id=task_id,
                benchmark=self.name,
                data=task_data,
                prompt=item["instruction"],
            )
            tasks[task_id] = task
        return tasks
