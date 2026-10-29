# Stage267 — exact full-history adjacent Bellman face (external ternary IID, N=12)

2026-10-29. Author: local portable TASK_RESEARCH author `EM-R2-STAGE267-20261029-0938`; not a Source-issued researcher/owner/session. **AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED**. Parent: Stage266 `PROOF_STAGE266.md` and `NEXT_TASK_PACKET_267.md`, existing Enterprise Math Draft PR #1571. The study concerns the declared **external IID auxiliary model**, not a P000-native six-dimensional Cell/Heartbeat dynamical theorem.

## Frozen source / authority reading

GLOBAL_KNOWLEDGE_V1 canonical `awdawmip/chatgpt-global-knowledge main@848e2c3d1ac63d2b3b9736e6b3d8e7473d051cf0` was verified by remote branch read. Enterprise Math control `main@40e57903388e6f6aef21c1bdfb1d5312deadb76e`. Read both global entry files, project TASK_RESEARCH router, project AGENTS, P000 original and startup projection (`770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` matches), ACTIVE Heartbeat/structural residual and joint-observer constraints, `docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md`, and `docs/PORTABLE_RESEARCH_PROTOCOL.md`. Native service `research_authority_granted=false`; task/owner inventory returned `CONTROL_QUOTA`; neither current owner nor native CLAIM/Result is inferred. Older Stage266 input remains the exact immutable scientific parent and is not silently rebased to mutable main.

## Model and exact point theorem

Alphabet `{0,1,2}`, strictly positive IID source laws
`P=(1/8,1/24,5/6)` and `Q=(1/12,1/12,5/6)`, at most 12 observations. A policy observes the *entire ordered history* and may randomize. It may stop and decide `P` or `Q`, or (before depth 12) continue. Define `eP=P(decide Q)`, `eQ=Q(decide P)`, `tP=E_P[number observed]`, `tQ=E_Q[number observed]`. Let `V12(a,b)` be the minimum of `max(tP,tQ)` subject to both errors at most their real caps, and `+infinity` when infeasible.

At the Stage267 exterior target

- `a267=3776724593681/49533891379200`;
- `b267=1799211749497/2321901158400`,

**the exact global optimum** is

`V12(a267,b267)=5161630421173538432550553/897965538177763774955520 ≈ 5.748138655351969`.

Let

`lambdaP=9423522781990912/69612694876029`,
`lambdaQ=1710217803414276/23204231625343`,
`thetaP=0`, `thetaQ=1`, and
`H=616068176019744340149581/8418426920416535390208`.

For **all real** `(a,b)∈[0,1]^2`, the stronger *if and only if* statement holds:

`V12(a,b)=H-lambdaP*a-lambdaQ*b  <=>  (a,b)∈R267`,

where the nondegenerate parallelogram `R267=conv(J5,J6,L6,L5)` has exact positive area

`72513223829196875/276030719456218208796672`.

All vertices below are in `(eP,eQ,tP,tQ)` order; the **first two** components are the cap coordinates:

```
J5=(555154589/7739670528,3425906045/4353564672,
    13459124989/2902376448,330916723/60466176)
J6=(1253006053/15479341056,4425329935/5804752896,
    9918023951/1934917632,2919174409/483729408)
L5=(378878551937/5283615080448,146176716655/185752092672,
    27566628769787/5944066965504,254184258235/46438023168)
L6=(15836509331/195689447424,424845849965/557256278016,
    10156836789929/1981355655168,280280958235/46438023168)
```

The complete J5/J6 four-observer vectors exactly match Stage266. `R267` and `R266=conv(I5,J5,J6,I6)` share their *entire* J5–J6 side and have disjoint interiors; old I5/I6 have positive oriented area relative to `J5→J6`, while L5/L6 have negative area. Thus this is a new genuinely adjacent full-real equality region, not a single-point float extrapolation.

## Global lower bound and complete equality characterization

For count state `s=(i,j,k)` with `i+j+k≤12`, define the *one-ordered-history* likelihoods `p_s=(1/8)^i(1/24)^j(5/6)^k` and `q_s=(1/12)^(i+j)(5/6)^k`. The nonnormalized finite Bellman recurrence is

`B_s = min(lambdaQ*q_s, lambdaP*p_s, q_s+Σ_{t=0}^2 B_{s+e_t})` before depth 12; omit the continue action at depth 12. Stop-P costs the Q-error, stop-Q costs the P-error, and continue costs one Q-observation plus the optimal suffixes. The exact executable certificate checks **455 states**, **1,274 legal action costs**, **817 strictly positive gaps** (smallest `3670356301907/22987917777350752638861312`) and exactly two ties, namely

`(0,0,5): stop P = continue`, `(1,2,0): stop Q = continue`.

All other legal actions have strictly positive gaps against the selected minimum. Backward induction at every ordered prefix gives `lambdaP*eP+lambdaQ*eQ+tQ≥B_(0,0,0)=H`. With positive multipliers, `eP≤a`, `eQ≤b` and `max(tP,tQ)≥tQ`, it follows that every admissible policy obeys `max(tP,tQ)≥H-lambdaP*a-lambdaQ*b`.

