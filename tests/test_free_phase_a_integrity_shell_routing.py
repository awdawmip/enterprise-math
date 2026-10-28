from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHELL = "research_roles/EM_FREE_RESEARCHER_PHASE_A_INTEGRITY_SHELL.md"
SUBSTRATE = "definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md"


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def test_integrity_shell_remains_zero_example_rigor_surface_when_explicitly_used():
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


def test_agents_free_hot_path_uses_primitive_substrate_and_triggered_full_policies():
    text = read("AGENTS.md")
    assert SUBSTRATE in text
    assert "FREE Phase A receives the **primitive substrate**" in text
    assert "FOUNDATION_FOR_DISCOVERY != CATALOG_OF_CURRENT_ACHIEVEMENTS" in text
    assert "Load triggered semantic policies only when needed" in text
    assert "FOUNDATIONAL_LOGIC.md" in text
    assert "native_semantics_admissibility.json" in text
    assert "do not preload the general current-result router" in text


def test_free_role_and_anti_anchor_keep_full_integrity_policy_triggered_not_default():
    role = read("research_roles/EM_FREE_RESEARCHER_ROLE.md")
    anti = read("research_roles/EM_FREE_RESEARCHER_ANTI_ANCHORING_PROTOCOL.md")

    assert SUBSTRATE in role
    assert "foundational/native-semantic typing only when required" in role
    assert "Phase B — mandatory tool dedup and reuse resolution" in role

    assert SUBSTRATE in anti
    assert "foundational/native-semantic typing when the candidate makes such claims" in anti
    assert "Phase B — comparison and collision audit" in anti

    # The current hot contracts intentionally do not make the standalone shell a
    # mandatory default read. It remains an active zero-example rigor artifact,
    # while Phase-A default input is the primitive substrate plus triggered
    # integrity rules. This preserves the newer P000-bound/global minimal-packet
    # design instead of reintroducing an older default-read edge through a test.
    assert SHELL not in role
    assert SHELL not in anti


def test_tool_surface_free_hot_start_is_minimal_and_integrity_policy_is_triggered():
    text = read("docs/EM_RESEARCH_TOOL_SURFACE.md")
    section = text.split("## FREE hot start", 1)[1].split("## Triggered reads", 1)[0]
    assert SUBSTRATE in section
    assert SHELL not in section
    assert "FOUNDATIONAL_LOGIC.md" not in section
    assert "native_semantics_admissibility.json" not in section
    assert "suggested question/lens menu" in section

    triggered = text.split("## Triggered reads", 1)[1]
    assert "foundational/native-semantic policy" in triggered
    assert "when such claims are being frozen" in triggered
