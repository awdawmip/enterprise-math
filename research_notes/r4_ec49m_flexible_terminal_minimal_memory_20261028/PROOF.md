# EC49M — Flexible terminal decisions, strict four-observable separation, and minimum causal recall

**Status:** `AUTHOR_PROVED / EXACT_FRACTION_ENUMERATION_PASS / UNREVIEWED / NOT_ADMITTED / NATIVE_REGISTER_PENDING`.
**Provenance:** Direct continuation of EC49L, `awdawmip/enterprise-math` PR #1646, immutable commit `931bf561432ed4a8e2b95479f2ad4d626d1c2a33`. Independent author-side portable research; not a native session/CLAIM/Result or independent review. Author locally identified as `R4-EC49M-20261028-LOCAL` (not a service-issued identity).
**Frozen inputs:** GLOBAL_KNOWLEDGE_V1 `main@e531e8ab792fe44637f9d3be0a73ab5c0cf48669`; Enterprise Math current scientific input `main@bd0dd87b6864ce4994cee0a7d32eaacb0cfa4263`. ACTIVE P000 and worldview unchanged.

## 1. Model and declared observer

Use the finite strictly positive rational **auxiliary positive-weight BRC** branch model of EC49L, *not* native signed BRC, native X6 coordinates, or physical heartbeat time. The two source measures P and Q are separate exact rational branch weights over latent pairs (W,Y). The observer is the four-vector

`O=(alpha=P(accept), beta=Q(accept), E_P T, E_Q T)`, where T counts (i) the first selected/forced action and (ii) each purchased Y sensor; T is an observation count, not native time. Branch provenance W and joint W/Y weights are retained before any forgetting quotient.

The initial external W is one of U,V,C0,C1 with masses

| W | P(W) | Q(W) | P(Y=1 | W) | Q(Y=1 | W) | first action |
|---|---:|---:|---:|---:|---|
| U | 3/8 | 1/8 | 1/4 | 3/4 | optional A=1 or STOP |
| V | 3/8 | 1/8 | 3/4 | 1/4 | optional A=0 or STOP |
| C0 | 1/8 | 3/8 | 1/2 | 1/2 | mandatory A=0 |
| C1 | 1/8 | 3/8 | 1/2 | 1/2 | mandatory A=1 |

Every one of the 8 latent W×Y atoms under **each** source has strictly positive rational weight. After the first action, the unaugmented controller knows its own A but forgets W and whether the first action was forced; upon A=a it buys Y with probability q_a. **A nonpurchase rejects**, as in EC49L. **New relaxation:** after buying Y it may choose ACCEPT with arbitrary real probability `r_(a,y)` depending on retained A and the observed Y; before the purchase there is no discretionary acceptance. Every policy decision uses source-independent behavioral probabilities with fresh private randomization. The full-memory controller retains W after the first action and may use `q_W` and `r_(W,Y)`. Both controllers use the identical first-stage menu and latent P/Q measures.

This exact terminal relaxation is the question being tested; allowing ACCEPT before Y purchase is a *different* model and not covered by the separation certificate below.

## 2. Theorem A — relaxing terminal acceptance kills the EC49L irrational-only target

EC49L's original rational target

`O*=(7/64,13/64,27/32,41/32)`

had no rational fresh behavioral implementation with the *fixed* rule ACCEPT iff Y=1. With discretionary terminal acceptance the **same target is reachable by an entirely rational fresh behavioral policy even without restoring W**:

`p0=1, p1=0, q0=3/4, q1=1/4; r_(0,0)=0, r_(0,1)=1, r_(1,0)=r_(1,1)=1/2`.

Here p0 is the probability to take A=1 at U, p1 to take A=0 at V. Exact source-by-source summation gives

