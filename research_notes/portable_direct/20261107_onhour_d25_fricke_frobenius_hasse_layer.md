# D25 — Fricke cutoff source: sub-Frobenius germ and first nonzero Hasse layer

Date: 2026-11-07. TASK_RESEARCH author-side portable result, **UNREVIEWED / NOT_ADMITTED**. Frozen Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, immutable science `c47e13e4aba0e006366f989d6334d443f6333ae3`. Consumes exact Fricke/Picard–Fuchs operator and cutoff identity at `9924d627da2b8bec897405ab8d7ef9ecbb6aeccc`. No claim/session authority is inferred from this publication.

## Definitions and new theorem

For an arbitrary prime p>3, work over the p-adic étale coefficient algebra `O_p=Z_(p)[s]/(s^2-2)`. It is a product of two coefficient ports at split primes and a quadratic extension at inert primes. No scalar/branch quotient is taken. For ε=±1 let `t_ε=ε6s`, `u=t-t_ε`, and use the unchanged exact Fricke maps
[
z(t)=rac{108t^2(t+9)(t+8)^2}{(t+12)^6},qquad
w(t)=rac{256t^3(t+8)(t+9)^3}{(t^2+36t+216)^4},
]
[
R(t)=H(t)M(t)=rac{3(t^2-72t-648)(t^2+16t+72)}
{2(t+6)(t+12)(t^2-24t-288)}.
]
Put `C_p=binom(2p,p)^2 binom(3p,p)/108^p` and
`D_p=binom(2p,p)^2 binom(4p,2p)/256^p`.
The already proved **exact** inhomogeneous cutoff source is
[
F_p(t):=(L_U^{(t)}E_p)(t)=-p^3{C_pz(t)^p-R(t)D_pw(t)^p}.
]
All denominators in these rational functions are units in the local Taylor ring around either `t_ε` for p>3. Thus `S_p(u):=F_p(t_ε+u)/p^3` is a well-defined formal series in `O_p[[u]]`.

**Theorem (entire first Frobenius layer).** Let `z_1=z'(t_ε)=-1+ε3s/4` and `w_1=w'(t_ε)=4/9-ε8s/27`. For every prime p>3,
[
oxed{quad S_p(u)equiv rac{R(t_ε+u)}{96}-rac1{18}
+u^pleft[rac3{32},w_1^pR(t_ε+u)-rac19z_1^pight]
pmod{(p,u^{2p})}.quad} 	ag{1}
]
The parentheses indicate simultaneous coefficient reduction mod p and truncation at u^(2p). In particular, **every Hasse coefficient of degree 0,...,p−1** is exactly that of the rational germ `R(t_ε+u)/96-1/18` modulo p.

At the first new Frobenius Hasse degree p, however, the *difference* between the true source and this rational germ is
[
oxed{quad [u^p](S_p-R/96+1/18)
=rac5{18}-ε,left(rac2pight)rac{7s}{36}pmod p.quad}	ag{2}
]
Its norm under `s↦-s` is
[
oxed{quad operatorname{Norm}(Delta_{p,ε})=rac1{648}
otequiv0pmod p,quad p>3.quad}	ag{3}
]
Thus the first genuinely Frobenius-scale correction to the smooth germ is nonzero in *every* prime characteristic p>3, simultaneously in both conjugate ports. The conclusion is specifically about this Picard–Fuchs source, not about the original native H0/B0 operator or the weighted second-digit mother claim.

For target p≡13,19 (mod24), `(2/p)=-1`. At the positive fiber:
[
Delta_{p,+}=5/18+7s/36,qquad
[u^{p+1}](S_p-R/96+1/18)=5(s-1)/216pmod p.
]
For p=19 these Hasse residues (constant,s-coefficient) are respectively `(14,6)`, `(2,17)`; for p=373 they are `(21,52)`, `(278,95)`, in `F_p[s]/(s^2-2)`. At p=373 the norm of the first correction is `255 mod 373`. The negative fiber gives conjugate coefficients.

The previously missing ordinary source jets below degree p now follow without new integration:
[
F_p''(t_ε)/p^3equiv 475/576-ε2015s/3456,qquad
F_p'''(t_ε)/p^3equiv -19205/2304+ε3395s/576pmod p.
]
These are **ordinary derivatives**; (2) uses the Hasse/Taylor coefficient `[u^p]`, which must not be replaced by a p-th ordinary derivative in characteristic p.

## Proof

Use Lucas to obtain `C_p≡1/9` and `D_p≡3/32` mod p. The exact special-fiber values are `z(t_ε)=1/2`, `w(t_ε)=1/9`, `R(t_ε)=4`. Rational Taylor series with unit denominators satisfy freshman's dream
[
z(t_ε+u)^pequiv 2^{-1}+z_1^pu^p,quad
w(t_ε+u)^pequiv 9^{-1}+w_1^pu^p
quad pmod{(p,u^{2p})}.
]
Substituting these directly into the exact source identity proves (1), including every coefficient from 0 to 2p−1. At degree p, the correction is `(3/8)w_1^p-(1/9)z_1^p`. Frobenius fixes `F_p` rational scalars and maps `s^p=(2/p)s`, yielding (2). Its norm is
`25/324-98/1296=1/648`; this is a p-unit for p>3. The degree p+1 coefficient is `(3/32)w_1^pR'(t_ε)`; evaluating `R'(t_ε)=(-35+ε25s)/3` gives the stated target-class value. Two more exact rational differentiations of R yield the second/third ordinary source jets. This proof keeps the 216 and 2304 legs separate until their certified source combination.

## Exact, executed validation and scope

`d25_frobenius_hasse_source_germ_check_20261107.py` performs symbolic equality of both rational fibers, derivatives through order 3 and norm, plus independent truncated polynomial arithmetic in `F_p[s]/(s^2-2)` at p=5,7,11,13,19,373, **both ε ports**, through degree p+1. All 12 full polynomial checks passed on 2026-11-07; for p373 both ε ports were fully materialized (not merely predicted). At p373 the actual first two defect coefficients at the positive fiber are `(21,52)` and `(278,95)`.

BRC application: `COMPOSE_APPLIED`; typed carrier = two coefficient streams and two conjugate fiber ports; observer = finite source jet and p-th Hasse coefficient; allowed operations = rational pullback, multiplication by R, Frobenius/Hasse expansion and norm only after ports retained. The nonzero norm certifies that erasing the u^p residual loses a future-observable source correction. No new native benchmark has been executed.

## Smallest remaining mother-objective unit

Integrate this nonhomogeneous Frobenius-layer source against the *actual three independent homogeneous Picard–Fuchs initial constants* to reconstruct the finite **weighted** 216/2304 transfer; specifically evaluate the Dwork/Frobenius normalization at p=19 and 373, then attempt the uniform mod p^4 transfer. Preserve the original-class native p373 H0/B0 divided-power/Frobenius/κ experiment and its independent reproduction under support issue #1559. Required Source Researcher session/CLAIM/run and reviewer admission remain unknown; original request `onhour11-20261106-1400-exact-research-lane-continuation` remains unreplayed.

Status: `AUTHOR_SIDE_PROVED / EXACT_SYMBOLIC_AND_MODULAR_CHECKED / UNREVIEWED / NOT_ADMITTED`.
