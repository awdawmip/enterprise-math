# D25 / SECOND-DIGIT-LIFT — factorial form of the original Clausen cutoff

Date: 2026-10-30 (Asia/Hong_Kong). TASK_RESEARCH logical lane: **chatgpt-research-onhour-enterprise-math-20260923**, distinct from CONTROL_PLANE_MAINTENANCE. Mother: **ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION**. Task: **RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT**. Publication: **TP2-B6F4FC938FF94941C1B7**. Frozen scientific Source pin **c47e13e4aba0e006366f989d6334d443f6333ae3** unchanged.

**Classification:** AUTHOR-SIDE / EXPLICIT ALL-PRIME FACTORIAL CUTOFF CERTIFICATE / EXECUTED EXACT ORIGINAL-BINOMIAL REGRESSION / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.

**Scope and originality:** The previously published [2026-10-26 original-source alignment](20261026_onhour_d25_native_lift_source_port_identity.md), immutable commit **2d7bdfd7821d3afac8eaefb4b88bfedca8ff46be**, already proved both the truncated Clausen identity and **Q/p² ≡ R_p (mod p)** on frozen target classes. The present work provides an **explicit factorial, two-index formula for that same pre-existing cutoff**, a direct valuation proof, a second provenance-preserving reconciliation to frozen R, and a new independent exact original-binomial checker. It does **not** claim to invent the already established LIFT equivalence.

## Original object, coefficient identity and signed observer

For each prime \(p=6m+1\ge7\), in \(\mathbb Z_{(p)}\), let
\[
 A_p=\sum_{n=0}^{p-1}(6n+1)\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n},\qquad
 g_k=\frac{(1/6)_k(1/3)_k}{(k!)^2},\qquad
 G_p(z)=\sum_{k=0}^{p-1}g_k z^k.
