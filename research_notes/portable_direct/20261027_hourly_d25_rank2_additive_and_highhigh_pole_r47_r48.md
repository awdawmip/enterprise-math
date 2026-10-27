# D25/LIFT R47–R48 — rank-two additive source recovery and a sharp high-high pole obstruction

2026-10-27, Asia/Hong_Kong. Portable author research in the genuine Research lane `chatgpt-research-hourly-enterprise-math-20260923`, not the maintenance lane. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, parent D25/LIFT/JT2 OPEN. Frozen *scientific* source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` preserved. R23, R36, R38–R46 are consumed, not recredited. `AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY`. Nothing here is a native CLAIM/OPEN/checkpoint/Result/review.

## Exact original source, and R47 source-faithful additive recurrence

For all k>=0 retain independently the original rational sources
[
w_k=rac{(6k+1)(2k)!(3k)!}{(k!)^5,216^k},quad
s_k=rac{(8k+1)(4k)!}{(k!)^4,2304^k},quad d_k=w_k-s_k.
]
Define their *separate*, exact first-order ratios
[
a_k=rac{(6k+7)(2k+1)(3k+1)(3k+2)}
{36(6k+1)(k+1)^3},quad
b_k=rac{(8k+9)(2k+1)(4k+1)(4k+3)}
{288(8k+1)(k+1)^3}.
]
Theorem R47-A: `w_(k+1)=a_k w_k`, `s_(k+1)=b_k s_k`; moreover
[
a_k-b_k=
rac{(2k+1)(2688k^4+6160k^3+4456k^2+1166k+85)}
{288(k+1)^3(6k+1)(8k+1)}>0.
	ag{47.1}
]
Hence for every k>=0 over the rationals the original *labelled* pair is recovered from **two consecutive additive observations**:
[
oxed{w_k=rac{d_{k+1}-b_kd_k}{a_k-b_k},qquad
s_k=rac{d_{k+1}-a_kd_k}{a_k-b_k}.}	ag{47.2}
]
Consequently `d_0=0`, `d_1=85/288`, and
[
oxed{(a_k-b_k)d_{k+2}
-(a_ka_{k+1}-b_kb_{k+1})d_{k+1}
+a_kb_k(a_{k+1}-b_{k+1})d_k=0.}	ag{47.3}
]
This is a division-free second-order recurrence for the **unchanged original difference**.

*Proof.* Adjacent factorial cancellation yields the stated ratios. Cross-multiplication yields (47.1); all polynomial coefficients are positive. The observation matrix `[[1,-1],[a_k,-b_k]]` has determinant `a_k-b_k`; invert it to obtain (47.2), then advance one rank and eliminate w,s to obtain (47.3). At k=1, w=7/18 and s=3/32, hence d1=85/288. QED.

Two is minimal among scalar *linear observations of freely variable source amplitudes* (one scalar cannot invert a two-dimensional state), **not** a claim about additional known trajectory metadata. Over `Z_p` the same compression is valid modulo p^r only when `(k+1)(6k+1)(8k+1)P(k)` is a unit, where P is the positive quartic in (47.1). Singular rank inputs must retain both original sources. At k=0, P(0)=85 and every target p=6m+1>=7 is safe; later modular singular ranks exist (e.g. p=43,k=5). Rational invertibility is not modular invertibility.

## R48: high-high valuation and the minimum singularity of reflected additive repair

For each prime p=6m+1>=7 let `H=floor((3p-1)/4)` and `I_p={H+1,...,p-1}`.

Theorem R48-A. For every k in I_p,
[
v_p(w_k)=3,quad v_p(s_k)ge3,quad w_k-s_kin p^3mathbb Z_p.
	ag{48.1}
]
But `d_1=85/288` is a p-adic unit for **all** such primes. Therefore for arbitrary p-integral high-high coefficients `c_(p,k)` even chosen nonlocally,
[
oxed{d_1+sum_{kin I_p}c_{p,k}(w_k-s_k)
otequiv0pmod {p^3}.}	ag{48.2}
]
If a high-high-only coefficient system is to cancel this exact one-port low residual, **at least one** coefficient must have valuation <= -3. Coefficients of valuations >= -2 leave the high-high sum divisible by p, whereas d1 remains a unit.

*Proof.* For k in I_p the factorial arguments lie in p<=2k<2p, 2p<=3k<3p, 3p<=4k<4p<p^2; k! is a p-unit. Legendre yields valuations 1,2,3 respectively. The original W weight `6k+1` is a unit here: p=6m+1 implies its only possible zero rank k=m lies outside this band. The original S weight `8k+1` may raise, not lower, valuation. Denominators 216,2304 are units. The only possible prime numerator factors of 85 are 5 and 17, neither in target class, proving d1 a unit. QED.

Theorem R48-B (sharp, original endpoint):
[
oxed{rac{w_{p-1}}{p^3}equiv5,qquad
rac{s_{p-1}}{p^3}equiv7,qquad
rac{d_{p-1}}{p^3}equiv-2pmod p.}	ag{48.3}
]
The middle residue is 0 at p=7; its true s valuation is 5, not 3. Thus d_(p-1)/p^3 is a unit for all target primes, and the -3 pole requirement is valuation-sharp. Specifically `c=85/576 mod p` gives
[
d_1+c,rac{d_{p-1}}{p^3}equiv0pmod p.
	ag{48.4}
]
This deliberately chosen coefficient only cancels **one** low-rank port at **one digit**. It is not a global WZ construction, nor proof of W=S modulo p^3.

*Proof of (48.3).* Writing `U_p(n!)=n!/p^{v_p(n!)}`, grouping Wilson blocks and the p-multiples gives `U_p((ap+b)!)=(-1)^a a! b! mod p` for 0<=b<p and a<=3 here. Wilson reflection implies `U_p((p-1)!)=U_p((2p-2)!)=U_p((3p-3)!)=U_p((4p-4)!)=-1 mod p`. At k=p-1 insert these values into the exact weighted w,s fractions and apply Fermat to 216^(p-1),2304^(p-1); the normalized residues become 5 and 7. Their difference is -2, nonzero modulo every p>=7. QED.

## Executed evidence, provenance, BRC and next action

Actual local stdlib `Fraction`/p-free-factorial author verification **PASS**: 35 ranks checking both source ratios, the rational determinant, two-source reconstruction and the order-two recurrence; 80 primes `7<=p<=997, p=1 mod6`; 9,125 high-high ranks checked by integer valuations; independent endpoint units (5,7,-2) for all 80 primes; unit-eligible modular reconstructions while excluding rather than hiding singular denominators. Code stored as `research_notes/portable_direct/20261027_hourly_d25_source_faithful_rank2_and_upper_pole_r47_r48_check.py`. These checks corroborate explicit algebraic theorems; they are not native p=373 H0/B0 experimentation, formal verification or independent review.

BRC `COMPOSE_APPLIED`: retain label W/S, integer rank, actual transition, additive observer, necessary next-rank residual, exact determinant and modular singularity, high-band valuation and coefficient pole separately. The rank is an arithmetic auxiliary index, not one of the six Enterprise native X6 Cell coordinates; no 2D native plane or full-X6 dynamic theorem is asserted. P000/ACTIVE residual-faithful worldview and the distinct frozen scientific pin are unchanged.

**Next exact mathematical unit:** construct the finite Green/adjoint summation of (47.3) with BOTH endpoint/source components, compare its boundary term to R36's finite PF Green observer and R23's original p^2-divided low-half discrepancy, then test exact low-band constraints at p=13,19,181,373 while retaining modular P(k) singularities, six z=2 Hasse J/E ports and positive-infinity provenance. No redoing R45/R46 multiplicative scalar/affine obstruction. Native formal route requires a current, winning Research CLAIM and authorized run; #1558 remains the support path for predecessor mismatch. Research-Activity update is `REGISTER_PENDING` absent a verified own active session. H0/B0, [X]U modulo p², Frobenius eta/kappa, native p373 and independent Driver review remain OPEN.
