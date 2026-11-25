# PREFIX-1097 -- Explicit monotonic last-negative cones and an effective integer search bracket

2026-11-26. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / FINITE_EXACT_RATIONAL_CERTIFICATE / NOT_REVIEWED. Independent continuation of PREFIX-1096, retaining the original TASK_RESEARCH activity RA-0ABD84561C86E53067DB0322 / EM-DIRECT-780BBE. Own registration metadata recovered by r6-20261126-0751-own-recovery, original registration r6-20261123-2358-session-start-own-v1, no runs. Owner query r6-20261126-0751-owner-read SUCCEEDED / error=null, fixed as_of 2026-11-25T23:52:23.806064Z, Source 609525b844ebe988aac82d76d95e329b2e101336, LEASED filter empty. No new CLAIM or shared task mutation.

Frozen input P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; Stage46 X6 chart O, incoming -e1, reversal signed -5 (phase cover 5q), all other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Full paired six-axis Cell equality, phase, sign, port and ordered multiplicity remain in the original BRC CT carrier. Only the inherited exact radial observation and its analytic certificates are used here; no new native propagation, classical numerical reference or physical residual attribution.

Parents, immutable:
- 8d25f98107e9602c08ad92e01254d808955431f4:research_notes/portable_direct/2026-11-26_r6_prefix1092_two_anchor_effective_positive_tail.md (weighted C^3 observer bound and rational cutoffs).
- 08f0330096daa21d866aef04ea1db0c6d4f24384:research_notes/portable_direct/2026-11-26_r6_prefix1095_certified_lower_edge.md (first root and uniform lower-band sign/derivative certificate).
- 0919218e87c1f6a094123bb19ff315c17846b778:research_notes/portable_direct/2026-11-26_r6_prefix1096_second_order_last_negative_edge.md (asymptotic localization; explicit finite remainder still open).
- e5f4fc3df56133a943b1fd5d1b9784771066b1ea:research_notes/portable_direct/2026-11-25_r6_prefix1082_exact_ct_integer_sign_triangle.md (exact integer sign oracle); f8e95de9568ac9e174179902e12d90f5d6e608a6:research_notes/portable_direct/2026-11-26_r6_prefix1093_grouped_euler_occupancy.md (linear arithmetic-step CT occupancy recurrence).
- 7e8adcd9dac8e9ae5662c71aed1e2211458f12f0:research_notes/portable_direct/2026-11-25_r6_prefix1075_uniform_positive_tail.md (observer identity and integration by parts at zero).

## 1. New result

Write D_m(k)=D(m+8,k)=L(x^m(1-x)^k), y=1-x. Let b be the exact first simple lower-band zero of the effective density from PREFIX-1095. For all integers m,k in either of the following two cones,

    m >= 280000, k >= 21m;
    m >= 100000, k >= ceil(107m/5),

we prove the strict inequality

    D_m(k+1) - (1-b) D_m(k) > 0.

Thus D_m(k)/(1-b)^k is strictly increasing in k throughout each cone. This proves a global one-way sign property on the infinite suffix, not just local asymptotic derivative positivity. A nonnegative observation cannot be followed by a negative one in the cone.

Additionally, for EVERY integer m >= 1000000 we prove

    D_m(21m) < 0,   D_m(22m) > 0.

Combining these results yields an explicit global integer bracket:

    21m <= K_last(m) <= 22m-1  (m>=1000000).

K_last is the final strictly negative integer observation, including the possibility that its successor is exactly zero. Binary search on the exact inherited CT sign oracle in [21m,22m] returns K_last using at most ceil(log2(m)) interior sign calls, since the endpoints have certified signs. Or two adjacent exact signs D_m(j)<0<=D_m(j+1) with j in either monotonic cone certify the last negative globally. This is a bound on sign-oracle calls, not bit complexity or measured end-to-end acceleration. No million-scale CT table is computed here. This route removes the need to know the explicit O(m^-2) constant of PREFIX-1096 for exact final-integer certification in the stated ranges.

## 2. Exact first-edge input and local lower bounds

From PREFIX-1095,
    bl=(6800006737/5368709120)^2/36 < b <
    bu=(3400003369/2684354560)^2/36.
For t=sqrt(36x), g(x)=36/(4*36^8) * R^3/[(R-16)^3(R-4)^3] * F(t), R=36x.
The parent certifies F>0 on [0,5/4] and F'<-8*10^9 on [5/4,13/10], with the unique zero t*=sqrt(36b) there. Thus g>0 on (0,b), g<0 on (b,w] where w=169/3600. In particular h(x)=(b-x)g(x)>=0 on (0,w]. These are inherited analytic certificates, not re-anchored or independently reviewed this turn.