- Under P: stage-1 first-action mass `5/8`, sensor-purchase mass `7/32`, so `E_P T=27/32`. Acceptance: `C0,Y1` contributes `3/64`; the `U+C1` action-1 branch, accepted with probability 1/2, contributes `1/16`; hence `alpha=7/64`.
- Under Q: stage-1 first-action mass `7/8`, sensor-purchase mass `13/32`, so `E_Q T=41/32`. Acceptance: `C0,Y1` contributes `9/64`; the `U+C1` action-1 branch contributes `1/16`; hence `beta=13/64`.

Thus EC49L's *necessity* of irrational parameters depends essentially on its fixed terminal acceptance condition; the same target alone cannot certify irrationality under the enlarged action space. This does not prove that **every** rational target in the unaugmented, imperfect-recall region has a rational behavioral realization.

## 3. Theorem B — flexible terminal decisions still do NOT restore the entire observation region

Define the linear support functional `L(O)=alpha-2 beta` (no time penalty, so T remains in the four-coordinate witness but is not used for this separator). In the compressed controller, before multiplying by the (nonnegative) sensor-purchase probability q_a and terminal acceptance probability r_(a,y), the four possible conditional acceptance coefficients `P(A=a,Y=y)-2Q(A=a,Y=y)` are exactly

```
(a,y)=(0,0):  (-3 p1 - 10)/32
(a,y)=(0,1):  ( 7 p1 - 10)/32
(a,y)=(1,0):  ( 7 p0 - 10)/32
(a,y)=(1,1):  (-3 p0 - 10)/32.
```

All four coefficients are strictly negative for all `p0,p1 in [0,1]`. Hence for **every real compressed behavioral policy**, not merely rational or deterministic policies,

`L(O_compressed)= sum_(a,y) q_a r_(a,y) [P(A=a,Y=y)-2Q(A=a,Y=y)] <= 0`.

Equality is attained by never buying Y (q0=q1=0), so the exact compressed support value is `0`. A retained ex-ante shared seed also cannot break this inequality: every conditional pure compressed policy has L<=0 and a mixture preserves this linear upper bound.

The full-memory controller has a legal pure policy: take the U and V first actions, buy Y after U and V but not after C0/C1; accept exactly when `(W=U,Y=0)` or `(W=V,Y=1)`. Its exact outcome is

`O_full=(9/16,1/16,7/4,5/4)` and `L(O_full)=7/16`.

This is the **maximum** over full-memory behavioral policies: at each W a terminal atom is accepted only if its P mass minus twice its Q mass is positive. U contributes exactly `7/32` from Y=0; V contributes `7/32` from Y=1; C0 and C1 contribute zero, and no first/sensor choice can improve the sum because L has no T penalty. Therefore

`sup_(O in S_compressed) L(O)=0`, `sup_(O in S_full) L(O)=7/16`, `gap=7/16`.

So **the entire original four-dimensional observation region differs**, and the displayed full-memory vector lies outside even the convex hull of compressed outcomes. This is stronger than a local action-distribution mismatch, and it remains true after allowing terminal accept/reject decisions and arbitrary shared randomization independent of W. It is a theorem under the exact protocol in §1, not a claim about models allowing premature accept or extra history-dependent signals.

## 4. Theorem C — one external-history bit is necessary and sufficient for exact region preservation in this model

Let the controller retain its own first action A and one binary externally observed memory bit

`D=TEST` for `W in {U,V}`, and `D=CAL` for `W in {C0,C1}`.

On any non-stopped history reaching the second stage, `(A,D)` uniquely reconstructs the original W:

`(1,TEST)<->U`, `(0,TEST)<->V`, `(0,CAL)<->C0`, `(1,CAL)<->C1`.

Thus the one-bit augmented controller can implement every W-specific buy and W/Y-specific terminal rule **history by history**. Conversely, a full-history policy can ignore W beyond `(A,D)` because all reachable W possibilities are uniquely reconstructed. Identical chance weights, observable branches, action counts and acceptance events are preserved under both sources. Consequently:

