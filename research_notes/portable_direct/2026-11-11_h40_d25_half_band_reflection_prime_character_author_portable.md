# D25/LIFT — Exact half-band reconstruction modulo p^4

**2026-11-11 · TASK_RESEARCH · AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED.**

Source: `awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3` (immutable science pin). Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`; parent `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION` still OPEN. This is a new application of the earlier author-proved harmonic reflection lemma, not a renewed claim of that lemma or a native H0/B0 result.

## Theorem (HB4)

For **all primes p >= 7 with p = 6m+1**, define in the p-adic integers
\[
a_k={(2k)!(3k)!\over216^k(k!)^5},\quad W_p=\sum_{k=0}^{p-1}(6k+1)a_k,\quad L_p=\sum_{j=0}^{3m}(6j+1)a_j.
\]
For \(2m<j\le3m\), \(A_j=a_j/p\) is a p-unit. Put \(H_n=\sum_{i=1}^n i^{-1}\pmod p\), \(Q_p(216)=(216^{p-1}-1)/p\pmod p\), and \(D_p(j)=2H_{2j-1}+3H_{3j-p-1}-5H_{j-1}-Q_p(216)\pmod p\). Then
\[
\boxed{
W_p\equiv L_p+
p^2\sum_{j=2m+1}^{3m}{(1+6p-6j)(1+pD_p(j))\over36j^3A_j}
+p^3\sum_{j=1}^{2m}{6j-1\over18j^3a_j}
\pmod{p^4}.}\tag{HB4}
\]
The middle sum is computed modulo p² and the last modulo p. All displayed denominators are p-units in their ranges. The formula is an exact observer reduction for the weighted sum at the stated precision; the higher-index coefficients' signed provenance is preserved through explicit repair coordinates.

## Proof

The source recurrence is \(a_0=1,\ a_{k+1}/a_k=(2k+1)(3k+1)(3k+2)/[36(k+1)^3]\). For \(k<p\), Legendre's formula gives \(v_p(a_k)=\lfloor2k/p\rfloor+\lfloor3k/p\rfloor\), hence valuations \(0,1,2,3\) on the successive ranges \([0,2m]\), \([2m+1,3m]\), \([3m+1,4m]\), \([4m+1,6m]\).

Reuse the proved two-digit reflection identity (R2), for \(1\le j<p\):
\[
{a_ja_{p-j}\over p^3}\equiv
-{(-1)^{q_2+q_3}q_3!(2-q_3)!\over36j^3}
(1+p[2H_{r_2-1}+3H_{r_3-1}-5H_{j-1}-Q_p(216)])\pmod{p^2},
\]
where \(q_2=\lfloor2j/p\rfloor,q_3=\lfloor3j/p\rfloor,r_2=2j-q_2p,r_3=3j-q_3p\). The exact source of R2 (not recredited) is [the 2026-11-11 harmonic lift](https://github.com/awdawmip/enterprise-math/blob/597ec5477d44563ac7073328183bac472ebd42ab/research_notes/portable_direct/2026-11-11_h40_d25_reflection_p2_harmonic_lift_author_portable.md).

In \(2m<j\le3m\), \(q_2=0,q_3=1\), giving \(a_{p-j}/p^2\equiv(1+pD_p(j))/(36j^3A_j)\pmod{p^2}\). In \(1\le j\le2m\), \(q_2=q_3=0\), giving \(a_{p-j}/p^3\equiv-1/(18j^3a_j)\pmod p\). Finally, the *exact* index involution yields
\[
W_p-L_p=\sum_{j=1}^{3m}(1+6p-6j)a_{p-j}.
\]
Apply the respective reflected formulas, respecting the two- and one-digit precisions. In the middle range retain the \(6p\) term; in the high range reduce its weight modulo p. This produces HB4. □

Reduction modulo p³ yields the exact **HB3** identity
\[
\boxed{W_p\equiv L_p+p^2\sum_{j=2m+1}^{3m}{1-6j\over36j^3A_j}\pmod{p^3}.}
\]
Thus the frozen-class uniform claim \(W_p\equiv p\pmod{p^3}\) for \(p\equiv13,19\pmod{24}\) has a precise remaining lower-half/reciprocal-middle finite-WZ target. HB3 is a proved equivalence; the universal target itself remains open in this author line.

## Exact finite checks and arithmetic semantics

A standalone exact integer modular-recurrence verifier exhaustively checked **611 primes** \(7\le p\le10000,\ p\equiv1\pmod6\) (312 in the frozen p mod24 classes, 299 additional). All **480983** mirrored middle terms were checked modulo p², all **961966** high terms checked modulo p, and all 611 complete W reconstructions agreed modulo p⁴ (1,442,949 reflection checks). Direct factorial coefficient crosschecks for \(p=7,13,19,31,73,157,373\) agreed.

| p | L mod p⁴ | middle mod p² | high mod p | W mod p⁴ |
|---:|---:|---:|---:|---:|
| 13 | 24687 | 75 | 5 | 19786 |
| 19 | 127091 | 161 | 4 | 82327 |
| 157 | 249127600 | 23177 | 96 | 584354000 |
| 373 | 7176413322 | 68898 | 278 | 11832087049 |

A separate exact finite check on **all 1227 primes** \(5\le p\le10000\) confirmed \(W_p\equiv p\) for \(p\equiv1\pmod3\) (611 instances) and \(W_p\equiv-p\) for \(p\equiv2\pmod3\) (616 instances), modulo p³. This is a **bounded exact computation**, not a proof for arbitrary primes or a novelty assertion.

The BRC carrier is the indexed rational signed weighted sequence, observer \(W_p\bmod p^4\), allowed later operation reduction to mod p³. Repair terms preserve the differing p-adic valuation blocks, index involution, and cancellation data; native Frobenius or shifted observers are not quotiented by this identity.

The runnable two verifiers and full 611-row/1227-row JSON certificates are delivered in the companion portable ZIP. Local original source checks: half-band verifier SHA256 `407407a9e98d9c1a4fde6b0c2651206bf2c5343aafd26fb8e4bf1c6215d4fc7b`, half-band certificate `4f5c51183bd310747f17eb5ca46aa3c27ca22da4953bb81eef856658b4dfcc95`, character verifier `950eac36741b71433d51a35e72c9ab8ea8306d91df1538186a99d5c3d8f724e5`, character certificate `aa653ca457f9fa064c26a37988cd289777dce13af9cf583b44d41c4b76f7a908`. ZIP SHA256 `a5f48d5d691aa28aa976bbe5755870b90db77f9b9f3f021b486ef2bfa5bdb085`.

**Boundary and next action.** Author evidence is UNREVIEWED / NOT_ADMITTED; the native original-class H0/B0 Frobenius experiment requires its lawful Source session/CLAIM and remains unrun. The UR V2 original four-file package (94,687 bytes, SHA256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`) has not been recovered, and its completed mathematics should not be recomputed. Next portable action: construct a finite paired/WZ certificate for HB3's explicit lower-half-plus-middle sum.
