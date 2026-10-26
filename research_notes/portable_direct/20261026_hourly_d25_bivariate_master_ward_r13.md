# D25/LIFT — Exact bivariate generating Green–Ward identity with four genuine finite faces

Date: 2026-10-26. Requested Research lane `chatgpt-research-hourly-enterprise-math-20260923`, distinct from maintenance. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen science Source `c47e13e4aba0e006366f989d6334d443f6333ae3` remains unchanged. **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.**

## Scientific question and preserved inputs

The previous `20261026_hourly_d25_universal_ward_face_repair_rank_jet_r13.md` gave an arbitrary observer of the true oriented Ward sources and one genuine left face. The established `20261026_hourly_d25_diagonal_rank_moment_closed_recurrence_r11.md` supplies separate (k-1,k-2) source expressions (J_n^{ab}+E_n^{ab}). The new question is whether all of those Hasse-index couplings and both finite cutoff orientations arise from a **single exact two-parameter finite-carrier relation**, rather than six independently guessed source equations. We preserve (j,ell) order, Hasse indices, genuine boundary cells, infinity orientation and later high–high population. No positive/infinity or high-high term is identified with a finite face.

For integer (mge1), (p=6m+1), define regular rational germs near (t=s=0)
[
f_r(z)=rac{(-m-z)_r(-2m-2z)_r}{(1-p/2-3z)_r,r!},quad 0le r<p,qquad f_0(z)=1.
]
They satisfy **exactly**
[
D_z(r)f_r(z)=A_z(r-1)f_{r-1}(z),quad
D_z(r)=r(r-p/2-3z),quad
A_z(r)=(r-m-z)(r-2m-2z).	ag{1}
]
No use of a formal p-adic division by p is involved. For (L=1-2m, N=2m-1), define finite oriented moments
[
mathcal M_n^{h}(t,s)=
sum_{substack{1le j,ellle2m\ell-j=n}}
j^h f_j(t)f_{p-ell}(s),qquad hin{0,1}.
]
Outside (nin[L,N]), set (mathcal M_n^h=0). The coefficient of (t^a s^b) equals the established genuinely labelled (M_n^{ab,h}).

## Theorem — exact master identity for every Hasse degree

Let
[
C_n=(p-n)(p/2-n),quad
A_n=6m-2n,quad B_n=-18m^2+9mn-n^2.
]
For every (Lle nle N), the following is an **identity of rational functions regular at (t=s=0)**:
[
oxed{egin{aligned}
&[p-2n-3(t+s)],mathcal M_n^1
+[-C_n+3s(p-n)],mathcal M_n^0\
={}&[A_n-3(t+s)],mathcal M_{n+1}^1\
&+[B_n+4mt+(14m-3n)s+2(t^2-s^2)],mathcal M_{n+1}^0
+mathcal E_n(t,s).
end{aligned}}	ag{2}
]
The **real finite face** is
[
oxed{
mathcal E_n(t,s)=
egin{cases}
2(m+t)^2 f_{p-n-1}(s)
-(6m^2-8ms+2s^2)f_{2m-n}(t)f_{4m}(s),&nge0,\[2pt]
(20m^2-14ms+2s^2)f_{-n}(t)f_{p-1}(s)
+(2mt-2t^2)f_{2m}(t)f_{p-(2m+n+1)}(s),&n<0.
end{cases}}	ag{3}
]
Both cases contain **two different boundary populations**. In particular, the end-of-array terms do not become invisible by formally extending a hypergeometric series to infinity.

### Proof with all four cutoff origins

Multiply (1) at (r=j,z=t) by (f_{p-ell}(s)), multiply the reflected instance at (r=p-ell,z=s) by (f_j(t)), and subtract. For (n=ell-j), the difference of unshifted factors is
[
D_t(j)-D_s(p-ell)
=[p-2n-3(t+s)]j-C_n+3s(p-n).
]
The first shifted term has (j'=j-1,ell'=ell); the second has (j'=j,ell'=ell+1). Both have new difference rank (n+1) and the same product (f_{j'}(t)f_{p-ell'}(s)). Their coefficient difference is the exact polynomial
[
A_t(j')-A_s(p-ell')
=[A_n-3(t+s)]j'+B_n+4mt+(14m-3n)s+2(t^2-s^2).
]
Summing the common shifted interior yields the two moments on the RHS of (2).

