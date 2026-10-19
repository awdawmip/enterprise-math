# RSA-270 continuation: level-9 BRC branch = CM 3-divisibility = Eisenstein cubic residuosity

Status: `RESEARCH NOTE / EXACT EQUIVALENCE + HARDNESS RECLASSIFICATION / NOT CANONICAL PROMOTION`  
Researcher-ID: `EM-DIRECT-66DE45`  
Research mode: `TASK_RESEARCH`  
At: `2026-09-08T02:18:00+08:00`  
Parents:
- `research_notes/RSA270_LEVEL9_CHARACTER_SPLIT_20260906.md`
- `research_notes/RSA270_CHARACTER_WEIGHTED_BRC_INTERFACE_20260906.md`

No RSA-270 factor is obtained.

## 1. Public RSA Challenge prior and the two level-9 branches

The original RSA Challenge generation record fixes

`p ≡ q ≡ 2 (mod 3)`.

For RSA-270, `N≡1 (mod9)`. Therefore the unordered factor residues modulo 9 have exactly two possibilities:

`B_split = {8,8}`,

`B_nonsplit = {2,5}`.

The earlier BRC/character notes showed that the level-9 torsion packet distinguishes these two branches. This note identifies the branch with two standard arithmetic-geometric decision problems.

## 2. CM elliptic curve formulation

Take

`E : y^2 = x^3 + 1`

and the rational point

`T=(0,1)`.

T has exact order 3.

Let r>3 be a rational prime with `r≡2 (mod3)`.

### 2.1 Exact point count

Because gcd(3,r-1)=1, the cube map `x -> x^3` is a bijection of `F_r`. For every `y in F_r`, the equation

`x^3 = y^2-1`

has exactly one x. Hence there are r affine points plus the point at infinity:

`#E(F_r)=r+1`.

### 2.2 The 3-Sylow is cyclic

Write

`E(F_r) ~= Z/aZ x Z/bZ`, `a|b`.

For an elliptic curve over F_r, `a | r-1`. Also `a | #E(F_r)=r+1`. Thus

`a | gcd(r-1,r+1) | 2`.

So the 3-primary subgroup is cyclic.

Since T has order 3,

`T in 3 E(F_r)`

iff the 3-Sylow has order at least 9, i.e.

`9 | #E(F_r)=r+1`.

Therefore

`T in 3E(F_r) <=> r≡8 (mod9)`.

### 2.3 Composite modulus

The RSA factors are not 2 or 3, so E has good reduction at p and q. Chinese remaindering gives

`E(Z/NZ) ~= E(F_p) x E(F_q)`

for this decision problem. Hence

`T in 3E(Z/NZ)`

iff T is 3-divisible in both local groups.

Under the two H2 branches:

`{p,q}={8,8} mod9 <=> T in 3E(Z/NZ)`,

`{p,q}={2,5} mod9 <=> T notin 3E(Z/NZ)`.

Thus the first hidden ternary BRC digit is exactly a fixed-point 3-divisibility problem on one fixed CM elliptic curve.

## 3. Eisenstein cubic-residuosity formulation

Let

`omega^2+omega+1=0`,

`O=Z[omega]`,

and

`lambda=1-omega`, `Norm(lambda)=3`.

Every rational prime `r≡2 (mod3)` is inert in O, so

`O/(r) ~= F_(r^2)`.

The local cubic residue symbol is

`(lambda/r)_3 = lambda^((r^2-1)/3) mod r in {1,omega,omega^2}`.

### 3.1 Exact supplementary law

In characteristic r,

`lambda^r = 1-omega^r = 1-omega^2 = -omega^2 lambda`

because `r≡2 (mod3)`. Thus

`lambda^(r-1) = -omega^2`.

Since r is odd and `r≡2 (mod3)`, `(r+1)/3` is even. Therefore

`(lambda/r)_3
 = (-omega^2)^((r+1)/3)
 = omega^(2(r+1)/3)`.

Consequently:

- `r≡8 (mod9) -> (lambda/r)_3=1`;
- `r≡5 (mod9) -> (lambda/r)_3=omega`;
- `r≡2 (mod9) -> (lambda/r)_3=omega^2`.

## 4. The two RSA-270 branches have the same cubic Jacobi symbol

For the split branch:

`{8,8} -> {1,1}`.

For the nonsplit branch:

`{2,5} -> {omega^2,omega}`.

In both cases the product is 1. Hence the multiplicative cubic Jacobi symbol satisfies

`(lambda/N)_3 = (lambda/p)_3 (lambda/q)_3 = 1`

on both branches.

So ordinary cubic reciprocity/Jacobi-symbol computation cannot distinguish the branch: exactly as with quadratic residuosity at Jacobi symbol +1, the public multiplicative symbol erases the local split.

The missing datum is the **sum/local pair**, not the product.

## 5. Exact cubic-residuosity decision equivalence

By CRT,

`O/(N) ~= O/(p) x O/(q) ~= F_(p^2) x F_(q^2)`.

An element is a cube modulo N iff it is a cube in both local factors.

For lambda, the local cube condition is exactly `(lambda/r)_3=1`. Therefore:

**Theorem (level-9 cubic residuosity equivalence).**

`{p,q}={8,8} mod9`

iff

`lambda is a cube in (O/(N))^*`.

And

`{p,q}={2,5} mod9`

iff lambda is not a cube modulo N, even though its cubic Jacobi symbol is 1.

Combining with the elliptic result:

`BRC level-9 branch`
` <=> T=(0,1) is 3-divisible on E:y^2=x^3+1 mod N`
` <=> lambda=1-omega is a cubic residue modulo N in Z[omega]`.

## 6. Hardness interpretation

This is much sharper than the earlier vague statement that the route reaches a generic QR/phi(N) wall.

The first unresolved ternary digit is a **higher-residuosity decision problem**: product/Jacobi information is efficiently available, but deciding whether the element lies in the cube subgroup of the composite residue ring requires the hidden local split.

Higher residuosity is a standard cryptographic hardness assumption. As in quadratic residuosity, the decision problem can be strictly weaker than full factorization; this note does not claim an unconditional reduction from branch decision to factoring for one query.

However, the existing BRC branch-oracle theorem plus repeated higher-conductor lifts shows that an oracle supplying the corresponding split at every level through the Coppersmith cutoff would factor RSA-270.

## 7. Cross-check with APR-CL

Standard APR-CL/Jacobi-sum tests also work in cyclotomic residue rings and can prove compositeness or restrict prime-divisor residue classes. A direct finite test of the standard `p=3,k=2` APR-CL global-root condition at auxiliary primes `19,37,73,109,127,163` did **not** distinguish the two level-9 branches: it failed uniformly on the tested composite semiprimes.

This is consistent with the distinction above. APR-CL's ordinary compositeness condition is not the same as deciding whether the fixed Eisenstein element lambda is locally cubic at both hidden factors.

## 8. Updated frontier

The level-9 BRC bit is now attached to three exactly equivalent views:

1. factor residue split `{8,8}` vs `{2,5}` modulo 9;
2. 3-divisibility of a fixed rational torsion point on a fixed CM elliptic curve;
3. cubic residuosity of `1-omega` modulo the RSA modulus in the Eisenstein ring, under public cubic Jacobi symbol 1.

This makes the right classical comparison explicit. Any claimed cheap level-9 BRC evaluator should be checked against known higher-residuosity methods, not merely against generic modular arithmetic or ordinary Jacobi symbols.
