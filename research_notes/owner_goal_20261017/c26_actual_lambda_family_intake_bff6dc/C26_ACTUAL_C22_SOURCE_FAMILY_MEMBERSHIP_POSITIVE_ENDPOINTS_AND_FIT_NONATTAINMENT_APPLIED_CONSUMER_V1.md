# Actual C22 source family: finite membership, positive endpoints and a C26 unattained fit

Classification: RESULT_ONLY_STANDARD_APPLIED_COMPOSE / same-family applied-consumer ledger.
Author: EM-DVR-BFF6DC, SID MCP-47562f9f432d4978a7bea0dd60ecc4aa, no RA.
First artifact creation follows the actual clock observation 2026-10-17 12:40:28 UTC.
Status at creation: AUTHOR_HAND_PROVED / LOCAL_UNREVIEWED.
Author Source: PENDING. Independent technical whole: PENDING.
This is not a new Paper, generic Tool, Native experiment, registration or physical fit.
Root supplies routing/CONTROL and zero mathematical construction or votes.

## 1. The restored literal input and the new obligation

The old C26 model uses a specified nonempty family of positive mean-one targets K.
Its admitted-data image and its general relative-closure theorem did not define
the original source-parametric family. The actual definition has now been located
by immutable citations, rather than guessed from filenames:

C26 original11047 -> C25 -> C24 -> C23 -> the C22 remote transcription.

The C22 transcription is Source15dd9dc4beb060eeb3e76f13fa481486293f1100,
research_notes/divisor_extrema/20261014_c22_seventh_order_parameter_reconstruction.md.
Its actual body is 13359 UTF8 bytes, SHA256
c84fe60e7e9822eb3e3a03e71abb4ccba00844da1104865415afe56a372ef9cd,
Git blob bd6fda0b3cf249dcf769cf17ec318e8894abdc03.
The original attachment described in C23 also has length13359 but has SHA256
587d1e4ff325fe3b7b42a437a20488264f2b9270ba2499040d48e5686a78911c
and blob bf27478277eca90bec261cd5a24ed7f9bf757d7f. These are DIFFERENT artifacts.
I have read the complete remote transcription, not that original attachment.

Fix one literal rectangular graph G for 2^a 3^b, a,b>=1, with vertices V,
edges E and square faces F. Here V,E,F also denote their cardinalities when
used in counts. The actual full graph is for 2^a 3^b*5*7; it is not an integer prefix.
Put r=E+F, p=V+2E+F, Y=F2^r, s=|Y|=2^r.
The parameters are

  lambda=(q_v, alpha_e, beta_e, z_f) in (0,1)^p.                         (1)

The domain is the OPEN cube, not all positive real parameters and not its endpoints.
The target family denoted by calF below is precisely the image of this cube.
The known graph and the complete r independent old characters are part of the input.
No claim is made about unknown graphs or access to these observations by an instrument.

The new obligations are concrete: give a finite exact member test for this calF;
identify exactly which formal closed-cube endpoints remain positive on ALL Y;
and determine a real best-fit attainment case for the original C26 carrier.
The abstract arbitrary-family closure theorem is not re-proved or re-branded here.
Every finite algebraic and positivity argument used below is supplied.

## 2. Literal character coordinates and the finite parameter map

Use H=F2^F x F2^E, with h=(T,U). The face boundary is
partial_2:F2^F -> F2^E and the edge boundary is partial_1:F2^E -> F2^V.
The actual source formula is

  c_(T,U)(lambda)
    = product_(f in T) z_f
      product_(e in U) alpha_e
      product_(e in U triangle partial_2 T) beta_e
      product_(v in partial_1 U) q_v,
  K_lambda(y)=sum_(h in H) c_h(lambda) (-1)^(h dot y).                  (2)

