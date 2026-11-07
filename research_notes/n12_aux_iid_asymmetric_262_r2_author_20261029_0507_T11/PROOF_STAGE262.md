# Stage262 — next exact all-real Bellman face across R261 D5—D6

Date: 2026-10-29. Classification: **AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED**. This is an external finite ternary IID auxiliary sequential-test theorem, **not** a native Heartbeat World/X6/three-dimensional-slice theorem, a Source Result, or independent Driver acceptance.

## Immutable inputs and control boundary

Scientific predecessor: Enterprise Math Draft PR #1571, Stage261 commit `ce24c0b4779d9ad84ce546271c5c0637991e6c3c`, `PROOF_STAGE261.md` and `NEXT_TASK_PACKET_262.md`. On this run the verified GLOBAL_KNOWLEDGE_V1 canonical read was `main@253970b693bd99d2ad6039a052cef097f74662ed` (same snapshot for global bootstrap, manual, P000 original/startup projection and ACTIVE worldview); original P000 Git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` matched startup projection. Enterprise Math control read `main@b5b9e5a248d49d780acad67d6087b51693112d15`, including AGENTS and portable research protocol. Current native service reported `research_authority_granted=false`, `CODE_REVIEW_REQUIRED`; exact owner inventory returned `CONTROL_QUOTA`. This researcher did **not** obtain a native CLAIM or Source review authorization. Scope is local author-level exact reasoning plus authorized PR publication, without modification of P000/ACTIVE/worldview or native shared task state.

Fix horizon `N=12`, `P=(1/8,1/24,5/6)`, `Q=(1/12,1/12,5/6)` for observations in `{0,1,2}`. A policy may at any complete ordered history stop and decide P, stop and decide Q, or continue unless already at depth 12. Randomized decisions and stopping are permitted. Define `eP=Pr_P(decide Q)`, `eQ=Pr_Q(decide P)`, `tP=E_P[T]`, `tQ=E_Q[T]` and `V12(a,b)=min max(tP,tQ)` over all policies with `eP<=a`, `eQ<=b` (infinite if infeasible). This notation uses **external** Euclidean parameter-plane geometry for a two-error observer, not a native two-dimensional Enterprise plane.

## Main theorem and target

Use the exact rational Bellman multiplier certificate

```
lambdaP = 11983936/141145
lambdaQ =  7680708/141145
thetaP = 0, thetaQ = 1
H = 22366403903/411578820
```

There are precisely four distinct equality-fiber deterministic policy vectors; label them by the two tie actions at count states `(0,0,5)` and `(0,1,6)`, where bit `0` chooses the earlier action (`decide P` / `decide Q` respectively) and bit `1` chooses `continue`. In order `(eP,eQ,tP,tQ)`, the vertices are:

```
D5  mask 00:
(1166286571/11609505792,3274031045/4353564672,
 2092263019/483729408,1774015963/362797056)
F5  mask 01:
(4312568159/46438023168,13246202305/17414258688,
 8556473951/1934917632,7350985727/1451188224)
F6  mask 11:
(182851367/1719926784,471373465/644972544,
 348833063/71663616,298085351/53747712)
D6  mask 10:
(1786693553/15479341056,4182329935/5804752896,
 3064528817/644972544,2580799409/483729408)
```

Let `R262=conv{D5,F5,F6,D6}` denote the **error-plane** convex hull of their first two observer entries. This is a strictly convex rational quadrilateral, oriented counterclockwise in that order, with exact Euclidean parameter-area

```
area(R262) = 75810302734375 / 623984373770747904.
```

**All-real optimal-face theorem.** For every real `a,b∈[0,1]`, including all boundary and irrational pairs,

```
V12(a,b) = H − lambdaP*a − lambdaQ*b  iff  (a,b) ∈ R262.
```

The two polygons `R261` and `R262` intersect *exactly* in their common full `D5—D6` error-plane segment; their interiors are disjoint. Their four-observer values also agree at these two shared endpoints, and hence on the entire shared convex-mixture edge. This closes the Stage261 unresolved D5—D6 crossing without silently upgrading the auxiliary model to original six-dimensional dynamics.

