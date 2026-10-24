# R251 — Sharp contrast-Krylov certificate for the R250 positive-BRC packet

Date: 2026-10-24. Classification: **author-side exact theorem within the declared finite positive-BRC affine model**, not native X6 heartbeat validation, formal Result, Driver review or Foundation acceptance.

## Immutable premises / scope

GLOBAL_KNOWLEDGE_V1 main@107912e6223c152ac2f65ee3f2086ca45c413b96; original P000 `projects/enterprise-math/P000_REALITY_FOUNDATION.json` blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE_LOCKED; Source main@bf48e0514f0e7eb54b8d5b36dd142786b6a8bc43. Reused `brc_transport.py` blob be1debe367263931bd5e93fd750be3ed54624fe1 and `brc_control_port.py` blob 44def6b8ac787e798d3cc2c6be16f873f91b9db8 at the exact `Affine.then / EffectHistogram / ControlPacket.then` interface-law level. Predecessor R250: commit d6c0caaec6b26d184b72723eb5ebd6f8d4a2cef3, `research_notes/R250_FINITE_HOLONOMY_BRC_FULL_HISTOGRAM_20261024.md`.

Three nonspatial controls S={0,1,2}, one reusable letter a, unit-positive weighted/count BRC alternatives:
- state 0: (2,R_-1), (2,T_-1);
- state 1: (0,R_-1), (0,T_-1);
- state 2: (1,T_+1), (2,T_-1).

These are six-dimensional formal affine maps `T_k(z)=(z1+k,z2,...,z6)` and `R_k(z)=(-z1+k,-z2,z3,...,z6)`. Observer discards only terminal control; retains the *joint full affine-effect and weight/multiplicity histogram*. Intermediate controls still govern subsequent compositions. Ordered original path IDs are not observed here. Compare starting controls 0 and 1.

## Theorem R251.1 — exact contrast Krylov rank four

Work over K=Q(x), indeterminate x. The R250 faithful anti-chronological Laurent representation Ψ(F)=ρ(F^{-1}) gives

```
A=Ψ(R_-1)=[[0,x^-1],[x,0]]
B=Ψ(T_-1)=diag(x,x^-1)
C=Ψ(T_+1)=diag(x^-1,x)
N=[ 0   0    0    0    x    x^-1 ]
  [ 0   0    0    0    x    x^-1 ]
  [ x  x^-1  0    0    0     0   ]
  [ x  x^-1  0    0    0     0   ]
  [ 0   0   x^-1  0    x     0   ]
  [ 0   0    0    x    0    x^-1 ] .
```

For i=0,1 let α_i=e_(0,i)^T−e_(1,i)^T interpreted as row contrasts, and W_(i,k)=α_i N^k. For i=0 direct exact multiplication gives

```
W_0=( 1, 0, -1, 0, 0, 0 )
W_1=( -x, -x^-1, 0, 0, x, x^-1 )
W_2=( 0, 0, 1, 1, -1, -1 )
W_3=( 2x, 2x^-1, -x^-1, -x, -x, -x^-1 ).
```

For i=1, W_0=(0,1,0,-1,0,0), and W_(1,k)=W_(0,k) for every k≥1. The 4×4 determinant on columns (0,1,2,3) of W_0,...,W_3 equals (x²−1)/x² for i=0 and −(x²−1) for i=1, both nonzero in K. Thus each reachable contrast span has rank at least 4. Direct multiplication also yields for **both** i:

`α_i N^4 + α_i N^2 − (x+x^-1) α_i N = 0.`  (★)

Multiplying (★) on the right by every N^k proves closure, so each contrast span has **exact rank 4**. The contrast-specific annihilator is `λ(λ³+λ−x−x^-1)`. The full N characteristic polynomial is `λ²(λ−x−x^-1)(λ³+λ−x−x^-1)`: the contrast need not reach all six coordinates/modes. **Rank four is a linear contrast dimension, NOT a four-control-state positive-BRC quotient.**

## Theorem R251.2 — exact and sharp distinguishing depth three

For j=0,1 set β_j=Σ_(q=0..2)e_(q,j). Complete joint-effect equality for all future words is equivalent to all α_i N^k β_j=0: faithfulness of the R250 representation distinguishes every affine group effect. From the displayed rows, the (j=0,j=1) signed external comparisons at k=0,1,2 are (0,0), and at k=3 are `(x−x^-1,x^-1−x)≠(0,0)`. Therefore **only depths 0...3 need be checked** to certify *every future depth for this packet/start pair*, and the depth-3 positive-branch witness shows this bound cannot be lowered. R250's general n|H|−1=5 remains valid and is NOT generally improved by the particular rank calculation.

For D_k=(α_i N^k β_0,α_i N^k β_1), (★) gives `D_(k+4)+D_(k+2)=(x+x^-1)D_(k+1)` for all k≥0. D_0,D_1,D_2 are zero and D_3 nonzero; therefore no homogeneous constant-coefficient recurrence of order ≤3 can generate this same observable sequence. Its minimal recurrence order is exactly **4**.

Independent direct positive histogram check at depth 3: starting control 0 has `R_-3:1,R_-1:3,T_-3:1,T_-1:3`; starting control 1 has `R_-3:1,R_-1:2,R_+1:1,T_-3:1,T_-1:2,T_+1:1`. Each consists of eight **positive** BRC paths. Their *external mathematical comparison* is `R_-1+T_-1−R_+1−T_+1`. No signed BRC branch or amplitude cancellation is posited.

Specializations x=±1 collapse different effects and cannot be used to prove joint-effect equality: x is a formal indeterminate. All results are for the observer and operations above, not for arbitrary new alphabet, hidden path-ID probes, native heartbeat dynamics, or physical time.

## Exact checking and status

Exact SymPy Q(x) proof-certificate checker finds for both i the Krylov ranks [1,2,3,4,4], both nonzero minors, recurrence residue identically zero, charpoly and distinguishing depth 3; independent positive integer path DP checked depths 0..10. Separate C++17 positive-branch DP checked depths 0..12, exact counts 2^k, and the four comparison atoms. All PASS. The Python/C++ checks do not replace the displayed algebraic argument. `ControlPacket.from_edges` native Source **was not imported/executed**: `REUSE_APPLIED` at interface law, `REUSE_IDENTIFIED_EXECUTION_UNAVAILABLE` at native execution. No pi/trigonometry/classical dynamics numerical substitute was used.

Prior art: Stefan Kiefer, *Notes on Equivalence and Minimization of Weighted Automata* (2020), https://arxiv.org/abs/2009.01217 . The linear-algebra method is standard; the concrete R250 contrast calculation is R251's author-side contribution.

GitHub actor awdawmip verified. Read-only native task query: CONTROL_QUOTA; own session creation: STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Active Owner, task CLAIM and real researcher activity were NOT established. GitHub research-note persistence is not formal Result admission.

**R252:** In a permitted pinned native Source Python execution call `Affine`, `ControlPacket.from_edges`, `.then`, and `EffectHistogram` with the exact unit-positive six-axis edges, compare histograms depths 0...3; separately check actual P000/heartbeat admissibility and R193 original branch/path-ID observer, recomputing the rank whenever observer/alphabet changes.
