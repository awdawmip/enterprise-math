# Prime Fusion Theorem Package — Version 1

Status: `ACTIVE RESEARCH PACKAGE / NOT CANONICAL FOUNDATION / TASK_RESEARCH`
Date: `2026-08-23`
Researcher-ID: `EM-FREE-P7K4N2`
Research-Mode: `TASK_RESEARCH`
Origin: free-discovery prime arrangement program, post-freeze theorem packaging
Source foundation: `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`
Scope: one native sector `S_12`; cyclic sector copies are symmetric, but no unproved cross-seam global-neighbor claim is made.

## 0. Objects and status discipline

For an interior sector cell with positive integer coordinates `(a,b)` define

`N(a,b) = a^2+b^2`,

`C(a,b) = a^2-ab+b^2`.

`N` is the current sector-local native squared-length readout. `C` is a classical triangular-carrier quadratic readout used here as a second channel. Their simultaneous arithmetic is the object of this package.

A **dual-prime cell** means `N(a,b)` and `C(a,b)` are both ordinary primes.

Theorems below are unconditional elementary algebra/number theory. Statements about infinitely many dual-prime cells, Bateman–Horn asymptotics, empirical continuous limit laws, and novelty are explicitly outside the proved layer.

---

## T1 — Simultaneous diagonal coordinates

Put `u=a+b`, `v=a-b`. Then `2N=u^2+v^2`, `4C=u^2+3v^2`. Conversely `u^2=3N-2C`, `v^2=2C-N`. Hence every interior cell satisfies `C<N<2C`, with strictness for nondegenerate dual-prime cells.

## T2 — Exact common-divisor law

For all integers `a,b`, `gcd(N(a,b),C(a,b))=gcd(a,b)^2`. In particular primitive cells have coprime channels.

## T3 — Fusion algebra and discriminant 12

Let `f=X^2+1`, `g=X^2+X+1`, `F=fg`. Because `g-f=X` and `f-X(g-f)=1`, the two factors are comaximal in `Z[X]`, hence

`R=Z[X]/(F) ~= Z[i] x Z[omega]`.

Moreover `Disc(F)=(-4)(-3)*1^2=12`. For `xi=(i,omega)`, the component norms of `a+b xi` are exactly `N(a,b)` and `C(a,b)`.

## T4 — Primitive pointed quotient collapse

For a primitive cell, set `N=N(a,b)`, `C=C(a,b)`, `H=NC`. Then

`R/(a+b xi) ~= Z/NZ x Z/CZ ~= Z/HZ`.

The natural pointed residue is `r == -a*b^{-1} (mod H)`; it satisfies `F(r)==0 (mod H)`.

## T5 — Exact channel recovery

For the pointed residue in T4,

`N=gcd(H,r^2+1)`, `C=gcd(H,r^2+r+1)`.

No cross-channel factor can leak because `gcd(x^2+1,x^2+x+1)=1` for every integer `x`, via the Bezout identity `x^2+1-x[(x^2+x+1)-(x^2+1)]=1`.

## T6 — Reciprocal-trace Boolean collapse

For a unit `r mod H` with `F(r)=0`, let `T=r+r^{-1}`. Since `F` is reciprocal,

`F(r)/r^2=T^2+T`.

Thus `e:=-(r+r^{-1})` is idempotent mod `H`. For a primitive cell,

`N=gcd(e,H)`, `C=gcd(e-1,H)`.

The quartic fusion equation therefore collapses through reciprocal trace to a Boolean channel idempotent.

## T7 — Unordered cell reconstruction from `(H,e)`

Given an idempotent `e mod H`, put `N=gcd(e,H)`, `C=gcd(e-1,H)`. Assume `NC=H`, `gcd(N,C)=1`, and `C<N<2C`. Then a positive primitive unordered cell exists exactly when

`U=3N-2C`, `V=2C-N`

are perfect squares. In that case

`{a,b}={ (sqrt(U)+sqrt(V))/2, (sqrt(U)-sqrt(V))/2 }`.

The square roots automatically have the same parity because `U==V==N (mod 2)`.

## T8 — Dual-prime finite-quotient characterization

For an interior primitive cell with both channels greater than `1`, dual primality is equivalent to

`R/(a+b xi) ~= F_p x F_q`

with distinct primes `p=N`, `q=C`. Equivalently the total norm is the square-free semiprime `pq` with the two prime factors attached to the canonical channel components. This is a structural reformulation, not an algorithmic speedup claim.

## T9 — Prime residue classes and reciprocity lock

For an interior dual-prime cell with `p=N>3`, `q=C>3`, exactly one branch occurs:

`p==1 (mod 8) <=> q==1 (mod 12)`,