`S_(A,D) = S_full` as the **raw four-dimensional sets** for arbitrary real fresh behavioral policies (indeed, exact pathwise distributions agree).

Zero added bits leaves only A and fails by Theorem B, while one binary bit works. Therefore **exactly one additional binary memory bit is minimum for this fixed four-history protocol**, holding the own-action memory A and the stage/action rules fixed. This is not an information-theoretic minimum for arbitrary other protocols or an X6 coordinate.

## 5. Rational points recover rational fresh behavioral policies after full memory restoration

For this finite model, every deterministic full-memory policy has a rational four-vector because all source atoms and observation counts are rational. Every real behavioral policy yields an ex-ante distribution over finitely many deterministic complete plans (product of its behavior probabilities); hence every achievable vector belongs to the rational polytope spanned by the deterministic vectors.

Conversely, perfect recall of W, A and Y permits any mixture of deterministic plans to be converted into an outcome-equivalent fresh behavioral policy: condition the mixture's plan weights at each reached information set on the controller's own remembered previous actions. This conditioning is independent of whether P or Q generated the exogenous chance observations. For a **rational** point O in this rational polytope, the finite linear system `sum_i lambda_i V_i=O`, `sum_i lambda_i=1`, `lambda_i>=0` has a **rational** feasible basic solution lambda. Conditionalization of rational lambda produces rational behavioral action probabilities (zero-denominator unreached sets may use any rational rule).

It follows that every rational O achievable in `S_full=S_(A,D)` is achievable by rational fresh behavioral decisions in that model. This is a finite rational-polytope/Kuhn perfect-recall consequence and **not** an assertion of general originality or a result for imperfect-recall `S_A`. Theorem B also shows that merely adding a shared seed without D does not preserve `S_full`.

## 6. Narrow deletion-of-calibration corollary

Delete C0/C1 and renormalize each source's masses over U,V. Keep the original restricted first-action menus: U may continue **only** with A=1, V may continue **only** with A=0, or stop. Every continuation's own action A then identifies W. The unaugmented retained-A controller is effectively perfect recall on all non-stopped histories; it has the same full four-observable region as W-memory, and every rational point in that region has a rational behavioral implementation by §5.

This corollary does **not** cover a uniform menu allowing both A=0 and A=1 after both U and V: that different interface can reintroduce merged histories even without C0/C1. It therefore narrows EC49M's calibration-removal problem without claiming its fully general resolution.

## 7. Exact verification, literature scope and next obligation

`VERIFY.py` is the actual executed standard-library `fractions.Fraction` checker. It verifies all 8 positive latent leaves under each source, constructs the rational terminal-rescue policy, checks the four compressed coefficient signs, **exhaustively evaluates all 256 compressed deterministic policies** and **all 16,384 full-history deterministic policies**, and checks the exact support maxima plus the explicit one-bit decoding. `EXACT_REPORT.json` is captured stdout from the execution. The continuum statements are covered by the algebraic sign and per-W optimality proofs, not inferred from finite grids. No formal Lean proof or independent Driver review is claimed.

External context, not originality claims: Kuhn's perfect-recall equivalence (see MIT OCW 2021 lecture source in `SOURCES.md`) supplies the standard policy-conversion principle. Anderson–Montúfar (ICML 2026) characterize semi-algebraic feasible sets in a different infinite-horizon, memoryless POMDP setting. That background does not establish the concrete rational sign separator here; the exact finite model is analyzed above.

**Next independent unit EC49N:** test no mandatory calibration with a *uniform* first-action menu and genuinely merged post-action histories; allow terminal action choices both after and before sensor purchase in carefully separated models. Either exhibit an irrational-only rational four-target with complete algebraic exclusion, or prove a rational-realizability theorem with its exact action/recall hypotheses. Extend the minimal-memory result to multi-stage action-dependent observation kernels and resource costs; any signed BRC / native X6 transfer remains a separately typed proof obligation.
