# R692｜E* 原生X6-BRC：单比特回归观察的三步识别与最小来源记忆

Date: 2026-11-10. Status: AUTHOR-PROVED / EXACT_FINITE_VERIFIED / UNREVIEWED / NOT_ADMITTED.
Role: independent author-side calculation; no official task CLAIM or Result implied.
Mother task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`.
Scientific freeze (unchanged): task Source `a72226e2430ffa4786321ac86e7f0c599d5f0389`, R687 E* `028d5612f9562bc22ac7593f03426fc32b1a9259`, R690 `7b1633d3e6ba84f76a3e323aa272f851bf1e0f90`, R691/R691b `df5c9edbb18b123a828e3e6ead2a1a0f606511a5`.

## 1. Question and observer

R691b established four source-memory states when the **full** next-step S3 group distribution is queried, under the following declared future protocol: every successive four-step macro repeats the preceding source direction `sigma=(s_i,s_j)∈{--,-+,+-,++}`; independently choose any of the 15 pairs `0<=i<j<=5` with equal probability. Each macro is the ordered native X6 path `s_i e_i, s_j e_j, -s_i e_i, -s_j e_j` and returns to its starting Cell and root phase.

Ask a strictly smaller question: the observer sees only the **single Boolean event** that the complete S3 frame after `k` future macros equals its frame before those macros. Its exact probability is `r_k(a,sigma)`; the observer may query any finite `k>=1`. Root phase `a∈{0,1,2}` is fixed, with `b∈{0,1}` yielding the same square-macro kernel. The input frame may be any fixed `p∈S3`, because a convolution return probability is independent of the initial frame.

A finite-horizon observation signature is `(r_1,...,r_h)`. Two hidden source labels are future-equivalent exactly when their signatures agree for **every** `k>=1`.

## 2. General finite-group return-trace theorem

Let `G` be any finite group, `m=|G|`, and let `mu` be a probability measure on `G` with rational weights. Let `P_mu` be its left regular convolution matrix on `Q[G]`; let `r_k(mu)=mu^{*k}(e)`, with `r_0=1`.

**Lemma (finite-horizon completeness).** For any two such measures `mu,nu`:

```text
  r_k(mu)=r_k(nu) for every k>=1
  if and only if
  r_k(mu)=r_k(nu) for k=1,...,m.
```

**Proof.** Each diagonal entry of `P_mu^k` is `mu^{*k}(e)`, since left convolution returns any group element to itself exactly when the net product is the identity. Thus `tr(P_mu^k)=m r_k(mu)`. The first `m` power traces determine the coefficients of the monic degree-`m` characteristic polynomial by Newton identities in characteristic zero. Therefore equality of the first `m` return probabilities implies equality of the two characteristic polynomials. Cayley–Hamilton then supplies the **same** linear recurrence for all later traces `tr(P^k)` with the same initial values. All later return probabilities coincide. The other direction is immediate. QED.

Consequently the minimal deterministic hidden-state quotient needed to answer **all exact return-probability queries** is computable by at most `m` such probabilities: one state per distinct signature (with any already known phase/frame held fixed). This is an observer-dependent quotient, not a claim that probability distributions can be inferred with certainty from one random sample.

For the present `G=S3`, **six** return-probability horizons are always sufficient to determine this future equivalence relation.

## 3. Sharp E* result: phase a=0 needs three steps

The R691 exact native kernel counts, reproduced independently from the source E* frame-update rule, yield the following rational probabilities. All cells use denominator appropriate to each `k` and retain exact precision.

| source direction sigma | r_1 | r_2 | r_3 |
|---|---:|---:|---:|
| -- | 2/5 | 13/25 | 62/125 |
| -+ | 2/5 | 8/25 | 33/125 |
| +- | 2/5 | 1/5 | 22/125 |
| ++ | 2/5 | 8/25 | 41/125 |

**Theorem R692-A.** Under the stated direction-repeat E* macro protocol at any root phase `(a,b)` with `a=0`, the smallest time horizon `h` whose complete set of return-probability queries `r_1,...,r_h` distinguishes all four direction sources is **exactly `h=3`**. Indeed the four **single** third-horizon probabilities are already pairwise distinct; their smallest pairwise gap is `8/125`.

**Proof.** At `k=1` every direction has return mass `6/15=2/5`, so no distinction is possible. At `k=2` the -+ and ++ sources coincide at `72/225=8/25`, so two steps cannot separate all four. At `k=3` the exact integer return counts (over `15^3=3375` source paths) are `1674,891,594,1107` in direction order `--,-+,+-,++`. Dividing by `3375` gives the distinct fractions in the table; the closest pair differs by `(1107-891)/3375=8/125`. These counts are products in the six-element group `S3` and are checked independently by native four-step path enumeration. QED.

For `a=1`, the four first-horizon return probabilities are `(2/5,3/5,4/5,1)`; for `a=2`, they are `(1,4/5,3/5,2/5)`. Therefore their sharp distinguishing horizon is `h=1`.

**Corollary R692-B (weak observer, same exact predictive-memory capacity).** At each fixed root phase, all four direction labels are pairwise nonequivalent even for the much smaller family of Boolean return-observer probability queries over arbitrary future macro counts. With the current frame and phase already known, a deterministic exact predictive state must retain four source equivalence classes: a two-bit fixed-width code is sufficient and necessary. At phase `a=0` this necessity first becomes visible at the third return query, not at one or two.

## 4. Reproduction and exact coverage

The source file `R692_ESTAR_RETURN_OBSERVER_EXACT.js` is the actually executed self-contained ECMAScript enumerator. It begins with the six E* root triples:

```text
(a,b): (0,0)->012, (1,0)->013, (2,0)->014,
       (0,1)->023, (1,1)->123, (2,1)->013.
