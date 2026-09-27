# Observer-sensitive approximation contracts

Status: AUTHOR_SYMBOLIC_DERIVATION / SHARED_CONTEXT / NOT_ADMITTED.
Activity: RA-CAAAC604CB513AEA8BBC1DFC.
Base: EM commit 951cc16cb09635fae9f93230d96030fdaa2035b3,
`qft_row_queries/point_queries/MASS_WEIGHTED_APPROXIMATION_BOUND.md`.

These are bounds for the actual full native two-arm instrument, with all
signed residual coordinates and ordered feedback preserved. They do not
construct a polynomial oracle or prove generic QFT dequantization. The
amplitude-query sampling and stability approach has direct antecedents in
Bravyi, Gosset and Liu, https://arxiv.org/abs/2112.08499 . The specific bounds
below are derived here, with no assertion of literature-wide novelty.

## 1. The sampler only needs the projective row family

For one measured prefix h write v=v_h, M=||v||^2 and let u=u_h be a complete
consistent approximate row function, fixed independently of the private
latent path. The sampler's score at z uses u(z), T_h u(P_i^-1 z), and a
fair fallback if both are zero. Multiplying the entire u_h by one common
nonzero real scalar changes none of these probabilities. Consequently set

    Eproj_h = inf_(c real) ||v_h-c u_h||^2
            = M_h - <v_h,u_h>^2/||u_h||^2, if u_h != 0;
            = M_h, otherwise.

The existing reference-kernel argument, applied to c u and taking the
infimum over nonzero c, gives

    TV <= sum_i sum_(|h|=i) min(M_h, sqrt(M_h Eproj_h))
       <= sum_i sqrt(sum_(|h|=i) Eproj_h).

All final TV bounds are capped at 1. If the optimizing scalar is zero,
the first bound for that prefix is simply M_h; equivalently take a limit
through nonzero scalars. This handles an orthogonal u as well as u=0.
There is no online requirement to compute c, M, the norm of u or the
overlap. They are analysis quantities; a usable algorithm still needs an
efficiently established error certificate. Choosing a different scalar
for each label generally changes the kernel and is not covered.

Example: u=8v has Eproj=0 and exactly the same sampler, whereas its ordinary
squared error is 49M. Thus global raw L2 accuracy is a sufficient condition,
not a necessary requirement for successful sampling.

## 2. Direct cost of replacing a local score by a fair bit

At a positive-mass exact prefix define x_z=v_h(z),
y_z=T_h v_h(P_i^-1 z), S_z=||x_z||^2+||y_z||^2 and

    L_h = sum_z |<x_z,y_z>|,    G_h = sum_z <x_z,y_z>.

The exact proposal law is S_z/(2M_h), and the exact local plus probability
is 1/2+<x_z,y_z>/S_z. Using the same proposal and an independent fair bit
therefore changes the joint bit/next-label kernel by exactly

    L_h/(2M_h).

If this replacement is made on a declared prefix set H_i, reference-kernel
telescoping gives terminal joint TV at most

    (1/2) sum_i sum_(h in H_i) L_h.

This requires no row approximation at replaced steps if an independent
upper certificate on L is available. Computing L by enumerating all rows
is a validation technique, not an efficient general certificate.

The *single-step marginal bit* error is only |G_h|/(2M_h). Cancellation
can make it much smaller than the joint error. It cannot be substituted
for L in intermediate steps: the latent conditional law affects future
outputs. It is valid when only that last bit is observed and the latent
label is discarded, or when a separate propagation argument is supplied.

## 3. Robust support separation

Suppose A is a work-label set satisfying A intersection P_i A = empty.
Let epsilon = sum_(w outside A)||v_h(w)||^2/M_h <= 1/2. Define normalized
mass distributions p(w)=||v_h(w)||^2/M_h and q(w)=p(P_i^-1 w).
Then p(A)=1-epsilon and q(A)<=epsilon. Cauchy--Schwarz within A and its
complement gives

    L_h/M_h <= sum_w sqrt(p(w)q(w))
             <= sqrt((1-epsilon)q(A)) + sqrt(epsilon(1-q(A)))
             <= 2 sqrt(epsilon(1-epsilon)).

The last function is increasing up to q(A)=1-epsilon; our allowed range
q(A)<=epsilon<=1/2 lies before that maximum. A fair replacement thus has
joint-kernel TV at most sqrt(epsilon(1-epsilon)) <= sqrt(epsilon).
At epsilon=0 it is exact for arbitrary admitted ordered T_h. For larger
epsilon use the general trivial 1/2 bound for a fair-bit replacement.

A finite-sample guess of A does not certify epsilon. Discovery, leakage
estimation, confidence failure and label-set membership costs must all be
charged. This is a robust extension of support-disjointness certificates,
not a claim that approximate separation is available on hard instances.

## 4. Plain suffix-path Monte Carlo: exact error, limited implication

Fix an actual raw prefix g at depth k. For a target h=g+s at k+ell, let
Z_(h,e) be the actual signed orthogonal native feedback word and work
permutation applied to v_g along preparation suffix e, without the usual
factor 2^-ell. Uniform e then has E Z=v_h and ||Z||^2=M_g. A mean u_h of m
independent paths, chosen as a consistent row function before queries,
satisfies

    E ||u_h-v_h||^2 = (M_g-M_h)/m.

Completeness of the actual instrument implies, for fixed g,

    sum_s E ||u_(g,s)-v_(g,s)||^2 = (2^ell-1) M_g/m.

Summing all g at depth k gives (2^ell-1)/m. Correlation between different
target histories does not affect these expectation identities. The m
paths within each estimator are independent and sampled with replacement.

This proves the cost of meeting the *global raw L2 sufficient contract*
with this particular estimator. It is neither a sampling-TV lower bound
nor a general oracle/algorithm lower bound. In particular, zero-mass
histories can contribute to this L2 error yet have no exact-reference
weight in the sharper sampler bound. For a=1 the native standard initial
trajectory emits only plus bits: all positive-reference prefix path
estimators are exact, while impossible measured prefixes account for the
aggregate variance above.

Jensen and the prefix cap instead give expected reference-weighted error
at most sum_(g,s) min(M_(g,s), sqrt(M_(g,s)(M_g-M_(g,s))/m)). This depends
on the actual mass dispersion. No cheap mass oracle or dispersion
certificate is supplied by this formula. Projective error and direct
coherence certificates offer further ways to avoid overpaying for raw
field accuracy, without assuming that they are easy to compute.
