# PREFIX-508 — Explicit mod-6 compiler for BRC V-support and interval moments

Date: 2026-11-05 (Asia/Shanghai). Author-side Researcher-ID: EM-DIRECT-7E330D. Native research activity: RA-59AD0564D9C39E47F9211A1B (MCP issued; no formal CLAIM). **Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.**

Scientific input is frozen at \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d\`, with its native X6, five-axis restricted path observer. Normative policies were freshly read from current canonical main and are not part of the frozen scientific input. Direct predecessors: PREFIX-499, 500 and 507.

## Mother objective and new result

Continue exact gapless ranking/unranking of the signed native X6 path observer, including BRC cancellation observations and order-sensitive KMP/first-source controller state, with a declared native append-then-reencode operation. This note supplies an explicit practical row compiler for PREFIX-507's V-interval moments, replacing the generic existential quantifier-elimination construction with a fixed small modulus.

**Theorem (effective mod-6 V-row interval compiler).** For either gate g in {aab,aba}, for all integer n>=0, signed five-axis displacement y, and fixed W, and for each controller state (q,t), the set

    {V in Z : (q,t) belongs to C_g(n,y,V,W)}

is a finite union of intersections of integer intervals with residue classes \`V ≡ r (mod 6)\`. At most a constant number of intervals and operations are required, uniformly in n,y,W; there are no parametric variable moduli and no generic Presburger solver. Every interval endpoint is computed by affine integer arithmetic, floors and ceilings on the input parameters. Consequently, exact sums \`F(L,H)=Σ_{V=L}^H k_g(n,y,V,W)\` and \`T(L,H)=Σ_{V=L}^H (V+1) k_g(...)\` are computable using a fixed number of exact integer operations and O(1) auxiliary integer cells after the compiler's finite suffix table has been initialized. For valid path observations, integer operands have O(log(n+2)) bits; per-bit cost of arithmetic is accounted for separately. This is an actual explicit fixed-modulus construction, not only an existence result.

The theorem applies to the originally declared six-dimensional X6 **restricted five-axis path family** (sixth coordinate unused), not a different five-dimensional ontology. Retained observations: \`n\`, \`y=(y_a,y_b,y_c,y_d,y_e)\`, five signed-axis cancellation counts \`p_i\`, \`V=p_b+2p_d+p_e\`, \`W=p_c+p_e\`, terminal KMP prefix length q for g and first-source tag t∈{N,B,C}. Source B is the first native b/B step; source C the first native c/C step. Colors \`a,b,B,c,x\` collapse the other primitive directions as in PREFIX-499; this is only the verified observer quotient for the stated future operation.

## Proof 1: exact suffix/first-source cases

Let \`m=(n-Σ_i |y_i|)/2\`. Reject invalid parity, n<Σ|y| or W<0. For each suffix s of length ℓ=min(n,3), at most 5^3=125 possibilities, define its color occupancies \`u_a,u_b,u_B,u_c,u_x\`, and \`s_B=u_b+u_B\`, \`s_C=u_c\`. The terminal KMP state q is determined by s. Any remaining prefix is an arbitrary permutation of the remaining color multiset.

Exactly two constructions can yield a first-source tag:

1. **Prefix-first B or C:** a nonempty prefix contains at least one step of the desired source type. Reorder the prefix with that type first. All other prefix colors are arbitrary.
2. **Suffix-first:** the prefix has no source steps, so the *total* source occupancies equal \`s_B,s_C\`; t is exactly the first source in s, or N when there is none.

These alternatives exhaust every ordered color word. No-source N is covered by the second case. Using all suffixes and taking a union counts each reachable controller state only once.

For a fixed displacement y write \`a+=max(y_a,0)\`, \`a-=max(-y_a,0)\` and analogously for b, and \`S=|y_d|+|y_e|\`. Put \`d=p_d\`, \`e=p_e\`, \`z=d+e\`. Occupancy equations from the frozen observer are

    p_a=m−V−W+z,
    p_b=V−2z+e,
    p_c=W−e,
    k_a=p_a+a+, k_b=p_b+b+, k_B=p_b+b−,
    k_c=2p_c+|y_c|,
    k_x=p_a+a−+2z+S = m−V−W+3z+a−+S.

Every inequality and parity condition that follows is exact integer arithmetic.

## Proof 2: prefix-first branch eliminated to one integer interval

For suffix s choose first prefix source tag t=B or C. Set

    A=max(0,u_a−a+);
    B=max(0,u_b−b+,u_B−b−);
    C=max(0, ceil((u_c−|y_c|)/2));
    K=u_x−a−−S.

If t=B, replace B by \`max(B,ceil((s_B+1−|y_b|)/2))\`; if t=C, replace C by \`max(C,ceil((s_C+1−|y_c|)/2))\`. The +1 guarantees a source of desired type in the freely ordered prefix.

These finite color/first-source conditions reduce to

    p_a>=A, p_b>=B, p_c>=C, k_x>=u_x, d>=0, e>=0.

For fixed z the e inequalities are

    max(0,2z−V+B) <= e <= min(z,W−C).

An integer e exists precisely when W>=C, z<=V−B, 2z<=V+W−B−C, and z>=0. The a/x conditions impose \`z>=V+W−m+A\` and \`3z>=V+W−m+K\`. Therefore the branch is feasible **iff**

    W>=C and
    max(0, V+W−m+A, ceil((V+W−m+K)/3))
       <= min(V−B, floor((V+W−B−C)/2)).

This one-dimensional inequality is necessary and sufficient, with a constructive witness e and d=z−e. Substituting \`V=6h+r\` (r=0,...,5) makes all five lower/upper expressions *integer affine in h*:

    lower: 0;
           6h+(r+W−m+A);
           2h+ceil((r+W−m+K)/3).
    upper: 6h+(r−B);
           3h+floor((r+W−B−C)/2).

The six pairwise lower<=upper conditions, together with \`0<=V<=2m\`, each give a constant or an integer half-line bound for h. Their intersection is one integer interval (possibly empty) for each r. Thus each prefix-first suffix branch compiles into six explicitly bounded residue intervals.

## Proof 3: suffix-first equality branch

When the prefix contains no source, total b/B occupancies and total c occupancies are exactly the suffix counts. Feasibility therefore requires

    y_b=u_b−u_B,
    P=(s_B−|y_b|)/2 in Z>=0,
    Q=(s_C−|y_c|)/2 in Z>=0.

Then p_b=P, p_c=Q, e=W−Q and \`2z=V+W−P−Q\`. The conditions e>=0, z>=e, p_a>=A and k_x>=u_x are equivalent to

    W>=Q;
    V+W−P−Q ≡ 0 (mod 2);
    V >= W+P−Q;
    V >= 2(u_x−a−−S−m)−W+3(P+Q);
    V <= 2m−W−P−Q−2A.

The color b/B and c inequalities follow from the fixed total counts and the y_b equality. Hence suffix-first contributes a single **mod-2** interval, which can be split into mod-6 classes. The n<3 cases use the entire word as s; prefix-first can only apply if a prefix exists.

Combining the finitely many branches yields for each controller state and r a finite list of integer h intervals. Sorting and merging overlapping/adjacent intervals is exact union, and the fixed suffix bound proves O(1) cardinality and compiling arithmetic independent of n.

## Exact counting and weighted moment

For each disjoint merged h interval [h0,h1] of residue r, intersect with \`ceil((L−r)/6)<=h<=floor((H−r)/6)\`. With a resulting interval [a,b], put N=b−a+1. Its contribution to F is N; its contribution to T is

    Σ_{h=a}^b (6h+r+1) = N * (3(a+b)+r+1).

Sum independently for all (q,t) and residue r. Controller-state multiplicity is exactly preserved. A singleton check is the ordinary support oracle. The {0,2} hole at n=2, y=(0,0,0,0,0), W=0, (q,t)=(0,N) is reproduced for both gates.

## Implemented compiler (precise pseudocode)

The attached standalone source \`prefix508_mod6_compiler.py\` implements the full rules using Python arbitrary-precision integers and no third-party packages. Its procedure is reproduced here in algorithmic steps; all divisions are mathematical floor/ceil over signed integers.

    COMPILE(g,n,y,W):
      reject invalid n/parity/mass/W; m=(n−sum(abs(y)))/2
      for each s in {a,b,B,c,x}^{min(3,n)}:
        compute (u_a,u_b,u_B,u_c,u_x), q from terminal suffix of g
        for first-prefix tag in {B,C}, if a prefix exists:
          calculate A,B,C,K from Proof 2
          for r=0..5:
            V=6h+r
            intersect integer half-line constraints lower_i(h)<=upper_j(h)
            with 0<=6h+r<=2m; append [hmin,hmax] to (q,tag,r)
        if source totals in prefix can be zero:
          calculate P,Q and inequalities/parity from Proof 3
          for r=0..5:
            append exact h interval under parity and V bounds
            to (q,first_source_in_s,r)
      sort and merge each (q,tag,r)'s intervals; return map
    MOMENT(map,L,H):
      for each controller state, residue and merged h interval:
        intersect with query interval
        add N to F, N*(3*(a+b)+r+1) to T
      return (F,T)

The full executable certificate is distributed with the local evidence archive alongside the result JSON; this research note is the canonical proof and algorithm specification.

## Executed independent exact-integer certificate

Executed locally with Python 3 standard library only. The independent baseline is dynamic programming over all ten primitive signed directions, **retaining the full ten-direction count tuple and ordered KMP/first-source state until observer readout**. The compiler is tested against that independent native baseline. All (y,W) rows for n=0..6 and both gates are tested, with every V∈[0,n] and every integer interval [L,H] in the certificate's stated range. Deterministically spaced samples of rows are additionally tested for n=7,8,9. The compiler is also independently compared on 60 longer random-source probes at n=9,17,32,64,127 using bounded integer d/e occupancy plus five-color suffix enumeration.

Actual certificate summary (one execution of the provided Python source):

- Status: \`ALL_CHECKS_PASS\`.
- Exactly **76,042** V membership comparisons and **594,678** inclusive V-interval F/T comparisons against the independent ordered native baseline for the declared rows.
- n=6: 3,024 of 3,024 (y,W) rows per gate fully tested; n=7,8,9 respectively 185,181,181 sampled rows per gate.
- Independently reconstructed \`{0,2}\` first-source N gap for both gates.
- 60 longer independent d/e-fiber probes at n up to 127, all passed.
- Integer semantics: Python unbounded exact integers; no floating-point equality or numerical tolerance. Source includes the deterministic random seed 508 and independent baseline definitions. Exact test results are retained in \`PREFIX508_EXECUTION.json\` in the downloadable evidence package.
- Performance: this certificate establishes correctness over the executed finite scope; the universal theorem follows from proofs 1–3, not timing or numerical extrapolation. A separate production throughput comparison is an open engineering task.

## Current state and next discriminating unit

Author-side algebraic proof and finite exact test complete; independent mathematical review and admission remain open. The formal rotation task \`RS-X6-NATIVE-ROTATION-DYNAMICS\` was queried through native control; its publication is X6U/P0 and is presently a separate unclaimed formal task. This result contributes an exact BRC fiber counting component toward its path-lift subobjective; it does not independently derive the outstanding physical rotation dynamics.

**PREFIX-509:** Integrate mod-6 compiled F/T into the PREFIX-504/505/506 block-index and Monge builder; measure bit-cost, time, number of interval components, retained Python heap bytes, rank/unrank, and native append+reencode against original single-V support queries. Test whether fixed-gate suffix templates can be minimized without changing controller-state support. Preserve frozen scientific inputs and P000 scope.

### Sources

Frozen EM science \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`; PREFIX-499/500/507 original project notes; standard Presburger elimination context: Christoph Haase et al., *An Efficient Quantifier Elimination Procedure for Presburger Arithmetic*, ICALP 2024, DOI 10.4230/LIPIcs.ICALP.2024.142 (published 2024-07-02); the explicit bound of modulus six is proved directly here and not attributed to general QE.
