# EC49BS — Typed selective-ensemble BRC, exact native reduction, finite-state realization

**2026-10-31 | Author-side portable research | UNREVIEWED / NOT_ADMITTED.**
Parent: EC49BR (PR #1730), `NEXT_TASK_EC49BS.md` in `EC49BR_GROUP_ORBIT`. No canonical Task owner, CLAIM, Result, review or activity-registration is asserted. Local/executing author is the present Researcher-4 scheduled conversation, not an independent reviewer of its predecessors.

## New exact mathematics

Let `D={+E1,-E1,...,+E6,-E6}`, `w:D→Q_{>0}`, `U_{n,z}={ordered words of n signed-X6 steps whose displacement is z∈Z6}`. A selected ensemble is a finite map `μ:U_{n,z}→Q_{≥0}` carrying exact word identity, ordering, multiplicity and optional source tags. An ordered Boolean sequence of selectors yields `F(t)`. Define

`SelectiveBRC(n,z,w,μ,F) = Σ_{t∈U_{n,z}} μ(t) F(t) Π_{j=1}^{n} w(t_j)`.

A tagged-source filter must be applied *before* collapsing source labels into multiplicities. A fixed instrument observes `χ_w(σt)` and a covariant instrument `χ_{σw}(σt)`, with `(σw)(σd)=w(d)`; the latter equals `χ_w(t)` exactly.

**Theorem A (conservative native reduction).** For `μ≡1` and `F≡1`, the defined selective sum equals `signed_brc.endpoint_weight(n,z,wp,wm)` for EVERY nonnegative integer n, integer six-axis z and strictly positive rational signed weights. Proof: every word uniquely has `a_i+k_i` plus and `b_i+k_i` minus steps, where `a_i=max(z_i,0)`, `b_i=max(-z_i,0)`, `Σk_i=(n-Σ|z_i|)/2`. For every feasible k the order count is `n!/Π_i(a_i+k_i)!(b_i+k_i)!`, exactly the original native kernel's rational summand; impossible parity/length has zero paths on both sides. No new numerical propagation law is substituted for the pinned native BRC.

**Theorem B (finite-state selection).** For any complete DFA `(Q,q0,δ,F)` recognizing a selector on signed ordered words, form the 6-variable Laurent-polynomial transition matrix `T_{ab}(x)=Σ_{d:δ(a,d)=b}w(d)x^{Δ(d)}`. Then the selected all-word BRC equals `[x^z] Σ_{b∈F}(T(x)^n)_{q0,b}`. The identity follows by induction over all ordered word prefixes, with each term preserving its original branch and exact multiplicity. This is the established weighted-automata construction applied to the typed native X6 carrier, NOT a claim of independently inventing weighted automata. For custom nonregular source-provenance conditions, use a provenance-aware tagged carrier or explicitly prove the state reduction.

**Theorem C (exact DP resource upper bound).** If `s=|Q|` and `B` is a common denominator of the twelve weights, scaling each transition weight by B gives integer DP, then division by `B^n`. At step k at most `(2k+1)^6` displacement states are possible, so total arithmetic operations `O(12ns(2n+1)^6)`, working integer words `O(s(2n+1)^6)`, bitlength `≤1+⌈n log₂(12 Amax)⌉` for nonzero intermediate numerator sums, `Amax=max_d B w(d)`. An |H|-member fixed-group ensemble has the corresponding |H| multiplier. This is pseudo-polynomial in n, not an input-bit complexity bound.

**Theorem D (future-language memory lower bound).** If the allowable future filters include every singleton word predicate on `U_{2m,0}`, then all nonnegative rational ensembles require `dim_Q = |U_{2m,0}| = signed_brc.endpoint_multiplicity(2m,0) ≥ 2^m` rational-linear additive coordinates. The singleton-weight rows have positive diagonal entries and are linearly independent; the nonnegative baseline argument proves no smaller rational-linear additive state can reproduce all future outputs. The smaller polynomial-time DP bound of Theorem C is for computing ONE FIXED DFA query, not simultaneously representing every possible future selector. No arbitrary encoding/bit lower bound is asserted.

## Exact falsifying witnesses for premature compression

(1) The words `(+E1,+E2,-E1,-E2)` and `(+E2,+E1,-E1,-E2)` share displacement, signed histogram and product weight, but the selector “contains consecutive (+E1,+E2)” distinguishes them. (2) Two source-tagged copies of one identical path have identical unfiltered weighted totals under distinct source assignments; source-A filtering distinguishes the assignments. Thus projecting to endpoint, histogram, or source-blind totals cannot support this future operation language.

## Actually executed author audit

The complete local checker `VERIFY_EC49BS.py` was executed TWICE with byte-identical exact JSON outputs using Python Fraction and the original unmodified native file `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` **Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176`**. Its exact full source, proof, stdout, next task and source ledger are supplied in the adjacent encoded archive (see below), not reconstructed by this summary.

Weights `wp=(2,5/2,5/3,7/4,11/5,13/6)`, `wm=(1/2,2/3,3/4,4/5,5/6,6/7)`. Exhaustively enumerate all `Σ_{k=0}^4 12^k=22621` native ordered words and compare `1375` endpoint weight/count kernel values. Compare `1547` nonzero DFA filter DP states with independent brute enumeration. At n=6 and z=0, the complete closed-path space contains `19920` paths: unfiltered weight `27430273363/411600`, prefix +E1/suffix −E1 weight `26133109/29400`, and substring (+E1,+E2) weight `32230/21`. Fixed swap (E1 E2) n=4 gives `1261/42` versus original `1261/70`; covariant swap gives `1261/70`. The all-integers scope follows the proofs; these tests are finite exact audits.

## Reproduction and sources

The full archive `EC49BS_exact_sources.tar.xz.b64` is UTF-8 base64. Extract: `base64 -d EC49BS_exact_sources.tar.xz.b64 | tar -xJf -`. It contains **PROOF_EC49BS.md, VERIFY_EC49BS.py, EXACT_REPORT_EC49BS.json, NEXT_TASK_EC49BT.md, SOURCES_AND_HANDOFF_EC49BS.md, MANIFEST_EC49BS.json**. Archive SHA256 (binary after base64 decode): `efd01bb0be82d4d75d8cfffc19e1766896eb5130364bea8b9be947afe3e3f797`; it is 12192 bytes. Run `python VERIFY_EC49BS.py` from the EC49BS directory with the pinned native `signed_brc.py` available as declared in the source handoff. Original project code is not replaced. Formal Source admission is distinct from artifact storage.

**Frozen scientific source pins:** GLOBAL_KNOWLEDGE_V1 `main@a08122dc5be8c74586a760b59d218b54923bcfbc`, Enterprise Math `main@0e30c3ba78dc5767e83f15b4a75f791353cc174d`; incoming author PR HEAD `9178acfb72a9b6abe5020447b76dd66290d45c0a`. P000, ACTIVE worldview and native X6/observer contracts were read and are unchanged. Native service `research_authority_granted=false`, `CODE_REVIEW_REQUIRED`; exact owner inventory `CONTROL_QUOTA` (5/5). Thus `AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_NATIVE_AUDIT_PASS / PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED`.

**Next EC49BT:** For fixed n=6,z=0, compute exact rational-linear observation rank for a restricted language generated by signed substring, end filters and finite H; publish sparse rank certificates, distinguishing a finite-state single-query computation from minimum all-future-language memory.
