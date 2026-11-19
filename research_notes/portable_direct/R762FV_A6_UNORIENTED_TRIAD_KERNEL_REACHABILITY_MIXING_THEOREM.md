# R762FV — Uniform unoriented native-axis triad BRC kernel: sharp A6 reachability and exact 3-step mixing bound

Date: 2026-11-19. Scientific status: AUTHOR_PROVED / EXACT_EXHAUSTIVE_VALIDATION_PASS / NOT_REVIEWED.
Parent task: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`.
Frozen scientific input: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\` and its P000 signed-six-axis / Cell-torsor / triadic-balance companions; taskbook \`@857280d1012943290d141d1317179c40ec3cbdf8:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md\`.
Antecedents: R762FT–FU in draft PR #2794 @ \`5e90f1f21f2f65297e0aebe656d31ce6b7506c2e\`.

## Research question and explicitly typed model

R762FU proves the unique normalized \`S6\`-equivariant, two-branch positive BRC kernel for a **fixed unordered triad** \`T={a,b,c}\`: one branch for each of its inverse directed three-cycles, weight \`1/2\` each. Extend it by choosing \`T\` uniformly among all \`binom(6,3)=20\` native-axis triples, independently at each **formal BRC depth step**. This gives the convolution kernel

\[
\mathcal K=\frac1{40}\sum_{g\in\mathcal C_3}[g],
\]

where \(\mathcal C_3\subset S_6\) is the full conjugacy class of 40 directed 3-cycles. Each branch retains its chosen triple, orientation, step order, signs, named source labels and positive rational mass \`40^{-h}\` at depth \(h\). Composing label permutations supplies *only* the declared coarse rotation observer \(R_h=g_h\cdots g_1\), not an erasure of its BRC source word or a native force-cancellation law.

This is an \`S6\`-equivariant candidate on the known axis-permutation skeleton. P000 specifies six signed native axes, \`PERP_E\`, native angle 120°, primitive triadic balance and a six-dimensional Cell torsor; it does not by itself license a physical \`TRIADIC_CLOSURE_E\` rotation event. All statements below are therefore about the explicit combinatorial candidate, not physical time or Source-native event authorization.

## Theorem 1 — exact group reachability and minimum branch depth

Let \(A_6\) be the 360 even permutations of the six named native axes. For every \(h\ge0\), a depth-\(h\) history yields an even permutation. Conversely, **every** element of \(A_6\) occurs at depth \(h=3\), whereas after two steps only 270 elements occur; the 90 missing elements have cycle type \((4,2)\).

More precisely, for any even permutation \(\pi\in A_6\), let \(o(\pi)\) denote the number of odd-length cycles, counting fixed points. Its minimal number of 3-cycle factors is

\[
\boxed{\ell_3(\pi)=\frac{6-o(\pi)}2.}
\]

This classification is complete:

| Cycle type | Elements | Shortest 3-cycle word |
|---|---:|---:|
| \(1^6\) | 1 | 0 |
| \(3\,1^3\) | 40 | 1 |
| \(2^2\,1^2\) | 45 | 2 |
| \(3^2\) | 40 | 2 |
| \(5\,1\) | 144 | 2 |
| \(4\,2\) | 90 | 3 |

*Argument.* Every 3-cycle is even, so an odd permutation is never reached. Multiplying by one 3-cycle changes the count of odd-length cycles by at most 2, hence any 3-cycle expression for \(\pi\) has length at least \((6-o(\pi))/2\). This lower bound is attained: each odd cycle of length \(2a+1\) decomposes into \(a\) 3-cycles; after pairing the even-length cycles (there are an even number in an even permutation), each length-\(2a\) cycle can be shortened to one transposition using \(a-1\) 3-cycles, and the two remaining disjoint transpositions factor into two 3-cycles. Each paired even-cycle contribution is therefore \(a+b\) factors. The sum is exactly \((6-o(\pi))/2\). The 6-axis table follows by classifying even cycle types. At depth 3, classes whose shortest length is less than 3 can also be represented with three factors: a 3-cycle \(\gamma\) can be replaced by \(\gamma^{-1}\gamma^{-1}\), and the identity by \(\gamma^3\). Thus all 360 are hit by exactly three branches. \(\square\)

## Theorem 2 — exact depth-three class coefficients

Let \(N_3(\pi)\) be the number of ordered triples of allowed directed 3-cycles whose product is \(\pi\). It depends only on the full \(S_6\) conjugacy cycle type, and the exact integer coefficients are:

| Cycle type | Elements | \(N_3(\pi)\) per element | Total histories |
|---|---:|---:|---:|
| \(1^6\) | 1 | 400 | 400 |
| \(3\,1^3\) | 40 | 306 | 12,240 |
| \(2^2\,1^2\) | 45 | 224 | 10,080 |
| \(3^2\) | 40 | 114 | 4,560 |
| \(5\,1\) | 144 | 175 | 25,200 |
| \(4\,2\) | 90 | 128 | 11,520 |
| **Total** | **360** | | **64,000 = 40³** |

The coefficients are finite exact integer identities, certified by the attached exhaustive checker: it generates all \(6!=720\) permutations, all \(\binom63\times2=40\) oriented three-cycles, directly enumerates all 64,000 ordered triples, independently recovers the same numbers by four successive integer convolution rounds, checks uniformity on each conjugacy class, and tests all 28,800 \(S_6\)-conjugation images. No floating-point arithmetic or sampled subgroup is used. A second independent direct enumeration in Python agreed with the same table. This finite certificate proves the exact 6-axis coefficients; no claim about other dimensions or unverified primitive actions is inferred.

## Theorem 3 — exact three-step positive minorization and geometric mixing

Let \(P\) be the Markov kernel associated with \(\mathcal K\) on \(A_6\), and \(U\) the uniform probability measure on its 360 elements. Since each 3-cycle branch is invertible, the walk is a group convolution and \(U\) is stationary. The exact table shows that every element has at least 114 third-step preimages, so for all \(x,y\in A_6\),

\[
P^3(x,y)=\frac{N_3(yx^{-1})}{40^3}\ge\frac{114}{64000}=\frac{57}{32000}
=\frac{513}{800}\,U(y).
\]

Hence, for every starting even rotation \(x\) and all integers \(k\ge0\),

\[
\boxed{\lVert \delta_x P^{3k}-U\rVert_{\rm TV}\le(287/800)^k.}
\]

*Proof.* Decompose \(P^3=(513/800)\,U+(287/800)\,Q\), with \(Q\) another stochastic kernel, which is possible entrywise by the displayed lower bound. Translation invariance and stationarity of \(U\) imply contraction of total variation toward \(U\) by at most \(287/800\) per three steps. Iteration proves the result. \(\square\)

At precisely three steps the total variation is **exactly**
\[
\boxed{\lVert\delta_x P^3-U\rVert_{\rm TV}=209/1800.}
\]
The exact integer check computes \(\frac12\sum_{\pi\in A_6}|N_3(\pi)/64000-1/360|\). This gives a sharper measurement than the general minorization bound at \(k=1\).

## Source-preserving interpretation and exposed residual

The \(40^h\) formal BRC branch words of length \(h\) remain named and ordered. The group product has at most 360 values, and after three steps exactly 360, giving a two-stage representation: the coarse endpoint observer \(A_6\) and the still-retained path/source fiber. At \(h=3\), the exact fibers have sizes 114–400 depending on endpoint class. A future operation asking for stepwise orientation, original triad or source order can distinguish histories within one fiber. Consequently \(\mathcal K\)'s endpoint-mixing theorem does **not** authorize discarding provenance, claiming a physical steady state or treating 360 as the whole decorated packet state. The exact observer/horizon distinction meets the P000 joint-relation and BRC preservation requirements.

Parity is a sharp group-level obstruction: any number of these directed three-cycle branches remains in \(A_6\) and never reaches any of the 360 odd axis permutations. If a later native operator needs an odd permutation, it requires an independently licensed additional primitive/macro operation or a richer state transition; adding more of the present three-cycle branches cannot suffice.

## Validation, reproducibility, next decisive questions

Files: \`R762FV_VERIFY.mjs\` (standalone Node.js 18+ integer checker) and \`R762FV_EVIDENCE.json\` (machine-readable full coefficients and checks). Author-side calculation covers all 720 permutations, 40 three-cycle generators, all 64,000 length-three words, all relevant 360 rotation states and 28,800 conjugation checks; all PASS. Mathematical and physical review: \`NOT_REVIEWED\`.

Next, use the **frozen native** Cell/Link/Port incidence and legal-update predicate to decide whether both inverse 3-cycles on all 20 axis triples can actually fire, and whether the same Source-native transition transports signed BRC provenance. In a restricted set of admissible triads, recompute the generated subgroup/support and look for a concrete obstruction or a typed source-to-candidate morphism. Separately preserve the q9 full-vector normalized period open problem; this model does not solve it.