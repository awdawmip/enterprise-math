# D25/LIFT — exact reflection Green pairing, retained value/derivative ports, and a p=373 nonzero witness

2026-10-25 · TASK_RESEARCH portable author proof + exact integer checker · **UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, research logical conversation chatgpt-research-hourly-enterprise-math-20260923. Frozen scientific Source pin **c47e13e4aba0e006366f989d6334d443f6333ae3** unchanged. Research-Activity/registration, authorized native CLAIM/open/run, Result, Driver review and mathematical acceptance are separate; this portable note claims none of those execution outcomes.

## Inherited precise source mathematics (not re-credited)

Let p=6m+1 >=13 be prime, n=2m=(p-1)/3 and
$$
c_k=\frac{(3k)!}{27^k(k!)^3},\qquad
A(X)=\sum_{k=0}^{n}c_kX^k,\quad B(X)=A(1-X),\quad
P(X)=X(1-X).
$$
All coefficients are in Z_(p). From the earlier *coefficientwise* Hesse/Legendre reflection theorem,
$$
D(X)=\frac{A(X)-B(X)}p\in\mathbf Z_{(p)}[X].
$$
The earlier two-port work established, at
$$
R=\mathbf Z_{(p)}[T]/(T^2-2),\quad u=(2-T)/4,\quad
\sigma(T)=-T,\quad \sigma(u)=1-u,
$$
the original source expansions A(u)=a+bT, A'(u)=e+dT and integral ports v=b/p, w=e/p. These are **ordinary Hesse polynomial** ports, not a chosen divided-power H0/B0 representative. For target CM-inert primes p≡13,19 (mod24), the inherited CM0 statement additionally yields a≡0 (mod p).

The prior Picard–Fuchs forcing used the exact polynomial operator
$$
L=P\partial_X^2+(1-2X)\partial_X-2/9,\qquad
C=\frac{p+1}{9}c_n.
$$
No polynomial reflection or prior two-port identity is newly claimed here.

## New theorem: reflection Green pairing and exact global-to-local identity

Define the **ordered, signed source pairing**
$$
\boxed{\mathcal W(X)=P(X)\big(A(X)B'(X)-A'(X)B(X)\big).}
$$
For all p=6m+1 >=13 the following are exact identities over Q[X]:
$$
\boxed{LA=-pC\,X^n,\qquad LB=-pC\,(1-X)^n,}
\tag{1}
$$
$$
\boxed{\mathcal W'(X)
=pC\big[X^nB(X)-(1-X)^nA(X)\big].}
\tag{2}
$$
Moreover, $\mathcal W/p\in\mathbf Z_{(p)}[X]$ and its exact reflection form is
$$
\boxed{\frac{\mathcal W(X)}p
=P(X)\big(A'(X)D(X)-A(X)D'(X)\big).}
\tag{3}
$$

