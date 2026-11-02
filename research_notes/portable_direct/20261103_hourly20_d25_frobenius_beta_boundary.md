# D25 — finite Wronskian Frobenius-boundary and beta quadrature (2026-11-03)

Status: AUTHOR-DERIVED / HAND-PROVED / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific Source c47e13e4aba0e006366f989d6334d443f6333ae3. Logical Research conversation chatgpt-research-hourly-enterprise-math-20260923, separate from maintenance chatgpt-hourly-enterprise-math-20260921. This is external finite-field arithmetic and a portable author-side result.

## Inherited exact source

Let p=6r+1 >= 7 be prime, u=3r=(p-1)/2, theta=z d/dz, and work in F_p[z]. Let

$$
\ell(z)=\sum_{k=0}^r {r\choose k}{2r\choose k}z^k,\quad
Q(z)=(G_p(z)-\ell(z))/p\bmod p,\quad
\Omega(z)=\ell\,\theta Q-Q\,\theta\ell.
$$

Let a_n=(1/2)_n(1/3)_n(2/3)_n/(n!)^3 be the **original 216** source coefficients and

$$
S(z)=\sum_{n=0}^{2r}s_nz^n,\qquad s_n=(9n+4)a_n/36\bmod p.
$$

The previously proved finite Gauss–Wronskian identity (Enterprise Math commit cd37f09ddd8511b790ae4ffe564ae001cf7cc423) is

$$
(1-z)\Omega'(z)+u\Omega(z)=S(z),\quad \Omega(0)=0,\quad \deg\Omega\le u. \tag{W}
$$

The frozen target classes p mod 24 in {13,19} satisfy inherited CM0: ell(1/2)=0 mod p. Write g=ell(1/2)/p mod p, j=(theta ell)(1/2) mod p. The earlier open second-carry equality was 12gj-12Omega(1/2) ?= 1 mod p.

## F1. Exact polynomial Frobenius-boundary theorem

Define the polynomial primitive

$$
I(z)=\int_0^z (1-t)^u S(t)\,dt\quad\text{in }\mathbb F_p[z].
$$

This is algebraic coefficientwise integration: (1-t)^u S(t) has degree <=5r, and all denominators 1,...,5r+1 are units modulo p=6r+1.

**Theorem. For every such p, an exact equality in F_p[z] holds:**

$$
\boxed{(1-z)^{u+1}\Omega(z)=I(z)-z^p/6.}\tag{F1}
$$

**Proof.** Since Q=(G_p-ell)/p and deg ell=r, its top coefficient is

$$
Q_{2r}=\frac{(1/6)_{2r}(1/3)_{2r}}{p((2r)!)^2}
\equiv\frac{(-1)^r r!(r-1)!}{6(2r)!}\pmod p.
$$

The unique factor p of (1/6)_{2r} occurs at j=r and contributes p/6; remaining factors give (-1)^r r!(r-1)!, while (1/3)_{2r} gives (2r)! modulo p. The coefficient of z^u in Omega is therefore

$$
[z^u]\Omega=(2r-r){2r\choose r}Q_{2r}=\boxed{(-1)^r/6}\pmod p.
$$

Differentiate the proposed left side. Since u+1=-u in F_p, (W) implies

