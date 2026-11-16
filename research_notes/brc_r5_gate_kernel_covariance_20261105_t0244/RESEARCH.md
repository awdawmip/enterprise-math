# R5: exact two-source gate–kernel covariance residual at a lawful LR merger

Status: AUTHOR_DERIVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.
Scope: an auxiliary finite positive two-source BRC stop/continue model, with all free P/Q declarations and O4=(eP,eQ,TP,TQ). This is a derivation about **canonical Q-occupancy Markovization**; no claim of FULL/LR image or hull separation follows from a nonzero canonical reconstruction residual alone.

## 1. Frozen frontier and question

Frozen scientific inputs: Global `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Current behavioral rules were separately loaded from canonical main, without changing these pins. Continue the positive-P/Q likelihood-ratio stopped-tree R5 series, especially `research_notes/brc_r5_q_lumpable_occupancy_markovization_20261105_t0140/RESEARCH.md` at `f34b4fbcf2292e3758dcaf43f46b016f841c1baa`. The mother objective is a lawful R5 model with equal complete O4 convex hulls and unequal actual real-behavior images.

Selected discriminating question: for a non-lumpable, positive-probability two-source merger, calculate **exactly** which information is lost when the FULL continue gate is averaged at the common likelihood-ratio key. Separate the resulting numerical O4 defect from global LR reachability.

## 2. Typed BRC experiment

At time t=1 two distinct provenance histories A,B share the LR key r=1. Under Q they have respective masses w_A,w_B>0, w_A+w_B=1; under P they have the same masses, so this is a lawful LR merger (the preceding branch to A or B has equal P and Q probabilities). At that key, FULL can choose STOP and declare P, STOP and declare Q, or CONTINUE, with source-dependent probabilities s_h^P,s_h^Q,c_h>=0 summing to 1. All continuing histories stop at time t=2. Conditional on CONTINUE from h, a finite terminal LR key r_j>0 is reached with strictly positive Q kernel K_h(j), satisfying

```
sum_j K_h(j) = 1,
sum_j r_j K_h(j) = 1.
```

The corresponding P kernel is r_j K_h(j), also a strictly positive probability distribution. At terminal key (h,j), FULL declares P with arbitrary probability f_hj in [0,1]; otherwise it declares Q.

The seedless LR policy `L°` reconstructed from this FULL policy has common first-gate action probabilities `sbarP=sum_h w_h s_h^P`, `sbarQ=sum_h w_h s_h^Q`, `C=sum_h w_h c_h`. At terminal LR key r_j it declares P with Q-occupancy-weighted frequency

```
muF_j = sum_h w_h c_h K_h(j),
f_j  = (sum_h w_h c_h K_h(j) f_hj) / muF_j   if muF_j>0,
f_j  = 0 otherwise.
```

This respects all seedless (t,r) information keys. The LR continuation mass at j is `muL_j=C*Kbar_j`, with `Kbar_j=sum_h w_h K_h(j)`.

## 3. Exact covariance theorem (all real behavior probabilities)

Define `D_j=muF_j-muL_j`. Then

```
D_j = sum_h w_h (c_h-C) K_h(j)
    = sum_h w_h (c_h-C)(K_h(j)-Kbar_j).
sum_j D_j = 0,     sum_j r_j D_j = 0.
```

For the two-source case the residual factorizes exactly:

```
D_j = w_A*w_B*(c_A-c_B)*(K_A(j)-K_B(j)).
```

The complete four-dimensional observation defect of the specified canonical reconstruction, in order (eP,eQ,TP,TQ), is

```
O4(FULL)-O4(L°) =
(-sum_j r_j D_j f_j, sum_j D_j f_j, 0, 0).
```

Moreover the Q-total-variation distance between the **terminal LR-key distributions** (equivalently between the final time-and-key-and-declaration distributions after using the same f_j on both sides) is exactly

```
TV = (1/2) sum_j |D_j|
   = w_A*w_B*|c_A-c_B|*TV(K_A,K_B).
