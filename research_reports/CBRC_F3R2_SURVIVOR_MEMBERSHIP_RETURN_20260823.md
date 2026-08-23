# CBRC F3R2 — Survivor Membership Predicate Completion Return

Researcher-ID: `EM-CBRC-F3R2-6C8E41`

Task: `RS-CBRC-F3R2-SURVIVOR-MEMBERSHIP-PREDICATE-COMPLETION`

Owner branch:

`research/cbrc-f3r2-survivor-membership-predicate-completion`

Taskbook source:

`f4a98e4c0f9f8669f75e44ee1ef979236334b48a`

Allowed F3R owner packet:

`02dd3cc0be4843cbfa4b4bb3b83ec886b6429648`

Driver review:

`93c48c015c4b1522eaf8566586ed76bab31fa324`

Primary verdict:

`F3R2_ALL_SURVIVORS_DECIDABLE_BY_FINITE_EXACT_PREDICATE`

Hard target:

`BALANCED_MIXING_SURVIVOR_MEMBERSHIP_PREDICATE_CLASSIFIED`

Target-leak status:

`TARGET_LEAK_AUDIT_PASS`

## 1. Executive result

The arbitrary-operator membership gap is closed.

Let a full current-carrier two-slot additive automorphism be

`M=(A,B,D)`

with

`A=[[a,b],[c,d]] in GL_2(Z)`,
`B in M_2(F3)`,
`D in GL_2(F3)`.

Define the two cross-pair gcd invariants

`g(A)=gcd(|a|,|d|)`,
`h(A)=gcd(|b|,|c|)`.

Then the exact survivor predicate is

`SURVIVOR(M) <=> g(A)>1 and h(A)>1`.

Equivalently, without presupposing that `M` is already an automorphism,

`SURVIVOR(A,B,D)`

iff all of the following hold:

1. `det(A)=+1 or -1`;
2. `det(D) != 0 mod 3`;
3. `gcd(|a|,|d|)>1`;
4. `gcd(|b|,|c|)>1`.

There is **no additional condition on `B`**.

Consequences:

- membership depends only on the free block `A`;
- every surviving free block has all `81*48=3888` torsion/cross lifts;
- no lift survives only because of a torsion-sensitive scalar;
- no free survivor exists outside the union of the F3R support-splitting strata `S_{p,r}`;
- every survivor belongs to at least one such stratum, usually several;
- every admissible first column still has infinitely many successful second-column completions, but not every unimodular completion succeeds.

Thus F3R's support-splitting family was not merely a large subclass: its union over prime pairs is exactly the complete survivor set.

## 2. Torsion-min envelope theorem

The first step is to eliminate the possibility that torsion/cross data can rescue a bad free block.

Let

`q:C1 -> R_nonnegative`

be any full admissible marked scalar for `M=(A,B,D)`.

For every free integer `n`, define

`f(n)=min_{t in F3} q(n,t)`.

### Theorem 2.1 — torsion-min envelope

`f` satisfies the exact free conservation problem for `A`:

1. `f(n)>=0`;
2. `f(0)=0`;
3. `f(1)=1`;
4. `f(-n)=f(n)`;
5. for all `x,y in Z`,
   `f(ax+by)+f(cx+dy)=f(x)+f(y)`;
6. for the elementary first-column split,
   `f(a)=f(c)=1/2`.

#### Proof

Fix free input coordinates `(x,y)`.  Write their residues modulo three as `r`.

As the two input torsion labels `t=(t1,t2)` range over `F3^2`, the two output torsion labels are

`B r + D t`.

Because `D in GL_2(F3)`, this is a bijection of `F3^2`.

Full marked conservation holds pointwise for every input torsion pair.  Taking the minimum over all nine input torsion pairs therefore gives

`min_{s1,s2} (q(u,s1)+q(v,s2))
 = min_{t1,t2} (q(x,t1)+q(y,t2))`,

where `(u,v)=A(x,y)`.

The two minima separate by coordinate, hence