All products are finite; empty products are1.
The no-collision coordinate interpretation can be checked directly:
the old7 horizontal edges determine U and the old5 horizontal edges determine
U triangle partial_2 T. Thus they determine partial_2 T.
A nonempty face subset in a finite rectangle has an exposed edge, so its
face boundary is nonzero. Hence partial_2 is injective and T is determined.
The q boundary is then fixed. The unit T and unit U characters give r independent
coordinates, and every source character is their product. These are the complete
relative old characters in (2), not only bottom-face variables.
In particular the only source with trivial old boundary is h=0 and c_0=1.

For each parameter index i let gamma_i in Y be the column defined by
(Lh)_i=h dot gamma_i. Explicitly, gamma_(z_f) is its face unit vector,
gamma_(alpha_e) its edge unit vector, gamma_(beta_e) has edge part the
e unit vector and face part the e row of partial_2, and gamma_(q_v)
has edge part the v row of partial_1 and face part0. Thus

  c_h(lambda)=product_(i:h dot gamma_i=1) lambda_i.                    (3)

The z and alpha columns alone are a basis of Y, so all columns span Y and L
is injective. Orthogonality of the 2^r characters gives the exact inverse

  c_h= s^(-1) sum_(y in Y) K(y)(-1)^(h dot y).                         (4)

Consequently mean_y K_lambda=1, and equality of all c_h means equality of K.
Equations (2)-(3) also define a POLYNOMIAL map K on the formal closed cube
[0,1]^p. This endpoint extension is a mathematical compactification.
It does not declare endpoint parameters admissible under the original rule (1),
or assert that their original microscopic weights remain strictly positive.

## 3. Exact positivity at every formal endpoint

For lambda in [0,1]^p introduce independent bits delta_i with probabilities
P(delta_i=0)=(1+lambda_i)/2 and P(delta_i=1)=(1-lambda_i)/2.
Let X=sum_i delta_i gamma_i in Y. This is a finite auxiliary probability identity,
not a physical dynamics, scientific simulation or an added observation.

For any h, independence gives E[(-1)^(h dot X)]=c_h(lambda).
Summing the characters and using their orthogonality therefore proves

  K_lambda(y)=s P(X=y).                                                (5)

This proves nonnegativity of every endpoint K, as well as mean1, without
cancellation estimates. Let I(lambda)={i:lambda_i<1}.
An i outside I is a deterministic zero bit. Every assignment of bits on I
has STRICTLY positive probability, including when lambda_i=0.
The possible sums of their columns are exactly their F2-span. Thus

  supp K_lambda = span_F2{gamma_i:i in I(lambda)},
  K_lambda(y)>0 for EVERY y
     iff span_F2{gamma_i:lambda_i<1}=Y.                                (6)

This is necessary and sufficient at all endpoints simultaneously.
There is no assumption that a positive marginal makes every original raw
microscopic weight strictly positive. Interior (1) satisfies (6).

For example lambda=0 gives K=1. Conversely all lambda_i=1 gives
K=s times the point mass at y=0 and is not a positive target on all Y.
There are also positive upper endpoints: take one q_v=1 and all other
parameters1/2. The z and alpha columns still belong to I and span Y,
so this K is strictly positive. Every c_h is positive, but the parameter
q_v is still outside the original open domain. Checking positive coefficients
alone cannot test original membership.

## 4. A finite exact test for the original STRICT family

The selected coefficients are taken by (4) from an arbitrary supplied
strictly positive, mean-one K. For each edge e=(u,v) and face f write

  W_e=alpha_e beta_e q_u q_v,
  B_f=z_f product_(e in partial f) beta_e.                             (7)

For each vertex v fix two distinct incident edges e=(u,v),h=(v,w).
Every vertex has such a pair because a,b>=1. Let R_v be the source
T=empty,U={e,h}. For every edge fix one incident face f(e), which also exists,
and let H_e be source T={f(e)},U={e}. Formula (2) gives

  R_v=(alpha_e beta_e)(alpha_h beta_h) q_u q_w,
  H_e=z_f alpha_e product_(h in partial f,h!=e) beta_h q_u q_v.         (8)

