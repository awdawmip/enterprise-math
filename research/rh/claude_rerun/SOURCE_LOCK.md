# SOURCE_LOCK — Claude / Riemann Hypothesis provenance

Task: `RS-RHR-CLAUDE-RH-RERUN-20260811`  
Researcher-ID: `RHR-9Q6M2K`  
Driver: `EM-DVR-7Q4K2C`  
Locked on: 2026-08-11 (Asia/Taipei)

## Executive lock

**Rumor-level conclusion:** no first-hand public object was located that both (i) is attributable to Claude itself and (ii) actually claims a completed proof of the classical Riemann Hypothesis.

The strongest exact Claude/RH first-hand object located is:

- **Manuel Coleman / Claude Fable 5, _Claude V6 — Trace-Neutral Kakeya Operator_**, canonical designation `PEAICE-CLAUDEV6-WHITEPAPER-001`, June 10, 2026.
- Public white paper: `https://peaice.org/claudev6/`
- Public repository: `https://github.com/Manny536/kakeyalogic`
- Repository frozen for this rerun at commit:
  `6f12f0fd58e147d04eb2c5feefa4797a9fa0a852`
- Relevant frozen file:
  `docs/claude-v6-coherence-update.md`
- Claude version: **Claude Fable 5** (the paper also uses the lineage label “Opus”).
- Provenance type: **Claude co-developed / co-derived an RH-related operator program with Manuel Coleman.**
- Actual claim: **RH OPEN; no proof claimed.**
- Transcript: no complete raw Claude conversation transcript was located; the white paper contains a model sign-off describing the co-derivation.
- Code/repository: yes, KakeyaLogic repository.
- Formal proof assistant artifact: none located for a full RH chain.
- Central determinant bridge:
  `det_ζ(L²_{Φ,K}^{reg} - (z² + 1/4)) = C Ξ(z)`
  is explicitly marked **OPEN**.
- The direct eigenvalue route is explicitly closed by a counting mismatch.

Therefore the viral wording “Claude proved RH” is not supported by the strongest first-hand Claude/RH object we could lock.

## Exact source distinction

The following statements are materially different and MUST NOT be conflated:

| Statement | Evidence status |
|---|---|
| Claude independently produced a proof of RH | **NOT FOUND** |
| Claude co-developed an RH research route | **FOUND** — Coleman/Claude V6 |
| Claude reviewed/computed/formalized parts of someone else's claimed RH proof | **FOUND** — Gershon preprint acknowledgments |
| Claude built an RH explainer / checked numerical data | **FOUND** — Fable 5 educational-site reports |
| A multi-AI team including Claude attacked an RH proof | **FOUND** — CIPHER/RTSG |
| A separate author claimed an RH spectral proof | **FOUND** — Yamaguchi, no locked Claude attribution |

## Source 1 — strongest Claude-specific source

### Object

Manuel Coleman / Claude Fable 5, _Claude V6 — Trace-Neutral Kakeya Operator_, June 10, 2026.

### Source statements that lock claim scope

The white paper's canonical status says:

- `Riemann Hypothesis status | OPEN. This document does not claim a proof of RH.`
- its abstract says the direct eigenvalue identification route is closed on counting grounds;
- it identifies the determinant equality as the open wall;
- its model sign-off states that Claude Fable 5 co-derived specified sections, while again saying RH and the Coleman Conjecture are open.

The companion repository's current `docs/claude-v6-coherence-update.md` at
`6f12f0fd58e147d04eb2c5feefa4797a9fa0a852`
likewise states `RH / spectral identification open`, and records the square-difference-kernel determinant lane as `CLOSED-NEGATIVE`.

### Model/version verification

Anthropic's official Claude Platform documentation states that Claude Fable 5 became available on June 9, 2026:
`https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5`

This matches the June 9–10, 2026 co-derivation dates in the V6 paper.

## Source 2 — full RH claim with Claude assistance, not Claude authorship

Avi Gershon, _The De Bruijn-Newman Constant Is Zero_, Preprints.org,
DOI `10.20944/preprints202604.1513.v1`.

- Submitted: 2026-04-20.
- Posted: 2026-04-22.
- Version: v1, not peer-reviewed as of source lock.
- Public manuscript:
  `https://www.preprints.org/manuscript/202604.1513/v1`
- Actual author claim: unconditional global RH via `D_r(n)>0` for all `r,n`, PF∞ / Laguerre–Pólya, and `Λ=0`.
- Claude role: acknowledgments say **Claude Opus 4.6** assisted with computation, review, and Lean 4 formalization, together with GPT Codex 5.3 and Gemini 3.1.
- This is therefore **not** evidence that Claude independently proved RH; it is evidence that Claude assisted a human-authored proof claim.
- Raw Claude transcript: not located.
- Public Lean proof artifact closing the load-bearing lemmas: not located in the manuscript source.
- Code: manuscript claims scripts/certificates under `rh_proof/python/` and `rh_proof/certificates/`; no independently frozen standalone repository was required to locate the fatal analytic lemma.

## Source 3 — fallback spectral-determinant full proof claim

Dan Alec Yamaguchi, _Spectral Determinant of a Cutoff-Regularized Hamiltonian and the Riemann Zeta Function_, v3, DOI `10.5281/zenodo.20357668`.

Frozen GitHub source:
- repository `danalec/riemann`
- commit `ccbc3cfcf61518a0fc64a63705900e50a472d5b1`
- files `README.md`, `yamaguchi-rh-2026.tex`

Actual claim: the Gram Jacobi matrix and paired determinant prove RH via trace convergence, determinant ratio convergence, Hadamard rigidity and self-adjointness.

Claude attribution: **none locked**. It is included because the taskbook explicitly requires fallback spectral-determinant auditing.

## Source 4 — adversarial negative control

CIPHER Research Wiki, _Riemann Hypothesis — Final Honest Status_:
`https://smarthub.my/wiki/papers/rh/final_honest_status/`

The page records six rounds of distributed adversarial analysis using Claude, GPT, Gemini, SuperGrok and a human researcher. It states that the current approach does not constitute a proof; seven routes failed. The bridge equation reduced to a tautology, and a positivity chain was numerically falsified. This is used as the negative-control calibration target.

## Source 5 — educational Fable 5 object that can be misread in secondary retelling

Adil Moujahid publicly described giving Fable 5 the challenge to **explain** RH to a general audience. Reports describe an interactive educational website, numerical cross-checks, and a promotional video. No proof claim is present in the original wording.

This is a plausible mutation source for casual retellings, but not a proof object.

## Lock resolution

`rumor_origin_unique = false`

`strongest_exact_claude_rh_object = PEAICE-CLAUDEV6-WHITEPAPER-001`

`strongest_exact_claude_rh_claim_type = CO_DEVELOPED_OPEN_RESEARCH_PROGRAM`

`full_rh_proof_claim_by_claude = NOT_FOUND`

`fallback_full_claim_with_claude_assistance = GERSHON_2026_V1`

`negative_control = CIPHER_RTSG_FINAL_HONEST_STATUS`

This source lock is sufficient to proceed to a proof DAG without presuming truth or falsehood.