Equality forces every *reached* ordered history to take Bellman-minimizing actions (strict positivity at all other actions), and both errors to saturate caps. The only two choice histories are distinct and non-ancestral: `(0,0,5)` is the **unique** five-neutral prefix `(2,2,2,2,2)`; `(1,2,0)` is reached by exactly **one** ordered prefix `(1,0,1)`. The two other permutations of the multiset `(0,1,1)` stop strictly earlier at `(1,0,0)` or `(0,2,0)`. Neither tie state can precede the other since their count coordinates are incomparable. Consequently each has a freely selected continuation probability `r,u∈[0,1]` without any interaction term. Under the full P/Q source-aware four-observer map,

`Obs(r,u)=J5+r*(J6-J5)+u*(L5-J5)`, and exactly
`L6-J6=L5-J5` in all four components.

This identifies the complete Bellman-equality observer family with the nondegenerate parallelogram, **not merely** a subset of count-Markov policies. Complete ordered-history policies offer no further equality degrees of freedom because other decisions are uniquely forced at reached histories. Each vertex and all convex interpolations have `tQ>tP`; therefore for every cap in this region a Bellman-equal feasible policy has objective exactly `tQ`. Conversely an outside cap cannot saturate and attain the Bellman lower bound. The finite collection of ordered histories and compact product of decision simplexes imply attainment whenever feasible, so an infimum not attained cannot create equality outside the region. This establishes the *iff* over **all real caps**.

## Constructive rational primal / strict original Stage266 witness improvement

Mix `J5,J6,L5` with these **strictly positive** exact rational weights, respectively:

```
wJ5=14334589146395604771/29005289531678750000
wJ6=14212741739101945229/29005289531678750000
wL5=9159172923624/580105790633575
```

They sum to one. Their mixture has exactly `(eP,eQ)=(a267,b267)`,
`tP=233550929091376870539472079/47891495369480734664294400`,
`tQ=5161630421173538432550553/897965538177763774955520` and
`tQ-tP=125208080113635537589672243/143674486108442203992883200>0`.

The dual equality `tQ=H-lambdaP*a267-lambdaQ*b267` is exact, so the primal policy proves *global optimality*. It improves the valid Stage266 external target witness upper bound `3336652788737/580475289600` by the strict positive rational amount `980699616828237937/1683685384083307078041600`. The previous witness was feasible, **not optimal**; the new result does not retroactively change Stage266's own theorem.

## Arithmetic and provenance audit

Run `python STAGE267_EXACT_FACE.py` (standard library only). The **actual executed source** deterministically regenerates the Bellman table with `fractions.Fraction`; separately computes all four deterministic corner policies by *integer count-state path multiplicity* and by a *different full ordered-history DFS* that multiplies P/Q source likelihoods along each actual branch. The latter visits **3,808 nodes and 2,540 terminal branches** across the four policies. For **each** policy the P and Q terminal masses are exactly 1 separately; every component of each observer agrees with the independently computed count-flow result. It then checks all convex, area, adjacency, mixture and strict-gap identities. The saved stdout begins `STAGE267_EXACT_ALL_REAL_FACE_PASS`. This is a finite exact proof certificate plus the mathematical Bellman/compactness argument, not float LP or a general physical-world theorem.

BRC reuse classification: `REUSE_APPLIED` for positive rational source-mass propagation, preservation of branch identity and ordered-path multiplicity, and an explicitly observer-safe *IID finite-horizon* sufficient count quotient. Retained: P/Q mass, four observations, complete terminal path enumeration for cross-check, legal future actions and horizon N=12. Erased *only after proof*: noncontributing history labels for the exact four-observer Bellman recurrence. Nothing establishes that this quotient preserves P000-native X6 relations, heartbeat evolution, structural residual or phase.

## Stage268 exact feasible research frontier

Across `R267`'s **other** side L5–L6, define deterministic policy `W` by taking the L5 Bellman-minimizing count-state policy and changing **only** `(3,3,5)` from stop-Q to continue. Exactly **21 ordered histories** reach this count state. Independent full-history DFS verifies the P/Q terminal mass normalizations and its exact tuple

`W=(378877764437/5283615080448,146176760405/185752092672,27566635857287/5944066965504,254184389485/46438023168)`.

The explicitly feasible strictly outside point is the mixture `(49/100)*L5+(49/100)*L6+(1/50)*W` with caps

`a268=134248354729/1761205026816`, `b268=215912422795/278628139008`,

and feasible `tQ=66742910965/11609505792 > tP`. Its orientation relative to L5→L6 is `-456621484375/15335039969789900488704` (old-side J5 has positive orientation), and the Stage267 support slack is the **strictly positive** `32602722110875/179593107635552754991104`. This certifies only feasibility and strict exteriority, **not** the Stage268 optimum. Next: recover a new rational supporting Bellman dual and complete adjacent face or exact obstruction, preserving original path multiplicity and P/Q masses.

## Evidence and boundaries

Files in the same versioned research directory: `PROOF_STAGE267.md`, `STAGE267_EXACT_FACE.py`, `STAGE267_EXECUTED_STDOUT.txt`, `NEXT_TASK_PACKET_268.md`. No credentials, external private observations or new shared permissions. The present scientific result is **AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED**; native task Owner/CLAIM, Source Result, independent Driver admission and correspondence to P000 native X6 remain unestablished. PR publication is persistence, not mathematical independent acceptance.
