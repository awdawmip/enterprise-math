# R762DZ — Exact leading cyclotomic spectrum and asymptotic content slope of full three-coordinate positive BRC

2026-11-18 (Asia/Shanghai). TASK RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142; original author identity EM-X6-3050F6; own lineage CLAIM MCP-d6d2c143cc4d2df4dea1c00c. Mathematical status: author proof and independently rerunnable modular evidence; independent review NOT_REVIEWED.

## Frozen scientific scope

Use P000 V5 from awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 and taskbook from @e3f42efac29a2da2d95be391f3231a664e2fade0. Reuse R762DN's full-three-coordinate lower bound without rederivation and R762DU–DY's previously completed modular BRC certificates.

Let Q=3^a with a>=2, d=3^(a-1). Let R_Q=Z[(C_Q)^3], P=1+X+Z+XY+YZ+XYZ, and let c_Q(n) be the gcd of the nonnegative integer coefficients in P^n. Denote nu_Q(n)=v_3(c_Q(n)). This is the same positive six-named-branch terminal observation, not a new primitive signed triadic event.

## Theorem: exact minimum cyclotomic valuation and its multiplicity

Fix a primitive Qth root of unity zeta in K=Q_3(zeta) and pi=zeta-1. Normalize v_3(3)=1. Then pi is a uniformizer with v_pi(3)=phi(Q)=2d, hence v_3(pi)=1/(2d).

For every character indexed by (i,j,k) in (Z/Q)^3, write lambda_ijk=P(zeta^i,zeta^j,zeta^k) and set
\[
D(i,j,k)=2ij+ik+2jk\pmod3.
\]
Then
\[
v_3(\lambda_{ijk})=1/d \quad\Longleftrightarrow\quad D(i,j,k)\ne0\pmod3.
\]
When D=0, v_3(lambda)>=3/(2d), with v_3(0)=infinity. In particular,
\[
\boxed{\min_{i,j,k}v_3(\lambda_{ijk})=1/d,\qquad
\#\{(i,j,k):v_3(\lambda_{ijk})=1/d\}=\frac{2}{3}Q^3.}
\]
The latter set includes exactly 18 of the 27 residue triples modulo three, repeated (Q/3)^3 times. Of the 27 triples, D has residue frequencies {0:9,1:6,2:12}.

**Proof.** Put x=X-1, y=Y-1, z=Z-1. The exact integral identity is
\[
P=6+3(x+y+z)+2xy+xz+2yz+xyz.
\]
For every integer r>=0, ((1+pi)^r-1)/pi is congruent to r modulo pi. Because v_pi(3)=2d>=6, after substituting X=zeta^i,Y=zeta^j,Z=zeta^k and reducing modulo pi^3, the constant, linear and cubic/higher terms vanish and
\[
P(zeta^i,zeta^j,zeta^k)\equiv
pi^2(2ij+ik+2jk)\pmod{pi^3}.
\]
The residue field is F_3. Therefore exactly the characters with D!=0 have v_pi(lambda)=2, while the others have v_pi(lambda)>=3. The finite residue count is exact by enumerating the 27 triples; the companion checker also verifies the coefficient through the independent six-branch binomial expansion. This proves the theorem.

An explicit minimal-valuation witness is (i,j,k)=(1,1,0), where
\[
P(zeta,zeta,1)=2(1+zeta+zeta^2)=2\,\frac{zeta^3-1}{zeta-1}.
\]
Since v_pi(zeta^3-1)=3 and v_pi(zeta-1)=1 for a>=2, this value has v_pi=2. QED.

## Corollary: uniform two-step enclosure and exact growth rate for the BRC content

For every integer n>=0,
\[
\boxed{\max\{0,\lfloor n/d\rfloor-2\}\le nu_Q(n)\le\lfloor n/d\rfloor.}
\]
Consequently for each fixed a>=2,
\[
\boxed{\lim_{n\longrightarrow\infty}\frac{v_3(c_Q(n))}{n}=\frac1d.}
\]
This slope is exact even before settling the R762DN pointwise all-horizon content conjecture.

**Proof.** The lower inequality is the previously saved R762DN Theorem B, which uses the finite C_3 group-ring and Frobenius lift. For the upper bound, if all coefficients of P^n were divisible by 3^t, evaluating the integer group-ring element at (zeta,zeta,1) would yield an algebraic integer in 3^t O_K. That evaluation is P(zeta,zeta,1)^n and has normalized v_3=n/d. Thus t<=floor(n/d). The squeeze bounds differ by at most two, proving the limit. R762DN also excludes all non-three prime factors of the content; thus c_Q(n)=3^nu_Q(n). QED.

## Exact verification, interpretation and next question

Companion R762DZ_VERIFY.py independently enumerates the 27 F_3 character leading terms directly from six branch monomials; it checks D and its 9/6/12 distribution. It also performs a direct six-shift cyclic positive-BRC recurrence in exact modular integer arithmetic for Q=9, n=1..54 and Q=27, n=1..108. For each n the checker tests both stated content inequalities and total-mass congruence; 324 modulus/valuation assertions plus 162 mass checks are exhaustive **only over those declared finite windows**. R762DZ_EVIDENCE.json contains expected boundary samples and byte hashes for the final arrays; no floating point or numerical roots are used.

The theorem is about the cyclotomic spectrum of the **candidate positive terminal full-three-coordinate BRC observer**. It does not supply native signed TRIADIC_CLOSURE_E Cell/Link/Port authorization or future-safe native event-state compression; the original X6 six-dimensional spatial carrier and provenance remain unchanged.

Next scientific frontier: resolve which of the at most three possible nu_Q(n) values is attained at every n (R762DN conjectures the lower endpoint for a>=2), potentially by converting the primitive-character valuation into a coefficient extraction witness; separately obtain the licensed native signed event predicate and V17/V29/V39 transport.