For any rational witness interval [a,z] within [25/576,w] that lies strictly on one side of [bl,bu], set delta=max(a-bu,bl-z)>0. Since dt/dx=18/t>=180/13 throughout this interval and between it and b, the mean value theorem gives |F(t)|>=8*10^9*(180/13)*|x-b|. Both factors R-16,R-4 are negative; hence their cubic product is positive and its magnitude <=16^3*4^3. The uniform rational lower bound is

    G(a,z)=36/(4*36^8)*(36a)^3/(16^3*4^3)*8*10^9*(180/13)*delta.

Then |g|>=G and h>=G*delta on [a,z]. For any nonnegative m,k the witness contribution to the appropriate positive or negative mass has magnitude at least
    W=G*(z-a)*a^m*(1-z)^k,
or use G*delta in place of G for h. This is a genuine finite interval lower bound; the density is not replaced by a sampled value.

## 3. Complement estimates including the root multiplier

Use the PREFIX-1092 exact weighted distribution bound

    |L(f)| <= sum_(j=0..3) C_j ||x^(3+j) f^(j)||_infty,
    C=(114025897/629856,118208/2187,1637/324,4/27).

The product rule and |b-x|<=1, x<=1 prove that L_h(f)=L((b-x)f) satisfies the same bound with
    C'_j=C_j+(j+1)C_(j+1) for j=0,1,2; C'_3=C_3.
This preserves the BRC observer identity rather than modifying the original signed carrier. On the regular lower band its ordinary density is h. The cutoff at zero is legitimate for both observers by PREFIX-1075's O(x^3) coefficient/derivative estimates, and multiplication by b-x preserves those boundary estimates.

Let chi_(s,z) be the C^3 cutoff of 1092, equal to one for x<=s and zero for x>=z, transition 1-(35t^4-84t^5+70t^6-20t^7), t=(x-s)/(z-s). Both chi and 1-chi have derivative sup bounds R_i/(z-s)^i, R=(1,7,42,420). For any nonnegative norm vector A define

    J(A,s,z)=sum_j A_j sum_(i=0..j) binom(j,i) R_i/(z-s)^i.

For f=x^m y^k with k>=3 and m>=0, the differentiated cutoff terms in the weighted norm have monomials x^p y^q with p=m+3+i+l, q=k-l, i+h+l=j, 0<=j<=3, h<=m. Their maximum on the support of the right complement (x>=s) occurs at x=s if

    (m+6)/(m+6+k-3) <= s.

The maximum on the support of the left cutoff (x<=z) occurs at x=z if
    (m+3)/(m+3+k) >= z.
These are sufficient because p/(p+q) is increasing in p and decreasing in q; the endpoints handle zero powers directly. Under the corresponding condition let x0=s for the complement or x0=z for the left cutoff. Then in either case

    |L_A(cutoff*f)| <= J(A,s,z)*(1+m+k)^3*x0^m*(1-x0)^(k-3).

Here L_A denotes L or L_h with its applicable vector. Proof: all terms reach their maximum at the indicated endpoint, x0^p<=x0^m, (1-x0)^q<=(1-x0)^(k-3). Sum the derivative multiplicities using falling powers <= ordinary powers, so the remaining factor is bounded by (1+m+k)^3 times J. This proves the coarse bound without any asymptotic or float estimates.

Divide by the witness W of section 2, with G replaced by G*delta for h. For a fixed witness [a,z] and fixed cutoff parameters, the ratio of adverse bound to witness lower bound is at most

    K*(1+m+k)^3*(x0/a)^m*q^k,
    q=(1-x0)/(1-z),
    K=J/[(1-x0)^3*G*(z-a)].

Use the h lower bound in K when appropriate. This ratio is the only quantity needing finite rational verification. On a cone k=cm+t with integer c and t>=0, write p=(x0/a)*q^c; increasing m by one at fixed t multiplies the ratio by at most p*((N+c+1)/N)^3 and increasing t by one at fixed m multiplies it by at most q*((N+1)/N)^3, where N=1+(1+c)m0 is a base lower bound for 1+m+k. Thus strict comparisons at m0 control the entire unbounded cone. For a fixed row of k=cm only the m comparison is required, even if q>1.

## 4. Explicit monotonicity

Use v=469/10000, w=169/3600, and decompose L_h(f) into local integral with chi_(v,w) plus the right complement. The local density h is nonnegative on its support. For the broad cone use [a,z]=[4545/100000,45451/1000000], a>b, z<v. The local integral >=W with G*delta. The right mode condition at m0=280000,k=21m0 is checked exactly and persists as m increases since the limiting mode 1/22<v, and as k increases by monotonicity. The exact rational comparisons give
    K<2*10^32, p<999503/10^6, (999503/10^6)^10000<1/100.
At m0 the resulting ratio bound is
    U_broad = 2*10^32*(1+22*280000)^3/100^28 < 1/100.
Both step factors from section 3 are strictly below one. Hence L_h(f)>0 for all m>=280000,k>=21m.