At the explicitly frozen Stage262 cap pair

```
a262 = 6259962086479/58047528960000
b262 = 25643113985/34828517376
```

we obtain the **exact global optimum**

```
V12(a262,b262) = 1311158074687830583/256034952345600000
                ≈ 5.121012044160318.
```

It is achieved by independently sampling at the root the three deterministic policies `D5,F5,D6` with respective positive rational weights

```
wD5 = 6390764742101/13783691406250
wF5 =  196764774912/6891845703125
wD6 =   279975884573/551347656250
```

which add to one. The resulting four observer values are exactly

```
eP = a262
eQ = b262
tP = 1551378313594273399/341379936460800000
tQ = 1311158074687830583/256034952345600000
tQ−tP = 4183622218063/7255941120000 > 0.
```

Thus the maximum stopping time equals `tQ`, and both error caps are attained with equality. The exact dual lower bound matches the primal policy, establishing global optimality for *all* complete ordered-history randomized policies, not merely a selected class of count-based policies.

## Proof of universal dual and finite equality fiber

At count state `s=(i,j,k)` the likelihood ratio for **each individual ordered history with those counts** is `L(s)=Q(h)/P(h)=(2/3)^i 2^j`, strictly positive. Normalize Bellman future cost by positive `P(h)`. The three legal action costs are

```
B_s(P) = lambdaQ * L(s)
B_s(Q) = lambdaP
B_s(C) = L(s) + Σ_{z=0}^2 P[z] H(s+unit_z),  if i+j+k<12,
H(s) = min of legal costs, with H defined backward from depth 12.
```

Exact rational backward induction over all `binom(15,3)=455` count states gives `H(0,0,0)=22366403903/411578820`. The executable certificate enumerates every one of the 1,274 legal action costs and finds 817 strictly positive non-minimizer gaps. **Only two distinct two-way ties exist:** `(0,0,5)` between stop-P and continue, and `(0,1,6)` between stop-Q and continue. All other legal states have a unique minimizer. Because this recursion is the Bellman minimum at *every* possible count and all source probabilities are positive, induction on the remaining horizon yields for any randomized full ordered-history policy

```
tQ + lambdaP*eP + lambdaQ*eQ >= H.
```

Consequently `V12(a,b) >= H − lambdaP*a − lambdaQ*b` for all feasible pairs, because both error multipliers are strictly positive.

**Why count aggregation is sufficient here, but not a general erasure of provenance.** For each fixed count `s`, aggregate all visiting full-history P masses and P masses choosing each action. Define count-state conditional action probabilities as their ratios (arbitrary when there is no visiting mass). Since every history at `s` has *the same* positive `Q/P` ratio `L(s)` and all subsequent observations have IID kernels, forward induction proves equality of aggregated P and Q action masses, terminal errors, and continuation counts for **both** models. Thus exactly `(eP,eQ,tP,tQ)` is preserved by this quotient. Conversely any count policy defines a complete-history policy. This does **not** claim preservation of other observers, hidden joints, native path geometry, or arbitrary future non-IID transformations. The certificate also independently traverses complete ordered histories carrying distinct exact P and Q masses, rather than relying only on count recurrences.

A randomized count policy is a convex mixture of deterministic count policies: independently choose the action at each count state before the experiment. No state repeats along a strictly increasing count path, so finite product expansion preserves every action-path mass and the four observers. If an optimizing policy attains the Bellman lower bound, all positive-mass visited actions must have zero Bellman gap. Only the two tied count states may then choose between two actions; every other state must choose its unique minimizing action on any reached path. Consequently the **entire** four-observer equality fiber is exactly the convex hull of the four listed deterministic policies (unreachable-state choices have no effect). The exact certificate confirms all four satisfy equality `tQ + lambdaP*eP + lambdaQ*eQ = H`, all have `tQ>tP`, and all four are distinct.

