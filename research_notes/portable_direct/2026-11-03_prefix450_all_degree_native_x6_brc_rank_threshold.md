# PREFIX-450 — Universal sharp rank threshold for native X6 BRC polynomial observers

Date: 2026-11-03, Asia/Shanghai. Author-side mathematical proof and finite exact validation, pending independent Review and Admission.

Scientific source pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. This continues PREFIX-448 (quadratic, N=q+1) and PREFIX-449 (cubic, N=q+2), with the P000 native signed-six-axis space and separately typed historical control states. Current behavior, proofs and publication policy were read at global main e9a10d92f601b57896a20ff2a70f374f2906e475 and Enterprise Math control main 9061e4ebab6b6c4aaf97d7f6bd62273d959e0bec.

## Exact population and observer

For integers q>=2, d>=0 and N>=0, consider ordered signed native X6 words of common length N, with steps among the twelve primitive signed directions ±e_i, i=1,...,6. Every word has a six-integer displacement x(w) relative to a chosen native Cell anchor, and a nonspatial history sector

r(w) = number of negative-first-axis steps in w, modulo q.

The input is a finite bag of such words, with independent positive rational weights. For every history sector r and six-variable multiindex beta with |beta|<=d, retain the joint moment

T[r,beta] = sum_{w:r(w)=r} weight(w) * product_{i=1}^6 (x_i(w))^(beta_i).

There are B_d=binom(d+6,6) monomials per sector. Rank means the rational-linear rank of the map from formal word weights to the complete q B_d moment vector, equivalently its action on differences of positive rational sources.

## Theorem 450.1 (all orders, sharp duration)

For every q>=2 and d>=0, the least common word duration for full rational-linear rank q*binom(d+6,6) is

N_min(q,d) = q+d-1.

For every N>=q+d-1 full rank is attained; for every shorter N the rank is strictly smaller.

### Lower bound: one exact polynomial annihilator

Inspect the history sector r=q-1. Its words have at least q-1 negative first-axis steps, so their total number h of negative signed steps lies in [q-1,N]. Summing the six endpoint coordinates yields

L(x) = x_1+...+x_6 = N-2h.

For N<q-1 this sector is empty. For q-1 <= N <= q+d-2, the explicitly nonzero polynomial

P_(q,N)(x) = product_{h=q-1}^{N} (L(x)-(N-2h))

has degree N-q+2 <= d, and vanishes at EVERY legal endpoint in sector q-1. Thus its coefficient vector gives a nontrivial linear dependence among the degree<=d observation rows. This proof allows any extra negative-first-axis counts congruent to q-1 modulo q; it requires no special source distribution. For d=0, only the empty-sector case applies. This establishes N>=q+d-1.

### Upper bound: explicit legal affine simplex-grid interpolation

Let Lambda_d = {alpha in Z_{\ge0}^6 : |alpha|<=d}, having B_d nodes. For every r=0,...,q-1 and alpha in Lambda_d construct an ordered word by concatenating:
(1) r copies of -e_1, then q-1-r copies of +e_1;
(2) alpha_i copies of +e_i for i=1,...,5; 
(3) alpha_6 copies of +e_6 and d-|alpha| copies of -e_6.

Every constructed word is legal, has duration N=q+d-1 and has sector r, because the tail uses no -e_1. Its displacement is exactly

x_1 = q-1-2r+alpha_1,
x_i = alpha_i for i=2,...,5,
x_6 = -d + sum_{i=1}^5 alpha_i + 2 alpha_6.

Hence x=A alpha+b_r with det(A)=2, so all B_d sector endpoints are distinct and form an invertible affine image of the integer simplex grid Lambda_d.

The evaluation map on Lambda_d is an isomorphism for rational six-variable polynomials of total degree <=d. To prove this, use the multivariate Newton basis F_beta(z)=product_i binom(z_i,beta_i), ordered by total degree and then common lexicographic tie-break. F_beta(alpha)=0 whenever |alpha|<|beta|, and at equal degrees it is zero except when alpha=beta, in which case it equals 1. Its evaluation matrix is lower unitriangular. The affine invertible substitution x=A alpha+b_r preserves degree and therefore full rank. The q history sectors give independent blocks, proving rank q B_d. For larger N append +e_1 steps to every word. Such extension preserves its sector and translates its endpoint by a fixed vector; full rank remains.

### Explicit exact determinant