For the narrower cone, take [a,z]=[447/10000,44701/1000000], same v,w, and write m=100000+r+5j (0<=r<5), k=ceil(107m/5)+t. Put P=(v/a)^5*q^107. The actual rational comparisons give K<8*10^33, P<99366/100000, (99366/100000)^1000<1/570, and v/a<21/20. At the five starting residues use N<2240100 and (v/a)^r<=(21/20)^4; the extra factor q^ceil(107r/5) is <=1. The common ratio bound is

    U_narrow = 8*10^33*2240100^3*(21/20)^4 / 570^20 < 1/100.

The exact check gives P*((2240001+112)/2240001)^3<1 and q*((2240001+1)/2240001)^3<1. The right mode condition persists by the limiting mode 5/112<v and the base inequality at m=100000 (ceil only increases k). Hence L_h(f)>0 throughout this second cone.

Finally, exact linearity of the BRC observer gives
    L_h(f)=L((b-x)x^m y^k)=D_m(k+1)-(1-b)D_m(k).
Dividing by the positive (1-b)^(k+1) proves strict monotonicity of the normalized sequence, including the integer-zero case. No inference of monotonicity from raw unnormalized observation signs is used.

## 5. Explicit negative and positive endpoints

For m>=1000000, k=21m use the broad-cone witness [a,z] but now G (not G*delta). Let sL=446/10000,bL=447/10000. By the exact ordered endpoints, b<sL<bL<a<z<v<w. Decompose
    D_m(k)=L(chi_(sL,bL) f) + integral (chi_(v,w)-chi_(sL,bL))*g*f dx + L((1-chi_(v,w))*f).
The middle term is nonpositive on its support, since the cutoff difference is nonnegative and supported in [sL,w], and includes the entire negative witness interval. It is <=-W. The left mode bound is automatic since (m+3)/(22m+3)>1/22>bL, the right one follows from the broad-cone check. Apply the ratio bound of section 3 with x0=bL or x0=v and A=C. Exact finite checks:
    K_left<14*10^27, p_left<999877/10^6, (999877/10^6)^10000<3/10;
    K_right<2*10^29, p_right<999503/10^6.
The two ratios at m0=1000000 sum to at most
    U_negative = 14*10^27*(1+22m0)^3*(3/10)^100
                 +2*10^29*(1+22m0)^3/100^100 < 1/100.
Both decrease for increasing m with k=21m by the one-step factor check. Thus D_m(21m)<0.

For k=22m choose [a,z]=[4347/100000,43471/1000000] within [25/576,b), and s=444/10000,bP=445/10000. The cutoff chi_(s,bP) contains the positive witness and is supported strictly below b. Thus the local positive integral >=W and only the right complement must be paid. Its mode condition holds from m0 and persists since 1/23<s. The exact finite checks give
    K<13*10^27, p<999792/10^6, (999792/10^6)^10000<1/7,
    U_positive=13*10^27*(1+23m0)^3/7^100<1/100,
and the ratio decreases at k=22m. Hence D_m(22m)>0. Together with section 4 this proves the bracket and exact integer search in section 1. The proof covers all integers in the stated infinite cones by the finite ratio induction, not by sampling them.

## 6. Actual verification and next

Exact rational checker was locally executed in Python using Fraction. All assertions passed. Four adverse-to-witness ratio upper bounds (rounded display only):
    broad_monotone               4.674900196736e-04
    narrow_monotone              8.339735711892e-03
    negative_left_plus_right     7.682836824716e-03
    positive_complement          4.890158273227e-35
The local checker SHA256 is 81bbe39019a39db01cd0677dcbee3f33c5a1f4f18a3298447d8b4bc8462dc0da; git blob e565ad32329a08994457b635b37f6f2bca919f6b. Full checker saved and read back:
19cc166cfb372eb9f10fca6566c7de7d539dd6b6:research_notes/portable_direct/2026-11-26_r6_prefix1097_monotone_tail_check.py.
The remote blob matched the local git hash. This computation checks the explicit rational inequalities of the analytic proof, not million-scale CT observations or an end-to-end binary-search implementation. No new numerical reference, parent-density re-anchor, independent mathematical review, formal Result freeze or Working Truth promotion.

The old uniform positivity bound 1100+24700(m+1) is now replaced in the range m>=1000000 by positivity for every k>=22m (approximately 1122.7 times smaller leading slope); the stronger normalized-monotonicity assertion applies in its two stated cones. PREFIX-1096's more precise root prediction can be used to choose the first adjacent sign probes but is not itself a finite root interval. The next useful work is to lower the activation thresholds by a sharper local witness integral / Bernstein norm, then construct a certified fast exact-sign evaluator near the asymptotic edge without building an enormous CT table. Independently, derive the explicit O(m^-2) constant or sharpen the integer bracket to a small fixed width; do not repeat 1095 root isolation or the completed ratio inequalities without new evidence. Other spectral zeros, the small/intermediate-m global sign classification, the mother parameters p,d and B_fix,odd(32) remain open.
