# R146 — Exact affine-periodic phase-fiber multiplicities and uniform discrepancy

Date: 2026-11-14 (Asia/Shanghai).
Scope: the **external scalar tied-phase S23 finite mechanical-word observer**, not a native Heartbeat-X6 cell or a certified observer-safe native quotient.
Status: AUTHOR-SIDE EXACT PROOF + REPRODUCIBLE FINITE REGRESSION; independent review NOT_REVIEWED.
Frozen science input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

Predecessors: R143 convex interval projection (`research_notes/brc_s23_av_r143_projection_residue_tail_20261114/PROOF.md` at `84863c21633962404531ecce89a5abab85e8162a`), R145 mass conservation (`research_notes/brc_s23_av_r145_fiber_mass_20261114/PROOF.md` at `58afcdede78599fd674626818171b99a1cc5155b`). The integer counting below is derived explicitly.

## 1. Exact definitions

Fix integers `m>=1`, `K>=2`; put `L=K-1`. For `0<t<1` define the length-m binary word
[
S_i^{(K)}(t)=lfloor(L+i+1)tfloor-lfloor(L+i)tfloor,qquad 0le i<m.
]
For a word `w=(w_0,...,w_{m-1})`, let `s_0=0`, `s_j=sum_{i<j} w_i`. Its open free-intercept slope support `(alpha,beta)` is given by
[
alpha=maxleft(0,max_{i<j}rac{s_j-s_i-1}{j-i}ight),qquad
eta=minleft(1,min_{i<j}rac{s_j-s_i+1}{j-i}ight).
]
When `alpha>=beta`, the word is not in the finite Sturmian language and its fiber count is zero. Otherwise let
[
u_alpha=min_{0le jle m}(s_j+1-jalpha),quad
ell_eta=max_{0le jle m}(s_j-jeta).
]
Write the reduced rational endpoints as `alpha=a/b`, `beta=c/d` with `b,d>=1` and define the integers
[
U=min_j[b(s_j+1)-ja],qquad V=max_j[ds_j-jc].
]
Thus `u_alpha=U/b`, `ell_beta=V/d`. Let
[
C_w(K)=#{Ninmathbb Z: exists,tin(0,1) 
lfloor Ltfloor=N, S^{(K)}(t)=w}.
]
The count retains the distinct phase-index `N`; it is neither the number of parameter values nor the number of distinct words.

## 2. R146.1 — Closed integer formula (all m,K)

For every finite Sturmian word `w`, define
[
A_L=rac{La-U}{b}=Lalpha-u_alpha,quad
B_L=rac{Lc-V}{d}=Leta-ell_eta.
]
Then the following nonnegative integer is **exact**:
[
oxed{C_w(K)=leftlceilrac{Lc-V}{d}ightceil-
                  leftlfloorrac{La-U}{b}ightfloor-1.}	ag{1}
]
Proof: for a freely chosen intercept `r`, strict floor-prefix inequalities are
`s_j<r+jt<s_j+1`, including `0<r<1` from `j=0`. Their feasible polygon is convex, and the linear functional `Lt-r` maps it onto exactly the open interval `(A_L,B_L)`: at slope `t`, the section is `ell(t)<r<u(t)`; `Lt-u(t)` and `Lt-ell(t)` are increasing in `t`. The tied-phase condition `r=Lt-N` is therefore equivalent to an integer `N` strictly between `A_L` and `B_L`. For each such `N`, the intersection of the strict prefix inequalities with the line `r=Lt-N` contains an open interval of `t` and yields one and only one nonempty phase block `I_{N,w}`. The number of integers strictly between two reals `A<B` is `ceil(B)-floor(A)-1`, proving (1). Right-continuous floor boundary observations are also attained on a nearby open interval and create no extra blocks. QED.

The endpoints and `U,V` require at most `O(m^2)` exact rational comparisons from a supplied word; (1) then uses a constant number of integer divisions on bit lengths polynomial in `m+log(K+1)`. No phase-event enumeration is needed.

## 3. R146.2 — Exact affine period for every word

