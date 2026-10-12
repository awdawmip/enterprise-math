# Independent paper review of the two-index Heun and normalized CM kernel

Final verdict: PASS for the frozen finite lemmas, including the actual summand flux, modular terminal boundary, Heun equation, canonical integral transformations, full repaired Lambda functional and explicit kernel. The included OLD-R fourth-order recurrence and narrowly scoped failed ansatz proofs also pass. All seven formal inputs and twelve formal outputs match the final pin set. No mathematical correction was found. The final scalar identity (20), equivalently LIFT, remains OPEN.

Byte-review status: FINAL_FREEZE_PASS. The main paper has 19,573 bytes, SHA256 `970c8d6bce21ba1a595fc51e64cde52833bf5fdc1ed56a43215e2d6d5a5a42cd`, Git blob SHA1 `3ba693cc7166f5313b9586e702bc70831597951a`. FINAL_UNIT_PINS.json has 8,261 bytes, SHA256 `2a56ef63dbb69df5cc226b3de15fdbaadb933ba96d940ad09bd695799e63df5f`. The OLD-R helper has 7,583 bytes, SHA256 `4ebcbda95e0700587a6690ab9bb6300eba23c13eee8038f33ff02e37592b7cca`. These agree with Root's final author-freeze notification. The main paper and both helper papers are byte-identical to the versions fully read and mathematically reviewed, so their earlier paper derivations apply to the frozen bytes without semantic rereading. All formal pin entries were independently rehashed for length, SHA256 and Git blob SHA1; every entry matches. Any later semantic change requires a corresponding new review.

This is Root-authorized informal local paper preparation. Native Researcher ID and native Driver ID are UNKNOWN. The local label `cm24_forcing_peer_review` is not a registered identity and does not reuse EM-ENTERPRISE-3F2857. No native Task, Claim, identity, Source, host, accepted Result, remote operation, provider query or prime campaign was created or performed. No author checker was semantically read or executed. No prime was instantiated. All computations described below are independent paper algebra; the only local script use is byte metadata/pin generation.

The P000, Heartbeat X6/time, joint-observer and residual-fidelity contracts already read in this continuing session remain controlling. All variables, integrals, finite fields and CM extension calculations here are external finite classical arithmetic readouts. Native X6 and separately typed time remain unchanged, and no full-X6 propagation or complete-state collapse is asserted.

The full main paper and both helper papers were read. The previously reviewed forcing/four-boundary and three-integral theorems are explicit conditional premises, together with the frozen finite transport, reflection and CM0 inputs. Their earlier PASS results are not enlarged. An attempt to reuse the completed kernel helper returned `agent thread limit reached`; this bounded review therefore has one mathematical reviewer and claims no additional independent helper contribution. It is independent of the proof authors' derivations, but not blind because their papers were available. All author checker/report files in the final pin set were only hashed as opaque bytes during freeze verification; no report PASS or script execution supplies proof evidence here. The author's frozen field saying the increment was not yet reviewed records its earlier publication state; this separate final independent review supplies the later readback without changing those author bytes.

## 1. Finite connection formula and all parameter denominators: PASS

The coefficient of u^k in V_tilde(1-u) is

    (-1)^k binom(m,k)
       sum_(j=0)^(m-k)binom(m-k,j)binom(2m,j+k).

Replacing the last binomial by binom(2m,2m-k-j) makes this the coefficient of x^(2m-k) in (1+x)^(3m-k), hence binom(3m-k,m). This directly proves every coefficient of (2) over the integers, including both endpoints. No nonterminating Vandermonde parameter substitution is made.

The exact characteristic-zero ratio c_k/binom(3m,m) is (-m)_k(-2m)_k/[(-3m)_k k!], including its sign (-1)^k. Only after reduction modulo p does -m=1/6, -2m=1/3, -3m=1/2 identify it with the separate rational a_k sequence. All factorials in g=binom(3m,m) are below p, so g is a unit. The first vanishing factor of (1/2)_k has index k=3m+1; every denominator through k=m+1 is therefore a unit. The upper a_(m+1) numerator has the factor m+1/6=p/6 and vanishes modulo p, with no forbidden division.

