# CBRC-F7 — Self-contained positive-even rank-one quotient rigidity

Date: 2026-10-28 (Asia/Taipei). **NONBLIND / SOURCE-EXPOSED / PORTABLE AUTHOR-LEVEL PROOF / UNREVIEWED / NOT_ADMITTED**. This is a new, narrowly scoped derivation in a context that has read the F7 frozen Result and its original repair. It is **not** an independent native Driver Review, a reference pass, a synthesis, a task publication, or a new proof of the entire F7 return. No clean-blind claim is made.

## Exact source and attribution

- Enterprise Math reference snapshot: `main@988974d48b6df938b9ec48f1b09d3da15c169ea1`.
- Original, unchanged F7 frozen Result: `research_result_records/RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION/RR-AA38973D56330E59D315.json`, Git blob `3366edeae347e76b1f6a50bc45a6c6e4cd2dd472`.
- Original F7 author `EM-CBRCF7-83A1D4`, original theorem-repair return `research_returns/COHERENT_BRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION_REVISION_20260903.md`, Git blob `69265a0fadfd9fcd0be9354ff74f33e5e825fe84`.
- That return's Section 5 invokes an accepted earlier F4 rank-one free-block theorem to eliminate the period branch. Its historical F4 report was not accessible via this run's current GitHub-main file read; this note provides a **self-contained replacement argument only for that rank-one quotient implication**, without modifying either F4's historical mathematical status or the F7 Result.
- Project research basis: current locked P000 X6+separately typed time, global P000 frozen historical blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`, and observer/provenance preservation. The proof below is explicitly scoped to the **external integer additive quotient** in the F7 proof; it is not an X6 physical dynamical theorem or new ontology.

## Lemma (positive-even rank-one additive rigidity)

Let `g: Z -> R_{>=0}` satisfy `g(0)=0`, `g(-n)=g(n)` for all integers `n`, and `g(n)>0` for every `n!=0`. Suppose `M=[[a,b],[c,d]] in GL_2(Z)` obeys

```
g(a x+b y)+g(c x+d y)=g(x)+g(y)    for every (x,y) in Z^2.     (1)
```

Then `M` is a **signed permutation matrix**. No convexity, regularity, growth condition, bounded search, norm, or quadratic ansatz for `g` is assumed.

### Proof

We first show that the first column cannot have both entries nonzero. Suppose `a!=0` and `c!=0`.

**If `b=0`:** `det(M)=ad=+/-1`, so `a=+/-1`. Equation (1), specialized to `y=0`, gives `g(a x)+g(c x)=g(x)`. Evenness yields `g(a x)=g(x)`, and hence `g(c)=0`, contradicting `c!=0`.

**If `d=0`:** `det(M)=-bc=+/-1`, so `c=+/-1`. The same specialization gives `g(c x)=g(x)`, hence `g(a)=0`, a contradiction.

**If `b!=0` and `d!=0`:** Take the mixed first difference in `x` and `y` of (1), using `Delta_h g(z)=g(z+h)-g(z)`. The input right-hand side has mixed difference zero, so

```
(Delta_a Delta_b g)(a x+b y)
   +(Delta_c Delta_d g)(c x+d y)=0.                              (2)
```

Since `M` is unimodular, `(a x+b y,c x+d y)` ranges independently over `Z^2`. Holding either output fixed shows that each summand in (2) is a constant function. In particular, `Delta_a Delta_b g=C` on the whole integer line.

Put `L=lcm(|a|,|b|)>0` and let `Tg(n)=g(n+1)`. Negative-step first differences are translates and negatives of positive-step differences. For positive `A=|a|`, `B=|b|`, the exact finite shift-polynomial identity

```
(T^L-1)^2 =
  (1+T^A+...+T^(L-A))
  (1+T^B+...+T^(L-B))
  (T^A-1)(T^B-1)
```

therefore implies `Delta_L^2 g` is constant on `Z`. Consequently the integer sequence `h(k)=g(Lk)` is an exact polynomial of degree at most two in `k`. As `h(0)=0` and `h(-k)=h(k)`, it has the form `h(k)=alpha*k^2`. Strict positivity at `k=1` implies `alpha>0`.

Now set `x=L, y=0` in (1). We obtain

```
alpha*a^2 + alpha*c^2 = alpha.
```

But nonzero integers `a,c` satisfy `a^2+c^2>=2`, contradicting `alpha>0`.

Thus the first column has at most one nonzero entry. Interchanging the two input variables gives the same assertion for the second column. An invertible integer `2x2` matrix with exactly one nonzero entry in each column must place them in different rows, and its determinant `+/-1` forces both nonzero entries to be `+/-1`. Hence `M` is a signed permutation. QED.

## Direct application to the original F7 period branch

Retain exactly the **original F7 author's premises**, notation, and proof scope: `f:Z^2 -> R_{>=0}`, `f(0,0)=0`, `f(-n,m)=f(n,m)`, `n!=0 => f(n,m)>0`, and an exact `A in GL_4(Z)` conserving `f(x)+f(y)`. Assume `f` has a nonzero period. Positivity on nonzero old coordinate implies the period group is `H={0} x k Z` for some integer `k>=1`.

1. The period group of `F=f direct_sum f` is exactly `H direct_sum H`: the two first differences of `f` arising from a pair period are individually constant; a nonnegative function on the whole integer lattice cannot have a nonzero constant first difference along any integral step, by arbitrarily many positive/negative iterations.
2. Exact conservation and invertibility imply that `A` preserves this period group and induces an automorphism of the quotient `(Z direct_sum Z/kZ)^2`. Its induced old-coordinate map is some `M in GL_2(Z)`. For each fixed input old-coordinate pair, the induced map bijects the finite `(Z/kZ)^2` torsion fiber onto the fiber over its output old-coordinate pair.
3. Set `g(n)=min_{m mod k} f(n,m)`. This finite minimum satisfies `g(0)=0`, `g(-n)=g(n)`, `g(n)>0` for `n!=0`. Minimize the original conserved pair scalar over corresponding torsion fibers; their bijection gives precisely equation (1) for the induced `M`.
4. The lemma makes `M` a signed permutation. But F7's `A0` requires the old parts of **both** output slots of the first old elementary input to be nonzero, i.e. both entries of the first column of `M` nonzero. Contradiction.

Therefore the **period branch** of the original F7 rank classification is excluded by an explicit proof from its stated hypotheses, without a separate F4 rank-one theorem call. This does not alter the other F7 proof branches, ablations, source-exposure assessment, or its frozen Result verdict.

## Review boundary and next action

This narrowly scoped lemma is hand-proved by a source-exposed reader of the frozen F7 Result. Finite checker execution was neither required for, nor substituted for, the universal finite-difference argument. The proof still requires actual independent qualified review and the current exact F7 review set before any **native** Review/Reference/Synthesis/Follow-up action. The connected Site observed in this turn had only `source:read/control:read`, no current native Driver DA; the Result's `research_result_reviews/RR-AA38973D56330E59D315/` directory was absent in the verified source snapshot.

Do not modify the original Result or imply a new official task/accepted theorem. After authorized intake, an independent Driver can consume this optional proof patch in the semantic reference check and separately audit the remaining load-bearing F7 rank/hub cases against the frozen packet. Under the mother objective, preserve the original NO_GO candidate boundary pending that formal admission.

Method classification: reuse exact integer shift operators, unimodular quotient and original F7 period structure; no general-purpose toolkit promoted. The smallest remaining control action is to obtain the current authorized independent Driver session/DA, read the exact Result and the complete review set, then apply only missing native passes with Source-bound readback.
