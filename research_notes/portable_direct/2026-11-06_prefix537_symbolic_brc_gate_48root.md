# PREFIX-537 — Exact symbolic BRC–gate histogram, 48 rooted phases

Date: 2026-11-06, Asia/Shanghai. Task lineage: RS-X6-NATIVE-ROTATION-DYNAMICS, following PREFIX-536. Frozen scientific source: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Mathematical status: AUTHOR_DERIVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Precise observer
The frozen four-STAR, directed native-X6 path model has 48 phases; at each macro step there are 3 successors and 2 separately labeled INNER/OUTER Cell microstep choices, hence exactly 6^d histories from a fixed root. For root s define
`P_s(d;q,z)=sum_{w rooted at s, length d} q^{p_1(w)} z^{H(w)}`;
`p_1=min(N_+,N_-)` is the signed first-axis BRC cancellation count, and `H` counts consecutive-INNER gate events at target `(A,+L1,-L3)`.

## Constructive semiring-lift proposition
Put `sigma(i) in {-1,0,1}` for signed incidence of first axis at phase i, `epsilon(i)=abs(sigma(i))`, and T for the gate phase. For each `r in {-1,0,1}` start the following exact polynomial state over `Z[v,z]`:

```
f_0^r(i)=v^(2-abs(sigma(i)-r)),    g_0^r=0.
f_(d+1)^r(i)=2 sum_(j in NEXT(i)) v^(epsilon(i)+epsilon(j)) f_d^r(j)
 + sum_(m in NEXT(i), T in NEXT(m)) v^(epsilon(i)+2epsilon(m)+epsilon(T)) g_d^r;
g_(d+1)^r=(z-1) f_d^r(T).
```

For every root s with sigma(s)=r, the exact polynomial `f_d^r(s)` is divisible by `v^2`, and its remaining exponents are even. Substituting `v^(2p+2)->q^p` yields `P_s(d;q,z)` coefficientwise. Three common evolutions therefore suffice for all 48 fixed roots with no specialization in q or z. Proof: expand the earlier exact rank-one gate lift over the commutative polynomial ring, preserving both labeled INNER/OUTER realizations; the endpoint BRC identity `2p_1=K-abs(sigma(end)-sigma(root))` supplies precisely the terminal correction. The `z-1` term replaces the unit weight only on qualifying successive INNER branches. Every operation is addition/multiplication of integer-coefficient polynomials.

## Exact support and output bound
For every depth d, `P_s(d;1,1)=6^d`, and each coefficient is a nonnegative integer no larger than `6^d`. The primitive path observer gives `0<=p_1<=d`; PREFIX-527's `d_min(k)=4k-2` gives `H<=floor((d+2)/4)`; the earlier gate–BRC inequality gives `H<=p_1`. For `h_d=floor((d+2)/4)`, every nonzero coefficient is supported in `0<=h<=h_d, h<=p<=d`. Therefore there are at most `(h_d+1)(d+1)-h_d(h_d+1)/2` coefficients per root and each uses at most `floor(d log2(6))+1` bits. Dense output for all 48 roots through N has `O(N^3)` coefficient slots and `O(N^4)` worst-case bits. This is output accounting for the declared observer, not an upper bound on the raw provenance state.

## Actual complete finite certificate
The accompanying self-contained standard-library Python program reconstructs the 48 native directed phases; evaluates three shared sparse exact `Z[v,z]` lifts; independently enumerates the legal labeled transitions with full phase, last INNER bit, raw axis visits and gate count; and compares the complete `Z[q,z]` polynomial for all 48 roots at all depths 0..24 (1200 exact polynomial equalities).

Execution: `ALL_CHECKS_PASS`. At depth 24 the 48 rooted polynomials contain 1876 nonzero monomials in total (36 to 41 per root), 26 distinct rooted distributions, maximum gate degree 6, and maximum coefficient bit length 61. The largest intermediate lift dictionary sizes per sign seed (-1,0,+1) are (1900,1880,1901), serving respectively 4,40,4 roots. For example, at depth 6 from root (A,+L3,-L1):
`14592 + 28800q + 960qz + 2176q^2 + 128q^2z`.
The sum is 46656=6^6. Full per-depth statistics are reproducibly emitted as `PREFIX537_EXACT_EXECUTION.json`.

A separately instrumented local exploratory run measured 281 ms with tracemalloc for shared symbolic lifting and 1205 ms without tracemalloc for 48 raw dynamic programs; the differing profiler overhead means no controlled speedup ratio is claimed.

## Reproducibility observation
The PREFIX-536 benchmark source at commit `58c1caf4...` imports the PREFIX-535 sibling and tests for definitions `delta_coefficients` and `evaluate_roots`; the sibling at the same commit defines `denominator` and `evaluate` instead. The published import contract requires repair before a fresh execution of PREFIX-536 as written. PREFIX-537 uses a self-contained certificate and does not depend on that import.

## Next research
Run like-for-like symbolic/forward/scalar-11 benchmark instrumentation across several depths and memory budgets; investigate exact 26-class symbolic extraction and the costs of preserving Cell/provenance future operations. Continue the original native X6 rotation-dynamics mother question rather than promoting a histogram quotient outside the proved observer.
