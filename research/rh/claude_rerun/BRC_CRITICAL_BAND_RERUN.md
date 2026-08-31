# BRC_CRITICAL_BAND_RERUN — Toda defect field and conjugate-pair cluster carrier

Task: `RS-RHR-CLAUDE-RH-RERUN-20260811`  
Researcher-ID: `RHR-9Q6M2K`  
Driver: `EM-DVR-7Q4K2C`  
Parent checkpoint: `f3a3a5c7077e2f94b7a53e2762ea54441a74e958`

Status:

`CRITICAL_BAND_REDUCED_TO_DEFECT_STABILITY / CONJUGATE_PAIR_RCC_NCC_DERIVED / TURAN_MOMENT_SHORTCUT_KILLED / RH_NOT_CLOSED`

This checkpoint continues the constructive BRC rerun. It does not claim RH and does not promote a formal continuum limit to a discrete theorem.

## 1. Exact Toda/Dodgson carrier

For normalized Xi coefficients let

`D_{r,k}=det[a_{k+j-i}]`, with `D_{0,k}=1`, and define

`q_{r,k}=D_{r,k-1}D_{r,k+1}/D_{r,k}^2`

when the denominator is nonzero.

Desnanot–Jacobi gives the exact identity

`D_{r+1,k}D_{r-1,k}=D_{r,k}^2(1-q_{r,k})`.

Thus, while the lower-rank determinants are positive,

`D_{r+1,k}>0 iff q_{r,k}<1`.

A sign token is therefore terminal-only: an active BRC branch must retain `q` (or an equivalent correlation carrier) because the next-rank transition depends on it.

Applying the same identity at `k-1,k,k+1` yields the exact local dynamics

`q_{r+1,k} = (q_{r,k}^2/q_{r-1,k}) * ((1-q_{r,k-1})(1-q_{r,k+1})/(1-q_{r,k})^2)`.

The initial rows are `q_{0,k}=1` and `q_{1,k}=a_{k-1}a_{k+1}/a_k^2`.

## 2. First-failure NCC

If ranks through `r` are positive locally and the next update fails, `q_{r+1,k}>=1`. The predecessor must satisfy

`((1-q_{r,k-1})(1-q_{r,k+1}))/(1-q_{r,k})^2 >= q_{r-1,k}/q_{r,k}^2`.

Equivalently,

`Delta_k log(1-q_{r,k}) >= log(q_{r-1,k}) - 2 log(q_{r,k})`.

This is a determinant-space **No-Completion Cone Certificate (NCC)**: a negative branch cannot appear without entering an explicit local defect cone. BRC should retain/refine only branches approaching this cone rather than globally refining the entire `(r,k)` lattice.

## 3. Logarithmic field

Inside the positive region set

`q_{r,k}=exp(-u_{r,k})`, `u_{r,k}>0`, and `F(u)=log(1-exp(-u))`.

Taking logarithms gives

`u_{r+1,k}-2u_{r,k}+u_{r-1,k} + F(u_{r,k-1})+F(u_{r,k+1})-2F(u_{r,k}) = 0`,

or

`Delta_r u + Delta_k F(u)=0`.

Because `F'(u)=1/(exp(u)-1)>0`, the continuum principal part is elliptic as long as the branch remains positive.

## 4. Smooth critical scaling has no macroscopic crossing mechanism

This is conditional on a smooth scaling limit. Suppose `r~Nx`, `k~Ny` and `u_{r,k}->V(x,y)` smoothly. Then the exact lattice equation formally yields

`V_xx + (F(V))_yy = 0`.

If `u_{1,k}~c/k`, `c>0`, the scale-invariant ansatz `V(x,y)=U(s)`, `s=x/y`, has boundary slope `U'(0)=c` and gives

`U'' + d/ds[s^2 d/ds F(U)] = 0`.

After one integration,

`U'(s) * (1 + s^2/(exp(U(s))-1)) = c`.

Hence every positive smooth branch satisfies

