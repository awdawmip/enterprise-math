# P025 Supplement 87 — Local Odd-Prime Cover Transport and Support Resonance

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-cyclotomic-stage76`  
Depends on: P025 Supplements 84–86  
Hard block: `NONE`

## 1. Generic cover edges have one local quotient

Let

\[
r\ge3
\]

be an odd prime and let

\[
n=rm.
\]

For the difference sign, set

\[
A_m=p^m-q^m,
\qquad
Q^-_{m,r}
:=
\frac{p^{rm}-q^{rm}}{p^m-q^m}.
\]

For the same-sign sum route, `r` is automatically admissible because it is odd; set

\[
A_m=p^m+q^m,
\qquad
Q^+_{m,r}
:=
\frac{p^{rm}+q^{rm}}{p^m+q^m}.
\]

The Stage-84 cover multiplier is

\[
\Lambda_{m\to rm}
=
\frac{\Gamma\,m(Q)}r.
\]

The only missing local datum is the overlap factor `Gamma`.

## 2. P025-T185 — ancestor/quotient gcd is only `1` or `r`

Write

\[
X=p^m,
\qquad
Y=q^m.
\]

For the difference quotient,

\[
Q^-_{m,r}
=X^{r-1}+X^{r-2}Y+\cdots+Y^{r-1}.
\]

Modulo

\[
X-Y,
\]

we have `X=Y`, so

\[
Q^-_{m,r}
\equiv
rY^{r-1}\pmod{X-Y}.
\]

Because `Y` is coprime to `X-Y`,

\[
\boxed{
\gcd(A_m,Q^-_{m,r})
=\gcd(A_m,r).
}
\]

For the sum quotient,

\[
Q^+_{m,r}
=X^{r-1}-X^{r-2}Y+\cdots-XY^{r-2}+Y^{r-1}.
\]

Modulo

\[
X+Y,
\]

we have `X=-Y`, and every term reduces to the same unit multiple of `Y^{r-1}`. Hence again

\[
\boxed{
\gcd(A_m,Q^+_{m,r})
=\gcd(A_m,r).
}
\]

Since `r` is prime, the gcd is exactly `1` or `r`.

## 3. P025-D32 — cover support resonance

Call the cover **support-resonant** when

\[
\boxed{r\mid A_m.}
\]

Then the ancestor and the new quotient share exactly the cover prime `r`.

If the cover is not support-resonant, the two blocks have disjoint support.

Thus the radical-overlap correction is

\[
\boxed{
\Gamma
=
\begin{cases}
r,&r\mid A_m,\\
1,&r\nmid A_m.
\end{cases}}
\]

## 4. P025-T186 — the resonant prime enters the quotient only once

Assume

\[
r\mid A_m.
\]

The cover prime is distinct from the bases `p,q`; otherwise it could not divide `p^m\pm q^m`.

Ordinary LTE gives

\[
v_r(p^{rm}-q^{rm})
=v_r(p^m-q^m)+v_r(r)
\]

on the difference route, and the corresponding odd-exponent plus version gives the same statement on the sum route.

Since

\[
v_r(r)=1,
\]

we obtain

\[
\boxed{v_r(Q_{m,r})=1.}
\]

Therefore the overlap prime itself contributes no multiplicity residual inside the new quotient.

This separates the two roles cleanly:

- `r` may cancel normalization through support reuse;
- any quotient amplification beyond that must come from other repeated support.

## 5. P025-T187 — exact local odd-prime cover formula

Substituting the two possible overlap factors into Stage 84 gives

\[
\boxed{
\Lambda_{m\to rm}
=
\begin{cases}
\displaystyle \frac{m(Q_{m,r})}{r},
&r\nmid A_m,\\[3mm]
\displaystyle m(Q_{m,r}),
&r\mid A_m.
\end{cases}}
\]

This is the exact local transport law for every odd-prime same-sign cover.

## 6. Transport classification is now explicit

### Resonant locus

If

\[
r\mid A_m,
\]

then

\[
\Lambda=m(Q)
\]

is a positive integer. Therefore the edge is never attenuated:

- `m(Q)=1`: resonant transport;
- `m(Q)>1`: amplified transport.

### Nonresonant locus

If

\[
r\nmid A_m,
\]

then

\[
\Lambda=\frac{m(Q)}r.
\]

Therefore:

- `m(Q)<r`: attenuation;
- `m(Q)=r`: exact resonance;
- `m(Q)>r`: amplification.

So outside the support-resonance locus, the new quotient must pay an entire factor `r` merely to cancel the exponent-normalization cost.

## 7. P025-T188 — cover resonance is a prime-ratio congruence

Assume the cover prime `r` differs from `p,q`, as it automatically does on the resonant locus. Define

\[
x=pq^{-1}\pmod r.
\]

For difference,

\[
r\mid p^m-q^m
\iff
\boxed{x^m\equiv1\pmod r}.
\]

For sum,

\[
r\mid p^m+q^m
\iff
\boxed{x^m\equiv-1\pmod r}.
\]

Thus normalization cancellation is not hidden arithmetic. It is a finite root-of-unity condition on the prime ratio.

This is a second, much cheaper congruence precision layer than the repeated-prime-power signatures of Stages 77–79.

## 8. The Stage-84 trichotomy revisited

The `3->9` sum fixtures become transparent.

### Attenuated: `(q,p)=(5,59)`

The ancestor is not divisible by three, the quotient is squarefree, so

\[
\Lambda=\frac13.
\]

### Resonant: `(q,p)=(11,13)`

The ancestor is divisible by three, the quotient is squarefree, so

\[
\Lambda=1.
\]

### Amplified: `(q,p)=(7,29)`

The ancestor is divisible by three and the quotient has residual `19`, so

\[
\Lambda=19.
\]

A nonresonant edge may also amplify if the quotient residual exceeds `r`; this occurs, for example, on the `3->9` difference route for `(q,p)=(3,13)`.

## 9. P025-C30 — prime two is the unique universal resonance cover

Stage 86 proves that for odd bases

\[
2\mid p^m-q^m
\]

and

\[
2\mid p^m+q^m
\]

for every `m`. Hence the prime-two doubling edge always receives the overlap factor that cancels its normalization cost.

No odd cover prime has this universal property. For any odd prime `r`, choose one prime base equal to `r`; then `r` cannot divide the corresponding sum or difference ancestor because the other base is nonzero modulo `r`.

Thus:

\[
\boxed{
2\text{ is the unique cover prime with universal support resonance on odd-prime bases.}
}
\]

This explains Stage 86's universal dyadic non-attenuation.

## 10. P025-T189 — congruence-or-residual dichotomy

Suppose an odd-prime cover is non-attenuating:

\[
\Lambda_{m\to rm}\ge1.
\]

From P025-T187, either

\[
r\mid A_m,
\]

or, on the nonresonant branch,

\[
m(Q_{m,r})\ge r.
\]

Therefore

\[
\boxed{
\Lambda_{m\to rm}\ge1
\Longrightarrow
\big(r\mid A_m\big)
\ \lor\ 
\big(m(Q_{m,r})\ge r\big).
}
\]

More generally, if

\[
\Lambda\ge T,
\]

then:

- resonant branch: `m(Q)>=T`;
- nonresonant branch: `m(Q)>=Tr`.

So every strong odd-prime cover must pay through either finite congruence precision or a correspondingly larger new residual.

## 11. Precision interpretation

Every odd-prime cover contains two possible payment channels:

\[
\boxed{
\text{old support resonance}
\quad\text{or}\quad
\text{new quotient multiplicity}.
}
\]

The first is cheap to observe: one residue equation modulo `r`.

The second is expensive in value space but quantitative: without resonance, the quotient residual must compensate the full prime normalization cost.

This gives a theorem-native adaptive precision policy for exponent edges:

1. test the low-cost resonance congruence;
2. only if it fails, inspect quotient multiplicity deeply enough to decide whether it reaches the `r`-scaled threshold.

## 12. Prior-art / novelty discipline

The geometric-series congruence, gcd identity and LTE are classical mathematics.

P025 claims none of those ingredients individually.

The project-side candidate is their exact composition into the local projective cover multiplier, the support-resonance interpretation, and the congruence-or-residual routing dichotomy. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 13. Executable assets

Added:

- `src/enterprise_math/abc_odd_prime_cover_transport.py`;
- `tests/test_abc_odd_prime_cover_transport.py`.

The executable layer checks the gcd law, exact quotient valuation of the resonant cover prime, radical overlap, multiplier formula, ratio-congruence criterion, and all three transport classes.

## 14. Next frontier

No hard block exists. Continue with:

1. count the exact number of support-resonance ratio classes modulo `r`;
2. derive a finite height-`P` incidence bound for resonant prime-base pairs;
3. combine that with the nonresonant residual threshold `m(Q)>=Tr` into a cover-level sparse-state theorem;
4. determine whether cover-resonance signatures can be composed across Hasse paths without storing full prime bases;
5. use the result to build the orbit-normal form promised in Stage 86.
