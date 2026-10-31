# PREFIX-406 — execution, source and continuation evidence

Date: 2026-11-01. Research model: external static complex three-amplitude/five-Port; normalised I1=1; six nonzero-width closed rational readout bands.

## Frozen input and provenance
- GLOBAL_KNOWLEDGE_V1 canonical main: b687941eae4c219b60f62a03369de1449bd1ad23.
- Enterprise Math scientific/control read snapshot: 4d349d63a10612d9e196f49791bd5946c6dd9bba.
- Predecessor: research_notes/2026-11-01_prefix405_all_noisy_exact_refutation_and_robust_nonconvexity.md.
- Native site service: version 0.6.11, authenticated client sites-em-6abdec598ad48191aebece9a8232f041-ro; research_authority_granted=false; exact owner-task list read returned CONTROL_QUOTA. No task was claimed, no formal Result, no Driver review.

## Actual execution

Python 3.13.5, SymPy 1.14.0. Executed:
1. python prefix406_exact_psd_gap.py -> PASS_PREFIX406_ROBUST_PSD_RANK_GAP.
2. python prefix406_independent_fraction.py -> PASS_PREFIX406_INDEPENDENT_FRACTION_PSD_RANK_GAP.

Exact values independently checked:
- PSD witness H0=diag(1,1,0), rank 2;
- six lifted readouts (I2, Cu, I3, Cv, I4, I5)=(1,2,0,1,41,709/32);
- coefficient products a*conj(b)=39/2-2i, a*conj(c)=18-10i, b*conj(c)=14-6i;
- absolute error upper bound 74727/100000 < 3/4;
- universal PSD second-eigenvalue lower bound, strict: 5623/10000;
- rank-one strict exclusion margin: 217169319/100000000;
- endpoint perturbation bounds: 64470681/100000000, 82830681/100000000.
Both programs use exact rationals. First checker re-derives coefficients from the original complex matrix with SymPy; second independently uses Fraction complex pairs.

Actual local Git blob SHA-1 and remote readback targets:
- prefix406_exact_psd_gap.py: c1533d457bb7cc31d3767d0ba5cdc4996cf8c130
- prefix406_independent_fraction.py: 1de9f5edfb66530e416554703353480fe6fa2049

The proof is a universal exact inequality argument; the finite code runs check its arithmetic and symbolic ingredients, not all continuous PSD points by enumeration.

## Interpretation and limits

This is a concrete robust false-positive of the PSD feasibility relaxation, not a failure claim about general PhaseLift theorems under their random-sensing assumptions. Retain the original complex sources and phase/sign branches; rank-two PSD matrix is a mixture, not a single coherent source. No typed BRC computation, native X6 embedding, independent audit, Lean formalization, or mathematical admission is claimed. The full six-noisy boundary-only YES solver inherited from PREFIX-405 remains unfinished.

## Next minimal research unit PREFIX-407

Derive a reusable finite algebraic certificate for rank-one exclusion from PSD principal minors and linear Port slabs. Classify the I3=0 algebraic boundary slice completely, including rational and irrational phase branches; test whether the positive spectral gap can remain certified when the band widths are enlarged. Compare certificate size against the PREFIX-405 box-partition NO checker. Preserve each distinct source, observer, Port and phase branch. Formal native task authority and independent review remain pending.

Status: GITHUB_RESEARCH_EVIDENCE / AUTHOR_SIDE_EXACT_VERIFIED / UNREVIEWED / NOT_ADMITTED / NATIVE_REGISTER_PENDING.
