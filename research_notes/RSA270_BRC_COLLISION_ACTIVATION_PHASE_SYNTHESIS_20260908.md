# RSA-270 BRC Collision / Activation / Phase Synthesis

Status: `RESEARCH SYNTHESIS / EXACT FRONTIERS + ROUTE CLOSURES + NEXT HARD UNIT / NO FACTOR FOUND / NO SPEEDUP CLAIM`
Date: `2026-09-08`
Source snapshot before write: `main@c158e0eb19d430c521b764baf2f671e96edd924f`

## 0. Parent objective

Continue the composite odd-multiplier BRC attack on RSA-270 after the boundary-collision idea, without returning to already negative rotation/72-only/coarse-shadow routes.

This synthesis records the highest durable frontier reached in the continuation and identifies the smallest genuinely new units that remain. It is a research handoff, not a theorem or Foundation promotion.

---

## 1. Hidden multiplier lattice collapses exactly to two factor coordinates

For odd split `a=2r+1`, `b=2s+1`, the hidden boundary satisfies

`L_(a,b)-L_(1,1)=r*p+s*q`.

Hence the whole composite odd-multiplier boundary family is the linear image of a public integer lattice under the two hidden basis lengths `(p,q)`.

Exchange-pair sums/differences reduce to `(S,g)` with

`S=p+q`, `g=q-p`.

No larger composite multiplier horizon creates new algebraic dimensions by itself.

---

## 2. Exact collisions are too late; second moment is factor-complete immediately

A nontrivial exact boundary collision requires

`(a-c,b-d)=t(q,-p)`.

Parity forces even `t`, and the first odd-grid collision occurs at multiplier-coordinate horizon `2q+1`, i.e. factor scale.

But at `K=3`, centered hidden points are already `{0,p,q}`. Their pairwise square-distance energy is

`E3=p^2+q^2+(q-p)^2=2*S^2-6*N`.

Thus one exact hidden second moment already determines `S` and factors. General symmetric domains satisfy

`E_K=A_K*S^2+B_K*N`.

All such second moments are rank-one over the single unknown `S^2`; larger K does not add independent moment dimensions.

---

## 3. Fixed local modular route reaches an exact RSA-270 ceiling

For odd prime `ell` not dividing N, the local product fiber has hidden

`S^2=(a+N/a)^2 mod ell`.

Its exact quotient orbits under

`a -> a, N/a, -a, -N/a`

have count

`c_ell(N)=(ell+1+chi(N)+chi(-N))/4`.

Every `ell>=7` leaves at least two factor-sensitive S^2 orbits. `ell=5` collapses only when N is a nonresidue.

RSA-270 has `N mod5=2`, so together with the odd-prime universal 2/3-adic residue one gets

`S^2=1984 mod2880`,

`g^2=36 mod2880`,

`E3=2486 mod5760`.

Direct prime-power witnesses show this fixed local singleton does not lift to `2^7`, `3^3` or `5^2`. Fixed local residue-only work is therefore closed unless an additional factor-sensitive orbit selector is found.

---

## 4. Boundary order is exactly a least-factor threshold

Pure boundaries satisfy

`L_(2u+1,1)<L_(1,2v+1)`

iff

`u/v<q/p`.

Eliminating q gives

`u/v<q/p`

iff

`p<sqrt(v*N/u)`.

So the one-bit hidden boundary-order oracle is exactly a least-factor threshold oracle.

The same bit is a threshold of E3:

`u*v*E3 > 2*N*(u^2-u*v+v^2)`

for thresholds in the relevant ratio range.

Current square-gap BRC is orientation-blind because it retains `(a*p-b*q)^2` and erases the sign deciding the order bit.

---

## 5. Existing valuation-wall tool already implements threshold semantics

The admitted project tool

`t1.nonly_valuation_wall_gcd_extractor`

uses

`A_s=(2s)!(3s)!/(s!)^5`

with exact first-prime activation

`r|A_s <=> 3s>=r`

for prime r>3, s<r.