Let
[
P_w=operatorname{lcm}(b,d),qquad
Q_w=P_w(eta-alpha)=rac{bc-ad}{gcd(b,d)}inmathbb Z_{ge1}.
]
For **every** `K>=2`:
[
oxed{C_w(K+P_w)=C_w(K)+Q_w.}	ag{2}
]
Indeed, replacing `L` by `L+P_w` shifts both `A_L` and `B_L` by integers `P_w a/b` and `P_w c/d`. Apply (1), use integer-shift covariance of floor and ceiling, and subtract. In particular, for every `j>=0`, `C_w(K+jP_w)=C_w(K)+jQ_w`. This is an *exact*, not asymptotic, affine quasipolynomial law in `K`. Since `P_w<=m(m-1)` for `m>=2` (both reduced denominators at most `m`, and equal denominator `m` contributes only period `m`), one immediately obtains the simple word-specific sufficient horizon `K>=P_w+2` for `C_w(K)>=1`, although the earlier R139/R143 bounds are often sharper.

## 4. R146.3 — Uniform, length-independent discrepancy constant

Put `delta=beta-alpha>0` and `h=u_alpha-ell_beta`. Then
[
oxed{0le hle1.}	ag{3}
]
To see this, on the support interval the lower intercept envelope `ell(t)` and the upper envelope `u(t)` obey `0<=ell(t)<u(t)<=1`; continuity gives the weak endpoint inequalities. Also `ell(t)` is nonincreasing, so
`u(alpha)>=ell(alpha)>=ell(beta)`; and `u(alpha)<=1`, `ell(beta)>=0`.

For `xinmathbb R`, let `{x}=x-floor(x)` and `eta(x)=ceil(x)-x`, both in `[0,1)`. From (1),
[
oxed{C_w(K)-Ldelta=h-1+{A_L}+eta(B_L).}	ag{4}
]
Consequently, for every `m>=1`, every Sturmian `w`, every `K>=2`:
[
oxed{-1le C_w(K)-L(eta-alpha)<2.}	ag{5}
]
This strengthens the R145/R143B size-dependent error constant `2m(m+1)+3` to a uniform constant 2. The correction in (4) is periodic with period dividing `P_w`. Finite tests show positive discrepancy `17/15>1`, so a blanket absolute-error bound of 1 would be false.

## 5. R146.4 — Explicit total-variation convergence rate

Let `W_m` be the full finite Sturmian language, `F_m=|W_m|`, and `S=sum_{win W_m}C_w(K)`. By R145,
[
(m+1)Lle Sle(m+1)L+inom m2,qquad
sum_w(eta_w-alpha_w)=m+1.
]
Define the empirical block distribution `p_K(w)=C_w(K)/S` and its support-width limit
`pi_m(w)=(eta_w-alpha_w)/(m+1)`. Writing `G=S-(m+1)L`, the identity
[
p_K(w)-pi_m(w)=rac{C_w(K)-Ldelta_w-pi_m(w)G}{S}
]
and (5), `0<=G<=binom(m,2)`, imply
[
oxed{|p_K-pi_m|_{m TV}
le minleft(1,rac{F_m+rac12inom m2}{(m+1)(K-1)}ight).}	ag{6}
]
Thus convergence is quantified for every finite `m` and every integer `K>=2`, with transparent dependence on the full output-language size. Here `TV=(1/2)sum_w|cdot|`.

## 6. Reproduction and exact validation

The accompanying `check_r146.py` uses Python arbitrary-precision integers and `Fraction`, generates all binary candidates for `m=1,...,11`, constructs their support exactly, and tests (1)–(6) at `L=1,2,7,31,10^55+123` plus other aggregate samples.

Actual observed totals: 636 Sturmian word records; 3,180 exact affine-period checks; 3,180 discrepancy checks; 2,544 mass/membership entries; 44 total-variation checks. Independent chronological reduced-rational partition over every `m=1,...,6` and `L=1,...,9` provides 54 phase-partition cases and 792 per-word crosschecks against (1). Largest observed absolute discrepancy in this finite regression is `17/15`. Verification output `R146_FIBER_AFFINE_PERIODICITY_PASS`.

The universal statements (1)–(6) rest on the proofs above; finite regression tests implementations, boundary conventions and arithmetic.

## 7. Forward scientific problem

Use the exact periodic error term (4) and the integer-bound support (1) to classify the remaining Farey-avoidant words near the conjectural critical coefficient
[
E(m)=(m-2)lfloor(m-1)/2floor+1.
]
The unresolved all-length question is whether `T(m)=E(m)` for every `m>=5`. The R145B shifted-extremal family has projected width (>1) at the boundary; a universal minimum-width or arithmetic-residue alternative remains to be proved. Maintain the actual frozen science pin and explicit external-scalar observer typing before any native X6 interpretation.
