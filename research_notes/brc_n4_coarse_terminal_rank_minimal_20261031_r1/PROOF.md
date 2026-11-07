# BRC N=4: exact minimal source-prepared compression for a coarse public terminal observer

**Author-side analytic theorem and exact finite check; 2026-10-31.** Status: UNREVIEWED / NOT_ADMITTED. Continuation of immutable predecessor `71f3ed586bc4100bc7bc221fe814a326faca8461` in PR #1757. This is a finite, externally specified positive-weighted BRC experiment, not a native Heartbeat X6 physical dynamics result.

## 1. Carrier, time and quantifiers

Retain the original strictly positive 16 leaves `(S,J,K)`, `S ∈ {AU,AV,BU,BV}`, `J,K ∈ {0,1}`, with weights per individual K leaf (divide by 240):

| S | Q(J=0) | Q(J=1) | P(J=0) | P(J=1) |
|---|---:|---:|---:|---:|
| AU | 10 | 10 | 9 | 11 |
| AV | 20 | 20 | 5 | 5 |
| BU | 15 | 15 | 3 | 27 |
| BV | 15 | 15 | 30 | 30 |

Both full laws normalize, and K is fair given (S,J). At **stage two** the source-prepared experiment presents one of eight input states `x=(s,b)` with `b ∈ {P,Q}`; this is an *external preparation label*, NOT an originally observable physical bit or a seventh spatial axis. Under b, the next authentic bit J has conditional success probability

`p_AU,P=11/20, p_AU,Q=1/2; p_AV,b=1/2; p_BU,P=9/10, p_BU,Q=1/2; p_BV,b=1/2.`

The encoder `E(c|s,b)` is one fixed stochastic kernel applied **before J is drawn**. It is independent of which later lawful strategy is selected. For each allowed strategy H, a decoder `D_H(o|c)` may depend on H but must not have free access to s, b, the compression label as an observable, or the actual J/K. Exact fidelity is **statewise**:

`for every (s,b) and every H in the stated policy class:  L_H(o|s,b) = sum_c E(c|s,b) D_H(o|c).`

Only the **marginal public terminal record** is scored: `O=(T,Decision,Z_BU)`. No joint coupling to the already-realized J or K, and no faithful same-path recovery, are demanded. The optional BU-origin public sensor is `Z=J XOR Bernoulli(epsilon)` when `S=BU`; elsewhere its output is a separate absent symbol `⊥`. `0 ≤ epsilon ≤ 1/2`; the noise law is independent of preparation. This explicit BU-only emission convention is part of the theorem, not a claim that the original S2/S23 grammar mandates such a sensor. Policy tests below ignore Z. Stage-four strategies may read actual K **only after continuation**; none is allowed to rewrite K. The decoder may internally sample the same lawful conditional future, not tamper with an actual path.

Let `m*(H)` denote the minimum number of encoder symbols for one fixed H, and `m*(F)` the minimum for one encoder working for every H in family F. Randomized encoders and randomized decoders are both allowed; `S` is NOT provided free after encoding.

## 2. Exact theorems

Choose the fully lawful S23 strategy `W`: continue to stage three on all branches, stop there, and output Decision=P exactly when the contemporaneous P/Q likelihood ratio is >1. Thus `W` decides P at AU1, BU1 and all BV nodes, and Q at AU0, all AV nodes and BU0.

**Theorem A — one fixed policy.** Under the BU-only Z observer above, `m*(W)=4` for every real `0 ≤ epsilon ≤ 1/2`. If Z is expressly **suppressed** (one constant absent symbol for all S), the distinct, narrower fixed-policy problem has `m*(W)=2`.

**Theorem B — all lawful policies.** With `O=(T,Decision,Z_BU)`, `m*(all S23)=m*(all S2)=6` for every real `0 ≤ epsilon ≤ 1/2`. This remains true when Z is suppressed entirely: the distinguishing policies use only the Decision event. It is a coarse-output theorem that *does not assume retained S*; its number happens to equal the earlier six-state result with retained S for a different, newly certified reason.

### Proof of A: four symbols suffice and are necessary

Write four encoder symbols `N_Q,N_P,B_0,B_1`. For s ≠ BU, sample `N_P` with probability `P_W(Decision=P|s,b)` (AU: p_AU,b, AV: 0, BV: 1), otherwise `N_Q`; decode into respectively `(3,P,⊥)` and `(3,Q,⊥)`. For BU, encode `B_J` with probability `P(J|BU,b)`; decode `B_1` as `(3,P,Z)` and `B_0` as `(3,Q,Z)`, generating Z conditionally with the prescribed epsilon. This EXACTLY reproduces the six public atoms for both preparations, not merely a scalar TV distance.

