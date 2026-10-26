# Stage165 exact portable continuation: DUAL CANDIDATE ONLY

**Source:** Stage164 author full-real proof in this same directory. Frozen GLOBAL_KNOWLEDGE_V1 main@ad6b20175a75b09038ffaa5e43ec737463299e1e; Enterprise Math input main@658da84476e2ed11d5b243f35246ca0c4aefdb7c. Native owner/CLAIM/Result not verified. External finite ternary iid N14 model only; never treat this as a P000 X6 native result.

## Mother question and frozen model

Minimize V14(alpha)=inf max(tP,tQ) over all ordered-history random policies with eP,eQ <= alpha, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), n<=14. Keep first-hit ordered branches and P/Q positive rational weights. Existing Stage164 is complete as author proof (not independently reviewed); do not rerun it to fill a new stage.

## Completed exact Stage164 frontier

V14(alpha163+delta)=V163-(1249192/2175)*delta, every real delta in [0,17071484375/17158292304297984].
alpha164=62947091618416625195/180720939287325966336
V164=2138584004831606037541/180720939287325966336
Stage164 Bellman ties R=(10,0,1) Q/continue and S=(13,5,2) P/continue. First-hit counts 10/12056, four observer corners, zero mixed term, whole interval and right sharpness are in PROOF_STAGE164.md and certificate164_author.json. S reaches coin=1 at right endpoint; R is interior.

## New Stage165 dual-only candidate

From K164=211248/725, L164=615448/2175, follow dK=-1, dL=-10592/12501, fixing S to immediate P and keeping R tied. First new closure at t=620572679343/36028070975 produces
K165=13623672285/49693891
L165=40009085000/149081673
K165+L165=80880101855/149081673.
The exact two ties are R=(10,0,1) Q/C and G=(10,7,3) P/C; other 1238 gaps >0, min=8257109179793/821825520500736; root=819944053177461253554178891/4083385870731431154548736. Candidate is NOT a primal certificate.

## Smallest independent next scientific unit

Compute exact R/G first-hit ordered history counts and rational P/Q masses with S fixed P, then all four corners of M(r,g)=(eP,eQ,tP,tQ) with strict Bellman actions. Since R and G have same depth but different counts, their ordered first-hit cones cannot intersect. Check mixed coefficient zero with an unmerged ordered DFS (integer PN=(3,1,20), QN=(1,1,10)) independently of Fraction count-suffix recursion. Solve eP=eQ, determine legal coin segment, check inherited alpha164,V164 at the correct end, tP>=tQ, exact H0 dual equality, and strict right sharpness; report a rational obstruction if any of these fail. Preserve full-real quantifier and authored-vs-independently-reviewed distinction. Carry precise code/cert/log provenance.