The cubic substitution gives w=1-t^2(4t^2-3)^2. Expanding c_k[w_complement]^k yields precisely C_(k,j), 0<=k<=m and 0<=j<=2k, with n=k+j. Thus h_n=g sum_k q(k,n), and the support stops at n=3m. Y is even of degree 6m=p-1. The four stated rational endpoint values follow from w=0 there; the marked value w(a)=1/2 uses a^2=1/2 and retains CM0 as a further explicit premise.

## 2. The actual summand flux, including all support edges: PASS

In the interior, direct cancellation of the rising-product and binomial ratios gives, independently of an assumed telescoper,

    G(k+1,n)/q(k,n)
      =-(2n+1)(6k+1)(3k+1)/(3k-n+1),

    G(k,n)/q(k,n)
      =2(2n+1)(3k-n)(3k-n-1)/[3(n-k+1)].

Together with the three displayed q ratios, putting over 3(n-k+1)(3k-n+1) gives exactly the left side of (8). The author's expanded left-side rational expression has the same numerator and sign. Hence the displayed G is an actual certificate, not a conjectured existence statement.

The binomial form, rather than these interior ratios, is used at every support boundary:

* n=k-1: the sole left term is k(2k-1)a_k(-3)^(2k), and -G(k,k-1) has exactly that value.
* n=k: division by a_k(-3)^(2k), which is nonzero over the rationals, yields the two explicit cubic expressions in the paper; both are -16k^3/3-18k^2-23k/3-1. This includes k=n=0.
* n=3k+1: both sides equal 4(3k+1)(6k+1)a_k4^(2k), after the a_(k+1)/a_k ratio is used.
* n=3k+2: all q terms vanish and the only possibly supported forward G has prefactor zero.
* Below n=k-1 or above n=3k+2, all relevant binomial coefficients vanish. For k+1<=n<=3k the interior denominators are nonzero rational integers.

Thus (8) holds for all k,n>=0 with the stated conventions. Its actual binomial expression has no division by n-k+1 or 3k-n+1, so modular reduction does not use those potentially zero ratio denominators.

Summing over exactly k=0,...,m leaves G(m+1,n)-G(0,n). The lower value vanishes by binom(0,n+1)=0. The upper value vanishes modulo p by a_(m+1)=0, with all its actual denominators units. The upper endpoint generally survives in characteristic zero and is correctly not suppressed there. This proves the finite modular recurrence (9) with its actual upper boundary, independently of the differential derivation.

## 3. Heun coefficients and terminal degeneracy: PASS

For w=(1-u)(1-4u)^2,

    w'=-3(4u-3)(4u-1), w''=-48(2u-1).

Substituting these expressions into the finite Gauss pullback shows that the three cleared coefficients are respectively

    [(3/2)(4u-3)^3(4u-1)^2] * 2u(u-1)(4u-1),
    [(3/2)(4u-3)^3(4u-1)^2] * (20u^2-15u+1),
    [(3/2)(4u-3)^3(4u-1)^2] * (4u-1).

This verifies the common factor and its sign. It is a nonzero polynomial over F_p for p>=7, so rational-function cancellation is legal and proves (11); it is not pointwise division at a singular value.

Taking [u^n] gives coefficients (n+1)(2n+1), -(10n^2+5n+1), and 4n(2n-1), exactly (9). For 0<=n<3m, both forward factors are units. At n=3m, n=-1/2 modulo p; the forward factor vanishes, the middle factor is -1, and the lower factor is 4. The equation is therefore h_(3m)=4h_(3m-1), without division by its zero forward coefficient. At n=3m+1 the only remaining term contains 2n-1=p and vanishes. This certifies the endpoint and no scalar OLD-R comparison.

## 4. Canonical transforms of all three integrals: PASS

