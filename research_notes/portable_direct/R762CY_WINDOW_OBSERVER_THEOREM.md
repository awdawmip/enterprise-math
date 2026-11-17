# R762CY — Exact Port-window observer hierarchy for weighted C3 positive N-BRC

Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142; author-side continuation 2026-11-17.
Prior frontier: R762CX at `ccce89fd6fdd52ae61b3c4e64cd7e4211f6dd499`.
Frozen input: P000 V5 / signed X6 source commit `a72226e2430ffa4786321ac86e7f0c599d5f0389`. P000 remains unchanged.
Status: exact conditional positive N-BRC candidate-kernel mathematical proof, locally checked, independent review NOT_REVIEWED. No native signed TRIADIC_CLOSURE_E event permission is asserted.

## Model and observation language

Fix a named three-Port candidate component `i in Z/3Z`. From Port i, the `+` direction to i+1 has p independent positive source branches, and the `-` direction to i-1 has q branches, p,q positive coprime integers. D=p+q. For an initial Port 0, let C_t(i) count the length-t named-endpoint microbranch paths. Then
`C_0=(1,0,0)`, `C_{t+1}(j)=p C_t(j-1)+q C_t(j+1)` (indices mod 3), and `sum_i C_t(i)=D^t`.
Define `g_t=gcd(C_t(0),C_t(1),C_t(2))`, `g_0=1`.

For a finite time horizon h and a *window length* r with 0<=r<=h, the observer O_{h,r} sees, separately for every start time t=0,...,h-r, the joint probabilities of the **ordered named-Port tuple** `(X_t,...,X_{t+r})`. A window of length r uses r directed edges and r+1 Port observations. For r=0 this is the collection of one-time Port marginals; for r=h it is the entire named-Port trajectory. Since no self transitions exist on C3, a consecutive named-Port pair determines each `+` / `-` step uniquely. Microbranch IDs within a direction are not individually observed.

A realization uses M equiprobable initial seeds, one legal deterministic full Port trajectory of h edges per seed, and no further random input. It must reproduce all O_{h,r} windows *jointly and consistently* (each window marginal separately); it is not required to reproduce probabilities of longer windows than r. Let M_{h,r} be the smallest such positive integer.

## Theorem: sharp memory for every Port-window length

For every p,q>=1 with gcd(p,q)=1, every h>=0, and 0<=r<=h,

\[
\boxed{ M_{h,r}=\frac{D^h}{g_{h-r}}. }
\]

By R762CX's exact divisibility theorem,
\[
g_n=\begin{cases}
1,&n=0\text{ or }3\nmid D,\\
3^{\lfloor(n-1)/2\rfloor},&n\ge1,\ 3\mid D .
\end{cases}
\]
Thus `M_{h,0}=Q_h` exactly recovers R762CX endpoint-only memory; `M_{h,h}=D^h` is full directional-source-word memory. All intermediate lengths are now classified. If 3 does not divide D, every r costs D^h seeds. If 3 divides D, the ratio `M_{h,r+1}/M_{h,r}` is 3 exactly when `h-r` is odd and at least 3, and is 1 otherwise. The r-window hierarchy therefore has exact 3-adic plateaus; each newly resolved step of joint history either costs one ternary digit or costs no additional seed.

### Proof: exact lower bound

For a start time t and any directed word w of r choices with a positive steps and b=r-a negative steps, the joint event `(X_t=i, w)` has probability
\[
P_t(i,w)=\frac{C_t(i)p^a q^b}{D^{t+r}}.
\]
This word uniquely determines the ordered Port tuple. The gcd of all integer numerators over i and w is `g_t`: the gcd over w of `p^a q^{r-a}` is 1 because `p^r` and `q^r` are among the terms and gcd(p,q)=1. Also g_t divides D^t. Therefore the least common denominator of this finite joint distribution is exactly
\[
L_{t,r}=D^{t+r}/g_t.
\]
In any deterministic realization with M equiprobable seeds every event probability is an integer multiple of 1/M, hence `L_{t,r}|M`. Taking t=h-r forces `D^h/g_{h-r}|M`.

