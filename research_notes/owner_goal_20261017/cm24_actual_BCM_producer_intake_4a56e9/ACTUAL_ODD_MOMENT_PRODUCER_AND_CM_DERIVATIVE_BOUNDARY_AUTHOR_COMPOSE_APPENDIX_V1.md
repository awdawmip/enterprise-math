# The literal odd-moment producer and the CM derivative boundary

Status: AUTHOR_PROVED_UNREVIEWED / RESULT_ONLY_STANDARD_COMPOSE.
This is one noncanonical appendix in the existing fixed-connection/finite-CM
family. It repays the producer identity left conditional in the recent
integration; it does not claim a new paper, Tool, Task, novelty, or Source
acceptance. The author is the same warm EM-P11-4A56E9 actor, with current
activity 38/214. No helper39, scientific program, prime query, budget or
identity reset, or remote write was used for this proof. Author construction
in this precise unit is NONZERO. Root supplies routing, not a mathematical
vote or construction.

## 1. The gap and the literal inputs

The missing statement is about the independently prescribed odd moment
observer, not about a scalar defined to equal a desired derivative. Its
working definition is in the old 16666-byte member

  cm24-bilinear-cm-boundary-dictionary-20261012/
  FIXED_C_COEFFICIENT_BOUNDARY_AND_GENUINE_ODD_SOURCE.md.

The original member is directed collaborative working research, with its
original scalar comparison OPEN. Its labels PROVED and its checker results
are not accepted premises here. Its section 6 refers to a preceding
15944-byte member for the actual V_k and s_O:

  cm24-gauss-weighted-terminal-comparison-20261012/
  GAUSS_WEIGHTED_TELESCOPERS_AND_EXACT_PREFIX_RESIDUAL.md.

Both members were actually read completely in this intake. Only their
literal constructors are consumed. Every recurrence and terminal correction
needed below is independently proved from those constructors. No old
checker was read or executed; no neighboring member's proof is silently
consumed.

Fix a prime p=6m+1 with p congruent to 13 or 19 modulo 24, put N=3m, and
work in F_p. Then m>=2, N=(p-1)/2, and p>5. Use the exact already accepted
finite Gauss normalization

  a_i=(1/6)_i(1/3)_i / ((1/2)_i i!),  0<=i<=m,
  A(z)=sum_(i=0)^m a_i z^i,
  g=binom(3m,m),  A(1)=1/g,  A(1/2)=0.

Here g and every a_i through i=m are units. The first numerator zero in
(1/6)_i occurs at i=m+1, and the relevant denominator factors are all
units. In particular

  a_(k+1)/a_k =
       (k+1/6)(k+1/3) / ((k+1/2)(k+1)).                 (1)

The identities A(1)=1/g and A(1/2)=0 are honest reuse of the complete
15834-byte CM0 input, not claims proved again by this appendix. Also
2^N=-1 in these p classes, as paid in that input. Put

  rho(x)=x(4x-3)^2,
  f_k(x)=(1-4x)^2 rho(x)^k.

For a polynomial f=sum f_l x^l of degree at most N-1 and
c in {1/2,1,1/4}, the old, literal odd moment is

  J_c(f)=sum_l f_l c^(l+1)/(2l+1).

All its denominators are units: 1<=2l+1<=2N-1=p-2. The actual source
and affine-weighted total are

  V_k=8 J_(1/2)(f_k)+(8/3)J_1(f_k)+(20/3)J_(1/4)(f_k),
        0<=k<=m-1,
  L_O=sum_(k=0)^(m-1) a_k(k+1/6)V_k.                    (2)

Indeed deg f_k=3k+2<=N-1. No V_m is defined. For c=1 or 1/2 put the
independent coefficient moment

  E_c(A)=sum_(i=0)^m a_i c^i/(2i+1).

Its largest denominator is 2m+1<p. The actual old boundary observer is

  B_CM = L_O + 2a_m16^m/27 - 4/(3g)
                    - (4/81)E_1(A) - (8/27)E_(1/2)(A). (3)

