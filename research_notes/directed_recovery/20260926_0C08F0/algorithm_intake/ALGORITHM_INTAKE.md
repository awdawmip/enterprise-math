# Shor algorithm intake — 2026-09-26

Status: read-only source intake; shared author context, not independent review; no scientific execution or remote mutation performed by this intake.

Frozen reproducer: Stage87 HEAD `0852cad130c1d877174d235687cf60c19f318c58`. Current EM Source snapshot: `08da9612fd2b27195ce4d5f8efe8b8791c14fe2f`. GK canonical: `6dff66ce260d85fc0244598cae4c527ccc133e4f`, supplied by the root's exact sync handshake. Root README/CURRENT are historical Stage5/7 pointers, so use exact Stage80–87 entries below.

## Exact complete-circuit entry

`stage80/run.py:27 one_case(N,a,t,bank,intv,dim,bits)` performs:

1. `stage80/fixed_phase.py:291 prepare_fixed` → `stage79/phase_compiler.py:189 prepare` → `stage78/shor_benchmark.py:130 prepare_and_modexp`. Native quartet preparation enumerates Q=2^t control paths and controlled modular powers; work label is y=a^x mod N. No order/factors enter preparation. Modular multiplication is a permutation produced by actual BRC positive transition columns (`modular_columns`, line90), but its full table has 2^ceil(log2 N) entries and a dense graph.
2. `stage80/fixed_phase.py:274 run_qft`: bit reversal, then for bit b=0..t−1 each control c<b applies frozen phase bank[b−c+1], then actual H4 acting on b and one retained spectator. All internal residual modes remain. `compile_fixed_bank(10,32,64)` makes the frozen 61-mode bank; no new ideal/trigonometric QFT is substituted.
3. `stage80/fixed_phase.py:295 law`: exact integer squared norm over all work, spectator and internal modes for each k; denominator is the squared common dyadic denominator. This is a declared BORROWED_REFERENCE quadratic readout, not a Born-law derivation.
4. `stage78/shor_benchmark.py:247 denominators` and `:255 classical_postprocess`: CF convergent denominators q≤N−1; reject q unless a^q=1; reject odd q; compute a^(q/2) then actual BRC Euclid traces for gcd(h±1,N); validate each nontrivial factor. q is a verified returning exponent, not claimed minimal order. k=0, odd order, or trivial gcd are explicit retry outcomes.
5. The benchmark enumerates every k and reports exact success probability. It does not expose a single-shot retained-mode sample → retry → change-base end-to-end driver.

## Input and existing closure scope

The shipped acceptance suite is exactly `(15,2,4),(15,4,4),(15,7,4),(15,14,4),(15,2,8),(21,2,6),(21,8,6),(21,4,6),(21,2,10),(33,2,6),(33,5,6),(35,2,6)`; tolerance 1/10^6. Preparation explicitly rejects odd t. Coprimality is required by modular columns. The bank contains phases 2..10; `run_qft` requires bank coverage through t. The program has no complete documented validation contract for arbitrary N/a/t; avoid extrapolating beyond mathematical function preconditions and proofs. Only the t8 N15 and t10 N21 examples satisfy the usual Q≥N² precision setting.

Existing Stage80 theorem: for unmodified circuits, exact native fixed-word law is within `E_t=E79_t+((t−1)(t−2)/2)*4*2^(−B/2)` of ideal Shor; frozen B64/target32 gives E4,6,8,10=(15,51,111,195)/2^32. Full inverse retains all residual modes. This is already a conditional low-bit classical simulation, with explicitly potentially exponential state/table cost. Stages81–87 (and the later39/58/145/146 directions) study restricted future languages/observational quotients; they do not close general full-Shor storage or scalability.

## OPEN gaps and a distinct smallest closure route

**Recommended new unit: terminal-output instrument compilation.** Move each control bit's terminal computational measurement immediately after its last H4, because every subsequent use of that bit is as a diagonal classical control. Prove commutation of this projector with all subsequent controlled fixed phase words and other-bit H4 operations. Keep its outcome as a classical branch label and retain the *same* spectator and all61 residual modes. Recursively compute branch weights by exact integer squared norms; never renormalize by an irrational square root. Use exact rational Bernoulli sampling at each nonzero branch. Prove via deferred measurement that the resulting full output law equals the existing Stage80 law, then reuse unchanged CF/gcd postprocessing and inherited ideal-TV bound. This closes algorithmic output semantics rather than adding more observable moments. It does not in itself remove exponential work or establish spatial hardware.

The old `stage10/coherent_sampler.py` already samples a rational spectral phase j/r, but obtains r through classical order finding and uses stage6 Dyadic root/cos intervals. `stage13/factor_demo.py` compiles a sparse candidate law and runs CF/gcd. These are not the ACTUAL_TYPED_BRC_ONLY fixed-word route; they should be prior-work context only, not silent substitute implementations.

Specific OPENs after that unit: no general polynomial classical runtime; no autonomous six-axis routing/resource proof; no native probability-law derivation; no supported coherent access after the terminal-measurement contract; no all-input factor-success guarantee for a fixed bad base (e.g.15/a14). Factor retry and base-selection can be given an explicit bounded status, not false unconditional success. Odd-t preparation can be avoided by the next even t meeting Q≥N², without changing an original frozen case.

## Provenance inspected

Exact source files: stage78/shor_benchmark.py; stage79/phase_compiler.py; stage80/{fixed_phase.py,run.py,PROOF.md,TEST_CONTRACT.json,BRC_CONTRACT.json}; stage86/PROOF.md; stage87/{PROOF.md,BOUNDARY_CONTRACT.json}; older stage10/coherent_sampler.py and stage13/factor_demo.py. Current Source HANDOFF.md (blob bbdb1902f19511ba0c1ccf75d63892edb6cb03fc) and brc/PHASE34_RESEARCH_NOTE.md (blob7ac0bf29d8c28d334945fbca1310eb55f0b5061f) were fetched at the immutable snapshot above. The latter explicitly says the second-phase58 representation has not rerun full Shor. P000 and ACTUAL_TYPED_BRC_ONLY remain in force.
