# PREFIX-397 — 1250× larger five-Port six-source stability radius by centered polynomial bounds

Date: 2026-10-31. Status: AUTHOR_SIDE_EXACT_VERIFIED / UNREVIEWED / NOT_ADMITTED. Scope: external auxiliary static complex three-amplitude five-Port model only. This does NOT establish native P000 X6, a native three-dimensional slice, or typed BRC dynamics.

## Pinned provenance

GLOBAL_KNOWLEDGE_V1 main@99f2e35a7ceb2c6ae70ff99f10e981db7b3515e9 (bootstrap, manual, P000 projection checked against original blob, ACTIVE worldview and mathematics/BRC rules). Enterprise Math scientific and portable-research input main@adccf931b55c7460362ca035fac7c8d468f04e8d. Immediate reusable predecessor: research_notes/2026-10-31_prefix396_joint_noise_six_source_fiber.md and research_notes/prefix396_symbolic_sextic_checker.py. No existing task owner/CLAIM, Result, or review is claimed by this publication.

## Theorem: all five true intensities vary independently

For the static amplitude matrix
A = [[4,4,0],[0,-4,4],[-5+3i,0,-3+i],
     [-2-2i,4+4i,2+2i],[-2,0,5+2i]]
and nominal intensities
I0=(1,121/100,73/36,532313/23400,11531293/748800),
every positive real intensity vector satisfying max_j |Ij-I0j| <= 1/8000 has EXACTLY SIX inequivalent global-common-phase complex sources. Their real Cayley phase coordinate z has one simple root in EACH of the rational open intervals
(-9/4,-19/10),(-7/10,-3/5),(-1/20,-1/50),(1/10,1/5),(19,20),(150,180).
Every root is regular (elimination determinant nonzero); there are no other singular regular-coordinate sources or Cayley-at-infinity sources.

For the additional coherent observation Cu=|1+u|^2, with additive measurement error |Cu_measured-Cu_true| <= 1/200, all six possible noisy Cu ranges, allowing the ENTIRE five-dimensional intensity uncertainty set, are pairwise disjoint. Thus an observation consistent with this model identifies the unique source-bin label. Outside all six enclosures is a sound rejection; membership in an enclosure alone is NOT a complete realizability certificate. The certified intensity radius 1/8000 is 1250 times the predecessor's 1/10000000; it is a sufficient bound, not an optimum.

## Exact proof and error semantics

Write r=sqrt(I2/I1), k=I3/I1, s4=I4/I1, s5=I5/I1; nominal values are r0=11/10, k0=73/36, s40=532313/23400, s50=11531293/748800. Since I1>=1-xi>0, and r+r0>=r0, all realizable points lie in a four-dimensional rational enclosure centered at (r0,k0,s40,s50) with radii
rho_r=xi(1+121/100)/((11/10)(1-xi)),
rho_k=xi(1+73/36)/(1-xi),
rho_4=xi(1+532313/23400)/(1-xi),
rho_5=xi(1+11531293/748800)/(1-xi).
At xi=1/8000, r>1. This replaces the predecessor's overly loose common 50xi radius without treating the four normalized quantities as independent original measurements.

Set R=1+z^2, U=r(1-z^2), V=2rz, and define
l4=56U+24V+72R; m4=-24U+56V-40R;
n4=78U-8V+(32k+29r^2+53-2s4)R;
l5=980U+492V+980R; m5=-492U+980V-492R;
n5=1418U+(424k+709r^2+709-64s5)R;
D=l4*m5-m4*l5, C=m4*n5-m5*n4, T=l5*n4-l4*n5,
H=C^2+T^2-k*D^2.
The universal exact elimination identity H=(1+z^2)G with deg_z G<=6, and D=(1+z^2)D2 where
D2=(3776-4032r^2)R-256r(1-z^2)+47104rz,
are independently rechecked using SymPy.

For each of the TWELVE rational interval endpoints z*, write delta=(r-r0,k-k0,s4-s40,s5-s50). Expand the entire H(z*,delta) in Q[delta] exactly, retaining cancellations: H=h0+sum_{alpha!=0} h_alpha delta^alpha. Each resulting polynomial has precisely 40 nonzero monomials. The EXACT rational coefficient bound
B(z*)=sum_{alpha!=0}|h_alpha|prod_j rho_j^(alpha_j)
gives H(z*,delta) within [h0-B,h0+B] simultaneously for every point in the box. All 12 certificates have |h0|>B. Endpoint sign pairs are (-,+),(+,-),(-,+),(+,-),(-,+),(+,-). The old direct interval evaluation of C^2+T^2-kD^2 suffers cancellation dependency and did not certify xi=10^-6. The new coefficient expansion removes that specific overestimation; this is not a floating-point root experiment.

Continuity forces at least one root of G in each disjoint interval. Since deg G<=6, there are exactly six and each is simple; degree must equal 6, so the Cayley infinity leading coefficient does not vanish. Interval arithmetic on D2 across each ENTIRE z interval and parameter box gives respectively (-,-,-,+,+,-), all strict. Hence every root lifts to a genuine complex source. A singular solution with D=0 would force C=T=0 from its original two linear equations; H=0 then gives a seventh real G-root outside the six regular bins, impossible.

Finally Cu(z,r)=1+r^2+2r(1-z^2)/(1+z^2) increases strictly with r>1 and decreases with |z|>0. Sorting absolute-value root bins gives
(1/50,1/20),(1/10,1/5),(3/5,7/10),(19/10,9/4),(19,20),(150,180).
Bounding Cu at the rational extremal r,z endpoints yields five exact rational adjacent-bin gap lower bounds, all greater than 2eta=1/100. The minimum gap is approximately 0.010674004546004678; the exact rational margin is in the executable certificate. Subtracting two independent eta uncertainties still leaves all six classes disjoint.

## Executable evidence and genuine limitations

- research_notes/prefix397_exact_checker.py: rational four-variable polynomial operations, 12 centered sign bounds, six determinant interval enclosures, five coherent-observer gaps. Locally executed: PASS_PREFIX397_CENTERED_COEFFICIENT_CERTIFICATE.
- research_notes/prefix397_independent_sympy.py: independently forms universal sextic and D2 identity, audits 36 rational evaluations and two entire coefficient expansions. Locally executed: PASS_PREFIX397_INDEPENDENT_SYMPY_SEXTIC_AND_CENTERED_POLYNOMIAL.
- research_notes/2026-10-31_prefix397_verification_and_next.md records actual arithmetic, source pins, access/owner status and next problem. Local original scripts, exact JSON values, logs and complete proof are also bundled in the conversation evidence archive (SHA-256 in the run summary). Remote source files are intended to be directly reproducible but publication/readback alone is not evidence of remote execution.

The chosen bin geometry did not certify xi=1/7000 under this method; this is not an instability witness. No bidirectional feasibility algorithm for arbitrary measured I and Cu, no optimality result, no physical calibration and no original P000 X6/three-dimensional-slice/typed-BRC transfer have been proved.

## BRC / next mathematical obligation

Retain all six labeled phase-amplitude sources and five individual Port observations; the scalar Cu suffices only for the declared six-label discrimination experiment, not for every future operation. BRC reuse is observer-specific source-fiber/provenance preservation, not execution of native typed BRC.

PREFIX-398: given actual noisy five-Port readings and one noisy Cu value, produce a NECESSARY AND SUFFICIENT certified feasibility test, with quantifier elimination or rational interval existence certificates. An enclosure hit must not be mislabeled as a realizable source. Explore exact indistinguishability witnesses at larger error budgets. Keep all source labels and phase histories.