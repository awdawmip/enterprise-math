# D25 — quartic Gauss-square Frobenius carry across the p-index boundary

Date: 2026-11-04. Author-side portable mathematical evidence; exact finite-field proof and finite independent checks; UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen scientific input c47e13e4aba0e006366f989d6334d443f6333ae3. This does not update task authority or native Source checkpoints. Research logical lane chatgpt-research-hourly-enterprise-math-20260923; maintenance logical lane chatgpt-hourly-enterprise-math-20260921 remains separate.

## Precise statement

Let p=8q+5 be prime, p>=5, put L=5q+3 and t=2q+1=(p-1)/4. Use the **original** quartic coefficient and its classical Clausen square root:

\[
v_k=\frac{(1/8)_k(3/8)_k}{(k!)^2\,9^k},\quad
b_k=\frac{(4k)!}{(k!)^4\,2304^k},
\quad
P_p(z)=\sum_{k=0}^{L}\overline{v_k}z^k,\quad
B_p(z)=\sum_{k=0}^{t}\overline{b_k}z^k
\]
in \(\mathbb F_p[z]\). The bar means reduction of a p-integral rational number, not an abstract p-adic native operation. For these indices all v_k and b_k displayed are p-units.

**Theorem (two-band Frobenius carry).** There is a unique nonzero \(\lambda_p\in\mathbb F_p\), explicitly
\[
\boxed{\lambda_p=\frac{\overline{v_L}^{\,2}}{\overline{b_t}},}
\]
such that the following exact polynomial identity holds in \(\mathbb F_p[z]\):
\[
\boxed{P_p(z)^2=B_p(z)(1+\lambda_pz^p).}\tag{1}
\]
Thus coefficients of \(P_p^2\) are \(\bar b_n\) for \(0\le n\le t\), zero for \(t<n<p\), and \(\lambda_p\bar b_{n-p}\) for \(p\le n\le p+t=2L\). In particular the upper triangle has a nonzero residue polynomial even when its **weighted evaluation** vanishes. The carrier exponent p is the first characteristic-p recurrence singularity; it is not a change to the frozen source or native X6 coordinate system.

**Weighted consequence.** Let \(c_n=[z^n]P_p(z)^2\). The discarded upper-triangle quartic Clausen observer, with the original \(8n+1\) weight, has the precise first-digit representation
\[
\boxed{\sum_{n=p}^{2L}(8n+1)c_n
=\lambda_p\sum_{s=0}^{t}(8s+1)\bar b_s\quad\text{in }\mathbb F_p.}\tag{2}
\]
The previously established Guo–Zudilin quartic supercongruence (the full weighted V sum is \(p(-3/p)\pmod{p^3}\), for p>3) implies \(\sum_{s=0}^t(8s+1)\bar b_s=0\). Hence the left side of (2) vanishes in \(\mathbb F_p\). This **mod-p vanishing** does not remove the mod-\(p^2\) triangle; the p=13 example has \(T_v\equiv1170\pmod{13^3}\), and \(T_v/p\equiv-1\pmod {13}\).

## Proof of (1)

