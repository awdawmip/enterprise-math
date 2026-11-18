# R762EU — Ternary Lucas coefficient law and constant-size random-access BRC terminal shadow oracle

Date 2026-11-18. Parent RS-X6-TRIADIC-CLOSURE-DYNAMICS, frozen publication TP2-8B7E13C5904A2D6F1142. This is the **complete three-coordinate positive terminal model** with exactly six *named* branches (unit, X, Z, XY, YZ, XYZ), not signed or primitive native Cell/Link/Port events. Historical contributor lineage EM-X6-3050F6; this new portable note asserts no live CLAIM or Source publication. Mathematical review: **NOT_REVIEWED**.

## Precise statement and conditional boundary

Fix \(a\ge2,\ q=3^a,\ h=q/9\). In the three-coordinate group algebra let
\[
P=1+X+Z+XY+YZ+XYZ,\qquad
f_q(n)=\max(0,\lfloor 3n/q\rfloor-2),\qquad
S_q(n)=3^{-f_q(n)}P_q^n\bmod3\quad(n\ge0).
\]
The integrality and all-\(q\) lift needed for this normalized shadow were established in the **author-side, unreviewed antecedent R762ER**; they are explicit dependencies, not consequences of a finite test in this note.

Write \(n=hm+r\) with \(0\le r<h\). Write every global terminal as
\(x=hi+u,\ y=hj+v,\ z=hk+w\), \(0\le i,j,k<9\), \(0\le u,v,w<h\).
Let \(c_r(u,v,w)\) be the coefficient of \(X^uY^vZ^w\) in the *unwrapped* six-branch polynomial \(P^r\bmod3\).

**Theorem A — unconditional exact digit identity in the declared positive-terminal branch algebra.** Write \(r=\sum_{\ell}r_\ell3^\ell\), \(u=\sum_\ell u_\ell3^\ell\), and similarly for \(v,w\). Put \(K_d=P^d\bmod3\) for \(d=0,1,2\). Then
\[
\boxed{c_r(u,v,w)=\prod_{\ell\ge0}[X^{u_\ell}Y^{v_\ell}Z^{w_\ell}]K_{r_\ell}\pmod3.}\tag{A}
\]
The \(K_0,K_1,K_2\) coefficient arrays have precisely \(1,6,18\) nonzero entries, respectively. \(K_2\) has six entries equal to 1, twelve equal to 2, and its coefficient of \(XYZ\) is zero modulo 3.

**Theorem B — block factorization, conditional on the exact R762ER lift.** Given
\(S_q(hm+r)=\iota_h(S_9(m))P_q^r\bmod3\) with \(\iota_h(X_9)=X_q^h\), etc.,
\[
\boxed{S_q(n)[hi+u,hj+v,hk+w]
      =S_9(m)[i,j,k]\,c_r(u,v,w)\pmod3.}\tag{B}
\]
Thus there is no sum over nine-by-nine-by-nine coarse indices: the observer separates into **disjoint coarse blocks**.

**Theorem C — random access, conditional also on the unreviewed R762ET q9 eventual-period result.** Define \(\rho(m)=m\) if \(m<8\), else \(\rho(m)=8+((m-8)\bmod18)\). The 26 vectors \(S_9(0),\ldots,S_9(25)\), each with 729 trits, suffice for any \(a\ge2\), any \(n\ge0\), and any one requested endpoint:
\[
\boxed{S_q(n)[x,y,z]=S_9(\rho(\lfloor n/h\rfloor))[i,j,k]\prod_\ell(K_{r_\ell})_{u_\ell,v_\ell,w_\ell}.}\tag{C}
\]
A five-trit-per-byte, row-aligned encoding uses \(26\lceil729/5\rceil=\boxed{3796}\) bytes of base-table data; the three 27-entry digit kernels need at most another 81 trits uncompressed. After parsing the input and forming the quotient/remainder of \(n\) by \(h\), each coefficient query requires \(a-2\) ternary-digit iterations and constant-time finite-kernel lookups per digit. This operation count excludes bit-complexity of arbitrary-precision integer operations on the supplied inputs. Enumerating the full \(q^3\)-component output necessarily requires \(\Omega(q^3)\) output work.

## Proof of the carry-free Lucas identity

By Frobenius in the characteristic-three polynomial algebra,
\[
P^r=\prod_\ell P(X^{3^\ell},Y^{3^\ell},Z^{3^\ell})^{r_\ell}
=\prod_\ell K_{r_\ell}(X^{3^\ell},Y^{3^\ell},Z^{3^\ell}).
\]
All six original named branch monomials have per-coordinate exponents 0 or 1; each \(r_\ell\le2\), hence every monomial of \(K_{r_\ell}\) has coordinate exponents at most 2. The factors' contributions therefore form the intended base-three digits **without any carries or competing digit decompositions**. Extracting a monomial coefficient yields (A).

For \(K_2\), enumerate the 36 ordered pairs of the six named branches. They produce 19 candidate exponent triples, of which the \(XYZ\) entry occurs six times and vanishes modulo 3; of the remaining 18 entries, six have residue 1 and twelve have residue 2. \(K_0\) has one term, \(K_1\) six. The companion program builds these kernels from the six named shifts and checks this enumeration; generic external propagation is not substituted.

