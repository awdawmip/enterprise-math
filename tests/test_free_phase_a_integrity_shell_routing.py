from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHELL = "research_roles/EM_FREE_RESEARCHER_PHASE_A_INTEGRITY_SHELL.md"


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def test_integrity_shell_is_zero_example_rigor_surface():
    text = read(SHELL)
    assert "PHASE_A_INTEGRITY_SHELL != PHASE_B_FULL_AUDIT_POLICY" in text
    assert "RIGOR_DOES_NOT_REQUIRE_AGENDA_PRELOAD" in text
    assert "DISCOVERY_EVIDENCE != INDEPENDENT_VALIDATION_EVIDENCE" in text
    assert "current theorem/result names" in text
    assert "suggested open questions" in text
    for seeded in (
        "classical pi",
        "graph distance",
        "root choice",
        "random-walk",
        "current numbered route",
    ):
        assert seeded not in text


def test_agents_routes_free_rigor_to_shell_not_full_policies():
    text = read("AGENTS.md")
    assert SHELL in text
    assert "The integrity shell is the default FREE Phase-A rigor surface" in text
    assert "Do not preload their bodies in clean FREE Phase A" in text
    assert "FOUNDATIONAL_LOGIC.md" in text
    assert "native_semantics_admissibility.json" in text
    assert text.index(SHELL) < text.index("The full policies:")


def test_free_role_and_anti_anchor_route_to_shell():
    for rel in (
        "research_roles/EM_FREE_RESEARCHER_ROLE.md",
        "research_roles/EM_FREE_RESEARCHER_ANTI_ANCHORING_PROTOCOL.md",
    ):
        text = read(rel)
        assert SHELL in text
        assert "FOUNDATIONAL_LOGIC.md" in text
        assert "native_semantics_admissibility.json" in text
        assert "Phase-B" in text or "Phase B" in text


def test_tool_surface_has_shell_in_free_hot_start():
    text = read("docs/EM_RESEARCH_TOOL_SURFACE.md")
    section = text.split("## FREE_AXIOM_DISCOVERY hot start", 1)[1].split("## Triggered reads", 1)[0]
    assert SHELL in section
    assert "FOUNDATIONAL_LOGIC.md" not in section
    assert "native_semantics_admissibility.json" not in section
    triggered = text.split("## Triggered reads", 1)[1]
    assert "FREE Phase-B" in triggered
    assert "FREE Phase-A integrity shell" in triggered
