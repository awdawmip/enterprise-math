# C298 — Shared denominator compression: exact 125-path dyadic sign termination

**2026-10-25. AUTHOR EXACT; NOT SOURCE-CLAIMED, NOT DRIVER-REVIEWED, NOT ADMITTED.**

## Frozen question and provenance

For the C195/H168 79-positive-rational-branch auxiliary function f(v)=F(v)/2^128, continue the exact C297 dyadic sign-certification argument for 125 affine paths v_i(t)=w_i+t d_i on their C293 strips I_i=[k_i/2^24,(k_i+1)/2^24]. Its prior published *author-level* bound was P=660b+73527+134 for a non-root dyadic point t=k/2^b. Reuse, without promoting, C297's rigorous all-strip outward integer interval width less than 2^134, valid for any P>=0.

Provenance: parent C297 author commit c016c725739440b4a9d255169631a38f5ced6c10 (the parent of this branch); canonical account knowledge main ee7806e5717ca691678361ef779ed98115813649; Enterprise Math current source main b2049e0f8fc7c595260b4aedae50b16629523af3; exact frozen inputs C275 original 79-node evaluator, C284/C288 125 path extraction, C293 24-bit strips, and C297 source code/audit. All auxiliary, not native signed GF(2)-BRC/X6 or its P000 three-dimensional research slice.

## Theorem

For each frozen strip there are integer polynomials A_i,D_i with D_i(t)>0 on I_i, f(v_i(t))=A_i(t)/D_i(t), deg(A_i-D_i)<=deg(D_i)<=354, and D_i(t)<2^13799 for all real t in I_i.

Therefore every **non-root** dyadic t=k/2^b in its prescribed strip has its strict f(v_i(t))-1 sign certified by the existing positive outward integer evaluator at

**P = 354 b + 13799 + 134.**

The inherited C297 sufficient precision P=660b+73527+134 is reduced in both degree coefficient and height constant. For b=512 the respective conservative settings are P=195181 and P=411581. These are worst-case sufficient precision formulas, not observed required precision, performance guarantees, or root existence theorems. At an exact root no strict sign exists, so termination for that equality case is not claimed.

## Proof (shared primitive denominator factorization)

Every fixed or moving branch is a positive rational coefficient times explicit rational polynomial factors. On each strip all gap denominators have constant sign; the quadratic factors (2-p(t)^2),(3-p(t)^2) stay positive because the valid path coordinates remain strictly in (0,1). Orient each rational denominator positive. For each factor choose an exact positive integer common multiplier of numerator and denominator so it has integer-coefficient polynomials N_jl(t)/B_jl(t), with deg N_jl<=deg B_jl; this last property holds for the C275 fixed, moving and moving-base formulas.

Write B_jl=c_jl q_jl, where positive integer c_jl is its coefficient content and primitive integral polynomial q_jl is positive throughout I_i. The 79 term coefficients are rational C_j. Define scalar s_j=denominator(C_j) * product_l(c_jl) and S=lcm(s_1,...,s_79). For every primitive polynomial coefficient vector q set e_q=max_j multiplicity_j(q), retaining multiplicities **within** a term. Put D_i=S * product_q q(t)^e_q.

By construction each term's denominator divides D_i in Z[t]: s_j|S and each primitive factor exponent is dominated by e_q. Hence the product of D_i with each original term is an **integer polynomial**, so their sum A_i is integral. Also deg(A_i)<=deg(D_i) since no original term numerator factor has greater degree than its paired denominator factor.

The union of possible variable polynomial denominators has 300 fixed-moving linear node gaps (75 times 4), six unordered moving-moving linear gaps (12 ordered occurrences coalesce pairwise), and four moving-base degree-12 factors. Thus deg D_i<=300+6+4*12=354. Any constant path factor or coincident primitive polynomial can lower this degree. The exact replay finds degree 354 in 124 paths and 267 in one.

For t in [0,1], every integral q obeys |q(t)|<=sum_absolute_coefficients(q). Thus 0<D_i(t)<=M_i, where M_i=S * product_q (sum_absolute_coefficients(q))^e_q is an explicitly computed integer. The replay performs all 125 exact primitive factorizations and integer-LCM calculations; max bit_length(M_i)=13799, hence D_i(t)<2^13799 throughout the strip.

Let d_i=deg D_i. At t=k/2^b, provided f(v_i(t))!=1, the value 2^(d_i b)(A_i(t)-D_i(t)) is a nonzero integer, so |A_i(t)-D_i(t)|>=2^(-d_i b) and |f(v_i(t))-1|>2^(-d_i b-H_i), where H_i=bit_length(M_i). By the inherited C297 all-strip positive outward enclosure its integer width is strictly <2^134, or actual width <2^(134-P). Taking P=d_i b+H_i+134 makes this width smaller than the true threshold gap, so an interval enclosing f cannot also contain 1. The uniform maxima d_i<=354 and H_i<=13799 finish the proof.

No equality or cancellation between distinct physical/BRC provenance states is inferred by the rational-polynomial common denominator. It is only an arithmetic representation of this **positive auxiliary readout**.

## Executed exact verification and limits

Run the companion stdlib Python file C298_SHARED_DENOMINATOR_COMPACT_REPLAY.py in the existing research_handoffs folder, beside the inherited C275, C284, C288, C293, C297 inputs. The script validates the frozen C293 record SHA256 and C284 path certificate, reconstructs all 79 branch denominators independently from the original frozen C275 formulas, proves each term denominator divides D_i in Z[t], computes all 125 degree/height bounds and writes replay audit plus 125-path rows.

Observed exact results: 125/125 shared-denominator divisibility checks; degree distribution {354:124,267:1}; global bit-height bound 13799; independent source-C275 full-Fraction integrality crosschecks for six predetermined dyadic interiors of paths 0,8,24,64,96,124 all pass. The six sampled checks are *not* a universal substitute for the factored all-path argument. No floating tolerance is used for any mathematical decision. Original C297 continuous width is a frozen logical dependency and is not re-proved in the C298 compact replay.

## Next unresolved question

C299: Determine the genuinely reduced A_i/D_i degrees via exact polynomial gcd, rather than the shared-denominator upper degree; attempt stronger height bounds for primitive **reduced** denominators. Preserve independent BRC signed phase/port/provenance and future-operation fidelity questions; auxiliary continuity does not confer a native six-dimensional Cell theorem.

## Research control boundary

The native task query presently returns CONTROL_QUOTA; native Researcher session registration returns STATIC_READONLY_SCOPE_DENIED (operation_sent=false). Real-time active owner has not been established and there is no official CLAIM, Source Result, Driver review, or admission. This GitHub branch is an independently saved, explicitly noncanonical **author-level** mathematical handoff, not a bypass of native admission.
