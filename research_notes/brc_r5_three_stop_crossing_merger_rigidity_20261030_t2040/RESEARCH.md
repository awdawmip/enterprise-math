# R5 — terminal LR-collision rigidity after three genuine STOP/CONTINUE stages

Date: 2026-10-30 Asia/Shanghai. Evidence: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / SYMBOLIC_DETERMINANT_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

Frozen reads: GLOBAL_KNOWLEDGE_V1 main@eabd4df96bb9297b2935a8d0755b1535d89a7ff2; Enterprise Math main@d120a0afb085a3bba6d5856a71ba0b24f109e0a9. Scientific predecessor: 5d17318fabbbced773381b09278965ab2fdd302c, research_notes/brc_r5_general_stop_diamond_20261030_t1940/RESEARCH.md. This is a third genuine stop-decision epoch and crossing likelihood-ratio merger model, not the previously classified two-stop diamond.

## Question and exact scope

Can a third genuine STOP/CONTINUE stage with crossing likelihood-ratio (LR) collisions make the FULL and seedless LR real four-observer convex hulls equal while their actual real images differ? This study establishes a more general necessary condition for hull equality and an open full-four-dimensional family violating it. The original hull-equal / image-unequal mother problem remains OPEN.

Observable O=(e_P,e_Q,T_P,T_Q), where error e_L and absorption time T_L are expectations under probability law L=P or Q. FULL uses full observed history, LR only current time and P/Q likelihood ratio; all behavioral randomizations are local with no persistent shared random seed. Nature's latent branches carry strictly positive P and Q weights. The finite stochastic model is external auxiliary mathematics, not a new native X6 spatial model. BRC use is exact positive-weight branch/provenance preservation (definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json); no independent BRC engine run, signed-mass or native transfer is asserted.

## Theorem A: universal two-class final collision rigidity (all real parameters)

