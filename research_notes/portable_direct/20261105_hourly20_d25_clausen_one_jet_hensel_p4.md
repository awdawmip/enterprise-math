# D25 — Clausen one-jet Hensel lift through the fourth p-adic digit

Date: 2026-11-05 (+08). Exact task: \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; publication \`TP2-B6F4FC938FF94941C1B7\`. Frozen scientific input pin: \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. Author-side portable mathematical lemma; \`UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM\`.

## Statement and precision

Let p=6n+1>=7 be prime, x=1/2, u=p-1, and work in Z_(p) / p^4. Define the *terminating* polynomial

\[
G(z)={}_2F_1(-n,-2n;1-p/2;z),\qquad
\Psi(z)=G(z)\,[G(z)+12zG'(z)].
\]

Write \(g=G(x)\), \(v=G'(x)\) and let

\[
q_2=uv+\frac{2u^2}{9}g,\quad
q_3=(\frac{11u^2}{9}-2u+4)v+\frac{2u^3}{9}g,
\]

\[
q_4=(\frac{13u^3}{9}-6u^2+20u)v+
(\frac{22u^4}{81}-\frac{8u^3}{9}+\frac{32u^2}{9})g.
\]

These equal \(G''(x),G'''(x),G^{(4)}(x)\) **exactly**. Consequently all of the following are exact rational expressions in the single first jet \((p,g,v)\):

\[
f=\Psi(x)=g(g+6v),
\]

\[
A=\Psi'(x)=6v^2+(8+6p)gv+\frac43u^2g^2,
\]

\[
B=\frac12\Psi''(x)=\frac{26(v^2+gq_2)+18vq_2+6gq_3}{2},
\]

\[
C=\frac16\Psi'''(x)=
\frac{114vq_2+38gq_3+18q_2^2+24vq_3+6gq_4}{6}.
\]

**Theorem.** Suppose \(f\equiv0\bmod p\) and \(A\not\equiv0\bmod p\), as in the previous simple-root result for the relevant frozen first-digit classes. Define units and p-adic quotients at the *required* precision

\[
d=fA^{-1}\pmod{p^4},\quad b=BA^{-1}\pmod{p^2},
\quad c=CA^{-1}\pmod p.
\]

Then the unique root \(x_p\equiv x\bmod p\) of \(\Psi\) satisfies

\[
\boxed{x_p\equiv x-d-bd^2-(2b^2-c)d^3\pmod{p^4}.}
\]

All three nonconstant terms have well-defined precision: \(d\in p\mathbb Z_p\), so \(d^2\) requires \(b\bmod p^2\), and \(d^3\) requires \(c\bmod p\). Merely substituting the previous \(b\bmod p\) into the fourth-digit formula would lose a needed source coordinate.

**Universal branch-level cubic coefficients.** On the simple-root locus precisely one of the following holds:

- \(G\)-branch \(g\equiv0\), \(v\not\equiv0\bmod p\):
  \[
  b\equiv2/3,\quad c\equiv58/27,\quad 2b^2-c\equiv-34/27\pmod p.
  \]
- \(L\)-branch \(g+6v\equiv0\), \(g\not\equiv0\bmod p\):
  \[
  b\equiv10/3,\quad c\equiv70/27,\quad 2b^2-c\equiv530/27\pmod p.
  \]

Thus the **first jet** \((p,g,v)\) through \(p^4\) and the determined branch suffice to reconstruct the root through \(p^4\); explicit evaluation of \(G''\), \(G'''\) or \(G^{(4)}\) at x is unnecessary in the reconstruction. The independent checker nevertheless evaluates them to test the proof. This is a scope-typed compression for this \(\Psi\) observer, not a compression of the original signed six-port or native H0/B0 data.

## Proof

The Gauss equation is

\[
z(1-z)G''+[1-p/2-(1-3n)z]G'-2n^2G=0.
\]

At \(x=1/2\), its coefficient of \(G'\) is \(-u/4\); \(a(x)=1/4\), \(a'(x)=0\), \(a''(x)=-2\), \(b'(x)=(u-2)/2\). Differentiating the same equation zero, one and two times gives successively \(q_2,q_3,q_4\) as displayed. Direct product differentiation of \(\Psi=G^2+12zGG'\) then gives A, B, C, with no assumed modular identity.

Write \(\delta=x-x_p\in p\mathbb Z_p\). Taylor's theorem for this polynomial yields
\(0=f-A\delta+B\delta^2-C\delta^3\bmod p^4\). Divide by the unit A:
\(d=\delta-b\delta^2+c\delta^3\). Formal inversion in the nilpotent ideal \(p\mathbb Z/p^4\) gives \(\delta=d+bd^2+(2b^2-c)d^3\bmod p^4\). Hensel uniqueness follows because A is a p-adic unit.

For the branch coefficients, reduce \(u\equiv-1\bmod p\), \(q_2\equiv-v+2g/9\), \(q_3\equiv65v/9-2g/9\), \(q_4\equiv-247v/9+382g/81\). Substitution into A,B,C and then \(g=0\) or \(v=-g/6\) gives the four constants. The exact \(b\bmod p^2\) remains available from B/A and retains the first-jet/source dependence necessary for p^4. QED.

## Independent finite exact check (not the general proof)

The companion \`d25_clausen_one_jet_hensel_p4_20261105.js\` was based on a separately run BigInt checker using modular rational coefficient recurrence, one-pass streaming derivatives through order four and a second evaluation at the reconstructed root. The independent test of all 94 primes \(7\le p\le1200\), \(p\equiv1\bmod6\), produced **94/94 PASS** for derivative identities, branch cubic constants, and \(\Psi(x_p)=0\bmod p^4\). In that finite domain the first-digit premise and simple-root condition also held; those 94 tests are not the proof of the first-digit theorem outside the stated frozen target scope.

| p | branch | \(c\bmod p\) | \((2b^2-c)\bmod p\) | \(x_p\bmod p^4\) | \(\Psi(x_p)\bmod p^4\) |
|---:|:---:|---:|---:|---:|---:|
| 7 | L | 0 | 2 | 508 | 0 |
| 13 | G | 6 | 5 | 23888 | 0 |
| 19 | G | 12 | 10 | 62406 | 0 |
| 373 | G | 237 | 54 | 7348554128 | 0 |

The residues modulo \(p^3\) are respectively \(165,1918,675,31342631\), matching the prior one-jet proof's earlier precision.

## D25 continuation / provenance

Parent objective remains \(\Delta_p-R_p\equiv0\bmod p\) on the frozen target classes \(p\equiv13,19\bmod24\). This paper advances the **fourth-digit local Clausen branch operator**, which can be consumed by the earlier fourth-digit signed 216/2304 source decomposition without identifying those external coefficients with the original-class crystalline H0/B0 carrier.

Next exact local scientific unit: derive a signed fourth-digit source interface \(W_p-\Psi(x)\bmod p^4\), preserving full derivative/harmonic and valuation-port data, then compare its induced root/displacement corrections at \(p=13,19,373\). The broader uniform \(W_p\equiv p\bmod p^3\) proof, genuine native p373 H0/B0, \([X]U\bmod139129\), rank/Frobenius/\(\eta,\kappa\) and independent review remain separate open requirements. Do not count this author-side note as a canonical Source checkpoint, Result, review, admission, or native experiment.
