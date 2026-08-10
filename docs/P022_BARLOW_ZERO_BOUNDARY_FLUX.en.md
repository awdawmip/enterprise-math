# P022 — Sparse Zero-Boundary Flux and the Nonzero-Marker Problem

Status: `ACTIVE RESEARCH NOTE / EXACT LOCALIZATION + SHARP NEGATIVE CONTROL`  
Owner: `program/p022-geometry-v2`  
Depends on: prime-halving valuation flux; Franel no-adjacent-zero recurrence  
Current target: characterize when the canonical half-defect marker valuation vanishes.

## 1. Full edge flux is unnecessarily large

For an odd valuation prime `p` and a positive integer `x<p`, the prime-halving formula gives

\[
\psi_p(x):=v_p\Psi(x)
=
\sum_q w_q(x)
\left(
v_p(F_{(q+1)/2})-v_p(F_{(q-1)/2})
\right).
\]

The Franel recurrence implies that two adjacent terms below `p` cannot both vanish modulo `p`. Hence a nonzero edge gradient can occur only when exactly one endpoint is a Franel zero.

Let

\[
Z_p=\{j:1\le j<p,\ p\mid F_j\},
\qquad z_j=v_p(F_j).
\]

For a nonprime integer `r`, define `w_r(x)=0`. Then every zero `j` has at most two boundary edges:

\[
2j-1\quad\text{and}\quad2j+1.
\]

## 2. P022-LI38 — zero-boundary localization

The full valuation collapses to

\[
\boxed{
\psi_p(x)
=
\sum_{j\in Z_p}
z_j\Bigl(
w_{2j-1}(x)-w_{2j+1}(x)
\Bigr).
}
\]

For `x<p`, only zero indices below the largest edge endpoint of the DAG can contribute. In the forced-midpoint setting, right-side mirror zeros above the midpoint cannot be reached by the two roots `m` and `p-2`, so the computation is naturally left-local.

Define the signed crossing multiplicity

\[
c_x(j)=w_{2j-1}(x)-w_{2j+1}(x).
\]

Then the midpoint defect has the sparse formula

\[
\boxed{
v_p(D_m)
=
z_m+
\sum_{\substack{j<m\\p\mid F_j}}
z_j\,\Delta c_p(j),
}
\]

where

\[
\Delta c_p(j)=c_m(j)-c_{p-2}(j).
\]

This is the exact marker coordinate.

## 3. Three qualitatively different exact behaviors

The formula separates three cases that had previously been conflated.

### A. Positive unit marker

For the early target-family samples, the transfer correction vanishes and the midpoint is simple, giving

\[
v_p(D_m)=+1.
\]

This motivated the original one-unit conjecture, but it is not invariant.

### B. Negative nonzero marker inside the target family

For

\[
p=369581\equiv5\pmod{24},
\]

we have

\[
F_8=2p,
\qquad
\Delta c_p(8)=-2,
\qquad
v_p(F_m)=1.
\]

Therefore

\[
\boxed{v_p(D_m)=-1.}
\]

The support collides with a zero and flux balance fails, yet the marker remains perfectly usable because it is nonzero.

### C. Complete marker cancellation outside the target residue subfamily

Take

\[
p=157,\qquad m=78.
\]

The midpoint is forced because `p=5 (mod 8)`, and `p-2=155` is composite. The canonical relation contains the earlier zero `j=16` with exponent one. Exact recurrence modulo `p^2` gives a simple midpoint zero, while the sparse correction is `-1`. Hence

\[
\boxed{v_{157}(D_{78})=0.}
\]

This is a genuine vanishing marker. It shows that nonvanishing is not automatic for all forced-midpoint composite boundaries.

Importantly,

\[
157\equiv1\pmod3,
\]

whereas the selected infinite target family `p=5,23 (mod 24)` always has

\[
p\equiv2\pmod3.
\]

Thus the mod-3 restriction may carry real arithmetic content; it should not be treated as a cosmetic way to make `p-2` composite.

## 4. Correct research target

The hierarchy of increasingly weaker claims is now:

1. `support never meets Z_p` — false;
2. `transfer correction is always zero` — false;
3. `marker is always +1` — false;
4. `marker is always nonzero in the selected p=5,23 (mod 24) family` — still open and exactly sufficient for this marker strategy.

Hence the active marker problem is

\[
\boxed{
\kappa_p
:=
v_p(F_m)+
\sum_{j<m,\ p\mid F_j}
v_p(F_j)\Delta c_p(j)
\stackrel{?}{\ne}0
}
\]

for every target-family prime.

The formula also makes the failure condition exact:

\[
\boxed{
\kappa_p=0
\iff
\sum_{j<m,\ p\mid F_j}
v_p(F_j)\Delta c_p(j)
=-v_p(F_m).
}
\]

Future work should attack this integer crossing identity directly rather than reinstating support-disjointness.

## 5. A cancellation example that validates the flux viewpoint

There are also target-family primes for which an earlier zero is reached by both prime-halving DAGs with equal crossing multiplicity. For example `p=26013917` divides `F_19`; at the zero boundary `j=19`, the relevant `q=37` edge occurs with equal multiplicity in the `m` and `p-2` DAGs, so

\[
\Delta c_p(19)=0.
\]

Thus even a genuine zero encountered by both transfers can cancel before it reaches the defect coordinate. Endpoint incidence alone cannot decide the marker.

## 6. Executable assets

- `src/enterprise_math/p022_barlow_zero_boundary_flux.py`
- `tests/test_p022_barlow_zero_boundary_flux.py`
- explicit negative-marker certificate: `p022_barlow_half_defect_counterexample.py`

The zero-boundary implementation is an exact rewriting of the edge-flux identity. The large numerical examples are regression certificates, not a proof of the open nonvanishing statement.