`U'(s)=c/(1+s^2/(exp(U)-1))>0`.

Starting from `U(0)=0`, the smooth self-similar critical profile cannot cross to `U<0`.

Interpretation: a hypothetical Xi failure in the critical regime must break smooth scaling by creating a lattice-scale defect, boundary layer, or correlation spike. The remaining theorem target is therefore discrete stability, not a macroscopic saddle sign change.

Status: `CONDITIONAL_SMOOTH_LIMIT_RESULT / NOT_A_DISCRETE_RH_THEOREM`.

## 5. Exact calibration: exponential PF baseline

For `b_k=1/k!`,

`D^(b)_{r,k}=det[1/(k+j-i)!]`.

Multiply column `j` by `(k+j)!`; row `i` becomes the monic falling-factorial polynomial `(k+j)_(i)`. The determinant is a Vandermonde determinant, so

`D^(b)_{r,k} = product_{j=0}^{r-1} j!/(k+j)! > 0`.

Its exact ratio field is

`q^(b)_{r,k}=k/(k+r)`,

hence

`u^(b)_{r,k}=log(1+r/k)`.

The continuum profile `U(s)=log(1+s)` satisfies the critical-limit equation above with `c=1` exactly. This calibrates the scaling calculation against a fully positive discrete solution.

## 6. Exact no-go: positive moments + all Turan inequalities are insufficient

The Xi coefficients have the architecture `a_n=M_n/(2n)!` with positive moments `M_n`. A tempting shortcut is that positive/Stieltjes moment structure plus the full strict Turan family might imply PF-infinity. It does not.

Take the positive finite measure

`4 delta_1 + 3 delta_3 + 2 delta_4 + delta_14`

with moments

`M_n = 4*1^n + 3*3^n + 2*4^n + 14^n`,

and put `a_n=M_n/(2n)!`.

For `Q_n=M_{n-1}M_{n+1}/M_n^2`, the moment identity

`M_{n-1}M_{n+1}-M_n^2 = sum_{i<j} w_i w_j (x_i x_j)^(n-1) (x_j-x_i)^2`

gives

`Q_n-1 <= (195/28)(2/7)^(n-1) < 7(2/7)^(n-1)`.

For `n>=4`, this is `<2/(2n-1)`. For `n=1,2,3`, exact arithmetic gives

`Q_1=74/35<3`,
`Q_2=14785/9583<5/3`,
`Q_3=10146325/8743849<7/5`.

Therefore for every `n>=1`,

`Q_n < (2n+1)/(2n-1)`.

Since

`a_{n-1}a_{n+1}/a_n^2 = Q_n * (2n)(2n-1)/((2n+2)(2n+1))`,

we obtain the complete strict Turan family

`a_{n-1}a_{n+1}/a_n^2 < n/(n+1)`.

Nevertheless exact Bareiss arithmetic gives

`D_{4,2} = -66408249317/365783040 < 0`.

Classification: `COUNTEREXAMPLE_NEGATIVE_BOUNDARY / EXACT_RATIONAL`.

So any successful critical-band argument must use Xi-specific structure stronger than positive moments plus Turan.

## 7. Zero-space BRC carrier: retain off-line quartets as conjugate pairs

The normalized Xi coefficient generating function is entire of genus zero. Write its zero-factor alphabet as

`G(z)=G(0) product_j (1+alpha_j z)`.

For a zeta zero `rho=1/2+delta+i gamma`, the corresponding `G` zero is

`w=4(delta+i gamma)^2`,

so `alpha=-1/w`. The functional-equation/conjugation symmetries naturally group a nonreal `G` zero with its conjugate. The BRC atom is therefore

`Y_rho={alpha, conjugate(alpha)}`,

not two independently forgettable poles.

It satisfies

`|alpha|=1/(4(delta^2+gamma^2)) <= 1/(4 gamma^2)`

and, using only `|delta|<1/2`,

