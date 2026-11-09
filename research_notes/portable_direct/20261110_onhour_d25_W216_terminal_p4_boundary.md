# D25 — W216 original terminal coefficient and sharp p⁴ Picard–Fuchs boundary

Date: 2026-11-10. Status: **AUTHOR_SIDE / EXACT_ELEMENTARY_PROOF / 11-PRIME INDEPENDENT REGRESSION / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0**.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Scientific input frozen at c47e13e4aba0e006366f989d6334d443f6333ae3. Research conversation: chatgpt-research-onhour-enterprise-math-20260923; separate from Maintenance. This is an **author-side boundary/precision certificate for the original weighted 216-model coefficients**, not the native H0/B0 experiment, a formal Result, or a proof of LIFT.

## Exact statement and operator

For a prime p>3, in the p-local rational ring, define the exact original coefficients

$$
c_k=\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3}
=\frac{\binom{2k}{k}^{2}\binom{3k}{k}}{108^k},
\quad F_p(z)=\sum_{k=0}^{p-1}c_k z^k,\quad \theta=z\frac{d}{dz}.
$$

The original weighted 216 model is $W_p=[(1+6\theta)F_p]_{z=1/2}$. The standard finite Picard–Fuchs differential operator is

$$
\mathcal L=\theta^3-z(\theta+\tfrac12)(\theta+\tfrac13)(\theta+\tfrac23).
$$

**Theorem (every prime p>3).** The exact terminal valuation and residue are

$$
\boxed{v_p(c_{p-1})=3,\qquad c_{p-1}/p^3\equiv-1\pmod p.}\tag{1}
$$

The **exact finite polynomial** satisfies

$$
\mathcal L F_p(z)
=-c_{p-1}(p-\tfrac12)(p-\tfrac23)(p-\tfrac13)z^p
\equiv-\frac{p^3}{9}z^p\pmod{p^4}.\tag{2}
$$

At the frozen $z=\tfrac12$:

$$
\boxed{[\mathcal L F_p](1/2)/p^3\equiv-1/18\pmod p.}\tag{3}
$$

The original **last weighted coefficient** (index $k=p-1$) is

$$
\boxed{(6p-5)c_{p-1}2^{-(p-1)}\equiv5p^3\pmod{p^4}.}\tag{4}
$$

For both frozen target prime classes $p\equiv13,19\pmod{24}$, $p\ge13$, the right-hand normalized residues (3) and (4) are nonzero. Thus the differential equation is homogeneous modulo $p^3$ and has a fixed signed first forcing coefficient modulo $p^4$; omitting the final weighted term is safe modulo $p^3$, but **not** modulo $p^4$.

## Exact algebraic proof

For any of the three numerator Pochhammer parameters $(r,d)=(1,2),(1,3),(2,3)$,

$$
(r/d)_{p-1}=d^{-(p-1)}\prod_{j=0}^{p-2}(dj+r).
$$

There is precisely one index in $0,\ldots,p-2$ whose factor equals $\mu p$ for $\mu\in\{1,2\}$; its p-valuation is exactly one. All other factors represent the nonzero residues modulo $p$ with precisely the residue $r-d$ (from the omitted index $j=p-1$) absent. Wilson and Fermat give

$$
\frac{(r/d)_{p-1}}p\equiv\frac{\mu}{d-r}\pmod p.
$$

For $(r,d)=(1,2)$, $\mu=1$. For $(1,3)$ and $(2,3)$ the pair of $\mu$ values is $(1,2)$ for $p\equiv1\pmod3$ and $(2,1)$ for $p\equiv2\pmod3$. Therefore the product of the three normalized numerator residues is $1\cdot(\mu_1/2)\cdot\mu_2=1$. Wilson gives $((p-1)!)^3\equiv-1\pmod p$, proving (1) and exact valuation three.

The coefficient recurrence

$$
n^3c_n=(n-1+\tfrac12)(n-1+\tfrac13)(n-1+\tfrac23)c_{n-1}
\quad(1\le n<p)
$$

cancels every coefficient of $\mathcal L F_p$ except the $z^p$ boundary. This proves the exact equality of (2). The product of the three terminal factors modulo $p$ is $-1/9$, which combined with $c_{p-1}\equiv-p^3\pmod{p^4}$ gives (2). Fermat's $2^{-p}\equiv1/2$ and $2^{-(p-1)}\equiv1\pmod p$ yield (3) and (4).

Every division by $p$ is made only after the relevant p-integrality is established. All products carry their original signs, p-valuations, and source branches.

## Actual exact validation

The linked independent Python checker uses two independent coefficient pathways: (i) the modular Pochhammer recurrence and (ii) the exact binomial formula using arbitrary-precision integers. It checks *every* polynomial coefficient of $\mathcal L F_p$, from $z^0$ through $z^p$, modulo $p^4$, and both $z=1/2$ residue formulas. Executed for $p=5,7,11,13,17,19,23,37,43,73,373$: **11/11 PASS**. At $p=373$, the normalized residual coefficient is $290\pmod{373}$, and its value at $z=1/2$ is $145\pmod{373}$. The full all-prime statement rests on the algebraic proof, not the finite scan.

Artifact: research_notes/portable_direct/d25_W216_terminal_boundary_20261110.py.

## BRC / mother-target and durability

The observer is the *original* last weighted $W_p$ branch, not an unsigned convolution or a fitted replacement. A premature quotient modulo $p^3$ suppresses the force that becomes observable only modulo $p^4$. The exact parent LIFT interface remains

$$
\Delta_p-R_p\equiv(W_p-p)/p^2\pmod p
\quad(p\equiv13,19\pmod{24}),
$$

under frozen accepted UR and the earlier author-side signed-cutoff bridge; that bridge and the native experiment are **not** newly proved here. In particular $p=373$ has the original $\Delta_{373}=R_{373}=196$, not zero.

Fresh control continuation: request onhour11-20261110-0500-current-continuation, SUCCEEDED at 2026-11-09T21:02:50Z, control Source cb21c9452f5bc094493cd92bfa37be99ab988782. The own recovery_status call was refused with SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED. No own winning CLAIM/open run or formal Source checkpoint is verified; this proof is an author-side immutable research note.

**Highest native outstanding unit:** original-class fixed H0/B0 divided-power $[X]U\bmod139129$ at $p=373$, native rank, semilinear Frobenius direction, $\eta$, signed odd Green/Hesse branch, $\kappa$, original $\Delta_p-R_p$ and independent reproducibility. Issue #1559 remains OPEN / PENDING_OWNER. The comparison against the external Hesse candidate norm 122102 is conditional on actual authenticated native rank-one identification and $\eta$.

**Next discriminating actions:** an authorized native executor must run the exact frozen H0/B0 object and publish reproducible operator data. On a separate authorized portable mathematical route, test whether a finite WZ/Picard–Fuchs telescope for the original weighted $W_p$ retains the sharp $z^p$ boundary and exposes $(W_p-p)/p^2$ without deleting provenance. Do not re-run accepted UR, previous WZ/Green results, or broad finite scans. Research and Maintenance conversation IDs, proof/source pin, accepted old Results and owners remain separated.
