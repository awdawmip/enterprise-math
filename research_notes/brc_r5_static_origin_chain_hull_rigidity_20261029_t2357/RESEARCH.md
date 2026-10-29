# R5 — Static-origin absorbing stopping chains: hull-to-real-image rigidity

Date: 2026-10-29 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED**. This is author-side portable mathematics, not a Source CLAIM/Result/Driver review.

Frozen inputs: GLOBAL_KNOWLEDGE_V1 `main@b5a4c88d7e9d5040ad4ab233b023720ea9b3070a`; Enterprise Math `main@b7e005a480e17723d1fced8e1886681e78a3e88d`. Read the account bootstrap and manual, project AGENTS/P000/ACTIVE worldview/joint-observer preservation, TASK_RESEARCH and portable protocols. Predecessor: PR #1663 `de7a5f1b13cfe80c5a23cf753d0f2ca467cba50b`, whose four-moment result is nonabsorbing and explicitly outside the original stopping-observer target.

## Exact model
An initially observed provenance label `S=s` has positive probabilities `P_s,Q_s` summing to 1. At times `j=1,...,m`, the controller may stop or continue; time `m` forces stop. There are **no new exogenous observations or nature transitions before stopping**. On stop at `j`, terminal Bernoulli error rates are `p_sj=P(E=1|s,stop j)` and `q_sj=Q(E=1|s,stop j)`, all strictly between zero and one. FULL sees `s` and its earlier decisions. A seedless LR strategy sees only `(j,r_s)`, where `r_s=P_s/Q_s`. Since law-independent action probabilities cancel in P/Q path ratios, `r_s` remains fixed on all positive continue histories.

Partition sources into ratio classes `g={s:r_s=r_g}`. A FULL real behavioral policy induces any conditional stop-time distribution `d_s∈Δ_m`; conversely every `d_s` is implemented by sequential hazards `h_sj=d_sj/(Σ_{k≥j}d_sk)` when survival is positive, with arbitrary unreachable choices. LR can implement any `d_g∈Δ_m` similarly, but must share it over `s∈g`. The exact four-stopping-observer map is

```
e_P = Σ_s P_s Σ_j d_sj p_sj;    e_Q = Σ_s Q_s Σ_j d_sj q_sj;
T_P = Σ_s P_s Σ_j j d_sj;      T_Q = Σ_s Q_s Σ_j j d_sj.
```

BRC reuse: labeled positive P/Q origin and path masses, never fictitious signed probabilities; source compression is allowed only for precisely declared terminal observers and stopping horizon.

## Theorem 1: all-real hull-to-image rigidity
**For any finite S, horizon m, positive model as defined, and any real behavioral probabilities (including zero and one), the actual FULL and seedless-LR observer images are convex polytopes. Therefore**
```
conv(O_FULL)=conv(O_LR)  iff  O_FULL=O_LR.
```
The same argument holds for any finite vector of terminal expectation observers.

**Proof.** FULL is the affine image of `∏_s Δ_m` under the displayed observer map. LR is the affine image of `∏_g Δ_m` under the map obtained by repeating `d_g` across all sources in the class. Every simplex point is implemented by the stated seedless sequential hazards, including zero-flow boundaries. Both actual images are therefore polytopes already equal to their convex hulls. LR is a subclass of FULL. Hull equality consequently implies actual-image equality; the reverse is immediate. QED.

This rules out **all** static-origin/no-new-nature-information stopping chains from the mother target, regardless of their horizon, number of ratio classes, source-dependent terminal errors or observer polytope dimension. It strictly extends the predecessor's rank-≤3 obstruction for a single three-key chain. It does not rule out later stochastic splitting or reconvergence.

## Theorem 2: exact signed support-gap formula
For any real signed `w=(w1,w2,w3,w4)` define
`c_sj(w)=P_s(w1 p_sj+w3 j)+Q_s(w2 q_sj+w4 j)`.
Independently optimizing the simplex coordinates yields
```
min_FULL(w·O) = Σ_s min_j c_sj(w)
min_LR(w·O)   = Σ_g min_j Σ_{s∈g} c_sj(w)
Δ(w)          = Σ_g [min_j Σ_{s∈g} c_sj(w) − Σ_{s∈g} min_j c_sj(w)] ≥ 0.
```
The nonnegative bracket is zero exactly when the sources in that class possess **at least one common minimizing stop time**. Indeed, taking a minimizing common time `j*`, the bracket equals the sum of nonnegative slacks `c_s,j*−min_j c_sj`, which vanishes iff every slack does. Thus all-real all-signed convex-hull equality is equivalent to the common-argmin condition for every signed `w`; by Theorem 1 it also implies equality of actual images. With rational kernels a failing direction gives an exact rational support/Farkas certificate. QED.

