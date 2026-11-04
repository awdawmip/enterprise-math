# CM24 strong horizontal kernel: independent paper review

Date: 2026-11-04  
Reviewer: `EM-C34-D16900`, execution `/root/research_cm_formal_1104`  
Disposition: **PASS for the specified strong completion and unchanged connection.**  
No formal Review vote, Task transition, or parent completion is performed.

## Exact frozen object and independence

Author: `EM-ANALYSIS-3050DA`, execution `/root/research_analysis_1104`. The reviewed files are in `/workspace/agent_artifacts/balanced_resume_20261104/analysis/cm_next/`:

| File | SHA256 |
|---|---|
| `CM24_STRONG_HORIZONTAL_KERNEL_ZERO_AUTHOR.md` | `2d5800c2660eceaf424c5b3cfbcc3e825cb4dc6a9ccb796d0b33ec6fa05ffc5a` |
| `CM24_STRONG_KERNEL_INTERFACE.json` | `bf5f5d3c615b519873975728022d0c688c3224361650d124a0b253fc3d1ebcf9` |
| `CM24_STRONG_KERNEL_PROVENANCE.json` | `c96658794ac3796c4ac807fd5c7263fcbecca2988fd71b2793a921507ae9dfb5` |

I checked the paper and interface against the author's final freeze notification and read both completely, together with provenance. Before that notification I read only old Source background. I did not supply a construction, proof step, edit, or debugging feedback to the author. The planned question, common root and Source snapshot were exposed, so this is independent nonauthor review with shared context, not blind review. My current C34 authorship and separate R004/Hodge reviews do not concern this CM proof. Root contributes zero mathematical votes. Prior reviews of reused CM inputs do not vote on the new conclusion.

## Reused inputs actually checked

The exact weak-normal-form source has SHA256 `5b9e3acafdfeb0c008a02875fc4b53c46589a82505b69053f2b2d69d13f0c788`; the second-round separated-quotient paper has `60548b26b12a98b1d721b6e6f282c6fe3f063689ac7b928de2c3ad7b10bc9a10`. I read both completely and matched these hashes. I also read the first strong-completion/nonclosed-range proof and the specified weak-primitive uniqueness paper. These inputs supply respectively the actual scalar/row frames, bounded first infinity column and strong partial-fraction basis, faithful strong Laurent embedding, and the prior weak gluing result with its explicit annulus limitation.

The fourth-round recurrence paper was read from the preserved branch copy at `a3a9267e4143b3f61e81c8513e7ffff7c623b431`, and its SHA256 matches `09e26d4322403c2f4e79f3050f5fbffb7acce9ec60c403ff24d68e26ad9023a1`. I checked that both accompanying old independent reviews bind exactly those author bytes and the same `a_j=8[z^j]H_12` normalization. I reuse the established all-`k` valuation theorem; this report does not reissue it or turn branch publication into main-branch acceptance. Main Source remains pinned at `39556bf5207aa5ba559a27ec591c1bc1bf43b457`.

The new conclusion is exact strong kernel zero. The separated dimension five is already paid; actual image membership remains a distinct problem. The proof keeps the original primes, unramified DVR, lattice, localization, completion, and good-infinity normalization.

## Independent mathematical check

**1. Scalar identification and frame orientation.** For a column `y'=Dy`, set `v=y_1`. Its first equation gives `y_2=2Pv'−Av`. In the second equation, use `A'=6q` and `A²+B=−4Pq`; the resulting scalar equation is `2(Pv')'−4qv=0`. Thus the finite first coordinate `f_0(z_a(x))` really solves the same `Kcal`, with the same signs. The inherited column is integral and constant one, so both it and its formal inverse lie in `O[[x]]`.

At infinity, `Y(z)=J(z)H(z)` has derivative `−z⁻²D(1/z)Y(z)` precisely because `H'=Dinf H` with the displayed `−J⁻¹J'−z⁻²J⁻¹DJ`. Thus its first-row entries, not transposed or inverse-frame entries, are the scalar solutions `u_1=zH_11`, `u_2=zH_12`. The factor `z` is essential. From `H(0)=I` and `Dinf(0)`, `F(0)=1`, `G(0)=0`, and `G'(0)=1/8` follow. The integral first column comes from the actual prior Frobenius normalization, not from logarithmic growth of the full matrix.

**2. Strong local fields and embeddings are legitimate without analytic annuli.** In `E_x,0`, positive coefficients are bounded, and the negative tail tends to zero. For a fixed coefficient of a product, at either end of the convolution index one factor enters its vanishing negative tail; hence the summands tend to zero and multiplication is defined. The inverse-limit description gives reduction `k((x))`, completeness, and the DVR property. Inverting `p` provides a common valuation lower bound. Termwise differentiation is continuous because every integer multiplier has norm at most one. Its kernel is exactly `K`, by characteristic-zero coefficient comparison, and the `x⁻¹` coefficient of a derivative is zero.

At a finite pole, the image of `P` is `x` times a formal unit over each `O/p^n`. Substitution `r=a+x` is injective on polynomials; clearing the localized denominators and using their Laurent invertibility proves injectivity on the localization even though `O/p^n` has zero divisors. Inverse limits preserve this injection. The infinity embedding is the already proved one with `r=z⁻¹`. These are formal, bounded coefficient embeddings. No assertion that an arbitrary strong element belongs to a Robba ring or converges on a geometric annulus is used.