`p==5 (mod 8) <=> q==7 (mod 12)`.

Moreover

`(p/q)=(q/p)=(2/p)=(-1/q)=chi_12(q)`,

with `chi_12(q)=+1` on `q==1 mod12` and `-1` on `q==7 mod12`.

Proof sketch: odd `p` forces opposite parity of `a,b`. The even coordinate modulo `4` gives the paired mod-8/mod-4 branch; primitive representation gives `q==1 mod3`. Modulo `q`, with `t=a b^{-1}`, one has `t^2-t+1=0` and `p==t b^2`, so `(p/q)` is the quadratic character of an order-6 root, determined by `q mod12`; reciprocity applies because `p==1 mod4`.

## T10 — Four mixed phases and the order-12 automorphism orbit

Under T9, the pointed residue has `ord_p(r)=4`, `ord_q(r)=3`, hence `ord_H(r)=12`. The four simultaneous mixed roots are exactly

`{r,r^5,r^7,r^11}`

under `(Z/12Z)^x={1,5,7,11}`. The two shared-coefficient cell phases are `{r,r^11}={r,r^{-1}}`, corresponding to `(a,b)` and `(b,a)`; the remaining pair `{r^5,r^7}` are algebraically valid mixed roots but not the same-coefficient swap pair.

Thus the shared-coefficient phase is one coset bit in `(Z/12Z)^x/{+/-1} ~= C2`.

## T11 — Sixth-power phase-blind channel readout

Under T10,

`r^6==-1 (mod p)`, `r^6==+1 (mod q)`.

Therefore all four mixed phases have the same sixth power modulo `H`, and

`p=gcd(H,r^6+1)`, `q=gcd(H,r^6-1)`.

Channel recovery is phase-blind; phase recovery is a later layer.

## T12 — Local prime-direction classification

Let `l>3` be prime and `(a,b)` primitive modulo `l`.

If `l|N`, then `-1` is a square mod `l`, hence `l==1 or5 (mod12)`.

If `l|C`, then `-3` is a square mod `l`, hence `l==1 or7 (mod12)`.

Consequently `5 mod12` primes can occur only in `N`, `7 mod12` only in `C`, `11 mod12` in neither, and `1 mod12` is the only unramified class that may occur in either channel.

## T13 — Fixed-corridor local root count

Parameterize a corridor by `a=t+k`, `b=t`:

`F_k=2t^2+2kt+k^2`, `G_k=t^2+kt+k^2`.

Even `k` makes `F_k` identically even up to the finite value-2 degeneracy. For odd `k`, every prime modulus leaves a survivor class. More precisely, for prime `l>3`,

- if `l|k`, the union of roots is `{0}` and `nu_l(k)=1`;
- if `l` does not divide `k`, the two root sets are disjoint because `2G_k-F_k=k^2`, and

`nu_l(k)=2+chi_-4(l)+chi_-3(l)`,

namely `4,2,2,0` for `l mod12=1,5,7,11`.

Also `nu_2=0`, `nu_3=1`. Therefore every odd corridor is locally admissible. This does not prove infinitely many simultaneous primes.

## T14 — Sector-local nearest-neighbor matching theorem

Inside `S_12`, use carrier-neighbor steps `(1,0),(0,1),(1,1)`. For dual-prime cells with `N,C>3`, opposite parity of `a,b` excludes dual-prime adjacency in the first two directions. Every possible edge lies on a fixed `(1,1)` corridor. Along three consecutive corridor points, `u=a+b` advances by `2`, so one has `u==0 mod3`; since `4C=u^2+3v^2`, that point has `3|C` and, outside the finite `C=3` degeneracy, is not dual-prime. Hence every sector-local connected component has size at most `2`.

This theorem is sector-local only; no cross-seam global-neighbor statement is asserted.

## T15 — Finite-sieve corridor mean preservation

For any finite prime set `P`, put `M=prod(P)`. Parameterize `(a,b)=(t+k,t)`. The map `(t,k)->(a,b)` has determinant `-1` and is a bijection modulo `M`. Therefore the average, over `k mod M`, of the exact one-dimensional corridor survivor density equals the exact two-dimensional survivor density for `(N,C)` modulo `M`, with the same multiplicative normalization. This is an exact finite-level downward-collapse mean law, not an asymptotic prime theorem.

## Proved / conjectural boundary

The package claims T1–T15 only. It does **not** claim: infinitely many dual-prime cells; Bateman–Horn asymptotics; global three-sector seam matching; shortest-vector defect-spectrum formulas; empirical angle-limit laws; external novelty.

A deterministic checker is paired with this package on the same branch. It validates identities and finite modular consequences but is not a substitute for the proofs.
