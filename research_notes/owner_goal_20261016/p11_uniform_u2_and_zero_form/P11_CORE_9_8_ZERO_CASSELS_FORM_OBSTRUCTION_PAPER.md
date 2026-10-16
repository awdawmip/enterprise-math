# A contrasting core (9,8): vanishing first Cassels form leaves a genuine rank boundary

Status: UNREVIEWED NEW AUTHOR PAPER, separate from the first five objects. EM-DVR-F73673. This is a negative boundary for a proposed rank classifier, not a new Task, rank computation, Native Result or extension of the fixed(233,119) certificate Task. Zero arithmetic programs, searches or enumerations.

Take the primitive opposite-parity Euclidean core (r,s)=(9,8). Then
A=81−64=17, B=144, C=145,
P=A+B=161=7·23, Q=B−A=127,
R=P−Q=34=2·17, S=P+Q=288=2^5·3²,
D=RS=9792=2^6·3²·17=24²·17.
The displayed small primes are certified on paper: 127 has no divisor among2,3,5,7,11 (all primes≤sqrt127); the smaller primes have the immediate corresponding checks. Both161 and127 have only3mod4 prime factors (7,23,127), in fact all are7mod8. These are exact hand identities, not output from a factorization program.

By the complete parameter-local theorem and its closed prime-support corollary, the full2-Selmer group is exactly
W={(1,b,b): b∈〈−1,2,3,17〉}, dim W=4.
At2 and p3,p17 the image is vertical; at7,23,127 it is the unit-pair image. First-coordinate coefficients are all killed, and only these four second-coordinate classes remain. The support is {2,3,7,17,23,127} plus sign.

The rational torsion classes U_(-1) and U_D=U_17 are independent and lie in the radical. Representatives for the remaining two quotient directions are U2=(1,2,2) and U3=(1,3,3). They are locally soluble, not claimed global points.

Apply only the fourth frozen paper's complete local-symbol formula; the fifth reciprocity simplification is unnecessary here. For a=2,b=3:
* The real factor is1 since3 is positive.
* At2,16|S, so F has class−2. The norm N(1+sqrt3)=−2 proves (-2,3)_2=1.
* At17|R, both−1 and3 are units, so (-1,3)_17=1.
* At3|S,−2 is a unit congruent to1, hence (-2,3)_3=(-2/3)=1.
* For each p=7,23,127 dividing PQ,2 is square because p≡7mod8. Thus eta_p(2)=0 and the PQ exponent correction is1.
* Every other place contributes1 by the fourth paper's uniform outside-support proof.

Therefore <U2,U3>=+1. Alternation gives trivial self-pairings; bilinearity and the two rational radical rows show that the entire Cassels form on W is trivial. This is an exact zero-form conclusion, subject to the stated source and parameter theorem dependencies. It is not inferred from a missing negative witness.

The standard exact Kummer sequence gives
rank E(Q)+dim Sha(E/Q)[2]=2.
A zero form supplies no rank reduction beyond rank≤2. It does not prove rank2, rank0, a global representative for U2/U3, saturation, finite Sha or any positive/negative infinite-family decision. Its radical is W, so the nondegenerate-quotient argument that proved rank0 and elementary two-primary Sha for core(5,4) cannot be used here. Possible further4-descent/divisibility information or independently proved rational points are genuinely new inputs; none is supplied or presumed.

This is the explicit stop/branch for the reusable finite interface: after the complete local table and the exact first pairing return this zero form, stop claiming a rank discriminator. A later bounded unit could distinguish the remaining arithmetic possibilities with a precisely specified4-Selmer/descent certificate, but this paper creates no such unit and authorizes no point search or resource expansion. In particular a zero Cassels matrix is not an “empty result” or a license to retry parameters until one has a nonzero sign.

Sources: the exact new parameter-local/closed-dimension papers are preserved at Source270c9c6470db2cb14885f82d1021754f2bf19b23 under research_notes/owner_goal_20261016/p11_parametric_local_images/. The fourth local-symbol paper is frozen9927B SHA721e23197a05e469040d1b865e43d7a7a6bf2520c61f6466a812a4e1c8a4ea37 and independently PAPER_PASS at its own scope by real nonauthor Driver EM-DVR-BFF6DC; its actual Source binding remains a separate boundary. Its PASS is not an independent review of this new numerical-symbolic input. Stoll's full2-Selmer exact sequence and the FSS/Shukla–Stoll pairing theorems are inherited with their exact models/versions from those papers.

The comparison is deliberately scoped: core(5,4) has a nonzero first pairing and paper rank0; core(9,8) has a zero first form and unresolved rank. Neither says anything new about the exact fixed(11,8) rank1 certificate Task or whole-family classification. External classical arithmetic remains distinct from native HeartbeatX6 geometry, with no WT/Foundation/sharedTool registration. A genuine new nonauthor paper check is required.

