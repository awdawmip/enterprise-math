# R629｜signed BRC Newton 漂移差分探针：多项式背景下的最少观察数与方向恢复

Date: 2026-11-08. Status: **AUTHOR_SIDE_EXACT_PROOF / UNREVIEWED / NOT_ADMITTED**.
Parent: R628 @ `5c711f09b8420505d29be363003448d4c1d7469e`. Frozen scientific input: R462 @ `18783e01e3646c72b7aab3b16d3f565e83e6446f`, theta=0; signed K generator blob `7fa7a762f758b30c6090468ac43487daa34abad8`.
P000: native X6 six signed spatial axes; the schedule index k below is a **probe index**, not branch-grade, a seventh spatial coordinate, or a physical heartbeat clock. The actual heartbeat program remains unspecified in the read Source (`fixed_heartbeat_program=null`). Mother objective: a source- and future-operation-faithful bridge between signed BRC and the native X6 joint state.

## 1. Exact model and probe language

Write `P_j=K_(2j-1)`, `M_j=K_(2j)`, `D_j=P_j-M_j` (j=1,...,6), over `Z[t]`. The frozen source gives
`nu_t(D_j)=2j-2` and leading coefficients `c=(2,-8,6,106,83,9)`.
Let `pi` be a permutation of the six axis labels. Each spatial axis x has a **fixed across its scan** nonzero gain `A_x in Z[[t]]`, and an independently chosen nuisance function
`H_x(k)=sum_{l=0}^h B_(x,l) * binom(k,l)`, `B_(x,l) in Z[[t]]`, with h a fixed nonnegative integer. This is the integer-valued Newton-polynomial drift class on the integer probe index; six axes may have unrelated nuisances and gains.

For each axis use the alternating sign-selectable BRC probes
`Y_(x,k)=A_x P_(pi^-1(x))+H_x(k)` for even k and
`Y_(x,k)=A_x M_(pi^-1(x))+H_x(k)` for odd k.
Observe all k=0,...,h+1, either as complete formal series or their d-jets in `Z[[t]]/(t^(d+1))`. Two candidate explanations can separately choose their nuisance coefficients and gains. These are auxiliary signed source observations over the existing native X6 axis labels; the underlying ordered path, source ID, signed weights, multiplicity, branch-grade and separately typed time remain available as joint state until an operation-safe quotient is proved.

## 2. Exact finite-difference lemma

Let `r=h+1>=1`, `Delta f(k)=f(k+1)-f(k)`. Since `Delta binom(k,l)=binom(k,l-1)`, one has `Delta^r H_x(0)=0` exactly. For the alternating P/M signal,
`sum_(k=0)^r (-1)^(r-k) binom(r,k) S_j(k)=(-1)^r 2^(r-1) (P_j-M_j)`.
Consequently

```
Delta^(h+1) Y_x(0) = (-1)^(h+1) 2^h A_x D_(pi^-1(x)).
```

This identity is in `Z[[t]]`; it requires neither rational interpolation nor division by the finite-difference scale. The six-axis nuisance coefficients cancel exactly, including their signed BRC coefficient content.

**Integral Newton interpolation lemma.** Given any h+1 values `z_0,...,z_h in Z[[t]]`, there is exactly one degree-<=h Newton polynomial `N(k)=sum_(l=0)^h b_l binom(k,l)` matching them: `b_l=Delta^l z_0`. All coefficients remain in `Z[[t]]`. For two sequences of h+2 observations, equality of their order-(h+1) finite differences is equivalent to the existence of a degree-<=h Newton nuisance adjustment making the entire observation sequences equal. Proof: interpolate the first h+1 differences and compare the final value; its residual is precisely the top finite difference.

## 3. Theorems: sharp identifiability and sample count

**Theorem A (valuation-band iff).** Fix h>=0 and integers 0<=a<=b. Allow arbitrary nonzero gains with `a<=nu_t(A_x)<=b`. At **h+2 alternating probes per axis**, if `b-a<=1`, the whole orientation `pi in S6` is uniformly recoverable from d-jets if and only if `d>=b+8`. If `b-a>=2`, distinct orientations with admissible nonzero polynomial gains and Newton nuisances give **identical complete series** for all h+2 probes.

