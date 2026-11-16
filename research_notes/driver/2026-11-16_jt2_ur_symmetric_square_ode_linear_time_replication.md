# JT2 UR — Symmetric-square Legendre ODE recurrence, linear-time exact convolution replacement

Date: 2026-11-16. Status: PROVED ALGEBRAIC COEFFICIENT RECURRENCE + EXACT FINITE REPLICATION. All-prime UR norm–jet identity remains OPEN.

## Scientific target and provenance

For each prime \(p\le20000\), \(p\equiv13,19\pmod{24}\), set \(m=(p-1)/6\) and \(Q_m(Y)=P_{2m}(\sqrt{Y})\), where \(P_n(1)=1\) is the ordinary Legendre polynomial. Work with \(Y=1/2\), with coefficients of \(Q_m\) computed mod \(p^2\).

Set \(u=Q_m(1/2)/p\pmod p\) when \(Q_m(1/2)\equiv0\pmod p\), \(d=Q_m'(1/2)\pmod p\), and

\[
J_m(1/2)=\sum_{r=0}^{2m}\frac{[Y^r]Q_m(Y)^2}{2r+1}\,2^{-r}\pmod p,
\qquad \varepsilon_p=18ud-2J_m(1/2)-3\pmod p.
\]

The prior ODE coefficient recursion and 575-prime finite replication were saved by Driver \(`EM-DVR-DEBB5E`\) at [6137c925](https://github.com/awdawmip/enterprise-math/blob/6137c92545d752896731c764a13cf9d1c1cf7468/research_notes/driver/2026-11-16_jt2_ur_ode_coefficient_recurrence_full_575_exact_replication.md). This new author-side extension computes the coefficients of \(Q_m^2\) from a **third-order symmetric-square ODE**, replacing the quadratic-time pairwise convolution by a linear-time recurrence. Preserve original JT2 target ownership \(`EM-JT2-EF9380`\), earlier scoped independently accepted review \(`EM-DVR-57CCCE`\), and other original contributor IDs; this note is not an independent native review.

## The exact recurrence

For an integer \(m\ge1\), put \(C=m(2m+1)\), \(q(Y)=Q_m(Y)\), \(w(Y)=q(Y)^2=\sum_{r=0}^{2m} b_rY^r\). The Legendre ODE becomes

\[
2Y(1-Y)q''+(1-3Y)q'+Cq=0.
\]

For a generic ODE \(a q''+b q'+c q=0\) with constant \(c\), differentiation and elimination of \(q''\) give the polynomial **symmetric-square equation**

\[
a^2w'''+3ab w''+
(ab'-a'b+2b^2+4ac)w'+(-2a'c+4bc)w=0.
\]

Substitute \(a=2Y(1-Y)\), \(b=1-3Y\), \(c=C\). Dividing the resulting polynomial identity by \(2Y\) in \(\mathbb Q[Y]\), then clearing denominators, yields

\[
(2Y-4Y^2+2Y^3)w'''+(3-12Y+9Y^2)w''
+[4(C-1)+(6-4C)Y]w'-2Cw=0.
\]

Comparing the coefficient of \(Y^r\) gives, for \(0\le r\le2m-2\),

\[
\boxed{\begin{aligned}
&(r+2)(r+1)(2r+3)b_{r+2}\\
&\quad+4(r+1)\bigl(C-(r+1)^2\bigr)b_{r+1}\\
&\quad+(2r+1)\bigl(r(r+1)-2C\bigr)b_r=0.
\end{aligned}}
\]

Initial conditions are \(b_0=c_0^2\) and \(b_1=2c_0c_1\), where

\[
c_0=(-1)^m\binom{2m}{m}4^{-m},\qquad
c_1/c_0=-m(2m+1).
\]

The preceding two-term ODE coefficient recurrence constructs \(c_j\pmod {p^2}\). The boxed three-term recurrence constructs \(b_r\pmod p\) using only \(b_0,b_1\). For admissible \(p=6m+1\), all divisors used by either recursion and by \(J_m\) belong to \(\{1,\ldots,4m+1\}\subset\mathbb Z_p^\times\). Thus both recurrences are valid modulo \(p\), and the \(p^2\) coefficient construction is valid. No zero test is assumed: \(Q_m(1/2)\bmod p\) is checked before defining \(u\).

This proves an **\(O(m)\) modular-arithmetic algorithm** for each prime, including all coefficients required for \(J_m(1/2)\). Memory is \(O(m)\) because of one shared modular-inverse table (the new squared-polynomial recurrence itself retains only two previous coefficients). The older explicit pairwise convolution took \(O(m^2)\) arithmetic steps.

## Validation and reproducibility

The complete declared finite set of **575** primes \(p\le20000\) was recomputed with the new Python3 symmetric-square implementation. Exact results:

```
SUMMARY hi=20000 total=575 cmfails=0 e_nonzero=0
```

The **entire 575-row CSV and header** is byte-identical to the prior independently constructed Legendre-ODE coefficient-generation scan: SHA-256
`68e56352cd3a36f877068b6bf3ba222228716950b64dc34a7d33445536d454f0`.
This checks all finite \(u,d,J,\varepsilon_p\) values, not merely the final vanishing count. The Python implementation uses integer modular arithmetic only, with inverse existence justified above. The general symbolic recurrence was also directly compared with exact rational polynomial squaring for \(m=1,\ldots,9\).

Execute from repository root:

```sh
python3 experiments/jt2_ur_symmetric_square_linear_scan_20261116.py --limit 20000 --csv > /tmp/jt2_symmetric_square.csv
sha256sum /tmp/jt2_symmetric_square.csv
```

Published code: [exact symmetric-square scanner](https://github.com/awdawmip/enterprise-math/blob/c85bc86513f34ad75ea07d7bd27224057029d923/experiments/jt2_ur_symmetric_square_linear_scan_20261116.py).

## Mathematical significance and the open target

This is a distinct identity for the symmetric square of the Legendre solution and an asymptotically faster exact finite scanner. The full 575-prime evidence is reproduced byte-for-byte and now depends on two distinct coefficient-generation representations. The all-prime statement \(\varepsilon_p=0\) for admissible primes is still an open mathematical obligation. The recurrence makes a modular telescoping or creative-telescoping attack on \(J_m\) possible without explicit quadratic convolution.

Completion classification: one proved general polynomial identity; one finite exhaustive computational replication on the stated prime interval; no independent Native Result acceptance, formal Task completion, or JT2 parent closure.
