# EC49DJ supplementary lemma — exact obstruction to a one-neutral-gate tensor lift

**Scope.** Fix any set of r native signed-six-axis prefix paths p_1,...,p_r of the same length and displacement, with a finite whole-operation future alphabet and final A/B adjacency observer. Let F_x(p), F_y(p), F_1(p) denote the respective *complete, prefix-inclusive* future response vectors (supported on their respective disjoint weighted-x, weighted-y and count output channels, for every final joint-tag slot), including any admissible return restriction and seam changes. The positive BRC axis weights satisfy x_j>0, y_j=a*x_j+b with a,b>0.

For each base prefix p_i, prepend exactly one ordered, native-neutral pair G_j=(+Ej,-Ej) for any axis j in {1,...,6}. Since G_j returns to the same six-component endpoint and ends with a negative letter, all original A/B tags and all later seams are unchanged by prepending G_j. The future response vector satisfies the exact channel-separated identity

R(G_j p_i) = x_j [F_x(p_i)+a F_y(p_i)]
              + [b F_y(p_i)+F_1(p_i)].

By definition F_x,F_y include both the base-prefix and admissible future suffix weights, tag choice, endpoint-return and observer coordinates. No further prefix-product factor is multiplied into F_x,F_y. The equation follows directly from BRC multiplicativity and y_j=a x_j+b. It is valid over positive real or rational weights with matching field-rank semantics.

**Theorem.** All rows generated from the r fixed base prefixes by prepending any one such native gate span a vector space of dimension **at most 2r** (possibly smaller), regardless of how many axes are tried. Proof: for each fixed i, all six gate variants lie in the span of the two bracketed vectors, so a union of r families has rank at most 2r. QED.

**Consequence.** A six-prefix unweighted six-feature basis with one added neutral pair can have at most 12 weighted rank, and therefore cannot certify an 18-dimensional three-instrument observation space for an internal fibre. This is an exact **certificate-family obstruction**, not a true full-path rank deficiency. The independent EC49DJ extreme-fibre construction succeeds at 2h+8 specifically because it changes the *positive core itself* across witnesses; it is not restricted to one fixed base path plus one gate.

**Finite audit:** with x=(2,3,1,2,3,4), y=2x+1, h=2, the specific one-gate extensions of the EC49DE six-feature bases have observed weighted rank 12 of formal 18 for both exact-h and cumulative languages at D=0. The analytic bound holds for all models matching the hypotheses, independent of this sample. The source script of the exploratory finite sample is retained in the local EC49DJ handoff workspace; an independent replication should work against the current native X6 observer before promotion.

**Research status:** AUTHOR_ANALYTIC_LEMMA / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED. P000 and the six-dimensional native ontology unchanged.
