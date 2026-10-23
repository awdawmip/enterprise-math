# N=14 auxiliary iid sequential test: exact 49th affine interval (author-level, unreviewed)

**Date:** 2026-10-23. **Scope:** finite auxiliary iid test only; no native BRC/X6/Heartbeat correspondence, formal Lean proof, native task CLAIM/Result, or independent Research Driver review. Inputs: `awdawmip/chatgpt-global-knowledge@7a56e3a5a31c6af97f47a09befb54ae4443c9b41` and `awdawmip/enterprise-math@a57e28e541c36c73cbe37cd553caaacfaa7f0185`. Reuses 48th predecessor proof, standalone checker and certificate at `research_notes/2026-10-23_N14_auxiliary_iid_48th_exact_affine_*`.

## Model and theorem

Observations are iid under `P=(3,1,20)/24` or `Q=(2,2,20)/24`. A randomized history-dependent decision policy stops by `N=14`. Define `eP=P(decide Q)`, `eQ=Q(decide P)`, sampling expectations `tP,tQ`, and `V14(alpha)=min max(tP,tQ)` over policies with both errors <= alpha. Exact state `(n,a,b)` has a,b counts of symbols 0,1 and likelihood `Q/P=2^(a+b)/3^a`.

The inherited 48th endpoint is `alpha48=5171824538157082397/14900301753911083008`, `V48=12379139146742512069/931268859619442688`, with Q-stop probability `s48=8824703195037923/13926400000000000` at B=(12,0,1).

**Theorem.** For **every real** `0<=delta<=eta49=241752875/12934289716936704`,

`V14(alpha48+delta)=V48-(107338212/2807)*delta`.

Thus `alpha49=5171824816656394397/14900301753911083008` and `V49=12378473542489900069/931268859619442688`.

## Global exact Bellman lower bound

Let K=56719116/2807, `lambdaQ=K`, `lambdaP=72+8K/9=50619096/2807`, `Gamma=lambdaP+lambdaQ=107338212/2807`. Under reference P define

```
D(n,a,b)=min(lambdaQ*2^(a+b)/3^a,
             lambdaP,
             1+sum_i P_i D(child_i))
```

with continuation omitted at n=14. The three actions are immediately decide P, immediately decide Q, and sample again. Exact rational dynamic recursion checks **680** states, **1240** nonselected action comparisons, of which **1238** are strictly positive and exactly **two** have zero slack: A=(7,1,3) continue/decide-Q, and B=(12,0,1) continue/decide-Q. Exact root:

`Droot=8171917214718610284304369/615075691518064852992=V48+Gamma*alpha48`.

For every policy `max(tP,tQ)>=tP>=Droot-lambdaP*eP-lambdaQ*eQ>=V48+Gamma*(alpha48-alpha)`. Thus the line is a global lower bound even against fully ordered-history-dependent policies.

## First-stop survival and conditional continuations

Retain the inherited 48th endpoint stop tree, with former A48=(11,4,0) fixed to immediate P. Nominal A=(7,1,3) ordered histories number 140, but **34 already stopped**; precisely **106** survive. The exact alive masses are

`pA=6625/11943936, qA=6625/2239488`.

For B the 12 surviving histories have `pB=48828125/725594112, qB=48828125/362797056`. After choosing continuation at the special states, conditional tuples (P-error,Q-error, extra P-samples, extra Q-samples) are

`cA=(18868399/18874368, 487/11943936, 1029359/786432, 393323/331776)` and

`cB=(63/64, 1/144, 9/8, 13/12)`.

Count-state sufficiency applies to these conditional iid suffix laws only; ordered first-stop paths were explicitly preserved when deriving reach. The two special states are prefix-incomparable, since A histories contain a symbol 0 and B histories contain none.

## Global primal attainment for every real parameter

Randomize immediate Q at A with probability u in [0,1], and at B with probability s. Relative to the inherited endpoint, A changes errors by `(+Xu,-Yu)` and B changes them by `(+E*(s-s48),-H*(s-s48))`, where

```
X=pA*(1-cA[P-error])=39544625/225434243432448
Y=qA*cA[Q-error]    =3226375/26748301344768
E=pB*(1-cB[P-error])=48828125/46438023168
H=qB*cB[Q-error]    =48828125/52242776064
```

Equalizing the errors gives `s=s48-h49*u`, with `h49=(X+Y)/(E+H)=129735679/870400000000`. Then

`eP=eQ=alpha48+eta49*u`, `eta49=X-h49*E=-Y+h49*H=241752875/12934289716936704>0`.

The probabilities are legitimate throughout: at u=1, `s49=8822627424173923/13926400000000000>0`. The expected sampling time under P satisfies `tP=V48-Gamma*eta49*u`; its difference from tQ is affine and positive at both endpoints, with exact u=1 margin `1754761146460127401/3725075438477770752>0`. Therefore `max(tP,tQ)=tP` on the whole interval and attains the Bellman lower bound. Affinity for all real u follows from disjoint prefix events; an author-side backward four-corner recursion verifies zero mixed difference, and a distinct forward recursion checks five mixtures.

## Sharp right endpoint

Equality with the same support line requires both errors saturate alpha (positive multipliers) and all chosen actions have zero Bellman slack. Only A and B admit mixing. Any ordered-history-specific mixture reduces by iid suffix constancy to two state-average probabilities u,s. Error equalization forces `s=s48-h49*u`; since u<=1, `alpha<=alpha49`. The finite randomized-policy space is compact, so the same support line cannot remain attained for alpha>alpha49. This is sharpness of the **49th supporting line**, not an endpoint for V14 as a whole.

## Next candidate, limitations, reproducibility

Fix A to immediately decide Q at the 49th endpoint; retain B tied. A symbolic linear-in-K backward cost scan finds the next potential equality for decreasing K at **`K50=137448576/7601`**, state **`A50=(9,5,0)`**, continue/decide-P. **Dual candidate only:** 50th reachable masses, primal error balance, affine endpoint, and sharpness are not yet proved.

Portable `fractions.Fraction` verifier checks all 680 states and 1240 action comparisons, exact first-stop survival, suffixes, primal mixtures and K50 scan; complementary author-side checker enumerates 3^7 ordered paths and all four absorbing-probability corners to prove zero mixed effects. No formal or independently reviewed inference is claimed.

BRC reuse: `REUSE_APPLIED` for positive rational branch-weight propagation with ordered first-stop provenance; naive 140-path multinomial mass would incorrectly include 34 already-stopped histories. No signed/phase cancellation or native physical transfer is asserted.