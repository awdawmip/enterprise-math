# RSA-270 continuation: odd-prime-power character atlas and mixed-radix Coppersmith handoff

Status: `RESEARCH NOTE / EXACT GENERALIZATION + PORTFOLIO REDUCTION / NOT CANONICAL PROMOTION`  
Researcher-ID: `EM-DIRECT-66DE45`  
Research mode: `TASK_RESEARCH`  
At: `2026-09-08T00:55:00+08:00`  
Parents:
- `research_notes/RSA270_PRIMITIVE_CHARACTER_GALOIS_PROJECTOR_20260908.md`
- `research_notes/RSA270_PUBLIC_PRIOR_COPPERSMITH_CUTOFF_20260908.md`

No RSA-270 factor is obtained.

## 1. The 3-adic character channel is one member of an odd-prime-power family

Let `l` be any odd prime, `e>=1`, and

`m=l^e`.

The group `(Z/mZ)^*` is cyclic. Choose a faithful primitive character `chi_(l,e)` of exact order

`phi(m)=(l-1)l^(e-1)`.

A faithful character is automatically odd because the unique order-2 unit `-1` maps to `-1`.

Let `zeta=zeta_m`, let `sigma_a(zeta)=zeta^a`, and define the normalized primitive Gauss/Galois projector

`Pi_chi(Z)=tau(conj chi)^(-1) sum_(a mod m)^* conj(chi(a)) sigma_a(Z)`.

As before,

`Pi_chi(zeta^t)=chi(t)`

with chi extended by zero to nonunits.

## 2. All-level odd-prime-power BRC projector theorem

For odd n and `gcd(n,l)=1`, put

`D(zeta)=(zeta^2-1)/(2zeta)`.

Then:

**Theorem.**

`Pi_chi( D(zeta) P_(l^e n)(zeta) )
 = 2 chi(2)^(-1) A_(l,e)(n)`

where

`A_(l,e)(n)=sum_(d|n) chi(d)`.

### Proof

Write a divisor of `l^e n` as `l^j a`, `a|n`, `0<=j<=e`. In the normalized W-block the monomial exponent is

`t=(l^j a + l^(e-j)n/a)/2`.

For every intermediate layer `1<=j<=e-1`, both summands are divisible by l, so `l|t`; primitivity gives

`Pi_chi(zeta^t)=Pi_chi(zeta^-t)=0`.

Only the two extreme layers survive:

- j=0 gives `t ≡ a/2 (mod m)`;
- j=e gives `t ≡ (n/a)/2 (mod m)`.

Since chi is odd,

`chi(r/2)-chi(-r/2)=2 chi(2)^(-1)chi(r)`.

The divisor involution `a <-> n/a` makes the two extreme sums equal, proving the formula.

The attached verifier checks 96 exact numerical instances for `l in {3,5,7,11}`, `e=1,2,3` and eight odd test integers.

## 3. Semiprime residue completeness

For `N=pq`, `l∤N`,

`A_(l,e)(N)=(1+chi(p))(1+chi(q))
            =1+chi(N)+chi(p)+chi(q)`.

N gives the product

`chi(p)chi(q)=chi(N)`.

The projector gives the sum

`chi(p)+chi(q)`.

Hence the unordered pair `{chi(p),chi(q)}` is recovered as the two roots of a quadratic. Because chi is faithful, this determines

`{p,q} mod l^e`.

Thus the factor-residue-complete BRC channel exists at every odd prime-power conductor, not only powers of 3.

## 4. l-adic branch lifting

Suppose an ordered factor residue pair `(p0,q0)` is known modulo

`n=l^(e-1)`

and lift it to modulus

`m=ln`.

Write

`p'=p0+i n`, `q'=q0+j n`, `i,j in F_l`.

For `e>=2`, the product condition modulo m reduces to the single nondegenerate linear equation

`q0 i + p0 j = c (mod l)`

because the `ij n^2` term is divisible by `l^e`.

