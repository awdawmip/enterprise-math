# BRC N=4 S23 — sharp 2/3 risk of the previous decoder bank on a four-parameter continuum

Date: 2026-11-02. Author mathematical derivation plus executed exact-integer certificate. Independent review and native Result admission pending.

## Proposition (precisely scoped)

Preserve the original four-stop causal observation model, six separately labeled positive-weight sources `AU0,AU1,AV,BU0,BU1,BV`, shared parameters and the original source-mixture matrix. Use the **specified** 10-decoder bank from the previous 3D exact certificate at immutable commit `de0ddc3371ec886be1eb906958cb16e3b4db0978`: its seven fixed kernels `D1,D2,D3,D4,D6,D7,D8` plus the displayed `K1_new,K2,K3` of that source. For a strategy `z`, let

$$
L_D(z)=\max_{1\le i\le6}\operatorname{TV}(P_i(z),Q_i(D)),\quad
r_{\mathcal B}(z)=\min_{D\in\mathcal B} L_D(z),
$$

where `P_i` and `Q_i(D)` are the six original prepared probability rows and decoded rows. Set

$$
F_4(s,t,u,v)=(s,t,u,v,0;1,0,0,0,0,0),\quad (s,t,u,v)\in[0,1]^4.
$$

**Exact fixed-bank theorem:**

$$
\boxed{\sup_{(s,t,u,v)\in[0,1]^4}r_{\mathcal B}(F_4(s,t,u,v))=\frac23.}
$$

The infimum over redesigned free stochastic kernels is a different mathematical problem and is not part of this proposition.

## Sharp lower certificate: a four-parameter interior obstruction

At the legal strategy

$$
W_4=F_4(1/3,0,1,1/2)=(1/3,0,1,1/2,0;1,0,0,0,0,0)
$$

the exact total-variation errors, in the bank's original order `D1,D2,D3,D4,D6,D7,D8,K1_new,K2,K3`, are:

`(1,1,1,1,2/3,1,2/3,1,1,2/3)`.

Every decoder has error at least `2/3`, and three attain equality, proving the fixed-bank lower bound.

The 16 outer corners of the entire four-dimensional unit hypercube have maximum *minimum* decoder risk only `3/5`. Hence checking corners with independently selected decoders would miss this interior obstruction.

## Full real-domain upper certificate

The original preparation source formula is

$$
p(x,b,c)=(x,(1-x)b,(1-x)(1-b)c,(1-x)(1-b)(1-c)).
$$

The six source rows use `x\in\{s,t\}`, `b\in\{u,v,0\}` and original source-specific `c\in\{0,1\}`, with the original shared-source indices and the original fixed `6\times6` mixing matrix. Each prepared row is **separately affine in every one** of `s,t,u,v`. This includes the AV source's dependence on the fourth parameter `v`, rather than replacing it with an independently adjustable observation law.

Partition each axis into six closed intervals `[a/6,(a+1)/6]`, `a=0,...,5`. There are `6^4=1296` four-dimensional cells and `7^4=2401` distinct vertices. For every cell the executed exact-integer checker selects **one common decoder** from the bank whose maximum risk across **all 16 vertices and all six prepared rows** is at most `2/3`. `RUN_EVIDENCE.json` preserves the 1296-digit lexicographic decoder selection (last coordinate fastest); indices 0..9 map to the decoders listed above.

The checker constructs the original six source laws, their mixture and all 10 decoded laws exactly with probability denominator `N=3600`. For a pair of rows, it evaluates `\sum_{j=1}^4 |P_{ij}-Q_{ij}|` as an integer. The threshold is `4800`, giving TV threshold `4800/(2\cdot3600)=2/3`. All `1296\cdot10\cdot16` decoder/corner comparisons are covered (reusing identical vertex risks); every selected decoder passes.

Inside a cell, each prepared row is the **same** tensor-product barycentric convex combination of its 16 vertex rows. For a fixed decoder `D`, total variation is convex in the prepared law:

$$
L_D(F_4(s,t,u,v))
\le\max_{\epsilon\in\{0,1\}^4}L_D(F_4(\text{cell vertex }\epsilon)).
$$

This uses the *same decoder* at all 16 vertices; a different decoder per vertex would not establish the inequality for the bank's minimum. Because the cells cover `[0,1]^4`, the upper bound holds for every real parameter quadruple, with no density or floating-point assumption. Combining with the exact witness proves the proposition.

## An exact one-dimensional sharp ridge section

On `V(v)=F_4(1/3,0,1,v)`, the exact risk values are

- `L_{D8}(V(0))=1/2`, `L_{D8}(V(1/2))=2/3`;
- `L_{K3}(V(1/2))=2/3`, `L_{K3}(V(1))=1/2`.

Affinity in `v` and TV convexity give

$$
r_{\mathcal B}(V(v))\le
\begin{cases}
1/2+v/3,&0\le v\le1/2,\\
5/6-v/3,&1/2\le v\le1.
\end{cases}
$$

Both expressions are strictly below `2/3` away from `v=1/2`, while the witness table gives `r_{\mathcal B}(V(1/2))=2/3`. **Thus the maximum along this particular edge is uniquely attained at `v=1/2`.** No uniqueness is asserted across all four parameters.

## Quantifiers, reuse and next question

The earlier exact `3/5` result on `S18\cup J([0,1])\cup F([0,1]^3)` remains valid when kernels are reoptimized over that earlier domain. Since `F_4(s,t,u,0)=F(s,t,u)`, any joint optimization over the larger `S18\cup J([0,1])\cup F_4([0,1]^4)` has lower bound `3/5`; the *specified* bank from this note covers this union at `2/3`. Therefore the presently proved interval for the reoptimized four-parameter union is

$$
\boxed{3/5\le R_{4,\mathrm{joint}}\le2/3}.
$$

The new witness refutes `3/5` coverage by the previous **specific** ten-decoder construction, not `3/5` attainability after reoptimization.

**Next exact unit:** Adjoin `W_4` to the earlier accepted-as-author-frontier witness set and optimize the three free kernels; either construct a `3/5`-covering bank for the enlarged set or give a finite incompatibility certificate proving a strict increase. Then seek an exact common-decoder cover on the whole F4 cube after reoptimization. Maintain the frozen science pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`, all six sources, and true shared causal parameters.

## Provenance and reproducibility

- Frozen scientific pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
- Previous exact model, bank and three-parameter theorem: `de0ddc3371ec886be1eb906958cb16e3b4db0978`, `research_notes/brc_n4_s23_full_three_parameter_cube_sharp_three_fifths_20261102_research1/VERIFY.js` and `PROOF.md`.
- Run `node VERIFY.js` to reconstruct `RUN_EVIDENCE.json` using exact safe-integer operations, and compare the substantive fields. No external packages or randomization.
- The present four-parameter result is author proof plus exact computation; native session registration and owner/CLAIM were unavailable (`STATIC_READONLY_SCOPE_DENIED`, `CONTROL_QUOTA`). No formal Result, independent reviewer approval or P000 change has been claimed.
