# PREFIX-711-R6 — Mean-aware exact Gamma-clock interval certificates, 192×192

Date: 2026-11-12 (Asia/Shanghai).
Scientific pin: \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d\` (frozen).
Parent: PREFIX-675, frozen BRC two-stream auxiliary observer global maximization.
Immediate dependencies: PREFIX-705 (monotonic survivor tails), PREFIX-700 (correct Erlang-maximum moments), PREFIX-710 (exact Gamma-clock kernel and correction of PREFIX-709).
Evidence grade: \`AUTHOR_RECOMPUTED / EXACT_INTEGER_GAMMA_KERNEL / UNREVIEWED / NOT_ADMITTED\`.

## Theorem 711.1: exclusion for all real q >= 2

Let the independent completed clocks have T_p | N_p=k ~ Gamma(k,1) and let Y(p,z)=max(T_p,T_z), with mu=E[Y], W=Var(Y) and V_q=q² W-q mu. The parameter square is D=[0,1/2]². The 189-row stopping-count law and the width predicate are exactly those of the scientific pin; this is the auxiliary observer, not a native-X6 slice replacement.

Fix e=(0,3/20) and the rational grid G=192. For each 0<=i,j<G, let
a_ij=(i/(2G),j/(2G)), h_ij=((i+1)/(2G),(j+1)/(2G)) and B_ij=[a_ij,h_ij].

Let m_ij=mu(a_ij), U_ij=E[Y(h_ij)²]-m_ij², and define for t in [0,1/2]:
L_ij(t)=W(e)-U_ij-t[mu(e)-m_ij].

Define R_all as the union of boxes for which the two exact rational strict comparisons L_ij(0)>0 and L_ij(1/2)>0 both hold.

**Finite exact certificate:** Exactly 28,724 of 36,864 ordered boxes satisfy both comparisons. For every x in R_all and every real q>=2, V_q(e)>V_q(x). The relative excluded area of the whole square is exactly

**28724/36864 = 7181/9216 = 77.9188368055...%**,

and the absolute area is 7181/36864 (the square has area 1/4).

## Theorem 711.2: further exclusion for 12 <= q <= 24

Let R_[12,24] be the union of boxes satisfying L_ij(1/24)>0 and L_ij(1/12)>0. The same exact integer kernel certifies **28,871** boxes, relative fraction **28871/36864 = 78.3175998264...%**, absolute area 28871/147456. For every x therein and every real q in [12,24], V_q(e)>V_q(x).

## Proof

PREFIX-705's frozen survivor-tail order yields stochastically nondecreasing T_p and, by independent coupling, Y(p,z) in each coordinate. Consequently both mu and E[Y²] are coordinatewise nondecreasing. On any closed B_ij we have
mu(x)>=m_ij>=0 and E[Y(x)²]<=E[Y(h_ij)²].

Hence W(x)<=U_ij and, for every t>=0,

[W(e)-t mu(e)]-[W(x)-t mu(x)] >= W(e)-U_ij-t[mu(e)-m_ij] = L_ij(t).

The RHS is affine in t. If both endpoint comparisons on [0,1/2] are strictly positive, it is strictly positive throughout; multiply by q² with t=1/q. The same argument on [1/24,1/12] proves the second claim.

The numerical counts, not the analytic inequality, are finite exhaustive exact-integer calculations from the attached checker. It evaluates each of the 189 survivor rows (9,529 nonzero count entries), the exact Gamma-survivor convolution kernel, and all 36,864 ordered boxes. All comparisons are strict integer cross-products, without a floating-point criterion. The checker independently reproduces the previous 26,445-box PREFIX-710 baseline at G=192 and the exact (0,0) Gamma moment.

## Exact Gamma moments and complete coverage

Writing s_n(p)=Pr(N_p>n) for n=0,...,188, the Gamma-clock survival is S_p(u)=exp(-u) sum_n s_n(p) u^n/n!. Set c_nm=binom(n+m,n)/2^(n+m+1). Then

mu(p,z)=sum_n s_n(p)+sum_m s_m(z)-sum_nm c_nm s_n(p)s_m(z),

E[Y²](p,z)=2 sum_n (n+1)s_n(p)+2 sum_m (m+1)s_m(z)-sum_nm (n+m+1)c_nm s_n(p)s_m(z).

The checker implements these using the common integer denominator R=(384^188)²*2^377 for the 192-grid. There are 192² ordered axis boxes. Symmetry of independent streams permits one triangular loop with off-diagonal multiplicity two; every ordered box is counted exactly once. The witness e=(0,3/20) is computed with rational arithmetic. Executed verification: ALL_CHECKS_PASS PREFIX711-R6.

## Improvement, scope and next unit

PREFIX-710's correct but mean-discarding criterion selects 26,445 boxes at the same resolution. The new all-q criterion adds 2,279 boxes without losing any earlier one: an extra 2279/36864 of the square (6.182183... percentage points). Restricting to 12<=q<=24 adds another 147 boxes. The change retains the lower mean bound mu(a_ij) when comparing the witness's mean penalty, under the same correct Gamma-clock observer.

This is author-computed and awaits independent review. Exact global optimization remains open. Next: refine the 8,140 uncertified boxes (all q>=2), or the 7,993 uncertified boxes (q in [12,24]), using this exact Gamma kernel with adaptive local derivative/Bernstein bounds; compare remaining regions with exact boundary and interior stationary loci.