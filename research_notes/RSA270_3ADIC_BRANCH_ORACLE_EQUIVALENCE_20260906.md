# RSA-270 continuation: 3-adic branch-oracle factor reduction and cubic norm geometry

Status: `RESEARCH NOTE / CONDITIONAL REDUCTION + EXACT FIRST-LEVEL GEOMETRY / NOT CANONICAL PROMOTION`  
Researcher-ID: `EM-DIRECT-66DE45`  
Research mode: `TASK_RESEARCH`  
At: `2026-09-06T20:31:34+08:00`  
Parents:
- `research_notes/RSA270_3ADIC_TORSION_PACKET_LADDER_20260906.md`
- `research_notes/RSA270_LEVEL9_CHARACTER_SPLIT_20260906.md`

No RSA-270 factor is obtained.

## 1. Compact branch oracle

The full cyclotomic coefficient `C_e(N)=P_(3^e N)(zeta_(3^e))` is mathematically injective on the H2 local factor-pair lifts, but its canonical field representation has dimension growing with `3^e`. Therefore it is not appropriate to call the full coefficient itself a polylog-size oracle.

Define instead the **branch oracle** `B_e`.

Input:
- N;
- the already recovered unordered H2 residue pair `{p,q} mod M_(e-1)`, with `M_(e-1)=2*3^(e-1)`.

The product congruence modulo `M_e=2*3^e` leaves exactly three ordered Hensel lifts, hence at most three unordered candidates. `B_e` returns the index of the unique candidate consistent with the exact `3^e` torsion packet.

The output contains at most `log2(3)` bits. The previous torsion-packet injectivity theorem proves that the exact coefficient induces a well-defined `B_e`; the open problem is whether `B_e` can be computed from N by a compact N-only formula (for example one or two twisted traces) without first knowing the factors.

## 2. Conditional factorization reduction

**Theorem (branch-oracle reduction).** Under H2, access to `B_e` for successive `e=2,...,E` recovers the unordered factor residues modulo `M_E=2*3^E` by a deterministic three-candidate lift at each stage.

If `M_E > sqrt(N)`, the smaller prime factor p satisfies `0<p<sqrt(N)<M_E`; hence its least nonnegative residue modulo `M_E` is p itself. Among the final two residue representatives, computing `gcd(N,r)` identifies a nontrivial factor.

Thus a compact N-only implementation of the branch oracle at all required levels yields a complete factorization algorithm.

Conversely, knowing the factorization trivially evaluates every branch, so the hierarchy is factorization-equivalent in this conditional oracle sense.

### RSA-270 depth

RSA-270 has 895 bits. The least E satisfying

`2*3^E > sqrt(N)`

is

`E=282`.

Starting at `e=2`, at most 281 successive branch decisions suffice to identify the smaller factor exactly. This is `O(log N)` branch outputs. No claim is made that the currently known full cyclotomic coefficient can be produced or represented in polylogarithmic cost.

## 3. The first branch is also a sigma / four-square valuation bit

For RSA-270 under H2 and `N≡1 mod9`, the two factor-residue possibilities are `{2,5}` or `{8,8}` modulo 9.

Because `sigma(N)=(p+1)(q+1)`:

- branch `{2,5}` has `v_3(p+1)=v_3(q+1)=1`, hence `v_3(sigma(N))=2` and `sigma(N)≡18 (mod27)`;
- branch `{8,8}` has `v_3(p+1),v_3(q+1)>=2`, hence `v_3(sigma(N))>=4` and `sigma(N)≡0 (mod81)`.

Therefore the level-9 trace decision is equivalently the first unknown 3-adic valuation bit of `sigma(N)`.

For odd N, Jacobi's four-square formula gives

`r_4(N)=8 sigma(N)`.

Hence, in this RSA-270 H2 setting:

- `Tr(P_(9N)(zeta_9))=36 <=> r_4(N)≡9 (mod27)`;
- `Tr(P_(9N)(zeta_9))=0  <=> r_4(N)≡0 (mod27)`.

This reconnects the higher torsion branch directly to the Enterprise four-layer representation count. It does not make that coefficient cheap: computing the relevant count residue remains the same hidden arithmetic problem.

## 4. First branch as a cyclic cubic norm/splitting problem

Let

`K=Q(theta)`, `theta=zeta_9+zeta_9^(-1)`.

Then theta satisfies

`f(x)=x^3-3x+1`,

with discriminant 81. The ring `Z[theta]` is the full ring of integers.

### 4.1 Class number one

The Minkowski bound for this totally real cubic field is

`(3!/3^3)*sqrt(81)=2`.

Every ideal class therefore contains an integral ideal of norm <=2. But

`f(x) mod2 = x^3+x+1`

has no root over F2 and is irreducible, so there is no prime ideal of norm 2. Hence every ideal class contains the unit ideal and

`h_K=1`.

### 4.2 Explicit norm form

For

`alpha=a+b theta+c theta^2`,

the norm is

`Norm(alpha)=
 a^3 + 6a^2 c - 3ab^2 + 3abc + 9ac^2 - b^3 + 3bc^2 + c^3`.

For primes r!=3, K/Q is cyclic cubic of conductor 9. A prime splits completely iff `r≡±1 mod9`; otherwise it is inert.

Under H2 and `N≡1 mod9`:

- branch `{8,8}` means both p and q split completely;
- branch `{2,5}` means p and q are inert with inverse nontrivial Frobenius symbols.

Since `h_K=1`, in the split branch there exist algebraic integers of norm ±p and ±q, hence N is represented (up to sign) by the displayed cubic norm form. In the inert branch, an element norm cannot contain an inert rational prime to exponent 1, so ±N is not represented.

Thus the first torsion branch also has the exact geometric form

`Tr=0 <=> exists (a,b,c) in Z^3 with |Norm(a+b theta+c theta^2)|=N`,

while `Tr=36` corresponds to non-representability.

Equivalently, `Tr=0` iff `x^3-3x+1=0 mod N` has a solution; in that branch the polynomial has 3 roots modulo each prime and 9 CRT roots modulo N, while in the inert branch it has none.

This gives a concrete **cubic norm-coordinate / hidden splitting** formulation of the first BRC torsion lift.

## 5. What remains open

Three descriptions now coincide at the first unresolved level:

1. BRC: `Tr P_(9N)(zeta_9)`;
2. arithmetic: a twisted divisor sum / `sigma(N)` 3-adic bit;
3. geometry: splitting / norm representability in the real cyclic cubic field of conductor 9.

None currently supplies a known cheap N-only evaluation.

The highest-value next target is to test whether the norm-coordinate formulation admits a provenance-preserving BRC collapse or finite certificate that decides representability **without** searching a cubic-size coefficient box or effectively factoring N. A successful compact certificate would implement `B_2`; a proof that every such certificate computes the hidden cubic splitting bit would give the correct no-go boundary.
