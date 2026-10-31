# Stage335-B: exact rectangular Pareto uniqueness of the public r1=0 cusp

Date: 2026-10-31. Status: PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_SYMBOLIC_EXECUTED / UNREVIEWED / NOT_ADMITTED. **This is a theorem of a labelled three-visit Bernoulli/BRC auxiliary observer; no P000 native X6 transfer or whole-two-source global Pareto conclusion is claimed.**

## Source and authority

Frozen global knowledge: awdawmip/chatgpt-global-knowledge main@183f4a4eef6edc24eca6d4e25443d46366aaddbe; Enterprise Math canonical main@f54107bc7e398df175e435dfe3d9140619f9819b. Read canonical bootstrap/manual, original P000 (blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc), ACTIVE worldview, TASK_RESEARCH role, current portable protocol. Scientific predecessor Stage334-B is PR #1736 commit ecb16e8ba7a7c65142ebf4d419733402f203a79d, especially PROOF_STAGE334B.md and NEXT_TASK_PACKET_335B.md. This result rederives its own signs on a smaller rectangle; the new rectangle theorem does not require assuming the earlier unreviewed global sign-census proofs. Native status research_authority_granted=false; current owner query returned CONTROL_QUOTA. No native CLAIM or independent Driver review.

## Exact labelled model

For k=0,1,2,3 let B_k(z)=z^k(1-z)^(3-k), weights w=(1,3,3,1), target m=(61,21,9,9), r_k(x,y)=[4B_k(x)+B_k(y)]/5-m_k/160, b(x,y)=(5/32)sum_k w_k|r_k(x,y)|. Define D_3(a,z)=(1/2)sum_k w_k|B_k(a)-B_k(z)| and c(x,y)=[63 D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)]/256. All four binomial words, multiplicities and source tags are retained; sum_k w_k r_k=0. Previous two-source objectives are P=b(q1)+b(q2), T=33/1024+c(q1)+c(q2). Here we prove one-source optimality on a specified rectangle only.

## Exact theorem

Set R=[233/1000,119/500] x [561/1000,3/5]. For **every real** x0 in [233/1000,119/500], there is exactly one real y0=Y(x0) in (561/1000,577/1000) such that r1(x0,y0)=0. It has b(x0,y0) <= 96689637/16000000000 < 61/10000.

**For every real q0=(x0,Y(x0)) and every real q=(x,y) in R,**

    b(q) <= b(q0) and q != q0   ==>   c(q) > c(q0).

Consequently every point of this r1=0 arc is the **unique global tagged-cost minimizer at its own public-error budget among ALL points of R**, including at the tagged algebraic cusp y_d=(1+sqrt(13))/8. It is a continuum of non-excludable boundary candidates; outside-R competitors and two-source budget reallocations remain open.

## Proof A: continuous sign and root bounds

B0'(z)=-3(1-z)^2<0, B2'(z)=z(2-3z)>0 and B3'(z)=3z^2>0 on R. Therefore exact rational corner evaluations give

    r0(x,y) <= r0(233/1000,561/1000) = -16774829/5000000000 < 0;
    r2(x,y) >= r2(233/1000,561/1000) = 23471171/5000000000 > 0;
    r3(x,y) <= r3(119/500,3/5) = -707807/312500000 < 0.

Also r1_x=(4/5)(1-x)(1-3x)>0 and r1_y=(1/5)(1-y)(1-3y)<0 on R. The exact corner values are r1(233/1000,561/1000)=151829/5000000000>0 and r1(119/500,577/1000)=-234879/5000000000<0. Monotonicity and the intermediate value theorem give exactly one y0 in the specified open interval for each x0, and Y is strictly increasing. With r1=0 the weighted mass conservation yields b=15r2/16. Since r2 increases in both coordinates, b(q0) < (15/16)r2(119/500,577/1000) = 96689637/16000000000 < 61/10000.

## Proof B: exact public and tagged derivatives

On the whole R only r1 may change sign. The **original absolute value expression** equals max(b_minus,b_plus), where b_minus=15r2/16 and b_plus=15(r1+r2)/16. Indeed b_plus-b_minus=15r1/16. Their partials are

    (b_plus_x,b_plus_y)=(A,B), A=3(1-2x)/4>0, B=3(1-2y)/16<0;
    (b_minus_x,b_minus_y)=(C,D), C=3x(2-3x)/4>0, D=3y(2-3y)/16>0.