The W chain rule gives exactly

    dI_W/dt=2/(1-s)[Y/(1-t)-(1+s)/(1-t^2)].

Using sum h_n=Y(1)=1, (Y-1)/(1-t)=-sum h_n sum_(j=0)^(2n-1)t^j and (t-t^p)/(1-t^2)=sum_(r=1)^(3m)t^(2r-1) integrates to the displayed N_W.

For T, the exact chain rule is Y/[(1-s)(1+2t)]-1/[(1-t)(1+2t)]. Its non-Y remainder equals [(1+2t)^(p-1)-(1-t)^(p-1)]/[3(1-s)]. The other remainder is (Y-1)/(1+2t). Since Y(-1/2)=1, ordinary polynomial division at b=-1/2 gives its normalized primitive (1/2)sum h_n4^-n L_(2n)(-2t), with the displayed sign. Integrating the power difference gives the other two terms of N_T.

For E, elementary rational combination gives precisely [- (1-t)^(p-1)/3+4(1+2t)^(p-1)/3-(1+t)^(p-1)]/(1-s), whose primitive is N_E. Its two highest relevant polynomial coefficients cancel; in particular N_E has degree <=p-2, while N_W and N_T have degree <=p-1. Every actual log/integral denominator is in 1,...,p-1.

Derivative agreement alone would leave a Frobenius function. The numerator N_F(t)-N_F(1) gives an actual zero at t=1, reducing the possible denominator pole from p to p-1. The final constant in (13) makes the value zero at t=-1, which is z=0. Both sides have only that finite pole bound and are finite at infinity. A derivative-zero difference in F_p(t^p) cannot have a finite pole of order below p; with no polynomial part at infinity it is constant, and its value at -1 is zero. This proves the full normalized identity (13), including both terms often lost by derivative matching.

Setting t=0 and taking t=infinity gives exactly the two endpoint formulas (14). The infinity limit exists because degree N_F<=p-1<p, and corresponds to z=-1. It is not an omitted branch or an arbitrary constant.

## 5. Original pole repair and all Lambda weights: PASS

Substituting (14) into the preceding reviewed r_+,r_- gives (15) with the same signs. Applying Lambda to the repair term n(X)/(X^2-1)^3 at X=0,3,1/3 and X=zeta^-1 gives the coefficients

    c0=3(9a+5)/64, c1=3(7a+3)/64,

as in (16). For an independent check, zeta=3+4a, X_CM=3-4a and

    12/(X_CM^2-1)^3=-105/16-297a/32,
    12X_CM/(X_CM^2-1)^3=-9/8-51a/32.

Adding the three rational-node contributions reduces to those c0,c1. Hence the repair is present in the complete observer, not merely in P_hat.

Equivalently the repair's coefficients on r_+ and r_- are -3(1+2a)/16 and -3(1+a)/64. Combining them with (15) and the normalized integrals produces the full table:

| N evaluation | W weight | T weight | E weight |
|---|---:|---:|---:|
| 1 | -1/2 | 4 | 0 |
| -1 | 5(4a+3)/18 | -2(4a+3)/9 | 2(4a+3)/9 |
| a | -2a-1 | 4(a-1) | 2a+1 |
| 1/2 | -4a/9 | -40a/9 | -5a/9 |
| -1/2 | 0 | 0 | -3a-2 |

Every entry has been checked from ordinary rational substitution with a^2=1/2. In particular the repaired row at t=1 is (-1/2,4,0), and the -1/2 E row remains present. All fixed constants divide only by units for the target classes.

## 6. Explicit kernel and finite-log constants: PASS

Applying this table to the h_n-dependent terms -2L_(2n)(t) in N_W and 4^-n L_(2n)(-2t)/2 in N_T gives each of the eight terms of K_n in (17), with their exact coefficients. K_0=0 because L_0=0. No old R coefficient is assigned during this operation.

