# PREFIX-403: a 144-candidate exact realizability theorem with noisy I2 and Cu

Date: 2026-11-01. Author-side exact derivation and executable case checks; UNREVIEWED / NOT_ADMITTED / NATIVE_REGISTER_PENDING. This result concerns the **external auxiliary static three-complex-amplitude five-Port inverse model**. It is not a theorem about native P000 X6, the native three-dimensional slice, or typed BRC dynamics.

Source snapshot: GLOBAL_KNOWLEDGE_V1 main@1a1e0968079c9ab3e91279990e164d38f31838a5; Enterprise Math main@f8cc8141ca4c92b793ec694de7bfff9ad5e3bba6. Canonical bootstrap, manual, P000, ACTIVE worldview, BRC and portable research protocols were read with these source pins. PREFIX-401 and PREFIX-402 supply author-side, not independently admitted, predecessor results.

## Question and exact hypotheses

Use the original complex matrix

A = [(4,4,0), (0,-4,4), (-5+3i,0,-3+i), (-2-2i,4+4i,2+2i), (-2,0,5+2i)].

Its first three rows A3 have determinant -32+32i. After choosing global phase, write W=A3 Y=(1,u,v). Then B=A A3^{-1} has the three initial coordinate rows followed by
B4=(5/2+9i/2,3/2+7i/2,4i) and
B5=(11/4+15i/8,11/4+15i/8,5/4+9i/4).

The original Ports are Ij=|(B W)j|². Coherent observers are Cu=|1+u|² and Cv=|1+v|². Fix I1=1. Let I3=k and Cv=q be exact rational numbers; allow I2, Cu, I4 and I5 to lie in **arbitrary rational finite closed intervals** [Lj,Uj], including degenerate ones. The two noisy u-observers are allowed nonzero and independent error widths.

## Theorem — complete finite candidate reduction

Realizability of these six observations is equivalent to a finite list of at most **144 explicitly constructible algebraic source candidates**. A YES candidate reconstructs Y=A3^{-1}(1,u,v); a NO certificate checks at least one violated original observation bound for every enumerated candidate. The algebraic degree of each candidate over Q is at most four. This is a bound on candidate number and field degree, **not** a polynomial bit-complexity assertion.

Proof:

1. Write c=(q-1-k)/2 and D=k-c². If k<0 or D<0 then no complex v exists. If D=0, v=c is unique; otherwise exactly v=c+i√D and v=c-i√D are possible. This derivation is directly from I3=|v|² and Cv=1+|v|²+2Re(v) and does not divide by any eliminant.
2. For each fixed v, define h4(v)=-(a4+c4 v)/b4 and h5(v)=-(a5+c5 v)/b5 from B4 and B5. Then the four remaining observations are **exactly**
   I2=|u|²; Cu=|u+1|²; I4=(29/2)|u-h4(v)|²; I5=(709/64)|u-h5(v)|².
   Thus four rational measurement intervals become four closed annuli in the complex-u plane. Any negative upper bound immediately forces NO; a nonpositive lower bound creates no inner hole. Each annulus has at most two boundary circles.
3. For a fixed v, the feasible intersection K is compact because the I2 upper disk is bounded. If K is nonempty, maximize Re(u) over K. The maximizer is either a radius-zero center, a pairwise intersection of distinct boundary circles, or a left/right extremum of a single active circle. Indeed, in the last case a short arc in the remaining strict constraints would otherwise increase Re(u). Deduplicate identical circles, skip impossible concentric intersections, and enumerate the points. For n<=8 circles there are at most 2n+2*binomial(n,2)=n(n+1)<=72 candidates. A passing candidate suffices, and this argument proves a passing candidate is necessary. Since there are at most two v branches, the total is at most 144. Tangencies and zero-radius circles remain covered.
4. v belongs to K0=Q(√D), with [K0:Q]<=2. All circle centers belong to K0 and squared radii are rational. Extremal points and pairwise-circle intersection coordinates require at most one further square root over K0; their degrees over Q are at most four. Standard exact real-algebraic isolation/sign comparison decides every inequality. No numerical root scan is used in the mathematical completeness proof.

## Exact witnesses, exclusions and observer/provenance boundary

Let u0=59/63, u*=u0+i/10000, v*=1+i, k=2, q=5. Take I2 and Cu in nominal-centered intervals of radius 10^-8; fix I4=110122857795101/793800000000 and I5=1766982026494021/25401600000000 exactly. The complete algorithm returns **YES** with an original-source witness after 13 checked candidates, resolving the frozen-u false negative from PREFIX-402.

If I2=u0² and Cu=(1+u0)² are instead exact, then u=u0. With k=2 and q=5, v is 1+i or 1-i. Neither reconstructs the specified fourth-Port reading: the two differences (observed minus reconstructed I4) are 720029/200000000 and -262384879391/4200000000, both nonzero. Thus this record is rigorously **NO**; the implemented enumerator checked 38 candidates.

For k=2,q=3,I2=0,Cu=1 and I4,I5 in [0,1000], two distinct real sources u=0,v=+i√2 and u=0,v=-i√2 are both realizable. Indeed |a4|<6 and |c4 v|<6 imply I4<144; |a5|<4 and |c5 v|<4 imply I5<64. The v branch sign therefore remains future-observer-relevant provenance and must not be removed by source compression.

## Verification and next target

Executed Python 3.13.5 / SymPy 1.14.0:
- prefix403_exact_solver.py: PASS_PREFIX403_144_CANDIDATES_NOISY_U_EXACT_I3_CV (rational YES/NO and irrational-v YES/NO).
- prefix403_independent_original_A.py: PASS_PREFIX403_INDEPENDENT_ORIGINAL_A_NOISY_U_AND_TWO_V_BRANCHES (independent original A3 inverse, exact Port reconstruction and both frozen-branch differences).

The implementation aborts if SymPy cannot prove a demanded algebraic sign; an unknown comparison is never silently interpreted as NO. Universal theoretical decidability follows from the proved finite enumeration with a complete real-algebraic-number comparator; program execution is reported only for tested cases. BRC reuse resolution: REUSE_APPLIED for source-fiber/observer preservation; **no typed BRC computation** or heartbeat-native bridge was performed. Current native service reports research_authority_granted=false, control result CONTROL_QUOTA; an ordinary GitHub publication is not a session, Claim, formal Result or admission.

Next PREFIX-404: allow I3 and Cv also to have nonzero rational intervals, so v ranges over a continuous two-annulus region rather than two algebraic points. Build a complete, executable four-real-variable semialgebraic realizability decision, preserving singular fibers and all Port/provenance labels. Use PREFIX-402 branch-separation as a stress test, not a substitute for two-way feasibility.
