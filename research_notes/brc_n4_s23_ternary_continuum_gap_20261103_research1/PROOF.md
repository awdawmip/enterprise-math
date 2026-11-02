# BRC N=4 / S23: 11D ternary-grid exact 3/5 versus a sharp 2/3 real continuous edge

**Author date:** 2026-11-03. **Frozen science:** `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. **Pinned rational bank:** `57a6db1d81068504cca2b3a6ea809a63555473d6`. **Scientific state:** author-side exact integer computation plus an analytical one-dimensional proof, unreviewed/not admitted.

## Common model and statement

Use the original six separately labeled source preparations, with shared eleven real causal coordinates `z=(z0,...,z10) in [0,1]^11`. For each of the six source indices i, use

```
A=[0,0,0,1,1,1]; B=[2,2,3,2,2,4];
C=[5,6,7,8,9,10]; G=[0,0,1,2,2,3].
M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],
   [0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]].
```

The source row is `R(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c))`, the observed preparations are `P(z)=(M/20) R(z)`; observed decoder rows are `Q_D=(M/20)(D[G_i,*])_i`. Retain seven fixed stochastic decoders D1,D2,D3,D4,D6,D7,D8 and the *specific three* stochastic kernels K1_old,K2_old,K3_repair reconstructed exactly in `VERIFY.js`; no relabeling or source collapse. Set `L_D(z)=max_i TV(P_i(z),Q_{D,i})` and `m(z)=min_{D in this ten-bank} L_D(z)`.

**Theorem A — full ternary classification.** For the complete finite set `T3={0,1/2,1}^11`,

\[
\boxed{\max_{z\in T_3}m(z)=3/5.}
\]

This is a 177,147-element exact-integer exhaustive theorem. Exactly 47,853 ternary vectors have `m(z)=3/5`, and 110,288 have `m(z)=1/2`; the full 35-value histogram is in `RUN_EVIDENCE.json`. The witness `(1,1,0,0,0;0,0,0,0,0,0)` attains 3/5. In the binary subset `{0,1}^11`, the exact error histogram is `1/2:1280, 11/20:32, 3/5:736`.

**Theorem B — sharp real continuum edge.** Let

\[
E(x)=(x,5/6,1,1/2,1/2;\ 1/3,1/2,1,1/2,1/3,1/3),
\qquad x\in[0,1].
\]

Then

\[
\boxed{\max_{0\le x\le1}m(E(x))=2/3,}
\]

with a **unique maximizer** at `x=1/3`. The ten exact decoder risks there, in the order above, are

\[
(1,1,1,2/3,31/36,2/3,2/3,2/3,1,43/60).
\]

For the upper bound, the observed source tuple is affine in `x`; the maximum of six total-variation distances for a single fixed decoder is convex in `x`. The verifier gives `L_D4(E(0))=1/2`, `L_D4(E(1/3))=2/3`, `L_K1(E(1/3))=2/3`, and `L_K1(E(1))=3/5`. Convex interpolation and `m\le L_D` yield

\[
m(E(x))\le
\begin{cases}
1/2+x/2,&0\le x\le1/3,\\
7/10-x/10,&1/3\le x\le1.
\end{cases}
\]

Each bound is strictly below 2/3 away from `x=1/3`; the ten-error witness establishes equality there. Hence both supremum and uniqueness hold over **all real** `x` in the closed interval.

**Corollary C — an eleven-dimensional neighborhood.** For any `z,z'` in the legal parameter cube, use shared independent uniforms for the three causal branch decisions at each source. The source outcome mismatch probability is bounded by `|a-a'|+|b-b'|+|c-c'|`. Stochastic source mixing is total-variation contractive, so for each fixed decoder `|L_D(z)-L_D(z')|<=||z-z'||_1`. Minimum over the same fixed bank preserves this Lipschitz bound. Writing `z*=E(1/3)`,

\[
m(z)\ge2/3-\lVert z-z_*\rVert_1.
\]

Thus **every** `z` in the relative eleven-dimensional open `L^1` neighborhood `||z-z*||_1<1/15` satisfies `m(z)>3/5`. The intersection with `[0,1]^11` has positive 11D measure. This quantifies the continuum adversarial region missed by exact ternary enumeration.

## Exact executable certificate

`VERIFY.js` reconstructs the six-source mixing law and the ten pinned kernels, represents all stochastic decoder rows by integers over 210 and all causal rows by integers over `q^3`. At common denominator `20*210*q^3`, the numerator for each source-decoder total variation is exactly half the sum of four integer absolute differences. Every intermediate value is a safe integer, below `2^53`; there are no floating-point predicates.

The program exhausts all `3^11=177147` ternary assignments exactly once, identifies maxima and histograms, extracts the `2^11` binary subgrid, then computes the full ten-error vector at `E(1/3)` and the four decoder endpoints needed for Theorem B. `RUN_EVIDENCE.json` is the observed execution of this exact source in the tool runtime, and independent Python-stdlib integer recomputation produced the same ternary maximum, multiplicities, binary histogram and real-edge witness values. Reproduce with `node VERIFY.js > recomputed.json`.

## Scientific meaning and next question

For **this specific** ten-decoder bank, a complete 11D ternary policy check has maximum 3/5 while a legal real continuous edge has maximum 2/3. The gap is exactly `1/15`; the bank's overall real 11D supremum is at least 2/3. Earlier pinned results for S18, J, F5, C6 and the 2D T face remain available at their own fixed-bank and joint-optimization scopes.

Next investigate reoptimization of the three free kernels against the new rational witness `E(1/3)` together with the prior full continuous families. A finite repair is a useful candidate test; a uniform real-parameter upper bound needs a valid common-decoder-per-cell or an analytic certificate. The universal-in-kernels lower problem remains separately open. P000, original source provenance, frozen pin, ownership and review authority remain unchanged.
