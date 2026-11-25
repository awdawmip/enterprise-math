# PREFIX-1076 — Uniform beta tail and residual transport law

2026-11-25. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / HUMAN_RECHECKABLE / NOT_REVIEWED. Independent existing line EM-DIRECT-780BBE / TASK_RESEARCH. Own session metadata recovered (MCP-f6d93209fc8e4c5bb2c3b44f69a47174; no run or formal CLAIM authority). Prior r6-20261125-0950-owner-read SUCCEEDED, LEASED list empty as of 2026-11-25T01:51:38.894136Z. Fresh read r6-20261125-1050-owner-read submitted, initially QUEUED. No shared task mutation.

Frozen scientific input unchanged: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; Stage46 chart O, incoming -e1, reversal signed -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Full X6 Cell pairing, ports, sign, phase, multiplicity retained in the inherited exact constant-term observer. All integral coordinates below are analytical descriptions of that observer, not native spatial coordinates or new classical reference calculations.

Parents: 7e8adcd9dac8e9ae5662c71aed1e2211458f12f0:research_notes/portable_direct/2026-11-25_r6_prefix1075_uniform_positive_tail.md (read full, lower-edge density and C^3 observer); inherited through it PREFIX-1073, 1074 and 1068. Telescoping uses the defining alternating-difference identity and the fixed-n decay, independently of any new path enumeration. Parent conclusions remain author-conditional and not independently reviewed.

## 1. New quantitative theorem

Write m=n-8>=0, f=x^m(1-x)^k, D_m(k)=D(m+8,k)=L(f), a=m+4, b=k+1, mu=a/(a+b). Here a,b are beta shape parameters, unrelated to the regular-band spectral zero b_last. Let 0<eta<1/2. From PREFIX-1075, on a fixed lower-edge interval 0<x<delta<1/9,
    g(x)=A0*x^3+O(x^(3+eta)), A0=h(0)F(4)/(4*36^5)>0,
    F(4)=4283136/5,
and the full observer L has finite C^3 norm. For cutoff tests at zero the local density representation holds including the endpoint, by the scale derivative bounds of the parent.

There exist C_eta,K_eta>0, independent of m,k, such that for all integers m>=0, k>=C_eta(m+1),
    |D_m(k)/(A0*B(a,b))-1| <= K_eta*mu^eta.                  (1)
B(a,b)=integral_0^1 x^(a-1)(1-x)^(b-1) dx. C_eta may be enlarged so the right side is <1/4 and D_m(k)>0. Thus along every sequence with k/(m+1)->infinity, the complete signed BRC observation has the same uniform relative leading term A0 B(m+4,k+1); this is stronger than fixed-m asymptotics or uniform tail positivity alone. No numerical value of C_eta or K_eta is claimed.

Proof: choose a fixed smooth 0<=chi<=1, chi=1 on [0,delta/2], chi=0 on [delta,1]. The parent decomposition is
    D_m(k)=integral chi*g*f + L((1-chi)f).
The error of replacing chi*g by A0*chi*x^3 has absolute value <= H B(a+eta,b), and Jensen for the concave power yields B(a+eta,b)/B(a,b)=E[X^eta]<=mu^eta, X~Beta(a,b). This beta probability is only a normalization of the analytic observer, not a new model input.

The missing baseline A0 integral (1-chi)x^3 f is <= A0*(1-delta/2)^k. The complementary L term is <= H1(1+m+k)^3 (1-delta/2)^(k-3), by Leibniz through order three on x>=delta/2, k>=3 (derivatives of x^m of order >m vanish). Lower bound B(a,b)>=H2 (delta/8)^m(1-delta/4)^k, H2=integral_(delta/8)^(delta/4) x^3 dx>0. Thus the two complementary errors divided by B(a,b) are bounded by H3(1+m+k)^3 (8/delta)^m q^k, q=(1-delta/2)/(1-delta/4)<1. Select C_eta so k>=C_eta(m+1) implies m<=k and (8/delta)^m<=q^(-k/2). This gives H3(1+2k)^3 q^(k/2). Since mu=a/(a+b)>=1/(1+b) and exp decay dominates every fixed inverse power of b, this is O_eta(mu^eta) uniformly; indeed mu>=4/(k+5). Division by A0 proves (1). As C_eta increases, the maximum allowed mu can be made arbitrarily small (a<=4(m+1)). No differentiating little-o and no evaluating classical functions are needed.

## 2. Uniform discrete residual transport

The exact identity D_m(j)=D_m(j+1)+D_(m+1)(j) and the fixed-m decay to zero imply
    D_m(k)=sum_(j>=k) D_(m+1)(j).
Choose k>=2 C_eta(m+1) after enlarging C_eta if necessary, so all successor terms are positive and (1) applies to m and m+1 for all j>=k. Define the normalized residual-transport distribution on integers l>=0 by
    P_m,k(l)=D_(m+1)(k+l)/D_m(k).