**3. The finite-pole Wronskian works in those fields.** For two scalar solutions, direct differentiation gives `(P(uv'−u'v))'=u Kcal(v)−v Kcal(u)`. The Wronskian is therefore a constant `C_a∈K`. Division by the bounded unit `u=v_a` is allowed inside `E_x`, and `(v/u)'=C_a/(Pu²)`. The values of `P'(a)` are `−6,6,3,−3`, all nonzero units for the specified primes. Since `u(0)=1`, the right side has residue `C_a/P'(a)`. The left side has zero residue as a derivative. Hence `C_a=0`, and constant-field comparison gives `v=c_a v_a`, with no negative local Laurent powers. This conclusion needs only the bounded scalar solution, not the unbounded logarithmic companion or full gauge.

**4. Local principal-part removal is compatible with the strong topology.** The strong partial-fraction coefficients form a `c_0` family. At a fixed pole `a`, each polynomial basis element expands with integral coefficients; each principal-part basis element based at another pole does too, because all differences are units. Their coefficient-supremum norms are uniformly at most one. Multiplying by a `c_0` family therefore permits a convergent sum in the bounded power-series coefficient space. These terms produce no negative powers. The complete negative part is exactly the principal-part sequence for `a`, so its vanishing forces each such coefficient to be zero. After all four poles, the original element lies in `K<r>` with coefficients tending to zero. No overconvergence estimate is being substituted for the actual `c_0` condition.

**5. Infinity multiplication and the bounded local line are justified.** The identities `P(1/z)=−z⁻⁴Pinf(z)`, `u_1=zF`, and `d/dr=−z²d/dz` give the exact signed formula

`P(u_1 v'_r−u'_{1,r}v)=Pinf F² d(v/u_1)/dz`.

Because `F,F⁻¹∈O[[z]]`, `u_1` and its inverse belong to `E_z`; the quotient `w=v/u_1` is legitimate. Its derivative is `C/(Pinf F²)`, a bounded power series since `Pinf(0)=4` is a unit. Every negative coefficient `w_j` must vanish separately: the derivative coefficient is `j w_j`, and `j` is nonzero in `K`. This coefficient argument does not divide an infinite family while claiming a uniform norm bound; the bound on `w` is inherited independently from its membership in `E_z`.

Only after this negative tail is eliminated does the proof use `U=G/F` in the ordinary formal power-series ring. Its Wronskian is constant with value `4·(1/8)=1/2`, giving `U'=1/(2Pinf F²)` and `w=c+2CU`. If `U` were uniformly bounded, multiplication by integral `F` would make `G` uniformly bounded, contrary to the inherited all-`k` valuations. Hence a bounded `w` forces `C=0`. Adding a constant cannot cancel an unbounded positive-degree sequence. This proves the stated bounded local kernel `K zF`.

There is no illicit multiplication of unbounded `G`, `U`, or the full infinity gauge by a doubly infinite Laurent element. Formal products involving them occur only between power series with coefficientwise finite convolutions. That distinction is sufficient to close the strong-completion gap.

**6. The final intersection is formal coefficient uniqueness.** The global element, after finite-pole removal, maps at infinity to `Σ b_j z⁻ʲ`, supported on nonpositive exponents. The bounded local line consists of `c zF(z)`, supported on strictly positive exponents with nonzero leading coefficient when `c≠0`. Both are genuine elements of the same `E_z`; uniqueness of Laurent coefficients makes their intersection zero. Faithfulness then gives scalar kernel zero. No two analytically convergent rings with an unspecified overlap are invoked.

For a homogeneous row, the second equation gives `h_1=−2P h_2'+A h_2`; the first, equivalently the inherited row/scalar identity, gives `Kcal(h_2)=0`. Hence both components vanish. Scalar and row injectivity are correctly counted as two presentations of one result. Uniqueness of a primitive follows by subtraction, while existence does not.

## Verdict and retained limits

I found no mathematical must-fix in the frozen paper or its interface. The exact strong horizontal kernel is zero under the explicitly inherited integral and valuation inputs, and the intermediate bounded infinity local line is proved as stated. This is a completed deduction on the fixed CM object, not a result for a modified completion or gauge. It does not answer whether `(r,0)` lies in the actual strong image, classify the non-Hausdorff quotient, or evaluate `Y/Z/kappa`.

All new checking was by written reasoning and source/hash inspection. No scientific program, recurrence sample, symbolic solver, old checker, or BRC/Task execution was run. Existing matrix/valuation proofs are reused at their exact versions. Standard Wronskians, residues, and coefficient comparison are applied to a new strong-completion obligation; no new general tool family or global priority claim is approved. Formal research acceptance and remote persistence remain separate from this local PASS.

Researcher-ID: EM-C34-D16900 / TASK_RESEARCH  
EM-Source-Status: Read=Verified snapshot reused and pinned fourth-round branch; Write=⚠ Not written — Source publication pending; local review artifacts preserved. Identity registration remains pending.
