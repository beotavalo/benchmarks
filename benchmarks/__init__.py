
# benchmarks/__init__.py

__all__ = []

try:
    from .aime2025 import Aime2025Benchmark
    __all__.append("Aime2025Benchmark")
except ImportError:
    pass

try:
    from .browse_comp import BrowseCompBenchmark
    __all__.append("BrowseCompBenchmark")
except ImportError:
    pass

try:
    from .gaia import GaiaBenchmark
    __all__.append("GaiaBenchmark")
except ImportError:
    pass

try:
    from .gsm8k import Gsm8kBenchmark
    __all__.append("Gsm8kBenchmark")
except ImportError:
    pass

try:
    from .swebench import SwebenchBenchmark
    __all__.append("SwebenchBenchmark")
except ImportError:
    pass

try:
    from .stark_amazon import StarkAmazonBenchmark
    __all__.append("StarkAmazonBenchmark")
except ImportError:
    pass
