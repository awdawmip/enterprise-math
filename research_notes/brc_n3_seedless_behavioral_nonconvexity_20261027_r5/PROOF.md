# Exact N=3 nonconvexity of four-observable seedless time/LR compression

Date: 2026-10-27. Status: author-level proof with exact rational verification, **not** an independent Driver review, native Result, active Task CLAIM, or native P000/X6/Heartbeat dynamics result.

## Exact question and model
For finite ordered P/Q observation trees with positive rational branch probabilities, let O=(P(decide Q), Q(decide P), E_P(tau), E_Q(tau)). The question is whether the attainable four-vector image of policies observing only (time, exact L=P/Q), using independent local behavioral randomization without a persistent root seed, must be convex. The answer is **no**, already at horizon N=3 with eight leaves.

The branch probabilities (Q conditional; P conditional) are:

| Node | Children | Q | P |
| --- | --- | --- | --- |
| root | a,b | 1/3,2/3 | 2/3,1/3 |
| a | x,y | 1/2,1/2 | 1/4,3/4 |
| b | x,y | 2/3,1/3 | 1/3,2/3 |
| ax | u,v | 16/21,5/21 | 1/21,20/21 |
| ay,bx,by | u,v at each node | 1/2,1/2 | 1/2,1/2 |

All conditional probabilities are strictly positive and normalized. First-stage likelihood ratios: L(a)=2, L(b)=1/2. Second-stage likelihood ratios: L(ax)=L(by)=1, L(ay)=3, L(bx)=1/4. Terminal LR values: below ax, (1/16,4); below ay, 3; below bx, 1/4; below by, 1. Stop at root or any internal state, choose P or Q, or continue; final decision at depth three. Tau counts actual observations (root stop tau=0).

An ordered BRC branch-mass carrier retains the complete node identity and P/Q mass. The projection to (time,L) loses the distinction ax versus by. It is used here as an audited external finite probabilistic observer, not as an assertion about native X6 evolution.

## Signed objective and global lower bound for every randomized coarse policy
Define H(l)=min(l,1) and

    J(O)=e_P+e_Q+(389/1344)E_P(tau)-(347/1344)E_Q(tau),
    c(l)=(389l-347)/1344.

Then c(1)=1/32, c(2)=431/1344, c(1/2)=-305/2688, c(1/4)=-999/5376 and c(3)=205/336. The depth-three observation after ax has E_Q H(L3)=2/7, so its information gain at L2=1 is 5/7. The other depth-three signals carry no new information.

Condition on root continuation. Let x be the coarse probability of continuing at a (L1=2), y the probability of continuing at b (L1=1/2), and z the common continuation probability at second-stage LR=1, merging ax and by. Optimizing stop decisions pointwise by H, continuing at bx (because c(1/4)<0), and stopping at ay (because c(3)>0), yields for **all real x,y,z in [0,1]** the exact achievable lower envelope

    J >= 67/96 + (431/4032)x - (319/2016)y
                  + z[ -(51/448)x + (1/144)y ].                (1)

The right-hand side is attained when the other actions are the indicated optimum choices. In particular, (1) is an analytic bound over ALL locally randomized seedless coarse policies; it does not infer the stochastic result from deterministic enumeration.

Its derivative in y is -319/2016+z/144<0, so every global minimizer has y=1. Substitution gives

    J >= 34/63 + [431x + z(28-459x)]/4032.                  (2)

For x<=28/459 the minimizing z is 0, with excess 431x/4032, zero only at (x,z)=(0,0). For x>=28/459 the minimizing z is 1, with excess (1-x)/144, zero only at (x,z)=(1,1). Root stop costs H(1)=1>34/63, hence any globally optimal coarse policy continues at root surely. Allowing randomized root stopping does not create further optimal values. The only optimal coarse **sampling time pairs** are

    T0=(E_P tau,E_Q tau)=(13/9,19/9),
    T1=(E_P tau,E_Q tau)=(5/2,17/6).

Actions on unreached histories or tied final decisions at L=1 can vary but cannot alter either optimal time pair.

## Two feasible coarse vectors and an impossible midpoint
Both policies continue at the root and b, continue at second-stage bx, stop/decide P at ay, and at terminal nodes decide Q iff L<1 (otherwise P).

Policy S0: at a stop/decide P (x=0); at every second-stage LR=1 stop/decide P (z=0).
Policy S1: at a continue (x=1); at every second-stage LR=1 continue (z=1).

Exact Q/P mass summation:

    O0=(1/9,5/9,13/9,19/9),  J(O0)=34/63;
    O1=(5/42,3/7,5/2,17/6), J(O1)=34/63.

Their midpoint equals

    O*=(29/252,31/63,71/36,89/36), J(O*)=34/63.

If any seedless behavioral (time,L) policy produced O*, it would necessarily minimize J, and by (2) its time pair would be T0 or T1. The midpoint's time pair (71/36,89/36) is neither. This is an exact **no-real-solution certificate for the midpoint**, proving the compressed behavioral four-vector image is nonconvex.

O* is nevertheless achieved by a **full-history behavioral policy without a persistent initial seed**: continue at the root and b; at a continue with probability 1/2, otherwise stop/decide P; at ax continue certainly; at by continue with probability 1/2, otherwise stop/decide P; at bx continue, at ay stop/decide P, and at terminal nodes decide Q iff L<1, otherwise P. Direct rational mass accumulation yields O*.

## Verification and boundaries
The accompanying Python stdlib Fraction verifier checks positivity, P/Q normalization, all likelihood ratios, each vector and objective, and the full-history realization. It also exhausts 23,328 deterministic (time,L) action tables (3 root actions, 3^2 first-stage, 3^3 second-stage, 2^5 terminal), verifying exact J-minimum 34/63 and precisely the two optimal time pairs. **The universal randomized proof is the algebra (1)-(2); deterministic enumeration alone is not such a proof.**

This result makes the prior semialgebraic study's missing convexity obligation concrete at N=3. It does **not** solve the stronger open problem of *matching full/coarse convex hulls with differing behavioral images*: this example does not have equality of all signed supports. Indeed a full-history policy may improve J by at least 1/144 by continuing at ax while stopping at by. No native formal Result, independent review, real closed field QE run on the prior 32-leaf N4 instance, or native Heartbeat/X6 theorem is claimed.

## Sources and state
Current GLOBAL_KNOWLEDGE_V1 canonical-main read snapshot de99073a78bf0c28b3f93ea359665ea2e2015110; Enterprise Math research read snapshot 5fdbfb3a2517ae2b798e8ddcfce27a8ad75d9c3e. Direct predecessor research_notes/brc_n4_exact_semialgebraic_policy_20261027_r5/PROOF.md and NEXT_TASK.md. The exact BRC reuse is positive ordered branch probability mass, preserved identities, and source-aware likelihood-ratio readout. No claim that positive mass can model arbitrary signed/phase cancellation.