$$
\frac{d}{dz}[(1-z)^{u+1}\Omega]
=(1-z)^u[(1-z)\Omega'-(u+1)\Omega]
=(1-z)^u S=I'.
$$

The difference has zero derivative, zero constant term and degree <=2u+1=p; hence it is c z^p. Its top coefficient is (-1)^{u+1}[z^u]Omega=(-1)^{4r+1}/6=-1/6, so c=-1/6. QED.

The nonzero -z^p/6 term is a Frobenius boundary port arising from the kernel of differentiation in characteristic p. It is necessary for the exact polynomial identity and for the half-point readout.

## F2. Complete original-source beta moment

At z=1, (F1) gives I(1)=1/6. The exact polynomial beta integral

$$
\int_0^1 t^n(1-t)^u dt=\frac{n!\,u!}{(n+u+1)!}
$$

has denominators prime to p for n<=2r. Therefore, for **every** p=6r+1 >=7 prime,

$$
\boxed{\sum_{n=0}^{2r}(9n+4)a_n\frac{n!\,u!}{(n+u+1)!}\equiv6\pmod p.}\tag{F2}
$$

## F3. Finite character readout and a new exact equivalent target

For x in F_p minus {1}, set chi(y)=(y/p) for nonzero y. Fermat and Euler imply x^p=x and (1-x)^{u+1}=(1-x)chi(1-x), so (F1) becomes

$$
\boxed{\Omega(x)=\frac{\chi(1-x)}{1-x}\Big(I(x)-x/6\Big).}\tag{F3}
$$

At x=1/2 this is Omega(1/2)=2 chi(2)(I(1/2)-1/12). For p mod24 in {13,19}, chi(2)=-1; hence Omega(1/2)=1/6-2I(1/2), and the inherited second-carry question is exactly equivalent to

$$
\boxed{4g j+8I(1/2)\stackrel{?}{\equiv}1\pmod p\quad (p\bmod24\in\{13,19\}).}\tag{OPEN-F4}
$$

The equivalence is proved. The universal equality marked ? is still an open target.

## F4. Linear-time incomplete-beta reconstruction

For x in F_p let B_n(x)=integral_0^x t^n(1-t)^u dt (a polynomial primitive). Integration by parts yields

$$
B_0(x)=\frac{1-(1-x)^{u+1}}{u+1},\quad
B_{n+1}(x)=\frac{(n+1)B_n(x)-x^{n+1}(1-x)^{u+1}}{n+u+2},\quad 0\le n<2r.
$$

All denominators n+u+2<=5r+1<p are units. With

$$
I(x)=\sum_{n=0}^{2r}\frac{9n+4}{36}a_nB_n(x),\quad
\frac{a_{n+1}}{a_n}=\frac{(2n+1)(3n+1)(3n+2)}{18(n+1)^3},
$$

the complete original-source I(1/2) is computed by O(p) finite-field operations using streaming memory. This is a provenance-preserving BRC observer with an explicit character and Frobenius boundary.

## Exact executed checks and frontier

The accompanying standard-library verifier checks all 611 primes 7<=p<=10000, p=1 mod6: top Omega coefficient, complete beta moment, direct incomplete-beta recurrence versus independently propagated Omega recurrence. All pass. Among them the 312 target primes in classes 13,19 mod24 satisfy OPEN-F4 in this **finite** range. Nine sample primes 7,13,19,31,37,43,73,373,1171 also pass direct coefficient-by-coefficient construction of both sides of (F1) from ell and the independently formed Q.

For p=373: r=62, u=186, chi(2)=-1, [z^u]Omega=311=1/6, Omega(1/2)=27, I(1/2)=142, g=340, j=294, beta complete moment=6. Here 4gj=357, 8I=17, and 357+17=374=1 mod373. F1/F2/F3/F4 have algebraic proofs; the all-target second-carry equality remains unproved. The native H0/B0 p373 experiment is separate and not executed here.

The immutable mother objective remains Delta_p-R_p=0 mod p in both target classes. New author-side frontier: Frobenius boundary -z^p/6, complete beta moment (F2), character-aware exact readout (F3), and O(p) quadrature (F4). Next research unit: use the complete beta moment to split the original source integral at 1/2 and seek a terminating WZ/CM root-lift certificate for OPEN-F4, or a counterexample satisfying its hypotheses; then propagate the solved carry through the existing three-band source tower. Parallel 2026-11-03 onhour E3/E4 gauge work retains its independent authorship.

Control/read state at 2026-11-03: Gateway 0.6.11 reports UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false, native active-job quota 5/5. Existing historical #6637 is recovery-only (no run, unopened claim, pending mutation or unpublished upload in its recorded projection); #6638 ended FAILED with UPSTREAM_CODE_REVIEW_REQUIRED. Their source session/neutral staging and contribution history are preserved. No new native Source checkpoint, CLAIM, OPEN, Result or review is claimed. Support Issue #1558 owns the existing control defect; #1559 the unexecuted original-class benchmark. This publication is author-side GitHub evidence, UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.
