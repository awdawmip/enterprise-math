# P022 Composite Franel Equal-Depth Escape — Research Return

Status: `EXACT_FIRST_JET_REDUCTION_FROZEN / UNIVERSAL_ESCAPE_NOT_CLOSED`

Researcher-ID: `EM-P022ESC-A4C91E`
Task: `RS-P022-COMPOSITE-FRANEL-EQUAL-DEPTH-ESCAPE`
Publication: `TP2-E4537008BB8B0CCFF88F`
Claim: `chatgpt-p022esc-20260827-2237-a4c91e`
Source owner: `program/p022-geometry-v2@603ef1c72245612359f8b59cab7a492de21a9166`

## 1. Result

The retained forced-midpoint scale identity reduces continued escape at a target prime `p=6k-1` to

\[
v_p(F_{2k-1})=v_p(F_m)>0,\qquad v_p(F_{2k})=0,\qquad m=(p-1)/2=3k-1.
\]

The new step is an exact mod-`p^2` expansion of the forced midpoint. Define, in the p-local ring,

\[
a_j=(-1)^j\binom{2j}{j}^3 64^{-j},\qquad
S_p=\sum_{j=0}^{m}a_j,
\]

and modulo `p`

\[
T_p=\sum_{j=0}^{m}a_j\left(H_{2j}-\frac12H_j\right),\qquad
U_p=\sum_{j=0}^{m}a_jH_j.
\]

For every `0<=j<=m`, the identity

\[
\binom{m}{j}=(-1)^j\frac{\binom{2j}{j}}{4^j}
\prod_{r=0}^{j-1}\left(1-\frac{p}{2r+1}\right)
\]

is exact. Cubing and reducing modulo `p^2` gives

\[
\binom{m}{j}^3\equiv a_j\left(1-3p\left(H_{2j}-\frac12H_j\right)\right)\pmod{p^2}.
\]

Summing yields the exact first correction

\[
\boxed{F_m\equiv S_p-3pT_p\pmod{p^2}.}
\]

In the forced midpoint sector `p=5,7 (mod 8)`, `p|F_m`, hence also `S_p=0 (mod p)`. Put

\[
C_p:=S_p/p\pmod p.
\]

Then

\[
\boxed{F_m/p\equiv C_p-3T_p\pmod p.}
\]

Using the frozen P022 harmonic pairing `U_p=2T_p (mod p)` gives the compressed paired form

\[
\boxed{2F_m/p\equiv 2C_p-3U_p\pmod p.}
\]

Therefore the midpoint depth raises from one to at least two exactly when

\[
\boxed{2C_p-3U_p\equiv0\pmod p.}
\]

This is the requested next exact p-adic relation implied by the forced-midpoint structure and harmonic pairing.

## 2. Reconnection to the third-minus / scalar-Hasse side

The frozen Whipple bridge gives, for `n=2k-1=(p-2)/3`,

\[
F_n\equiv 2^nP_p(1)\pmod p.
\]

Thus the surviving escape sector necessarily lies on the scalar-Hasse locus

\[
P_p(1)=0.
\]

On that locus define the first quotient jet

\[
W_p:=2^{-n}F_n/p\pmod p.
\]

Because `2^n` is a p-unit,

\[
v_p(F_n)=1\iff W_p\ne0,
\qquad
v_p(F_n)\ge2\iff W_p=0.
\]

Together with the midpoint formula, the equal-depth mechanism has an exact first-jet trichotomy:

1. `W_p != 0` and `2C_p-3U_p != 0`: both depths are exactly one, so the equal-depth signature survives at first order;
2. exactly one of `W_p`, `2C_p-3U_p` vanishes: the depths are unequal, so this escape channel is killed immediately;
3. both vanish: both depths are at least two, and a second-jet comparison is genuinely required.

Hence the existing inputs do **not** justify a theorem that the equal-depth signature is impossible. The harmonic identity does not force opposite first-jet status; it merely collapses the midpoint first jet to the single scalar `2C_p-3U_p`.

## 3. Minimal exact exceptional condition

The smallest first-order exception is therefore the named locus

`P022_SIMPLE_SIMPLE_HASSE_JET_EXCEPTION`:

\[
\boxed{
P_p(1)=0,\quad
W_p\ne0,\quad
2C_p-3U_p\ne0.
}
\]

Any admissible prime satisfying this condition produces the surviving equal-depth signature with common depth exactly one, subject to the already-frozen earlier-escape hypotheses.

The only deeper unresolved branch is

`P022_DOUBLE_DEEP_HASSE_JET_EXCEPTION`:

\[
\boxed{
P_p(1)=0,\quad
W_p=0,\quad
2C_p-3U_p=0,
}
\]

where equality of valuations is a second-order question. This is strictly smaller than the former vague `composite Franel equal-depth` residue.

## 4. Finite regression

Task-local checker: `scripts/check_p022_composite_franel_equal_depth_escape.py`.

It verifies the exact midpoint mod-`p^2` expansion, the quotient formula, and the paired form for every target-sector prime below `5,000`. Exact local execution covered 168 such primes with zero first-jet failures and found zero scalar-Hasse zero candidates in that finite range. This is regression/falsification evidence only and is not used as proof of absence.

## 5. Hard-target disposition

Hard target:

`P022_COMPOSITE_FRANEL_EQUAL_DEPTH_ESCAPE_CLOSED_OR_MINIMAL_EXCEPTION_FROZEN`

Disposition:

`PASS / MINIMAL_EXACT_EXCEPTION_FROZEN`.

Universal escape closure is **not** proved. No admissible equality witness is asserted. The taskbook stopping rule is met because the next p-adic correction has been derived exactly and the remaining mechanism has been reduced to two explicit first-jet loci, with only the double-deep branch requiring a higher jet.

Strongest reusable theorem:

\[
\boxed{
2F_{(p-1)/2}/p\equiv 2\left(\frac1p\sum_{j=0}^{(p-1)/2}(-1)^j\binom{2j}{j}^3 64^{-j}\right)-3U_p\pmod p
}
\]

in the forced-midpoint sector, where the parenthesized p-quotient is taken in the p-local ring and is defined because the sum vanishes modulo `p`.

## 6. Next control-plane recommendation

Driver review this exact reduction. If accepted, do **not** reopen the whole composite Franel route. Publish at most one narrow successor targeting the first-order compatibility question between the scalar-Hasse quotient jet `W_p` and the midpoint jet `2C_p-3U_p`; only if the double-deep locus is shown nonempty should a second-jet successor be opened.

Hard block: `NONE` at this task scope.
