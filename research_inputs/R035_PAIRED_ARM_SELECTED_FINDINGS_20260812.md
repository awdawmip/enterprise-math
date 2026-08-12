# R035 Paired-Arm Selected Findings — Frozen Input for R040

Status: `RESEARCH INPUT / PROVENANCE-PRESERVING / NOT CANONICAL`

## Provenance

### Project arm

- Researcher: `EM-R035-6F2A91`
- Task: `RS-R035-POLYGONAL-REFINEMENT-ENDPOINT-DYNAMICS`
- Draft PR: `#523`
- Owner head: `a0aa4a91f8302feeb6e41fa94175e26a3f0a3f71`
- User-return ZIP SHA-256: `86ce91ce0fc0c2015c35ceb23e543c026af2d0e0a4a71cf0310c9095abe29d4f`

### Isolated arm

- Researcher: `ISO-POLY-4C8E17`
- Same mathematical task core, executed under explicit prohibition on Global Knowledge / Enterprise Math history / cross-conversation project memory.
- User-return ZIP SHA-256: `2cda7c60dfb38fb27033138c9d0036a578d5eb5ede0e681b1a85d96bd58cd0fc`
- This isolated return is external research evidence, not retroactively owned by the project arm.

## Shared independently recovered structure

For

\[
P_s(k)=\frac{(s-2)k^2-(s-4)k}{2},
\qquad
F_{s,r}(k)=L_s(rP_s(k)),
\]

both arms independently recovered the discriminant coordinate

\[
z_k=2(s-2)k-(s-4),
\qquad
z_k^2=(s-4)^2+8(s-2)P_s(k),
\]

and exact integer-square-root inversion.

Both arms also recovered:

1. `r=4` as a sharp structural boundary;
2. universal singleton-root interval support for all `s,k0,t` iff `r<=4`;
3. the minimal `r=5,s=3,k0=1` two-step gap witness;
4. exact `r=4` formulas:
   - `s=3`: `{2k,2k+1}`;
   - `s=4`: `{2k}`;
   - `s>=5`: `{2k-1,2k}` for positive `k`;
5. exact-hit arithmetic reducing to a generalized Pell-type discriminant equation.

These shared results are evidence that the main critical geometry is intrinsic to the polygonal endpoint problem rather than merely inherited terminology.

## Project-arm-only frozen results

The project arm additionally established:

- strict ordered lower map with finite jump bounds;
- only adjacent numerical parents can share a child;
- exact finite-support cardinality accounting `|D(S)|=2|S|-H-C`;
- universal distinct-parent no-recoalescence iff `r=1` or `r>=4`;
- a uniform all-`r>=5` two-step interval-failure family `s=r+1,k0=1`;
- self-loop classification and no nontrivial finite positive periodic supports for `r>1`;
- exact interval / separated-parent-forest carrier descriptions in the appropriate regimes;
- eventual lower-jump restriction to neighboring integers around `sqrt(r)`.

Do not attribute the isolated-only results below to the project arm.

## Isolated-arm-only frozen results

The isolated arm additionally established:

### Square refinement affine coding

For `r=q^2`, `q>=2`, and `s!=4`, exact-hit parents are finite in number and there exist an explicit integer offset `c` and finite threshold `K` such that

\[
E_s(q^2P_s(k))=\{qk+c,qk+c+1\}
\qquad (k>=K).
\]

From a singleton started beyond the stable threshold,

\[
S_t=q^t k_0+c(1+q+\cdots+q^{t-1})+
\left\{\sum_{j=0}^{t-1}\epsilon_jq^j:\epsilon_j\in\{0,1\}\right\}.
\]

Hence `|S_t|=2^t` with no recoalescence in the stable regime.

- `q=2`: the digit set fills an interval;
- `q>=3`: the support is an exact sparse base-`q` `{0,1}` digit set, with envelope scale `q^t` and relative density of order `(2/q)^t`.

### Square polygonal family

For `s=4`, `P_4(k)=k^2`:

- square `r=q^2`: deterministic dilation `k -> qk`;
- nonsquare `r`: rounded dilation `k -> {floor(sqrt(r)k), ceil(sqrt(r)k)}`;
- for nonsquare `r>=5`, distinct positive parents have disjoint children and positive singleton support doubles exactly.

### High-index separation

For fixed `r>=5`, the real inverse increment tends to `sqrt(r)>2`; above a finite threshold distinct-parent recoalescence disappears. After a drifting support crosses this threshold, further cardinality loss comes only from exact-hit parents.

## Driver synthesis candidate — NOT YET A THEOREM

The paired return suggests two potentially distinct structural axes:

1. **overlap / branching geometry**, strongly influenced by the position of `sqrt(r)` relative to `2`;
2. **arithmetic coding type**, strongly influenced by whether `sqrt(r)` is integral or irrational and by the exact-hit Pell structure.

Do not assume these axes are independent. R040 is opened specifically to prove, narrow, or kill that decomposition and to identify any coupling terms.

## Anti-convergence boundary

This memo is a shoulder, not a phase diagram mandate. R040 may discover a different organizing coordinate, may show that the proposed two-axis picture is redundant, or may split the dynamics into more than two genuinely independent mechanisms.
