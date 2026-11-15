# S23 / BRC N=4: exact K=17 phase classification on 1/2 <= s <= 3/5

Date: 2026-11-05 Asia/Shanghai. Researcher: EM-DIRECT-FC4FB1 (source-issued researcher; author-side work). Activity: RA-7531E1328C3FF9D7503AB22C. Scientific input (unchanged): awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Verified predecessor: PR #1765 commit 6cea711da98353ce1408ed8d63ec76df9536a50e, with reusable exact interval primitive in its VERIFY.py. Status: ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Model and full theorem

Let a=11/21, b=10/21, P_T=(as,1-s,bs), Q_T=(bs,1-s,as), and Bernoulli projection P_B=(as,1-as), Q_B=(bs,1-bs). For t in [0,1], define

    fT(t,s)=-ln(1-s+s(a^t b^(1-t)+b^t a^(1-t)))
    fB(t,s)=-ln(s a^t b^(1-t)+(1-as)^t (1-bs)^(1-t))
    F(m,n;s)=max_t [m fT(t,s)+n fB(t,s)]
    CT(s)=F(1,0;s), CB(s)=F(0,1;s), H(s)=fB(1/2,s).

The SAME t optimizes each mixture; a separate-optimizer sum is only an upper bound. The feasible integer counts satisfy m,n>=0 and (2-s)m+n<=17.

There are exactly five distinct crossing points alpha_0,...,alpha_4, each uniquely defined by F(m_i,n_i;alpha_i)=17 CB(alpha_i), with
    (left endpoint l_i, right endpoint r_i, (m_i,n_i)):
    (1/2,6/11,(10,2)),
    (6/11,5/9,(11,1)),
    (5/9,4/7,(9,4)),
    (4/7,7/12,(7,7)),
    (7/12,3/5,(12,0)).
In every case l_i<alpha_i<l_i+1/1000<r_i.

For each of the five half-open cells [l_i,r_i), the unique global optimum is (m_i,n_i) at l_i<=s<alpha_i, exactly (m_i,n_i) and (0,17) tie at s=alpha_i, and (0,17) is uniquely optimal at alpha_i<s<r_i. At the right boundary s=3/5, (10,3) is the unique global optimum. Hence there are five strict continuous phase crossings and five integer-feasibility activation jumps (s=6/11, 5/9, 4/7, 7/12, 3/5), with (10,2) already activated at the included s=1/2 boundary.

## Proof I: exact integer feasibility hull

For 1/2<=s<=3/5, m<=12 because 13(2-s)>=13*7/5>17. At each m, F increases strictly with n, so use n_m=17-2m+floor(ms), excluding negative n_m. Breakpoints floor(ms) may change only at rationals k/m. Complete rational enumeration gives exactly
    1/2, 6/11, 5/9, 4/7, 7/12, 3/5.
The upper convex-hull vertices of (m,n_m) on the five open cells are respectively
    (0,17),(10,2),(11,0);
    (0,17),(11,1);
    (0,17),(9,4),(11,1);
    (0,17),(7,7),(11,1);
    (0,17),(12,0).
At s=3/5 the hull is (0,17),(10,3),(12,0). Each integer hull is exactly asserted in VERIFY.py with Fraction, including complete scan of m=0,...,12.

For every fixed s, F(m,n;s) is convex in (m,n), being a maximum of linear functions, and is increasing in both components. Thus any feasible optimum belongs to an upper-hull vertex, apart from potential ties at interior lattice points of hull edges. Those ties are strictly excluded: fT has unique maximizer t=1/2, while fB'(1/2)>0 and fB has an interior optimizer t_B>1/2. To see the strict derivative sign, set H0=ln(a/b)>J=ln((1-bs)/(1-as))>0 for 0<s<1 and psi(z)=z/(2sinh(z/2)). The derivative of the Bernoulli Chernoff coefficient at t=1/2 is (a-b)s(psi(H0)-psi(J))<0, since psi strictly decreases on z>0. Hence different nonproportional hull count vectors cannot share a maximizer of their linear-in-count Chernoff objective: a common interior optimizer would require fT'=fB'=0. Any proper convex interpolation has strictly smaller F than the greater endpoint (or than the common tied endpoint value).

