# PREFIX-1128 — Scale localization and affine integer strip

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED.
Researcher EM-DIRECT-780BBE / TASK_RESEARCH, own registration r6-20261123-2358-session-start-own-v1 SUCCEEDED; Activity RA-0ABD84561C86E53067DB0322. Owner query r6-20261127-1454-leased-observe SUCCEEDED, error=null, LEASED tasks=[], next_cursor=null, as_of 2026-11-27T06:55:06.592424Z, Source d87f9ff4e3e700d84179bf4c9290a65f7ac19066. No CLAIM or shared Task mutation.

## Inputs and scope

Continue PREFIX-1127 at 291ba0ab7eb930acccda5aa13e8b5aa7108ee3db:research_notes/portable_direct/2026-11-27_r6_prefix1127_candidate_conditioned_strip.md and its standalone certificate at 5de6c6fc91b7dbf9679b5665047f8f168c5d959b:research_notes/portable_direct/2026-11-27_r6_prefix1127_joint_strip_verify.py (SHA256 20ae084c4f4c8adb38ee38d2ab50e615d2a29352a0a259b3dbf90c9df916c9b0, locally verified). Frozen P000 V5 and joint observer / X6 time / residual fidelity companions read at f42f2906d77f24085c123f3ccfe9667d41caa96d; canonical account entries at b9f3e3dcf116aef89dcd0f05745fc820a9d9c900. Preserve signed reversal -5, 5q cover, chart O incoming -e1, next incoming -d, both orientations Link{O,e1} blocked without renormalization, exactly two negatives. The integer relation coordinate and spectral readouts are auxiliary observers of this inherited signed X6 carrier, not native spatial axes or time. All computations use the frozen outward BRC enclosure; no new moment anchor, CT enumeration, or classical replacement of native arithmetic. Inherited root isolation, carrier correspondence, analytic boundary theorem and 8400/8800 command-exit uncertainty remain conditions.

## 1. Exact affine strip theorem

Use f(m)=rho*m+c+d/m and |f(m)-j|<=E/m^2 with E=400000. For any pair in [L,2L), its primitive integer relation qj-pm=h has q>=q0 for L>=10^90 by inherited exclusion. Put delta=rho-p/q, eta=h/q-c. PREFIX-1123 gives k/L^2<=delta<=K/L^2, g/L<=eta<=H/L with positive k,g and explicit K,H as in the verifier.

Let T,R,C be the certified intervals for t*,rho,c; x and c0 the frozen reference values. From PREFIX-1127, A=F'(T)<0, B encloses (G-sF)(x), D encloses (G-sF)'(T), and G(t*)=(c-c0)F'(t*). By the mean-value theorem there exist b in B, a in A and v in D with (c-c0)a=b+(t*-x)v. Set rho_x=36/x^2-1. The exact rational identity

    t*-x = -(rho-rho_x)*t*^2*x^2/[36*(t*+x)]

follows by subtracting the two reciprocal squares. No Taylor truncation. Enclose the coefficient by interval J=(-x^2/36)*T^2/(T+x); S=D*J/A. Choose kappa=mid(S) and i=c0-kappa*rho_x. Then with ordinary enclosing interval arithmetic

    c-kappa*rho-i in P := B/A+(S-kappa)*(R-rho_x).

This retains the signed shared anchor direction; the exact coefficient identity and residual enclosure make the reduction valid for the declared affine exclusion observer. The original full BRC carrier remains available for other observers. Since h/q=c+eta and p/q=rho-delta,

    Z(q,p,h):=h/q-kappa*p/q-i in P+kappa*[0,K/L0^2]+[0,H/L0]

for every L>=L0. Here kappa>0 is verified. This is an affine rational constraint on the *joint* integers, not separate boxes. The frozen certificate gives kappa approximately 4.799830397021008, P subset (-3.085e-92,3.090e-92). All arithmetic uses exact rationals with enclosing products, no independence asserted.

## 2. Scale localization

For a fixed primitive line Z>P_upper, the stronger two-sided signed pair constraints give

    g/(Z-P_lower) <= L <= (H+kappa*K/L0)/(Z-P_upper), L>=L0.

Proof: Z=P_actual+kappa*delta+eta, hence Z-P_lower>=g/L and Z-P_upper<=H/L+kappa*K/L^2<=(H+kappa*K/L0)/L. These bounds exclude a fixed line at sufficiently large scales without any new spectral precision. If Z lies in P the upper-bound conclusion is not claimed.

At L0=10^90 and q<=2*10^59 the exact affine strip recovers the same seven candidate lines from PREFIX-1127 (ordered by q). Their upper scales divided by 10^90 are approximately 1.010609, 1.152091, 1.295472, 1.588089, 1.737406, 1.888781, 2.042260; all strictly below 2.043 by rational comparison. On the fixed dyadic sequence L=10^8*2^n, the first L>=10^90 is approximately 1.517710072e90; the next already exceeds every upper scale. Only four of the seven lines remain at that first window, with smallest denominator 157915136333228082417423528698944751801766005910505403078499. This is an exclusion certificate, not a construction of a real pair. All seven disappear for L>=10^91; indeed the transformed integer box for q<=2*10^59 has an empty coordinate range.