Therefore boundary ordering did not create a new semantic primitive. It composes directly with the existing N-only activation wall. The current project implementation cost is linear in factor-scale recurrence length; generic fast recurrence/block-product methods reduce this to classical square-root-of-index territory rather than a new factoring result.

A tunable wall `(cs)!/(s!)^c` moves the activation index but conserves Theta(p) direct-stream factor work.

---

## 6. BRC state compression is extreme, but constructor compression is the real problem

For squarefree N,

`Phi_N(X)=gcd(X,N)`

obeys

`Phi_N(XY)=lcm(Phi_N(X),Phi_N(Y))`.

For semiprime N the exact multiplicative quotient has four divisor-lattice states `{1,p,q,N}`. Inside a certified one-factor zone below q, Boolean unit/nonunit is sufficient until success.

If a bracket `L<p<=U<q` has width `H=U-L<p`, the exact short activation wall

`C(U,H)=prod_(j=1)^H (L+j)/j`

has gcd 1 before p and gcd p after crossing p.

So a huge factor search can have a constant-size operation-safe BRC observer.

But no small-state theorem gives a small constructor automatically:

`STATE_COMPRESSION != EVALUATION_COMPRESSION`.

This is the main positive/Boolean BRC wall.

---

## 7. Strong external interval baseline and the (gamma,beta) phase diagram

Near balanced factor scale, the Harvey-Hittmeir deterministic interval-divisor method gives effective Coppersmith cell width about `N^(1/4)` and interval cost

`(H/N^(1/4)+1)*polylog(N)`.

Suppose an N-only preconditioner shrinks the least-factor interval to

`H=N^(1/2-gamma+o(1))`.

Then unresolved cell count is

`C=N^(1/4-gamma+o(1))`.

If a collective one-factor Boolean/gcd constructor processes C cells in

`C^(beta+o(1))`

work, the main exponent before charging the preconditioner is

`e=beta*(1/4-gamma)`.

To beat exponent one fifth:

`beta*(1/4-gamma)<1/5`.

Important axes:

- no growing localization (`gamma=0`) -> need `beta<4/5`;
- linear cell evaluation (`beta=1`) -> need `gamma>1/20`.

For 895-bit RSA-270, `gamma=1/20` corresponds to roughly 45 bits of genuinely growing magnitude localization.

This is the current quantitative admission test for any future BRC factoring claim on this line.

---

## 8. RSA-270 public construction priors do not supply growing localization

Archived RSA Challenge metadata gives the original-list factors as randomly chosen primes of approximately equal length and both `2 mod3`.

A 2026 solved-family study found all then-known Challenge factors start with prefix `11`, but classifies this as family-level high-bit evidence and does not establish an additional residual factor-balance signature or reduced factoring resistance.

The 2026-09-03 RSA-260 factorisation provides a new out-of-data-freeze consistency check: both 431-bit factors start with `11` and are `2 mod3`.

Even conditionally transferring prefix `11`, adjacent 447/448 bit allocation and mod-3 to RSA-270 gives only a few bits of finite pruning. Exact product consistency narrows the prefix-11 p interval by only about a further factor 2.13. These are constant-information constraints and correspond to `gamma=0`.

Route B is therefore closed absent genuinely new authenticated leakage or a new N-only growing-magnitude theorem.

---

## 9. Finite-group phase exposes a universal N-only shadow but decoding is the hard step

For every unit alpha modulo N,

`N+1-S=phi(N)`

implies

`alpha^S=alpha^(N+1)`.

More generally for every integer polynomial F,

`alpha^(F(S,N))=alpha^(F(N+1,N))`.

Hence

`alpha^E3=alpha^(2(N^2-N+1))`,

`alpha^(g^2)=alpha^((N-1)^2)`.

So all hidden S-polynomial collision energies have N-only group-phase images for free. The missing step is decoding the exponent residue/value from the phase, i.e. discrete-log/collision work.

The existing project rational-holonomy BRC carrier is positive rational/valuation-valued and cannot be silently identified with finite unit-group phase.

---

## 10. Minimal finite-group phase BRC is exactly BSGS

