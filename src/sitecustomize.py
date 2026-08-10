"""Temporary CI diagnostic hook for the R004 research proposal.

This file is intentionally temporary.  It does not alter test semantics; it
only mirrors unittest failures/errors into GitHub workflow annotations so the
connector can retrieve the first failing file/line when full job logs are not
available through the API surface.
"""

from __future__ import annotations

from pathlib import Path
import traceback
import unittest

_ROOT = Path.cwd().resolve()
_ORIGINAL_FAILURE = unittest.TextTestResult.addFailure
_ORIGINAL_ERROR = unittest.TextTestResult.addError


def _workflow_escape(text: str) -> str:
    return (
        text.replace("%", "%25")
        .replace("\r", "%0D")
        .replace("\n", "%0A")
        .replace(":", "%3A")
        .replace(",", "%2C")
    )


def _emit(test: unittest.case.TestCase, err, kind: str) -> None:
    frames = traceback.extract_tb(err[2])
    chosen = None
    for frame in reversed(frames):
        path = Path(frame.filename).resolve()
        try:
            path.relative_to(_ROOT)
        except ValueError:
            continue
        chosen = (path, frame.lineno)
        break
    if chosen is None:
        return
    path, line = chosen
    rel = path.relative_to(_ROOT).as_posix()
    message = f"{test.id()} | {err[0].__name__}: {err[1]}"
    print(
        f"::error file={_workflow_escape(rel)},line={line},"
        f"title={_workflow_escape('unittest ' + kind)}::"
        f"{_workflow_escape(message)}",
        flush=True,
    )


def _add_failure(self, test, err):
    _emit(test, err, "failure")
    return _ORIGINAL_FAILURE(self, test, err)


def _add_error(self, test, err):
    _emit(test, err, "error")
    return _ORIGINAL_ERROR(self, test, err)


unittest.TextTestResult.addFailure = _add_failure
unittest.TextTestResult.addError = _add_error
