# RSA-270 continuation: level-9 branch as a fixed cyclic cubic root problem; global Artin products are provably blind

Status: `RESEARCH NOTE / EXACT CYCLIC-CUBIC REFORMULATION + MULTIPLICATIVE-SYMBOL NO-GO / NOT CANONICAL PROMOTION`  
Researcher-ID: `EM-DIRECT-66DE45`  
Research mode: `TASK_RESEARCH`  
At: `2026-09-08T02:45:00+08:00`  
Parents:
- `research_notes/RSA270_LEVEL9_CM_CUBIC_RESIDUOSITY_EQUIVALENCE_20260908.md`
- PCF6 restricted fixed-probe boundary as independently audited in PR #1361/#1377.

No RSA-270 factor is obtained.

## 1. The fixed cyclic cubic polynomial

Let

`f(X)=X^3-3X+1`.

Its discriminant is

`disc(f)=81=9^2`.

If `zeta=zeta_9` and `a=zeta+zeta^(-1)=2 cos(2pi/9)`, then

`a^3-3a = zeta^3+zeta^(-3) = -1`,

so f(a)=0. Hence

`K=Q(a)=Q(zeta_9)^+`

is the real cyclic cubic subfield of the ninth cyclotomic field and

`Gal(K/Q) ~= (Z/9Z)^*/{+-1} ~= C3`.

## 2. Prime splitting / root criterion

For every prime r!=3, Frobenius in K is the class of r modulo 9 up to sign. Therefore

`f has a root mod r`

iff r has trivial Frobenius

iff

`r ≡ +-1 (mod9)`.

Because K/Q is cyclic of prime degree 3, a root is equivalent to complete splitting: in the nontrivial Frobenius classes f is irreducible cubic.

Under the documented RSA Challenge condition `r≡2 (mod3)`, the only possible residues are 2,5,8 modulo 9. Hence:

- `r≡8 mod9`: f splits into three linear factors;
- `r≡2 or 5 mod9`: f is irreducible and has no root.

The attached finite verifier checks this root-count law on primes below a regression bound.

## 3. RSA-270 branch = solvability of one fixed cubic congruence

For RSA-270, H2 and `N≡1 mod9` leave exactly

`B0={8,8}`

or

`B1={2,5}`.

By CRT:

- on B0, f has 3 roots modulo p and 3 modulo q, giving 9 roots modulo N;
- on B1, f has no root modulo either prime, hence no root modulo N.

Therefore:

**Theorem.**

`B0 <=> exists x mod N : x^3-3x+1 ≡ 0 (mod N)`.

This is the same decision as the fixed CM 3-divisibility and Eisenstein cubic-residuosity formulations from the parent note, expressed in a rational degree-3 algebra.

## 4. Étale algebra structure

Define

`A_N=(Z/NZ)[X]/(f)`.

Then:

- B0: `A_N ~= F_p^3 x F_q^3`;
- B1: `A_N ~= F_(p^3) x F_(q^3)`.

So the hidden ternary branch asks whether the fixed rank-3 étale algebra has split or inert fibers over both hidden CRT components.

Equivalently, B0 admits a linear-factor/evaluation quotient over each hidden component; B1 does not.

This is a natural PCF6-style selector/idempotent problem in a fixed low-rank algebra, but finding the refinement without exposing the hidden CRT decomposition is exactly the missing operation.

## 5. Global Artin product is identical on the two branches

Let `sigma` generate `Gal(K/Q)=C3`.

The local Frobenius pairs are:

- B0: `(1,1)`;
- B1: `(sigma,sigma^(-1))` (up to ordering).

Their product is the identity in both cases.

This is not accidental: the global Artin symbol of the rational composite ideal `(N)=(p)(q)` in the abelian extension K is multiplicative and equals the product of local Artin symbols. Since `N≡1 mod9`, that product is trivial.

Therefore every one-dimensional character rho of the cyclic Galois group satisfies

`rho(Frob_p) rho(Frob_q)=rho(Frob_N)=1`

on both branches.

**Corollary (multiplicative reciprocity blindness).** No N-only observable that is only a multiplicative Abelian Artin/reciprocity symbol for this cyclic cubic extension can distinguish B0 from B1.

The missing quantity is nonmultiplicative local-split data such as

`rho(Frob_p)+rho(Frob_q)`:

- B0 gives 2;
- B1 gives `omega+omega^2=-1` for a faithful character.

This is exactly the sum supplied by the BRC twisted divisor coefficient

`A_chi(N)=1+chi(N)+chi(p)+chi(q)`.

Thus the character-weighted BRC interface is not duplicating a standard global cubic Jacobi/Artin symbol; it asks for the hidden local sum erased by multiplicativity.

## 6. Relation to efficient Eisenstein cubic-symbol algorithms

Damgard--Frandsen's efficient Eisenstein-integer cubic-residuosity algorithm computes the cubic residuosity **symbol**

`[alpha/beta]_3`,

and for a composite denominator `beta=prod pi_i^(m_i)` its definition is the product of local symbols.

It is explicitly described as the Eisenstein analogue of a Jacobi-symbol algorithm.

Therefore, for the fixed `lambda=1-omega` used in the CM formulation, their efficient algorithm returns the already-public product symbol

`[lambda/N]_3=1`

on both RSA-270 branches. It does not decide whether lambda is a cube in both hidden CRT factors simultaneously.

This resolves the apparent conflict between an `O(n^2)` cubic-symbol algorithm and the hidden branch problem.

## 7. PCF6 cross-route boundary

The PCF6 prior-art audit freezes the following principle for a finite family of fixed H-independent determinant probes: each such probe reduces to a fixed integer resultant; a nonzero resultant has only finite prime support, while zero resultant is uniformly singular/non-separating. No universal hidden semiprime split follows from such a finite fixed family.

The fixed companion algebra of f is another low-rank representation of the same local-split question. Fixed trace/determinant/resultant identities of the companion matrix are functions of the fixed polynomial coefficients and cannot manufacture the missing local Artin sum.

An H=N-dependent nonlinear probe could in principle do more; this note does not rule that out.

## 8. Updated frontier

The first ternary BRC digit now has four equivalent exact presentations:

1. factor residues `{8,8}` versus `{2,5}` modulo 9;
2. 3-divisibility of `T=(0,1)` on `y^2=x^3+1` modulo N;
3. true cube-membership of `1-omega` in the Eisenstein CRT ring under cubic Jacobi symbol 1;
4. solvability of the fixed cyclic cubic congruence `x^3-3x+1=0 mod N`.

All standard multiplicative Abelian reciprocity symbols are provably blind because they see only the product of local Frobenius elements.

A successful N-only branch evaluator must compute a local-split **sum/refinement**, or otherwise break the hidden CRT symmetry; merely changing among these four coordinates cannot do it.
