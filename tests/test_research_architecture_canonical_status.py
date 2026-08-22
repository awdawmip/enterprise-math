import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_research_architecture_machine_status_is_canonical():
    data = json.loads((ROOT / "research_architecture.json").read_text(encoding="utf-8"))
    assert "CANONICAL" in data["status"]
    assert "PROPOSED" not in data["status"]


def test_axiom_candidate_machine_status_is_canonical():
    data = json.loads((ROOT / "research_axiom_candidate_state_machine.json").read_text(encoding="utf-8"))
    assert "CANONICAL" in data["status"]
    assert "PROPOSED" not in data["status"]


def test_human_architecture_and_candidate_protocol_are_canonical():
    for rel in (
        "docs/RESEARCH_ARCHITECTURE.md",
        "docs/RESEARCH_AXIOM_CANDIDATE_PROTOCOL.md",
    ):
        head = (ROOT / rel).read_text(encoding="utf-8")[:500].upper()
        assert "CANONICAL" in head, rel
        assert "DRIVER-PROPOSED" not in head, rel
