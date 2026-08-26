from __future__ import annotations

import json
from pathlib import Path

import pytest

from control_plane import research_task_head_serialization as heads


def test_same_task_always_uses_same_git_cas_path(tmp_path: Path) -> None:
    first = heads.head_path(tmp_path, "RS-SAME-TASK")
    second = heads.head_path(tmp_path, "RS-SAME-TASK")
    assert first == second == tmp_path / "research_task_heads" / "RS-SAME-TASK.json"


def test_different_tasks_do_not_serialize_each_other(tmp_path: Path) -> None:
    assert heads.head_path(tmp_path, "RS-A") != heads.head_path(tmp_path, "RS-B")


def test_unsafe_task_id_cannot_escape_head_directory(tmp_path: Path) -> None:
    with pytest.raises(heads.HeadSerializationError):
        heads.head_path(tmp_path, "../RS-ESCAPE")


def test_sync_rewrites_one_pointer_and_audit_detects_drift(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    record_dir = tmp_path / "research_task_records" / "RS-X"
    record_dir.mkdir(parents=True)
    record_file = record_dir / "TP-A.json"
    record_file.write_text("{}\n", encoding="utf-8")
    record = {
        "task_id": "RS-X",
        "publication_id": "TP-A",
        "publication_generation": 1,
        "_record_path": "research_task_records/RS-X/TP-A.json",
    }
    monkeypatch.setattr(heads.research_task_records, "current_records", lambda root: {"RS-X": record})

    heads.sync("RS-X", tmp_path)
    assert heads.audit(tmp_path) == []

    pointer = heads.head_path(tmp_path, "RS-X")
    value = json.loads(pointer.read_text(encoding="utf-8"))
    value["current_publication_id"] = "TP-SILENT-CONFLICT"
    pointer.write_text(json.dumps(value) + "\n", encoding="utf-8")
    errors = heads.audit(tmp_path)
    assert len(errors) == 1
    assert "head pointer drift for RS-X" in errors[0]