Let F(X)=X^nB(X)-(1-X)^nA(X)=\sum_{j=0}^{2n}f_jX^j and
$$
J(X)=\sum_{j=0}^{2n}\frac{f_j}{j+1}
\left(X^{j+1}-2^{-(j+1)}\right).
$$
All j+1<=2n+1=4m+1<p, so this is a p-integral, **fully finite** polynomial antiderivative with J(1/2)=0. Exact integration of (2) gives the new global-to-local identity
$$
\boxed{
\frac{\mathcal W(u)}p
=-\frac{A(1/2)A'(1/2)}{2p}+C J(u).
}
\tag{4}
$$
Both sides lie in the coefficient **base field** (the T-odd coordinate is exactly zero), and the right side is p-integral. Thus the normalized pairing can be computed by two independent source-preserving routes: raw A(u), A'(u), coefficient conjugation on the left; or center data and the explicitly finite forcing integral on the right. It is a scalar source-polynomial pairing, **not** a crystalline symplectic form or native Frobenius until a genuine same-class comparison is proved.

**Proof.** The hypergeometric recurrence
$(k+1)^2c_{k+1}=(k+\frac13)(k+\frac23)c_k$
cancels every coefficient below degree n in LA. The terminal coefficient is $-(n+\frac13)(n+\frac23)c_n=-p(p+1)c_n/9=-pC$, proving the first equation of (1). Reflection X↦1−X commutes with L, proving the second. Since $L=(P\partial_X)'-2/9$, subtraction gives
$(P(AB'-A'B))'=A LB-B LA$, which is (2). Substituting B=A−pD proves (3) and p-integrality. At X=1/2, $B=A$ and $B'=-A'$, hence $\mathcal W(1/2)=-A(1/2)A'(1/2)/2$. This proves (4).

For the provenance/base-field claim, F(1−X)=−F(X), so $J(1-X)=J(X)$ by differentiation and the shared normalization at X=1/2. Thus $\sigma(J(u))=J(u)$ in R. Likewise $\mathcal W(1-X)=\mathcal W(X)$. Finally coefficientwise A≡B mod p implies $A'(1/2)\equiv0$ mod p, which makes the divided center term p-integral. No CM operator is assumed. QED.

## New local theorem: a bilinear port surviving the p=373 even-zero anomaly

Extract at u the ordered coefficients A(u)=a+bT and A'(u)=e+dT. Exact coefficient conjugation gives
$$
B(u)=a-bT,\qquad B'(u)=-e+dT.
$$
Consequently, before any modular reduction,
$$
\boxed{
\mathcal W(u)=\frac18(4bd-2ae),\qquad
\frac{\mathcal W(u)}p=\frac{2vd-aw}{4}.
}
\tag{5}
$$
For the original CM-inert target classes, the inherited source CM0 implies a≡0 mod p. Hence
$$
\boxed{\frac{\mathcal W(u)}p\equiv\frac{v\,d}{2}\pmod p.}
\tag{6}
$$
Unlike the isolated even derivative port w, this **bilinear value/derivative observer** can survive its zero; equation (6) claims no universal nonvanishing and no ability to recover the full two-port jet from one scalar. In particular it is not the original LIFT residue.

### Exact finite source verification

The accompanying [integer checker](20261025_hourly_d25_hesse_reflection_green_pairing_p373_check.py) constructs A and A(1−X) independently by factorial recurrence/binomial expansion, evaluates their original derivatives in (Z/p²)[T]/(T²−2), and checks (2) by its *separate* finite antiderivative (4).

| p | v mod p | w mod p | d mod p | W(u)/p mod p |
|---:|---:|---:|---:|---:|
| 13 | 6 | 10 | 2 | 6 |
| 19 | 11 | 16 | 4 | 3 |
| 37 | 36 | 26 | 22 | 26 |
| 43 | 41 | 1 | 37 | 6 |
| 61 | 35 | 49 | 50 | 21 |
| 67 | 10 | 36 | 26 | 63 |
| 211 | 209 | 200 | 168 | 43 |
| **373** | **154** | **0** | **57** | **286** |

At p=373, source factorial evaluation recovers the prior raw residues
$$
A(u)=112646+57442T,\qquad A'(u)=130607T\pmod{139129},
$$
and yields the **new exact pairing residue**
$$
\boxed{\mathcal W(u)=106678=373\cdot286\pmod{373^2},\quad
\mathcal W(u)/373=286\pmod{373}.}
\tag{7}
$$
The independent Green route has $C\equiv40$ mod373, $J(u)=35047$ mod139129, $A(1/2)=9736$ and $A'(1/2)=129058=373\cdot346$ mod139129. In formula (4) its two normalized summands are
$$
-\frac{9736\cdot346}{2}\equiv140,\qquad
40\cdot35047\equiv146\pmod{373},
$$
so $140+146=286$, exactly matching the direct ring computation. This retains a nonzero branch-labeled source pairing even though w_373=0. Eight tests are **author finite exact checks**; they do not extend (6) to a nonzero all-prime theorem or independently review (1)–(6).

## BRC/Enterprise-coordinate observer discipline and next discriminating step

BRC resolution **COMPOSE_APPLIED** to the actually typed signed arithmetic carrier $(p,T,\sigma; A(u),A'(u);a,b,e,d; v,w; \mathcal W/p)$ and to the allowed operations derivative, reflection, finite integration, modulo p², and p-division. The pairing compresses the source state for **this declared bilinear readout**, but is not injective and is not sufficient for later unspecified native CM operations. It does not create a positive-mass model or alter P000.

The genuinely missing smallest Source task is an authenticated same-class divided-power H0/B0 basis/representative, directed semilinear Frobenius and $[X]U\bmod p²$, genuine normalization from the ordinary Gauss–Manin observable to frozen $\kappa$ and $\Delta_p-R_p$. The concrete next comparison is to test whether an actually normalized native alternating pairing transports (4)–(6) with explicit matrix and scalar factors; absence of those data remains an open proof obligation. At p373 any proposed map that divides by w must handle w=0, while v=154, d=57 and the pairing=286 remain nonzero.

**Do not repeat** the earlier reflection, half-rank Green inverse, two-port chart/forward jet, p<10000 exception scan, WZ scans, or native 19-unit completed checkpoint. This document is portable author evidence only. Native CM experiment NOT_RUN; theorem independent review NOT_DONE; no Source checkpoint, Result, or LIFT acceptance asserted. Parent D25/LIFT stays OPEN.
