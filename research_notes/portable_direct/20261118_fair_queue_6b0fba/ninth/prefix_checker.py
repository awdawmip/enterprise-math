"""Taskbook entry point for the prefix continuity checker."""
from pathlib import Path
import runpy

if __name__ == '__main__':
    runpy.run_path(str(Path(__file__).with_name('continuity_check.py')), run_name='__main__')
