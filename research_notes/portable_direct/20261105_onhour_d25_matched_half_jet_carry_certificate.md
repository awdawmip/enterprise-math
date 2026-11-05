# D25 / SECOND-DIGIT-LIFT — matched half-endpoint 2-jets and indispensable carry

Date: 2026-11-05. Task: \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; publication \`TP2-B6F4FC938FF94941C1B7\`; **immutable scientific input** \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. Research logical conversation \`chatgpt-research-onhour-enterprise-math-20260923\`. Classification: **AUTHOR-SIDE EXACT FINITE IDENTITIES / EXECUTED FINITE CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0**.

## Parent and consumed frontier

Frozen mother target is \(\Delta_p-R_p=0 \pmod p\) for \(p\equiv13,19\pmod{24}\). Previously derived source-aligned reduction gives the equivalent \(W_p-V_p=0\pmod{p^3}\), where
\[
W_p=\sum_{k=0}^{p-1}(6k+1)\frac{(1/2)_k(1/3)_k(2/3)_k}{2^k(k!)^3},\quad
V_p=\sum_{k=0}^{p-1}(8k+1)\frac{(1/2)_k(1/4)_k(3/4)_k}{9^k(k!)^3}.
\]
Consume Guo–Zudilin, *A q-microscope for supercongruences*, Adv. Math. 346 (2019), 329–358, arXiv:1803.01830v6: \(V_p\equiv V_H\equiv p(-3/p)\pmod{p^3}\), \(H=(p-1)/2\). Consume previous author-side, still unreviewed, half-endpoint source formula
\(W_p-V_p\equiv W_H-V_H+p^2C_A\pmod{p^3}\), with
\[
C_A=\sum_{H<k\le\lfloor(2p-1)/3\rfloor}(6k+1)
 \frac{(2k-p)!(3k-p)!}{216^k(k!)^5}\pmod p.
\]
Also consume accepted first-digit \(p^2\mid W_H-V_H\) on the target classes. No native rank/Frobenius input is claimed.

## New exact 2-jet construction — original A/B source labels retained

Let \(p=6n+1\) be prime, \(H=3n\). Write the three *original* Pochhammer parameters for each model in centered form \(\alpha=m_\alpha+p c_\alpha\), with integer \(m_\alpha\), rational \(c_\alpha\), as follows:

* A/216: \((-H,1/2),(-2n,1/3),(-4n,2/3)\).
* B/2304, \(p\equiv1\bmod4\), \(s=(p-1)/4\): \((-H,1/2),(-s,1/4),(-3s,3/4)\).
* B/2304, \(p\equiv3\bmod4\), \(s=(p-3)/4\): \((-H,1/2),(-(3p-1)/4,3/4),(-s,1/4)\).

Here \((m,c)\) denotes the parameter \(m+pc\). Let \(t_A=2,t_B=9\), weights \(w_A(k)=6k+1,w_B(k)=8k+1\). For \(0\le k\le H\), consider all three factor pairs \((m_\alpha+j,c_\alpha)\) with \(0\le j<k\). There are **at most one zero** among their integer first components; every nonzero first component is a \(p\)-unit. Put \(z_k=0\) or \(1\) for the zero count, and if \(z_k=1\), let \(c_{0,k}\) be its shift coefficient. Define the exact rational numbers
\[
R_k=\frac{\prod_{\alpha,j:\,m_\alpha+j\ne0}(m_\alpha+j)}{t^k(k!)^3},
\quad
L_k=\sum_{m_\alpha+j\ne0}\frac{c_\alpha}{m_\alpha+j},
\quad
J_k=\sum_{m_\alpha+j\ne0}\frac{c_\alpha^2}{(m_\alpha+j)^2}.
\]
Their denominators are \(p\)-units (for each fixed \(p,k\)). For either model \(\nu=A,B\), define three signed, provenance-labeled sums
\[
S_{0,\nu}=\sum_{k:z_k=0}w_\nu(k)R_k,
\]
\[
S_{1,\nu}=\sum_{k:z_k=0}w_\nu(k)R_kL_k
+\sum_{k:z_k=1}w_\nu(k)R_kc_{0,k},
\]
\[
S_{2,\nu}=\sum_{k:z_k=0}w_\nu(k)R_k(L_k^2-J_k)/2
+\sum_{k:z_k=1}w_\nu(k)R_kc_{0,k}L_k.
\]

**Theorem (exact polynomial-jet truncation, all target primes).** With \(\Xi_i=S_{i,A}-S_{i,B}\),
\[
W_H-V_H\equiv \Xi_0+p\Xi_1+p^2\Xi_2\pmod{p^3}.
\]
The required precision of the separate observables is only \(\Xi_0\bmod p^3,\ \Xi_1\bmod p^2,\ \Xi_2\bmod p\). This is a theorem about the exact frozen original coefficients and weights, not a fitted congruence. Proof: expand each nonzero factor as \(x(1+pc/x)\); collect the elementary symmetric degrees 0,1,2, using \(e_2=(L^2-J)/2\). If the unique integer zero occurs, factor its \(pc_0\) first, and keep only degrees 0,1 in the remaining product. All omitted terms have valuation at least 3. The explicit centered tuples guarantee the zero bound and p-unit denominators for \(k\le H\), on both residue classes.

Now take the **least nonnegative modular representatives** \(x_0\) of \(\Xi_0\bmod p^3\), \(x_1\) of \(\Xi_1\bmod p^2\), and \(x_2\) of \(\Xi_2\bmod p\). Accepted first-digit and the theorem imply \(x_0+p x_1\equiv0\pmod{p^2}\). The carry
\[
K_p=\frac{(x_0+p x_1)\bmod p^3}{p^2}\in\{0,\ldots,p-1\}
\]
is therefore exactly defined. Combine the proven half-endpoint transport to obtain the **one-finite-field-readout equivalent certificate**
\[
\boxed{W_p\equiv V_p\pmod{p^3}\quad\Longleftrightarrow\quad K_p+x_2+C_A\equiv0\pmod p.}
\]
All signed model branches, first two jet orders, zero-factor provenance, and the A upper valuation-two shell remain explicit. In particular, this removes all *per-term p^3 hypergeometric coefficient calculations* from the open certificate; the only p^3 object retained is the single deterministic carry from the zero/first jets. **Uniform vanishing of the displayed finite-field readout is NOT proved.**

**Discriminating counterexample to carry erasure.** For \(p=13\), \(K_{13}=12,\ x_2=4,\ C_A=10\); hence \(K+x_2+C_A=26\equiv0\pmod{13}\), whereas \(x_2+C_A=14\equiv1\pmod{13}\). A 'second jet plus upper shell only' proof is not even a valid candidate at \(p=13\). The carry cannot be quotient-erased. This negative statement applies only to this exact reduction, not to other potential representations or WZ certificates.

## Executed check and BRC observer scope

Independent programs computed matched jets using integer-centered factor products and sums of inverse factors, and half sums by the original rational hypergeometric recurrences; at p=13,19,139,373, the original binomial formulas were independently evaluated as well. For all **166 target primes p<=4999**, both A and B half-jet reconstructions agreed modulo p^3; first-digit carry was integral, matched the direct half-difference, and the open readout was zero. Failures=0. These checks validate the implementation and support (but do not prove) the remaining all-target supercongruence.

| p | x0 mod p³ | x1 mod p² | x2 mod p | Kp | CA | (Kp+x2+CA) mod p |
|---:|---:|---:|---:|---:|---:|---:|
|13|845|91|4|12|10|0|
|19|4864|29|14|15|9|0|
|139|447163|17077|119|7|13|0|
|373|17893183|134426|364|116|266|0|

**BRC operation:** a source-labeled, valuation-aware two-model jet/carry observer, composition by signed A−B and final output \(K+x_2+C_A\). Taking only the degree-2 jet is information-lossy (p13 is a verified counterexample); taking the single final zero scalar before retaining component identities erases the proposed WZ repair site. The classical p-adic calculations are an external exact arithmetic representation, not a new P000 native coordinate axiom.

## Next unfinished unit and native separation

Construct a p-parametric *terminating* 216↔2304 certificate for \(K_p+\Xi_2+C_A=0\), targeting the explicit carry \(K_p\) and the swapped B quarter-centering when p changes mod4. A candidate needs to match p13 and p19 before a general claim, and must retain A shell/zero-factor origins. The original same-class fixed-373 H0/B0 divided-power [X]U mod139129, module rank, native semilinear Frobenius, eta, kappa, signed Green/Hesse and independent replication are still NOT_EXECUTED; support issue #1559 is OPEN/PENDING_EXECUTOR. Portable jets do not satisfy that benchmark.

Original Source continuation receipt \`onhour11-20261105-1505-d25-own-read\` re-read SUCCEEDED, with \`execution_authorized=false\`. Own native session/CLAIM/run/Source checkpoint/Result are not established by this publication. Do not retry original queued request, borrow maintenance logical identity, or promote author-only evidence to accepted Result.
