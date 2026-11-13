# CBRC F7 — exact A6 survivor after removing invertibility

**Status:** NONBLIND / EXPOSED_AUTHOR_CONTEXT / SUPPLEMENTARY_AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE. This is a new scoped result for mandatory ablation A6, not a rewrite of the frozen reversible F7 theorem, Result, task or historical reviews.

**Frozen source:** Task `RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION`, Result `RR-AA38973D56330E59D315` (blob `3366edeae347e76b1f6a50bc45a6c6e4cd2dd472`), return blob `69265a0fadfd9fcd0be9354ff74f33e5e825fe84`. Its `proof_obligations.json` presently describes A6 as `CURRENT_PROOF_OPENS_OUTSIDE_SCOPE`. This note supplies an **exact existence witness** for precisely that relaxation. Current global P000 is respected; the F7 two-coordinate free quotient is an auxiliary typed model and is not promoted to a native two-dimensional plane.

## Exact theorem

On `C₂ = Z e ⊕ Z f ⊕ (Z/3)τ`, there are a scalar `q:C₂→R_{≥0}` and an **injective, non-surjective additive endomorphism** `M:C₂²→C₂²` satisfying every F7 scalar/algebraic condition other than reversibility/invertibility: `q(0)=0`, `q(e)=1`, inherited unary `R,J,S` invariance, positivity for all nonzero old projections, exact global two-slot conservation, A0 and balanced elementary outputs of scalar `1/2`, with genuine cross-slot mixing.

Define `φ(t)=1/2` for each nonzero integer `t` and `φ(0)=0`. For `a mod 3`, set

`q(n e+m f+a τ)=φ(n+m)+φ(n-m)`.                             (1)

The scalar is nonnegative, zero at the origin, `q(e)=1`, and independent of torsion. Since `R` changes only the torsion label and `S` reverses it, both preserve `q`. The inherited `J(n,m,a)=(-n,m,-a)` sends `(n+m,n-m)` to `(-(n-m),-(n+m))`; evenness of `φ` gives `J` invariance. If `n≠0`, the two channel integers cannot both vanish, so `q(n,m,a)≥1/2>0` (strict old-projection separation).

Let `C=[[1,1],[1,-1]]`, `D=diag(C,C)`, and define the permutation `Π(u₁,v₁,u₂,v₂)=(u₁,u₂,v₂,v₁)`. Put `A=D Π D`, namely

```text
A = [[ 1,  1,  1,  1],
     [ 1,  1, -1, -1],
     [ 1, -1,  1, -1],
     [-1,  1,  1, -1]].
```

On the free coordinates of `C₂²` define `M` by `A`, and on `(Z/3)²` by the identity. Since `C²=2I`, we have the **exact integer identity**

`D A = 2 Π D`.                                              (2)

The four channels of the two output slots are therefore exactly a permutation of **twice** the four input channels. For every integer `t`, `φ(2t)=φ(t)`. Summing the four scalar contributions in (1) proves

`q(M(x,y)_1)+q(M(x,y)_2)=q(x)+q(y)` for **every** pair `(x,y)` in `C₂²`.

The first old elementary input `(e,0)` has free coordinates `(1,0,0,0)`; (2) or direct multiplication gives `M(e,0)=(e+f,e-f)` with zero torsion. Both output old projections are nonzero, and `q(e±f)=φ(2)+φ(0)=1/2`, proving A0 and balance. Each of the four `2×2` slot blocks of `A` is nonzero and rank one. Thus `M` couples both old slots and is not a product/swap of independent unary slot maps.

Finally `det A=16`, so the free map is injective; the torsion identity makes `M` injective. Yet every image `Aw` has all channel coordinates `DAw` even, whereas `D(1,0,0,0)^T=(1,1,0,0)^T`. Hence `(e,0)` is **not** in the image: `M` is not surjective and not an automorphism. This isolates the one assumption removed in A6.

## Structural meaning and limits

`det C=-2` and `C J C⁻¹=[[0,-1],[-1,0]]`. The original F7 all-rank-one-block proof excludes this off-diagonal `J` channel swap only because `det A=±1` forces the extracted channel basis to be unimodular. Here the channel basis is index two and the combined integral endomorphism has determinant sixteen. The witness therefore explains exactly how the A6 relaxation escapes that proof.

This is an exact, globally conserved **non-reversible** survivor. It does not alter the frozen F7 no-go under `GL₄(Z)`, establish a minimum determinant, classify all endomorphisms, validate other ablations, or grant Foundation/P000/native review authority. Author-side shared-context work must remain separate from independent Driver review. A future DA-authorized Driver should read the exact Result and all current review records, inspect this addendum and decide whether a scoped A6 clarification is useful; keep the original authors, source pins and reviews unchanged.

## Reproduction

`CHECK.py` evaluates the integer determinant, equality (2), 6,561 free input pairs, unary `R,J,S` invariance at 507 marked inputs, the elementary balance/A0, and torsion-label invariance. The exact global proof is (1)–(2); the finite checks are regressions. `CHECK_RESULT.json` is the recorded local output. All claims are over the explicitly stated finitely generated abelian carrier, not the physical world.
