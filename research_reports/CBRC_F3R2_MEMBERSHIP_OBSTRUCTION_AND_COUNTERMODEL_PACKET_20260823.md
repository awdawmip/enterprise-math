# CBRC F3R2 — Membership Obstruction and Countermodel Packet

Researcher-ID: `EM-CBRC-F3R2-6C8E41`

Task: `RS-CBRC-F3R2-SURVIVOR-MEMBERSHIP-PREDICATE-COMPLETION`

Primary theorem:

`SURVIVOR(A,B,D) <=> gcd(|a|,|d|)>1 and gcd(|b|,|c|)>1`

inside the ambient automorphism class.

## 1. Why torsion cannot rescue a bad free block

For any full admissible scalar `q`, define

`f(n)=min_{t in F3}q(n,t)`.

For fixed free input residues, the torsion map is

`t -> B r + D t`.

`D` is invertible, hence this is a permutation of the nine torsion pairs.

Taking minima of the pointwise conservation identity gives exact free conservation for `f`.

Because `q(0,0)=0` and `q>=0`, `f(0)=0`.

Because `R` cycles all torsion labels over free coordinate one and `q(e)=1`, `f(1)=1`.

The actual balanced elementary outputs each have scalar `1/2`, so `f(a),f(c)<=1/2`; free conservation at `(1,0)` forces their sum to one, hence both equal `1/2`.

Therefore every full survivor produces a torsion-blind free survivor.  This is the exact reason no `(B,D)` choice can repair a bad `A`.

## 2. Four exact free annihilators

For the torsion-min free scalar,

`f(ax+by)+f(cx+dy)=f(x)+f(y)`.

Mixed input differences and the same calculation for the inverse give

`Delta_a Delta_b f=0`,
`Delta_c Delta_d f=0`,
`Delta_d Delta_b f=0`,
`Delta_c Delta_a f=0`.

The intermediate mixed-difference constants vanish because a nonzero constant would force a quadratic quasipolynomial term, while axis conservation gives bounded nonnegative subsequences

`0<=f(a^n)<=1`

and, for the inverse,

`0<=f(d^n)<=1`.

## 3. Exact periodic obstruction

Put

`g=gcd(|a|,|d|)`,
`h=gcd(|b|,|c|)`.

The gcd of the four Laurent-polynomial annihilators is

`(T^g-1)(T^h-1)`.

`det A=+-1` implies `gcd(g,h)=1`.

Hence

`f(n)=u(n)+v(n)+lambda*n`

with `u` `g`-periodic and `v` `h`-periodic.

Evenness forces `lambda=0`; therefore `f` has period `gh`.

If `g=1`, then `h|c` and period `h` gives

`f(c)=f(0)=0`,

contradicting `f(c)=1/2`.

If `h=1`, then `g|a` and period `g` gives

`f(a)=f(0)=0`,

contradicting `f(a)=1/2`.

This obstruction is independent of any downstream regularity assumption.

## 4. Small exact nonsurvivor certificates

### C1 — immediate axis certificate

`A=[[2,1],[3,1]]`,
`det A=-1`.

The first column is admissible, but

`gcd(2,1)=1`,
`gcd(1,3)=1`.

Already on input `(0,e)` the free outputs are `(e,e)`.

Any scalar would have to satisfy

`2 q(e)=q(0)+q(e)`,

that is

`2=1`.

So this operator fails before any subtle periodic argument is needed.

### C2 — both pair gcds one

`A=[[2,5],[3,7]]`,
`det A=-1`.

The first column `(2,3)` is admissible, but `(g,h)=(1,1)`.

The derived period is one, forcing `f(0)=f(1)`, contradicting normalization.

### C3 — only the off-diagonal pair gcd survives

`A=[[2,3],[3,5]]`,
`det A=1`.

Here `(g,h)=(1,3)`.

The derived period is three.  Since `c=3`,

`f(c)=f(0)=0`,

contradicting balance.

### C4 — only the diagonal pair gcd survives

`A=[[2,1],[3,2]]`,
`det A=1`.

Here `(g,h)=(2,1)`.

The derived period is two.  Since `a=2`,

`f(a)=f(0)=0`,

contradicting balance.

## 5. No support-stratum outsider

If `g,h>1`, choose primes

`p|g`,
`r|h`.

They are distinct.

Modulo `p`, `A` is anti-diagonal monomial.

Modulo `r`, `A` is diagonal monomial.

Therefore `A in S_{p,r}`.

Conversely every `S_{p,r}` matrix has one prime dividing its diagonal pair and the other dividing its off-diagonal pair, so `g,h>1`.

Hence exactly

`SURVIVOR_FREE = union S_{p,r}`.

There is no residual exceptional family.

## 6. Complete second-column countermodel boundary

Fix primitive admissible `(a,c)` and determinant sign `eps`.

With one completion `(b0,d0)`, all completions are

`(b,d)=(b0+k a,d0+k c)`.

A completion survives iff at least one prime divisor of `a` also divides `d`, and at least one prime divisor of `c` also divides `b`.

Equivalently

`k=-d0*c^-1 mod p` for some `p|a`,

and

`k=-b0*a^-1 mod r` for some `r|c`.

Thus successful completions are a finite union of exact CRT progressions; all other `k` are exact nonsurvivors.

## 7. Lift ablation

For each surviving free block:

- torsion-blind witness exists;
- every `B in M_2(F3)` survives;
- every `D in GL_2(F3)` survives;
- total lifts `3888`.

For each nonsurviving free block:

- torsion-min envelope would produce a forbidden free survivor;
- therefore no `B,D` survives;
- total lifts `0`.

So:

`LIFT_MEMBERSHIP_IS_ALL_OR_NOTHING_OVER_EACH_FREE_BLOCK`.

and

`TORSION_SENSITIVE_ONLY_LIFT_EXISTS=false`.

## 8. Physical-equivalence ablation

The pair

`(g,h)=(gcd(|a|,|d|),gcd(|b|,|c|))`

is unchanged by:

- left sign gauge;
- right sign gauge;
- `A -> P A P`;
- `A -> A^-1`.

Therefore both the positive verdict and the obstruction certificate descend to physical classes.

## 9. Deterministic evidence

Checker:

`scripts/cbrc_f3r2_validate_survivor_membership.py`

Digest:

`5df55db542c5027adbd5ad1e3f9c9278b0cf1275a8e9ba6cf74be4c340f5696c`

Regression mismatch count:

`0`.

No finite search is used as the proof of the arbitrary-integer theorem.