Full labelled Bernoulli comparison sign words (k=0,1,2,3) on R are x vs 1/4: -+++, x vs 3/4: --++, y vs 1/4: ++--, y vs 3/4: --sigma+. The only switch comes from B2(3/4)-B2(y)=(4y-3)(16y^2-4y-3)/64, at y_d=(1+sqrt(13))/8 in R. The other signs follow from Bk monotonicity and exact endpoint comparisons. Differentiating **all 16 tagged terms** with their multiplicities gives c_x=-p(x), p(x)=(1-x)(189-183x)/256>0 and

    c_y=q(y)=3y(1-y)/64 for y<y_d;
    c_y=q(y)=3y(18-25y)/256 for y>y_d.

At y_d, c is continuous; the one-sided expressions hold, and integration across that lone kink is valid.

## Proof C: exact uniform ratio gap

For all x,y in R, p(x)>43/100: its minimum at x=119/500 is 27707463/64000000. Also 0<A(x)<=801/2000, -B(y)>=183/8000, and 0<q(y)<49/2000. For y<y_d, q(y)<=3/256<49/2000. For y>y_d, 23/40<y_d (because 13>(18/5)^2) and q(y)=3y(18-25y)/256 decreases for y>23/40; hence q(y)<=q(23/40)=2001/81920<49/2000. These inequalities also bound both one-sided values at y_d.

Consequently, **uniformly on the whole rectangle**,

    p(x)/A(x) > M=860/801 > N=196/183 > q(y)/(-B(y));
    M-N=128/48861>0.

Let q0=(x0,y0) be a point of the r1=0 root graph and let b(x,y)<=b(q0)=b0.

If y>=y0 and x>=x0 with (x,y)!=q0, the strict increase of b_minus in both coordinates gives b(x,y)>=b_minus(x,y)>b_minus(q0)=b0, contradiction. Hence x<x0, and c(x,y)-c(q0) = integral_x^x0 p(u)du + integral_y0^y q(v)dv >0.

If y<y0 and x>=x0, the strict increase of b_plus in x and strict decrease in y gives b(x,y)>=b_plus(x,y)>b_plus(q0)=b0, contradiction. Hence x<x0. Put Sx=integral_x^x0 A(u)du>0 and Sy=integral_y^y0 (-B(v))dv>0. From b_plus(x,y)<=b(x,y)<=b0=b_plus(q0) we obtain Sx>=Sy. The exact ratio gap gives

    c(x,y)-c(q0)=integral_x^x0 p(u)du-integral_y^y0 q(v)dv
      > M*Sx-N*Sy >= (M-N)*Sy
      >= (2/33375)*(y0-y) > 0.

This is a rigorous **all-real-parameter**, all-points-in-R proof, not a finite sample. Both cases prove the theorem. The same argument applies if any integral crosses the tagged y_d cusp because c is continuous and piecewise differentiable.

## Verification, BRC reuse and remaining work

REPRO_STAGE335B_COMPACT.py uses exact Python Fraction and symbolic SymPy operations, verifies the four-word conservation, the three continuous corner signs, the root-endpoint signs, four branch derivative formulas, complete tagged signed derivative formulas and tag switch, exact rational uniform gap and public budget bound. It was executed twice with byte-identical stdout; the attached log ends STAGE335B_RECTANGULAR_R1_UNIQUE_CONSTRAINED_PARETO_EXACT_PASS. Continuous coverage comes from the monotonicity and integral proof above, not from the computer's finite sign checks. Status: author proof, arithmetic/symbolic executed, unreviewed and not canonically admitted.

**Next Stage336-B:** r0=0 and r3=0 zero strata, pair-zero intersections, possible outside-R single-source branches and the exact additive two-source allocation; find a strict competitor or certify complete global exclusion. The present source-labelled auxiliary observer has no demonstrated lossless mapping to P000 native X6 dynamics, third slice coordinate, triadic balance, independent time or final Cell address.