To restore the *actual* truncated domain, for (nge0): the (j'=0,ell'=n+1) first-shift cell adds (A_t(0)f_0(t)f_{p-n-1}(s)=2(m+t)^2f_{p-n-1}(s)); the (ell'=2m+1,j'=2m-n) second-shift cell subtracts (A_s(4m)f_{2m-n}(t)f_{4m}(s)), with (A_s(4m)=6m^2-8ms+2s^2).

For (n<0): the omitted (ell'=1,j'=-n) second-shift cell adds (A_s(p-1)f_{-n}(t)f_{p-1}(s)), with (A_s(p-1)=20m^2-14ms+2s^2); the omitted (j'=2m,ell'=2m+n+1) first-shift cell subtracts (A_t(2m)f_{2m}(t)f_{p-(2m+n+1)}(s)), and (-A_t(2m)=2mt-2t^2). These are exactly (3), proving (2) with all boundary signs. QED.

## New all-order source interface and limitation

Extract ([t^a s^b]) from (2), move its parameter-dependent terms to the right, and use (u_{a,r}=[t^a]f_r(t)). This gives **exactly** the inherited
[
(p-2n)M_n^{ab,1}-C_n M_n^{ab,0}
=A_n M_{n+1}^{ab,1}+B_nM_{n+1}^{ab,0}
+J_n^{ab}+E_n^{ab}
]
for **every** (a,bge0), with (J_n) containing only shifts by (a-1,a-2,b-1,b-2), and (E_n^{ab}=[t^a s^b]mathcal E_n(t,s)). Thus the entire quadratic (k-1,k-2) Hasse coupling, including genuine two-sided faces, is controlled by **one bivariate polynomial-coefficient generating identity**; it is not an independent conjecture for six individual channels. This is a reusable higher-jet input for cross-channel telescoping.

This generating relation alone does **not** establish extra cross-channel cancellation beyond its coefficient equations. It does not drop a boundary, erase the positive-rank infinity (Z^+), consume the distinct ordered high–high corner (H_p), or prove the original fixed (z=2) Clausen scalar. BRC `COMPOSE_APPLIED`: preserve finite ordered carrier, Hasse parameter sources, left/right shift origins, p-valuation and downstream observers. These indices are external auxiliary ranks, not native X6 axes; P000 is unchanged.

## Reproducible author checks

The companion standard-library checker `20261026_hourly_d25_bivariate_master_ward_r13_check.py` constructs the two independent (f_r(t),f_r(s)) from product ratios, builds **finite** (j,ell) moments without using the result, and checks (2) against all four actual faces.

**Executed PASS:** 36 rational all-rank identities at (m=1,2,3,4) (including composite (p=25), valid algebraically); **3914** modular all-rank identities at (p^3) across 23 primes (pequiv1mod6), including (p=733), using two distinct (p)-adically safe nonzero parameter pairs ((t,s)=(p,2p),(3p,-p)) for every prime. These are author-only algebra checks, not independent Driver verification or a native CM experiment. The rational germ proof establishes the identity beyond tested instances.

## Exact next science / control frontier

Next: apply ([t^a s^b]) of the bivariate master to the original *fixed* (z=2) six-channel signed scalar, rather than re-proving each (J/E) formula. Combine the universal face-repair adjoint, the nonzero (p=13) face and the (p=733) signed rank-jet face (236mod733), both true finite shift faces, distinct positive infinity (Z^+) and ordered high–high (H_p). Seek a real (k-1,k-2) cross-source cancellation; otherwise publish a fully labelled nonzero residual with a precise observer scope.

Frozen native Source checkpoint and protected historical session/staging remain unchanged. The new exact continuation request `researchhourly-20261026-2021-continuation-r13` returned `INVALID_ARGUMENT / CONTROL_QUOTA`, its exact receipt returned `CONTROL_REQUEST_NOT_FOUND`; no native authorized CLAIM/OPEN/checkpoint/freeze/Driver result is inferred. Control support: `enterprise-math#1558`. Mother D25/LIFT/JT2 OPEN; original-class (H_0/B_0), ([X]Umod p^2), Frobenius (eta), (kappa) mapping, native experiment and independent review remain unfulfilled.