This definition uses the actual V_k moments and a separately specified
top correction. It contains neither A'(1/2) nor a target discrepancy.

The assertion repaid here is B_CM=(2/3)A'(1/2). It will not identify this
B_CM with the different prefix quantity B_O in old equation (24), fill
the independent kappa constructor, or prove that scalar equation.

## 2. A polynomial certificate from the actual moments

Let E=2x partial_x+1. For an integer 0<=k<=m-1 define the polynomials and scalars

  D_k=3(2k+3)(6k+7)(6k+11),
  B_k=54(2k+3)(k+1)(2k+1),

  R_k(x)=r_0+r_1 x+r_2 x^2+r_3 x^3+r_4 x^4,
  r_0=18(2k+3)(k+1),
  r_1=-9(52k^2+132k+85),
  r_2=12(180k^2+464k+299),
  r_3=-16(6k+7)(42k+61),
  r_4=192(2k+3)(6k+7),
  Q_k(x)=rho(x)^k(4x-3)R_k(x).

These are polynomial identities, reduced in F_p only after forming
their coefficients. Differentiation gives exactly

  E Q_k = D_k f_(k+1) - B_k f_k.                       (4)

Here is a coefficient-level verification, rather than an invocation of
the old recurrence. Since x rho'/rho=3(4x-1)/(4x-3), the left side,
after factoring rho^k, is

  2x(4x-3)R_k' + 3(2k+1)(4x-1)R_k.

A monomial r_j x^j contributes
4(2j+6k+3)r_j to x^(j+1) and -3(2j+2k+1)r_j to x^j.
Substitution of the five displayed coefficients gives, in ascending
orders 0,...,5,

  -B_k, 9D_k+8B_k, -96D_k-16B_k,
  352D_k, -512D_k, 256D_k.

These are precisely the coefficients of
(4x-1)^2[D_k x(4x-3)^2-B_k]. No inverse in k is used.

The endpoint values of the same polynomial are

  R_k(1/2)=-(36k^2+96k+67)/2,
  R_k(1)=54k+77,
  R_k(1/4)=-4.                                         (5)

For 0<=k<=m-2, deg Q_k<=3k+5<=N-1. For any polynomial Q in this
degree range, the literal J formula gives J_c(EQ)=cQ(c).
Consequently, applying the three weighted moments in (2) to (4)
gives the independently proved interior row

  D_k V_(k+1) - B_k V_k = s_O(k),
  s_O(k)=2^(1-k)(36k^2+96k+67)+144k+656/3.              (6)

In detail, rho(1/2)=1/2 and rho(1)=rho(1/4)=1, so the endpoint sum
is

  -4*2^(-k)R_k(1/2)+(8/3)R_k(1)-(10/3)R_k(1/4),

which is exactly the displayed s_O(k). This proves that the old
prescribed s_O is the forcing of the actual J moments. The statement
is not assumed from the unreviewed predecessor.

## 3. The top row and its genuine characteristic-p correction

At k=m-1, the finite-field value of k is -7/6. The polynomial
certificate still holds without dividing by D_k, and its coefficients
reduce to

  D_k=0, B_k=8,
  R_k=32x^2-16x-2,
  Q_k=rho^(m-1)(128x^3-160x^2+40x+6).

Thus deg Q_k=N and its leading coefficient is

  q_N=[x^N]Q_k=128*16^(m-1)=8*16^m.

Although J_c is not defined on an arbitrary x^N term, E kills precisely
that term since 2N+1=p. Hence E Q_k has degree at most N-1, and direct
use of the legal J definition proves

  J_c(E Q_k)=cQ_k(c)-q_N c^(N+1).                       (7)

There is no division by p. The weighted missing-endpoint coefficient is

  8(1/2)^(N+1)+(8/3)+(20/3)(1/4)^(N+1)
       =8(-1/2)+8/3+(20/3)(1/4)=1/3,

