# D25 portable research: first omitted pole finite part for the upper B-chart

Status: \`AUTHOR_PORTABLE_PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT\`

Contributor lineage: \`EM-DIRECT-C4D02C\`

This is a portable mathematical unit. It claims no native session, CLAIM, run, canonical checkpoint, Result, review, or theorem admission.

## Source boundary and non-repetition

- Current global snapshot observed for this unit: \`chatgpt-global-knowledge@d1adcb6040a169a4b936a72f7e266109ac9ad9ec\`.
- Current Enterprise Math main observed for this unit: \`e99fb53f0a177112f7ff1362784f9f400e570f44\`.
- Canonical D25 progress blob remains \`51dd15a8142f3dda0506a306f9c0693a036f5891\`.
- Immediate portable predecessor is \`research_notes/d25_b_chart_q_endpoint_lift_20260929.md\`, blob \`ab117820a707ad17b10088510b44a16ef69ab491\`.
- This unit does not reopen the canonical normal-Dixon derivative, the raw complementary period, the \(k=3m\) tail, or the Gauss-Manin companion lane.

## 1. Setup

Let \(p=6m+1>3\) be prime. The upper \(B\)-chart is

\[
B_p=\sum_{j=0}^{2m-2} b_j,
\]

with

\[
b_0=\frac5{32},
\qquad
\frac{b_{j+1}}{b_j}
=
\frac{(j+1)(2j+5)(3j+4)(6j+11)}
{4(j+3)(2j+3)(3j+5)(3j+7)}.
\]

The predecessor note uses

\[
Q_j:=-\frac{(5/6)_j}{(2/3)_j}2^{-j},
\qquad
\delta_p:=\frac{Q_{2m-1}+8/3}{p}\pmod p,
\]

and proves

\[
\delta_p\equiv
-\frac43H_{3m}+\frac89H_{2m}-\frac49
\pmod p.
\tag{1}
\]

It reduces the still-open upper-chart target to

\[
B_p\stackrel?{\equiv}3-\frac34\delta_p\pmod p.
\tag{2}
\]

## 2. Exact term-to-carrier quotient

Direct cancellation of the Pochhammer term gives the exact rational identity

\[
\boxed{
\frac{b_j}{Q_j}
=
-\frac{(6j+5)(2j+3)}
{6(3j+4)(3j+2)(j+1)(j+2)}.
}
\tag{3}
\]

Set

\[
J:=2m-1=\frac{p-4}{3}.
\]

This is the first omitted term immediately after the \(B\)-chart. In (3), the factor \(3J+4=p\) shows that \(b_J\) has one explicit \(p\)-adic pole. Substitution gives the exact identity

\[
\boxed{
p\,b_J=A(p)Q_J,
\qquad
A(p):=
-\frac{(2p-3)(2p+1)}
{2(p-2)(p-1)(p+2)}.
}
\tag{4}
\]

The regular factor has the expansion

\[
A(p)=\frac38+\frac78p+\frac{15}{32}p^2+O(p^3).
\tag{5}
\]

Using \(Q_J\equiv-8/3+p\delta_p\pmod{p^2}\), equations (4)-(5) imply

\[
p\,b_J
\equiv
-1+p\left(\frac38\delta_p-\frac73\right)
\pmod{p^2}.
\tag{6}
\]

Therefore the Laurent finite-part digit

\[
\boxed{
\beta_p:=
\frac{p\,b_J+1}{p}\pmod p
}
\tag{7}
\]

is well-defined, and

\[
\boxed{
\beta_p\equiv\frac38\delta_p-\frac73\pmod p.
}
\tag{8}
\]

In particular the residue is universal:

\[
\boxed{
p\,b_{2m-1}\equiv-1\pmod p.
}
\tag{9}
\]

Combining (1) and (8),

\[
\boxed{
\beta_p
\equiv
-\frac12H_{3m}
+\frac13H_{2m}
-\frac52
\pmod p.
}
\tag{10}
\]

This is an all-prime consequence of the already-proved endpoint lift plus the exact quotient (3); no finite-prime scan is used in the proof.

## 3. Strict localization of the open bridge

Equation (2) is now exactly equivalent to

\[
\boxed{
B_p\stackrel?{\equiv}-2\beta_p-\frac53\pmod p.
}
\tag{11}
\]

Since \(\beta_p=(p b_J+1)/p\), the same open statement has the undivided form

\[
\boxed{
pB_p+2p\,b_{2m-1}+2+\frac{5p}{3}
\stackrel?{\equiv}0
\pmod{p^2}.
}
\tag{12}
\]

Thus the needed repair coordinate is not a generic period or a multi-moment vector. It is the finite part of the **first excluded singular term** at the valuation wall \(3J+4=p\).

The sum-to-endpoint problem has therefore been sharpened to:

\[
\text{regularized prefix }B_p
\quad\longleftrightarrow\quad
\text{first-pole residue/finite part of }b_J.
\]

The residue is already fixed by (9); only the finite part \(\beta_p\) remains in the open bridge.

## 4. One-step healing after the pole

At \(j=J\), the exact recurrence also gives

\[
\frac{b_{J+1}}{b_J}
=
p\,C(p),
\]

where

\[
\boxed{
C(p)=
\frac{(p-1)(2p+3)(2p+7)}
{4(p+1)(p+3)(p+5)(2p+1)}
=
-\frac7{20}+\frac{94}{75}p+O(p^2).
}
\tag{13}
\]

Combining (6) and (13),

\[
\boxed{
b_{2m}\equiv\frac7{20}\pmod p.
}
\tag{14}
\]

If

\[
\gamma_p:=\frac{b_{2m}-7/20}{p}\pmod p,
\]

then

\[
\boxed{
\gamma_p
\equiv
-\frac{94}{75}-\frac7{20}\beta_p
\pmod p.
}
\tag{15}
\]

So the simple pole is healed in one recurrence step: \(v_p(b_J)=-1\) and the next term is a \(p\)-unit with universal zeroth digit \(7/20\). The pole finite part is therefore the natural minimal coordinate; moving one step past the pole merely transports the same digit.

## 5. BRC typing

Population:
- regular upper-chart indices \(0\le j\le2m-2\);
- first excluded index \(J=2m-1\);
- one post-pole index \(2m\).

Retained carrier:
- \(B_p\);
- pole position/provenance \(3J+4=p\);
- residue \(p b_J\bmod p=-1\);
- finite part \(\beta_p\).

Safe compression proved here:
- the predecessor endpoint digit \(\delta_p\) may be replaced by \(\beta_p\) through (8);
- the harmonic target may be replaced by the finite-part target (11).

Unsafe compression:
- deleting the first omitted term because \(b_J\) is not \(p\)-integral;
- retaining only the residue \(-1\) and discarding the finite part.

Resolution:
\`COMPOSE_APPLIED / FIRST_EXCLUDED_POLE_FINITE_PART / VALUATION_AND_PROVENANCE_RETAINED\`.

## 6. Independent regression

A fresh dependency-free modular checker evaluates every prime

\[
p<10000,\qquad p\equiv1\pmod6,
\]

611 primes total.

It checks:
1. the predecessor \(Q_J\) endpoint lift input;
2. \(p b_J\equiv-1\pmod p\);
3. \(\beta_p=(3/8)\delta_p-7/3\);
4. the harmonic expression (10);
5. the one-step healed value \(b_{2m}\equiv7/20\pmod p\);
6. the first post-pole digit (15);
7. the still-conjectural regularized bridge (11)/(12) against direct \(B_p\).

Result:

\[
\boxed{611/611,\qquad0\ \text{failures}.}
\]

Items 2-6 have the finite algebra proof above. Item 7 remains falsification evidence only.

Checker:
\`research_notes/d25_b_chart_first_pole_finite_part_checker_20260929.py\`.

## 7. Exact next unit

Do not enlarge the state back to multiple moments and do not reopen the canonical D25 normal-derivative lane.

The next proof target is the regularized finite-prefix congruence

\[
pB_p+2p\,b_{2m-1}+2+\frac{5p}{3}
\equiv0\pmod{p^2}.
\]

Seek a finite summation/adjoint certificate that retains the pole row rather than deleting it. A successful certificate closes the upper \(B\)-chart. If it fails, the failure must identify an additional repair coordinate at the prefix-to-first-pole interface.
