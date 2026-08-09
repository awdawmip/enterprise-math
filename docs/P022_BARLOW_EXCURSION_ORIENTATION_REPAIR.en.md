# P022 — Excursion-Wise Orientation Repair for Absolute Barlow History

Status: `ACTIVE RESEARCH NOTE / EXACT FINITE FIBER SPECTRUM / PRIOR-ART SENSITIVE`  
Owner: `program/p022-geometry-v2`  
Depends on: Barlow signed prefix drift; P011 fiber/collision spectrum  
Cross-route relevance: P018/P023 boundary-triggered repair and history precision

## 1. Absolute history forgets less than one sign per layer

For a one-sided microscopic stacking word

\[
\sigma=(\sigma_1,\ldots,\sigma_N)\in\{-1,+1\}^N,
\]

define signed prefix drift

\[
\delta_k=\sum_{j=1}^{k}\sigma_j
\]

and absolute history

\[
\boxed{d_k=|\delta_k|.}
\]

The path

\[
0,d_1,d_2,\ldots,d_N
\]

is a nonnegative nearest-neighbor walk.

Passing from signed drift to absolute drift loses orientation.  A naive repair would store one sign bit for every layer.  This note proves that is far from minimal.

## 2. Excursions

Call a **nonzero excursion** a maximal interval beginning with a departure

\[
0\to1
\]

and continuing until the next return to zero, or until the final time if no return occurs.

Let

\[
\boxed{
e(d)=\#\{k:d_{k-1}=0,\ d_k=1\},
}
\]

with `d_0=0`.

This is exactly the number of excursion starts.

## 3. P022-ER01 — sign is rigid inside one excursion

Suppose an excursion has begun and the signed drift at its first positive state is either `+1` or `−1`.

While the absolute path remains positive, signed drift cannot change sign without crossing zero.  But crossing zero would terminate the excursion.

Therefore the orientation chosen at the departure from zero fixes the sign of the entire excursion.

Conversely, when an excursion returns to zero, the next departure can independently choose either orientation.

Hence the hidden sign degrees of freedom are indexed by **excursions**, not by layers.

## 4. P022-ER02 — exact microscopic fiber size

For a fixed legal absolute history `d`, assign independently one orientation

\[
\epsilon_j\in\{-1,+1\}
\]

to each of its `e(d)` excursions.

This uniquely reconstructs signed drift by

\[
\delta_k=\epsilon_j d_k
\]

inside excursion `j`, and therefore reconstructs the microscopic stacking increment

\[
\sigma_k=\delta_k-\delta_{k-1}\in\{-1,+1\}.
\]

Different orientation assignments produce different words.

Thus the observation fiber is exactly

\[
\boxed{
|\{\sigma:|\delta(\sigma)|=d\}|
=2^{e(d)}.
}
\]

So the minimal exact orientation repair is

\[
\boxed{
\text{one bit per excursion}.
}
\]

No bit is needed at interior layers of an excursion.

## 5. Event-driven precision

This yields a concrete finite example where hidden information is created only at a boundary event:

\[
\boxed{
\text{new orientation freedom appears exactly when the absolute state leaves zero.}
}
\]

A fixed-rate repair budget would over-store information.  The exact repair schedule is event-driven by visits to the zero boundary.

This is structurally related to P023's minimal boundary-bit repairs, but the present theorem is independently derived from Barlow excursion dynamics.  Any upstream abstraction should separate the general boundary-triggered principle from this specialization.

## 6. P022-ER03 — number of absolute histories with a fixed excursion count

Let

\[
A_{N,e}
=
\#\{d:\text{length }N\text{ absolute history with }e\text{ excursions}\}.
\]

These counts have closed forms.

### Odd length

Let

\[
N=2m+1.
\]

Then

\[
\boxed{
A_{2m+1,e}
=
\binom{2m+1-e}{m+1-e}.
}
\]

### Even length

Let

\[
N=2m>0.
\]

Then