`f(u)+f(v)=f(x)+f(y)`.

Nonnegativity and `q(0,0)=0` give `f(0)=0`.

At free coordinate `1`, accepted `R` cycles all three torsion labels, so M2 plus `q(e)=1` gives

`q(1,0)=q(1,1)=q(1,2)=1`;

therefore `f(1)=1`.

Accepted `J` identifies the free signs after minimizing over torsion, so `f(-n)=f(n)`.

Finally, the actual elementary outputs of `M(e,0)` each have scalar `1/2` by balance and conservation.  Hence

`f(a)<=1/2`,
`f(c)<=1/2`.

Applying the just-proved free conservation to `(1,0)` gives

`f(a)+f(c)=f(1)+f(0)=1`.

Therefore both inequalities are equalities:

`f(a)=f(c)=1/2`.

This proves the theorem.

### Corollary 2.2

If any full lift `(A,B,D)` survives, then the free block `A` admits a torsion-blind balanced conserved scalar.

So torsion sensitivity can enlarge the scalar family of an already-surviving operator, but it cannot enlarge the operator membership set.

## 3. Free scalar setup

From now on let

`f:Z -> R_nonnegative`

satisfy

`f(0)=0`,
`f(1)=1`,
`f(-n)=f(n)`,

and

`f(ax+by)+f(cx+dy)=f(x)+f(y)`                        `(E)`

for every `x,y in Z`, with

`f(a)=f(c)=1/2`.

Since `A` is unimodular, `A^-1` also conserves the same scalar.

From `(E)` at `(0,1)` and from the first column of `A^-1` one obtains

`f(b)+f(d)=1`,
`f(d)+f(c)=1`.

Hence

`f(b)=f(d)=1/2`.

Thus every entry of a surviving free block is nonzero and has absolute value at least two.

More generally, for every integer `n`,

`f(an)+f(cn)=f(n)`,
`f(bn)+f(dn)=f(n)`,
`f(dn)+f(cn)=f(n)`,
`f(bn)+f(an)=f(n)`,

so

`f(an)=f(dn)`,
`f(bn)=f(cn)`.

## 4. Mixed-difference annihilator theorem

For an integer step `m`, write

`Delta_m f(t)=f(t+m)-f(t)`.

Take the mixed discrete difference in the two input variables of `(E)`.  With

`u=ax+by`,
`v=cx+dy`,

one gets

`(Delta_a Delta_b f)(u) + (Delta_c Delta_d f)(v)=0`.

Because `A` is a bijection of `Z^2`, `u` and `v` range independently.  Therefore

`Delta_a Delta_b f = kappa`,
`Delta_c Delta_d f = -kappa`

for one constant `kappa`.

### Lemma 4.1 — the constants vanish

`kappa=0`.

A standard one-dimensional finite-difference decomposition for coprime nonzero steps `a,b` gives, from

`Delta_a Delta_b f = kappa`,

a representation

`f(n)=kappa*n^2/(2ab) + lambda*n + u(n)+v(n)`,

where `u` is `|a|`-periodic and `v` is `|b|`-periodic.

The axis conservation relation gives

`0 <= f(a^m) <= f(1)=1`

for every `m>=0`.

If the quadratic coefficient is negative, nonnegativity fails for large `|n|`.  If it is positive, the bounded sequence `f(a^m)` is impossible.  Hence the quadratic coefficient, and therefore `kappa`, is zero.

Applying the same argument to the inverse matrix yields the remaining two zero mixed differences.

Thus every survivor satisfies exactly

`Delta_a Delta_b f = 0`,
`Delta_c Delta_d f = 0`,
`Delta_d Delta_b f = 0`,
`Delta_c Delta_a f = 0`.                                 `(D)`

## 5. Polynomial gcd collapse

Let `T` denote the unit shift on sequences and put

`P_m=T^|m|-1`.

Negative steps differ only by multiplication by a Laurent monomial unit, so `(D)` says that `f` is annihilated by

`P_a P_b`,
`P_c P_d`,
`P_d P_b`,
`P_c P_a`.

