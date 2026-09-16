# RSA-270 continuation: exact Galois-equivariant linear-state lower bound for local BRC traces

Status: `RESEARCH NOTE / EXACT SCOPED LOWER BOUND / NOT CANONICAL PROMOTION`  
Researcher-ID: `EM-DIRECT-66DE45`  
Research mode: `TASK_RESEARCH`  
At: `2026-09-08T01:42:00+08:00`  
Parents:
- `research_notes/RSA270_LOCAL_TRACE_PRIMITIVE_SPECTRUM_20260908.md`
- `research_notes/RSA270_WEIGHTED_LOCAL_TRACE_COMPRESSION_20260908.md`

Tool reuse: `T7_FINITE_SYMMETRY_EQUIVARIANCE -> REUSE_APPLIED`; `T8_RELATION_OBSERVABLE_SPECTRUM -> REUSE_APPLIED`.

No RSA-270 factor is obtained.

## 1. Setup

Let

`m=l^e`, `e>=2`,

with l odd prime, and let

`G=U_m=(Z/mZ)^*`.

Let `H_b:G->C` be the odd packed local branch functional from the parent note. Its multiplicative Fourier support was proved exactly to be

`S = {primitive odd Dirichlet characters modulo l^e}`.

Hence

`|S| = D_(l,e) = (1/2) l^(e-2)(l-1)^2`.

For `g in G`, let left translation act by

`(T_g H_b)(x)=H_b(g^(-1)x)`.

## 2. Orbit-span dimension theorem

**Theorem.**

`dim_C span{T_g H_b : g in G} = D_(l,e)`.

### Proof

The Fourier characters diagonalize the regular representation of the finite abelian group G. If

`H_b = sum_(chi in S) hhat(chi) chi`,

then

`T_g H_b = sum_(chi in S) hhat(chi) chi(g^(-1)) chi`.

Every coefficient `hhat(chi)` on S is nonzero by the primitive-spectrum theorem. The character evaluation vectors

`g -> chi(g^(-1))`

are mutually orthogonal as chi ranges over distinct characters. Therefore the translates span one independent one-dimensional eigenspace for every chi in S and no others. The dimension is exactly `|S|=D_(l,e)`. QED.

## 3. Equivalent translation-matrix rank theorem

Define the full translated-query matrix

`M[g,x] = H_b(g^(-1)x)`, `g,x in G`.

Then

`rank_C(M) = D_(l,e)`.

This is simply the previous theorem written as row rank, but it gives a representation-independent factorization lower bound.

Suppose a linear state model of dimension d represents every translated local query in the form

`M[g,x] = <u_g, v_x>`

with `u_g,v_x in C^d`, or more generally factors

`M=A B`

through a d-dimensional state. Then

`d >= rank(M) = D_(l,e)`.

This statement does **not** require choosing the Fourier basis and does not depend on the implementation of the state.

## 4. Galois-equivariant consequence

Any exact linear state space that is closed under the full unit/Galois action and contains one local branch functional `H_b` must contain its whole orbit. Therefore its dimension is at least

`D_(l,e)=(1/2)l^(e-2)(l-1)^2`.

Examples:

- l=3: `D=2*3^(e-2)`;
- l=5: `D=8*5^(e-2)`;
- l=7: `D=18*7^(e-2)`.

At the pure ternary Coppersmith cutoff `e=141`, the exact lower bound is

`D_(3,141)=2*3^139`.

Thus no full-Galois-equivariant linearization of the local weighted trace can have dimension polynomial in e.

This is stronger than the earlier observation that the character expansion is dense: it is a **basis-independent matrix-rank obstruction**.

## 5. Scope boundary

This is deliberately not advertised as a lower bound for all possible factorization algorithms.

The RSA lifting workflow does not ask for every translated query simultaneously. At level e it already knows the previous unordered residue pair and asks only the one-to-four local fibers selected by that state.

Therefore the theorem rules out:

- fixed/poly(e)-dimensional **Galois-equivariant linear** states carrying the whole query family;
- any linear factorization of the full translated-query matrix through fewer than D dimensions.

It does not rule out:

- a nonlinear state;
- a state that explicitly breaks Galois symmetry using the known previous residue fiber;
- a target-N adaptive recurrence that computes only the currently requested `W_b`;
- a state whose dimension depends on the specific branch history rather than supporting all translates.

That asymmetric target-adaptive loophole is now the only mathematically meaningful escape from the symmetry lower bound.

## 6. Finite verification

The attached verifier orders G by powers of a primitive root, constructs the exact translated-query matrix, and checks

`rank(M)=D_(l,e)`

for small prime-power groups. The theorem itself is the Fourier/orbit proof above; finite ranks are regression evidence only.

## 7. Next question

Break the symmetry intentionally.

Condition on a known previous residue pair modulo `l^(e-1)` and restrict to its l product-compatible lifts. Determine the minimal exact state/query rank on **that conditional fiber only**.

If the conditional rank is O(1), this explains why the four-trace decoder can remain narrow even though the global orbit rank is exponential. The remaining issue would then be whether those O(1) conditional observables can be evaluated from N without reconstructing the global character state.