```

Consequently `|Delta eQ|<=TV`, `|Delta eP|<=max_j(r_j)*TV`, and both expected stopping times are preserved. With first-gate probabilities fixed, the supremum of `|Delta eQ|` over free terminal P/Q labels is **exactly TV**; choose `f_j=1` when `D_j>0` and 0 otherwise. Thus `D=0` characterizes lossless *terminal key-distribution* aggregation by this particular canonical reconstruction; in the two-source case this occurs iff `c_A=c_B` or `K_A=K_B`.

**Proof.** The FULL terminal Q mass is the sum of source-resolved continuing masses, while LR multiplies the averaged first gate by the unconditional source-mixture kernel; subtraction yields D, and elementary two-source expansion yields the factorization. The two row-normalization identities yield the zero total mass and zero first LR moment. Initial STOP actions match after Q averaging, including their P weights since source LR=1. Terminal P-declaration Q mass in FULL equals `muF_j f_j` by definition of f_j; LR uses `muL_j f_j`. Thus the Q error coordinate difference is `sum D_j f_j`. The P error difference is `sum r_j D_j(1-f_j)=-sum r_j D_j f_j` because the first LR moment vanishes. Stopping time T_Q is `1+C`; stopping time T_P is `1+sum_j r_j muF_j=1+C` on FULL, and the same identities apply to LR. For TV of the terminal joint output, splitting a fixed key's mass according to the same f_j preserves its absolute difference `|D_j|`. The signed-measure bound yields the risk inequalities. Finally `sum D_j=0` implies the maximal integral of any [0,1]-valued terminal declaration against D is its positive variation, equal to TV; the sign selector attains it. QED.

## 4. Exact rational witness and finite check

Take `w=(1/2,1/2)`, terminal `r=(1/2,1,3/2)`, with

```
K_A = (1/4,1/2,1/4),
K_B = (5/16,6/16,5/16).
```

Every Q and P transition is strictly positive, with row mass and row LR expectation exactly one. The two source kernels have Q TV distance `1/8`. Choose FULL gate `c_A=1,c_B=0` (B stops and declares P), and terminal P declaration exactly at LR=1 (Q at the other two keys). Then

```
D = (-1,2,-1)/64; TV=1/32.
O4(FULL) = (1/4, 3/4, 3/2, 3/2).
O4(L°)   = (9/32, 23/32, 3/2, 3/2).
O4(FULL)-O4(L°) = (-1/32, +1/32, 0, 0).
```

Standard-library Fraction program `VERIFY.py` exhausts **576 deterministic FULL policies** (3 first actions per source and 2 terminal declarations at each of the 6 provenance-terminal pairs). All exact factorization, zero-moment, time-preservation, risk, and TV assertions pass; **192/576** have a nonzero canonical O4 reconstruction difference. See `EXACT_OUTPUT.txt`. All-real identities follow from the displayed algebra, not from the finite enumeration.

## 5. Interpretation and next work

BRC carriers: source-labeled positive rational Q/P weights, stop/continue actions, terminal LR keys, joint gate–kernel state, and four observation coordinates. The projected LR key alone discards the signed *difference of positive branch masses* `D`; D itself is a bookkeeping difference, not a negative probability. `REUSE_APPLIED`: positive-weighted BRC provenance and the previous Q-key occupancy Markovization interface. The new observation is a scoped exact covariance identity, not a claim of novelty over classical covariance/MDP occupancy theory.

A nonzero defect in this *specified* averaged LR policy does **not** establish that the FULL point is outside the entire LR image. In particular, single-merger R5 models with unequal terminal experiments can have stronger support-function obstructions, as already studied in the R5 predecessor chain. The mother problem remains open.

Next: use this covariance form as an exact diagnostic for two interacting continue resources or merged gates. Derive their joint D-vectors (including correlation terms), test exact full O4 hull equality with rational certificates, then test actual LR-image nonmembership in a candidate that passes the hull stage. Preserve all positive P/Q kernels, free declarations, merged LR provenance, and frozen input pins.

## 6. Sources and status

Internal primary source: `awdawmip/enterprise-math` Draft PR #1767; predecessor `f34b4fbcf2292e3758dcaf43f46b016f841c1baa` and `docs/RESEARCH_CONTINUATION_PROTOCOL.md` main `406e965c173e86da48e7121db7b394b0f0b7f8bf`. Global main rules snapshot `58ded97e8aeb5f52b4a7de8c2aebc97ff51ca1a6`. P000 ACTIVE was read at this snapshot, unchanged. No outside paper is required for the proof. Status: AUTHOR_DERIVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. Actual native task owner/CLAIM authority must be read separately from canonical control; author-side storage is not a task Result or independent review.