**Sufficiency of R262 for all real error caps.** Every point of the quadrilateral has a convex representation by its four deterministic policies, using real mixing probabilities when necessary. Sampling that mixture at the root yields `eP=a`, `eQ=b`, and `tQ>tP`; its `tQ` meets the universal lower bound. Thus equality holds throughout R262, irrational points included.

**Necessity, including infeasible boundary cases.** The finite full-history randomized-policy space is a finite product of compact action simplexes, with four observations continuous in the action kernels. Therefore every feasible minimization attains its infimum. If `V12(a,b)` equals the stated finite affine lower bound, the optimizer must satisfy `eP=a`, `eQ=b` (strictly positive multipliers) and have zero Bellman slack, hence its error pair lies in the equality-fiber quadrilateral. An infeasible pair has value `+infinity` and cannot equal that finite affine expression. This proves the iff for all real caps in the declared unit square.

## Convexity, Stage261 adjacency, fidelity

In the counterclockwise order `D5,F5,F6,D6`, the four consecutive orientation determinants are

```
34459228515625/311992186885373952
6891845703125/51998697814228992
6891845703125/51998697814228992
34459228515625/311992186885373952
```

all strictly positive. Rational shoelace arithmetic gives the stated exact area. Along the directed edge `D5→D6`, the two remaining new vertices `F5,F6` are strictly on the negative side; the three nonshared Stage261 vertices `E12,C12,C5`, with their exact error coordinates taken from immutable Stage261, are strictly on the positive side. All four coordinates of `D5,D6` coincide with Stage261's immutable source vectors; therefore the convex regions meet exactly in that closed segment and preserve the full declared observer values on their common edge. The Stage262 chosen cap has signed determinant `-878615/278628139008`, strictly outside R261 but inside R262.

BRC-compatible provenance is used concretely as separate positive rational P/Q branch masses, preservation of ordered-branch multiplicity, and a formally scoped observer quotient. No assertion is made that these are native BRC–Shor operations, six-axis rotations, P000 dynamics, or a proof of the discrete-world physical hypothesis.

## Reproducible evidence and Stage263

`STAGE262_EXACT_FACE.py` is a standalone **executed** standard-library Python Fraction certificate. It asserts all 455 Bellman states, 1,274 actions, 817 strict gaps, two tie states, four distinct exact observer vectors, convexity, hull area, R261 adjacency, target mixture/dual equality, exact next-boundary crossing, and an **independent full ordered-history DFS for every deterministic equality policy**. The independent DFS visits 2,131 history nodes and 1,422 terminal branches in total; each policy terminates with P/Q mass exactly one and agrees *exactly* with the count-DAG calculation. Actual stdout is preserved verbatim in `STAGE262_EXECUTED_STDOUT.txt`, ending with `STAGE262_EXACT_ALL_REAL_FACE_PASS`. Executed source SHA256: `e64b5384a08493e23cf8e81120953062398a75844ba456af3a235741f69c5d81`. All-real inference additionally uses the human proof above; testing four policies alone is not a theorem about arbitrary real caps absent the quotient/compactness/duality arguments.

Exploratory SciPy/HiGHS floating LP suggested the exact dual and also indicated that the next Stage263 candidate is feasible, but floating LP is explicitly **not** the proof, does not certify exact Stage263 feasibility, and is not required to reproduce Stage262.

Next frontier: cross the other edge `F5—F6` at

```
a263 = 1443791791151/14511882240000
b263 = 6493321465/8707129344
oriented_area(F5,F6,(a263,b263)) = -415295/139314069504.
```

Stage263 must first construct an exact feasible full-history policy or exact infeasibility certificate for this outside point, then seek a new rational Bellman dual, exact primal witness, all-real equality-face characterization, and BRC-labelled source-path audit. It must preserve all Stage262 certified units, P000 native-transfer boundary, and Source/Driver role boundaries; see `NEXT_TASK_PACKET_263.md`.