The finite polynomial identity L(x)=[1-x^p-(1-x)^p]/p is coefficientwise integer division followed by reduction. Evaluating at the rational unit arguments gives the paper's six q_2,q_3 identities. Pairing reciprocal indices gives L(x)=-x^pL(1/x). At the marked a this yields L(-2a)=-2aL(-a), while summing even powers gives sum_(r=1)^(3m)a^(2r)/r=L(a)+L(-a). All entries of the base-value table follow directly.

Substitution of that base table into the full Lambda weights gives q_2 coefficient -8(1+2a)/3, log terms -4aL(a)+2L(-a), and q_3 coefficient 1 from Lambda. Adding the original two q_3 contributions gives coefficient 3, exactly Gamma in (18). Thus (19) is a proved transformation of the fully fixed observer, not a newly fitted constant. The conjugate formula changes a to -a; only the whole expression has the inherited base-field scalar membership.

The final coefficient interface (21) also preserves all three independent terms: C_(i,j)=g v_i i! binom(2i,j)4^j(-3)^(2i-j)/(1/2)_i; the middle term is exactly OLD-R's v_i coefficient; the last term is exactly the binomial finite integral for 6tau. Its denominators satisfy i+r<=4m<p, and (1/2)_i and the original D_r denominators are units. The log update is used only below n=3m; extending it to the next step would divide by p and is correctly excluded.

## 7. Included OLD-R fourth-order recurrence and bounded failed forms: PASS

The helper's second difference H_n-2H_(n-1)+H_(n-2)=D_n+5D_(n-1) follows by retaining exactly the last two diagonal bands. With A_n=(n-1/6)(n-1/3), its ratio numerator 2(n-1)^2+5A_n equals P_n/18. This gives the stated third-order H recurrence without division by P_n.

For J_n=2B_nH_n, the displayed e_n equals 2B_n times that second difference. Multiplication of its first-order recurrence by 4n^2*18^3 gives precisely the helper's alpha,beta,gamma,delta coefficients, and replacing J_j by R_j-R_(j-1) proves the fourth-order recurrence. The rational initial values H_1,H_2,R_1,R_2,R_3 have been checked directly from the fixed ratios; the n=2 boundary R_-1=0 is retained.

At n=m=-1/6 modulo p, c_m=0, a_m=6, P_m=64, so alpha_m=9600 while the other three coefficients vanish. Thus the terminal equation is 9600(R_(m+1)-R_m)=0. This constant is a unit for p=6m+1>=7; it determines the next increment and gives no value condition on R_m. The m=1 exceptional recurrence index is explicitly excluded and its zero increment follows directly from B_(m+1)=0. No uniform division by an interior P_n is justified or claimed.

The polynomial-adjoint no-go uses commuting operators with leading parts -i^2/2 and r^2. Cancelling a highest-degree syzygy and reducing by the commuting pair strictly lowers degree, eventually contradicting a nonzero affine right side. It applies only to the prescribed polynomial factors. The simultaneous-diagonal no-go likewise correctly transforms to N(r)f(r+1)-C(r)f(r)=1+6n over Q(n)(r); its pole-chain endpoints have incompatible integer-shift orbits, and polynomial leading degree is k+3 with nonzero coefficient k+1. It applies only to that single diagonal rational flux. General independent rational two-variable fluxes, finite-field and higher-order forms are not excluded.

## What has and has not been proved

Frozen paper lemmas passing this review are: finite connection coefficients; the two-index triangle; actual all-support summand flux; legal modular upper endpoint; finite Heun coefficients/terminal; all three normalized integral transformations; full old pole-repair contribution; Lambda weights; explicit K_n/Gamma; and the auxiliary fourth-order OLD-R recurrence at its stated scope.

None compares this kernel with OLD-R plus 6tau. The zero in (20), the original LIFT identity, weighted p^3 supercongruence, raw period normalization and native full-X6 propagation remain OPEN. Heun homogeneity, its terminal coefficient relation, and CM0 are not an evaluation of the final observer. Final independent verification of the frozen author bytes and complete pin set is PASS, as recorded in FREEZE_READBACK.md and REVIEW_PINS.json.