These are the same literal four-, five-, six- and seven-parameter
characters as in the restored C22. Their labels are fixed geometrically;
one must not substitute an arbitrary coefficient with the same degree.
There are E+F+V+E=p selected coefficients.

First require these selected W,B,R,H to be strictly positive, so the following
ratios are defined. Compute SYMBOLIC exact squared parameters

  t_(q_v)=W_e W_h/R_v,
  t_(beta_e)=W_e B_(f(e))/H_e,
  t_(alpha_e)=W_e H_e/[B_(f(e)) t_(q_u) t_(q_v)],
  t_(z_f)=B_f^2/product_(e in partial f) t_(beta_e).                    (9)

The necessary and sufficient finite certificate for K in calF is:

(i) the selected coefficients are positive;
(ii) EVERY t_i in (9) satisfies 0<t_i<1;
(iii) for EVERY nonzero h in H, c_h>0 and
      c_h^2=product_(i:h dot gamma_i=1) t_i.                           (10)

This is a finite exact algebraic certificate, not a numerical algorithm,
termination/bit-cost promise or an accessible physical measurement protocol.
It can be expressed using comparisons and rational operations on the coefficients;
there is no need to run numerical square-root evaluation.

Proof of necessity: from (7)-(8), W_e W_h/R_v=q_v^2 because the shared
q_v occurs twice in the numerator and not in R_v. Similarly W_e B_f/H_e
cancels all factors except beta_e^2; substituting that and q squares gives
alpha_e^2, and the last equation gives z_f^2.
Thus t_i=lambda_i^2, so (i)-(iii) follow.

For sufficiency define the positive mathematical square root
lambda_i=sqrt(t_i). Condition(ii) puts it in the ORIGINAL open cube.
Every product in (10) is the square of the positive source monomial (3).
Condition(iii) therefore gives c_h equal to that monomial, with no sign ambiguity.
The constant coefficient is1 by mean-one normalization. Fourier inversion (4)
gives K=K_lambda. The same recovery (9) proves uniqueness of this interior lambda.
All unselected source coefficients are checked in (10); the p selected
coefficients alone do not license declaring arbitrary data admissible.

This explicitly fills the old good-schedule condition K_R in calF, once the
actual target K_R is supplied. It does not supply a statistical fit, a way
to obtain the complete old-character data, or an inverse on zero parameters.
For the upper-endpoint example in Section3, the same algebra returns
t_(q_v)=1, so it fails(ii), even though all target entries and coefficients
are positive. There is no different interior representation that evades this test.

## 5. The actual positive closure, rather than an unspecified F

Let Pplus={K:Y->R:K(y)>0,mean K=1}. The polynomial image
K([0,1]^p) is compact. Since (0,1)^p is dense in the closed cube,
continuity implies both inclusions and yields

  closure_(all mean-one real vectors) calF = K([0,1]^p),
  closure_(Pplus) calF
    = {K_lambda:lambda in [0,1]^p,
                   span{gamma_i:lambda_i<1}=Y}.                       (11)

Here is the argument without any injectivity assumption at zero:
a sequence of interior images has a subsequence of parameters converging
in the compact cube; its image is the limit. Conversely any closed-cube
parameter is the limit of interior parameters, so its image is a limit
of interior images. Intersect with Pplus and apply (6).
Endpoint parameter fibers can be nonunique; (11) is an image statement
and does not classify those fibers.

In particular 1 belongs to this positive closure, but 1 does NOT belong to calF.
Indeed choose any edge e, which exists. The character h=(empty,{e}) is nonzero
and its source coefficient W_e is strictly positive at every interior lambda.
The same nonconstant Fourier coefficient of the constant function1 is0.
There can therefore be no interior lambda representing1.

