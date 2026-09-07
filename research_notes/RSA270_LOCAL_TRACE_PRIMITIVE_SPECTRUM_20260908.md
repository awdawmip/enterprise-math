# RSA-270 continuation: a local BRC branch trace has the full primitive-odd character spectrum

Status: `RESEARCH NOTE / EXACT SPECTRAL THEOREM / NOT CANONICAL PROMOTION`  
Researcher-ID: `EM-DIRECT-66DE45`  
Research mode: `TASK_RESEARCH`  
At: `2026-09-08T01:18:00+08:00`  
Parents:
- `research_notes/RSA270_WEIGHTED_LOCAL_TRACE_COMPRESSION_20260908.md`
- `research_notes/RSA270_PRIMITIVE_CHARACTER_GALOIS_PROJECTOR_20260908.md`

No RSA-270 factor is obtained.

## 1. Why four output integers can still hide a high-dimensional arithmetic state

The preceding note compressed one complete l-adic local residue-flow vector into one weighted integer per occupied previous-level fiber, hence at most four integers per lift.

This raises the obvious computational question: does output width <=4 imply a low-dimensional product-side character state?

The answer is no. The local trace is sparse in the **additive residue basis** but maximally broad in the new **multiplicative character basis**.

## 2. Local additive function on the unit group

Let

`m=l^e`, `n=l^(e-1)`, `e>=2`,

with l odd prime, and fix a unit base fiber `b mod n`.

Choose an integer packing base `B>=6`. Define on units `x mod m`

`G_b(x)=sum_(j=0)^(l-1) B^j c_m(x-(b+j n))`,

where `c_m` is the Ramanujan sum for modulus m.

For x in the lift fiber

`x=b+d n`,

we have exactly

`G_b(x)=n [ l B^d - S_B ]`,

where

`S_B=sum_(j=0)^(l-1) B^j`.

Outside the fiber `x≡b mod n`, `G_b(x)=0`.

The normalized W-block is sign-antisymmetric, so the branch functional uses the odd function

`H_b(x)=G_b(x)-G_b(-x)`.

The weighted local trace of a factor packet is a divisor-branch sum of H_b evaluated at the normalized extreme residues.

## 3. Multiplicative Fourier transform

Let `U_m=(Z/mZ)^*`, and for a Dirichlet character chi modulo m define

`hat H_b(chi)=sum_(x in U_m) H_b(x) conj(chi(x))`.

Let

`K=ker(U_m -> U_n)`.

For e>=2, K has order l and consists of the l current lifts of one previous residue.

### 3.1 Characters descending to the previous level vanish

If chi is trivial on K, then it is constant on the fiber bK. Since

`sum_(d=0)^(l-1) [l B^d-S_B]=0`,

the transform of G_b vanishes. Hence

`hat H_b(chi)=0`.

These are exactly the characters whose conductor divides `l^(e-1)`.

### 3.2 Every character nontrivial on K survives the local packing

If the restriction of chi to K is nontrivial, write it along the additive lift coordinate as

`lambda(d)=omega^(c d)`, `c!=0 mod l`,

for a primitive l-th root omega (the factor b merely permutes c).

The constant `-S_B` term disappears under the nontrivial character sum, leaving a scalar multiple of

`sum_(d=0)^(l-1) B^d omega^(-c d)
 = [1-B^l] / [1-B omega^(-c)]`.

For integer B>1 this is never zero. Therefore the transform of G_b is nonzero for **every** character nontrivial on K.

### 3.3 Antisymmetry keeps exactly the odd half

Since

`H_b(x)=G_b(x)-G_b(-x)`,

substitution `y=-x` gives

`hat H_b(chi)
 = [1-conj(chi(-1))] hat G_b(chi)`.

Thus even characters vanish and odd characters survive.

Combining the three steps gives the exact support theorem.

## 4. Theorem: full primitive-odd support

**Theorem (local-trace spectral support).** For `e>=2`, the multiplicative Fourier support of `H_b` is exactly the set of primitive odd Dirichlet characters modulo `l^e`.

Equivalently,

`hat H_b(chi) != 0`

iff

- chi is nontrivial on `ker(U_(l^e)->U_(l^(e-1)))`, i.e. has exact conductor `l^e`;
- `chi(-1)=-1`.

The number of such characters is

`1/2 [phi(l^e)-phi(l^(e-1))]
 = (1/2) l^(e-2) (l-1)^2`.

So one locally packed integer trace has a multiplicative-character expansion involving **every primitive odd character at the new conductor level**, with no zero coefficients.

Examples of the exact support size:

| l | e=2 | e=3 | e=4 |
|---:|---:|---:|---:|
| 3 | 2 | 6 | 18 |
| 5 | 8 | 40 | 200 |
| 7 | 18 | 126 | 882 |
| 11 | 50 | 550 | 6050 |

## 5. Interpretation for BRC

This supplies the missing explanation for an apparent paradox:

- in additive BRC residue coordinates, a lift decision is concentrated in <=4 previous fibers and can be packed into <=4 integers;
- in multiplicative arithmetic coordinates, each such local integer is a dense superposition of the entire primitive odd character layer.

Therefore

`SMALL OUTPUT WIDTH != SMALL CHARACTER STATE`.

The local branch selector is not merely one faithful character coefficient `A_e`; it is an additive localization whose multiplicative Fourier decomposition simultaneously mixes all primitive odd twists of conductor `l^e`.

For l=3,e=2 this specializes to the two primitive odd characters modulo 9, matching the earlier level-9 order-6 character/conjugate description.

## 6. Consequence for product-side algorithms

Any strategy that evaluates a local weighted trace by first decomposing into multiplicative twisted divisor sums faces a character layer of size

`Theta(l^e)`.

This is **not** a computational lower bound against every possible product-side algorithm: a direct additive/Cartier recurrence could in principle avoid explicit Fourier expansion.

It does, however, rule out the intuition that the <=4 output traces can simply be represented by <=4 fixed character coefficients at high precision.

Together with the finite-state no-go, the evidence now points to the same bottleneck from two directions:

- global coefficient view: infinite ternary kernel / no fixed finite state;
- local trace view: full primitive-odd multiplicative spectrum at each new conductor.

The only remaining plausible opening is a target-adaptive **additive** recurrence that transports the localized residue-flow functional through the BRC product without resolving its dense character spectrum.

## 7. Verification

The attached verifier explicitly constructs `H_b` on `U_(l^e)`, computes its full character Fourier transform using a primitive root, and verifies

`support = {primitive odd characters}`

for

`l in {3,5,7,11}`, `e in {2,3}`.

The observed support counts exactly match the formula above.
