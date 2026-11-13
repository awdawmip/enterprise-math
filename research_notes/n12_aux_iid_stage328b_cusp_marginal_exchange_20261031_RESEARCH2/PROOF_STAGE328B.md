# Stage328-B — Exact cusp marginal-exchange obstruction and earlier rational two-block witness

2026-10-31. Classification: PORTABLE_AUTHOR_PROOF_AND_COUNTEREXAMPLE / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED. Auxiliary three-visit, two-source Bernoulli BRC model; not P000-native X6 dynamics.

## Frozen evidence, authority

GLOBAL_KNOWLEDGE_V1 canonical main@bab8501c72c23032c08c8dea882d5430007e4a59 (governing bootstrap/manual, EM project router, ACTIVE worldview, P000 projection checked against original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc). Enterprise Math main@cadef72c7c0768fa79c822812c76f753459cbb80 (docs/PORTABLE_RESEARCH_PROTOCOL.md). Predecessor Stage327-B at 740ad84cafee89cf6e595ed88593be80f7ba7251. Stage307-B.2 minimizer and Stage316-B eight-rate reduction are inherited author-only. Native dispatch: CONTROL_QUOTA; own session start: STATIC_READONLY_SCOPE_DENIED, operation_sent=false. No current authenticated task owner, native CLAIM, Source Result or Driver review.

## Model

For k=0,1,2,3 put B_k(z)=z^k(1-z)^(3-k), p=(61,21,9,9)/160, and r_k(x,y)=4/5 B_k(x)+1/5 B_k(y)-p_k. Define

b(x,y)=5/32 sum_k binom(3,k)|r_k(x,y)|,
D_3(a,z)=1/2 sum_k binom(3,k)|B_k(a)-B_k(z)|,
c(x,y)=[63 D_3(1/4,x)+D_3(3/4,x)+9 D_3(1/4,y)+7 D_3(3/4,y)]/256.

The inherited eight-port reduction is P=b(x,y)+b(x',y'), T=33/1024+c(x,y)+c(x',y'). All word multiplicities and source labels are retained. The inherited unique public minimizer (x*,y*) satisfies r0=r1=0 and
231083940855521/10^15<x*<231083940855522/10^15,
555508857277/10^12<y*<555508857278/10^12.
Let beta*=b(x*,y*).

## Theorem A: failure arbitrarily close to the tagged cusp

Set y†=(1+sqrt(13))/8, let x† be the unique r1(x†,y†)=0 root in (0.237,0.238), and set epsilon†=b(x†,y†)-beta*. Exact rational intervals certify

21814072269/10^13 < epsilon† < 21814072271/10^13.

Parameterize the increasing r1=0 right branch from (x*,y*) by s=b-beta* and write phi(s)=c(x(s),y(s)). Then exact one-sided slope bounds are

-1.197919<phi'(0+)<-1.197917,
-1.163998<phi'(epsilon†+)<-1.163995,

hence phi'(epsilon†+)-phi'(0+)>1/30.

**Proof.** On the branch r1=0, r0<0, r2>0, r3<0, so b=15r2/16. Write h(z)=(1-z)(1-3z), g(z)=z(2-3z). By r1_x=4h(x)/5>0 and r1_y=h(y)/5<0, y'=-4h(x)/h(y)>0, B'=db/dx=15/16[(4/5)g(x)+(1/5)g(y)y']>0. Check all 16 source-tagged Bernoulli comparisons: the only sign crossing near y† is B_2(3/4)-B_2(y) in the 7D_3(3/4,y) term. Exact symbolic polynomial differentiation then gives c_x=-(1-x)(189-183x)/256, c_y(left)=3y(1-y)/64, c_y(right)=3y(1-y)/64+(21/256)g(y). Thus phi'=(c_x+c_y*y')/B'. An exact algebraic root bracket for 16y²-4y-3, a rational r1-root bracket for x† and the inherited (x*,y*) brackets yield the stated strict slope inequalities.

For all epsilon>epsilon† sufficiently close to epsilon†, by continuity within the right chamber phi'(epsilon)>phi'(0+). Let H(t)=phi(epsilon-t)+phi(t) for 0<t<epsilon-epsilon†. Then H'(0+)=phi'(0+)-phi'(epsilon)<0. Some positive t therefore produces a strictly cheaper **two-group** allocation with exactly the same public budget. The old single-block candidate is not globally optimal for any such epsilon, so the infimum of failure budgets is **at most epsilon†<0.002181407228**, possibly earlier. This does not establish a global Pareto kink exactly at epsilon†.

## Theorem B: fully rational earlier competitor

Let X=23781/100000, and Y be the unique real r1(X,Y)=0 root in (0.575,0.576). Compare the one-block candidate (x*,y*),(X,Y) with

q1=(2378087/10^7,575698999217604420/10^18),
q2=(23108514/10^8,555512675903066452/10^18).

The full public- and tagged-word exact rational interval checker proves

2182376328/10^12 < epsilon_w=b(X,Y)-beta* < 2182376330/10^12,
b(x*,y*)+b(X,Y)-b(q1)-b(q2)>2547/10^12>0,
c(x*,y*)+c(X,Y)-c(q1)-c(q2)>10733/10^12>0.

Both public and tagged TVs are strictly smaller for the admissible rational pair. This witness at epsilon_w<0.002183 improves the previous Stage327-B witness epsilon<0.002864. It does not assert that (q1,q2) is globally optimal.

## Verification and scope

The author-side Python Fraction and SymPy exact-polynomial verifier was actually executed (both STAGE328B_LOCAL_CUSP_MARGINAL_EXCHANGE_EXACT_PASS and EXPLICIT_RATIONAL_TWO_GROUP_WITNESS_PASS). The verifier isolates Y†, X† and Y roots with rational endpoints; checks all 16 tagged comparisons and exact symbolic derivative identities; evaluates outward interval bounds for candidate and competitor. Exact interval computation, not a finite float grid, proves the displayed strict inequalities. The Stage324 253-leaf global certificate was not re-run. All inherited Stage307/316 statements remain author-only and have not undergone independent review or native admission.

**Next Stage329-B:** obtain a complete global exclusion of smooth, kink and allocation competitors over 0.0002<epsilon<=epsilon†, or produce an even earlier exact witness. Distinguish alternate one-block branches, asymmetric/symmetric splits, and the tagged cusp. P000's native signed X6 paths, three-dimensional slice including its third coordinate, triadic closure, independently ordered time and registered lossless final Cell addresses remain separate proof obligations.