Define

`g=gcd(|a|,|d|)`,
`h=gcd(|b|,|c|)`.

Because `det(A)=+-1`, no prime divides all four entries, so

`gcd(g,h)=1`.

In the Laurent polynomial PID, the gcd of the four annihilator polynomials above is exactly

`G(T)=(T^g-1)(T^h-1)`.

One way to see this is cyclotomic-factor by cyclotomic-factor:

- a factor occurs in every one of the four products iff its order divides both `a,d`, or divides both `b,c`;
- the first condition contributes `T^g-1`;
- the second contributes `T^h-1`;
- because `g,h` are coprime, their only common root is `1`, and both sides carry the same double multiplicity there.

Therefore Bezout in the Laurent polynomial ring gives

`G(T) f = 0`.                                             `(G)`

### Theorem 5.1 — forced period

Every admissible free scalar is `g*h`-periodic.

Indeed, the roots of `(G)` are roots of unity.  Since `gcd(g,h)=1`, the only repeated root is `1`, so every two-sided real solution is

`f(n)=u(n)+v(n)+lambda*n`,

with `u` `g`-periodic and `v` `h`-periodic.

Evenness of `f` forces `lambda=0`.

Hence

`f(n+gh)=f(n)` for every integer `n`.

This periodicity is derived from conservation.  No periodic scalar ansatz is assumed.

## 6. Exact free-block membership theorem

### Theorem 6.1

For arbitrary `A=[[a,b],[c,d]] in GL_2(Z)`, a nonnegative even normalized balanced conserved scalar exists iff

`gcd(|a|,|d|)>1`
and
`gcd(|b|,|c|)>1`.

#### Necessity

Let `g,h` be as above.

If `g=1`, Theorem 5.1 makes `f` `h`-periodic.  Since `h|c`,

`f(c)=f(0)=0`,

contradicting balance `f(c)=1/2`.

If `h=1`, the same argument makes `f` `g`-periodic.  Since `g|a`,

`f(a)=f(0)=0`,

again contradicting balance.

Thus `g>1` and `h>1`.

#### Sufficiency

Assume `g>1` and `h>1`.

Choose a prime

`p|g`

and a prime

`r|h`.

Since `gcd(g,h)=1`, `p!=r`.

Modulo `p`,

`a=d=0`,

and unimodularity forces `b,c` to be nonzero, so `A mod p` is anti-diagonal monomial.

Modulo `r`,

`b=c=0`,

and unimodularity forces `a,d` to be nonzero, so `A mod r` is diagonal monomial.

The two permutation types are opposite.  Therefore the accepted F3R support-splitting theorem applies:

`q_{p,r}(n,t)=1/2*(1_{p does not divide n}+1_{r does not divide n})`

is nonnegative, unary-invariant, normalized, balanced, and exactly conserved.

Hence `A` survives.

Deliverable:

`F3R2_FREE_BLOCK_MEMBERSHIP_CLASSIFIED`.

## 7. Exact position of the support-splitting strata

The preceding proof gives the identity

`SURVIVOR_FREE`

`= union_{distinct primes p,r} S_{p,r}`

`= {A in GL_2(Z): gcd(|a|,|d|)>1 and gcd(|b|,|c|)>1}`.

Therefore:

`FREE_SURVIVORS_OUTSIDE_ALL_S_p_r = NONE`.

The `S_{p,r}` are not merely examples, not merely extremal rays, and not merely a generating family.  Their union is the exact full free survivor set.

A given survivor need not determine a unique prime pair.  It belongs to every compatible stratum obtained by taking one prime divisor of `g` and one prime divisor of `h` with the opposite monomial orientation.

Thus the F3R underdetermination theorem remains intact: the membership set is now exact, but it still contains infinitely many inequivalent matrices and overlapping prime-pair presentations.

Deliverable:

`F3R2_SUPPORT_SPLIT_STRATA_POSITION_CLASSIFIED = UNIVERSAL_EXACT_COVER`.

