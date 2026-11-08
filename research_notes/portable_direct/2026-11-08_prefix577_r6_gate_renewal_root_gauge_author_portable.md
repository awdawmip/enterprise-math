# PREFIX-577-R6: exact gate renewal and root-independent reward excursions

**2026-11-08** · **AUTHOR_EXACT_INTEGER_AND_RATIONAL_PROVED / UNREVIEWED / NOT_ADMITTED** · `TASK_RESEARCH` author-side portable mathematics. Scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`, unchanged original 48-phase/96-port/576-tagged-action kernel (underlying Git blob `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41`). Roots: `0, ±e1, ±e2, ±e3, ±e4`. No Source CLAIM, canonical checkpoint, native CM run, independent review, or mathematical admission is asserted.

## New exact theorems

**A. Regenerative BRC gate.** The original seven-coordinate per-step reward is `(R1,R2,R3,R4,R5,R6,K)`. The only `K=1` edges originate at ports `7,29,31` (one tagged action each) and **every** such edge ends at the same native port `9=2*TARGET+1`, for all nine roots. Starting from port 9, let `T=inf{n>=1: K_n(step)=1}`. The original port graph is irreducible and bipartite, every port can reach a gated source in at most four steps, and T is a.s. finite with exponential tails. Every return to the gate regenerates an independent, identically distributed complete native excursion.

Let `C[p,q]` be the **integer** count of *nongate* original tagged transitions p→q, `g[p]` the number of gated actions out of p, and `b_j=e9^T C^j g`. The certificate verifies the following **96 coordinate exact integer identity**, not a numerical spectral fit:

```
(C^11 - 20*C^9 - 396*C^7 - 4944*C^5 - 32832*C^3 + 186624*C)*g = 0.
b[0..11] = [0,0,0,20,0,448,0,18608,0,586240,0,21965120].
```

Thus the full first-gate return probability generating function is the exact rational function

```
F(z) = E_9[z^T]
     = z^4 (3-z^2) (z^4+2z^2+5)
       / (972-540z^2-297z^4-103z^6-19z^8+3z^10).
```

It follows for **every** permitted root that `T` is even, its minimum is 4,
`Pr(T=4)=5/324`, `Pr(T=6)=7/729`, `Pr(T=8)=1163/104976`, and

```
E[T]=192; E[T^2]=72928; Var(T)=36064;
E[T^3]=41550000; E[(T-192)^3]=13699248.
gate mean-rate=1/192; gate asymptotic variance-rate
=36064/192^3=1127/221184.
```

The final variance-rate independently recovers the earlier BRC stationary gate cumulant via marked-edge renewal.

**B. Strong nine-root pathwise invariance of gate excursions.** For original tagged edge p→q, native spatial axis k, root r, and signed phase occupancy `s(p,k)`, the frozen original edge definition gives

```
R_k^r(p,a)-R_k^0(p,a) = h_{r,k}(p)-h_{r,k}(q),
h_{r,k}(p) = (abs(s(p,k)-r[k])-abs(s(p,k)))/2.
```

This was directly verified in all `9×576×6=31,104` original root/edge/axis positions and follows algebraically from the original edge formula. A gate excursion starts **and ends at native port 9**, so the telescoping boundary term is exactly zero. Under identical tagged action choices, the complete six-axis **cumulative reward vector of each entire gate excursion is pathwise identical across all nine roots**, even though individual root-dependent edge rewards can differ. The gate count per excursion is exactly one.

**C. Exchange-invariant excursions and joint reward statistics.** The inherited exact nine-root ordered seven-coordinate word theorem (author-side commit `7dc57fac1334e39470685e63ee4f6a3c28668c21`) classifies port 9 as an invariant singleton initial law under the exchange `R5↔R6`. The first gate is defined entirely by the unchanged `K` observer; splitting into the disjoint finite events `{T=n}` extends this word-law symmetry to the *unbounded, integrable, variable-length full gate-excursion reward sequence*. Successive gate excursions are i.i.d. with this symmetry.

The native chain has uniform stationary distribution on 96 ports (six incoming and six outgoing tagged actions per port); each of the six axes has rate `96/576=1/6` and the gate has rate `3/576=1/192` for every frozen root. Exact renewal-reward identities yield `E_9[cycle R_k]=32` for **each** k=1,..,6. An independent exact 96×96 rational absorption-equation solve yields

```
D = cycle(R5-R6); E[D]=0; E[D^2]=32;
lim_{n→∞} Var_9(R5,n-R6,n)/n = 32/192 = 1/6.
```

At first gate length `T=4`, exact path-count multiplicities for `(R5,R6)` are `(0,0):4,(0,1):8,(1,0):8` (20 paths); for `T=6` they are `(0,2):80,(1,1):288,(2,0):80` (448 paths). At `T=8` there are 18,608 successful original-action paths. These finite checks verify the **original full tagged-edge carrier**, not an assumed renewal approximation.

## Evidence and boundaries

Reproducible files, bundled for this run under `PREFIX577_R6_GATE_RENEWAL_ROOT_GAUGE_AUTHOR_PORTABLE_20261108.zip`:

- `verify_gate_renewal_exact.py` (stdlib; 96-coordinate Krylov, gate reachability, parity, exact PGF, 31,104 coboundary checks, finite joint first-hit histograms).
- `GATE_RENEWAL_EXACT_CERTIFICATE.json`, SHA-256 `52dd29e112ed1db33a960b0ac9a2e850f22f0206c9af501e4bf926f05cff5d6c`.
- `verify_gate_reward_moments_sympy.py` (independent SymPy exact rational absorbing-state solve over all nine roots).
- `GATE_RENEWAL_REWARD_MOMENT_CERTIFICATE.json`, SHA-256 `0145f9e0d3b2cf91f3196d119161926f762aabe1fe39fc91f399ba87071827f2`.
- Exact unchanged inherited native-kernel extract and initial-law vertex certificate.
- Full expanded proof and manifest.

Local portable ZIP SHA-256: `09afbec1cfda153c989e2b3d610ae1f9832a4bef51a72d68be52cd7a060a53e6`. The inherited 51-state ordered-word dependency proof was separately reexecuted with exactly the same certificate hash; it is **dependency verification** and remains credited to its prior source.

**Observer scope:** renewal reduction is an exact factor for the native gate and gate-to-gate continuation; the labeled 96-port process, native six-axis spatial rewards, joint relation data and ordered time remain distinct. It is not a replacement for the underlying P000 Heartbeat-world ontology or other observers. The Source D25 original-class CM experiment is still a separate unfinished unit. The authentic UR V2 original four-file 94,687-byte bundle, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`, is a separate provenance recovery target; no forged replacement is proposed.

**Next scientific step:** obtain exact bivariate gate-first-return generating function `F(z,x,y)` for native `(R5,R6)`, retaining the gate-resolved port dependence; compare the five-class BRC marginal and the marked-edge 96-state system by an observer-preserving factorization, verifying `x↔y` invariance. Formal research identity, CLAIM, checkpoint, Result and independent Review must follow actual Source authorization.
