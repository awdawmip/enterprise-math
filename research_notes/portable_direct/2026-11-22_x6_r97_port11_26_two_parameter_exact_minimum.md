# X6 R97 — Exact two-parameter optimum for every Port budget 11–26

Date: 2026-11-22 (Asia/Shanghai).
Status: SYMBOLIC_AUTHOR_PROOF / EXACT_FRACTION_AUTHOR_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.
Scope: conditional **positive-count four-channel BRC star-moment histogram observer**, with one unknown common additive offset. This is **not** the native X6 Cell/Link/triadic-force/heartbeat observer or evidence of a native physical residual.

## Provenance and frozen scope

Continues X6 R96 (the exact T=11 cross-section), [2026-11-22_x6_r96_T11_complete_port_tie_atlas.md](2026-11-22_x6_r96_T11_complete_port_tie_atlas.md), observed on current main, blob \`2a571766243b041e1e0ec016584e973b3e2d53ff\`. Reuses the R96 scientific pin \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\`; current P000 V5, ACTIVE worldview, joint-observer preservation and ordinary portable method rules are read as separate behavioral/ontological sources. No P000 mutation, no task input repin and no claimed native observer descent.

This work concerns only the exact algebraic observer defined below. Positive-count moments are not signed or phase-resolved amplitudes. No ordinary matrix exponential, trigonometry, classical physical reference run or native heartbeat evolution was used.

## Model

Unoriented nonzero differences \`a=(x,y,z)∈Z³\` are identified under \`a~−a\`, with

\[
q(a)=\max\Bigl(\sum_i\max(a_i,0),\ \sum_i\max(-a_i,0)\Bigr),
\]
\[
u=x+3y+6z,\qquad v=3x+12y+30z,\qquad h=7x+39y+126z.
\]

For \`w=(1,1,S,T)\`, \`S,T≥1\` real, define the conditional BRC histogram objective

\[
F(a;S,T)=\max\left\{
\frac{|u|}{2},
\frac{|v|}{S+1},
\frac{|h|}{T+1},
\frac{|v-u|}{S+1},
\frac{|h-u|}{T+1},
\frac{|h-v|}{S+T}
\right\},
\qquad
\eta^*(p;S,T)=\min_{\substack{0\ne a\in\mathbb Z^3\\q(a)\le p}}F(a;S,T).
\]

## Theorem — complete optimal *value* for 11–26 Port

For **every integer \`11≤p≤26\` and all real \`S,T≥1\`**, independently of the Port budget within this band,

\[
\boxed{\eta^*(p;S,T)=
\min\left\{
\frac12,\ \frac{12}{T+1},\
\max\left(\frac3{S+1},\frac6{T+1}\right)
\right\}.}
\]

Three explicit feasible vectors attain the three terms, respectively:

| Direction | (u,v,h) | q | Exact F |
|---|---|---:|---|
| \`s=(10,-5,1)\` | (1,0,1) | 11 | \`1/2\` |
| \`d=(6,-4,1)\` | (0,0,12) | 7 | \`12/(T+1)\` |
| \`b=(9,-5,1)\` | (0,-3,-6) | 10 | \`max(3/(S+1),6/(T+1))\` |

This theorem classifies the optimal *value*, **not** the full tie set. Other vectors may tie at walls, and the Port budget can alter tie multiplicities even though the optimal value stays constant.

### Proof over the complete integer domain

The moment map is invertible over \(\mathbb Q\), with the exact inverse already established in R96:

\[
(x,y,z)=
\left(\frac{h+19u}{2}-4v,\frac{-h-14u+7v}{3},
\frac{h+11u}{12}-\frac v2\right).
\]

Integer differences satisfy \(v\in3\mathbb Z\) and \(h-u\in6\mathbb Z\).

* If \(u\ne0\), the first BRC gap yields \(F(a)\ge |u|/2\ge1/2\), attained by \(s\).
* If \(u=0=v\), then the inverse map forces \(h=12k\), and \(a=k(6,-4,1)\). For \(a\ne0\), \(|h|\ge12\), so \(F(a)\ge12/(T+1)\), attained by \(d\).
* If \(u=0,\ v\ne0\), we prove that for \(q(a)\le26\), neither \(h=0\) nor \(h=v\) is possible:
  - If \(h=0\), the inverse map gives \(a=(-4v,7v/3,-v/2)\). Integrality forces \(v=6k\), hence \(a=k(-24,14,-3)\) and \(q(a)=27|k|\ge27\).
  - If \(h=v\), the inverse map gives \(a=(-7v/2,2v,-5v/12)\). Integrality forces \(v=12k\), hence \(a=k(-42,24,-5)\) and \(q(a)=47|k|\ge47\).
  Consequently \(v\ne0,\ h\ne0,\ h-v\ne0\). From \(v\in3\mathbb Z,\ h\in6\mathbb Z\), it follows that
  \[
  |v|\ge3,\qquad |h|\ge6,\qquad |h-v|\ge3.
  \]
  The exact BRC gaps imply
  \[
  F(a)\ge\max\left(\frac3{S+1},\frac6{T+1}\right),
  \]
  attained by \(b\) because \(S+T\ge S+1\).

The three exhaustive cases establish the stated minimum. In particular, the Port cutoff 26 is **sharp for this argument**: at \(p=27\) the excluded line \(a=(-24,14,-3)\) becomes available and can improve the optimum for sufficiently large \(S\). This proves the theorem. ∎

## Corollary — explicit T>11 chambers for 11–26 Port

For \(11<T\le23\):
- \(S\le5\): \(\eta^*=1/2\).
- \(S>5\): \(\eta^*=\max(3/(S+1),6/(T+1))<1/2\).

For \(T>23\):
- \(S<(T-3)/4\): \(\eta^*=12/(T+1)\), with \(d\) attaining it;
- \(S>(T-3)/4\): \(\eta^*=\max(3/(S+1),6/(T+1))\), with \(b\) attaining it;
- at \(S=(T-3)/4\), both \(b\) and \(d\) attain the minimum.

Within the \(b\)-dominated chamber, its controlling gap switches at \(S=(T-1)/2\). These are **value** walls; full tie classification is a separate problem.

## Reproducibility and limitations

The author independently enumerated **31,031** unoriented nonzero integer differences with \(q\le26\), checked the \`u=0\` divisibility/dominance classification on all **160** such directions, and checked the exact minimum for **24** rational \((S,T)\) pairs and **8** Port budgets (192 cases, **2,411,712** in-budget exact rational comparisons). All assertions passed in Python \`fractions.Fraction\`. Companion verification source: \`x6_r97_port_11_26_exact_verify.py\`; JSON certificate: \`x6_r97_port_11_26_results.json\`. The infinite real-parameter theorem rests on the symbolic proof above, not on sampling. No independent audit or formal proof checker is claimed.

Native limitations: no preservation certificate yet connects this lossy four-channel count observer to named native six-dimensional Cell identities, composite paths, signed/triadic-force events, branch provenance or ordered heartbeat time. No physical-law claim, Source Result, Review or formal Task completion follows from this theorem. The new portable file does not assert current RS-X6 ownership or a CLAIM.

## Next precise question

Extend the classification from the Port band \(11\ldots26\) to \(p\ge27\), where the new \(u=h=0\) direction is feasible. Determine the earliest additional co-optimal rays as \(T>11\) and \(S\) vary, and separate pure value walls from tie-multiplicity walls. Preserve the P000 native observer bridge as an independent unsolved task.
