
import json
from pathlib import Path
from typing import Any

from core.base_benchmark import BaseBenchmark
from core.models.task import EvaluationResult, Task


class Gsm8kBenchmark(BaseBenchmark):
    """
    Benchmark for evaluating the performance of models on the GSM8K dataset.
    """

    def __init__(self, data_dir: str | None = None):
        """
        Initializes the benchmark.

        Args:
            data_dir: The directory where the GSM8K data is stored.
        """
        if data_dir is None:
            data_dir = Path(__file__).parent / "tasks"
        self.data_dir = Path(data_dir)
        self._tasks = self._load_tasks()

    @property
    def name(self) -> str:
        return "Gsm8k"

    def get_task_ids(self) -> list[str]:
        return list(self._tasks.keys())

    def get_task(self, task_id: str) -> Task:
        if task_id not in self._tasks:
            raise ValueError(f"Task {task_id} not found")
        return self._tasks[task_id]

    def evaluate(self, task_id: str, output: Any) -> EvaluationResult:
        task = self.get_task(task_id)
        expected = task.data.get("answer", "")
        if str(output).strip() == str(expected).strip():
            return EvaluationResult(
                score=1.0,
                score_explanation="Correct answer"
            )
        else:
            return EvaluationResult(
                score=0.0,
                score_explanation=f"Expected: {expected}, Got: {output}"
            )

    def _load_tasks(self) -> dict[str, Task]:
        """
        Loads tasks from the data files.
        """
        tasks = {}
        for json_file in self.data_dir.glob("*.json"):
            with open(json_file) as f:
                data = json.load(f)
                task = Task(
                    task_id=data["task_id"],
                    benchmark=self.name,
                    data=data
                )
                tasks[task.task_id] = task
        return tasks
