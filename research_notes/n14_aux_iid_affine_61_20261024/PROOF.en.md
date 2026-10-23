# N=14 auxiliary iid sequential testing — 61st exact affine segment

**2026-10-24; author-level exact finite-model proof; not independently reviewed.** This is an auxiliary iid model result, not a theorem about native BRC, X6, or Heartbeat dynamics. The previous author's 60th segment and inherited stopping tree are available at [immutable source](https://github.com/awdawmip/enterprise-math/blob/043023a89d275308b65b13c07499e1a2843d5c7f/research_notes/2026-10-24_N14_auxiliary_iid_60th_exact_affine_AUTHOR_UNREVIEWED.md). GLOBAL_KNOWLEDGE_V1 main was pinned at `c99ad291db5bec0b509a17257752504f64483274`; the current P000 projection matches canonical original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`.

## Exact statement

With `P=(1/8,1/24,5/6)`, `Q=(1/12,1/12,5/6)`, and stopping horizon `N=14`, allow every ordered-history-dependent randomized stop/decision strategy. Write `eP=P(decide Q)`, `eQ=Q(decide P)`, `tP=E_P(tau)`, `tQ=E_Q(tau)`, and

`V14(alpha)=inf {max(tP,tQ): eP<=alpha, eQ<=alpha}`.

Inherit the proven-author base endpoint
`alpha60=5171839496325066167/14900301753911083008`,
`V60=12355052125433941189/931268859619442688`, with balanced randomization at `B=(12,0,1)` of `s60=25954556736212699/41779200000000000`.

Set `A61=(7,5,0)`, `K61=18824330664/2180893`,
`lambdaQ=K61`,
`lambdaP=72+(8/9)K61=16889762664/2180893`, and
`Gamma61=lambdaP+lambdaQ=35714093328/2180893`.
Let

`eta61=381656275/11497146415054848`.

**Theorem.** For every real `delta in [0,eta61]`,

`V14(alpha60+delta)=V60-Gamma61*delta.`

The right endpoint is exactly

`alpha61=5171839990951598567/14900301753911083008`,

`V14(alpha61)=12354545878161016789/931268859619442688`.

The displayed supporting line cannot remain equal to `V14` for any `alpha>alpha61`. This is a right-edge sharpness result for the line, not termination of the value function.

## 1. Exact Bellman global lower bound

For a count state `(n,a,b)`, the iid likelihood ratio is `L=Q(h)/P(h)=2^(a+b)/3^a`. In units of P, recursively define

`D(n,a,b)=min {lambdaQ*L, lambdaP, 1+sum_i P_i D(child_i)}`

with the third option omitted at `n=14`. Since the recursion minimizes after every possible observed prefix, including arbitrary full-history behavior, `D(0,0,0)` is a dual lower bound for the full policy class. For any admissible strategy,

`D(0,0,0) <= tP+lambdaP*eP+lambdaQ*eQ <= max(tP,tQ)+Gamma61*alpha`.

Exact Fraction dynamic programming visits all **680** count states and checks all **1240** nonselected actions against the inherited deterministic stop tree, now fixing old `A60=(11,6,5)` to immediate Q. There are **1238 strict positive gaps**, zero negative gaps, and precisely two action ties:

`A61=(7,5,0): continue vs immediately decide P`;
`B=(12,0,1): continue vs immediately decide Q`.

The smallest positive gap is `201720865/4239655992`. The exact dual root is

`D(0,0,0)=85082113601245326370789183/14933806890161950162944 = V60+Gamma61*alpha60`.

Thus the claimed affine formula holds as a **universal lower bound** throughout the real interval.

## 2. Exact first arrival and conditional risks

The `A61` count state has `C(7,5)=21` nominal ordered words, and **all 21 are genuine first arrivals** under the inherited stop tree. Because each surviving ordered word has the same P/Q likelihood,

`pA=175/393216`, `qA=175/2985984`.

The balancing state `B` has 12 genuine first arrivals:

`pB=48828125/725594112`, `qB=48828125/362797056`.

The conditional risk quadruple `(eP,eQ,tP,tQ)` under continuing is

`cA=(2636705/4586471424, 3961603/3981312, 224489029/191102976, 4141703/2985984)`,

