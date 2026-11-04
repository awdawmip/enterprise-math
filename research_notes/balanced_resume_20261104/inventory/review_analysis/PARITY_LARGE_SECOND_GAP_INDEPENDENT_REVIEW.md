# Independent paper review of the bounded-total-scale large-second-gap theorem

Reviewer: `EM-REVIEW-53C747`, agent `/root/research_inventory_1104`.
Role: direct `TASK_RESEARCH` paper reviewer, locally allocated identity, `REGISTER_PENDING`.
Reviewed author: `EM-ANALYSIS-3050DA`, agent `/root/research_analysis_1104`.
Date: 2026-11-04.

**Verdict: PASS — no unresolved mathematical defect found in the stated new theorem and its conditional composition with the cited source theorems.** This is an exact-version nonauthor paper finding, not a formal Task disposition, accepted Result, Working Truth, source publication, or proof-kernel certificate. The inherited original signed-trace normalization and earlier theorems retain their source status. No formal mathematical acceptance is issued.

Frozen manuscript: `PARITY_BOUNDED_TOTAL_SCALE_LARGE_SECOND_GAP_AUTHOR.md`, SHA256 `52332f92d0435d26c1e7985dba96d1be7fee508c98100fdcff66e8530fbb0207`. I verified this digest before reviewing the text. The review does not cover later revisions automatically.

## Independence and evidence boundary

I performed the portfolio/source inventory before this assignment, supplied the frozen Source snapshot and identified the compact-total-scale residue as a cold research direction. I did not supply the author's endpoint argument, identities, constants, manuscript edits, or repair. I received the author's completion metadata before reading the frozen paper. This review is nonblind and shares project/source context; it is independently derived by a different agent, not a claim of clean-room blindness. Root routed the review and supplied no mathematical finding.

The Source snapshot is `awdawmip/enterprise-math@39556bf5207aa5ba559a27ec591c1bc1bf43b457`. I directly read the new paper and its provenance file, the prior all-second-gaps tail, the bounded-relative-gap common-frame proof, the original centered-metric parity proof, and the all-S small-second-gap strip. Exact source digests and readback evidence are retained in the companion JSON. The earlier reviews are not being reused as a review of this manuscript.

Tools here were used for source reading, identity allocation, document preservation, and hashes. I ran no scientific code, symbolic expansion, parameter scan, numerical certificate, or stopped P11/m7 consumer. The checks below are paper derivations. This is external classical signed-matrix algebra; no native physical or geometric law follows.

## 1. Same-input congruence and secant orientation

On column coefficients in the monomial basis, `J[j-1,j]=j` implements differentiation. Thus `exp(xJ)` is translation of a polynomial argument by x, and averaging its derivative over `[0,b]` gives exactly `F_b`. The derivative rising-factorial polynomials have increasing degrees 0 through n−1 and nonzero leading coefficients, so their coefficient matrix U(t) is invertible. It is the SAME U(t) for L and N. Cancelling U from both forms preserves the relative trace.

For the second congruence, both forms use `T_t=exp(tJ/2)`. Since the relevant operators are polynomials in J,

`F_b T_t = exp((b+t)J/2) E_b`.

At b=L the output center is r/2; at b=N it is s/2. These different output centers arise from one common input change, so the trace equality is valid. A congruence by T sends `B^{-1}A` to `T^{-1}B^{-1}AT`; the orientation in the manuscript is correct. No term from either signed secant frame has been discarded.

## 2. Scale, inverse orientation, and uniform endpoint

For `C_v[j,j]=v^(j-m+1/2)`, the ratio of adjacent diagonal entries gives `C_v J C_v^{-1}=J/v`. Consequently `C_s E_N=E_(N/s) C_s`, and the centered second form is

`Bhat = C_s E_(N/s)^T M(1/s) E_(N/s) C_s`.

Taking its inverse gives exactly

`Bhat^{-1}=C_s^{-1} E_(N/s)^{-1} M(1/s)^{-1} E_(N/s)^{-T} C_s^{-1}`.

Now `C_s^{-1}=s^(m-1/2) diag(s^{-j})`; the two scalar factors therefore produce **2m−1**, not m+1 or 2m−2. Also `N/s=1-t/s`. This proves the manuscript's K and Z formula and the trace expansion, including the subtraction `n z^(2m−1)` after normalization.

At z=0 the only surviving summand is `K(0,t)[0,0] Ahat[0,0]`. Its first factor is independent of t and equals

`kappa_m=(E_1^{-T}e0)^T M0^{-1}(E_1^{-T}e0)`.

The transpose orientation is essential and is correct. Since E and its inverse contain only even powers of J, both preserve parity, as do their transposes. The displayed vector is nonzero and belongs to the even subspace. The inherited metric proof supplies a strictly positive even block, so its inverse has a strictly positive even block as well. Hence kappa is strictly positive and rational. This does not assert positivity of the full finite-z matrix. For n=1 all factors are scalars, the even block is positive, and no odd-block exception occurs.

For completeness, the source parity proof represents the centered limit by a residue/Fourier integral. Cross-parity terms vanish by reflection; after a diagonal sign congruence each same-parity block is a positive weighted Gram matrix, with overall sign positive for even and negative for odd indices. The endpoint vanishing order is at least two, so the integrals are finite, and independence of the cotangent monomials makes the blocks strict. This matches the M0 appearing in the manuscript's exact centered normalization.

On the closed triangle `t,L>=0, t+L<=R`, the earlier form is analytic and bounded because its metric denominators remain positive, including r=0. K is analytic near z=0 uniformly over this compact t-range. Therefore the endpoint limit is uniform on the triangle. The later explicit polynomial argument supplies a uniform rational neighborhood independently of a compactness-only assertion.