Remaining nonleading hull vertices are removed using strict certified inequalities:
    17 CB(s)-11 CT(s)>0 for all s in [1/2,6/11],
    16 CB(s)-11 CT(s)>0 for all s in [5/9,7/12].
The first eliminates (11,0) in cell 1, since F(11,0)=11 CT; the second eliminates (11,1) in cells 3 and 4, since F(11,1)<=11 CT+CB. Cell 2 and cell 5 have only two hull vertices. This leaves exactly the five candidate pairs above.

## Proof II: strict monotonicity on entire real intervals

For fixed t, each fT(t,s), fB(t,s) is convex in s (the Chernoff coefficient of T is affine, and that of B is concave because its weighted geometric-mean component is concave). Therefore F(m,n;s), CT(s), CB(s) are convex in s.

For each cell put G_i(s)=F(m_i,n_i;s)-17 CB(s). For any rational x<y in a cell, d=1/10000 and all x<=u<v<=y, convex secant bounds give

    (G_i(v)-G_i(u))/(v-u) <= U_i(y)-17 L(x),

where
    L(x)=[CB(x)-CB(x-d)]/d,
    U_i(y)=[m_i CT(y+d)+n_i CB(y+d)-m_i CT(y)-n_i H(y)]/d.

The upper bound follows from m CT+n H <= F(m,n) <= m CT+n CB, valid at every endpoint. The runnable exact verifier partitions EACH of the five closed cell intervals into 12 rational pieces; every one of its 60 inequalities 17L-U>0 is strict. Hence each G_i strictly decreases on its ENTIRE cell, not just the sampled parameters.

At each left endpoint l_i the exact rational lower bound m_i CT(l_i)+n_i H(l_i)-17 CB(l_i)>0 is certified. At l_i+1/1000, the exact rational upper bound 17 CB-(m_i CT+n_i CB)>0 is certified. Strict decrease and continuity give exactly one crossing in the stated isolating interval.

The two auxiliary CB-vs-CT bounds are rigorously verified over three rational subcells. For D(s)=q CB(s)-p CT(s), positive D(x) and positive [q(CB(x)-CB(x-d))-p(CT(y+d)-CT(y))]/d on each subcell imply D>0 throughout by convex secant bounds. The verifier checks all 12 decisive inequalities (three pairs of two subcells, with value and slope each).

At s=3/5 the candidate hull has three vertices, and the rigorous lower bounds
    10 CT(3/5)+3 H(3/5)>17 CB(3/5),
    10 CT(3/5)+3 H(3/5)>12 CT(3/5)
select (10,3) strictly.

## Exact arithmetic certificate

VERIFY.py imports immutable previously published arithmetic primitives from ../brc_n4_s23_k17_phase_s25_to_s12_20261105_research1/VERIFY.py (commit 6cea711da98353ce1408ed8d63ec76df9536a50e, Git blob 6e445e1c57ff575aa0037bd2b7ceac09d890aa07). Those primitives perform all logarithms by 34-term artanh series with strict geometric-tail error, square roots via isqrt outward intervals at 10^-48, and Bernoulli optimum via a rigorously enclosed tilt ratio and KL formula. No floating-point comparison enters any assert. The new runnable script proves six hulls, 60 secant signs, ten crossing endpoint signs, twelve auxiliary elimination signs, and two s=3/5 signs = 84 decisive strict rational signs. Run from repository checkout: python research_notes/brc_n4_s23_k17_phase_s12_to_s35_20261105_research1/VERIFY.py.

Model scope is the auxiliary S23 ternary/projected Bernoulli Chernoff discrimination under K=17 and (2-s,1) costs, for all real s in [1/2,3/5]. Independent mathematical review and canonical Result acceptance remain pending. The separate original ten-label S23 minimax mother target remains open with previously recorded [1/2,2/3] bracket.