Consequently this ACTUAL original family is not relatively closed in Pplus.
This is a property now proved for the specified source family, rather than
an assumption that the arbitrary-family theorem in the earlier ledger had settled.
The positive q_v=1 example in Section3 additionally shows that limiting targets
need not have a zero Fourier coefficient; strict upper parameter bounds matter.

## 6. The literal returned-control consumer and an unattained positive best fit

To ensure this is the original actual control carrier, take known scalars
rho_i in (0,1] and define a finite XOR operator

  T_rho f(y)=E_delta f(y+sum_i delta_i gamma_i),
  P(delta_i=0)=(1+rho_i)/2.                                           (12)

On each character its multiplier is product_(i:h dot gamma_i=1)rho_i.
Hence directly from (2)-(3), T_rho K_lambda=K_(rho lambda).
It preserves1, and it is entrywise strictly positive precisely when the
columns with rho_i<1 span Y, by the same finite support proof as (6).
This is the C23 known positive-control definition, not a physical time update.
For example controlling all z and alpha coordinates by known values in (0,1)
suffices. Fix any such known control for the remainder.

Use the literal C26 complete-observation model. There are distinct known
nonnegative integer positions n_j, labels b_j in {0,1}, and background
degree D>=0. The target in row j is K if b_j=0 and T_rho K if b_j=1.
The original nuisance constraints remain

  Q(y)>0, sum_y Q(y)=1;
  D_k(y)>0, D_k(y_ref)=1 (1<=k<=D);
  P_j(y)=Q(y) product_k D_k(y)^binom(n_j,k)
                 K_(b_j)(y) / Z_j.                                 (13)

Every row is a full strictly positive normalized distribution. Put
V_jk=binom(n_j,k), 0<=k<=D. Assume the actual GOOD schedule condition
b notin col_R V. With integer V,b this agrees with the rational column test.
There exists a rational vector w with w^T V=0 and w^T b=1.
In particular sum_j w_j=0.

Consider the complete positive data Pstar_j(y)=1/s in EVERY row.
For any interior lambda(t)=(t/2,...,t/2), 0<t<1, choose Q=1/s and all
D_k=1. Its row laws are K_lambda(t)/s or K_(rho lambda(t))/s:
mean K=1 makes these exact normalized laws.
Both converge to1/s as t tends0, because the only constant source is h=0.
Thus these are genuine original-family feasible positive arrays tending to Pstar.

For clarity, nonattainment is established directly on (13), without
borrowing an unproved lambda inverse or re-proving a general closure theorem.
If Pstar were reproduced by some interior K with ANY permitted positive
Q and D_k, form the exact cross-state log contrast and use w:

  sum_j w_j log(P_j(y)/P_j(y_ref))
    = log((T_rho K)(y)/K(y))
       -log((T_rho K)(y_ref)/K(y_ref)) =0.                            (14)

Every nuisance term cancels, including the original row normalizers.
Thus T_rho K=cK for some c>0.
Since T_rho has strictly positive stochastic rows and T_rho 1=1,
its positive eigenvector has to be constant:
at the maximum and minimum of K, weighted averaging gives c<=1 and c>=1;
if K is nonconstant, strict positivity makes both inequalities strict,
a contradiction. Mean1 then gives K=1, which Section5 excludes from calF.
Therefore Pstar is NOT realized by the original open-parameter family.