`cB=(63/64,1/144,9/8,13/12)`.

The first-arrival cylinders at `A61` and `B` are disjoint: the number `a` of symbol-0 observations cannot decrease from 5 to 0, and `B` is later in time. Importantly, `A61` is earlier than several deterministic later stops. In particular, of the 5164 first-arrival histories at prior `(12,7,2)`, **126 pass through A61**. Those paths are included in the *conditional continuation risks* above, not counted as independent contributions after early stopping at A61.

## 3. Balancing construction and primal attainment

Immediately decide P at `A61` with probability `u in [0,1]`; otherwise continue. At B, immediately decide Q with probability `s`. Relative to the baseline `u=0,s=s60`, define the strictly positive rational coefficients

`X=pA*cA.eP=461423375/1803473947459584`,
`Y=qA*(1-cA.eQ)=3449075/11888133931008`,

`E=pB*(1-cB.eP)=48828125/46438023168`,
`H=qB*cB.eQ=48828125/52242776064`.

Disjointness yields the **exact affine**, not first-order approximate, identities

`eP-alpha60=-X*u+E*(s-s60)`,
`eQ-alpha60=+Y*u-H*(s-s60)`.

Set

`h61=(X+Y)/(E+H)=9570903237/34816000000000`,
`s(u)=s60+h61*u`,

so both errors agree and

`eP(u)=eQ(u)=alpha60+eta61*u`,
`eta61=E*h61-X=Y-H*h61=381656275/11497146415054848>0`.

The upper endpoint probability is

`s(1)=25966041820097099/41779200000000000`,

which lies strictly between zero and one; the entire interval is admissible. Every selected randomized action minimizes the Bellman dual, so complementary slackness gives

`tP(u)=V60-Gamma61*eta61*u`.

Independent exact backward risk recursion verifies `tP>=tQ` at both endpoints, with endpoint gaps

`tP(0)-tQ(0)=657020365661213713/1241691812825923584`,

`tP(1)-tQ(1)=218832025422100171/413897270941974528`.

All risks are affine in `(u,s)`, because the two randomized cylinders never meet; the four-corner mixed differences vanish. Therefore `tP>=tQ` for every real `u in [0,1]`, proving the primal upper bound and equality for every `delta=eta61*u` in the theorem.

## 4. Sharpness of the right endpoint

The finite-horizon randomized-policy occupancy set is compact and polyhedral. Suppose the same supporting line attained `V14(alpha)` at `alpha>alpha61`. Because `lambdaP,lambdaQ>0`, equality in the dual chain forces both error constraints to bind and forces every reached action to have zero Bellman gap. The exhaustive action-gap certificate permits deviations only at `A61` and `B`. Even history-dependent randomization can be aggregated to effective probabilities `u,s in [0,1]`: all surviving prefixes of the same count state have identical P/Q likelihood factors and future conditional risks under the fixed downstream actions. Equal errors force `s=s60+h61*u`, hence `alpha=alpha60+eta61*u<=alpha61`, a contradiction. The right endpoint is sharp for this supporting line.

## 5. Reproducibility and limitations

Run standard-library Python 3 scripts from the adjacent directory:

```bash
python verify_n14_61.py
python verify_n14_61_crosscheck.py
```

Both programs actually passed local exact rational computation. The first checks all 680 Bellman states, 1240 action comparisons, first arrivals, conditional risks, and seven balancing parameters; the second independently enumerates ordered words (including `(12,7,2)` descendant history), minimizes the Bellman options, checks four-corner risk identities and seven parameters. They share inherited stop sets and are **two author-side checks**, not independent Driver admission. No native BRC arithmetic/physics transfer, Lean certificate, or external empirical validation is asserted.

The native control dispatch returned `CONTROL_QUOTA` this run: current owner and formal CLAIM remain **unknown/unobtained**. This publication is a source-level author research artifact, not a frozen Task Result.

After changing `A61` to immediate P, the next unproved dual candidate is `K62=1850688/229` at `A62=(10,4,0)`, continue versus immediately P. The next unit must compute genuine first arrivals, descendant-path effects, balancing, an entire real interval and right-edge sharpness under the updated stopping tree.
