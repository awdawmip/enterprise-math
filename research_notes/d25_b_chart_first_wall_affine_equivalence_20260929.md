# D25 portable research: first-wall affine equivalence and regular-only endpoint reformulation

Status: \`AUTHOR_PORTABLE_PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT\`

Contributor lineage: \`EM-DIRECT-C4D02C\`.

This is a portable mathematical unit. It claims no native session, CLAIM, run, canonical checkpoint, Result, review, or theorem admission.

## Source boundary

- Global authority snapshot for the present recovery line was refreshed separately before this write.
- Enterprise Math portable branch head immediately before this write: \`d2376f53b6fb7207ff793aeb9a8ff8512fd1d9ae\`.
- Canonical D25 local-progress blob remains \`51dd15a8142f3dda0506a306f9c0693a036f5891\`.
- Durable predecessor: \`research_notes/d25_b_chart_first_pole_finite_part_20260929.md\`, blob \`c9d586d8554e503c322937b5a3964ccdd2c720b0\`.
- This unit does not reopen the canonical LOW/B11 normal-Dixon derivative or the Gauss-Manin lane.

## 1. Setup

Let
\[
p=6m+1,\qquad N=2m-2,\qquad J=N+1=2m-1,
\]
and
\[
B_p=\sum_{j=0}^{N}b_j.
\]

The durable first-pole note proved
\[
p\,b_J\equiv -1+p\beta_p\pmod{p^2},
\]
and reduced the still-open upper-chart target to
\[
B_p\stackrel?{\equiv}-2\beta_p-\frac53\pmod p.
\tag{1}
\]

Define the first digit of the last regular row by
\[
b_N\equiv \frac{20}{9}+p\eta_p\pmod{p^2}.
\tag{2}
\]

## 2. Exact regular-to-pole wall map

At \(j=N\), the original exact recurrence gives
\[
\boxed{
p\frac{b_J}{b_N}
=
D(p):=
\frac{(p-4)(p-3)(2p-3)(2p+1)}
{4(p-2)(p+2)(2p-5)}.
}
\tag{3}
\]

Expanding the regular factor at \(p=0\),
\[
D(p)=
-\frac9{20}
-\frac{207}{400}p
+\frac{593}{1000}p^2+O(p^3).
\tag{4}
\]

Substituting (2) into \(p b_J=D(p)b_N\) gives
\[
p b_J
\equiv
-1+
p\left(
-\frac9{20}\eta_p-\frac{23}{20}
\right)
\pmod{p^2}.
\]
Hence
\[
\boxed{
\beta_p\equiv-\frac9{20}\eta_p-\frac{23}{20}\pmod p,
}
\tag{5}
\]
or equivalently
\[
\boxed{
\eta_p\equiv-\frac{20}{9}\beta_p-\frac{23}{9}\pmod p.
}
\tag{6}
\]

For the target primes \(p\ge 13\), the coefficient \(-9/20\) is a unit, so this is a reversible affine change of repair coordinate.

## 3. One-step post-pole chart

At \(j=J\),
\[
\frac{b_{J+1}}{b_J}=p\,C(p),
\]
with
\[
C(p)=
\frac{(p-1)(2p+3)(2p+7)}
{4(p+1)(p+3)(p+5)(2p+1)}
=
-\frac7{20}+\frac{94}{75}p+O(p^2).
\tag{7}
\]

Write
\[
b_{J+1}\equiv \frac7{20}+p\gamma_p\pmod{p^2}.
\]
Then
\[
\boxed{
\gamma_p\equiv-\frac{94}{75}-\frac7{20}\beta_p\pmod p.
}
\tag{8}
\]
Using (5),
\[
\boxed{
\gamma_p\equiv\frac{63}{400}\eta_p-\frac{1021}{1200}\pmod p.
}
\tag{9}
\]

Thus
\[
\eta_p\longleftrightarrow\beta_p\longleftrightarrow\gamma_p
\]
are three charts for the same one-dimensional repair datum. The simple pole changes valuation and provenance but does not add an independent degree of freedom.

## 4. Regular-only form of the open bridge

Substituting (5) into (1) gives the exactly equivalent regular-only target
\[
\boxed{
B_p\stackrel?{\equiv}\frac{27\eta_p+19}{30}\pmod p.
}
\tag{10}
\]

Since
\[
\eta_p=\frac{b_{2m-2}-20/9}{p}\pmod p,
\]
the undivided form is
\[
\boxed{
30pB_p-27b_{2m-2}+60-19p
\stackrel?{\equiv}0\pmod{p^2}.
}
\tag{11}
\]

Equivalently, using the post-pole digit,
\[
\boxed{
105pB_p-600b_{2m}+210-577p
\stackrel?{\equiv}0\pmod{p^2}.
}
\tag{12}
\]

Equations (10)-(12) are reformulations only; the upper \(B\)-chart congruence remains open.

## 5. BRC interpretation

Population: regular prefix \(0\le j\le 2m-2\), the first excluded pole \(j=2m-1\), and one healed row \(j=2m\).

Retained provenance: location of the valuation wall and the first lifted digit.

Safe compression proved here: the three local coordinates \(\eta_p,\beta_p,\gamma_p\) are reversibly equivalent on the target prime range.

Consequence: a proof certificate may work entirely on the regular chart using (11); it need not literally cross the Laurent pole, provided the affine wall map is retained.

Resolution:
\`COMPOSE_APPLIED / FIRST_WALL_AFFINE_EQUIVALENCE / LOCAL_REPAIR_DIMENSION_ONE / REGULAR_ONLY_ENDPOINT_REFORMULATION\`.

## 6. Status and next unit

The wall maps (3)-(9) are exact finite-algebra consequences of the original recurrence and its \(p\)-adic expansion. The bridge (10)-(12) is still conjectural and inherits the previous finite-regression evidence only.

Next: attack (11) on the regular chart. Do not retry a scalar one-state Gosper primitive; the durable predecessor already excludes that class after imposing \(p=6m+1\).
