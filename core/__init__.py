"""Core benchmark interfaces and models."""

from benchmarks.core.base_benchmark import BaseBenchmark, CodeExecutionBenchmark
from benchmarks.core.models.task import EvaluationResult, ExecutionResult, Task, TaskResult

__all__ = [
    "BaseBenchmark",
    "CodeExecutionBenchmark",
    "Task",
    "TaskResult",
    "EvaluationResult",
    "ExecutionResult",
]
