# D25/LIFT: finite-field tail formula and an exact cancellation at p=157

Date: 2026-11-10. Status: **AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED**. This is an author-portable mathematical result, not a native Source CLAIM, Result or independent review. Parent task: \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`; frozen science \`c47e13e4aba0e006366f989d6334d443f6333ae3\`, original interface \`research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md\` (blob \`cf36004694dc2c8c9134e2e1e989c076b88e4c03\`). This result consumes, without recrediting, the previously established three-block p-adic valuation lemma and second-digit correction identity.

## Theorem: one-field-digit formula

For every prime \(p\ge13\) with \(p\equiv13,19\pmod {24}\), let
\(a=(p-1)/6\), \(b=(p-1)/3\), \(B_0=1\), and
\[
B_{k+1}=B_k\frac{(6k+1)(3k+1)}{36(k+1)^2}\quad(0\le k<p-1).
\]
The frozen scalar interface supplies \(g=\sum_{k=0}^{p-1}B_k\), \(h=\sum_{k=0}^{p-1}(12k+1)B_k\), \(p\mid g\), \((g/p)h\equiv1\bmod p\). Write \(S_2=\sum_{k=b+1}^{p-1}B_k\) and \(\varepsilon=(-1)^{(p-1)/2}\). All inverses below are in \(\mathbb F_p\):
\[
\boxed{\quad h\equiv\mathcal H_p:=\sum_{j=0}^{a}(12j+1)2^{-j}{a\choose j}{b\choose j}\pmod p,\quad}
\]
\[
\boxed{\quad S_2/p^2\equiv\mathcal T_p:=
\frac{\varepsilon}{18}\sum_{k=b+1}^{p-1}
\left(2^kk^2{k-1\choose a}{k-1\choose b}\right)^{-1}\pmod p.\quad}
\]
Every denominator is nonzero because \(k<p\), \(a,b<k\), and all factorials used in these binomials are \(p\)-units.

The previous exact three-block lemma defines \(\Delta_p=((g/p)h-1)/p\) and its \(S_2\)-omitting counterpart \(\Delta_p^{\le b}\) modulo \(p\), and proves their difference equals \((S_2/p^2)h\pmod p\). Therefore
\[
\boxed{\Delta_p-\Delta_p^{\le b}\equiv\mathcal H_p\mathcal T_p\pmod p.}
\]
This computes the tail contribution **entirely in \(\mathbb F_p\)**, without computing the full \(B_k\) to precision \(p^3\).

### Proof

The exact recurrence is \(B_k=(1/6)_k(1/3)_k/[2^k(k!)^2]\). Since \(1/6\equiv-a\) and \(1/3\equiv-b\pmod p\), for \(j\le a\):
\[
B_j\equiv 2^{-j}{a\choose j}{b\choose j}\pmod p.
\]
All later terms have valuation at least one, proving the \(\mathcal H_p\) formula.

For each \(b<k<p\), the first rising factorial has exactly one factor \(p/6\), at index \(a\), and the second has exactly one \(p/3\), at index \(b\). Dividing by \(p^2\), reducing the remaining factors modulo \(p\), and using
\[
\prod_{j\ne a,\ 0\le j<k}(j-a)=(-1)^a a!(k-a-1)!,\qquad
\prod_{j\ne b,\ 0\le j<k}(j-b)=(-1)^b b!(k-b-1)!
\]
gives
\[
\frac{B_k}{p^2}\equiv\frac{(-1)^{a+b}a!b!(k-a-1)!(k-b-1)!}{18\cdot2^k(k!)^2}
=\frac{\varepsilon}{18\cdot2^kk^2{k-1\choose a}{k-1\choose b}}\pmod p.
\]
Sum over \(k>b\), then apply the already established tail correction identity. This is a complete symbolic proof under the original scalar interface.

## Exact cancellation prime: p=157

Here \(a=26,b=52\), \(p^2=24649\), \(p^3=3869893\). Two exact integer constructions (modular recurrence versus integer numerator/denominator product followed by modular reduction) agree at every \(k<p\):
\[
(S_0,S_1,S_2)\equiv(3416477,2606200,0)\pmod{p^3},
\]
\[
S_2\equiv286372082=74\cdot p^3\pmod{p^4}.
\]
Thus \(v_p(S_2)=3\), whereas **each** tail summand \(B_k\) has \(v_p(B_k)=2\). In particular \(\mathcal T_{157}=0\) but \(\mathcal H_{157}=h\bmod p=80\ne0\). The scalar values are
\[
G_p=g/p\equiv13712,\quad h\equiv13111\pmod{24649},\quad
\boxed{\Delta_{157}=\Delta_{157}^{\le52}=82\pmod{157}}.
\]
This is an exact example of *between-term cancellation* in the valuation-two tail. It rules out the possible generalization that this tail always contributes nontrivially to the second digit; it does not invalidate the previous eight nonzero examples or decide \(\Delta_p\stackrel{?}=R_p\).

## Reproducible finite checks and continuation

A field-only implementation uses \(\mathcal T_{b+1}\) above and the recurrence
\[
\mathcal T_{k+1}=\mathcal T_k (k-a)(k-b)/(2(k+1)^2)\pmod p,
\]
with the standard linear modular-inverse table. The isolated tail observer takes \(O(p)\) field operations and \(O(p)\) storage; this is not a claim about the complete native H0/B0 experiment or bit complexity.

The independent original modulo-\(p^3\) recurrence and the finite-field formula agree for all **45 admissible primes below 1000**, including the eight previous corrections \((9,6,10,3,46,51,110,197)\) at \((13,19,37,43,61,67,211,373)\). A finite-field formula scan over all **312 admissible primes \(\le10000\)** finds a unique zero at \(p=157\); this zero is independently recomputed at \(p^3\) and \(p^5\). This is a finite scan, not an all-prime uniqueness theorem.

Author-portable companion artifacts: \`verify_d25_tail_field_v1.py\`, \`check_p157_tail_zero.py\`, \`scan_tail_10000.py\`, three JSON certificates and verification log, in \`D25_TAIL_FINITE_FIELD_P157_PORTABLE_20261110.zip\` (local bundle SHA-256 \`a3d82896d969c5eab9534fb9b18cfc9e4992269fadd75f7af18ab94403553b97\`).

**Next unit:** obtain the actual original-class fixed H0/B0 divided-power module, semilinear orientation and native normalization, then evaluate \(R_{157}\) at the frozen source and compare to \(\Delta_{157}=82\). Preserve signed/odd branch provenance. Missing native CLAIM/session capability and missing original four-file UR V2 bundle remain separate writer/provenance tasks. UR V2 target: 94687 bytes, SHA256 \`4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76\`; its mathematics is already complete and is not recomputed here.
