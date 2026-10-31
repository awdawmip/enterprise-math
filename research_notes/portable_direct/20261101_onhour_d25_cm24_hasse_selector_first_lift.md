# D25: CM(-24) Hasse selector and exact first lift for p ≡ 19 (mod 24)

**2026-11-01, AUTHOR-SIDE / MATHEMATICAL PROOF USING CLASSICAL CM THEORY / EXACT FINITE CHECK / UNREVIEWED / NOT_ADMITTED.**  Task: SECOND-DIGIT-LIFT. Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3. Reuses the finite beta Legendre identities in Enterprise Math commits 42da097851a02b96f8ff2018f5c28096eec13866 and 993a408982a302265cb3c31f93e69e4751299500.

## Theorem A — universal finite-field zero selector

For any prime p>3, let m=(p-1)/2, n=floor(m/2) and
\[
F_p(z)=\sum_{k=0}^{p-1}\frac{(1/8)_k(3/8)_k}{(k!)^2}z^k,\quad
G_p=F_p(1/9),\quad H_p=[(1+16z\partial_z)F_p(z)]_{z=1/9}.
\]
All coefficients are p-integral rational numbers. Set \(\chi_{-6}(p)=({-6}/p)\). Then, **using the known Hilbert class polynomial for discriminant -24 and Deuring's classical CM reduction criterion**, we prove
\[
\boxed{G_p\equiv0\pmod p\ \Longleftrightarrow\ \chi_{-6}(p)=-1.}
\]
At every such inert prime \(H_p\not\equiv0\pmod p\). Both D25 target classes p≡13,19 (mod 24) are inert. This settles the selected Legendre mod-p zero with an explicit observer, without asserting a mod-p² annihilation.

## Proof of the exact Hasse/Legendre interface

Work over \(K=\mathbb Q(\sqrt2)\) and put
\[
u_0=\frac12-\frac{\sqrt2}{3},\quad
t_0=1-2u_0=\frac{2\sqrt2}{3},\quad
4u_0(1-u_0)=\frac19.
\]
Consider \(E_u:Y^2=X^3+2X^2+uX\) with discriminant \(\Delta=64u^2(1-u)\). Since \(u_0(1-u_0)=1/36\), the curve has good reduction at every prime p>3 of K, including degree-two residue-field primes.

The actual Hasse coefficient (not a scalar stand-in for an X6 experiment) is
\[
\begin{aligned}
\mathcal A_p(u)&=[X^{p-1}](X^3+2X^2+uX)^m\\
&=[X^m](X^2+2X+u)^m\\
&=\sum_{j=0}^{n}\frac{m!\,2^{m-2j}}{j!^2(m-2j)!}u^j.
\end{aligned}
\]
Modulo p, -m≡1/2, and the double-step Pochhammer identity gives
\[
2^{-m}\mathcal A_p(u)\equiv
\sum_{j=0}^{n}\frac{(1/4)_j(3/4)_j}{(j!)^2}u^j
\equiv P_n(1-2u).
\]
For the second equality, use \(P_n(1-2u)={}_2F_1(-n,n+1;1;u)\): the unordered parameter pair {-n,n+1} equals {1/4,3/4} in \(\mathbb F_p\). The exact finite degree n<p makes every denominator a unit. Thus the displayed identity is coefficientwise, not only an equality of evaluated scalars.

The two previously proved beta Legendre ports combine, on setting z=4u(1-u) and t=1-2u, to the polynomial equality
\[
F_p(4u(1-u))\equiv
\begin{cases}
P_n(t),&n\ {\rm even},\\
t^pP_n(t),&n\ {\rm odd}
\end{cases}
\pmod p.
\]
The odd branch is the prior identity \((1-z)^{(p+1)/2}P_n(\sqrt{1-z})/\sqrt{1-z}\), because 1-z=t². At u=u₀ the factors \(2^{-m}\) and \(t_0^p\) are nonzero. Therefore \(G_p=0\bmod p\) if and only if \(\mathcal A_p(u_0)=0\bmod p\), equivalently the good reduction of \(E_{u_0}\) is supersingular. This reduction respects the actual quadratic Frobenius embedding when \(\sqrt2\notin\mathbb F_p\).

The standard elliptic invariant is
\[
j(E_u)=\frac{64(4-3u)^3}{u^2(1-u)}.
\]
Exact arithmetic yields
\[
j(E_{u_0})=2417472+1707264\sqrt2.
\]
Direct substitution verifies that this is a root of the *known* Hilbert class polynomial
\[
H_{-24}(J)=J^2-4834944J+14670139392.
\]
It follows from the classification of CM j-invariants that \(E_{u_0}\) has CM by the maximal order of \(\mathbb Q(\sqrt{-6})\), whose fundamental discriminant is -24. By Deuring's CM reduction criterion, at every good p>3 its reduction is supersingular precisely when \(\chi_{-6}(p)=-1\), and ordinary when \(\chi_{-6}(p)=+1\). This proves the theorem for all primes p>3.

References for the *external* (not newly discovered) inputs: Hilbert polynomial -24 at https://numberdb.org/Hilbert_class_polynomials and https://oeis.org/A305474 ; Deuring criterion background at https://en.wikipedia.org/wiki/Supersingular_prime_%28algebraic_number_theory%29 ; an independent -24 CM curve catalogue at https://www.lmfdb.org/EllipticCurve/2.2.8.1/81.1/b/2 . The new step is the source-faithful identification of this particular beta observer with the Hasse coefficient.

