# Source and verification provenance

- New author-side result: 2026-11-04; class `AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_INTERVAL_EXECUTED`; no independent review or native Source Result.
- Frozen scientific baseline: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`, unchanged.
- Direct predecessor: `awdawmip/enterprise-math@bf6eecdfdc6723a3d8b00c18282795e661a45fc4:research_notes/brc_n4_s23_chernoff_sixth_order_boundary_20261103_research1/PROOF.md` (PR #1765).
- Current behavioral governance read at execution: global `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, output and math policies; EM `docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context`, `docs/PORTABLE_RESEARCH_PROTOCOL.md`, current research method and P000 / ACTIVE worldview.
- Reproduce: `python3 VERIFY.py`. Standard-library `fractions.Fraction` and `math.isqrt`; all assertions must pass. Output in `RUN_EVIDENCE.txt`; no float inputs or precision-library assumptions enter proof.
- Certifies: exact endpoint signs and the strictly positive derivative on a rational interval for fixed h=1/42. Computer implementation and analytic envelope formula are author-verified, not independently audited.
- Native activity / owner / claim: no verified current native Researcher-ID or CLAIM; control inventory query returned `CONTROL_QUOTA`, Site reported `research_authority_granted=false`; this PR is author-side and must not be treated as an admitted Result.
- Confidentiality: no tokens, credentials or session keys included.