For necessity, form the 8 × 6 matrix `M_W` whose row x is the public output distribution `L_W(.|x)`. The four aggregated output columns `(nonBU Q,nonBU P,BU Q,BU P)` obtained by summing Z on BU already contain, on rows `(AV,Q),(BV,Q),(BU,Q),(BU,P)`, the submatrix

```
[ 1 0 0   0   ]
[ 0 1 0   0   ]
[ 0 0 1/2 1/2 ]
[ 0 0 1/10 9/10]
```

of determinant `2/5`, so `rank(M_W) ≥ 4` independent of epsilon. The four-symbol factorization above gives `rank(M_W) ≤ 4`. Every common m-symbol stochastic factorization `M_W=ED_W` has `rank(M_W) ≤ m`, proving `m ≥ 4`. When Z is suppressed, the output has only two possible atoms, and pre-sampling Decision gives m≤2; AU P and Q have different Decision probabilities 11/20 and 1/2, ruling out m=1. QED.

### Proof of B: a nonzero six-policy rational minor

For each s, define the lawful S23 policy `H_s`: always continue through stage two; stop at stage three; Decision=P iff the **observed S equals s**, else Q. This is genuinely lawful despite the original S23 rule "equal contemporaneous likelihood ratios imply equal action": the six time-three ratio classes `AU0,AU1,AV,BU0,BU1,BV` are mutually disjoint across S, and both equal-ratio daughters within AV/BV receive the same decision. Continue kernels at AU/BU are both 1, satisfying S2. The policy may be implemented as a lookup on the ratio classes alone.

Also define two lawful policies `H_AU1` and `H_BU1` that decide P iff respectively `(S,J)=(AU,1)` or `(BU,1)`, and Q otherwise; again both stop at stage three and respect the ratio classes.

Consider the six columns of probabilities `P_H(Decision=P|s,b)` for `H_AU,H_AV,H_BU,H_BV,H_AU1,H_BU1`. Select the six rows `(AU,Q),(AU,P),(AV,Q),(BU,Q),(BU,P),(BV,Q)`; their exact matrix is

```
[ 1 0 0 0 1/2   0   ]
[ 1 0 0 0 11/20 0   ]
[ 0 1 0 0 0     0   ]
[ 0 0 1 0 0     1/2 ]
[ 0 0 1 0 0     9/10]
[ 0 0 0 1 0     0   ]
```

and determinant `+1/50 ≠ 0`. Thus this six-policy response matrix has rank at least six. For ANY universal encoder E with m columns, stacking one event probability per policy factors the response matrix as `E V` for policy-specific decoder event vectors. Hence `m ≥ 6`, even with randomized encoders, with arbitrary noise epsilon and with S absent from the public output.

For the upper bound, use the six **encoder** symbols `AU_P,AU_Q,AV,BU_P,BU_Q,BV`. Map (s,b) deterministically to its matching symbol, discarding b only at AV/BV. Given this symbol, draw J from the correct conditional law, draw fair K only when a lawful policy continues to its fourth-stage information set, draw Z when declared, and execute any given lawful law-independent S2/S23 policy. AV/BV may merge b because their conditional (J,K) laws agree under P and Q. This common policy-aware decoder reproduces the **entire law of the stated public terminal output** statewise, so m≤6. The S23 test policies are a subset of S2, and the decoder handles all S2, so both minima equal six. QED.

## 3. Scope, limits and relation to earlier results

The `4 vs 6` gap is for **one preannounced strategy versus post-encoding choice among all lawful strategies**. The `2 vs 4` fixed-policy gap depends on whether a BU-only sensor / absent tag is part of the public output. These are different observation interfaces and do not contradict each other. Pre-sampling at T2 is valid for distributional reconstruction; it DOES NOT restore the same actually realized J or K, nor preserve a joint history coupling with an external observer.

No probabilistic source-agnostic native physical transition or P000 Heartbeat time calibration was derived. The ordinary linear-rank factorization bound is classical linear algebra and compatible with statistical randomization/Blackwell sufficiency; the new claim is this exact lawful finite BRC instantiation, observer typing and rational separating certificate. There is no claim of a novel general Blackwell theorem. A fixed S23 policy with different time/stopping rules can require a different number of symbols; Theorem A is only W, not all fixed S23 policies.

## 4. Exact independent checks

`VERIFY.js` is the very BigInt function executed for this author-side result. It reconstructs the 16 positive source leaves and both normalizations, verifies W's exact four-symbol output factorization over four sensor errors (0,1/8,1/4,1/2), computes output matrix rank four, checks the 1/50 six-policy minor and rank six, and checks the six-state quotient on all 64 deterministic S23 ratio-class decisions stopping at stage three, at all four noise levels, eight prepared inputs each. The full continuum of real epsilon and all adaptive lawful S2 strategies follow from the analytic kernel proof, not that finite parameter check. Status remains author proof, exact executed finite check, no native Result, no independent review or admission.
