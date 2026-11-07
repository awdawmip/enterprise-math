# Stage329-B — First global Pareto optimizer transition below the tagged cusp

**Predecessor:** Stage328-B exact cusp marginal-exchange author proof, all-rational witness and executed Fraction/SymPy certificate; upstream Stage327-B / Stage324-B and Stage307-B.2/Stage316-B author claims. **Unreviewed / not admitted.** Observer is a two-source, three-future-visit Bernoulli BRC auxiliary model, not P000-native X6.

## Frozen exact input and proven frontier

For k=0..3, B_k(z)=z^k(1-z)^(3-k), p=(61,21,9,9)/160, r_k=4/5 B_k(x)+1/5 B_k(y)-p_k,
b=5/32 sum_k binom(3,k)|r_k|, D_3(a,z)=1/2 sum_k binom(3,k)|B_k(a)-B_k(z)|,
c=(63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y))/256.
Two-source objectives P=b(x,y)+b(x',y') and T=33/1024+c(x,y)+c(x',y'). Inherited public minimum at r0=r1=0 with root brackets in predecessor.

New Stage328-B derivative theorem: y†=(1+sqrt(13))/8 and r1(x†,y†)=0 define epsilon† in (0.0021814072269,0.0021814072271). The candidate right-branch cost slopes obey phi'(epsilon†+)-phi'(0+)>1/30. Therefore this specific one-block continuation is *not globally optimal* for every epsilon>epsilon† sufficiently close to epsilon†. First loss of that candidate is at most epsilon†, not necessarily equal to it.

Explicit earlier rational witness: q1=(2378087/10^7,575698999217604420/10^18), q2=(23108514/10^8,555512675903066452/10^18) beat the candidate (x*,y*),(X,Y), X=23781/10^5,r1(X,Y)=0, at epsilon_w in (0.002182376328,0.002182376330). Full-law public slack >2547/10^12 and source-tagged cost gain >10733/10^12. Fraction exact computation and symbolic 16-comparison derivative checker executed. All these proofs remain author-only.

## Next discriminating research unit

Prove full global exclusion of any alternative to the one-group right branch on an explicit subinterval of 0.0002<epsilon<=epsilon†, or provide a still earlier exact feasible competing pair. Cover all public-TV and tagged-TV sign chambers, all r0=0/r1=0 kink arms, constrained smooth KKT candidates, asymmetric and symmetric budget splits. A certificate may use rational interval branch-and-bound/KKT with complete coverage and careful algebraic cusp-boundary handling; it must exclude competitors in the full model, not just competing points on the assumed branch.

**Acceptance:** a proved interval of global optimality with exact assumptions and coverage certificate, an exact smaller failure witness, or an independently justified structural necessary/sufficient condition. Never infer a globally actual first switch solely from the tagged cusp. Do not rerun Stage324's old 253-leaf validation merely for startup.

P000 bridge remains separate: ordered signed X6 native steps, explicit 3D slice with third-coordinate semantics, triadic closure, independent time ordering, registered lossless final Cell address and observer-preserving transfer.

## Persistence/authorization

Native dispatch CONTROL_QUOTA and own session STATIC_READONLY_SCOPE_DENIED (operation_sent=false) at Stage328. No CLAIM, Result, Driver review or formal admission can be inferred. Stage328 evidence is stored on the existing Draft PR #1736 author branch; later author research must declare its own actual session and authority, preserve the branch's stage source and not claim independent reviewer status.