Since p0 and q0 are units, this equation has exactly l ordered solutions. Hence one level contains one base-l branch digit. The exact faithful coefficient selects the unique unordered lift.

The verifier checks the exact l-solution count on random unit states for `l in {3,5,7,11}` and `e=2,3,4`.

A compact additive-trace decoder can in principle be built from the same Ramanujan-fiber mechanism: the changed extreme exponents occupy only the finitely many previous-level fibers, so O(l) local traces suffice to expose the l-way branch. The especially clean 2--4 trace formula previously proved for l=3 uses the RSA Challenge H2 sign-sector separation and remains the narrowest current implementation.

## 5. Base-l Cartier product bridge

Define the l-section operator

`C_(l,r)(sum a_M Q^M)=sum a_(lM+r) Q^M`.

Let

`h=(l-1)/2`.

Because

`(l^e-1)/2 = h(1+l+...+l^(e-1))`,

the base-l expansion consists of e repeated digits h. Therefore the original BRC product satisfies

`C_(l,h)^e F(Q,u)
 = sum_(R>=0) P_(l^e(2R+1))(u) Q^R`.

Combining with the projector yields the direct odd-prime-power twisted Lambert/Eisenstein bridge

`[chi(2)/2] Pi_chi( D C_(l,h)^e F(Q,zeta) )
 = sum_(R>=0) A_(l,e)(2R+1) Q^R`.

The all-ones ternary path is thus the l=3 case of a repeated middle-digit prime-base Cartier path.

## 6. Mixed-radix handoff to Coppersmith

A single 3-adic tower is not mandatory. Let a fixed set of distinct odd primes be

`Lset={l1,...,lk}`

and recover an unordered factor residue pair modulo each `li^Ei`.

For fixed k, choosing one member of each local unordered pair gives at most

`2^k`

CRT residue candidates for p modulo

`M = 2 product_i li^Ei`.

The true p-residue is among them. Once

`M > N^(1/4)`,

run the constructive divisor-in-residue-class/Coppersmith algorithm on each candidate. Since k is fixed, the `2^k` pairing cost is constant.

This avoids the need for a cross-modulus label oracle.

### Equal-depth examples for RSA-270

Let every selected odd prime tower have the same exponent E. The exact smallest E for which

`(2 product(l in Lset) l^E)^4 > RSA270`

is:

| prime-power towers | E | log2 combined modulus | CRT pairings |
|---|---:|---:|---:|
| `{3}` | 141 | 224.480 | 2 |
| `{3,5}` | 58 | 227.600 | 4 |
| `{3,5,7}` | 34 | 229.284 | 8 |
| `{3,5,7,11}` | 22 | 224.821 | 16 |

Thus three parallel towers can reduce the longest sequential prime-power depth from 141 to 34, at the cost of wider local branch observables and eight final CRT candidates.

For the 3-adic tower, the public H2 metadata fixes the base residue modulo 3 and the first unresolved level is e=2. Other prime towers require their e=1 base split as part of the computation.

## 7. This is a depth/width tradeoff, not yet an algorithmic speedup

The atlas does not solve N-only coefficient evaluation.

- larger l gives more residue bits per level but wider cyclotomic/trace structure;
- adding towers decreases serial depth but increases total branch-observable work;
- the finite-state no-go already warns that the full coefficient sequences do not collapse to a fixed finite digit automaton.

The value of the mixed-radix atlas is architectural: any future compact local-trace evaluator can be parallelized across small odd prime bases, and Coppersmith only needs the product of recovered moduli to exceed `N^(1/4)`.

## 8. Preferred next unit

The next useful test is no longer another exact character identity. It is a cost comparison of **adaptive local traces**:

- 3-only: narrow 2--4 traces, up to e=141;
- 3+5 or 3+5+7: shallower towers but wider O(l) local trace vectors.

Derive the minimal separating trace count for an l-way lift as a function of the previous residue state, then optimize total trace work versus parallel depth. This is the correct metric for deciding whether mixed-radix BRC offers any computational advantage over the pure 3-adic route.
