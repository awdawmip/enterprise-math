# PREFIX-1059 — Candidate signed-BRC observer transfer, strict mixed minors and a uniform spectral margin

Date: 2026-11-24. Parent PREFIX-1058. Status: AUTHOR_CONDITIONAL_EXACT_PROOF / HUMAN_RECHECKABLE / NOT_REVIEWED. Independent portable note; no Task claim, formal Result or physical residual attribution.

## Scope and exact dependencies

Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. The model is precisely the Stage46 candidate, on the native chart-relative X6 affine Cell torsor, incoming h=-e1, outgoing numerator w(h,d)=1-6[h=d], new port -d, both orientations of Link {0,e1} absorbed without renormalization, exactly one outgoing negative native step, and terminal coherent square mass per named positive-travel port. Step count is not physical time. No new classical comparison, phase or pi evaluation and no new native run. The proof uses the inherited exact typed Z2 BRC identity, not an ordinary propagator substituted for it.

Read back immutable sources:
* PREFIX-1004 aec844a083f0517570ce1dd5924717db6880da98:research_notes/portable_direct/2026-11-22_r6_prefix1004_marked_collision_asymptotic.md; its exact phase-cover implementation b5976b3fa4254309cb00a23f8f944cbe1845cfeb:research_notes/portable_direct/PREFIX1004_R6_MARKED_COLLISION_CHECK.py. The historical all-fibre check n=5..9 was an independent typed N[Z2] recurrence, not a canonical Stage46 core invocation; no new execution claimed.
* PREFIX-1014 599f5d5306abae0101769432d6ff8da77517bf3e:research_notes/portable_direct/2026-11-22_r6_prefix1014_four_port_gram_orbits.md; PREFIX-1016 3d98b565222fa00867bcca382918ab33052304d8:research_notes/portable_direct/2026-11-22_r6_prefix1016_positive_port_three_A6_shifts.md.
* PREFIX-1026 539c70d40816ade6e130969bde1b224b1c01abb9:research_notes/portable_direct/2026-11-23_r6_prefix1026_hausdorff_spectral_transform.md; PREFIX-1033 fec5c00006e3693121ee18f6d0be661506e06410:research_notes/portable_direct/2026-11-23_r6_prefix1033_global_signed_density_bernstein_detection.md.
* PREFIX-1051 5df27cada185084996cab98b8736d5864e333d0f, PREFIX-1054 8c65067dfaa0cde6a032472d9cb7a9162ac81478, PREFIX-1055 4567d55f522ff9e565f6d5bf4cac825d6b39e5cf, PREFIX-1057 1253ec572d43e8c3afbddb1c3df0badf21561f82 and PREFIX-1058 a768f4b48f5e3df99fc7f9f79e2a30e1a5ca43fc:research_notes/portable_direct/2026-11-24_r6_prefix1058_zero_frobenius_complete_scalar_positivity.md (also read current main matching paper). Their scalar proof assumptions and certified lower bounds are inherited, not independently replayed in this note.

## 1. Exact typed terminal observer bridge

Let P_(n,j) be the labelled paths of length n obeying the frozen mask, grade 1 and final actual step +e_j. Keep the whole ordered branch word, each signed step, its multiplicity weight, native endpoint x and incoming port -e_j. For path p let M(p)=product of |w| and epsilon(p) be the parity of reversal events, including the initial incoming port comparison. The positive N[Z2] BRC cover carries M(p) at parity epsilon(p). Signed character chi(p)=(-1)^epsilon(p) M(p) is the exact numerator.

For the declared terminal observer, define the pair relation D_(n,j)={(p,q): p,q in P_(n,j), x(p)=x(q)}; pairs are ordered and both paths retain their provenance. A serial product of the two path characters gives chi(p)chi(q); no absolute value is taken before the character. Then

Q^+_(n,j) = sum_{(p,q) in D_(n,j)} chi(p)chi(q)
          = sum_x (sum_{p in P_(n,j): x(p)=x} chi(p))^2.