## Theorem B — unit partner and universally determined nonzero p-linear lift

The polynomial \(F_p\bmod p\) is nonzero (constant coefficient 1) and of degree <p. It solves its Gauss equation
\[
[z(1-z)D^2+(1-\tfrac32z)D-\tfrac3{64}]F_p=0\pmod p.
\]
At z₀=1/9 the leading coefficient z₀(1-z₀) is a unit. A double zero there would, by comparing the first nonzero coefficient in the Taylor expansion (its leading factor r(r-1) is nonzero for 2≤r<p), force \(F_p\equiv0\), contradiction. Hence whenever \(G_p=0\bmod p\), \(F_p'(z_0)\ne0\), so \(H_p=G_p+16z_0F_p'(z_0)\ne0\bmod p\).

For p≡19 (mod 24), the already proved *term-by-term* beta Clausen overflow has \(T_{\beta,p}\equiv0\bmod p^2\), and the exact source relation is
\[
B_p=G_pH_p-T_{\beta,p},
\quad
B_p=\sum_{k=0}^{p-1}(8k+1)
\frac{\binom{4k}{2k}\binom{2k}{k}^2}{2304^k}.
\]
Guo–Zudilin's proved 2019 theorem says \(B_p\equiv p(-3/p)\bmod p^3\); here \((-3/p)=+1\). Consequently \(G_pH_p\equiv p\bmod p^2\). Together with Theorem A and the unit-partner lemma:
\[
\boxed{v_p(G_p)=1,\qquad (G_p/p)H_p\equiv1\bmod p,\qquad
G_p/p\equiv H_p^{-1}\bmod p.}
\]
This is a universal nonzero first-lift formula for the entire p≡19 (mod24) target branch. Guo–Zudilin's external source: https://arxiv.org/abs/1803.01830 (Advances in Mathematics 346, 2019). The original 216 model and its stronger p⁴ affine bridge are not claimed solved.

For p≡13 (mod24), Theorem A likewise identifies the Gauss factor G (not H) as the mod-p zero, but the candidate \(G_p\equiv0\bmod p^2\) remains a separate open defect/carry problem; CM supersingularity by itself does not supply that higher-digit conclusion.

## Typed BRC/observer implications and exact execution

Carrier: the original p-integral beta coefficients, signed derivative weights, quadratic base-field embedding, and p-adic valuation. Observers: \(G_p\bmod p\), \(H_p\bmod p\), and for p≡19 the extra observer \(G_p/p\bmod p\). The CM inert/split bit is a proven safe quotient for the **Boolean G-zero observation only**. It does not preserve the first-lift value without H and the full signed boundary; for p=19,43,67,139 the first-lift residues are respectively 9,20,14,69. Frobenius embeddings, prime class, sign and valuation remain source labels. This does not create a new native X6 spatial dimension or satisfy the original fixed-373 benchmark.

Actually executed two equivalent standard-library integer validation implementations. The concise published program d25_cm24_compact_certificate_20261101.py checks **all 667 primes 5≤p≤5000** for CM zero selection (334 inert / 333 split), **all 166 primes 5≤p≤997** for *coefficientwise* Hasse/Legendre and finite beta observer congruence over \(\mathbb F_p[\sqrt2]\), and **all 29 primes p≤1500 with p≡19 (mod24)** for sourcewise signed tail p² and \(G_p/p\cdot H_p=1\bmod p\). All assertions passed locally. Representative exact values (p, G mod p², H mod p, G/p mod p) are (19,171,17,9), (43,860,28,20), (67,938,24,14), (139,9591,137,69). Finite checks validate these ranges and implementations; the all-prime results follow from the explicit proofs and named classical inputs. No formal proof checker or native fixed-373 H0/B0 divided-power/Frobenius execution took place.

## Recovery packet

Parent: original full weighted 216 congruence \(A_p\equiv p\bmod p^3\) for p≡13,19 (mod24). The stronger conjecture \(A_p-2B_p+p\chi_{-3}(p)\equiv0\bmod p^4\) remains OPEN. Immutable new frontier: CM(-24) selector, inert-branch unit-partner proof, and p≡19 nonzero first-lift inverse formula. Do not redo previous beta Legendre ports or high three valuation/reflection sectors. Next action: on p≡13 (mod24), prove or falsify the mod-p² beta defect/carry cancellation; next parent bridge is the joint original 216/2304 finite WZ/CM with signed tails. Fixed-373 original H0/B0 divided-power, semilinear Frobenius, rank, signed Green/Hesse, kappa and independent replication remain NOT_EXECUTED/PENDING_OWNER on Enterprise Math issue #1559.

Research logical lane: chatgpt-research-onhour-enterprise-math-20260923; maintenance lane not used. Read-only original recovery request research-onhour-20261031-0202-recovery-r15 (#6632) supplied no winning CLAIM/run; the exact dispatch request research-onhour-20261031-0205-dispatch-r15 (#6633) has final FAILED / UPSTREAM_CODE_REVIEW_REQUIRED. The current gateway's read-only status shows research_authority_granted=false, executor_binding_configured=false, CODE_REVIEW_REQUIRED. No repeat mutation, new dispatch, session assumption, Source checkpoint, Result or independent review is claimed. Research-Activity REGISTER_PENDING; native Source CHECKPOINT_PENDING. Earlier neutral staging remains separate from accepted sources. P000 and ACTIVE Heartbeat World unchanged; project proof is author-side and NOT_ADMITTED.
