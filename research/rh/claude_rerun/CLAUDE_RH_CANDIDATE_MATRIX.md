# CLAUDE_RH_CANDIDATE_MATRIX

Task: `RS-RHR-CLAUDE-RH-RERUN-20260811`  
Researcher-ID: `RHR-9Q6M2K`

Ranking criterion: first-hand provenance strength for the phrase “Claude proved RH”, not perceived mathematical plausibility.

| Rank | Candidate | Claude role | Full RH claim? | First-hand object / frozen version | Transcript | Code | Formal proof | Evidence strength for rumor | Rerun disposition |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | Coleman / Claude V6 Trace-Neutral Kakeya Operator | **co-developed / co-derived**; Fable 5 model sign-off | **NO** — explicitly says RH OPEN | PeAIce canonical paper, 2026-06-10; `Manny536/kakeyalogic@6f12f0f...` | no raw full transcript located | yes | no full RH formalization | **STRONGEST Claude-specific RH object, but contradicts rumor wording** | faithful rerun of operator and spectral bridge |
| 2 | Avi Gershon, _The De Bruijn-Newman Constant Is Zero_ | Claude Opus 4.6 acknowledged for computation, review, Lean 4 formalization | **YES, author claims unconditional RH** | Preprints.org `202604.1513.v1`, posted 2026-04-22 | not located | scripts/certificates claimed in paper | Lean assistance claimed; load-bearing Lean closure not located | **Plausible source of “Claude helped prove RH” → “Claude proved RH” mutation** | full DAG through first fatal lemma |
| 3 | Dan Alec Yamaguchi, Gram Jacobi / spectral determinant | no locked Claude attribution | **YES** | `danalec/riemann@ccbc3cf...`, v3, DOI 10.5281/zenodo.20357668 | N/A | yes, 77 C programs claimed | no full formal closure locked | fallback Candidate C from taskbook | adversarial spectral-bridge rerun |
| 4 | CIPHER / RTSG functional-bridge campaign | multi-agent adversarial assembly includes Claude | historical proof attempts; current page says **NO PROOF** | CIPHER Final Honest Status, Round 6 | public adversarial archive, not one raw Claude transcript | mixed | no full closed proof | negative control | verifier calibration |
| 5 | Adil Moujahid Fable 5 RH explainer | Fable 5 generated educational site/video and checked numerical data | **NO** | original social post + educational site reports, June 2026 | prompts summarized | site code not material | no | secondary-retelling hazard | provenance-only |

## Key distinction

The evidence currently supports:

`Claude co-developed RH research`  
and  
`Claude assisted review/computation/formalization of at least one author-claimed RH proof`

but does **not** support:

`Claude independently produced a completed RH proof`.

## Candidate route labels

- **A — Claude/Fable spectral operator**: Coleman/Claude V6.
- **B — Xi kernel / TP route**: Gershon 2026 v1.
- **C — spectral determinant / Hilbert–Pólya route**: Yamaguchi 2026 v3.
- **D — adversarially failed AI proof**: CIPHER/RTSG.

All four are retained because the taskbook requires verifier calibration even if the rumor itself resolves to a non-proof source.