\[
\boxed{
A_{2m,e}
=
2\binom{2m-e-1}{m-e}.
}
\]

For `N=0`, there is one empty history with zero excursions.

## 7. Proof of ER03 by Catalan decomposition

Let `C(z)` be the Catalan generating function,

\[
C(z)=1+zC(z)^2.
\]

A complete positive excursion of half-length at least one has generating function

\[
I(z)=zC(z).
\]

For odd total length, the last excursion cannot finish at zero.  After its forced first upward step, its remaining even-length nonnegative tail contributes

\[
\frac1{\sqrt{1-4z}}.
\]

Thus histories with `e` excursions contribute

\[
I(z)^{e-1}\frac1{\sqrt{1-4z}}.
\]

Using the standard coefficient identity

\[
\boxed{
[z^n]\frac{C(z)^k}{\sqrt{1-4z}}
=
\binom{2n+k}{n},
}
\]

gives the odd formula.

For even total length, the final excursion may either close or remain incomplete.  The union of these two possibilities simplifies to

\[
\frac{2z}{\sqrt{1-4z}}.
\]

Hence the coefficient is

\[
[z^m]
I(z)^{e-1}\frac{2z}{\sqrt{1-4z}},
\]

which gives the even formula by the same identity.

The Catalan and ballot/reflection ingredients are classical combinatorics; no novelty claim is made for those generating functions.

## 8. P022-ER04 — complete fiber profile of the absolute-history quotient

ER02 says every history with `e` excursions has fiber size

\[
2^e.
\]

ER03 counts how many such histories exist.  Therefore the complete fiber-size profile is supported only on powers of two:

\[
\boxed{
c_{2^e}=A_{N,e},}
\]

and

\[
c_s=0
\quad\text{for all other }s.
\]

Two exact consistency identities follow:

\[
\boxed{
\sum_e A_{N,e}
=
\binom{N}{\lfloor N/2\rfloor},
}
\]

the number of nonnegative prefixes, and

\[
\boxed{
\sum_e 2^eA_{N,e}=2^N,
}
\]

which reconstructs all microscopic stacking words.

The maximum number of excursions is

\[
\left\lceil\frac N2\right\rceil,
\]

so the largest orientation fiber is

\[
\boxed{
2^{\lceil N/2\rceil}.
}
\]

## 9. P022-ER05 — complete P011 collision spectrum

P011 defines

\[
J_k
=
\sum_y\binom{|O^{-1}(y)|}{k}.
\]

Substituting ER04 gives the closed finite expression

\[
\boxed{
J_k(N)
=
\sum_e
A_{N,e}
\binom{2^e}{k}.
}
\]

Therefore the collision polynomial of the absolute-history quotient is

\[
\boxed{
K_N(t)
=
\sum_e
A_{N,e}
\left((1+t)^{2^e}-1\right).
}
\]

This packages the full orientation ambiguity created by erasing excursion signs.

## 10. Precision consequence

The successive observation states now have a clean interpretation:

\[
\text{literal stacking word}
\to
\text{signed drift history}
\to
\text{absolute drift history}
\to
\text{coarser shell statistics}.
\]

At the signed-to-absolute step, the exact repair is not proportional to horizon length.  It is proportional to the number of zero-boundary excursions:

\[
\boxed{
\text{repair dimension}=e(d).
}
\]

So two histories of the same length can require very different repair sizes.

This is a concrete example of **state-dependent precision**: the amount of hidden information is determined by the realized path structure, not merely by a global resolution parameter.

## 11. Executable verification

Added:

- `src/enterprise_math/p022_barlow_excursion_repair.py`;
- `tests/test_p022_barlow_excursion_repair.py`.

The tests group every microscopic word through length ten by absolute history, verify the exact `2^e` fibers, reconstruct every word from excursion orientations, and compare the closed excursion-count and P011 collision formulas with direct finite enumeration.  Longer ranges verify the two global counting identities without enumerating all words.