using 2^N=-1 and 4^N=1. Applying (7) and the same endpoints (5)
therefore gives the actual terminal row

  -8 V_(m-1) = s_O(m-1) - (8/3)16^m.                  (8)

This is a consequence of the original finite moments. It neither
introduces V_m nor treats a formal zero coefficient multiplying an
undefined moment as zero. The full top correction is present.

## 4. Endpoint-correct finite telescoping

Put q_k=(k+1/6)(k+5/6) and define only the legal finite fluxes

  G_k=-2a_k q_k V_k,  0<=k<=m-1.

On the interior range 0<=k<=m-2, equations (1) and (6) imply

  G_(k+1)-G_k
    =a_k(k+1/6)V_k - a_(k+1)s_O(k)/[54(2k+3)].          (9)

To check the simplification, q_(k+1)=(k+7/6)(k+11/6) and

  D_k=108(2k+3)q_(k+1),
  B_k/D_k=(k+1)(k+1/2)/q_(k+1).

The homogeneous difference in (9) is
-2a_k[(k+1/6)(k+1/3)-q_k]=a_k(k+1/6).
The remaining coefficient is -2a_(k+1)q_(k+1)/D_k.
All divided factors in (9) are units; 2k+3<=2m+1<p.
Nothing requires dividing the vanishing D_(m-1).

The actual initial polynomial is f_0=1-8x+16x^2. Thus

  J_(1/2)(f_0)=7/30, J_1(f_0)=23/15,
  J_(1/4)(f_0)=2/15,
  V_0=308/45, G_0=-154/81.

For the last, separately legal row, coefficient reduction gives

  q_(m-1)=1/3,
  a_m/a_(m-1)=15/2,
  m-1+1/6=-1,
  54(2(m-1)+3)=36.

Writing V=V_(m-1), s=s_O(m-1), the actual last remainder is

  a_(m-1)(-1)V + G_(m-1) - a_m s/36
       =-a_m(8V+s)/36
       =-2a_m16^m/27

by (8). Sum (9) over 0,...,m-2 and append this explicitly computed
last remainder. The complete finite identity is

  L_O=154/81 - 2a_m16^m/27 + F_O,
  F_O=sum_(i=1)^m a_i s_O(i-1)/[54(2i+1)].             (10)

No undefined upper flux G_m was used. The separately prescribed
correction in (3) is exactly the one forced by the actual moments.

## 5. Evaluation of the prescribed forcing and the producer identity

The literal forcing (6), with k=i-1, gives the exact rational identity

  s_O(i-1)/[54(2i+1)]
     =4/3 + 4/[81(2i+1)]
       +2^(-i)[(4/3)i+2/9+8/[27(2i+1)]].              (11)

For example, its nonexponential numerator before division is
144i+224/3; its exponential numerator is
2^(2-i)(36i^2+24i+7). Clearing the common denominator verifies
(11) directly. All denominators occurring at 1<=i<=m are units.

Summing (11) with the actual a_i gives

  F_O = (4/3)(A(1)-1) + (4/81)(E_1(A)-1)
      + (2/3)A'(1/2) + (2/9)(A(1/2)-1)
      + (8/27)(E_(1/2)(A)-1)
      =4/(3g)+(2/3)A'(1/2)
          +(4/81)E_1(A)+(8/27)E_(1/2)(A)-154/81.        (12)

The derivative term uses
sum_(i=1)^m i a_i 2^(-i)=A'(1/2)/2. The four omitted i=0
constants sum to 4/3+4/81+2/9+8/27=154/81. No value is fitted
from a target scalar or from tau.

Combine (10), (12), and the independent definition (3). This proves

  B_CM=(2/3)A'(1/2).                                   (13)

It is the literal old producer, with its actual moment and top
correction, that has this value. The proof does not redefine B_CM.

For the precise, already whole-consumed modern interface, let
u=V'(1/2) with the accepted connection V(w)=gA(1-w). The accepted
CM0/simple-zero result gives u!=0, so

  B_CM=-2u/(3g) is a unit.