```

For each root `a=0,1,2; b=0,1`, each of the four direction signs, and each of the 15 unordered axis pairs, it follows four signed native coordinate moves, replaces the leaving triad label in its **existing frame slot** with the entering label, verifies native Cell return, and converts the resulting frame to a root-relative S3 permutation.

The code checks all **360** labeled native four-step paths against the 12 group-count kernels of R691; then performs exact integer group convolutions for `k=0,...,6`, checking `sum_g mass(g)=15^k` at every step. It asserts all three phase-specific minimum horizons, the exact a=0 `k=2` counts `117,72,45,72` and `k=3` counts `1674,891,594,1107`. The executed result is `ALL_EXACT_ASSERTIONS_PASS` and the full case-by-case integer evidence is in `R692_ESTAR_RETURN_OBSERVER_RESULTS.json`. The arithmetic stays within exact IEEE-754 safe-integer range: `15^6=11390625<2^53`. An independently implemented Python standard-library `Fraction`/integer path enumerator also reproduced these numerical claims in the local study.

The general lemma is an algebraic proof, not a conclusion from six tested powers. The E* result is a finite exact classification of the stated macro model, with all source paths enumerated and all asserted tests passing. No independent project mathematical review has been performed.

## 5. Source relation, research use, and next unit

- R691 shows why full-group one-step observation needs direction-source memory. R692 shows that the **far weaker single-bit return event** may hide the sources at one step yet require the same four predictive memory classes after several steps.
- The `tr(P^k)` method yields a general finite algorithm to classify future-observable source histories for any fixed finite-group BRC convolution kernel, and avoids using only one-step lumpability as a test for all-time sufficiency.
- The current 360-path E* candidate uses all 15 axis pairs, positive equal BRC weights and the explicit repeated-direction rule. Its frozen E* source is an author-level research construction. Actual X6 Link/Port permission, V29 PASS/TRANSFER and V39 event-history rules must be loaded before extending the conclusion to physical Cell/Port dynamics.
- Next precise unit: extract the actual current Link/Port/V29 transition-state and allowed-action semantics from pinned scientific files; replace the all-pairs macro kernel with the native permitted kernels and compute whether two equal (Cell,phase,frame) states with different source/port histories have different `r_k` or allowed-action sets. Preserve signed/source provenance and compute the smallest exact observer-future quotient, including a counterexample if a proposed quotient collapses distinguishable states.

## Mathematical background/prior-art classification

The finite-group return-probability and convolution setting is classical; the trace/Newton/Cayley–Hamilton lemma is a standard algebraic consequence. Relevant public prior art includes Vyshnevetskiy and Zhmud, *Random walks on finite groups converging after finite number of steps* (2008, https://admjournal.luguniv.edu.ua/index.php/adm/article/view/814/0) and Newton trace identities (e.g. https://www.math-challenge.org/en/projects/trace_cayley_hamilton_newton/problems/trace_cayley_hamilton_newton). The research increment claimed here is the **exact frozen E* source-versus-weak-observer classification and sharp three-step witness**, not novelty of these general tools.