### Proof: attainment for r>=1

Put `n=h-r` and `M=D^h/g_n`. R762CX's gcd formula implies `g_{t+1}/g_t` is 1 or 3, and whenever it is 3, 3 divides D. Consequently `L_{t,r}|L_{t+1,r}` for every t, and all probabilities `M P_t(i,w)` are nonnegative integers for 0<=t<=n.

Construct a time-layered directed multigraph. At layer t its nodes are length-(r-1) directed Port histories (equivalently r consecutive Port labels). Give the edge corresponding to each legal length-r directed Port window `(x_t,...,x_{t+r})` the integral multiplicity `M P_t(x_t,w)`; it runs from the first r Port labels to the last r Port labels. The outgoing total at every node in layer t equals the incoming total from layer t-1: these are both `M` times the same exact probability of its overlapping length-(r-1) Port history. This is a consistency identity for the original Markov kernel, not an assumed relaxation.

The resulting finite acyclic layered graph has integral nonnegative edge multiplicities and total initial flow M. By repeatedly following positive-flow edges and subtracting one unit, it decomposes into exactly M complete paths. Restoring the first r Port labels and appending the last label of each successive edge produces M legal h-step Port trajectories. Their r-window frequencies equal the prescribed edge multiplicities at every t. Thus `M_{h,r}<=M`, matching the lower bound.

### r=0 and boundary cases

When r=0, exact attainment by integral bipartite transports for the one-time Port marginal constraints is R762CX, Theorem 2; its hypothesis and deterministic no-new-randomness seed model are identical here. At h=r=0, one deterministic length-zero path suffices. The theorem follows.

The lower bound is an **equality for all h,r** in the stated observer language; it does not assume that the observed marginal process itself is deterministic.

### Nonprimitive weights

For arbitrary positive p,q, divide both by k=gcd(p,q). The normalized Port process depends only on p'=p/k, q'=q/k. Apply the theorem using D'=p'+q'. The number of **microbranch ID words** is a different observer and is not covered by the collapsed directional-Port window statement.

## Exact examples

For p=1,q=2,D=3,h=6, as r runs from 0 through 6, the optimal seed counts are
`[81,81,243,243,729,729,729]`.
For p=q=1,D=2,h=6, all seven values equal 64.
For p=1,q=2,h=3, the separate endpoint marginals need 9 seeds, but observing any adjacent named-Port pair at each time needs 27. This gives a sharp joint-observer failure of the endpoint-only quotient while preserving its stated promise.

## Evidence and relationship to native X6

`R762CY_WINDOW_OBSERVER_VERIFY.py` reproduces exact BigInt-equivalent Python integer checks for all 19 coprime pairs 1<=p,q<=5, 0<=h<=8 and 0<=r<=h. The author run checks 855 window cases; 112,917 integer-event divisibility assertions; 2,280 de Bruijn overlap layers; and 70 explicit integral full-path decompositions in the smaller box. See `R762CY_EVIDENCE.json`. The finite domain checks supplement the general algebraic proof and the cited R762CX gcd lemma. These statements are new relative to R762CX's r=0/full-word endpoints, but independent novelty review has not occurred.

This theorem is for the three named Port **candidate** graph inside a declared signed-X6 sector. It does not redefine six-dimensional Cell incidence, PERP_E, P000 triadic balance or primitive signed cancellation. Exact future-observer safety of a coarser residual needs the actual authenticated TRIADIC_CLOSURE_E event language, native V17/V29/V39 transport and oriented-pair-area provenance rules. This remains the key unresolved task.

Suggested next independent unit: for a particular source-backed legal E event, determine the maximum length of ordered Port window it may query and whether it also accesses earlier signed-area/provenance residues; then apply M_{h,r} or construct an explicit legal-suffix witness requiring a stronger joint carrier.
