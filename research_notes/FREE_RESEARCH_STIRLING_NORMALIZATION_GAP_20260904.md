# Free Research — Core/Full Normalization Gap in the `1/9` Chamber Match

Status: `FREE_RESEARCH_CORRECTION / NORMALIZATION_MISMATCH_EXPOSED / DIRECT_PROBABILITY_INTERPRETATION_BLOCKED / RESCALED_INTERTWINER_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_S3_STIRLING_CHAMBER_INTERTWINER_20260904.md`

## 1. Correction

Two exact coefficients equal `1/9`:

1. the quadratic survival factor of the weighted `S_3` lift–transpose–project mixer;
2. the deepest degree-three Stirling chamber as a fraction of the **full** logarithmic simplex packet.

These coefficients use different reference measures unless an additional normalization bridge is supplied.

Therefore the numerical equality must not be read as saying that the deepest chamber is the direct transition probability from the factorial core.

---

## 2. Three degree-three masses

Let

\[
u_a=\frac{\Lambda(a)}a,
\qquad
U_Y=\sum_{a\le Y}u_a.
\]

Define the factorial core mass

\[
C_Y
:=\sum_{a,b,c\le Y}u_au_bu_c
=U_Y^3.
\tag{2.1}
\]

Define the full degree-three product-simplex mass

\[
F_Y
:=\sum_{abc\le Y^3}u_au_bu_c.
\tag{2.2}
\]

Define the deepest mass

\[
D_Y
:=\sum_{\substack{abc\le Y^3\\
\text{exactly two of }a,b,c>Y}}
 u_au_bu_c.
\tag{2.3}
\]

From the first-mass law

\[
A(X)=\sum_{a\le X}u_a=\log X+O(1)
\]

and repeated Abel summation over the logarithmic chambers,

\[
\boxed{
F_Y=\frac92U_Y^3+O(U_Y^2),
}
\tag{2.4}
\]

while the Stirling chamber law gives

\[
\boxed{
D_Y=\frac12U_Y^3+O(U_Y^2).
}
\tag{2.5}
\]

The core identity (2.1) is exact.

---

## SNG-T01 — The three relevant ratios

Equations (2.1)–(2.5) give

\[
\boxed{
\frac{C_Y}{F_Y}
=\frac29+O(1/U_Y),
}
\tag{3.1}
\]

\[
\boxed{
\frac{D_Y}{F_Y}
=\frac19+O(1/U_Y),
}
\tag{3.2}
\]

and

\[
\boxed{
\frac{D_Y}{C_Y}
=\frac12+O(1/U_Y).
}
\tag{3.3}
\]

At the exact chamber-count level these are

\[
\frac6{27}=\frac29,
\qquad
\frac3{27}=\frac19,
\qquad
\frac36=\frac12.
\]

The Lean chamber packet now records all three ratios explicitly.

---

## SNG-N01 — Direct transition-probability reading is invalid

The weighted `S_3` mixer acts on the core product ensemble and satisfies

\[
\mathcal E_{\rm core}(\mathcal K_3x)
=\frac19\mathcal E_{\rm core}(x).
\tag{4.1}
\]

The deepest chamber satisfies

\[
D_Y/F_Y\to1/9,
\]

but

\[
D_Y/C_Y\to1/2.
\]

Therefore

\[
\boxed{
\text{mixer survival }1/9
\ne
\text{deep/core mass }1/2.
}
\tag{4.2}
\]

No measure-preserving identification from core histories to deepest histories follows from the coefficient equality alone.

This blocks the strongest reading of the earlier coefficient alignment.

---

## 5. What remains valid

The following statements remain exact:

1. the deepest chamber and constant maps carry the same `S_3` permutation representation;
2. the deepest/full fraction is `1/9`;
3. the global mixer standard eigenvalue is `1/3`, hence its energy factor is `1/9`;
4. the colored deepest kernel is balanced at each lower endpoint;
5. the scalar endpoint erases its standard component.

What is missing is a map that aligns their **normalizations and amplitudes**.

---

## 6. Required normalization bridge

There are two legitimate routes.

### Full-packet normalization

Normalize all degree-three histories by `F_Y`.  Then the deepest colored kernel is a subprobability kernel of mass

\[
1/9+O(1/U_Y).
\]

One must embed the incoming standard field into this full packet and compute the core contribution under the same normalization.

### Core normalization

Normalize the mixer input by `C_Y`.  Then the deepest chamber has mass

\[
1/2+O(1/U_Y).
\]

To realize the mixer energy factor `1/9`, the deep transfer amplitude must carry an additional squared normalization factor asymptotic to

\[
\frac{1/9}{1/2}=\frac29.
\tag{6.1}
\]

Equivalently, a core-normalized value intertwiner requires amplitude scale

\[
\sqrt{2/9}.
\]

The origin of this amplitude factor is currently open.

---

## 7. Consequence for the cascade

The abstract recurrence

\[
E_{k+1}\le\frac19E_k+\varepsilon_k
\]

remains correct **conditional on** a normalized colored transfer of squared norm at most `1/9`.

The Stirling chamber count alone does not supply that norm relative to the core input.  A valid arithmetic cascade must first prove one of the normalization bridges in Section 6.

This is now the leading structural gap.

---

## 8. Updated next theorem

Construct a common Hilbert-space normalization for the factorial core and full degree-three simplex packet, and prove the exact norm of the core-to-deep colored transfer.

The desired outcome is either:

\[
\|T_Y^{\rm deep}\|_{\rm std}^2
=\frac19+O(1/U_Y),
\]

or a no-go showing that no canonical transfer with that norm exists under the current readout.

Only after this step may the deepest chamber be inserted into the one-ninth cube-root recurrence as an actual arithmetic transition.