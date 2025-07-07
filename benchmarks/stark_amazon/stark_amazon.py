import pandas as pd
from pathlib import Path
from typing import Any, Literal

from core.base_benchmark import BaseBenchmark
from core.models.task import EvaluationResult, Task


class StarkAmazonBenchmark(BaseBenchmark):
    """Benchmark for STaRK Amazon dataset."""

    def __init__(
        self,
        data_dir: str | None = None,
        subset: Literal["synthesized", "human_generated", "all"] = "all",
    ):
        """Initialize the benchmark.

        Args:
            data_dir: Optional path to data directory. If None, uses default.
            subset: The subset of the dataset to use.
        """
        if data_dir is None:
            # Use path relative to this file
            data_dir = Path(__file__).parent / "tasks"
        self.data_dir = Path(data_dir)
        self.subset = subset
        self._tasks = self._load_tasks()

    @property
    def name(self) -> str:
        """Return the benchmark name."""
        return f"StarkAmazon_{self.subset}"

    def get_task_ids(self) -> list[str]:
        """Return all task IDs."""
        return list(self._tasks.keys())

    def get_task(self, task_id: str) -> Task:
        """Get a specific task by ID."""
        if task_id not in self._tasks:
            raise ValueError(f"Task {task_id} not found")
        return self._tasks[task_id]

    def evaluate(self, task_id: str, output: Any) -> EvaluationResult:
        """Evaluate the model output for a task.

        Args:
            task_id: The task ID to evaluate
            output: The model's output

        Returns:
            EvaluationResult with score and explanation
        """
        task = self.get_task(task_id)
        expected = task.data.get("answer", "")

        if str(output).strip() == str(expected).strip():
            return EvaluationResult(score=1.0, score_explanation="Correct answer")
        else:
            return EvaluationResult(
                score=0.0, score_explanation=f"Expected: {expected}, Got: {output}"
            )

    def _load_tasks(self) -> dict[str, Task]:
        """Load tasks from data files."""
        tasks = {}
        subsets_to_load = []
        if self.subset == "all":
            subsets_to_load.extend(["synthesized", "human_generated"])
        else:
            subsets_to_load.append(self.subset)

        for subset_name in subsets_to_load:
            subset_dir = self.data_dir / subset_name
            for csv_file in subset_dir.glob("*.csv"):
                df = pd.read_csv(csv_file)
                for i, row in df.iterrows():
                    task_id = f"{subset_name}_{csv_file.stem}_{i}"
                    task_data = row.to_dict()
                    task = Task(
                        task_id=task_id,
                        benchmark=self.name,
                        data=task_data,
                        ground_truth=task_data.get("answer"),
                    )
                    tasks[task_id] = task
        return tasks