## 3. Scalar Beta integral and its lower bound

Because `J e0=0`, both F and T fix e0. Thus the scalar coordinate is `Q_r[0,0]`, with the stated factor n!/m. Inserting

`1/(x)_m=(1/n!) integral_0^1 y^(x-1)(1-y)^n dy`

and summing the alternating binomial weights gives `(1-y^(1/m))^n`. The first prefactor is 1/m. With `y=u^m`, the exponent calculation is

`y^(r+1/m-1)dy = m u^(mr)du`.

The factor m cancels 1/m, giving exactly the exponent **mr** and the integral in the paper. It is strictly positive at every r>=0, including r=0.

For k=ceil(mR), on `[1/4,1/2]` and 0<=r<=R, one has `u^(mr)>=4^{-k}` and both remaining factors are at least `2^{-n}`. Multiplying by interval length 1/4 gives `4^{-k} 2^{-2n}/4 = 4^{-(k+m)}`. Thus alpha is a valid positive rational uniform lower bound with no positive lower bound on a or r.

## 4. Polynomial divisibility, denominator signs, and inclusive thresholds

The finite-difference cancellation needed for W is valid entrywise: every coefficient of z-degree d<n in the expansion before summing is a polynomial in the node theta of degree at most d. Its signed binomial sum vanishes. Multiplication by the common polynomial Q preserves divisibility by z^n. Thus W is genuinely a rational polynomial matrix, and Q(0)=1 gives W(0)=M0.

The denominator product q is correctly enumerated: the factors `mr+mh+i+1` for 0<=h,i<m cover 1 through m² once each. Consequently q(r) is positive and increasing for r>=0, with nonzero rational q(0). Multiplying the earlier form by q clears every metric denominator and leaves polynomial matrices in (t,L), including the closed origin.

With sigma=sign(det M0), `d(0)=|det M0|=d0>0`. The adjugate construction satisfies

`Kmat/d = Q V adj(W) V^T/det(W) = V M^{-1} V^T`

where defined. The sigma signs cancel, so there is no determinant-sign reversal in `P/(q d)`. At z=0, `Kmat=d0 E_1^{-1}M0^{-1}E_1^{-T}`, whence `P(0,t,L)>=d0 kappa q(0)alpha=gamma` on the triangle. The one-by-one adjugate convention includes m=2.

The absolute coefficient bounds hold on the stated rectangle even when R<1: for nonnegative t,L<=R, `t^a L^b<=R^(a+b)`, and for 0<=z<=1, `z^ell<=z` whenever ell>=1. No positivity of the individual coefficients of P is needed. The separate zero-Bd and zero-BP definitions avoid division by zero. For `z<=rho`, these bounds imply simultaneously `d>=d0/2` and `P>=gamma/2`.

Because Q(z)>0, the positive d also proves W and M invertible. E and C are invertible, so Bhat is invertible throughout the claimed large-gap domain; using its inverse is not circular. The upper denominator bounds are `q(r)<=q(R)` and `d(z)<=sum|d_l|=Dmax`, both positive. Therefore the stated lower bound `P/(qd)>=gamma/[2q(R)Dmax]` has the correct inequality direction.

Finally `c>=1/(m rho)` implies `s=r+mc>=1/rho` and hence `z<=rho`. Equality at the threshold is allowed; the half-margin estimates remain strictly positive. All finite algebraic constants are rational and explicitly defined. The paper correctly makes no efficiency, evaluated-constant, or parameter-coverage claim.

## 5. Composition and actual compact residue

The read source tail gives positivity for every c>0 once `m(S+a)>=R_m`, with rational R_m>=1. The source small-gap strip gives positivity for all S>=0, `0<a<=A0`, and `0<c<=delta_m(A0)` for a supplied positive rational A0. Taking `A0=R_m/m` meets that input hypothesis exactly.

A physical nonpositive point must first have `S+a<A0`. This implies `0<a<A0`, so the small-gap theorem applies and excludes `c<=delta`. The new theorem applies on this bounded-total-scale region and excludes `c>=C`. The remaining strict inequalities are exactly `delta<c<C`; all three boundaries are covered inclusively. If delta>=C there is no such point. Otherwise adjoining `a=0`, `S+a=A0`, `c=delta`, and `c=C` gives a closed bounded subset of R³, hence a compact closure. The cited raw-form source provides an analytic extension and nonzero determinant on the nonnegative orthant; no singular-frame inverse is silently required at a=0.

This reduces the possible-counterexample domain but does not prove positivity on it. The m parameter remains fixed. It does not settle all-m uniformity, full coefficientwise positivity, HCM0, P11 endpoint core, or the mother goal. The new boundary theorem and its compact-reduction corollary form one result-domain extension, not two independent discoveries.

## Final disposition

No must-fix issue was found. The precise claim reviewed is the bounded-earlier-scale large-second-gap lower bound, including all stated parameter and threshold endpoints, together with the compact-residue corollary under the cited earlier theorems. The common frame, signed terms, positive scalar observer, rational coefficient certificate, and inherited-hypothesis gluing are coherent.

The next mathematical obligation is a sign proof or a source-bound counterexample in the bounded middle region. Merely optimizing the asymptotic constants is not an automatic successor. Bounded project dedup does not establish external historical priority. This report supplies neither a new general tool family nor a formal Task vote.

Researcher-ID: EM-REVIEW-53C747 / TASK_RESEARCH

EM-Source-Status: Read=Verified snapshot reused (39556bf5207aa5ba559a27ec591c1bc1bf43b457; exact hashes in REVIEW_BINDING.json); Write=⚠ Not written (local review preserved; shared Source publication pending).
