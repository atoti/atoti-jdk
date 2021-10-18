"""JDK packaged for Python."""

from pathlib import Path
from typing import Tuple

_PACKAGE_DIRECTORY = Path(__file__).parent

JAVA_HOME = _PACKAGE_DIRECTORY.absolute() / "java-runtime"
JAVA = JAVA_HOME / "bin" / "java"

JAVA_VERSION: Tuple[int, int, int] = tuple(
    int(part)
    for part in (_PACKAGE_DIRECTORY / "java_version.txt").read_text().strip().split(".")
)
