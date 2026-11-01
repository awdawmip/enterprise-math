# EC49DC-1 — Generic-weight robustness of the all-h signed-X6 positive-BRC theorem

2026-11-01, **AUTHOR_ANALYTIC_PROOF / TWO_WEIGHT_EXACT_CHECKS_PASS / PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED**. Reuses EC49DB's source pins, all twelve signed primitive X6 directions, full ordered A/B tags, return-suffix alphabet a,b,c,d,e and separate W0/W1/count BRC channels. No native CLAIM, accepted Result or independent mathematical review.

## Parameterized theorem and rank fields

Let x=(x1,...,x6), y=(y1,...,y6) have **strictly positive real** components and let all negative-step BRC weights equal 1. Under arbitrary real weights we consider the **real-linear** rank of the future-observer matrix. On the subfamily of *positive rational* weights the entries are rational, so the same formula holds for **rational-linear** rank, matching the original Enterprise Math category. This is not a claim that arbitrary irrational weights yield identical minimum rational-linear memory.

For each of the same nine stored EC49DB literal seed path/return-suffix/tag matrices M_j(x,y) define its determinant polynomial Δ_j(x,y). For the following four tag classes define Γτ(x,y) as the 3×3 determinant with three columns (product of x weights in g, product of y weights in g, 1), using each row's three fixed four-positive-letter gadgets:

| Tag | Three gadgets |
| --- | --- |
| Neither | 1111,3111,2311 |
| B only | 3211,2111,3221 |
| A only | 1112,1122,3112 |
| Both | 1211,2121,3121 |

Let

\[
Q(x,y)=(x_1-x_3)(y_2-y_3)-(x_2-x_3)(y_1-y_3)
\]
and
\[
P(x,y)=Q(x,y)\prod_{\tau}\Gamma_\tau(x,y)\prod_{j=1}^{9}\Delta_j(x,y).
\]

**Theorem:** The set **U={(x,y)∈(R>0)^12 : P(x,y)≠0}** is a nonempty, relatively Zariski-open and Euclidean open dense subset of the strictly positive weight orthant. For **every** (x,y) in U and **all integers h≥2**, the exact-h and cumulative-(1..h) returning-suffix observers attain full rank at first literal length **n_sat(h)=2h+8**, with the EC49DB defect table (12/12 at defect0, 15/18 at odd defect, 18/18 at even-positive defect) and global ranks

\[
\dim O_{=h}=\frac{3(11h^2+15h+8)}2,\quad
\dim O_{\le h}=18h^2+24h+12.
\]

For rational weights, U∩Q>0^12 inherits the identical conclusions over Q. U is a sufficient parameter set; conditions P=0 do NOT establish failure of full rank.

## Analytic proof

**Algebraicity.** Each literal native signed-X6 path's BRC channel weight is a monomial in the x_i or y_i with nonnegative exponents; future tag tests are weight-independent Boolean selectors. Every 3-channel observation-matrix entry is 0 or a monomial, so every Δ_j and Γτ is a polynomial with integer coefficients. At the EC49DB reference x=(2,3,3,2,1,1), y=(3,2,3,2,1,1), all nine Δ_j are nonzero modulo prime 1,000,003 by an actually executed literal-path checker, the four Γτ equal (-216,+216,+216,+216), and Q=1. Thus P is not the zero polynomial, its zero set has empty interior, and U is nonempty and dense as claimed.

**All interior fibers.** Exact EC49DB gate insertions before -E3, between -E3 and +E3, and neutral horizon shifts preserve the prefix's ordered A/B and all future-final tags, for every possible weight choice. The added positive letters multiply *all columns* in each BRC row by a fixed strictly positive monomial g0 (or g1), and the count coordinate by 1. Adding suffix compensation a,e,b or a neutral ae has the same multiplicative property. For any of the nine base minors, the derived 3r×3r minor equals

\[
\det M_{\rm lift}=(g_0g_1)^r \Delta_j(x,y),
\]

where g0,g1>0. The nine seeds supply all interior defect/parity/sign cases for all h≥2. Their nonvanishing on U proves full interior rank; the six-feature future-safe upper bound depends only on the A/B transition structure, not weights.

**Entire extremal boundary.** The negative E1-edge and positive E1 corner families in EC49DA use exactly the fixed four gadget triples above. Each block is multiplied by positive monomials contributed by endpoint runs and tag-safe suffixes, hence its determinant is Γτ times a strictly positive factor: all 12 boundary directions exist when Γτ≠0. On the positive mixed E1/E2 edge EC49CZ replaces a tag-safe positive E3 neutral pair in three variants: (X,Y,1), (X·x1/x3,Y·y1/y3,1), (X·x2/x3,Y·y2/y3,1). Their determinant equals **XY·Q(x,y)/(x3y3)**, which is nonzero on U. Four disjoint tag blocks furnish a 12×12 minor at every extreme fiber for every h.

**Earliest length independent of weights.** At D=(-2h,0,0,0,0,0), only the complete suffix e^h returns. At n=2h+6, for the final tag containing both A and B, prefixes can have at most three positive E1/E2 letters. There are only two possible positive patterns, 121 and 212. Whatever the positive weights, the three-channel observations for this tag lie in a span of dimension at most two, while the other three tags supply at most three dimensions each. The fiber rank is therefore at most 11, not 12. Native neutral-pair padding excludes earlier even lengths, and parity excludes odd lengths. Thus n_sat(h)≥2h+8 for every parameter point, matching the construction.

This is a generic positive-weight **abstract observer** theorem. Neither P000 nor the ACTIVE worldview has changed; the result does not establish native phase interference, arbitrary two-dimensional physical slices, or heartbeats.

## Executed exact validation and next

The executed Python 3 standard-library **VERIFY_EC49DC_WEIGHT_OPEN.py** reuses the actual EC49DB seed data and executable checker. Reference weights give Q=1, Γ=(-216,216,216,216). A second explicit point **x=(2,3,5,2,1,1), y=(5,4,5,2,1,1)** gives Q=3, Γ=(-3000,3600,3600,3600). For each point all 9 literal seed minors are nonzero mod 1,000,003 and all **1,298** lifted interior minors for h=2..12 pass. This demonstrates two members of U; the universal and generic claims follow from the algebraic proof, not a sampled weight grid.

Next: independent symbolic/Lean formalization and exact certificate-size analysis; determine whether specific P=0 parameters genuinely lose observer rank or merely break the particular witness certificate; probe alphabet changes separately. Existing EC49DC formalization/robustness task remains open. Project status PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.