## Proof of disjoint coarse blocks

Use the exact R762ER antecedent normalized lift. Every monomial of \(\iota_h(S_9(m))\) has each exponent divisible by \(h\). Every monomial of \(P^r\) has each exponent between 0 and \(r<h\). Consequently, the residue \((hi+u,hj+v,hk+w)\) can arise only from its indicated coarse triple and indicated fine triple; even modulo \(q=9h\), distinct blocks cannot overlap. The group-algebra product gives exactly (B). Apply the R762ET author-side periodicity \(S_9(m+18)=S_9(m)\) for \(m\ge8\), together with (A), to obtain (C).

## Reuse of R762ER support law and new exact ternary residue histograms

Let \(A_1(m)\), \(A_2(m)\) count residues 1 and 2, respectively, among the 729 entries of \(S_9(m)\). Define the *integer* products
\[
\sigma(r)=\prod_\ell s_{r_\ell},\quad(s_0,s_1,s_2)=(1,6,18),
\qquad
\delta(r)=\prod_\ell d_{r_\ell},\quad(d_0,d_1,d_2)=(1,6,-6).
\]
The digit-product kernel has \(\sigma(r)\) nonzero coefficients; the imbalance between counts of residues 1 and 2 is \(\delta(r)\). Multiplication by a nonzero coarse coefficient preserves or swaps these residue classes. With \(A=A_1(m)+A_2(m)\), \(D=A_1(m)-A_2(m)\),
\[
\boxed{\#\operatorname{supp} S_q(n)=A\,\sigma(r),}\tag{D}
\]
\[
\boxed{
\#\{S_q(n)=1\}=\frac{A\sigma(r)+D\delta(r)}2,\qquad
\#\{S_q(n)=2\}=\frac{A\sigma(r)-D\delta(r)}2.}\tag{E}
\]
**Novelty boundary:** Equation (D), the exact nonzero-support count, was already established in R762ER (Equation (4)); it is reproduced here as a consistency and bookkeeping identity, **not** as a new support theorem. The new refinements are the separate residue-1/residue-2 counts (E), the explicit digitwise coefficient oracle (A)–(C), its bounded 26-row encoding, and the direct per-coordinate verification against named-branch convolution.

For unbounded \(m\), replace \(m\) by \(\rho(m)\). This determines both the exact support and ternary residue histogram for any three-power modulus using one 26-row table and the base-three digits of \(n\bmod h\). In particular, \(q=27,n=26\) has \(\#\operatorname{supp}=324\cdot18=5832\).

## Reproducible validation and material scope

The standalone JS checker performs **14,400** nonwrapped exact coefficient tests for every \(0\le r\le14\), every \(0\le u,v,w\le r\); it separately computes 27 full q9 shadows (\(n=0,\ldots,26\)), 79 full q27 shadows (\(n=0,\ldots,78\)) by the original six named branches modulo \(3^7=2187\), and compares all \(79\cdot27^3=\mathbf{1,554,957}\) q27 terminal coefficients against (B). It also performs **3,710** arbitrary-precision integer oracle spot checks and 79 entire-vector support/signature checks; all passed. The modulus exceeds every needed normalization divisor through the checked ranges (maximum \(3^6\)). Boundary checks confirm \(S_9(8)=S_9(26)\) and \(S_9(7)\ne S_9(25)\). No floating-point, pi, trigonometry, Taylor/Pade/Cayley, continuous or signed-physics replacement is involved.

Companions: R762EU_LUCAS_ORACLE_VERIFY.js (reproducible algorithm and checks); R762EU_EVIDENCE.json (actual observed support counts, sample ternary residue histograms and verification coverage); R762EU_Q9_PACKED_TRITS.hex (the actual 3796-byte row-aligned compressed q9 lookup table as 7592 hex digits). Those three files and this proof must be read back from the GitHub branch before claiming publication.

**Evidence boundary:** The digit law (A), block uniqueness, and counting identities conditional on (B) are proved algebraically. The universal normalized lifting identity R762ER and the eventual-period theorem R762ET remain **NOT_REVIEWED**; neither all-q dependency is independently established by these q9/q27 finite checks. No formal proof checker or independent mathematical review is claimed. No legal primitive TRIADIC_CLOSURE_E permission, signed Cell/Link/Port provenance, native X6 transfer or V17/V29/V39 future-operation equivalence follows.

## Next research

Independently audit R762ER's normalized Frobenius/valuation step and R762ET's finite q9 spectral-annihilator certificate, since they are load-bearing for (B)–(E). In parallel, investigate a *provenance-retaining* finite-digit observer for future named signed operations; distinguish terminal path aggregation from lawful native event semantics. Investigate the compression lower bounds separately rather than claiming 3796 bytes is optimal.

## Exact antecedents

R762ER: https://github.com/awdawmip/enterprise-math/pull/2734, head 39787270e99ef3c698f43409b208dbe16b073ebb. R762ET: https://github.com/awdawmip/enterprise-math/pull/2740, head 38b098bf04149ee8fdb1da48fee00ffe62846064. Current method and version separation: docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context, docs/PORTABLE_RESEARCH_PROTOCOL.md and research_priorities/research_method.json. P000, ACTIVE worldview and frozen task science have not been repinned.
