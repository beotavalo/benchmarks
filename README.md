# AI Benchmarks

A modular collection of standardized benchmarks for evaluating AI models. Each benchmark can be installed independently with only its required dependencies.

## Quick Start

```bash
# Install only the benchmarks you need
uv pip install -e ".[aime]"        # Just AIME (no external deps)
uv pip install -e ".[gaia]"        # Just GAIA (no external deps)
uv pip install -e ".[swebench]"    # Just SWE-bench (Docker, datasets, etc.)
uv pip install -e ".[gsm8k]"       # Just GSM8K (datasets)
uv pip install -e ".[stark_amazon]" # Just Stark Amazon (no external deps)
uv pip install -e ".[ml_bench]"    # Just ML-Bench (datasets)
uv pip install -e ".[all]"         # Everything

# Check what's installed
python examples/modular_usage_example.py
```

See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed installation and usage instructions.

## Available Benchmarks

### AIME (American Invitational Mathematics Examination)
- Mathematical problem-solving benchmark
- 30 problems from AIME 2025 (15 from each exam)
- Integer answers between 0-999
- See `AIME2025/README.md` for details

### GAIA (General AI Assistants)
- Real-world task benchmark requiring various capabilities
- 466 tasks across 3 difficulty levels
- Tasks may include file analysis, web search, multi-step reasoning
- See `GAIA/README.md` for details

### SWE-bench (Software Engineering Benchmark)
- Code generation benchmark for real-world software issues
- Requires generating patches to fix bugs in open-source repositories
- Includes test execution to verify correctness
- See `swebench/README.md` for details

### GSM8K (Grade School Math)
- Mathematical reasoning benchmark
- 1319 problems from the GSM8K test set
- Integer answers
- See `benchmarks/gsm8k/README.md` for details

### Stark Amazon
- Question-answering benchmark based on the STaRK (Synthesized and Task-oriented question answering) dataset for Amazon product reviews.
- Contains two subsets:
    - A large synthesized dataset generated from product reviews.
    - A smaller, human-generated evaluation set for more nuanced validation.
- See `benchmarks/stark_amazon/README.md` for details.

### ML-Bench
- A benchmark for evaluating LLMs and AI agents on repository-level machine learning tasks.
- See `benchmarks/ml_bench/README.md` for details.

## Unified Interface

All benchmarks implement a common interface defined in `base_benchmark.py`:

### Base Interface (All Benchmarks)

```python
# Core components (always available)
from core import BaseBenchmark, Task, EvaluationResult

# Specific benchmark (if installed)
from benchmarks.aime2025 import AIMEBenchmark
from benchmarks.gaia import GAIABenchmark
from benchmarks.swebench import SWEBenchVerified
from benchmarks.gsm8k import Gsm8kBenchmark
from benchmarks.stark_amazon import StarkAmazonBenchmark
from benchmarks.ml_bench import MLBenchBenchmark

# Initialize
benchmark = AIMEBenchmark()  # or GAIABenchmark(), SWEBenchVerified(), Gsm8kBenchmark(), StarkAmazonBenchmark(), MLBenchBenchmark()

# Get tasks
task_ids = benchmark.get_task_ids()
task = benchmark.get_task(task_id)

# Evaluate - common interface for all benchmarks
result = benchmark.evaluate(task_id, model_output)
print(f"Score: {result.score}")
print(f"Explanation: {result.score_explanation}")
```

### Extended Interface (Execution-Based Benchmarks)

Benchmarks like SWE-bench that require code execution extend the base interface:

```python
# For detailed execution results
if hasattr(benchmark, 'evaluate_with_execution'):
    task_result = benchmark.evaluate_with_execution(
        task_id=task_id,
        output=model_output,
        use_modal=True  # or other execution parameters
    )
    print(f"Execution time: {task_result.execution.execution_time}")
    print(f"Execution trace: {task_result.execution.execution_trace}")
```

## Benchmark Types

### Simple Evaluation Benchmarks
- **AIME**: Compare numeric answers
- **GAIA**: Compare text answers with normalization
- **GSM8K**: Compare numeric answers
- **Stark Amazon**: Compare text answers
- **ML-Bench**: Compare text answers

These benchmarks inherit from `BaseBenchmark` and implement simple answer comparison.

### Execution-Based Benchmarks
- **SWE-bench**: Execute code patches and run tests

These benchmarks inherit from `ExecutionBasedBenchmark` and provide both:
- Simple `evaluate()` interface for compatibility
- Extended `evaluate_with_execution()` for detailed results

## Usage Examples

See the `examples/` directory for complete examples:

- `example_aime.py` - AIME usage example
- `example_gaia.py` - GAIA usage example
- `example_gsm8k.py` - GSM8K usage example
- `example_stark_amazon.py` - Stark Amazon usage example
- `example_ml_bench.py` - ML-Bench usage example
- `unified_example.py` - Shows unified interface across all benchmarks

Run examples from the project root:
```bash
python -m examples.example_aime
python -m examples.example_gaia
python -m examples.example_gsm8k
python -m examples.example_stark_amazon
python -m examples.example_ml_bench
python -m examples.unified_example
```

## Directory Structure

```
ai-benchmarks/
├── pyproject.toml      # Root package with optional extras
├��─ core/               # Core interfaces and models (minimal deps)
│   ├── __init__.py
│   ├── base_benchmark.py
│   └── models/
│       └── task.py
├── benchmarks/
│   ├── aime2025/       # AIME benchmark (no external deps)
│   │   ├── aime_benchmark.py
│   │   └── tasks/
│   ├── gaia/           # GAIA benchmark (no external deps)
│   │   ├── gaia_benchmark.py
│   │   └── files/
│   ├── gsm8k/          # GSM8K benchmark (datasets)
│   │   ├── gsm8k_benchmark.py
│   │   └── tasks/
│   ├── stark_amazon/   # Stark Amazon benchmark (no external deps)
│   │   ├── stark_amazon.py
│   │   └── tasks/
│   ├── ml_bench/       # ML-Bench benchmark (datasets)
│   │   ├── ml_bench.py
│   │   └── tasks/
│   └── swebench/       # SWE-bench (Docker, datasets, etc.)
│       ├── swebench.py
│       └── harness/
└── examples/           # Usage examples
    ├── example_aime.py
    ├── example_gaia.py
    ├── example_gsm8k.py
    ├── example_stark_amazon.py
    ├── example_ml_bench.py
    ├── unified_example.py
    └── modular_usage_example.py
```

## Adding New Benchmarks

To add a new benchmark, see the comprehensive guide: [ADD_NEW_BENCHMARK_GUIDE.md](ADD_NEW_BENCHMARK_GUIDE.md)

Quick overview:
1. Create directory under `benchmarks/your_benchmark_name`
2. Implement class inheriting from `BaseBenchmark` or `CodeExecutionBenchmark`
3. Add dependencies to root `pyproject.toml` (if any)
4. Update root `__init__.py` with try-except import
5. Add tests, documentation, and examples