1. For \(p=8q+5\), the first numerator factor divisible by p in \((1/8)_k\) occurs at index \(j=L=5q+3\), because \(8L+1=5p\). Thus \(v_k\) is a p-unit through k=L and \(v_{L+1}\equiv0\pmod p\). The Gauss differential operator \(\mathcal D=\theta^2-\frac z9(\theta+\frac18)(\theta+\frac38)\), \(\theta=z\,d/dz\), annihilates the **polynomial** \(P_p\) over \(\mathbb F_p\): all interior coefficient recurrences hold and the one missing top coefficient has the factor \(L+\frac18=5p/8=0\).
2. The classical Clausen symmetric-square identity transfers the second-order Gauss ODE into the third-order Picard–Fuchs ODE
\[
\mathcal L=\theta^3-\frac z9(\theta+\tfrac12)(\theta+\tfrac14)(\theta+\tfrac34).
\]
Consequently \(C(z):=P_p(z)^2\) satisfies \(\mathcal LC=0\) in \(\mathbb F_p[z]\). Writing \(C=\sum c_nz^n\) gives
\[
n^3c_n=\tfrac19(n-\tfrac12)(n-\tfrac34)(n-\tfrac14)c_{n-1}.\tag{3}
\]
3. For \(0\le n<p\), the exact rational Clausen convolution gives \(c_n=\bar b_n\), because all terms \(v_k\) with k>L vanish modulo p (and n<p). By Legendre's formula, \(v_p(b_n)=\lfloor 4n/p\rfloor\) for \(0\le n<p\). Hence \(c_n=b_n=0\) in \(\mathbb F_p\) for \(t<n<p\).
4. At n=p, the coefficient \(n^3=0\) in (3); the previous coefficient is already zero, so (3) places no constraint on \(c_p\). Set \(\lambda=c_p\). For \(1\le s\le t\), substituting n=p+s into (3) reduces exactly to the original b-recurrence for \(b_s\) in characteristic p, yielding \(c_{p+s}=\lambda\bar b_s\). Since \(2L=p+t\) and the top coefficient is \(c_{2L}=\bar v_L^2\), with \(\bar b_t\ne0\), this fixes \(\lambda=\bar v_L^2/\bar b_t\ne0\). Both sides have degree \(2L\), proving (1).

Equation (2) follows from \(8(p+s)+1=8s+1\) in characteristic p. The inference of weighted zero uses the named existing theorem, not a new independent proof of it.

## Exact checker, coverage, and next boundary

The accompanying standalone Python checker evaluates original rational recurrences in modular arithmetic. Executed locally: all 79 primes p<=2000 with p mod8=5 passed; the **entire polynomial** (1) was directly convolved and checked for all 51 primes p<=1200, while the 28 larger primes were checked at eight separated index positions, the top-coefficient formula, and the original weighted triangle separately modulo p². It also independently reconstructs low b_k by integer binomials for p<=101. Finite numbers are checks of the universal symbolic proof, not its replacement.

| p | lambda mod p | T_v/p mod p (exact computation) |
|---:|---:|---:|
| 5 | 1 | 1 |
| 13 | 10 | 12 |
| 29 | 16 | 1 |
| 37 | 4 | 36 |
| 61 | 27 | 60 |
| 373 | 290 | 372 |

A new finite pattern, **not proved here**, is \(T_v/p\equiv-(\!-3/p)\pmod p\) for all 79 tested primes. This would yield a concise second-digit triangle port: the missing universal obligation is a congruence for the finite Gauss square-and-derivative \(S_v^2+16S_vD_v\) modulo p², where \(S_v=\sum_{k<p}v_k\) and \(D_v=\sum_{k<p}kv_k\). The exact rational identity
\[
T_v=S_v^2+16S_vD_v-V_p
\]
holds at every p; the checker observes \(S_v^2+16S_vD_v=0\pmod{p^2}\) in its finite test, and the proved quartic V theorem supplies the remaining term. Next unit: prove this Gauss mod-p² cancellation for target p mod24=13,19, or locate a known theorem with exact source/scoping; preserve the p=13 triangle through the second digit. Do not re-prove the prior Clausen convolution or rename a finite observation as universal proof.

BRC/source observer: original ordered factor indices (i,j), original quartic denominators, all p-unit factor residues, mod-p convolution, the p-index Frobenius boundary, and the weighted z-derivative readout are retained separately. This is a valid classical finite-field result and is not a native H0/B0 X6 experiment.

Native control at last direct read: gateway 0.6.11 / UPSTREAM_CODE_REVIEW_REQUIRED / research_authority_granted=false / executor_binding_configured=false / 5 of 5 active jobs. No native CLAIM, authorized OPEN, Source checkpoint, Result, mathematical review or admission is represented by this author-side file. Support owner: enterprise-math issue 1558; native 373 issue 1559. Prior requests and protected staging untouched.
