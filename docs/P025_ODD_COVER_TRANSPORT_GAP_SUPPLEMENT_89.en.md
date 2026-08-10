# P025 Supplement 89 — Odd-Cover Transport Spectral Gap and Two-Bit Qualitative State

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-cyclotomic-stage76`  
Depends on: P025 Supplements 87–88  
Hard block: `NONE`

## 1. Stage 87 still treated the quotient residual as arbitrary

Stage 87 gives the exact local formula

\[
\Lambda_{m\to rm}
=
\begin{cases}
m(Q)/r,&\text{nonresonant},\\
m(Q),&\text{support-resonant},
\end{cases}
\]

for an odd cover prime `r`.

Taken alone, this formula formally allows many intermediate multiplier values. But the quotient `Q` is not an arbitrary integer: it is a prime-index cyclotomic value.

That extra structure creates a large spectral gap.

## 2. The new quotient is cyclotomic

Write

\[
X=p^m,
\qquad
Y=q^m.
\]

For a difference cover,

\[
\boxed{Q=\Phi_r(X,Y).}
\]

For a same-sign sum cover,

\[
\boxed{Q=\Phi_{2r}(X,Y).}
\]

The bases `X,Y` are coprime.

## 3. P025-T196 — repeated quotient primes are `1 mod 2r`

Let `s` be a repeated prime divisor of `Q`.

The exceptional cover prime `r` can occur only on the support-resonant locus, and Stage 87 proves

\[
v_r(Q)=1.
\]

So any repeated prime satisfies

\[
s\ne r.
\]

For the difference quotient, the ratio

\[
XY^{-1}\pmod s
\]

has exact order `r`. For the sum quotient it has exact order `2r`.

In the difference case, `r|s-1`; since both `r` and `s` are odd, `2|s-1` also, hence

\[
2r\mid s-1.
\]

The sum case gives the same divisibility directly.

Therefore in both signs

\[
\boxed{s\equiv1\pmod{2r}.}
\]

In particular

\[
\boxed{s\ge2r+1.}
\]

## 4. P025-T197 — quotient residual gap

If `Q` is squarefree, then

\[
\boxed{m(Q)=1.}
\]

If `Q` is nonsquarefree, choose any repeated prime `s`. Since the exponent of `s` in `Q` is at least two,

\[
s\mid m(Q).
\]

By P025-T196,

\[
\boxed{m(Q)\ge2r+1.}
\]

Hence there are no quotient residual values in the interval

\[
\boxed{1<m(Q)<2r+1.}
\]

for an odd-prime cover.

This removes most of the formal possibilities left open by Stage 87.

## 5. P025-T198 — transport spectral gap

Combine P025-T197 with the Stage-87 multiplier formula.

### Nonresonant branch

If `Q` is squarefree,

\[
\boxed{\Lambda=1/r.}
\]

If `Q` is nonsquarefree,

\[
\boxed{
\Lambda
=\frac{m(Q)}r
\ge
\frac{2r+1}{r}
>2.
}
\]

Thus the nonresonant branch jumps directly from strong attenuation to more-than-twofold amplification.

### Support-resonant branch

If `Q` is squarefree,

\[
\boxed{\Lambda=1.}
\]

If `Q` is nonsquarefree,

\[
\boxed{
\Lambda=m(Q)\ge2r+1.
}
\]

Thus the resonant branch jumps directly from exact preservation to amplification by at least `2r+1`.

## 6. P025-C31 — formal nonresonant exact resonance is impossible

Stage 87's bare formula allowed the algebraic possibility

\[
m(Q)=r
\]

on a nonresonant cover, which would give

\[
\Lambda=1.
\]

P025-T197 excludes this completely:

\[
\boxed{
\text{a nonresonant odd-prime cover can never be exactly resonant.}
}
\]

Likewise there is no weak amplification interval

\[
1<\Lambda\le2
\]

on the nonresonant branch.

This is a genuine correction/refinement of the formal Stage-87 trichotomy.

## 7. P025-T199 — qualitative transport needs only two natural bits

Define

\[
R:=\mathbf1_{\{r\mid A_m\}},
\]

the ancestor support-resonance bit, and

\[
S:=\mathbf1_{\{Q\text{ squarefree}\}},
\]

the quotient-squarefree bit.

Then the exact transport class is:

\[
\boxed{
\begin{array}{c|c|c}
R&S&\text{transport class}\\ \hline
0&1&\text{attenuated}\\
1&1&\text{resonant}\\
0&0&\text{amplified}\\
1&0&\text{amplified}
\end{array}}
\]

Equivalently,

\[
\boxed{
S=0\Longrightarrow\text{amplified},
}
\]

while for `S=1`, `R` distinguishes attenuation from resonance.

Thus the exact qualitative future query does **not** require the numerical value `m(Q)`.

## 8. Both bits are genuinely needed among these natural observables

The resonance bit alone is insufficient:

- `(q,p)=(11,13)`, `3->9` sum: `R=1`, squarefree quotient, resonant;
- `(q,p)=(7,29)`, `3->9` sum: `R=1`, repeated quotient, amplified.

The squarefree bit alone is also insufficient:

- `(q,p)=(5,59)`, `3->9` sum: squarefree quotient, nonresonant, attenuated;
- `(q,p)=(11,13)`: squarefree quotient, resonant.

So neither one-bit natural projection factors the three-state future query.

The pair `(R,S)` does.

## 9. Exact fifth-cover calibrations

The same gap is visible beyond `r=3`.

### Resonant fifth cover

For

\[
(q,p,m,r)=(19,29,2,5)
\]

on the difference branch, the quotient contains

\[
11^3,
\qquad
11\equiv1\pmod{10},
\]

and

\[
m(Q)=121.
\]

The edge is resonant in support and amplified by

\[
\Lambda=121.
\]

### Nonresonant fifth cover

For

\[
(q,p,m,r)=(7,47,2,5)
\]

on the sum branch, the quotient contains

\[
41^2,
\qquad
41\equiv1\pmod{10},
\]

so

\[
m(Q)=41
\]

and

\[
\boxed{
\Lambda=\frac{41}{5}>8.
}
\]

Again there is no weak-amplification regime.

## 10. Precision consequence

For the future query

\[
\text{"attenuated, resonant, or amplified?"}
\]

full quotient factorization is unnecessary.

The natural sufficient state is

\[
\boxed{(R,S).}
\]

This is much cheaper semantically than storing the full quotient residual, its repeated modulus, or its cyclotomic factorization.

However this is **task-relative**. If the future query asks for the exact multiplier `Lambda`, then `m(Q)` must be recovered whenever `Q` is nonsquarefree.

So the same arithmetic edge naturally supports multiple precision layers.

## 11. Prior-art / novelty discipline

Cyclotomic order arguments are classical. The congruence restriction on repeated prime divisors is a standard consequence of multiplicative order.

P025 claims none of those ingredients individually.

The project-side candidate is the transport spectral-gap consequence, the exact two-natural-bit qualitative compiler, and its use as a task-relative precision state. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 12. Executable assets

Added:

- `src/enterprise_math/abc_odd_cover_transport_gap.py`;
- `tests/test_abc_odd_cover_transport_gap.py`.

The executable layer verifies repeated support modulo `2r`, the residual floor, the four logical bit combinations realized by exact fixtures, and the absence of weak amplification in tested covers.

## 13. Next frontier

No hard block exists. Continue with:

1. distinguish the minimal state for the binary future query `Lambda>=1` from the ternary transport-class query;
2. derive exact short-circuit observation trees for those queries;
3. compare information-minimal and computational-cost-aware observation orders;
4. build the dyadic/odd-cover orbit normal form using only the future-relevant edge labels;
5. return this result to P023/A2 as a concrete theorem-backed pressure test of future-relative precision.
