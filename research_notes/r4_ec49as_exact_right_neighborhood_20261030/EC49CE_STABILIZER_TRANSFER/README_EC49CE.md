# EC49CE — Stabilizer-aware integral orbit transfer for signed-X6 BRC

2026-10-31. **Author-side analytic proof + exact integer audit; PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED.** This is static path combinatorics, not a heartbeat physical dynamics claim.

## Exact sources and carrier
GLOBAL_KNOWLEDGE_V1 frozen current-main snapshot `c7fcc26913ced2dbf663c420ee058e3cade936dd`; Enterprise Math main `991bcd37fb61895b06655e1416dec064ace4d7d9`; predecessor [EC49CD](../EC49CD_ORBIT_DP/README_EC49CD.md) at immutable commit `61d002dffb201bc3ea6cd6a9ac840774be774910`. Read P000, ACTIVE worldview, native X6, joint-observer, autonomous and portable research protocols. Native `signed_brc.py` source blob `300a96e3dc24bf6fff73743037a0347a8bc83176`; exact `endpoint_weight` and `endpoint_multiplicity` used for independent totals.

Ordered primitive directions `±E1,...,±E6`; six signed **chart-relative** displacement components, retaining order and multiplicity. Three BRC channels: two positive integer weight instruments `w0+=(2,3,3,2,1,1)` and `w1+=(3,2,3,2,1,1)`, negative weights all 1; plus count. A nine-state automaton tracks occurrences of `A=(+E1,+E2)` and `B=(+E2,+E1)`. Target is zero displacement and 4 labelled Boolean A/B atoms × 3 channels. Allowed continuation is one further signed step with its DFA update; arbitrary future observers are not covered.

Let `K=C2×C2=<s=(E1 E2),t=(E5 E6)>`. On state `x=(z,q)`, the group permutes axis coordinates and corresponding DFA factors. On the vector of three output channels `T_s` exchanges the two instruments and `T_t` is identity. Both the typed step operator and its exact return-cone pruning are equivariant: `f_j(gx)=T_g f_j(x)`.

## Theorem — integral direct orbit-to-orbit transition without source-orbit expansion
For each canonical reachable source `r`, set `H_r=Stab_K(r)`. Partition the twelve step letters into `H_r`-orbits and take exactly one representative `a` per orbit. Let `y=δ(r,a)`, `d=can(y)`, choose `k∈K` with `ky=d`, define `E=Stab_K(r,a)=H_r∩Stab_K(a)` and `H_d=Stab_K(d)`. Because K is abelian, `E≤H_d`. The contribution of the **entire orbit of that one edge** to destination `d`, from vector `v=f_j(r)`, is exactly

```
C_(r,a→d) v = Σ_{[h] in H_d/E} T_(h k) diag(w0(a),w1(a),1) v.
f_(j+1)(d) = Σ_r Σ_{a in representatives(H_r\Sigma), can δ(r,a)=d} C_(r,a→d) f_j(r).
```

Every entry of the compiled `3×3` operator is a nonnegative **integer**; no rational division or average is used. For every nonnegative length and every intermediate layer, the compiled representative values lift exactly to the complete unquotiented positive signed-X6 weighted-DFA path histogram, hence give all twelve terminal observations. At odd length, the zero-displacement outputs vanish.

**Proof.** (1) The action on directed edges is `g·(x,a)=(gx,ga)` with `δ(gx,ga)=gδ(x,a)` and `W_(ga) T_g=T_g W_a`. (2) Every group orbit of directed edges has a source whose state is a canonical representative. Two letters outgoing from that representative generate the same edge orbit iff related by `H_r`; the construction therefore enumerates every edge orbit exactly once. (3) For a chosen edge `(r,a)`, all group elements carrying its target `y` to `d` are exactly `{h k:h∈H_d}`. Two such elements yield the same **edge** iff their quotient lies in its stabilizer `E`, giving precisely the cosets `H_d/E`. Since `E` fixes source, letter and their equivariant weighted contribution, the displayed sum counts each distinct incoming edge once. (4) The initial empty-path vector `(1,1,1)` is stabilizer invariant. Inductively the compiled transfer reproduces every canonical target's complete incoming sum, and equivariant lifting reconstructs all full states. Labelled DFA atoms are retained, not scalar-averaged. QED. For a nonabelian group the target stabilizer denominator is conjugated to `kEk^{-1}`.

