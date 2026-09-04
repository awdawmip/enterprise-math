# Gregory–Machin continuation: rank-two valuation-plane seed-bound no-go

Status: `FREE_RESEARCH / EXACT NEGATIVE BOUNDARY + C8 ENDPOINT FAMILY / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-B2817C / FREE_AXIOM_DISCOVERY`
Issue: `#1160`
Checker: `research_notes/experiments/gregory_machin_rank2_seed_bound_nogo_20260904.py`
Depends on: Gaussian valuation decomposition, rational support-two direction-generator theorem, complement endpoint law.

## 1. Question

For support two, every unequal-multiplier endpoint pair under denominator height `H` comes from a primitive free direction of multiplicative norm below `sqrt(2)H`.  This gives a genuine dimension reduction from a quadratic atom box to an order-`H` Gaussian seed box.

Can support three admit the same kind of theorem: enumerate all relevant rank-two planes from two primitive basis generators whose multiplicative norms are `O(H)`?

The answer is **no**, even for exact `C8` diagonal endpoint circuits.

---

## 2. A saturated rank-two family

Fix three distinct split primes

\[
p,q,r\equiv1\pmod4.
\]

For every integer `K>=1` define free valuation columns

\[
\boxed{
v_1=(K,1,0),\qquad
v_2=(K,0,1),\qquad
v_3=(0,1,-1)=v_1-v_2.
}
\]

The plane lattice is

\[
L_K=\mathbf Z v_1+\mathbf Z v_2
=\{(K(a+b),a,b):a,b\in\mathbf Z\}.
\]

The `2x2` minors of the `3x2` basis matrix are

\[
\boxed{(-K,K,1)}.
\]

Their gcd is one.  Therefore `L_K` is saturated in `Z^3`; this is not an artifact of choosing a nonprimitive sublattice.

---

## 3. Every plane basis has one quadratically expensive free generator

The subgroup of `L_K` whose first coordinate is zero is

\[
\{(0,a,-a):a\in\mathbf Z\},
\]

which has rank one.

Hence any two independent lattice vectors generating `L_K` cannot both have first coordinate zero.  At least one basis vector `w` satisfies

\[
|w_p|\ge K.
\]

For the multiplicative Gaussian free norm

\[
M(w)=p^{|w_p|}q^{|w_q|}r^{|w_r|},
\]

this forces

\[
\boxed{M(w)\ge p^K.}
\]

So every lattice basis contains a generator of free norm at least `p^K`.

---

## 4. Yet the circuit is realized by rational atoms of denominator only O(p^(K/2))

Choose oriented Gaussian primes `pi_p,pi_q,pi_r` and form

\[
\gamma_1=\pi_p^K\pi_q,
\qquad
\gamma_2=\pi_p^K\pi_r,
\qquad
\gamma_3=\pi_q\bar\pi_r.
\]

Their exact free valuation columns are `v_1,v_2,v_3` and their raw Gaussian norms are

\[
N(\gamma_1)=p^Kq,
\qquad
N(\gamma_2)=p^Kr,
\qquad
N(\gamma_3)=qr.
\]

Fold each Gaussian class into a strict first-octant primitive rational atom.  Either folded branch has denominator at most the complement denominator, and for a pair `(b,a)` of norm `N`,

\[
(b+a)^2<2(a^2+b^2)=2N.
\]

Therefore every required branch has denominator bounded by

\[
\boxed{
H_K
<\sqrt{2\max(p^Kq,p^Kr,qr)}+1.
}
\]

For fixed `p,q,r`,

\[
H_K=\Theta(p^{K/2}).
\]

Combining with the basis lower bound gives

\[
\boxed{
\min_{\text{bases of }L_K}\max(M(w_1),M(w_2))
\ge p^K
=\Theta(H_K^2).
}
\]

Thus no universal exponent strictly below two can bound both rank-two basis-generator norms in terms of the realizing atom denominator height.

In particular, the rank-one `O(H)` seed theorem has no rank-two analogue of the same form.

---

## 5. The obstruction survives the C8 diagonal endpoint requirement

It remains to show that this family is relevant to the actual #1160 endpoint problem rather than only to free valuation geometry.

The primitive relation is

\[
v_1-v_2-v_3=0,
\]

so its coefficient magnitudes are all one.

After first-octant folding, each column may acquire an overall free sign and an even `C8` torsion shift.  The corresponding primitive free relation still has coefficients `c_j in {+1,-1}`.

If its torsion pairing

\[
E=\sum_jc_j\varepsilon_j\pmod8
\]

is already odd, the general `C8` target theorem scales it to the diagonal class.

If `E` is even, replace any one atom by its complement.  Complementation changes

\[
(\varepsilon,v)\mapsto(1-\varepsilon,-v).
\]

To preserve the same free relation, flip that coefficient `c -> -c`.  Its torsion contribution changes from

\[
c\varepsilon
\]

to

\[
-c(1-\varepsilon)=c\varepsilon-c.
\]

Since `c=+/-1` is odd, the total torsion parity flips.  Therefore the complemented branch has odd target pairing.

Hence for every `K` there exists a strict rational three-atom word in this plane satisfying

\[
\boxed{V_1^{c_1}V_2^{c_2}V_3^{c_3}=\tau}
\]

for suitable odd-scaled coefficients.

The checker verifies this explicitly for `p,q,r=(5,13,17)` and `1<=K<=12`; exactly four of the eight complement choices hit an odd `C8` target at every tested `K`.

---

## 6. Exact negative theorem

For every `epsilon>0`, there is **no** constant `C_epsilon` such that every generalized rational support-three diagonal endpoint circuit with denominator height at most `H` can be represented by a saturated valuation-plane basis satisfying

\[
M(w_1),M(w_2)\le C_\varepsilon H^{2-\varepsilon}.
\]

Indeed the family above has basis maximum at least `p^K`, while its realizing height is `Theta(p^{K/2})`; therefore

\[
\frac{p^K}{H_K^{2-\varepsilon}}
=\Theta(p^{K\varepsilon/2})\to\infty.
\]

Freeze:

\[
\boxed{
\texttt{RANK1\_LINE\_SEED\_BOUND}\not\Rightarrow
\texttt{RANK2\_PLANE\_SEED\_BOUND\_WITH\_EXPONENT<2}.
}
\]

---

## 7. Algorithmic consequence

A complete generalized support-three search cannot rely only on two small Gaussian plane-basis generators.  One must retain at least one additional resource coordinate capable of carrying quadratic plane complexity, for example:

- bounded prime palette;
- bounded Pluecker/exterior height;
- bounded weighted free norm of observed atom columns;
- or another explicitly declared plane-resource budget.

This explains why the exact `p,q<=5000` prime-plane audit is a legitimate bounded subfamily but cannot simply be promoted to a complete all-plane theorem by increasing a linear seed cap.

The next useful question is therefore **which exterior/Pluecker resource is both complete and computationally economical for low-completion-cost circuits**, not whether the rank-one seed theorem can be copied one dimension higher.