This is exactly the existing coherent joint-fibre readout (not positive total mass). Equivalently set F^L_(n,j)=sum_p chi(p) z^{x(p)} in the formal six-coordinate group ring. Multiplying by its reversed-exponent copy and extracting CT imposes equality of all six coordinates; the port and grade already match by construction. The group ring is an observer of the X6 carrier, not a replacement for branch history. The signed character is multiplicative on serial weights and linear over alternatives, so the path sum is an exact BRC character identity.

For transparency the PREFIX-1004 masked positive packet can also be checked directly from these path classes. Write S=sum_i z_i, U=sum_i z_i^-1, a=z1. For the free packet the unique negative step is first, interior, or penultimate. Their factors after extracting z_j S^(n-3) are SU-6S/a, SU-36 (n-3 identical interior positions), and SU-6S/z_j, respectively. This follows from sum_i z_i^-1(S-6z_i)^2=S^2 U-36S and the two endpoint reversal factors. Thus F_(n,j)=z_j S^(n-3) A_(n,j), A=(n-1)SU-36(n-3)-6S/a-6S/z_j. Remove paths with first +e1: these are a F_(n-1,j), as their next incoming port is again -e1. Among remaining paths the only forbidden crossing possible is the third step 0->e1: the total coordinate sum at time t after the single negative step is t-2, so a return to 0 can only occur at t=2; the reverse crossing e1->0 would require first +e1, already excluded. The prefixes (-e_i,+e_i,+e1) have total numerator sum -5 sum_i(1-6[i=1])=0. The prefixes (+e_i,-e_i,+e1), i!=1, have sum -25. Their common continuation is positive-only, of numerator z_j S^(n-4); its port and displacement coincide at the prefix endpoint, with histories still retained. Removing the forbidden prefix family therefore adds +25 a z_j S^(n-4) to the character. This reproduces the exact masked packet for n>=5; no merging of different terminal ports. The zero sum of the first prefix family is only a signed readout identity, not erasure of the branch provenance.

The subsequent immutable PREFIX-1014 and PREFIX-1016 identities apply to precisely that CT, with fixed j=2 for comparison (not the sum of five ports). For n=m+4, m>=1, let Delta_n=Q^+_(n,1)-Q^+_(n,2). Then Delta_(m+4)=sum_(s=1..3)c_s(m) A6(m+s), with c_s as in PREFIX-1016. PREFIX-1026 and 1033 identify this exact expression with integral y^m g(y)dy on [0,36]. In particular the inherited scalar representation now transfers to the defined candidate signed-BRC terminal readout by composition of exact identities. It does not require interpreting the auxiliary phases as native state or using new classical computations.

**Candidate transfer theorem.** Conditional on the inherited scalar certificate chain, for all m>=1,k>=0,

E_(m,k)=sum_(i=0..k)(-1)^i binom(k,i)36^(k-i) Delta_(m+i+4)
        =integral_0^36 y^m(36-y)^k g(y)dy >0.

The proof is linearity and PREFIX-1058. The m=0 scalar extension is 2412 and is not identified here with a native n=4 observation. Define p_n=Delta_n/36^n, the candidate probability contrast. Then (-1)^k forward_difference^k p_(m+4)=E_(m,k)/36^(m+k+4)>0. In particular p_n>0, p_n>p_(n+1), and p_n-2p_(n+1)+p_(n+2)>0 for every n>=5. This is a candidate observer theorem, not validation of the historical canonical kernel or native physical residual attribution, which remains NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION.

## 2. A new explicit common positive margin

Using the actual prior certificates, for 0<y<36 one has the stronger common lower bound

g(y) > (c/240) y (36-y)^(5/2),

where c>0 is the inherited upper-edge coefficient. Proof, without additional numerical execution:
- 0<y<=1/240: g/c>2600000 y by PREFIX-1058, and (36-y)^(5/2)<=36^(5/2)=7776.
- 1/240<=y<=39/16: g/c>80 by PREFIX-1057. The required right-hand coefficient is <=(39/16)*7776/240=3159/40=78.975<80.
- 39/16<=y<=4: g/c>3078000 by PREFIX-1055; 4*7776/240=129.6 is smaller.
- 4<=y<=16: g/c>598600 by PREFIX-1054; 16*7776/240=518.4 is smaller.
- 16<=y<36: g/c>251(36-y)^(5/2) by PREFIX-1051; y/240<=36/240<251.