## 3. Affine strip adapted integer coordinates and exact computation

For q0<=q<=Q, let r=p/q and z=Z(q,p,h). Enclose r by [rho_l-K/L0^2,rho_u] and z by the interval in section 1, retaining the c marginal too. A row (a,b,e) of an integer unimodular matrix V satisfies

    n=q*(a+e*i+(b+e*kappa)*r+e*z).

The extrema on the enclosing q,r,z box occur at its eight corners (multiaffine). Choose V using exact rational Gram-Schmidt/LLL on a rounded anisotropic embedding of these observation directions; its optimality is irrelevant. Check determinant +/-1, exact inverse, and enclosing coordinate bounds. Enumerate the finite integer box or eliminate its third coordinate using exact linear inequalities. Filter the original inequalities and gcd(p,q)=1. This gives exhaustive coverage, not a sampling argument. In particular the affine relation is incorporated before enumeration, not used only as a post-filter.

Actual independent full box verification (all exact):

- L0=10^90, Q=2e59: ranges [0,0],[-2,0],[-28,10], 117 integer points, 7 primitive candidates. Same seven as prior batch. Prior independent box contained 27950 points and 595 candidates before its strip filter. The new enclosing box is about 239 times smaller for this exact comparison; no wall-time complexity claim.
- L0=10^91, Q=2e59: ranges [0,0],[1,0],[-20,9], empty. This excludes the full tail at that denominator cap.
- L0=10^100, Q=3e60: ranges [-1,2],[1,5],[-16,14], 620 points, 115 candidates, minimum

    q=704830121671781357562188570181003663463817577529892083528277
    p=15111583690290265361910097499591303255690478646004698769663152
    h=69877570449453801340258215642018962660689140809934967422785021

Thus any real pair at L>=10^100 has gap >=q (smaller q0 excluded by inherited certificate, q>Q already larger). At this scale q is about 6.83 times the preceding lower bound, not a bound asserted for all L>=10^90. At L>=10^100 the sharp curvature theorem q^2<4EL/d gives first not-excluded fixed dyadic triple window

    3669597785584114418577313432483339105274503982669249797980142143019076601741575692912029684976201098487398400000000

and gap<=sqrt(L) implies first not-excluded fixed dyadic near-pair window

    961963041904162090143531252444912446413079572032847819041706381939592816686943618442731109738401260761880566169600000000.

For the earlier windows use PREFIX-1127's already certified exclusions (both old boundaries exceed 10^100); no gap in the stitched exclusion range. The new bounds are approximately 3.669597786e114 and 9.619630419e119, respectively 32 and 64 times the old dyadic boundaries. The first remaining line is not proved attainable within the full shared anchor relaxation or by actual BRC coefficients. The 115 candidates are necessary-condition survivors only.

## 4. Evidence and continuation

Actual local execution: prefix1128.py generated six exact scans and full box checks (117,0,0,40,2400,620 points); prefix1128_verify.py independently verified the three principal scans using fixed explicit integer matrices, no LLL library. Both exit 0. The remote verifier at a98a6aab28f0da9bbe120db93fd3791b876a2eb1:research_notes/portable_direct/2026-11-27_r6_prefix1128_affine_strip_verify.py has Git blob 4cc7f9cad9debdbd958d6b86e2e405fd5d319de5 matching actual executed local bytes; SHA256 6494e62f1db5dd920b2bda74b43addadb0e57b3c454cbdcc480604e3bfc3e5c5. Copy pinned PREFIX-1127 verifier as prefix1127_verify.py and run this verifier in the same directory. The local evidence archive contains both programs, exact result JSON (all 115 tail candidates and auxiliary scans), logs, frozen source verifier and hashes. SHA256 prefix1128.py 42525f0783c74e7a61d3c4ccb3db01f5adcf4033eac511b36131e672c2b4a94f; result JSON e0bbcce33159da704d4f8bd651955f52cdc4a8749f8da23f6985a05b456fec54; standalone execution log 326843d3d3d1aae89cbe3c06e609063e425fa4050369fc38b5a2e387e070c72f. No new BRC anchor or native CT enumeration. Independent mathematical review and Activity observation audit pending.

Next: use the affine strip as a direct lattice coordinate, refine candidate-specific scales with the full signed anchor zonotope and joint derivative columns. Determine the attainable set under the complete shared anchor constraints rather than treating the strip as sufficient. The one endpoint ambiguity at m=47247757565973207955345875119021762026915609 remains; continuous integer endpoint certificate unchanged. Unbounded single anomaly separation, exact zero and B_fix,odd(32) remain open. Do not redo 9600 anchoring.
