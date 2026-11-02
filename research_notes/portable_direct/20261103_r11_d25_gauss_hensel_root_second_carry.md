# D25 — Gauss CM Hensel roots and second-order original-source carry

**2026-11-03 +08:00. AUTHOR-DERIVED / HAND-PROVED / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.**
Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. The actual scheduled TASK_RESEARCH logical lane is `chatgpt-research-hourly-enterprise-math-20260923`, separated from maintenance. Mother: `Delta_p-R_p=0 mod p`, for p mod24 = 13 or 19. The Gauss polynomial below is **not** the differently typed G_p of the frozen mother scalar interface.

## Inherited interface and definitions

For each prime p=6r+1>=7, set z0=1/2 in Z_(p), theta=z d/dz and

`ell(z)=sum_{k=0}^r binom(r,k)binom(2r,k)z^k`,
`G(z)=G^Gauss_p(z)=sum_{k=0}^{p-1}(1/6)_k(1/3)_k z^k/(k!)^2`,
`F(z)=sum_{k=0}^{p-1}(1/2)_k(1/3)_k(2/3)_k z^k/(k!)^3`.

Inherit, without taking new credit, the finite identities G=ell mod p and F=G² mod p² **coefficientwise** from `20261102_r11_d25_gauss_deformation_wronskian_second_carry.md` and its prior finite Clausen source. In target classes, the accepted CM0 input gives ell(z0)=0 mod p. Define Q=(G-ell)/p mod p coefficientwise; Omega=ell theta Q-Q theta ell; the integer-lift quotients g=ell(z0)/p mod p, h=G(z0)/p mod p and j=(theta ell)(z0) mod p. Thus h=g+Q(z0), Omega(z0)=-j Q(z0). The inherited **OPEN** second-carry statement is 12jh ?= 1 mod p.

## H1 — Squarefree terminating Gauss polynomial (PROVED)

For all primes p=6r+1>=7, ell has only simple roots over the algebraic closure of F_p.

**Proof.** ell = 2F1(-r,-2r;1;z) satisfies exactly
`z(1-z)ell''+[1+(3r-1)z]ell'-2r²ell=0`.
ell(0)=1 and ell(1)=binom(3r,r) is a p-unit (3r<p). For a multiple root a not in {0,1} with multiplicity 2<=m<=r<p, the lowest (z-a)^(m-2) coefficient of the equation is a(1-a)m(m-1)c, where c is the first nonzero Taylor coefficient, and is nonzero. Contradiction. QED.

At an inherited CM0 root z0, the derivative ell'(z0)=2j is therefore a unit; the inverses of j below are justified.

## H2 — Exact first Hensel digits and one-point equivalent test (PROVED REDUCTION)

The unique roots of ell and G modulo p² in the residue class z0 are alpha=z0+p delta_ell and beta=z0+p delta_G with

`delta_ell=-g/(2j)`, `delta_G=-h/(2j)` in F_p.

Their **source-tagged relative displacement** is

`delta_G-delta_ell=Omega(z0)/(2j²)` in F_p.

Taylor at z0 and H1 prove these formulas. The currently OPEN equality 12jh=1 is **exactly equivalent** to

`G^Gauss_p(1/2-p/(24j²)) = 0 (mod p²)`.   (H2-test)

Indeed this value equals p(h-1/(12j)) mod p². The equivalence is proved; the all-prime vanishing remains OPEN. The comparison retains the integer lift of ell and the original-source Wronskian rather than erasing their provenance.

## H3 — Second Hensel root digit and original 216 defect (PROVED)

Choose canonical root digits delta, epsilon in {0,...,p-1} such that G(z0+p delta+p² epsilon)=0 mod p³. Let d=G'(z0) mod p², e=G''(z0) mod p. Hensel/Taylor gives

`G(z0)=-p delta d-p²(epsilon d+delta²e/2) (mod p³)`.

With C=[(1+6theta)G²](z0)=G(z0)²+6G(z0)G'(z0), this gives

`C/p=-6 delta d²+p(delta²d²-6 epsilon d²-3delta²ed) (mod p²)`. (H3a)

**New endpoint jet removal.** At z0, the Gauss ODE and ell(z0)=0 give
`ell''(z0)=-ell'(z0) (mod p)`, because z0(1-z0)=1/4 and [1+(3r-1)z0]=(p+1)/4=1/4 mod p. Therefore e=-d mod p, yielding the derivative-simplified exact formula

`C/p=-6 delta d²+p(4delta²d²-6epsilon d²) (mod p²)`. (H3b)

Define the original-source finite-Clausen defect (derivative before scalarization)
`E_p={[(1+6theta)(F-G²)](z0)}/p² (mod p)`.
It is well-defined by the inherited coefficientwise p² congruence. With the **full original weighted 216** observable W=[(1+6theta)F](z0), one obtains

`W/p=-6delta d²+p(4delta²d²-6epsilon d²+E_p) (mod p²)`. (H3c)

This is a genuine second-order signed carry transport. It preserves (1) first root displacement, (2) second root digit, (3) derivative unit mod p², and (4) independent original 216/finite-Clausen defect. The previously established three-band theorem covers the shortened cutoff; H3c by itself does not assert a new native experiment, a universal W=p mod p³, or an exact map to the distinct frozen mother Delta-R observer. QED.

## Executed exact checks and p=373 certificate

A standard-library integer checker separately constructs G, original F and binomial ell. It checked H1/H2 root formulas, displacement and equivalence at **all 312** primes 7<=p<=10000 with p mod24 in {13,19}. The inherited second-carry numerical assertion held in this finite set; that is not its universal proof. The checker independently evaluated both polynomial branches, exact mod-p³ root digits and the original weighted F source on seven primes {13,19,37,43,181,373,1171}; H3a/H3b/H3c passed for all seven.

For p=373: r=62, j=294, g=340, Q(z0)=57, Omega(z0)=27, h=24, delta_ell=276, delta_G=274, epsilon=321, d=78545 mod373², e=158 mod373, E_373=177, beta=32638 mod373² and 18815053 mod373³, C/373=73109 mod373². Thus W/373=73109+373*177=1 mod373² (exact original arithmetic). For p=19, E_19=7, delta=15, epsilon=3 and C/19=229 mod361; W/19=1 mod361. The nonzero source defect is a concrete signed-information preservation witness.

The checker is **author-side**, not native original p=373 H0/B0. Evidence: `d25_hensel_root_20261103.py` and `d25_hensel_root_20261103_results.json` in this directory. BRC is COMPOSE_APPLIED to original index and signed (6k+1) weights, p-adic digits, distinct Gauss/ell/F sources, derivative operations, and explicit scalar observer. The special e=-d projection is certified for this exact root/observer; this classical arithmetic is an external model, not a native X6 geometry transfer.

## Exact next action and control boundary

Seek a source-faithful finite Gauss/CM certificate for the predicted H2 root shift, or an exact target counterexample. Independently analyze the second-digit cancellation between epsilon, d mod p² and E_p in H3c against the existing original-216 three-band precision tower, then prove any map back to the frozen Delta_p-R_p interface before claiming task closure. Preserve CM0/Clausen work, original frozen inputs, contributions and non-repeated completed units.

Live Gateway 0.6.11: `UPSTREAM_CODE_REVIEW_REQUIRED`, research_authority_granted=false, executor_binding_configured=false, active control quota 5/5; this turn's one continuation read returned `CONTROL_QUOTA`. Existing control support #1558 and native H0/B0 support #1559 retain ownership. No new service session, CLAIM, authorized OPEN, Source checkpoint, Result, review or scientific admission was made; existing staging/old session/request state was left untouched.