It is a genuine probability mass on this positive tail only; the signed observer away from the tail has not been turned into a positive measure. Reference law:
    P0_m,k(l)=B(a+1,b+l)/B(a,b).
This is positive and sums to one by summing x*(1-x)^l inside the beta integral (monotone convergence). It is the beta-geometric law: conditionally on X~Beta(a,b), L has mass X*(1-X)^l.

For the numerator, mu'=(a+1)/(a+b+l+1)<= (1+1/a)*mu<=5mu/4. Applying (1) twice gives
    sup_(l>=0) |P_m,k(l)/P0_m,k(l)-1| <= K'_eta*mu^eta.       (2)
Hence total variation <= K'_eta*mu^eta/2, and the comparison is uniform even for arbitrarily remote l, not merely a bounded observation window. Increase the ratio threshold so K'_eta*mu^eta<1/2 if needed. Every nonnegative statistic with finite reference expectation then has expectation within relative K'_eta*mu^eta of the beta-geometric reference. If the reference expectation diverges, the actual expectation diverges by the same positive lower comparison.

For a fixed positive integer r<a, this yields exact leading factorial moments:
    E_P[(L)_(falling r)] =
      r! * (b)_(rising r) / ((a-1)_(falling r)) * [1+O_eta(mu^eta)].
Indeed a geometric law with success parameter x has factorial moment r!*((1-x)/x)^r (differentiate its convergent generating series r times); integrate to obtain r! B(a-r,b+r)/B(a,b). For r>=a, the beta integral diverges at x=0 and therefore the actual factorial moment diverges. These statements also cover fixed m and arbitrary growing k in the uniform tail. In particular E[L]=b/(a-1)*(1+O(mu^eta)), and the second factorial moment equals 2b(b+1)/[(a-1)(a-2)]*(1+O(mu^eta)). The first three factorial moments always exist since a>=4. This characterizes how residual propagation can have a finite mean but a genuine power-law far tail for fixed path length.

## 3. Survival and a unified crossover law

For every integer l>=0 the exact telescoping identity gives
    P(L>=l)=D_m(k+l)/D_m(k).
By (1) this equals [1+O_eta(mu^eta)]*B(a,b+l)/B(a,b), uniformly over all l>=0. Since a is an integer, the beta ratio has an elementary exact product
    B(a,b+l)/B(a,b)=prod_(i=0)^(a-1) (b+i)/(b+l+i).
Thus the truncation error in reconstructing D_m(k) from the positive successor tail is controlled relatively by this explicit product, even for unbounded l.

Let t>=0, l=floor(t*b/a). Uniformly for t in a fixed compact interval [0,T] and k>=2C_eta(m+1), the product satisfies
    P(L>=floor(t*b/a))=(1+t/a)^(-a) [1+O_(eta,T)(mu^eta)].
To prove the approximation, set h(s)=log(1+l/s). For s>=b, |h'(s)|=l/[s(s+l)]<=l/b^2. The log of the product differs from -a log(1+l/b) by at most l*a*(a-1)/(2*b^2)<=T*a/(2b). Replacing l/b by t/a costs at most a/b in the log. Since a/b=mu/(1-mu)=O(mu) and eta<1, these errors are O_T(mu^eta). Exponentiate and combine (1).

Consequently for fixed m (a fixed), as k->infinity, the scaled residual waiting offset aL/b has survival (1+t/a)^(-a) in the limit (floor or ceil changes the threshold by at most one, asymptotically negligible by the same product bound). When m->infinity and k/(m+1)->infinity, the same scaled offset converges to the unit exponential law, since (1+t/a)^(-a)->exp(-t). For compact t the additional error is O_T(1/a), via the elementary log expansion or its integral bound. The crossover is proved for the normalized positive BRC tail, not for physical time, and not for the signed critical windows.

## 4. Interpretation, evidence and open work

New: uniform relative beta leading term, positive residual-transport law with uniform pointwise relative accuracy, exact factorial moment threshold, and a fixed-length power-law to large-length exponential crossover. These follow by a scoped analytic proof from the full joint observer, the inherited zero-edge cancellation, and exact telescoping. No new path enumeration, native kernel run, classical trigonometric or pi computation, or independent review. No claim of native physical attribution, and no loss of original signed joint state; the probability description is limited to its proved positive tail.

The extremal regular spectral zero locations b_last,b_low and the first boundary remain open. The uniform constants are still existential: numerical certification requires a quantitative delta and derivative/observer norms from the frozen exact BRC carrier. Next: use the proven beta product to design a relative truncation certificate with explicit constants, or derive quantitative lower-band sign bounds from exact weighted density/observer data. Do not redo the parent algebra or numerical pathway. Mother B_fix,odd(32) remains open.