Let a finite rooted stochastic STOP/CONTINUE tree have final optional STOP at time tau and mandatory CONTINUE absorption at time tau+1. Every preceding STOP absorbs strictly before tau; all natural leaf paths i have p_i,q_i>0 with sum p=sum q=1. The final likelihood ratio p_i/q_i takes exactly two distinct positive values R_0 and R_1, indexed by v(i) in {0,1}. From every preceding decision history g, the alternative final ratio class remains reachable with strictly positive Q-mass Q(g,v') for either selected class v and its opposite v'. All conditional terminal Bernoulli-error probabilities under P and Q share one common kernel: final CONTINUE has error beta_i in (0,1); final STOP has error beta_i+c_i in (0,1); preceding STOP errors are also in (0,1). FULL may act separately at all histories; seedless LR shares the last action among all histories with the same final ratio.

**Necessity:** If the FULL and LR convex hulls of O are equal, c_i must be constant within *each* final LR collision class. Equivalently, if two histories i,j in one class satisfy c_i != c_j, then an explicit real signed linear functional H has strictly larger FULL than LR support value.

**Proof:** Fix a final class v with unequal c_i. Pick sigma in {+1,-1} such that h=max_{v(i)=v}(sigma*c_i)>0, set ell=min(sigma*c_i)<h, and choose theta with max(0,ell)<theta<h. Then sigma*c_i-theta has both strict signs. Let v' be the other class. Solve the two affine equations
    A*R_v+B=theta*R_v,
    A*R_v'+B=K+theta*R_v
for A,B; uniqueness follows from R_v!=R_v'. Use H=sigma*e_P+A*T_P+B*T_Q.

The pathwise time coefficient per unit Q mass, A*(p_i/q_i)+B, is theta*R_v>0 for the selected final class and K+theta*R_v>0 for the other. Take K>max_g P(g)/Q(g,v'), with the maximum over all earlier stopping histories g; it exists because the tree is finite and the alternative class remains reachable with positive mass. If a preceding decision STOPs rather than CONTINUEs, every alternative-class descendant, had the controller continued, would have absorbed at least one time unit later. Thus switching STOP to CONTINUE increases H's time part by at least K*Q(g,v'), while its sigma*e_P part can fall by strictly less than P(g) (all Bernoulli error probabilities lie in (0,1)). The H improvement is strictly positive independent of future decisions. When LR shares a preceding action across histories, these positive improvements add, so all optimizing FULL and LR policies continue at every reachable preceding stage.

At the final STOP versus CONTINUE, each path has H gain
    g_i = sigma*p_i*c_i - (A*p_i+B*q_i).
For the target class this equals p_i*(sigma*c_i-theta), with positive and negative values. For the other class, g_i=q_i*(sigma*R_v'*c_i-K-theta*R_v)<0 once K is enlarged further if needed. The earlier-continuation inequalities survive increasing K. At the selected class, FULL chooses each last STOP independently, gaining sum_i max(0,g_i), but LR must use one shared real STOP probability and gains max(0,sum_i g_i). Their exact support gap is
    Delta = sum_{i:v(i)=v} max(0,g_i) - max(0,sum_{i:v(i)=v} g_i) > 0.
The strict inequality follows from both signs. This is valid for all real local behavioral policies, not just enumerated deterministic policies. A strict linear-support gap separates the convex hulls. QED.

**Limits:** The theorem requires exactly two final LR ratio classes and positive alternative-class reachability at every earlier decision history, plus the common P/Q terminal-error kernel. It does not classify other final merger cardinalities, blocked branches, P/Q-specific error kernels, or the actual images when final slopes do agree. The condition is necessary, not sufficient.

## Concrete full-rank crossing-merger construction

Nature reveals X in {0,1} before epoch-2 STOP/CONTINUE; after continuing it reveals U in {0,1} before epoch-3 STOP/CONTINUE; after continuing it reveals V in {0,1} before epoch-4 STOP/CONTINUE; continuing at 4 absorbs at 5. Every STOP is genuine absorption.

Q(X=x,U=u) in order (00,01,10,11) is (3/8,1/8,1/8,3/8).
Q(V=0|X,U=u)=w_u, with w_0=3/4 and w_1=1/4.
Define q_xuv=q_xu*w_u for v=0, else q_xu*(1-w_u).
Define p_xuv=R_v*q_xuv, with R_0=1/2 and R_1=3/2.

All 8 paths have strictly positive mass, sum P=sum Q=1. The exact ratios are time 2: P(X=0)/Q(X=0)=7/8 and P(X=1)/Q(X=1)=9/8; time 3: p_xu/q_xu=r_u with (r_0,r_1)=(3/4,5/4); time 4: p_xuv/q_xuv=R_v=(1/2,3/2). Thus the time-3 merger groups histories by U across X, and the later crossing merger groups histories by V across both X and U. LR can independently choose early s_x, middle h_u and late z_v; FULL can choose s_x,h_xu,z_xuv. Neither has persistent randomness.

Preterminal STOP errors and time-5 continuation error each have probability 1/2. A time-4 STOP has error probability 1/2+c_xuv, where c_000=a, c_100=-b, c_xu0=0 otherwise, and c_xu1=d for all x,u. The open parameter domain is
    0<a<1/2, 0<b<1/2, -1/2<d<1/2, d!=0.
All error probabilities remain strictly inside (0,1).

For full deterministic or independent real behavioral probabilities, with w^P=p,w^Q=q:
    e_L=1/2+sum_xuv w^L_xuv*s_x*h_xu*z_xuv*c_xuv,
    T_L=sum_xuv w^L_xuv*[2+s_x*(1+h_xu*(2-z_xuv))].
For LR replace h_xu by h_u and z_xuv by z_v. These are exact polynomial observation maps.

## Theorem B: explicit strict hull gap and full four-dimensionality throughout an open family

Use the fixed signed observer direction H=e_P+4*T_P-2*T_Q. At a final V=0 path the time coefficient is 4p-2q=0, while at V=1 it is 4q>0. From each middle history (x,u), continuing instead of stopping increases H by more than 4q_xu1-p_xu>0 because 4(1-w_u)>r_u for u=0,1. From each early X=x history the improvement is more than 4Q_x(V=1)-P_x, which equals 3/4-7/16>0 for x=0 and 5/4-9/16>0 for x=1. These bounds cover arbitrary later actions and also the source-shared LR action. Thus every maximizing policy continues at times 2 and 3.

At the final V=1 class, STOP gain is (3d/2-4)q_xu1<0; all continue. At V=0, the only nonzero gains are +9a/64 at (0,0,0) and -3b/64 at (1,0,0). From baseline full CONTINUE H=1/2+4*5-2*5=21/2, therefore for **every real parameter** in the above open domain,
    sup_FULL H = 21/2+9a/64,
    sup_LR H   = 21/2+max(0,(9a-3b)/64),
    Delta_H    = min(9a,3b)/64 > 0.
The FULL witness with all earlier CONTINUE, final STOP only on (0,0,0), has
    O_star(a)=(1/2+9a/64, 1/2+9a/32, 5-9/64, 5-9/32).
It lies outside the entire real LR convex hull; its infinity-norm distance from the actual LR image is at least Delta_H/7.

To prove the separating model has full four-dimensional affine rank, index the 64 LR deterministic strategies lexicographically by six bits (s_0,s_1,h_0,h_1,z_0,z_1), 0-based. Policies 0,16,20,21,26 are legal. Subtract the policy-0 observation from the other four, forming the column matrix
    M = [[0, 0, 27d/64, -3b/64],
         [0, 0, 9d/32,  -3b/32],
         [9/16, 3/2, 69/64, 45/64],
         [1/2, 5/4, 31/32, 21/32]].
An exact rational determinant expansion gives det(M)=81*b*d/65536 != 0. Hence LR's convex hull and therefore FULL's convex hull both have affine dimension exactly 4 throughout this open a,b,d region. Four-dimensionality does *not* rescue hull equality.

For a=b=1/4, d=1/8:
    sup_LR H = 1347/128 = 2694/256;
    sup_FULL H = 2697/256;
    gap=3/256;
    O_star=(137/256,73/128,311/64,151/32);
    dist_infinity(O_star,O_LR)>=3/1792;
    det(M)=81/2097152.
This provides an integer-coefficient Farkas-style separating inequality
    e_P+4T_P-2T_Q <= 1347/128
for every LR real strategy, violated by the displayed FULL witness.

## Exact computational verification

VERIFY.py, executed with Python standard-library fractions, exhaustively enumerates 64 LR and 16384 FULL deterministic policies for each of three independent legal rational parameter triples: (1/4,1/4,1/8), (1/8,3/8,-1/4), (3/8,1/8,1/4). It checks exact positive mass normalization, both crossing ratio mergers, probability legality, all support maxima and signed gaps, the explicit FULL witness, and the five-point affine determinant formula. EXACT_OUTPUT.txt is its actual stdout. The last line is PASS_EXACT_R5_CROSSING_THREE_STOP_FULLRANK_NO_GO.

VERIFY_SYMBOLIC.py independently recomputes the 5 legal LR observations from P/Q weights with SymPy symbolic a,b,d, yielding det(M)=81*b*d/65536; SYMBOLIC_OUTPUT.txt records its actual stdout and PASS_SYMBOLIC_CROSSING_THREE_STOP_RANK4_DET. The all-real theorems are analytical; finite checks cover only the enumerated rational instances. No floating-point LP, external priority assertion, independent review, native Result/CLAIM, mathematical admission, Lean proof, or native X6 transfer was performed. The task-owner read reported CONTROL_QUOTA; authorized native execution ownership could not be established, so this is portable author proof/evidence only.

## Next unresolved scientific unit

Keep the strictly positive crossing geometry and all three true STOP/CONTINUE epochs, but enforce equal final error slopes c_xuv=kappa_v within each V ratio class (the new necessary condition). Introduce source/history-sensitive middle STOP error and/or final continuation-baseline errors while preserving one common P/Q terminal experiment. First certify full four-dimensional hull equality by rational FULL-to-LR convex-combination certificates (Caratheodory at most five LR points per FULL point), or rule it out with a strict signed Farkas separator. Only for a rigorously hull-equal candidate seek an exact semialgebraic separation of actual seedless LR images or construct an implementing LR strategy. Preserve individual branch provenance and record the precise limit of every discarded candidate. P000 and ACTIVE worldview are unchanged.