Under the previously used literal row projective metric
dist(P,P')=max_j[max_y log(P_j/P'_j)-min_y log(P_j/P'_j)],
continuity on positive finite arrays gives dist(P(t),Pstar)->0.
Consequently

  inf_(original actual calF and ALL allowed Q,D_k) dist(P,Pstar)=0,
  but that infimum is NOT ATTAINED by an original admissible model.    (15)

This holds for every such fixed known positive T_rho and good schedule.
It is not merely a restricted-family counterexample chosen arbitrarily:
the family, controls, normalization, nuisance quantifiers and data in (15)
are those of the restored C22/C23/C26 finite carrier.
The bad-schedule case is outside this claim. There is no conclusion here
about best-fit attainment for each other data table, a preferred physical
regularization, real precision/sample cost, or a parameter estimator.

## 7. Source ledger, actual reading, and what was not admitted

A. Previously owned C26 original provenance:
Source617d4013a72cb3985be0dce93fb7e83b7cce28a8,
research_notes/divisor_extrema/20261017_c26_returned_controls_drift_identifiability.md,
11047B/df8fbd48693890d63ea3cae5cd46d88f9ebf8ebbaf9fc79a5a71eb5f1ffee161/
12e40af5ff8378e219812189bfaa3ad45a85ee02.
Its genuine whole reading was already completed before my original C26 review.
This phase recovered only the needed reference lines from my own original raw.
No new original-C26 whole, compare, experiment or registration was invented.

B. Exact actual citation chain, each newly personally full-read once in
an untruncated immutable managed response, with own UTF8 SHA/blob/URL binding:
- C25 Sourcef2e46a25194fc89cd540d7e87f7108b4b1f06e28,
  research_notes/divisor_extrema/20261016_c25_structured_drift_multilevel_identifiability.md,
  9923B/b5e40d8d39ac221936e6996da4095699ecde42eb1afc34aa22f93fe844a242fb/
  1593a20391f08cb738d95048ab4ae7272000c507.
- C24 Sourcead64fb86b1dd3df173a47c2fb2e95f932c5b54a1,
  research_notes/divisor_extrema/20261015_c24_bounded_drift_inverse_certificates.md,
  11829B/99d7d2d426f9590c2aa0d8199ce3d89b34d62d58b95efc355d613403da705898/
  5eb2820e205855e8fea75781b20a4db23e15858d.
- C23 Source87577d0e11761c50d358aa8c804bb62c3394e6ee,
  research_notes/divisor_extrema/20261015_c23_two_level_blind_reference.md,
  9623B/dfa77387eba6b61017e34bce5ff94d401a16cbb667277ca9aad7b78414fe4d14/
  2e5994baa4e4d6ee16b3aa85e1cbd2f6647a9892.
- C22 transcription Source15dd9dc4beb060eeb3e76f13fa481486293f1100,
  research_notes/divisor_extrema/20261014_c22_seventh_order_parameter_reconstruction.md,
  13359B/c84fe60e7e9822eb3e3a03e71abb4ccba00844da1104865415afe56a372ef9cd/
  bd6fda0b3cf249dcf769cf17ec318e8894abdc03.

The actual immutable URL for each is
https://github.com/awdawmip/enterprise-math/blob/{Source}/{path}.
The original args and ENTIRE managed results are durably preserved in this
directory as ORIGINAL_EXACT_C25_IMMUTABLE_INTAKE_ENTIRE_RESULT.json,
ORIGINAL_EXACT_C24_IMMUTABLE_INTAKE_ENTIRE_RESULT.json,
ORIGINAL_EXACT_C23_IMMUTABLE_INTAKE_ENTIRE_RESULT.json and
ORIGINAL_EXACT_C22_TRANSFER_IMMUTABLE_INTAKE_ENTIRE_RESULT.json.
These are reading records, not newly performed original commit comparisons.

C. Already genuinely accepted downstream interfaces, personally whole-read
and Source-bound, are honestly reused:
- Good schedule/model:17238 at c1c633fec98a2e5ce02e93972045551ec662b33f,
  research_notes/owner_goal_20261017/c26_returned_control_schedule_criterion_4a56e9/C26_ARBITRARY_RETURNED_CONTROL_SCHEDULE_DRIFT_ALIAS_IFF_AUTHOR_COMPOSE_APPENDIX_V1.md;
  17238B/e9936a2f886d866339364acc5526b3d6945539e199142755112983bfa7fb6427/
  e292a9a04f0fa5aaab051dca325cb7d794f219a4.
- Actual positive-image interface: my14637 at
  b61a68c6bbf114e8c133f4fcdd409f40092c1408,
  research_notes/owner_goal_20261017/c26_finite_image_consumer_bff6dc/C26_POSITIVE_DATA_IMAGE_AND_NORMALIZED_RECOVERY_APPLIED_CONSUMER_APPENDIX_V1.md;
  14637B/5db4457c58034578da707221ee0ef80fa7b646ff236d014e032a50066d8ba01e/
  423f496e2a9d265ef19f2860d2210b863c71fb5a.
- General arbitrary-F closure was separately proved by9F7 at
  3aac62eaf614e2fa00ac6c21890a94cef8072260,
  research_notes/owner_goal_20261017/c26_restricted_fit_closure_9f7a5c/C26_RESTRICTED_TARGET_RELATIVE_CLOSURE_AND_ACTUAL_BEST_FIT_ATTAINMENT_AUTHOR_COMPOSE_APPENDIX_V1.md;
  16883B/c7b210f80d6a8b80643dd7cc33ea8b88711fbb7432366be96568d91e8e4f2996/
  ba20fbe7776898854cb8549238d299c73aef09bf.
  My genuine technical whole/Source18920 and9F7 ordinary2/35803 were already closed.
  It is contextual interpretation of the new actual-family result, not its
  missing actual-family definition or a replacement for proofs (6),(10),(15).

My old K-REUSE ledger had truthfully not read C24 or C22 at its creation.
They are newly read NOW; that history is not overwritten and no new K-inverse
claim or novelty is manufactured from this intake.
C25/C24/C23/C22 retain their SELF_CHECKED_UNREVIEWED/conditional status.
Reading their whole texts is NOT admitting their old experiments, BRC execution,
physical correspondence, code counts, registration, Native scope or all original
mathematical theorems. This new appendix supplies its used finite arguments.
Original session denials and registration-pending facts are not repaired by reading.

## 8. Contribution, finite stopping point, and creation context

BFF supplied the new actual-family member/endpoint/fit-consumer construction
after this bounded literal intake; private/internal construction is NONZERO.
Old source-map and known-control credit belongs to the original C22/C23 authors;
4A's schedule theorem, my prior positive-image/best-fit contributions and9F7's
general closure theorem retain their separate scope and contribution.
No original source author or reviewer supplied a new proof repair here.
A/CF/4A were not asked for formulas, proofs or new construction for this branch.

Root asked for an actual orphan entry and permitted exact citation following,
but supplied zero mathematical formulas, construction or votes.
9F7 received only the restored input-definition/source-pins metadata before
Root's CP3 mathematical-pause update arrived; I then explicitly queued it as
metadata only and requested no body intake, proof, repair or provisional vote.
No new consumer argument was shared with a prospective independent reviewer.

This is one finite consumer. It closes the literal input gap in writing
"K_R belongs to the original F" and supplies a concrete original-family
nonattainment case; it does not classify every best fit or every endpoint
parameter fiber. It does not extend the original lambda domain, reopen Student
column/arc/coefficients, alter old C26 sources, or reanimate LC/hdiv/P11/M7/R101/
883 STOP/budget branches. No external literature search, scientific code,
sampling, enumeration, numerical computation, Native/formalTask, helper,
new identity/RA/budget or remote Source mutation occurred for this proof.
Only exact managed source reading and administrative UTF8/file/hash IO ran.

At this artifact's creation the new body's complete actual selfreading and
external oncefreeze are subsequent observations, not prospectively asserted
by this paragraph. New author Source and independent whole remain pending.
All upstream creation words/status and original attachment-vs-transcription
identities remain unchanged. Parent Goal remains OPEN.

Global-Knowledge-Sync: main@67a02007 / GLOBAL_KNOWLEDGE_V1
