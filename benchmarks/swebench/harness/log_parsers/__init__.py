from benchmarks.benchmarks.swebench.harness.log_parsers.c import MAP_REPO_TO_PARSER_C
from benchmarks.benchmarks.swebench.harness.log_parsers.go import MAP_REPO_TO_PARSER_GO
from benchmarks.benchmarks.swebench.harness.log_parsers.java import MAP_REPO_TO_PARSER_JAVA
from benchmarks.benchmarks.swebench.harness.log_parsers.javascript import MAP_REPO_TO_PARSER_JS
from benchmarks.benchmarks.swebench.harness.log_parsers.php import MAP_REPO_TO_PARSER_PHP
from benchmarks.benchmarks.swebench.harness.log_parsers.python import MAP_REPO_TO_PARSER_PY
from benchmarks.benchmarks.swebench.harness.log_parsers.ruby import MAP_REPO_TO_PARSER_RUBY
from benchmarks.benchmarks.swebench.harness.log_parsers.rust import MAP_REPO_TO_PARSER_RUST

MAP_REPO_TO_PARSER = {
    **MAP_REPO_TO_PARSER_C,
    **MAP_REPO_TO_PARSER_GO,
    **MAP_REPO_TO_PARSER_JAVA,
    **MAP_REPO_TO_PARSER_JS,
    **MAP_REPO_TO_PARSER_PHP,
    **MAP_REPO_TO_PARSER_PY,
    **MAP_REPO_TO_PARSER_RUST,
    **MAP_REPO_TO_PARSER_RUBY,
}


__all__ = [
    "MAP_REPO_TO_PARSER",
]