Consequently for every m,k>=0 in the scalar extension and m>=1 in the candidate native contrast,

E_(m,k) > (c/240) 36^(m+k+9/2) B(m+2,k+7/2).

B is the usual positive beta integral. No evaluation of pi or phases is needed. This supplies a single strictly positive analytic margin at all orders, including arbitrarily high mixed differences. A prospective representation-error measure with total variation dominated by eta*(c/240)y(36-y)^(5/2)dy, eta<=1, cannot change any of these signs. This sufficient robustness condition covers a signed error in the contrast measure only; no actual native mapping error bound is asserted.

## 3. All-order strict sign-regularity of mixed-index contrast matrices (new)

For every r>=1, integers 0<=m_1<...<m_r, 0<=k_1<...<k_r, set M_ij=E_(m_i,k_j). For the native transfer require m_1>=1. Then

(-1)^(r(r-1)/2) det M > 0.

Proof: expand the two determinants and integrate termwise to obtain the exact Andreief identity
det M = 1/r! integral_[0,36]^r det[y_l^(m_i)]_(i,l) det[(36-y_l)^(k_j)]_(j,l) product_l g(y_l)dy_l.
On the ordered simplex 0<y_1<...<y_r<36, the first generalized Vandermonde determinant is positive: it factors as product_(a<b)(y_b-y_a) times a Schur polynomial whose nonnegative integer coefficients and nonzero monomial sum make it positive for positive variables (the partition is (m_r-r+1,...,m_1)). The second determinant has reversed increasing arguments and therefore sign (-1)^(r(r-1)/2), by the same factorization. Their product is invariant under simultaneous permutation of the integration variables. The simplex has positive measure and g is strictly positive there. Thus the claimed sign holds for every finite size, every set of distinct increasing indices, not only contiguous Hankel minors. With g replaced by w(y)=y(36-y)^(5/2), the same reasoning and the margin in section 2 give the explicit determinant comparison
(-1)^(r(r-1)/2) det M > (c/240)^r (-1)^(r(r-1)/2) det [36^(m_i+k_j+9/2) B(m_i+2,k_j+7/2)].
The reference signed determinant is itself positive. This makes the mixed-index sign test quantitatively robust at the measure level.

At r=2, for m'<m'' and k'<k'', E_(m',k')E_(m'',k'') < E_(m',k'')E_(m'',k'). Thus the residual ratio E_(m,k+1)/E_(m,k) strictly decreases with m, and E_(m+1,k)/E_(m,k) strictly decreases with k. Together with the exact positive recursion E_(m+1,k)+E_(m,k+1)=36 E_(m,k), these ratios describe a two-index tradeoff, not just positivity of isolated entries. The arbitrary-order minor signs provide a new discriminating test for future candidate BRC implementation checks. A single violated sign in an exactly matching observer would refute at least one link of the proof chain.

## Evidence and continuation

Human-recheckable proof: exact BRC pair relation and grade-one path decomposition, inherited scalar identity and interval certificates, beta integration, generalized Vandermonde/Andreief identity. No new numerical or physical-model run. The inherited evidence is not independent review. No observer-safe quotient for arbitrary future operations is claimed. Preserve native Cell, port, grade, branch, sign, multiplicity, source and ordered history. The next scientific question is to revalidate the canonical signed-BRC implementation against the exact labelled path semantics and derive a similarly scoped result for a genuinely new grade or Link configuration; a second negative step may introduce further forbidden returns and must not simply reuse the grade-one mask formula. Mother B_fix,odd(32) in {19,20} remains open.

Control: historical own registration r6-20261123-2358-session-start-own-v1 re-read SUCCEEDED; EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322, Activity source read shows empty checkpoints. Current scoped LEASED request r6-20261124-1750-sites-leased-observe-v1 last seen RUNNING/NATIVE_RUNNER, error=null; no current formal claim or execution authority established. Independent non-task note, no protected write or Activity association claimed.
