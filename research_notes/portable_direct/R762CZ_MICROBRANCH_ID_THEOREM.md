# R762CZ — Exact cost of retaining named microbranch provenance in Port windows

Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS. Companion to R762CY and R762CX, 2026-11-17. Frozen science at P000 V5 `a72226e2430ffa4786321ac86e7f0c599d5f0389`.

Status: mathematical proof in the explicitly defined positive three-Port N-BRC candidate; independent review NOT_REVIEWED. This is not an asserted native signed TRIADIC_CLOSURE_E event.

## Two exact observation languages

Let p,q be **arbitrary positive integers**, D=p+q, g=gcd(p,q), p'=p/g, q'=q/g and D'=D/g. At every step of the named Port cycle C3 there are p individually named clockwise microbranches and q individually named anticlockwise microbranches, each with probability 1/D. The start Port is fixed at 0.

For horizon h and 0<=r<=h, consider two classes of r-edge windows at each start time 0..h-r:

- `DIR_{h,r}`: the joint ordered Port labels (thus each + / - direction), while ignoring microbranch identities.
- `MIC_{h,r}`: the start Port together with the **ordered sequence of r individually named microbranch IDs**.

Both observers at r=0 mean one-time named Port marginals at all times 0..h. Let N_dir and N_mic denote minimal numbers of equiprobable initial deterministic h-step trajectories required to match all corresponding windows, with no new randomness.

Define C'_t as the three terminal-Port path counts for weights (p',q'), and `g'_t=gcd_i C'_t(i)`. The unnormalized weighted path counts satisfy `C_t=g^t C'_t`.

## Theorem — sharp identity cost for every finite window

For every p,q>=1, h>=0 and 0<=r<=h,

\[
\boxed{N_{\rm dir}(h,r)=\frac{(D')^h}{g'_{h-r}},\qquad
N_{\rm mic}(h,r)=\frac{D^h}{g^{h-r}g'_{h-r}}=g^r N_{\rm dir}(h,r).}
\]

In particular, if p,q are coprime, the two observers have the same **minimal seed cardinality**, even though one retains strictly more labeled history when p>1 or q>1. If the two weights have a nontrivial common divisor g, keeping every individual branch ID for an r-edge window incurs exactly a factor g^r in the sharp seed budget. Equality of budget is a rational-denominator statement, not an observer-equivalence/quotient-safety certificate.

### Proof of directional-window formula

Each step is normalized by D, so erasing distinctions among the g replicas of each primitive directional branch leaves the exact transition probabilities p'/D', q'/D'. The resulting entire named-Port stochastic process is equal in law to the coprime kernel with weights p',q'. The R762CY window theorem applies at every h and r, giving `(D')^h/g'_{h-r}` with a matching integral path realization.

### Proof of microbranch lower bound

At a start time t, a particular named source word b=(b1,...,br) and start Port i have exact joint probability
\[
\Pr(X_t=i,B_{t:t+r-1}=b)=\frac{C_t(i)}{D^{t+r}}.
\]
There are D^r distinct words, each with the same conditional probability, irrespective of their directions. Therefore the gcd of all integer numerators of this finite joint distribution is precisely `g_t=g^t g'_t`. This gcd divides D^{t+r}, and its exact reduced common denominator is `L^{mic}_{t,r}=D^{t+r}/g_t`. Any equiprobable M-seed realization reproducing the window must satisfy `L^{mic}_{t,r}|M`; at t=h-r, we obtain `D^h/g_{h-r}|M`.

### Proof of microbranch attainment

The exact gcd formula for the primitive coprime kernel from R762CX gives `g'_{t+1}/g'_t` equal to 1 or 3, with the factor 3 occurring only when 3 divides D'. Consequently `g_{t+1}/g_t=g(g'_{t+1}/g'_t)` divides D=gD'. Thus `L^{mic}_{t,r}` divides `L^{mic}_{t+1,r}` for every t, and with M=D^h/g_{h-r}, all prescribed window multiplicities `M C_t(i)/D^{t+r}` are integers.

Use a time-layered de Bruijn graph whose vertex records the starting Port and the previous r-1 microbranch IDs. Each r-ID window is an edge from its initial overlap to the shifted overlap, weighted by exactly the integer multiplicity just computed. Consecutive edge layers have equal integral incoming/outgoing overlap totals because they are two marginalizations of the same genuine Markov source process. Integral flow decomposition into M paths yields M legal, individually labeled h-step trajectories matching all microbranch windows simultaneously. For r=0 use the endpoint transport theorem R762CX. This attains the lower bound.

Substituting `C_t=g^t C'_t` gives the displayed ratio g^r. QED.

## Concrete non-coprime cases

With p=2,q=4,g=2,h=5, as r=0,1,...,5 the directional budgets are
`[27,81,81,243,243,243]`
and the microbranch-ID budgets are
`[27,162,324,1944,3888,7776]`.

With p=q=2,h=5, direction-window budgets are all 32; ID-window budgets are
`[32,64,128,256,512,1024]`.

This gives a provenance-specific information lower bound that does not arise from endpoint-only observation, and it identifies exactly how much information is lost when g indistinguishable copies are collapsed in the observer.

## Reproduction and scope

`R762CZ_MICROBRANCH_VERIFY.py` tests all 16 positive p,q<=4 (including noncoprime), every 0<=h<=5 and every 0<=r<=h: 336 window cases, 2,688 reduced-marginal integrality assertions, 320 exact overlap-layer checks and 78 explicit full trajectory decompositions. See `R762CZ_EVIDENCE.json`; arithmetic is exact integers. These finite checks supplement the universal argument.

Whether native TRIADIC_CLOSURE_E can query microbranch identity or only named directions/Ports remains unresolved. The correct native minimum requires its source-backed event permission and V17/V29/V39 legal transport. Retain any signed path-area/provenance needed by such permissions and do not infer a safe quotient from equal M.