\]
Write \(x=G_p(1/2)\), \(y=G'_p(1/2)\), and \(B_k=g_k2^{-k}\).
The classical **Clausen** identity of formal power series over \(\mathbb Q\) is
\[
 {}_2F_1(1/6,1/3;1;z)^2
 ={}_3F_2(1/2,1/3,2/3;1,1;z).
\]
Every coefficient of degree \(n<p\) is exactly identified, with its original \(216\) denominator and **signed weight \(6n+1\)**, so
\[
 A_p=x^2+6xy-Q,\qquad
 Q=\sum_{\substack{0\le i,j<p\\i+j\ge p}}
 (6(i+j)+1)\,B_i B_j. \tag{1}
\]
This is an exact rational identity: \((1+6\theta)G_p(z)^2\), \(\theta=z\,d/dz\), evaluated at \(z=1/2\), is \(x^2+6xy\). The cutoff \(Q\) preserves the original **ordered pair** of source indices and may not be discarded.

## Explicit factorial high-source formula

The exact \(p\)-adic valuation of \(g_k\) is
\[
 v_p(g_k)=
 \begin{cases}
 0,&0\le k\le m,\\
 1,&m<k\le2m,\\
 2,&2m<k<p.
 \end{cases} \tag{2}
\]
Indeed \((1/6)_k\) gains one factor \(p/6\) when \(k\ge m+1\), and \((1/3)_k\) gains one factor \(p/3\) when \(k\ge2m+1\). The factorial denominator remains a \(p\)-unit for \(k<p\).

For \(2m<k<p\), isolate **both exact factors of \(p\)** before reducing modulo \(p\):
\[
 \boxed{\frac{g_k}{p^2}\equiv c_k:=
 \frac{(-1)^m m!(2m)!(k-m-1)!(k-2m-1)!}
 {18(k!)^2}\pmod p.} \tag{3}
\]
Every factorial in (3) has index below \(p\). For the low source \(0\le i\le m\),
\[
 g_i\equiv\binom mi\binom{2m}{i}\pmod p. \tag{4}
\]
The retained cutoff pairs \(i+j\ge p\) have total valuation at least \(2\). Their valuation equals \(2\) **only** for a low/high pair with \(1\le i\le m,\ p-i\le j<p\), or its transpose. Hence, uniformly for every prime in the declared \(p=6m+1\) class,
\[
 \boxed{Q/p^2\equiv\tau_p\pmod p},\qquad
 \boxed{\tau_p=
 2\sum_{i=1}^{m}\sum_{k=p-i}^{p-1}
 (6(i+k)+1)\binom mi\binom{2m}{i}\,
 \frac{(-1)^m m!(2m)!(k-m-1)!(k-2m-1)!}
 {18(k!)^2}\,2^{-(i+k)}
 \pmod p.} \tag{5}
\]
The sum is *triangular*, retains the original port labels \((i,k)\), and contains only denominators invertible modulo \(p\).

Combining (1) and (5) gives the exact coefficientwise reduction
\[
 \boxed{A_p\equiv x^2+6xy-p^2\tau_p\pmod{p^3}.} \tag{6}
\]

## Exact reconciliation with the already frozen original R port

The 2026-10-26 author note independently proved
\[
 R_p=2\sum_{i=1}^{m}B_i\sum_{a=1}^{i}(1+6(i-a))C_a
 \equiv Q/p^2\pmod p,\quad
 C_a\equiv B_{p-a}/p^2\pmod p. \tag{7}
\]
The current explicit high-source expression gives \(B_{p-a}/p^2\equiv2^{-(p-a)}c_{p-a}\) and the low expression gives \(B_i\equiv2^{-i}\binom mi\binom{2m}{i}\). Reindex (5) by \(a=p-k\) to obtain \(1\le a\le i\le m\), and note
\[
 6(i+k)+1=6(i-a+p)+1\equiv6(i-a)+1\pmod p.
\]
Therefore (5) equals the **same** original \(R_p\) term-by-term modulo \(p\):
\[
 \boxed{\tau_p\equiv
 2\sum_{i=1}^{m}B_i\sum_{a=1}^{i}(1+6(i-a))C_a
 =R_p\pmod p.} \tag{8}
\]
This is an exact, source-matched identification, not an inference from matching numerical residues. Equations (1), (6), (8) are an independently checkable **factorial realization of the previous cutoff theorem**, not a separate novel proof of LIFT.

## Remaining second-digit obligation

The previously derived and source-aligned target CM/Hasse condition is \(G_p(1/2)\equiv0\pmod p\) for \(p\equiv13,19\pmod{24}\). Set \(h=x/p\in\mathbb Z_{(p)}\). From (6),
\[
 \boxed{A_p\equiv6ph y+p^2(h^2-\tau_p)\pmod{p^3}.} \tag{9}
\]
The still-open universal LIFT is consequently equivalent to
\[
 \boxed{6h y+p(h^2-\tau_p)\equiv1\pmod{p^2}
 \quad(p\equiv13,19\pmod{24}).} \tag{10}
\]
The accepted D24 first digit implies \(6hy\equiv1\pmod p\), so equivalently \((6hy-1)/p+h^2-\tau_p\equiv0\pmod p\), where the \(p\)-local division precedes reduction. This is the **previously known joint product/cutoff criterion in explicit factorial coordinates**, not an all-prime solution to it.

## Actually executed, exact and reproducible

Python standard-library integer checker:
**research_notes/portable_direct/d25_a216_twofactor_clausen_boundary_20261030.py**.

The program was actually run and compared independent original \((6n+1)\binom{2n}{n}^2\binom{3n}{n}/216^n\) integer-binomial sums with (6), checking both factorial (3) and original signed cutoff (5). It **also independently recomputes the frozen original reflected scalar** from the separate \(C_1=1/10\), \(C_{a+1}/C_a=36a^2/[(6a+5)(3a+2)]\) recurrence and asserts \(R_p=\tau_p\pmod p\) on every tested prime. **All 45 primes** with \(7\le p<500,\ p\equiv1\pmod6\) passed, including **23 target-class primes**. A separate fixed-\(p=373\) run also passed.

| \(p\) | \(m\) | \(G_p(1/2)\bmod p^3\) | \(G'_p(1/2)\bmod p^2\) | \(\tau_p\bmod p\) | \(A_p\bmod p^3\) |
|---:|---:|---:|---:|---:|---:|
| 13 | 2 | 988 | 1 | 0 | 13 |
| 19 | 3 | 1596 | 344 | 12 | 19 |
| 373 | 62 | 24495656 | 78545 | **196** | 373 |

The nonzero \(p^2\tau_p\) contribution at 19 and 373 is essential to the original \(p^3\) arithmetic. This check is **finite exact evidence**, not a proof of (10) for every target prime.

BRC resolution: **COMPOSE_APPLIED**. The state carrier is the original signed convolution indexed by \((i,k)\), valuations \(0/1/2\), exact factorials, and future observation \((1+6\theta)\) modulo \(p^3\). The equivalence to frozen \(R_p\) is justified by the explicit reindexing (7)–(8). This is external scalar arithmetic, not native X6/H0/B0 execution.

## Scientific and operational continuation

**Smallest remaining arithmetic unit:** prove or refute (10) uniformly on the frozen target classes using a joint \(p\)-adic Gauss value/derivative and the mandatory cutoff (5)/(8). Consume the accepted D24 first-digit, CM zero, earlier signed regular-tail and low two-zone sources; avoid repeating the already established Clausen/R equivalence.

**Separate original native benchmark:** Enterprise Math issue **#1559** requests the original fixed-\(p=373\) H0/B0 divided-power \([X]U\bmod139129\), actual semilinear Frobenius normalization, module rank, signed odd Green/Hesse, \(\kappa\), and independent replication. This author's scalar computation does not execute any such native experiment.

At 2026-10-30 read, the Site gateway reported **research_authority_granted=false**, **write_relay_enabled=false**, and Source sync **CODE_REVIEW_REQUIRED**; own checkpoint list returned **ACCESS_DENIED**. No Source-native Researcher identity, claim, open, run, checkpoint, Result, review or admission is asserted by project repository persistence. Existing unverified request identifiers were not replayed. Research and maintenance logical conversations remained isolated.
