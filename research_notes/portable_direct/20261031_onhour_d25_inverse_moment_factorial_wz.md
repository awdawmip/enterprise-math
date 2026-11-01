# D25 / SECOND-DIGIT-LIFT — explicit terminating factorial form of the inverse Clausen strip

2026-10-31 Asia/Hong_Kong. Logical Research lane chatgpt-research-onhour-enterprise-math-20260923. AUTHOR-SIDE / PROVED EXACT FACTORIAL TRANSPORT / EXECUTED 330-PRIME EXACT CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_EXECUTED / REGISTER_PENDING. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3; P000 ACTIVE unchanged.

## Consumed prior result and precise question

Our earlier **same-turn** verified proof at EM commit 79a574c7bc6ce2ec8b2de65e99689e2d3d3254fc gave, for p=6l+1 prime, m=2l, h=3l, the original 216 coefficients
\[
a_n=\frac{(1/2)_n(1/3)_n(2/3)_n}{2^n(n!)^3}
\]
and the signed second-valuation strip
\[
\frac{S_2}{p^2}\equiv\mathcal I_p:=
\sum_{k=m+1}^h\frac{1-6k}{36k^3(a_k/p)}\pmod p.
\tag{1}
\]
Here every a_k/p is a p-unit. This is a source-preserving inverse-middle moment for the specific original weighted observer, not the native H0/B0 Frobenius computation.

**New question:** Can (1) be written as a bounded terminating hypergeometric sum with an explicit rational term-ratio and no hidden p-adic normalization, so a finite WZ/CM joint cancellation is directly testable?

## New all-prime exact factorial theorem

For 1≤j≤l, put k=m+j and
\[
C_p=h!\,(2m)!\,m!\in\mathbf F_p^\times.
\]
Then
\[
\boxed{\frac{a_{m+j}}p\equiv
\frac{C_p\,(j-1)!}
{3\,(l-j)!\,(m-j)!\,2^{m+j}((m+j)!)^3}\pmod p.}\tag{2}
\]
All factorials lie below p, so every denominator in (2) is a unit.

**Complete derivation.** Since p=6l+1 and m=2l, h=3l, the three exact p-adic parameter presentations are
\[
1/3=-m+p/3,\quad1/2=-h+p/2,\quad2/3=-2m+2p/3.
\]
In the range k=m+j≤h, modulo p we have
\[
(1/2)_k\equiv(-1)^k h!/(h-k)!,
\quad(2/3)_k\equiv(-1)^k(2m)!/(2m-k)!.
\]
For the once-crossed factor,
\[
\frac{(1/3)_{m+j}}p\equiv
\frac{(-m)_m}{3}\prod_{r=1}^{j-1}r
=\frac{(-1)^m m!(j-1)!}{3}\pmod p.
\]
The combined sign is (-1)^{2k+m}=+1 since m=2l. Substituting h−k=l−j and 2m−k=m−j gives (2).

Inverting (2), inserting into (1) and canceling the k³ factor against ((m+j)!)³ yields the *finite factorial moment*
\[
\boxed{\mathcal I_p\equiv\frac1{12C_p}
\sum_{j=1}^l(1-6m-6j)\,t_j\pmod p,}\tag{3}
\]
where
\[
t_j=\frac{2^{m+j}((m+j-1)!)^3(l-j)!(m-j)!}{(j-1)!}.
\tag{4}
\]
The term ratio is now an **exact rational hypergeometric identity**
\[
\boxed{\frac{t_{j+1}}{t_j}
=\frac{2(m+j)^3}{j(l-j)(m-j)},
\quad 1\le j<l.}\tag{5}
\]
All denominators are p-units in this range. This is a rigorous transformation of the original scalar strip observer, with exactly l=(p−1)/6 terms, not a proof that its value vanishes.

## Actual independent precision checks and labels

Executed research_notes/portable_direct/d25_inverse_moment_factorial_check_20261031.py using stdlib exact modular integer arithmetic, independently constructing original a_{m+j}/p via recurrence mod p² and the factorial closed form; checked (2) for **every j** in all **330 primes 7≤p≤5000 with p≡1 mod6**, including 166 frozen p≡13,19 mod24. It also independently compares every t_j to the exact (5) recurrence and checks (3) against the earlier source-preserving inverse moment (1). Terminal marker: PASS_D25_FACTORIAL_INVERSE_MOMENT.

Representative moment residues: p7→5, p13→10, p19→9, p37→20, p67→58, p157→98, p373→266. All tests are finite exact evidence; the **all-prime** identities (2)-(5) follow from the factorial algebra.

## Concrete continuation, BRC and responsibility

COMPOSE_APPLIED: original high-strip observer → first-valuation normalized coefficient u_k=a_k/p → finite factorial source with index j and signed weight (1−6m−6j). This transformation is lossless for the **declared scalar signed strip** modulo p, but not for all other future coefficient observers. The explicit recurrence (5) is a WZ-ready kernel; a Gosper-only scalar certificate is not assumed to exist.

The open original E.2 bridge remains
\[
(D_0+D_1)\equiv0\pmod{p^2},\qquad
\frac{D_0+D_1}{p^2}+
\frac1{12C_p}\sum_{j=1}^l(1-6m-6j)t_j\equiv0\pmod p.
\]
These global cancellations are **unproved**; an empirical finite match is not acceptance.

Highest-priority separate native benchmark #1559 remains OPEN/PENDING_OWNER for p373 actual original-class H0/B0 divided-power [X]U mod139129, rank, semilinear Frobenius/eta, signed odd Green/Hesse, kappa and independent replication. No native run or replacement. Original Research-lane recovery #6632: no verified own CLAIM/run. Original dispatch #6633: FAILED UPSTREAM_CODE_REVIEW_REQUIRED; no duplicate request. Stage SD-d7c23e7984c2ddaac60a neutral. Formal Source sync/register/review remains pending. Source scientific pin, identity and scheduler unchanged.

Next smallest mathematical action: use (5), with the declared signed boundary, to construct or refute a genuine *joint* finite WZ/telescoping certificate against (D0+D1)/p². Do not replace the remaining sum by its numerical zero or discard the original low E.2 source.