`|arg alpha| = 2 atan(|delta|/|gamma|) <= 1/|gamma|`.

## 8. Exact conjugate-pair RCC

For a two-row partition `(a,b)`, `a>=b>=0`, and a conjugate pair

`Y={R exp(i theta), R exp(-i theta)}`,

the two-variable Schur/Weyl formula is

`s_(a,b)(Y) = R^(a+b) * sin((a-b+1)theta)/sin(theta)`.

At `theta=0` the positive limit is `(a-b+1)R^(a+b)`.

Thus the whole conjugate pair has an exact future observable and may be kept as one **Recoalescence Congruence Certificate (RCC)** state `(R,theta,(a,b))`.

## 9. Pair-unsafe NCC

Let `m=a-b+1`. For `0<|theta|<pi`, the pair factor is nonnegative whenever `m|theta|<pi`. Hence a negative pair contribution requires

`m > pi/|theta|`.

For a zeta pair this implies the necessary condition

`a-b+1 > pi |gamma|`.

For the rectangular Xi minor, `D_{r,k}=s_(r^k)({alpha_j})`, every partition allocated to one pair has width at most `r`, so `a-b+1<=r+1`.

Therefore if all zeros through height `H` are verified on the critical line and `r+1<=pi H`, every unverified pair is pair-safe. Iterating Littlewood–Richardson branching gives nonnegativity. This recovers the known low-rank sector strip in BRC cluster language.

More importantly, once `r>pi H`, not every branch becomes unsafe. A negative global branch must contain at least one pair allocation satisfying the extreme imbalance condition above.

## 10. Unsafe branch-local amplitude

For two variables,

`|sin(m theta)/sin(theta)| <= m`.

Thus

`|s_(a,b)(Y)| <= m R^(a+b)`.

If the branch is pair-unsafe, then `a+b >= a-b > pi|gamma|-1`. Since `R<=1/(4 gamma^2)` and `m<=r+1`,

`|s_(a,b)(Y_rho)| <= (r+1) * (4 gamma^2)^(-(pi gamma-1))`.

This is an extremely strong **branch-local** decay certificate. It is not yet a global proof: Littlewood–Richardson multiplicities, the positive-prefix Schur ratios, and accumulation over infinitely many pairs must still be charged.

The next zero-space target is therefore precise:

`total absolute unsafe LR branch mass < certified positive safe margin`.

## 11. Two concrete open bridges

### `TODA_STABILITY_BRIDGE`

Use the certified Xi smoothness of the initial coefficient-curvature row to prove that exact evolution cannot enter the first-failure defect cone in the critical region. This should use local/on-demand BRC refinement rather than one global quadratic Taylor collapse over an `O(r)` window.

### `PAIR_CLUSTER_DOMINATION`

Split the zero alphabet into a verified positive prefix and conjugate-pair RCC atoms. Recoalesce every pair-safe LR branch. Bound only the pair-unsafe NCC branches using their extreme imbalance and amplitude cost.

The two carriers expose different correlations and may be combined: Toda identifies where a determinant defect must appear; zero-pair branching identifies what spectral configuration could supply it.

## 12. Final classification

Proved/exact in this checkpoint:

- local `q` dynamics and first-failure NCC;
- logarithmic discrete Toda field;
- exact exponential baseline determinant and ratio solution;
- positive-measure + all-Turan counterexample;
- conjugate-pair Schur RCC;
- pair-unsafe imbalance NCC;
- branch-local unsafe amplitude bound.

Conditional only:

- smooth self-similar critical-limit positivity.

Open:

- discrete Xi Toda stability;
- global unsafe LR-branch domination;
- full critical-region cover;
- RH.

Return state:

`BRC_CRITICAL_CARRIER_FOUND / FIRST_FAILURE_DEFECT_LOCALIZED / CONJUGATE_PAIR_CLUSTER_CERTIFICATE_FOUND / TWO_CONCRETE_BRIDGES_OPEN / RH_NOT_CLOSED`.
