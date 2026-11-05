# D25 — Clausen tangent-square first jet and exact quadratic denominator defect

Date: 2026-11-06. Scope: finite-field algebra for every prime q >= 5. Status: AUTHOR-DERIVED / EXACT ALGEBRA / PORTABLE / 47-PRIME EXACT CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT.

Mother Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Preserve original scientific input pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. This is a new algebraic auxiliary route to the signed-carry observation, not a proof of the frozen native LIFT target.

## 1. Definitions

Let q >= 5 be prime, epsilon = 1 for q = 1 mod 6, epsilon = -1 for q = 5 mod 6, m=(q-epsilon)/6 and delta=(1-epsilon)/2. Put a=2m-delta, b=3m-delta, c=4m-delta. Then a+c=q-1 and b=(q-1)/2. Work in F_q with a formal parameter t and a polynomial variable z. For 0 <= j < q all factorial/rising-factorial denominators used below have invertible constant term.

Write
[
V_j(t)=(-a-t)_j(a+1-t)_j(1/2-t)_j,quad
M_j(t)=rac{V_j(t)}{j!^2(1-3t)_j},quad
C_j(t)=rac{V_j(t)}{j!(1-t)_j(1-2t)_j}.
]
Here `(x)_j` is the rising factorial and `[t^r]` denotes an ordinary Taylor coefficient. Because `-b=1/2` and `-c=a+1` in F_q, `M_j(t)(1/2)^j` is precisely the previous D25 directional-jet term
`(-1/2)^j product_{s=a,b,c}binom(s+t,j)*j!/(1-3t)_j` in F_q[[t]].

Define `G_t(z)=sum_{k=0}^{q-1} g_k(t) z^k`, where
[
g_k(t)=rac{((-a-t)/2)_k((a+1-t)/2)_k}{(1-t)_k k!}.
]
Let `T_{<q}` truncate a formal z-series to degrees <q. Set `D=1+6z d/dz`.

## 2. Theorem A: exact first-jet tangent square, and second-jet defect

For each `0 <= j < q`,
[
M_j(0)=C_j(0),quad [t]M_j(t)=[t]C_j(t),
quad [t^2](M_j-C_j)=2 H_j^{(2)} M_j(0),
]
where `H_j^{(2)}=sum_{k=1}^j k^{-2}` in F_q (H_0^{(2)}=0). In addition, the classical Clausen identity, coefficientwise over F_q[[t]], gives
[
sum_{j=0}^{q-1}C_j(t)z^j=T_{<q}igl(G_t(z)^2igr).
]
Consequently
[
sum_{j<q}[t]M_j(t)z^j=
T_{<q}!left(2G_0(z)dot G(z)ight),
]
and the precise second-jet obstruction to extending the *same* squared expression is
[
[t^2]sum_{j<q}(M_j-C_j)z^j
=2sum_{j<q} H_j^{(2)} M_j(0)z^j.
]
Here `G_0=G_t|_{t=0}`, `dot G=dG_t/dt|_{t=0}`. These are identities of polynomial coefficients modulo q and do not equate an untruncated infinite hypergeometric sum with a finite sum at z=1/2.

**Proof.** The ratio is independent of the three numerator parameters:
[
rac{M_j(t)}{C_j(t)}=
rac{(1-t)_j(1-2t)_j}{j!(1-3t)_j}
=1+2H_j^{(2)}t^2+O(t^3).
]
Indeed the log coefficient of t is zero (1+2-3=0); at t^2 it is `(-1^2-2^2+3^2)H_j^{(2)}/2=2H_j^{(2)}`. This derivation works even where a numerator rising factorial vanishes at t=0. Multiplying the ratio by C_j proves all three coefficient assertions. Clausen's rational formal identity
`2F1(A,B;A+B+1/2;z)^2 = 3F2(2A,2B,A+B;2A+2B,A+B+1/2;z)`
applies with `A=(-a-t)/2`, `B=(a+1-t)/2`, `A+B=1/2-t`. Its denominator parameters are `1-2t,1-t`. For j<q these coefficients reduce legitimately to F_q[[t]], yielding the truncated statement.

