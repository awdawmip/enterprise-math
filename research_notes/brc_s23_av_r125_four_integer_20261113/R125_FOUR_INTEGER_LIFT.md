# R125 — Fixed four-integer exact feasibility for the fully signed S23 AP observer

Date: 2026-11-13 (Asia/Shanghai). Author-side research after R124 `fc30c1b8f9eb06ac807091eb420c53c02f06d58d`, with frozen scientific input `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. The model is the original S23 auxiliary directed-circle observer; native X6 Cell/Link/Port event licenses and P000 are unchanged.

## Theorem: no explicit endpoint-phase atomization needed

Let `I=(l,h)` be a nonempty bounded open rational parameter interval whose *old-history* eligibility signature is fixed; `x,l,h` are rational. Let `a,c,j,N,d` be arbitrary signed integers, `d!=0`, and `m>=2`. New times form `t_i=N+i*d` for `0<=i<m`. Define

`Y_i=x+(N+i*d-j)theta`, `A={a theta}`, `C={c theta}`, and
`M_i(theta)=1[{Y_i} in [A,C)_directed]`, with coinciding endpoints denoting the empty arc.

Each prescribed m-bit vector has an **exact finite reduction to at most `2^(m+1)|P_m|+1` fixed-dimensional rational-integer feasibility systems**, each involving at most **four integer variables**. The `+1` is needed only for the all-zero bit vector at a coincident-endpoint parameter. `P_m` is the R121 arithmetic-progression floor-word vocabulary, of cardinality `1+sum_(r=1)^(m-1) (m-r) phi(r) = Theta(m^3)` (classical finite Sturmian-word count). All strict/weak endpoint semantics are preserved. An exact rational `theta` witness can be recovered from every feasible system.

For any fixed `m`, the feasibility decision and witness can be performed in bit complexity polynomial in the binary length of `x,l,h,a,c,j,N,d` using fixed-dimension integer programming. In particular the reduction generates no parameter cuts proportional to `|a|,|c|,|a-c|,|N|` or `|d|`. This is a complexity consequence of the fixed-dimensional integer programming theorem, not an assertion that the bounded enumerator supplied below implements that algorithm.

### Proof: four integer floors

Introduce exactly four integers

`p=floor(a theta)`, `r=floor(c theta)`, `n=floor(x+(N-j)theta)`, `k=floor(d theta)`.

They are constrained by the rational-affine weak/strict inequalities

`0<=a theta-p<1`, `0<=c theta-r<1`,
`0<=x+(N-j)theta-n<1`, `0<=d theta-k<1`.

The circular endpoints are now rational-affine `A=a theta-p`, `C=c theta-r`; crucially we no longer partition the parameter interval at their integer crossings. Split into the **three exact orientations** `A<C`, `A>C`, `A=C` using strict inequalities or equality.

For `A<C`, the allowed bit-1 segment is `[A,C)` and bit-0 segments are `[C,1)`, `[0,A)`. For `A>C`, bit-1 segments are `[A,1)`, `[0,C)` and bit-0 segment is `[C,A)`. Empty zero-width segments may be skipped. For `A=C`, every `M_i=0`; this exact equality branch contributes at most one special feasibility system, independent of the words.

For strict orientations, choose one of the at most two segments for each requested bit. Put `Y_0=n+alpha` and `d theta=k+beta` with `alpha,beta in [0,1)`. The exact floor identity from R121 gives

`floor(Y_i)=n+i*k+q_i`, `q_i=floor(alpha+i*beta)`, `q in P_m`.

For each chosen segment `[L_i(theta,p,r),U_i(theta,p,r))`, impose

`Y_i(theta)-U_i(theta,p,r)< n+i*k+q_i <=Y_i(theta)-L_i(theta,p,r)`.

All these inequalities, the four floor constraints, the orientation, and `l<theta<h` are **linear with rational coefficients** in one real unknown `theta` and four integers `p,r,n,k`. Every genuine `theta` yields one of the systems. Conversely, any feasible system has each `Y_i-(n+i*k+q_i)` in its chosen segment inside `[0,1)`, hence those integers are the genuine `floor(Y_i)` and each requested original bit holds. The orientation equality branch handles all isolated coincident endpoints and the globally equal case `a=c`.

Eliminate only `theta` using rational Fourier–Motzkin: each lower and upper affine bound is compared, strictly if either contributing endpoint is strict. Equality constraints are two weak inequalities. The resulting system has `O(m^2)` rational-affine inequalities in **four integer variables**. Multiplying by positive denominators converts every rational strict integer inequality to a weak inequality with the integer right-hand side reduced by 1. All coefficients retain polynomial bit length under this single-variable elimination. The integers are bounded by floors of the endpoint ranges, hence the projected system is bounded. A feasible integer vector recovers an exact rational `theta` from the original lower/upper bounds (midpoint if there is slack, common rational value if both tight and weak).

For each strict orientation there are at most `2^m` segment choices and `|P_m|` words; the equality branch adds one if all bits are zero. Thus one pattern uses at most `2^(m+1)|P_m|+1` four-dimensional systems. With `m` fixed, a standard exact fixed-dimensional integer programming algorithm gives polynomial bit complexity in all input coefficient lengths. To enumerate all attained bit vectors, multiply this bound by the at most `2^m` patterns; explicit output and witness length remain charged separately. QED.

## Exact computational cross-check

The standalone verifier `check_r125.py.gz.b64` decodes beside the R124 verifier `check_r124.py.gz.b64` (both required in the same directory); run `python check_r125.py`. The solver used for validation **exhaustively enumerates bounded p,r,n,k** and a finite overcomplete floor-word set on small random inputs, eliminates theta by exact Fraction intervals with strict/weak endpoint flags, and compares every attained m=2 or m=3 vector to an independent full affine-cut atomization.

Deterministic seed `1252026`: 30 random fully signed instances, 30 complete open-interval signature-set comparisons, 177 exact rational witnesses, 7,104 four-integer/word trials, 1,714 independent full critical atoms, 24 isolated coincident-endpoint cases; 10 large signed coefficient/time **forward** identities. All assertions passed, `R125_FOUR_INTEGER_REDUCTION_PASS`. This tests the reduction under the listed bounded inputs, not Lenstra implementation or full bit-complexity performance.

## Required predecessor correction discovered during R125

R123's `PROOF.md` and accompanying `check_r123.py` used the proposed bound `floor(min(f(l),f(h))) <= floor(f(theta)) <= ceil(max(f(l),f(h)))-1`. This **fails for a constant integral affine phase** `f(theta)=z in Z`: the bounds become `z<=floor(f)<=z-1`. A concrete original-model counterexample is `x=0,N=j=a=0,c=1,d=1,m=2,I=(0,1)`, for which every `theta in (0,1)` has signature `(M_0,M_1)=(1,0)`, but R123's original code reports all four signatures absent.

The safe corrected bound for every affine phase on a bounded rational interval is

`floor(min(f(l),f(h))) <= floor(f(theta)) <= floor(max(f(l),f(h)))`.

It may include an unattained endpoint floor, which the actual strict parameter constraints discard; its range is finite and its endpoints have polynomial binary length. Replacing exactly two upper-bound expressions in the copied R123 verifier recovers witness `theta=1/2` for signature `10`, while the original complete regression still returns `R123_FLOOR_SUM_LATTICE_PASS` (1,500 signed floor-sum tests, 800 random polygon tests, 680 S23 signature queries among other checks). This repairs the *bound and finite enumeration implementation* without altering R123's floor-sum lemma. Reproduction, exact old/new outputs and a minimal patch are in `R123_BOUND_CORRECTION.md`, `fix_r123_floor_bounds.patch`, `verification_r123_correction.json`. Preserve R123 original immutable source as historical evidence.

## Next frontier

R126: implement a genuine fixed-dimensional integer solver or a structure-specific exact 4D reduction for these signed S23 systems. Measure the end-to-end resource cost of avoiding `a,c` phase cuts; add adversarial tests with `a,c` hundreds of digits, exact endpoint equality, and singular weak/strict facet intersections. Resolve the R123 correction in any implementation that reuses the old file. Formal Task CLAIM and independent mathematical review retain their separate authorization.