For the current P20431 product-defined
tau=-C_*u/4, with that paper's unchanged independent C_*, equation
(13) also yields C_*B_CM=8tau/(3g). This last consequence consumes
P's actual product definition. It does not independently authenticate
every older finite-integral or double-prefix definition of tau.
No assertion that C_* itself is nonzero is made.

## 6. Source custody, complete reading, and actual contribution history

Both new old inputs are members inside immutable containers, not
standalone files fetched at fictitious Git paths.

Input I:
- Repository awdawmip/enterprise-math.
- Container Source e899e041a8c303626a0baf684c5788932a2e95d3.
- Container path:
  driver_reviews/mcp/MCP-cd5eefdde49843898b2a70c1af94d8dd/cbfd584a49eaf28cab04/CM24_FIXED_C_UNIT_COMPLETE_FROZEN_SOURCE_BUNDLE.json
- Container 61712 UTF8 bytes; SHA256
  64f0b4984bfa46640b36b9a64a08e931765f21b9d68bfd778488536cd9521b95;
  GitOID b0fbf6adf43d648263744b82d121c1ba872d47d5.
- The exact 16666-byte member named in section 1 has SHA256
  22da57abfeb18af76dcd0002a0c07c1f169e1d73720fe7e589701a385d084388
  and GitOID c092e6abb38127fbc52aa0971bc319178be8df3b.
- Actual local complete semantic reading: opening and all eight sections,
  tool chunk a0e906, 4167 tokens, with no truncation.
- One personal managed github_fetch_file fetched the fixed container.
  Its complete original arguments and entire result were saved before
  assertions. Decoding exactly matched the already read local member.

Input II:
- Container Source 1558a5de9af0f6336d2091e7f30627754f3763a5.
- Container path:
  driver_reviews/mcp/MCP-cd5eefdde49843898b2a70c1af94d8dd/a397b754917bb34480b0/CM24_NEW_FLUX_AND_WEIGHTED_UNITS_COMPLETE_FROZEN_SOURCE_BUNDLE.json
- Container 120248 UTF8 bytes; SHA256
  cf253c72a54b7bd21a1520f8038c088ef673d8e3a39638f1601434f9a672fc41;
  GitOID 9486a9337e5ef9a085c914937264b6beaabd0698.
- The exact 15944-byte member named in section 1 has SHA256
  a36dd3154d6a599d2a92703c3420d08e834c9e868bc4134ec4fbf6907a0f2eac
  and GitOID 407e45c376ba715fd0dd6b4e3d46879dc045a490.
- Actual local complete semantic reading: opening and all seven sections,
  tool chunk a26160, 3986 tokens, with no truncation.
- One personal managed github_fetch_file fetched the fixed container
  concurrently with the local whole read; subsequent exact decoding
  matched the complete local bytes. No Source compare is newly claimed.

Container gzip/base64 decoding, length/SHA/OID checks, and exact member
extraction were custody operations, not scientific verification programs.
Reading the selected member is not reading every other bundle member.
Neither old script, symbolic check results, nor old directed helper proof
was adopted as an independent mathematical premise.

Original complete arguments/results and the two minimal member-binding
receipts are saved beside this appendix, under the intake directory:
- OWN_EXACT_OLD_CONTAINER_SOURCE_ORIGINAL_ARGUMENTS_ENTIRE_RESULT.json
- EXACT_16666_MEMBER_OWN_CONTAINER_BINDING_MINIMAL_RECEIPT.json
- OWN_EXACT_15944_PREDECESSOR_CONTAINER_SOURCE_ORIGINAL_ARGUMENTS_ENTIRE_RESULT.json
- EXACT_15944_PREDECESSOR_MEMBER_OWN_CONTAINER_BINDING_MINIMAL_RECEIPT.json

The transport method in those saved wrappers is the supported
github_fetch_file alias. No server call_id or full original MCP namespace
is invented.

