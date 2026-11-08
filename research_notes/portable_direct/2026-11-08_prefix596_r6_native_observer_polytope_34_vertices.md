# PREFIX-596-R6 — The native BRC triple-observer behavior polytope has exactly 34 vertices

Date: 2026-11-08 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_RATIONAL_LEMMA / UNREVIEWED / NOT_ADMITTED. Scientific input pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.

Dependencies: the original native BRC kernel of PREFIX-565; PREFIX-590 exact finite-window ranks; PREFIX-591 all-horizon 33-dimensional cubic observer space; PREFIX-594 root-universal full triple-law invariance; PREFIX-595 exact 34 native observation classes and rank-one four-class circuit. This lemma retains the exact `(T,P0,P1)` observer and six original labeled actions used in those results.

## Exact statement

For each of the 96 original ports i, let `F(i)` be the vector of **all normalized rational moments of total degree at most 3** of `(T_n,P0_n,P1_n)`, over path lengths `n=0,1,2,3,4,5`, using the original zero-root uniform six-action BRC kernel. Let `B` be the convex hull in this finite rational coordinate space of `{F(i):0<=i<96}`. Thus `B` describes exactly the permitted finite-window moment vectors from **all native initial-port probability distributions**.

Then `B` has precisely **34 distinct vertices** and affine dimension **32**. Up to relabeling the 34 distinct port-behavior types, its unique affine dependence is
`
F(6)+F(29)=F(7)+F(28)
`
where `F(6)=F(30)` and `F(7)=F(31)`, and the other 30 types each occur with zero coefficient. No one of the 34 vertices is a convex combination of the other 33.

The same set of 34 port types and the same affine relation describe the **universal full triple-path-law behavior polytope** for all lengths and externally predetermined nine-root schedules: the all-length observation space is exactly U of dimension 33 and the finite-window moment vectors through depth five already span U.

## Proof

1. PREFIX-590 verifies that the cumulative rational rank of native moment observations from lengths 0 through 5 is 33. PREFIX-591 proves the full all-length cubic observer span U also has rank 33. Hence the finite-window rational moment observables span U exactly. In particular, equality/distinction of port evaluation vectors on U is exactly equality/distinction of their length-0..5 moment features. The common n=0 constant moment gives an affine hyperplane of codimension one.
2. PREFIX-595 reconstructs the U basis from the original kernel and identifies exactly 34 distinct port evaluation rows. Rational row elimination gives rank 33. Since there are 34 rows, the affine relation space is one-dimensional. Its native equality `v(6)+v(29)=v(7)+v(28)` is explicitly verified componentwise on all 33 U-basis functions, and has zero coefficient sum, so it spans that one-dimensional affine relation space.
3. Suppose some distinct feature vertex v_c belongs to the convex hull of the remaining 33. The equality `v_c=Σ_{d!=c} λ_d v_d` with `λ_d>=0` and `Σ λ_d=1` would yield a nonzero affine relation with exactly one positive coefficient and all other coefficients nonpositive. But every nonzero affine relation is a scalar multiple of the four-point circuit `(+1,+1,-1,-1)`, which has two strictly positive and two strictly negative entries. Contradiction. Thus all 34 distinct feature vectors are extreme. Their affine dimension is 33-1=32.
4. PREFIX-594 proves all-horizon path laws for every allowed root schedule factor through U and already include the finite-window moments at zero root. Thus the universal behavior map has the same kernel and same 34 extreme row types. This extends the polytope statement to the universal specified observational language, without changing the finite proof basis.

## Consequences for positive state representation

The exact 34-class Markov quotient proved in PREFIX-595 is **minimal among deterministic partitions of the original ports** that preserve the declared universal triple-path laws. In addition, consider any representation using abstract states whose individual observation behaviors are themselves achievable by native probability mixtures (i.e. each latent state law lies in B), with arbitrary *stochastic encoding* of each original pure port into the latent states. Because each of B's 34 vertices is extreme, reproducing all 34 pure native types requires at least 34 distinct such latent states. The PREFIX-595 quotient attains the bound.

By contrast, the previously proved 33-dimensional **linear** observer representation (including constant) uses signed affine coordinates for exact calculations: its 32 variable parameters are sufficient but are not a positive 33-state Markov realization. General representations whose latent state laws are not constrained to be native mixtures constitute a separate realization question.

## Exact check and next question

The PREFIX-595 published executable certificate checks 34 distinct classes, 33-dimensional row rank and the explicit four-port circuit; PREFIX-590/591 establish the finite-depth rank and all-length span respectively, and PREFIX-594 establishes root-universal full triple-law factorization. This conclusion is an exact convexity argument from those rational certificates, with no additional floating-point data.

Next: derive a direct four-phase/native-action explanation for the four-point relation; test the minimal dimension of unconstrained positive hidden-state realizations and compare bit complexity and update costs of 33-linear vs 34-positive interfaces.