## 8. Exact second-column classification

Fix an admissible primitive first column `(a,c)^T`, so

`gcd(a,c)=1`,
`|a|>=2`,
`|c|>=2`.

Fix determinant sign `eps in {+1,-1}`.

Choose one Bezout completion `(b0,d0)` such that

`a*d0-c*b0=eps`.

Every completion with that determinant sign is uniquely

`b=b0+k*a`,
`d=d0+k*c`,
`k in Z`.

The exact membership condition becomes

`gcd(|a|,|d0+k*c|)>1`
and
`gcd(|c|,|b0+k*a|)>1`.                                  `(K)`

Equivalently, there must exist a prime `p|a` and a prime `r|c` such that

`k = -d0*c^(-1) mod p`,
`k = -b0*a^(-1) mod r`.

Because `gcd(a,c)=1`, `p!=r`; each pair gives one CRT residue class modulo `pr`.

Hence all successful second columns are exactly the finite union

`K_eps(a,c) = union_{p|a, r|c} (k_{p,r} + pr Z)`.

This proves simultaneously:

- not every unimodular second-column completion survives;
- every admissible first column has infinitely many successful completions;
- the successful completions are an explicit finite union of arithmetic progressions;
- there are no additional exceptional completions outside the support-splitting union.

This closes the second-column gap left by F3R.

## 9. Exact full lift membership

### Theorem 9.1

For an ambient automorphism triple

`(A,B,D) in GL_2(Z) x M_2(F3) x GL_2(F3)`, 

`(A,B,D)` survives iff

`gcd(|a|,|d|)>1`
and
`gcd(|b|,|c|)>1`.

There is no further restriction on `B` or `D`.

#### Proof

Necessity is Theorem 2.1 plus Theorem 6.1.

For sufficiency, choose any compatible `p|g`, `r|h` and use the torsion-blind witness `q_{p,r}`.  Since this scalar ignores the torsion coordinate entirely, the free-to-torsion cross block `B` and the invertible torsion block `D` cannot change its value.  The free block already conserves it, so every lift conserves it.

Thus each surviving free block has exactly

`81*48=3888`

surviving lifts.

Each nonsurviving free block has exactly zero.

In particular:

`TORSION_SENSITIVE_ONLY_LIFT_EXISTS = false`.

Torsion-sensitive scalar laws may exist on some already-surviving lifts, as F3/F3R showed, but they never create a new operator membership class.

Deliverable:

`F3R2_FULL_LIFT_MEMBERSHIP_CLASSIFIED`.

## 10. Scalar-variable elimination and exact feasibility criterion

F3R represented fixed-operator scalar laws by a normalized nonnegative annihilator cone `Q(M)`.

F3R2 eliminates those scalar variables completely at membership level:

`Q(M) != empty`

iff

`gcd(|a|,|d|)>1 and gcd(|b|,|c|)>1`.

The forward implication is not a restatement of cone nonemptiness: it is the torsion-min envelope theorem plus the mixed-difference / Laurent-polynomial gcd obstruction.

The reverse implication supplies an explicit scalar witness.

Thus the feasibility problem is reduced to two ordinary integer gcd computations.

For a nonsurvivor the obstruction certificate is exact:

- if `g=1`, every hypothetical torsion-min scalar is forced to be `h`-periodic and therefore gives `f(c)=f(0)=0`, contradicting `f(c)=1/2`;
- if `h=1`, every hypothetical torsion-min scalar is forced to be `g`-periodic and therefore gives `f(a)=f(0)=0`, contradicting `f(a)=1/2`.

No infinite scalar search is necessary.

Deliverable:

`F3R2_SCALAR_FEASIBILITY_IFF_CLASSIFIED`.

## 11. Physical-equivalence normal form

The accepted free physical equivalence is generated by

`A -> E_L A E_R`,
`A -> P A P`,
`A -> A^-1`,

where `E_L,E_R` are diagonal sign matrices.

Under all these generators,

`gcd(|a|,|d|)`

and

`gcd(|b|,|c|)`