For candidate exponent population C, an explicit two-support phase meet-in-the-middle with supports A and B must satisfy

`A*B>=C`.

Therefore

`A+B>=2*sqrt(C)`.

Balanced baby-step/giant-step achieves the scoped bound. Increasing branch arity without extra algebra does not automatically beat the square-root wall.

Large multiplicative order enlarges the injective phase range; it is not a free discrete logarithm.

Thus a phase-BRC extension only becomes algorithmically new if it either reduces the guaranteed candidate population or constructs the phase collision implicitly in sub-square-root work.

---

## 11. Composite multiplier phase also collapses to one hidden trace

Let

`Y=alpha^S`, `z=alpha^g`,

and for exchange pair `(a,b),(b,a)` put

`d=(a+b)/2`, `c=(a-b)/2`.

Then hidden phase values are

`U=Y^d z^(-c)`,

`V=Y^d z^c`.

Their product is N-only; all exchange-sensitive trace data reduce to

`tau_c=z^c+z^(-c)`

with recurrence

`tau_(c+1)=tau_1*tau_c-tau_(c-1)`.

So larger composite multiplier phase grids still contain only one hidden trace coordinate. Higher traces are just Chebyshev polynomials of `tau_1`.

No independent phase dimension is created by enlarging the multiplier lattice.

---

## 12. Direct boundary phase search is prior-art-identical

The hidden boundary exponent is

`X=2L_(a,b)+2=a*p+b*q`.

For any unit alpha,

`alpha^X == alpha^(a+b*N) (mod p)`,

`alpha^X == alpha^(a*N+b) (mod q)`.

Therefore a correct candidate x for the boundary linear form immediately gives a factor gcd against the corresponding public phase anchor.

This is exactly the Lehman/Hittmeir/Harvey type linear-combination phase bridge, up to coefficient naming. The direct continuation “expand `(a,b)`, group-search `L_(a,b)`” is therefore not a new candidate family.

The project’s earlier X6/Frobenius multiresolution line also already found generic factor-scale width walls and classified scalar cyclic periods into multiplicative-order/Pollard-p-1 territory.

Route C is closed unless a new theorem shrinks the guaranteed coefficient/candidate family or beats the explicit square-root phase collision.

---

## 13. Current route table

### Closed / do not replay without new evidence

- exact boundary collisions at larger K;
- larger second-moment families `E_K`;
- fixed local prime residues and cheap J/R shadows;
- square-gap proximity as a substitute for orientation;
- direct streamed valuation walls;
- generic BSGS/product-tree/random-access repackaging;
- ordinary Lucas/Chebyshev/Frobenius/multiplicative-order reinterpretations;
- direct group search of the same `a*p+b*q` boundary family;
- fixed RSA-270 construction prefixes/residue priors as if they were growing bits.

### Genuine open units

**A. Collective one-factor constructor:** with no growing preconditioner, construct the OR/proper-gcd state of `C` balanced Coppersmith cells in effective `C^beta` work with `beta<4/5`, without simply invoking a stronger known factoring engine.

**B. Growing N-only preconditioner:** derive a factor interval/coset with localization exponent `gamma>0`; with linear cell evaluation, crossing the current one-fifth benchmark needs `gamma>1/20`.

**C. New phase candidate reduction:** prove an N-only selection theorem producing a guaranteed factor-bearing exponent/linear-form population asymptotically smaller than the best known deterministic parameterizations before BSGS.

Any mixed A+B route is scored by

`beta*(1/4-gamma)<1/5`

with all preconditioner construction costs charged.

---

## 14. Current result

RSA-270 is **not factored** by this continuation.

The gain is a much sharper research boundary:

- collision energy, factor threshold, valuation wall and finite-group phase have been algebraically unified;
- several superficially new multiplier/phase ideas have been identified as exact restatements of classical deterministic-factorisation mechanisms;
- the surviving research target is now quantitative rather than terminological.

Next continuation should begin directly at A/B/C above and must not re-open closed branches merely because they can be expressed in a different BRC observer language.

No Foundation promotion, Working Truth promotion, or factoring-speedup claim is made.