## Corollary: source-offset, observer-safe BRC quotient
Suppose within every ratio class `g`, terminal kernels are **source-offset separable**:
`p_sj=a_s+b_gj` and `q_sj=c_s+d_gj`, with probabilities remaining strictly between 0 and 1. Then `O_FULL=O_LR` constructively. For any FULL stop flows define
`d_gj=(Σ_{s∈g}Q_s d_sj)/(Σ_{s∈g}Q_s)`.
Since `P_s=r_g Q_s` within each class, this preserves simultaneously the P and Q class/time stop flows. Source offsets contribute fixed `Σ_s P_s a_s` and `Σ_s Q_s c_s`; shared time profiles depend only on preserved flows. Hence all four observers agree. Explicit hazards realize `d_g`. This proves only the declared four-observer, finite-horizon quotient; retained provenance may matter to future operations. QED.

## Strictly positive rational witness: FULL and LR equal, four-dimensional interior
Use three sources and three stop times, with initial P/Q weights:
```
source      P_s  Q_s  ratio
A           1/8  1/4   1/2
B           1/8  1/4   1/2
C           3/4  1/2   3/2
```
Terminal error probability rows under P and Q:
```
source  (p_s1,p_s2,p_s3)       (q_s1,q_s2,q_s3)
A       (1/5,3/10,1/5)        (1/5,1/5,3/10)
B       (1/4,7/20,1/4)        (1/4,1/4,7/20)
C       (1/4,1/4,1/2)         (1/4,1/2,1/4)
```
For AB, `p_Bj−p_Aj=q_Bj−q_Aj=1/20` for each time, so the source-offset corollary applies although A and B have distinct terminal kernels and collide at every decision.

At the LR deterministic strategy both classes stopping at t=1, `V0=(39/160,19/80,1,1)`. Relative to this base, switching class AB to t=2 or t=3, then class C to t=2 or t=3, produces four displacement columns
```
U_AB2=(1/40,0,1/4,1/2)
U_AB3=(0,1/20,1/2,1)
U_C2 =(0,1/8,3/4,1/2)
U_C3 =(3/16,0,3/2,1).
```
Their exact determinant is **1/1280≠0**. The product of two interior 2-simplexes maps to a genuinely four-dimensional open set in the common FULL/LR observer polytope. A dimensional rank argument alone cannot detect lost information in this safe class.

Concrete FULL schedules:
`d_A=(1/3,1/2,1/6)`, `d_B=(1/5,2/5,2/5)`, `d_C=(1/6,1/3,1/2)`.
Exact observer:
`O=(279/800,22/75,541/240,87/40)`.
Equivalent seedless LR class schedules are
`d_AB=(4/15,9/20,17/60)` and `d_C=(1/6,1/3,1/2)`;
hazards `(4/15,27/44,1)` and `(1/6,2/5,1)`. Nature kernels are all strictly positive; the forced last stop is a controlled action.

## Sharpness: nonseparable source-time interaction gives strict signed separation
Take `P_A=P_B=Q_A=Q_B=1/2` with ratio 1, three stop times, and strictly positive terminal probabilities
```
p_A=(1/4,1/2,3/4); p_B=(3/4,1/2,1/4);
q_A=(1/5,1/2,4/5); q_B=(4/5,1/2,1/5).
```
Every real LR stop distribution makes `e_P=e_Q=1/2`, hence **`20e_P+20e_Q≥20`** for all LR strategies. FULL chooses A to stop at 1 and B at 3, giving `O*=(1/4,1/5,2,2)` with left side **9**. The exact signed support gap in direction `(20,20,0,0)` is **11**, with `dist_∞(O*,O_LR)≥11/40`. The sourcewise minimizing times are disjoint. This is a strict-convex-hull *exclusion*, not the mother-problem solution.

## Executed validation, evidence and remaining boundary
The standalone `VERIFY.py` uses Python standard-library exact `Fraction` and permutation determinant. Actual executed `EXACT_OUTPUT.txt` verifies initial positive normalized masses, all terminal kernels, class ratios and offsets, determinant 1/1280, explicit hazard lift, **21,952** denominator-6 FULL schedules with exact source-flow matches, 9 deterministic LR class profiles, and 3 LR/9 FULL deterministic support witnesses for the unsafe model; it ends in `PASS_EXACT_R5_STATIC_ORIGIN_CHAIN_HULL_RIGIDITY`. Finite checks are regression; the all-real claims are proved by the simplex/hazard/support argument, not by sample count.

No Lean check, literature-novelty proof, physical X6 correspondence or independent mathematical review. Native status reported `research_authority_granted=false` and current owner inventory returned `CONTROL_QUOTA`; no formal Source CLAIM/Result/review was obtained. This GitHub note is neutral portable evidence.

**Next:** construct a strictly positive post-initial stochastic split/reconvergence with ≥3 consequential LR decisions and actual absorbing four-observer outputs; obtain exact rational convex-combination certificates or Farkas separators for *every* FULL deterministic observer versus LR hull, including all signed directions. Only a candidate passing full hull equality should proceed to all-real polynomial/nonmembership proof with all zero-reach and 0/1 boundary policies. See `NEXT_TASK.md`.
