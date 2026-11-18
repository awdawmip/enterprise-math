# S23/AV — exact all-finite-H inversion counts via Euclidean floor sums

Date 2026-11-08. Direct continuation of `PROOF.md` in this directory, same frozen science `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Status: mathematically derived exact algorithm and executed integer certificates; independent review pending.

## Result: direct rank correction without enumerating inversion directions

Retain `r=ln7/ln(10/7)`, `u=(a,c)=(79,431)`, `w=(D,P)=(380295,2074774)`, `M=D+P=2455069`; `79P-431D=1`. Let `epsilon=79r-431>0`, `eta=P-Dr>0`, and `alpha=epsilon/eta>0`. The universal inversion-charge rank identity from `PROOF.md` reads

```text
rank_theta(v,j)-rank_L(v,j) = F(H-v-j) - G(v,j),

F(T)  = # {(A,B) in positive integers: 510A+M B<=T, B>alpha A},
G(v,j)= # {(A,B) in positive integers:
           79A+DB<=v, 431A+PB<=j, B>alpha A}.
```

For every finite integer `T,v,j>=0`, these counts admit exact evaluation by Euclidean floor sums and binary search, with no enumeration of pairs `(A,B)`.

Define `z(A)=floor(alpha A)` and `S_alpha(n)=sum_{A=1}^n z(A)` (`S_alpha(0)=0`). For `T>=0`, set

```text
U_F(A)=floor((T-510A)/M)
N_F=max(0,floor((T-M)/510))
k_F=max {A in [1,N_F] : U_F(A)>z(A)}, or zero if empty.
```

Then

```text
F(T) = sum_{A=1}^{k_F} floor((T-510A)/M) - S_alpha(k_F).   (F)
```

For `p=(v,j)`, set

```text
U_v(A)=floor((v-79A)/D)
U_j(A)=floor((j-431A)/P)
U_G(A)=min(U_v(A),U_j(A))
N_G=max(0,min(floor((v-D)/79),floor((j-P)/431)))
k_G=max {A in [1,N_G] : U_G(A)>z(A)}, or zero if empty.
K(p)=Pv-Dj
s=min(k_G,max(0,K(p)-1)).
```

Then the second count is exactly

```text
G(v,j)=sum_{A=1}^s floor((j-431A)/P)
      +sum_{A=s+1}^{k_G} floor((v-79A)/D)
      -S_alpha(k_G).                                    (G)
```

**Proof.** Fix `A`. The allowed positive `B` values satisfy `B>=floor(alpha A)+1`. Their upper bound is `U_F(A)` or `U_G(A)`, giving `max(0,U-z)` possibilities. The upper bounds are nonincreasing in `A`, while `z(A)` is nondecreasing, so contributing indices form the initial interval `1..k`. Each `k` is determined by monotone binary search. The `U_G` upper bound switches at a single exact coordinate: since `aP-cD=1`,

```text
(v-aA)/D <= (j-cA)/P
  iff P*v-D*j <= (aP-cD)*A
  iff K(p)<=A.
```

Taking floors preserves the `min` identity, so indices `A<K(p)` use `U_j` and indices `A>=K(p)` use `U_v`. This proves (F) and (G).

Every sum `sum_{A=L}^R floor((x-yA)/m)` is an integer Euclidean floor sum, including negative coefficients via Euclidean quotient/remainder normalization. `S_alpha(n)` can also be computed by rational Euclidean floor sums **with a finite exact certificate**, as follows.

### Constructing the irrational floor-sum oracle

The ratio `alpha` is irrational, because a rational value would imply `r=(431+P*alpha)/(79+D*alpha)` rational, contradicting the prime-factor proof for `r` in `PROOF.md`.

Construct strict rational intervals `r_-<r<r_+` from the atanh power series with rigorously bounded tails. The increasing fractional-linear transform

```text
alpha(r)=(79r-431)/(P-Dr)
```

gives rational endpoints `alpha_-<alpha<alpha_+`. For any required finite `N`, compute the two rational floor sums

```text
S_-(N)=sum_{A=1}^N floor(A*alpha_-)
S_+(N)=sum_{A=1}^N floor(A*alpha_+).
```

If `S_-(N)=S_+(N)`, then every individual floor `floor(A*alpha)` for `1<=A<=N` equals its endpoint floors, because their differences are all nonnegative and their total is zero. Hence **one equality of two exact rational floor sums certifies the entire irrational prefix without iterating its A values**. If the sums differ, refine the atanh interval and repeat. Since `alpha` is irrational and `N` is finite, each `A*alpha` has a positive distance to the nearest integer, so this process terminates. Use `N=max(N_F,N_G)` (or any proven upper bound) once per query, then perform (F) and (G).

For fixed certified precision, the remaining operations are logarithmically many binary-search steps and Euclidean floor sums. Bit complexity includes the arbitrary-precision integers and any required refinement of the certified log interval; we do not claim a uniform precision-independent runtime bound.

## Executed evidence

`VERIFY_FLOOR_SUM.py` implements the above with Python standard-library `Fraction`, bounded atanh, exact signed Euclidean floor sums, and monotone binary search. It checks exact `F,G` against **full inversion-direction enumeration** for horizons 4,910,647; 4,910,648; 7,365,717; 9,820,786; 9,821,296; 12,275,855; 25,000,000; and 100,000,000. It then executes exact, nonenumerative `F,G` queries at `H=10^9,10^12,10^15`. All checks passed (see `RUN_FLOOR_SUM.txt`).

For a fixed query `H=10^15,p=(H//3,H//2)`, the exact computed counts were

```text
F(H-|p|_1)=1,349,231,563,744,924
G(p)=17,002,579,759,343,968
rank_theta(p)-rank_L(p)=-15,653,348,195,599,044.
```

These are exact finite integer floor-sum results, not full enumeration at that scale.

## Observer semantics and follow-on

The original auxiliary S23/AV observer's full joint (1,4) count carrier, label-3 padding, and frozen source domain remain in force. BRC reuse classification `REUSE_APPLIED`: the result refines an exact ordered-readout operator with integer provenance, without quotienting the joint carrier. It supplies an exact count/rank algorithm for any finite `H` and preserves the separate empirical, review, lawful mother-model mapping, and capacity questions.

Next discriminating calculation: combine this rank oracle with exact prefix occupancy to classify all newly affected gaps at `H=2,455,579`; compare the seventh capacity plateau with its previous bound. A second route is an optimized certified `rank_L/select_L` interface exposing both sign and index with a shared floor-sum library.
