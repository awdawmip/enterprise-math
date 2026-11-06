# D25 — Universal Clausen defect and complementary-index finite-field reflection

Date: 2026-11-06. Lane: TASK_RESEARCH, portable author-side science. Mathematical status: AUTHOR-PROVED EXACT ALGEBRA; 81-PRIME FINITE EXACT CHECK; UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT.

Mother task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; original frozen scientific input `c47e13e4aba0e006366f989d6334d443f6333ae3`. This extends the previously proven four-shell and Clausen second/third-jet results; those established units are not recredited.

## 1. General all-order defect theorem

For \(j\ge0\), work over \(\mathbb Q[[t]]\). The previous signed jets are

\[
M_j(t)=(-1/2)^j\frac{j!}{(1-3t)_j}\prod_{s\in\{a,b,c\}}\binom{s+t}{j},
\qquad
C_j(t)=(-1/2)^j
\frac{\prod_{s\in\{a,b,c\}}\prod_{r=0}^{j-1}(s+t-r)}
{j!(1-t)_j(1-2t)_j}.
\]

The exact ratio is a universal unit independent of the numerator parameters \(a,b,c\), *even when their product has zero constant term*:

\[
\boxed{M_j(t)=R_j(t)C_j(t),\qquad
R_j(t)=\prod_{h=1}^{j}\frac{(h-t)(h-2t)}{h(h-3t)}.}
\]

Write \(H_j^{(n)}=\sum_{h=1}^j h^{-n}\). Then

\[
\boxed{\log R_j(t)=\sum_{n=2}^{\infty}
\frac{3^n-1-2^n}{n} H_j^{(n)}\,t^n.}
\]

For \(R_j=\sum_{n\ge0} E_{j,n}t^n\), the all-order triangular recurrence is

\[
\boxed{nE_{j,n}=\sum_{k=2}^{n}
(3^k-1-2^k)H_j^{(k)}E_{j,n-k},\quad
E_{j,0}=1,\ E_{j,1}=0.}
\]

It follows that

\[
E_{j,2}=2H_j^{(2)},\quad E_{j,3}=6H_j^{(3)},\quad
E_{j,4}=16H_j^{(4)}+2(H_j^{(2)})^2.
\]

The new **fourth-jet Clausen defect** is therefore

\[
\boxed{
[t^4](M_j-C_j)=
2H_j^{(2)}[t^2]C_j+
6H_j^{(3)}[t]C_j+
\left(16H_j^{(4)}+2(H_j^{(2)})^2\right)C_j(0).
}
\]

For a prime \(p\ge5\) and \(0\le j<p\), all formulas through \(n<p\) reduce correctly in \(\mathbb F_p\). We do not divide by \(n=p\).

**Proof:** After cancelling the common numerator only as a formal polynomial factor, the displayed multiplicative identity is exact and does not require its invertibility. For each \(h\), take the formal logarithm of \((1-t/h)(1-2t/h)/(1-3t/h)\); the linear term vanishes. Summing over \(h\) gives the logarithmic series. Differentiate \(R=\exp(\log R)\) and compare coefficients, giving the recurrence and fourth-order identity. Every required denominator is invertible in characteristic \(p\) for \(n,j<p\).

## 2. Exact complementary-index reflection theorem

**For every prime \(p\ge5\) and \(0\le j<p\), as rational functions in \(\mathbb F_p(t)\):**

\[
\boxed{R_j(t)\,R_{p-1-j}(-t)=1-t^{p-1}.}
\]

**Proof:** Reindex the missing factors \(h=j+1,\dots,p-1\) by \(h=-k\bmod p\), \(k=1,\dots,p-1-j\). Their factors are precisely those in \(R_{p-1-j}(-t)\). Thus the product is \(R_{p-1}(t)\). For each \(u=1,2,3\), Fermat's theorem and the factorization of \(X^{p-1}-1\) give

\[
\prod_{h=1}^{p-1}(h-ut)=(ut)^{p-1}-1=t^{p-1}-1,
\quad \prod_{h=1}^{p-1}h=-1.
\]

Therefore
\[
R_{p-1}(t)=\frac{(t^{p-1}-1)^2}{-(t^{p-1}-1)}
=1-t^{p-1}.
\]
The identity is in the rational function field and remains valid as a formal series at \(t=0\).

For \(2\le n<p-1\), complementarity also yields
\[
H_{p-1-j}^{(n)}=(-1)^{n+1}H_j^{(n)}\pmod p.
\]
Thus the all-order Clausen defects cancel multiplicatively under the involution \((j,t)\mapsto(p-1-j,-t)\) below degree \(p-1\), with the **exact critical residual** \(-t^{p-1}\). This is not a claim that the entire D25 weighted signed sum cancels.

## 3. Source/observer application and exact finite check

For the frozen target primes \(p\equiv13,19\pmod{24}\), write \(p=6m+1\). The weighted observer \(D=1+6z\partial_z\) loses the coefficient at \(j_*=m\) modulo \(p\). The new reflection pairs its Clausen defect with \(p-1-m\); one must keep both labelled source coordinates and their carry-shell provenance before evaluating a scalar sum.

At \(p=13,19,373\), the exceptional labelled tuple
\((j_*,M_{j_*}(0),H_{j_*}^{(2)},[t^2](M_{j_*}-C_{j_*}))\bmod p\)
is, respectively,
\((2,6,11,2)\), \((3,8,4,7)\), and \((62,122,124,43)\).
The weighted output of this one coordinate vanishes modulo \(p\), but its unweighted higher jets remain visible.

The accompanying standalone verifier `d25_allorder_clausen_complementary_20261106.py` uses separately recurred \(M_j,C_j\), harmonic-number \(R_j\) coefficients, and the reflection product. **81/81 primes PASS:** all 80 primes \(5\le p\le421\) and \(p=1009\), every \(0\le j<p\), all Taylor coefficients through \(t^4\); the \(p=5\) exceptional critical term \(-t^4\) is checked. These finite tests are supporting exact checks, not the all-prime proof.

## 4. Frozen mother objective and immediate research continuation

Next, try a labelled \((j,p-1-j)\)-paired finite telescope for
\[
\Theta_p=W_p/p-Z+S/6
\]
in the \(G=0\) and \(G\ne0\) branches, starting with \(p=13,19,373\). Test the actual weights, binomial support and carry layers; a universal identity for the unweighted multiplier \(R_j\) alone does **not** establish that telescope. If a pairing fails, preserve the exact residual as a new observer datum and pursue other routes.

The frozen target remains \(\Delta_p-R_p\equiv0\pmod p\) for \(p\equiv13,19\pmod{24}\). Authentic native original-class H0/B0, \([X]U\bmod p^2\), Frobenius \(\eta,\kappa\), and independent review remain separate unsatisfied obligations. BRC action: COMPOSE_APPLIED on source-labelled signed shells; no positive-mass engine or native CM experiment executed. No claim/open or formal Result is asserted.
