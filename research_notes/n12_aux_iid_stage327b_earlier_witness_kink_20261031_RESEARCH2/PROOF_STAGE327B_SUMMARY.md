# Stage327-B — portable author-only exact counterexample and tagged-cost kink

2026-10-31. Status PORTABLE_AUTHOR_PROOF_AND_COUNTEREXAMPLE / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED. This is an auxiliary 3-future Bernoulli positive-probability two-source BRC model, NOT native X6.

Frozen global source main@970b5c00edacde19d0a8c5b6a6660e77d9877f57; Enterprise Math main@d93aeaece6d8d0916680c5de40ad66a7fbeaa18b. Prior Stage325-B immutable 71e1c73f8ff8c97ffaf2ff73c89e95ea4b9ed48a. Stage326-B author handoff held locally (previous create_commit platform safety refusal) and not represented as canonical. Native owner request CONTROL_QUOTA; session_start STATIC_READONLY_SCOPE_DENIED. No native CLAIM, Source Result or Driver admission.

Define B_k(z)=z^k(1-z)^(3-k), p=(61,21,9,9)/160, r_k=(4B_k(x)+B_k(y))/5-p_k, b=5/32 sum_k C(3,k)|r_k|, D_3(a,z)=1/2 sum_k C(3,k)|B_k(a)-B_k(z)|, c=[63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)]/256. Full inherited public/tagged objectives P=b(x,y)+b(x',y'), T=33/1024+c(x,y)+c(x',y'). Conditional inherited (x*,y*) minimizer is enclosed by x* in (231083940855521,231083940855522)/10^15, y* in (555508857277,555508857278)/10^12.

THEOREM 1 (new strict witness): X=24001/100000, unique Y in (.58,.59) solving r_1(X,Y)=0; q=(2354398,5688542)/10^7. Put eps=b(X,Y)-b(x*,y*). Exact Fraction interval arithmetic yields:
  eps in (0.002863295202,0.002863295203)
  b(x*,y*)+b(X,Y)-2b(q) in (2.5536e-8,2.5537e-8)
  c(x*,y*)+c(X,Y)-2c(q) in (6.4622e-8,6.4623e-8).
Thus the symmetric (q,q) has strictly less public error AND tagged error than the named one-group continuation at this eps, improving the previously proved author-only upper obstruction from <0.003014 to <0.002864. No claim that symmetric q is globally optimal or that the first actual switch is located.

THEOREM 2 (new algebraic cusp): y_dagger=(1+sqrt(13))/8, r_1(x_dagger,y_dagger)=0 with x_dagger in (.237806902,.237806904). The identity B_2(3/4)-B_2(y)=(4y-3)(16y^2-4y-3)/64 gives a unique transverse k=2 tagged discrepancy zero. All other tagged atoms stay nonzero in the isolated box. There r0<0, r1=0, r2>0, r3<0; hence b=15r2/16. Put g(z)=z(2-3z), h(z)=(1-z)(1-3z), y'=-4h(x)/h(y)>0, b'=(15/16)[(4/5)g(x)+(1/5)g(y)y']>0. The one-sided candidate slope jump satisfies
  [dc/db]_+-[dc/db]_-=(21/256)*g(y_dagger)*y'(x_dagger)/b'(x_dagger)
  in (0.11665548,0.11665549).
This is a positive kink of the CANDIDATE r1=0 branch, not proof that the true global Pareto frontier has that kink.

Verified by actual standalone Python fractions.Fraction program with 96 bisections and polynomial endpoint/critical-point interval TV envelopes; result STAGE327B_EARLIER_WITNESS_AND_TAGGED_CUSP_EXACT_PASS. Earlier global author certificates not rerun, and independent mathematical review has not occurred. The local handoff contains the entire proof, program, run stdout and Stage328-B next packet. Next: global rational sign-chamber/KKT exclusions in epsilon (0.0002,0.002864) before claiming first transition. Preserve distinct source/provenance observations; P000 native X6/3D slice/triadic closure/time/Cell encoding remains unbridged.