With identical graded-lex orders on the B_d nodes and the monomial columns, the integer evaluation determinant of each sector construction is

D_(6,d) = 2^[ binom(d+6,7) ] * product_{|beta|<=d} product_{i=1}^6 beta_i!.

Translation by b_r gives a unitriangular action on the graded polynomial basis; the homogeneous degree-k action induced by A has determinant det(A)^[binom(6+k-1,6)]. Summing exponents over k=1,...,d gives binom(d+6,7). Monomial-to-Newton triangular transition contributes the product of the multiindex factorials. This proves a nonzero integer determinant, independently of q and r.

For q=3 and d=0,1,2,3,4, the sharp lengths are N=2,3,4,5,6, and the full observation ranks are 3,21,84,252,630. Degree 2 and 3 recover the exact duration claims in PREFIX-448 and PREFIX-449.

### Positive source and recovery scope

On the selected q B_d words, the observation matrix is invertible. Therefore different rational weight vectors on those words have distinct full moments. Every formal signed variation can be embedded as a small difference between two strictly positive rational weight bags. The result is an exact linear-rank and selected-family recovery theorem. It is not a bit-complexity bound and does not assert recovery of all arbitrary path-level provenance from moments. Selected node weights can be recovered by inverse affine change followed by multivariate Newton finite differences.

## Typed BRC consequence

For the frozen positive affine-effect BRC family, on an edge r->s with rational weight lambda>0, multiplicity m>=1 and affine x'=Ax+b, set

T'[s,beta] = sum_(edges r->s) lambda*m * sum_(|alpha|<=d) C_(beta,alpha)(A,b) T[r,alpha],

where C_(beta,alpha) is the rational coefficient of x^alpha in product_i ((Ax+b)_i)^(beta_i). Degree never increases under affine substitution, so this typed history-port polynomial observer is exactly closed under any finite positive rational alternatives and serial affine composition, with faithful control-label transitions. The original frozen interfaces used are src/enterprise_math/brc_transport.py (blob be1debe367263931bd5e93fd750be3ed54624fe1) and src/enterprise_math/brc_control_port.py (blob 44def6b8ac787e798d3cc2c6be16f873f91bdb8): BRC reuse status REUSE_APPLIED, not new tool acceptance.

## Exact certificate and scope

The companion executable Python 3 standard-library certificate tests q=2,3,4 and d=0,1,2,3,4, 45 sector matrices in total. Each integer matrix determinant modulo prime 1000000007 equals the analytic determinant formula, with every constructed word's legality, sector, duration, endpoint and distinctness checked. An independently enumerated finite domain of 42 (q,d,N) lower-bound cases checks the annihilating polynomial on all reachable sector endpoints, not just the construction. Exact Fraction arithmetic checks 51 source terms and 252 degree<=3 conditioned affine-BRC output moments against direct weighted-word propagation. The accompanying original execution log records PASS. The theorem's infinite parameter scope follows from the preceding proof; finite checks validate those instances.

The original upstream ControlPacket / EffectHistogram / MomentState Python classes were inspected at frozen blobs but not directly imported or executed this run. This is an author-side mathematical observer result, not physical heartbeat evolution or native residual attribution.

## Next discriminating unit

In an execution host with the frozen upstream module available, run unchanged ControlPacket, EffectHistogram, MomentState against q=3,d=2,N=4 simplex-grid words; compare exact direct effect-histogram evaluation, moment_action and finite serial/parallel propagation, including a mixed-axis shear. Then measure complete endpoint histogram and the q B_d sector moments by actual serialized bytes, fraction denominators and integer bit lengths. Higher-order ports are a proposed extension (original MomentState is quadratic). Preserve source pin, source provenance and separate independent review/admission.

## Research record and authority

P000 and ACTIVE heartbeat-world X6 / joint-observer constraints remain unchanged. Source behavior: Enterprise Math current control main 9061e4ebab6b6c4aaf97d7f6bd62273d959e0bec read on 2026-11-03; scientific input fixed at f42f2906d77f24085c123f3ccfe9667d41caa96d. Global control main e9a10d92f601b57896a20ff2a70f374f2906e475. Native control request status succeeded at issue 6645; dispatch issue 6646 failed with SOURCE_TREE_SIZE_LIMIT files=20001/20000, so no active owner, research-role CLAIM, Result, Review or Admission is asserted. Published GitHub research notes are not themselves formal task acceptance. No credentials or shared permissions were changed.