Actual already accepted interfaces reused, without a new GET or vote:
- A CM0 author15834 at Source
  1689ce708127993e6892803d3179afd4d232765f:
  research_notes/owner_goal_20261017/cm24_finite_heun_CM0_7cda51/ACTUAL_FINITE_HEUN_RECIPROCITY_AND_CM0_APPLIED_CONSUMER_WORKING_AND_CONTEXT.md
  SHA ce9384557b631c4cad9d7aa54f0a43400704726077f93f4d5dd219dcac2d2fbc,
  OID dbe6b0c0ab2fc357f54e0fe7fd7e957b6fccb73e.
- CF Gauss simple-zero author9578 at Source
  e126e291ceac1e3eacaa9734d85a25dfec2c919f:
  research_notes/owner_goal_20261017/cm24_finite_gauss_simple_zero_cf1677/FINITE_GAUSS_CM0_SIMPLE_ZERO_AND_CONDITIONAL_ODD_SOURCE_UNIT_APPLIED_CONSUMER_V1.md
  SHA 7c7e6949e69a15f1a81415d08fbc946689307d7e683c5b39addecf59c57c5532,
  OID 47ea0712a09e8678895f1c6b60b786e0a9d7b114.
- A partial P20431 at Source
  17a98a752ae6b01a28db1315db3d26dacf8c1330:
  research_notes/owner_goal_20261017/cm24_reciprocal_density_orphan_intake_7cda51/CM_RECIPROCAL_DENSITY_TERMINAL_CANCELLATION_PARTIAL_COMPOSE_WORKING_AND_CONTEXT.md
  SHA 2a3e634bb1d0cbdeba5b872a22bbe920bb19b4ac55e781aa228843c9f2a11bc1,
  OID f50e90f3a8cc26cd9a918cedfe18856036afdb7e.
This author has genuinely completed those mathematical wholes and personal
immutable Source/exact bindings. My authored older review16463 and
integration review19890 are historical work, not fresh votes on them.

The original 2026-10-12 local authors/helpers retain their original
constructor and claimed-identity credit; their native identities are
UNKNOWN in the consumed old text. This appendix makes no originality
claim over their same displayed equality. Its new contribution is a
self-contained, personally paid proof from their literal moment
constructors, including an explicit polynomial certificate and the
genuine top-row correction, for a still-unpaid reusable interface.

A and CF were contacted only for occupation/previous-coverage metadata.
A disclosed private planning associations NONZERO, no new frozen proof,
and relinquished this exact scope; she supplied only the exact predecessor
locator/pins. CF disclosed that his old16666 literal whole and later9578
consume the producer conditionally, with no personally frozen accepted
producer proof. Neither supplied this author formulas, a proof, or repair.
My own warm CM/partial/integration work and private associations remain
NONZERO; this is not cold or blind work. Root routed the finite gap
without mathematical construction. No prospective peer verdict is assumed.

## 7. Result and remaining boundaries

The complete bounded result is the actual producer identity (13), its
unit consequence using accepted simple-zero data, and the conditional
P-product pairing explicitly stated in section 5. It is a standard
finite polynomial/moment composition in the same family.

The old scalar comparison remains OPEN. In particular:
- no independent kappa producer has been recovered or fitted;
- the prefix quantities B_H and B_O are not identified with B_CM;
- the old equation (24), Eq16, weighted pairing/h_div, and the LIFT and
  raw-period goals are not closed;
- the original unreviewed/directed sources, their checkers, unknown
  native identities, and registration/Source histories are not promoted;
- no physical readout, Native propagation, numerical campaign, whole
  container kernel, or all-prime result is claimed.

This manuscript is prepared for a genuine nonauthor technical whole.
It is not that peer's report and is not yet Source-published or accepted.
The author will actually read the complete saved manuscript and freeze
its exact bytes/pins once after that reading. Subsequent Source or peer
facts must be recorded separately without changing these creation words.
