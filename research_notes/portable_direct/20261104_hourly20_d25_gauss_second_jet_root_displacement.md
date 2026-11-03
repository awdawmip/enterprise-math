# D25 — All-residue Gauss second-jet endpoint and Hensel displacement

Date: 2026-11-04 (+08). Status: **AUTHOR-DERIVED / ALGEBRAICALLY PROVED IN STATED SCOPE / FINITE EXACT CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. This is portable author evidence, not a native CLAIM/OPEN, Source checkpoint, Result, independent review, or P000 change.

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; immutable scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Stable Research logical lane `chatgpt-research-hourly-enterprise-math-20260923`, disjoint from maintenance `chatgpt-hourly-enterprise-math-20260921`. Prior input: `research_notes/portable_direct/20261104_hourly20_d25_gauss_endpoint_derivative_defect.md` at verified source; retain its exact original Gauss objects and parameter-jet/Jacobi program.

## 1. Original observers and exact two-jet theorem (new algebraic result)

For all integers `n>=1`, define over Q
[
c_k=rac{(1/8)_k(3/8)_k}{(k!)^2},quad
F_n(z)=sum_{k=0}^{n-1}c_kz^k,quad
G_n(z)=F_n(z)+16zF_n'(z),quad z_0=rac19.
]
All identities in this section are exact rational identities (not asymptotic expansions). Let
[
E_n(z)=-rac{16n^2c_nz^{n-1}}{1-z},quad
A(z)=rac{1+7z}{16z(1-z)},quad
B(z)=rac{5z-1}{16z(1-z)}.
]
The truncated Gauss ODE (previously proved) yields the *inhomogeneous two-observer first-order system*
[
oxed{quad F_n'(z)=rac{G_n(z)-F_n(z)}{16z},qquad
G_n'(z)=A(z)G_n(z)+B(z)F_n(z)+E_n(z).quad} 	ag{1}
]
It is valid for `z != 0,1`. Importantly, the omitted `k=n` source is the explicit forcing `E_n`.

Define two observed defects at `z_0`:
[
D_1(n)=G_n'(z_0)-rac98G_n(z_0)+rac9{32}F_n(z_0),
]
[
D_2(n)=G_n''(z_0)+rac{1701}{512}G_n(z_0)-rac{2673}{512}F_n(z_0).
]
Then the exact **second-jet endpoint theorem** is
[
oxed{D_1(n)=-18n^2c_n9^{1-n},}	ag{2}
]
[
oxed{D_2(n)=-rac{81}{2}(4n-3)n^2c_n9^{1-n}
=rac{9(4n-3)}4D_1(n).}	ag{3}
]
Thus the derivative-data transport has an exact p-dependent *homogeneous elimination* `D_2(n)-9(4n-3)D_1(n)/4=0`, while the physically sourced value of each defect is fixed by the omitted end coefficient. Both equations are valid for every positive integer `n`.

**Proof.** The coefficient recurrence `(k+1)^2 c_(k+1)=(k+1/8)(k+3/8)c_k` gives `z(1-z)F_n''+(1-3z/2)F_n'-3F_n/64=-n^2c_n z^(n-1)`. Substitute `F_n'=(G_n-F_n)/(16z)` to get (1). Differentiating (1), substituting `F_n'`, and collecting produces
[
G_n''=
rac{39z^2+13z-4}{64z^2(1-z)^2}G_n+
rac{15z^2-5z+2}{32z^2(1-z)^2}F_n+
left(rac{n-1}{z}+rac{1}{1-z}+A(z)ight)E_n.
]
At `z=1/9` the first coefficients are `-1701/512` and `2673/512`, the last multiplier is `9(4n-3)/4`, and `E_n(1/9)=-18n^2c_n9^(1-n)`. This proves (2)-(3).

## 2. Universal residue-class endpoint coefficients (new extension)

For each prime `p>=5`, take `n=p`. If `a,b` are the unique integers `0<=a,b<p` for which `8a+1` and `8b+3` are divisible by `p`, respectively, put `m=(8a+1)/p` and `h=(8b+3)/p`. The pairs `(m,h)` for `p mod8=1,3,5,7` are `(1,3),(3,1),(5,7),(7,5)`. Removing the unique multiple of `p` from each rising factorial and applying Wilson gives
[
c_pequivrac{mh}{64}=rac{d_p}{64}pmod p,qquad
d_p=egin{cases}3,&pmod8in{1,3},\35,&pmod8in{5,7}.end{cases}
]
Since `9^(p-1)=1 (mod p)`, equations (2)-(3) yield the complete third-digit endpoint pair
[
oxed{D_1(p)equiv-rac{9d_p}{32}p^2pmod{p^3}},	ag{4}
]
[
oxed{D_2(p)equivrac{243d_p}{128}p^2pmod{p^3}}.	ag{5}
]
For every prime `p>=11`, both displayed defects have exact valuation 2, because the numerator `d_p` is a p-unit. At `p=5,7`, `d_p=35` and the defects vanish modulo `p^3`. The earlier derivative source `-315p^2/32` is precisely the `p mod8=5,7` branch of (4); equation (5) is the new *second-derivative/curvature endpoint*.

## 3. Hensel root-displacement witness (proved local statement; global residue assignment tested)

For a prime `p>=5`, all coefficients of `F_p` and `G_p` belong to `Z_p`. For either observer `J_p in {F_p,G_p}`, if `J_p(z_0)=0 (mod p)` and `J_p'(z_0)` is a p-unit, the unique root modulo `p^2` in `z_0+pZ_p` is `z_0+p delta_J`, where
[
oxed{delta_Jequiv-rac{J_p(z_0)}pigl(J_p'(z_0)igr)^{-1}pmod p.}	ag{6}
]
This follows by Taylor expansion modulo `p^2`. The previous first-root transversality theorem establishes the unit-derivative hypothesis for the observed chosen F or G zero at `z_0`. The candidate `J_p(z_0)=0 (mod p^2)` is thus equivalent, **conditional on the first-digit zero**, to vanishing of the computable Hensel displacement. No CM/Jacobi universal root-class assertion is inferred from the finite test.

## 4. Executed exact computation (new range)

The companion compact standard-library Python script evaluates `t_k=c_k9^(-k)` for every integer `0<=k<p` by `t_(k+1)=t_k(8k+1)(8k+3)/(576(k+1)^2)` in `Z/p^3Z`, retaining weights `1, 16k+1, 9k, 9k(16k+1), 81k(k-1)(16k+1)`. It tests (4),(5), the exact (3) elimination, and the Hensel shift using only units `k<p`. It ran successfully for all **1227 primes 5<=p<=10000** (all four mod-8 classes), and **622 primes** in the original `p mod8=5,7` sector; among those, 309 F-selected primes `p mod24=13,23` and 313 G-selected primes `p mod24=5,7` had zero Hensel displacement and selected factor zero modulo `p^2`. This increases the old 157-prime root assignment test to 622 instances, without upgrading it to a theorem.

Sample tuples `(p,selected,F mod p²,G mod p²,selected derivative mod p,D1/p² mod p,D2/p² mod p)`:
`(13,F,0,137,8,6,5)`,
`(23,F,0,243,3,11,12)`,
`(29,G,287,0,9,11,20)`,
`(373,F,0,110861,45,165,285)`,
`(2053,F,0,2845091,1205,1979,1526)`.

This is exact finite arithmetic with explicit domain and no native experimental equivalence claim. The first-order and second-order endpoint forcing are verified against the *same original finite Gauss sum*, not fitted independent data.

## 5. Observer/provenance and next action

BRC interface: retain `(p,k,z,alpha,beta,c_k,t_k,F,G,F',G'',E_p)` with `p`-adic valuations, original finite index, signed endpoint forcing, derivative observer, and residue class. At `p^2`, the differential data permit homogeneous projection; at `p^3`, the explicit source coordinate `d_p p^2` repairs it. Operations in scope: further differentiation, Hensel lifting, Jacobi parameter-jet comparison, Clausen weighted finite truncation and signed 216/2304 comparison; no claim to native spatial-state reduction.

**Next smallest science unit:** derive a **source-typed finite-field/Jacobi trace or CM arithmetic certificate** proving or refuting the residue selection `F_p(1/9)=0 (mod p)` at `p mod24=13,23`, and then a p² parameter-jet cancellation certificate. Retain both `k=p` boundary defects (4)-(5) when differentiating any proposed certificate; test first at 13,23,373 and 2053, then connect to 216–2304 mod-p³ comparison. Frozen mother target `W216(p-1)=p (mod p³)` at `p mod24=13,19` remains open.

**Control:** gateway 0.6.11 read 2026-11-04: `UPSTREAM_CODE_REVIEW_REQUIRED`, `research_authority_granted=false`, `executor_binding_configured=false`, `active_jobs=5/5`. Previous actual research recovery read `kimi-query-bridge#6637` was SUCCEEDED, prior continuation `#6638` had terminal failure (2026-11-01). Historical session and neutral staging remain protected. No fresh native claim, authorization or checkpoint from this author-side note.