are unchanged.

Therefore the membership pair

`mu(A)=(g(A),h(A))`

is itself a physical-equivalence invariant.

A canonical decision normal form is:

1. verify `det A=+-1`;
2. verify `D in GL_2(F3)`;
3. compute `mu(A)=(g,h)`;
4. return survivor iff `g>1 and h>1`.

If a representative is also desired, use the already accepted finite physical free orbit and choose its lexicographically least flattened matrix; the membership answer is unchanged.

The decision algorithm terminates after finite Euclidean gcd computations.  No factorization is required to decide membership.

Prime factorization is needed only to output one explicit `q_{p,r}` witness or the complete CRT list of second-column strata, and trial division gives finite termination.

Deliverable:

`F3R2_PHYSICAL_MEMBERSHIP_NORMAL_FORM_CLASSIFIED`.

## 12. Exact counterexamples outside the support strata

Several admissible-first-column unimodular matrices fail the predicate:

1. `[[2,1],[3,1]]`, with `(g,h)=(1,1)`;
2. `[[2,5],[3,7]]`, with `(g,h)=(1,1)`;
3. `[[2,3],[3,5]]`, with `(g,h)=(1,3)`;
4. `[[2,1],[3,2]]`, with `(g,h)=(2,1)`.

The first has an especially small direct certificate:

input `(0,e)` has free outputs `(e,e)`, so conservation would require

`q(e)+q(e)=q(0)+q(e)`,

hence

`2=1`.

These examples show concretely that an admissible first column does not make every second-column completion survive.

By Theorem 7, there is no counterexample in the opposite direction: no survivor lies outside every `S_{p,r}`.

## 13. Deterministic checker

Required checker:

`scripts/cbrc_f3r2_validate_survivor_membership.py`

Deterministic digest:

`5df55db542c5027adbd5ad1e3f9c9278b0cf1275a8e9ba6cf74be4c340f5696c`

The checker verifies:

- accepted canonical `A0=[[2,3],[3,4]]`;
- the inherited infinite `A_t` six-periodic family;
- explicit admissible-first-column nonsurvivors outside all displayed strata;
- bounded `GL_2(Z)` regression through entry bound `9`;
- `1768` unimodular matrices in that box;
- `96` theorem-predicted survivors;
- `800` admissible-first-column but nonsurviving matrices;
- zero mismatch between the gcd predicate and the union of support-splitting strata;
- `33184` fixed-first-column / second-column CRT comparisons with zero mismatches;
- all `81*48=3888` lift choices for a survivor and zero for a nonsurvivor;
- `34992` exact torsion-affine bijection checks underlying the torsion-min envelope reduction;
- physical-equivalence invariance;
- `theorem_enumeration_mismatches=0`.

The bounded scan is regression evidence only.  The arbitrary-integer completeness theorem is the proof in Sections 2–10.

## 14. Final closure

Primary verdict:

`F3R2_ALL_SURVIVORS_DECIDABLE_BY_FINITE_EXACT_PREDICATE`.

Acceptance labels:

- `F3R2_FREE_BLOCK_MEMBERSHIP_CLASSIFIED`
- `F3R2_FULL_LIFT_MEMBERSHIP_CLASSIFIED`
- `F3R2_SCALAR_FEASIBILITY_IFF_CLASSIFIED`
- `F3R2_SUPPORT_SPLIT_STRATA_POSITION_CLASSIFIED`
- `F3R2_PHYSICAL_MEMBERSHIP_NORMAL_FORM_CLASSIFIED`
- `BALANCED_MIXING_SURVIVOR_MEMBERSHIP_PREDICATE_CLASSIFIED`
- `TARGET_LEAK_AUDIT_PASS`

Exact final predicate:

`SURVIVOR(A,B,D)`

`<=> det(A)=+-1`

`and det(D)!=0 mod 3`

`and gcd(|a|,|d|)>1`

`and gcd(|b|,|c|)>1`.

`B` is arbitrary.

No F4 or downstream comparison was opened.
