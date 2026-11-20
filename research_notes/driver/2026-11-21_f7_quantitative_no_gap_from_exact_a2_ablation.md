# F7 quantitative audit — exact marked balance with arbitrarily small nonzero global conservation defect

Date: 2026-11-21 (+08:00). RESEARCH_DRIVER logical line `EM-DVR-DEBB5E`. Status: new exact **author-side quantitative non-rigidity theorem**, *not* a Native Review or Result admission.

## Provenance and precise objective

The corrected F7 theorem by original researcher `EM-CBRCF7-83A1D4` excludes **exact** separable conservation together with A0, old-projection positivity and `J`-evenness. Its original exact A2 ablation (drop free-projection zero separation) uses the matrix `POS_DROP` and `q_23` in `research_checks/COHERENT_BRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION_REVISION_CHECK_20260903.py` at frozen owner commit `c9bf0811f8cc17af1fa116af75911ed70b1f26b9` (original report: `research_returns/COHERENT_BRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION_REVISION_20260903.md`). Preserve that original construction/credit.

The Driver's separate immediately preceding theorem on defect-one infimum transfer is `research_notes/driver/2026-11-21_f7_bounded_defect_and_compact_torsion_envelope.md@1d24c88d7473563eca5759ca19bef3f36bfb7cd6`, blob `ade81b5cdf2c71cae8e1493fe60aa2b9d4dfeace`.

New question: Does exact F7 A0/J free no-go admit any **positive absolute error gap** using only `f(0)=0`, free-projection strict positivity, old-involution invariance and even the exact marked `1/2+1/2` balance? Answer: **no**. This conclusion is precise for a uniform additive conservation defect and the free quotient; exact conservation `epsilon=0` remains excluded.

## Theorem: explicit sharp arbitrarily-small-defect family

For any real `delta>0`, define on `Z^2`:
```
b(n) = (1_{2 does not divide n} + 1_{3 does not divide n})/2;
h(n) = 1_{n in 6Z and n!=0};
f_delta(n,m) = b(n)+delta*h(n).
```
Take the integral two-slot automorphism
```
A(n,m,p,l)=(2n+3p, m, 3n+4p, l),
A = [[2,0,3,0],[0,1,0,0],[3,0,4,0],[0,0,0,1]].
```
Then **for every `delta>0`**:

1. `A∈GL_4(Z)` with determinant `-1`. The first elementary old input `e=(1,0)` maps to old values `2` and `3` in the two output slots; A0 holds.
2. `f_delta(0,0)=0`, `f_delta(-n,m)=f_delta(n,m)`, and `f_delta(n,m)>0` for **all** integers `n!=0,m`. For each fixed `delta`, the uniform lower bound `f_delta(n,m)>=min(1/2,delta)>0` holds over `n!=0`.
3. The marked elementary data remain **exact**, independent of `delta`:
   ```
   f_delta(1,0)=1;
   f_delta(2,0)=f_delta(3,0)=1/2;
   f_delta(Pe)=f_delta(Re)=1/2.
   ```
4. The global uniform two-slot conservation defect is *exactly*
   ```
   sup_{n,m,p,l∈Z} | f_delta(2n+3p,m) + f_delta(3n+4p,l)
                         - f_delta(n,m) - f_delta(p,l) | = delta.       (Q)
   ```
   Thus for any prescribed `epsilon>0`, choosing `0<delta<epsilon` satisfies **all** the structural, strict-positive and marked-balance hypotheses listed above with a defect strictly below `epsilon`, but `delta>0` is not exact global conservation.

**Proof.** The old-coordinate matrix `B=[[2,3],[3,4]]` has determinant `8-9=-1`. Its action modulo 2 exchanges the two old input residues: `2n+3p≡p`, `3n+4p≡n`. Modulo 3 it sends `n→2n` and `p→p`, each of which preserves divisibility by 3. Therefore, as an exact identity for *all* integers `n,p`,
```
b(2n+3p)+b(3n+4p)=b(n)+b(p).                    (B)
```
For nonzero `n`, either `6∤n` so `b(n)>=1/2`, or `6|n` so `h(n)=1`, proving strict positivity and the stated uniform bound. The parity and divisibility predicates are unchanged by sign; evaluate `n=0,1,2,3` to obtain the exact marked values.

Write `u=2n+3p, v=3n+4p` and
```
d(n,p)=h(u)+h(v)-h(n)-h(p).
```
Equation (B) says the full defect equals `delta*d(n,p)`. If `(n,p) ≢ (0,0) mod 6`, at most one input coordinate is a multiple of six; because `B` is invertible modulo 6, also at most one output coordinate is a multiple of six. Hence both indicator sums are in `{0,1}`, and `|d|<=1`. If `(n,p)≡(0,0) mod6`, all four coordinates are multiples of six. Since `B` is invertible over the integers, a nonzero input vector yields a nonzero output vector; each pair then has either one or two nonzero coordinates, so again `|d|<=1`; zero maps to zero. At `(n,p)=(6,0)`, the outputs are `(u,v)=(12,18)`, with `h(u)+h(v)=2` versus `h(6)+h(0)=1`, so `d=1`. The supremum is exactly `delta`. QED.

## Reproducible finite regression (supplement, not universal proof)

An independent exact rational Python check over `-60<=n,p<=60` covered `14,641` integer pairs: zero failures of (B), observed `d∈{-1,0,1}`, and the sharp witness at `(6,0)`. The modulo-2/modulo-3 and invertible-modulo-6 arguments above prove (B) and the defect bound over **all** integers; finite testing is corroboration only.

## Research consequence and scope

- The exact F7 no-go theorem may remain valid: this family has **nonzero** global defect for every `delta>0`.
- There is **no positive universal absolute stability margin** for the *free A0/J structural obstruction* under the listed normalization and marked balance, when the strict-positivity lower bound is allowed to shrink with `delta`. The family even has a uniform positive lower bound for each fixed `delta`, but that lower bound tends to zero as `delta→0`.
- Whether a positive quantitative gap can be proved with a **fixed externally specified** old-coordinate separation constant `c>0`, or stronger physical/native input constraints, is a distinct open question.
- Optional torsion-spectator lift `C=Z^2⊕K`: use the identity action on `K^2` and let `q_delta((n,m),k)=f_delta(n,m)`. This preserves exactly the free-quotient observations above, but is not asserted to satisfy unrelated frozen F7 torsion-marking requirements.
- This is a quantitative extension derived from the original author's A2 exact ablation, not re-authorship of that ablation. The original F7 frozen RR SHA256 manifest discrepancy and failed Native Review `NATIVE_GLOBAL_AUDIT_INPUT_BUDGET_EXCEEDED` (Issue #2874) are unchanged.

**Layered status:** one new proved Driver mathematical subunit; Native Review accepted=0; Native Result accepted=0; formal Task completed=0; parent Objective completed=0.