## 3. Theorem B: no truncation remainder in the target class q=6m+1

For q=6m+1 (including every frozen target prime q=13 or 19 mod 24), `G=G_0` has degree <= m, and `dot G` has degree <= 2m over F_q. Therefore `G^2` has degree <=2m and `2G dot G` degree <=3m<q. The first-jet formulas of Theorem A hold as ordinary polynomial identities *without* T_{<q}.

To see the derivative bound, the first upper parameter of g_k(t) is `-m-t/2`; its rising factorial has one zero at t=0 for k>=m+1. The second parameter `m+1/2-t/2` reduces to `4m+1-t/2` in F_q; its rising factorial adds a second zero for k>=2m+1. Thus `[t]g_k(t)=0` for k>=2m+1, while `g_k(0)=0` for k>=m+1.

At z=1/2 define the previously used observations
[
Z=sum_{j<q} M_j(0)2^{-j},quad
L=sum_{j<q}(6j+1)M_j(0)2^{-j},quad
S=sum_{j<q}(6j+1)[t]M_j(t)2^{-j}.
]
Then, writing `G'=dG/dz` and `dot G'=d(dot G)/dz`,
[
oxed{Z=G^2,quad L=G(G+6G'),quad
S=(2G+6G')dot G+6Gdot G',}
]
all evaluated at z=1/2.

On the established first-digit locus L=0, this gives a genuinely different branch expression:
[
oxed{S=6G'dot Gquad	ext{if }G=0;qquad
S=G(dot G+6dot G')quad	ext{if }G
e0.}
]
This decomposes the signed-carry parameter tangent into a Gauss factor and an inhomogeneous Gauss tangent with exactly specified branch behavior. Under the earlier D25 input identity `B=6Z-S` when L=0, the same formulas give B branch by branch.

## 4. Consequence for the smallest open certificate

The earlier author-side conditional `Theta_q=W_q/q-Z+S/6` (assuming q divides W_q and the compatible L=0 source conditions) becomes, for q=6m+1:
[
Theta_q=
egin{cases}
W_q/q+G'dot G,&G=0,\
W_q/q-G^2+(G/6)(dot G+6dot G'),&G
e0.
end{cases}pmod q
]
Thus the proposed universal `Theta_q=0` reduces to two precise Gauss-jet evaluations. The actual `W_q/q` evaluation, and its connection to the original native divided-power H0/B0 and semilinear Frobenius/kappa, remain open at this source boundary. Independently, the quadratic defect `2H_j^{(2)}M_j(0)` identifies the extra term for a second-parameter-jet route rather than silently extending first-order Clausen equivalence.

## 5. Exact finite checks and observer/provenance

A standalone Python finite-field verifier compared `M_j,C_j`, the first two Taylor jets of `G_t(z)^2`, and the quadratic defect **coefficient by coefficient** for 47 primes: all primes 5<=q<=211, plus q=373 and q=1009. All passed. It also verified the untruncated q=6m+1 Gauss factorization and its branch formulas. Exact sample `(q,Z,L,S,weighted quadratic defect)`:
`(13,0,0,7,3)`, `(19,0,0,13,18)`, `(373,0,0,367,239)`, `(1009,482,0,868,210)`.
Computation uses modular inverses only for 1,...,q-1. No floating error or numerical truncation assumption. This finite test corroborates the proof, not an all-prime acceptance decision.

This preserves D25's observer labels (Z, L, directional S, regular/single-carry origin) and records the operation t-derivative separately from the spatial z-derivative. Frozen scientific Source pin is unchanged. The original 373 native H0/B0, [X]U mod373^2, semilinear normalization eta, kappa, Delta_p-R_p and independent review remain the mother objective's native obligations.

Author-side repository publication is NOT native session/CLAIM/OPEN, a Source canonical checkpoint, a native experiment, Result or mathematical admission.
