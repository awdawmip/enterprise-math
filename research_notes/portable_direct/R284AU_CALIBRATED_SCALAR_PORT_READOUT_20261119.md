# R284AU — Calibrated finite-scalar readout for directed Port spanning trees

Date: 2026-11-19. **AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED**.
Lineage: R284AT (oriented spanning-tree reconstruction), R284AS, R284AQ and R284AR. Parent source: `research_notes/portable_direct/R284AT_SPANNING_TREE_DIRECTED_PORT_COMPLETENESS_20261119.md`, read Git blob `5d615eb33b5351a8e84878636a548887608fa9f4`. Preserve prior R284AR frozen science pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. This is auxiliary named Port-channel research, NOT native Heartbeat X6 evolution; P000 and the joint-observer preservation contract are unchanged. No CLAIM, Result, or independent review is implied.

## AU1. Exact scalar observer and calibrated input

Let `n>=2` and `C in Q_{>0}^{n*n}`. Available scalar queries are `F_C(d)=det(diag(d)-C)` and, for edges `(u,v)` of one fixed *oriented spanning tree*, `H_C^{uv}(d,z)=det(diag(d)-C-zE_uv)`. Each returns **one exact rational number**, not the full formal polynomial. Suppose a known positive integer `Q` makes `A=QC` integral and a known `B>=max |A_ij|`, `B>=1`. The entries are unknown; Q and B are calibration metadata. The observer may query zero or positive rational diagonal values and `z=1/Q`. Physical attainability, analog noise, and unknown-denominator inference are outside this model.

## AU2. Deterministic one-value coefficient extraction

For an integer polynomial `f(t)=sum_{j=0}^m a_j*t^j` with `|a_j|<=L` and integer `T>2L+1`, its top coefficient is uniquely
`a_m=nearest_integer(f(T)/T^m)`.
Indeed `|f(T)/T^m-a_m|<=L/(T-1)<1/2`. Zero top coefficients and signed coefficients are included, and the required rounding can be performed using integer arithmetic.

For `S subseteq [n]`, write `x_i(t)=0` for `i in S` and `x_i(t)=t` otherwise, `f_S(t)=det(diag(x(t))-A)`, `h_{S,uv}(t)=det(diag(x(t))-A-E_uv)` and `g_{S,uv}=h_{S,uv}-f_S`. Their degrees are at most `m=n-|S|`. The Leibniz expansion over permutations and the constant-versus-diagonal-t selection shows that every coefficient of f or h has absolute value at most
`K=n! * 2^n * (B+1)^n`.
Each coefficient of g is at most `2K`. Fix the **same** integer `T=4K+3` for every query. Then one f_S(T), or the difference of one h_S(T) and f_S(T), suffices to extract the exact `t^m` coefficient. Responses for `C` at `d=x(T)/Q`, `z=1/Q`, multiplied by `Q^n`, yield precisely these integer oracle values.

## AU3. Finite-scalar recovery theorem

**Theorem.** Every such C can be recovered entrywise from at most
[
N(n)=n+inom n2+(n-1)+2(n-1)(n-2)=O(n^2)
]
exact scalar determinant answers, using exactly the `n-1` directed intervention channels of a preselected oriented spanning tree. All chosen queries and returned rational values have bit lengths polynomial in `n`, `log(B+1)`, and `log Q`. No full-rank or genericity premise is required.

**Proof.** (1) The top coefficient for S={i} in f is `-a_ii`: n baseline readings recover all diagonals. (2) For S={i,j}, it is `a_ii*a_jj-a_ij*a_ji`, so another `binom(n,2)` baselines recover every strictly positive pair product `p_ij=a_ij*a_ji`. (3) For a tree edge probed in direction (u,v), the top coefficient of `g_{ {u,v},uv}` is `-a_vu`. Its baseline was read in (2); only one additional edited reading is needed, and `a_uv=p_uv/a_vu`. (4) For each tree edge (u,v) and third vertex w, the top coefficient of `g_{ {u,v,w},uv}` is
[
a_{vu}a_{ww}-a_{vw}a_{wu}.
]
One baseline and one edited reading supply the named path product `q_{uv|w}=a_vw*a_wu`. There are `(n-1)(n-2)` edge/third-vertex pairs; reuse repeated baseline queries when convenient. (5) Recover off-tree entries by induction from an arbitrary root x along the unique tree path: for a parent p and new y, the measured orientation of edge {p,y} provides either `a_yx*a_xp` or `a_px*a_xy`. Divide by the earlier known strictly positive factor and obtain its reverse entry from `p_xy`. This is exactly the named directed-path propagation proved in R284AT, and it recovers all of A, then C=A/Q. The stated call count adds these four observation classes. QED.

**Bit accounting.** `log2(T)=O(n log n+n log(B+1))`. Each scaled determinant is at most `n!*(T+B+1)^n` in absolute value, with polynomial bit length. Returned fractions have denominator dividing `Q^n`. The reconstruction has polynomially many exact arithmetic operations and polynomially bounded intermediate bit lengths. These are *response/query* bounds, not an experimentally measured total runtime or a claim about physical measurement precision.

## AU4. Lower bound with explicit scope

**Proposition.** If m fixed scalar determinant queries form a continuous map from an open set of real strictly positive n-by-n matrices into `R^m`, then entrywise injectivity implies `m>=n^2`.

**Proof.** For m<n², append zeros to the output to get a continuous injection from an open subset of `R^(n²)` into `R^(n²)`, whose image lies inside an m-dimensional coordinate subspace. Invariance of domain requires the image of an open subset under a continuous injection to be open, contradiction. QED.

This is a real-open **fixed-query continuous-sensing** lower bound. It is NOT an impossibility theorem about arbitrary discontinuous/adaptive rational encodings or a finite calibrated-height input population. AU3 achieves the same O(n²) scalar-query order in its separate calibrated rational model; constants and physical conditioning are open.

## AU5. Source fidelity / BRC scope

The compact large-base numeral preserves only because the calibration bound and exact rational oracle make coefficient extraction reversible. The proof keeps separately named single-site minors, ordered pair products, the signed cofactor difference and labeled directed two-step Port paths. It does not replace signed cancellation by positive aggregate BRC mass. No six-axis source object is projected away: the measured matrix is an explicitly auxiliary algebraic observer, not an asserted X6 spatial or heartbeat dynamics.

## AU6. Reproduction, scope and next work

Companions: `R284AU_scalar_port_reconstruction_checker.py`, `R284AU_r1_calibrated_scalar_61case_verification_20261119.json`. Standard-library Python, arbitrary precision integers/`Fraction`, seed `28420261119`. Exact validation: 61 full recoveries (sizes n=2..6), arbitrary oriented spanning trees, strictly positive integer matrices including rank-one and singular, and the R284AR three-channel transpose-ambiguous witness; 1,643 total oracle evaluations. Each case asserts exact entry recovery, bound-respecting top-coefficient extraction, and the scalar-call upper bound. Largest observed T is 51 bits, largest determinant response 256 bits. Finite verification does not prove AU4 or analog robustness. Independent review remains NOT_REVIEWED.

Open: optimize the constant in N(n); derive bounded-d,z/noisy stability or sharp counterexamples; remove known Q,B; analyze zero/nonpositive edge cases and disconnected interventions; measure end-to-end bit complexity against R284AT full-polynomial and R284AP algorithms. Source publication, Activity, formal Claim/Result, and Review are separate status dimensions. A separately authored R284AU_exact_verification.json appeared concurrently in canonical main; its 208-case payload remains untouched, is not evidence generated by this 61-case checker, and is not conflated with this continuation.