**Required stabilizer factor — strict counterexample.** Source `r=((-1,0,0,0,0,0),q=0)` is reachable by `-E1` and has `H_r={1,t}`. Taking `a=-E2`, the canonical destination is `d=((-1,-1,0,0,0,0),q=0)`, with `E={1,t}` but `H_d=K`. Thus `|H_d/E|=2`. The two distinct paths `(-E1,-E2)` and `(-E2,-E1)` land in the same destination orbit; their BRC weights all equal one. Correct count/weight contribution is `(2,2,2)`, while omitting stabilizer multiplicity incorrectly yields `(1,1,1)`. This is not a rounding issue.

## Exact numerical audit and practical boundary

Actual local execution: `VERIFY_EC49CE.py` compares full DP, EC49CD expanding quotient and direct compiled quotient after **lifting the entire state map at every layer**, at n=0,2,4,6,8,10,12,14. It checks all labelled terminal atoms and native `endpoint_weight`/`endpoint_multiplicity`; exact integer arithmetic only. `VERIFY_EC49CE_PORTABLE.py` is a smaller separately executed reproduction of full-vs-compiled all-layer equality. Full author evidence also contains `BENCH_EC49CE.py`, `EXACT_REPORT_EC49CE.json`, and `BENCH_REPORT_EC49CE.json`.

| n | native closed words | native weighted return | full peak states | quotient peak states | EC49CD canonical edge updates | direct compiled target updates |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 96,807,312 | 2,737,312,704 | 5,932 | 2,115 | 36,353 | 30,448 |
| 12 | 8,175,770,064 | 441,121,650,816 | 16,022 | 5,418 | 115,684 | 98,840 |
| 14 | 748,315,668,672 | 76,914,770,549,760 | 38,232 | 12,412 | 316,123 | 274,693 |

At n=14 canonical update events fall ~13.1% relative to EC49CD, but this implementation does **not** outperform in cold-process time or memory. Fresh process observations (full / expanded / compiled): `2.507/3.574/4.413 s`; maximum RSS `122128/104460/194056 KiB` (including Python overhead and compiled cache). The compiled transfer cache reached 25,983 representative keys across the accumulated n≤14 check. Quotient three-channel payload peak is 489,060 bits versus full 1,510,231 bits; neither excludes Python container/matrix/cache overhead, and these are not physical information-theoretic minima.

Each representative compilation visits ≤12 letter-orbit representatives and ≤|K| cosets each, and each transfer has ≤12 distinct destinations. Exact arithmetic complexity has the same coarse `O(n^7)` output-vector bit-memory and `O(n^8)` schoolbook bit-time exponents as EC49CD; there is no asymptotic improvement claim. Caching transfer matrices for all visited six-dimensional (z,q) keys incurs additional `O(n^6 log n)` key bits plus bounded integer coefficients, although Python object overhead makes this expensive at tested n.

## Authority, delivery, next question
Native service 0.6.11: `research_authority_granted=false`, `executor_binding_configured=false`, active-job quota 5/5; a read-only owner inventory call returned `CONTROL_QUOTA`. No Source owner, formal CLAIM/Result, Driver review or admission was inferred. All research is an author-side portable draft. No P000/ACTIVE worldview modifications.

**Next EC49CF:** replace the unlimited compiled transfer cache with per-layer bounded caching or on-the-fly stabilizer transfer; prove a bound covering cache/key memory and benchmark fresh-process RSS/time at n=14,16 while retaining each intermediate labelled observation. Compare double-coset aggregation and canonicalization costs. Scientific success is a sound operator and measured resource change, not an assumed speedup.