*Proof.* The finite difference has valuation `nu(A_x)+2j-2`. For width<=1, the valuation bands `[a+2j-2,b+2j-2]` are disjoint, and at `d=b+8` all j<=5 have appeared. A remaining invisible axis must be j=6. For d<=b+7, exchange j=5 and j=6 with gains `t^b`. Their top-difference jets are both zero. The interpolation lemma supplies a degree-<=h Newton background correction so that all h+2 observed jets agree. For width>=2 write `D_5=t^8 U_5`, `D_6=t^10 U_6`, `U_5(0)=83`, `U_6(0)=9`. Choose `A_5=t^(a+2) U_6`, `A_6=t^a U_5`; then `A_5 D_5=A_6 D_6` as full integer polynomials. Exchange j=5 and j=6 on two axes and interpolate the nuisance difference. The finite-difference lemma makes all h+2 full outputs equal. Other axes stay unchanged. This witnesses both directions exactly.

**Theorem B (normalized leading gains).** If `0<=nu_t(A_x)<=R`, and each leading gain coefficient is +1 or -1, then h+2 probes per axis recover all orientations uniformly at **optimal jet depth** `d=R+8`, without a narrow common valuation band.

*Proof.* The first nonzero coefficient in the top difference has absolute value `2^h |c_j|`; the six values `|c|=(2,8,6,106,83,9)` are pairwise distinct. At d=R+8, j<=5 have appeared and the sixth axis follows from the permutation constraint if unseen. At d<=R+7, exchanging j=5,6 with gains `t^R` yields equal top-difference jets, and the integral interpolation lemma gives identical complete measured d-jets. Thus the threshold is sharp.

**Theorem C (minimal number of probes for arbitrary degree-h drift).** For this nuisance class, at most h+1 measurements per axis can be made identical across **all 720 orientations**, even if the full formal series are observed and gains are fixed to `t^a` (or to 1). Hence h+2 probes per axis are the smallest possible for a uniform recovery guarantee in Theorem A's narrow-band case or Theorem B's normalized case. Proof: for each candidate orientation and every axis, Newton-interpolate `-A_x S_(pi^-1(x))(k)` on the observed k=0,...,h; the resulting allowed H_x makes each of these observations zero. This is an exact construction with integer series.

Examples: constant background h=0 uses 2 probes (R628); affine Newton drift h=1 uses 3 probes and `Y_0-2Y_1+Y_2=2A(P-M)`; quadratic drift h=2 uses 4 probes and `Delta^3 Y_0=-4A(P-M)`. Total scalar signed source readings are `6(h+2)`. The direction result concerns reconstructing the six-axis orientation; source provenance and future X6 updates retain their separate observer-preservation obligations.

## 4. Test coverage and route

`R629_VERIFY.js` reproduces the frozen signed K generator as used in R628 and computes with BigInt integer polynomials. Exact checks at h=0,...,4 and all 720 permutations cover the difference identity, two valuation bands, two normalized gain families, h+1-probe zero-output construction, low-depth collision and wide-band complete polynomial collision. The accompanying JSON records the executed counts. A separate local Python arbitrary-integer implementation independently reproduced the 36,050 test count and PASS with the same valuation/leading arrays (not used for a universal inference). All-h and all-d results follow the proofs above.

**Reuse resolution:** `T0_BRC=REUSE_APPLIED` (frozen signed K); `T6_OPERATION_SAFE_QUOTIENT=REUSE_APPLIED` (specified observer/future-operation scope); R628 paired-difference law is extended to the Newton nuisance class, without proposing a new top-level toolbox family. Exact finite differences act on **probe readouts**, not as a substitute for the source BRC update or a physical time propagator.

**Next:** Inspect any actual Source-registered native internal-field sign-selectable observation. Determine whether a bounded Newton-degree nuisance and fixed-within-scan gain are justified by the operation's input/output contract. If yes, prove an operator-level commuting square and a future-operation descent certificate; if no, preserve the precise failing temporal/source coupling and test a source-tagged/calibrated repair. The Source's `fixed_heartbeat_program=null` leaves the physical-time evolution correspondence to be established.
