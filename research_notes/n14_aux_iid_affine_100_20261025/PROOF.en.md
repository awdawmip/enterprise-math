# Stage100: an exact minimax affine interval for an external N=14 iid sequential test

**Scientific status:** Author-side exact finite-model theorem, two locally executed Fraction implementations, not an independently reviewed native Enterprise Math Result. This is an EXTERNAL iid auxiliary model; P000, native BRC, native X6 and Heartbeat physical claims are unchanged. Source: Stage99 author proof and Stage100 candidate under research_notes/n14_aux_iid_affine_99_20261025 at Enterprise Math main@b1bc74126d9f4e844ada89be8fcc4daaa489566b.

## Problem and exact result

Observations in {0,1,2} are iid with probabilities P=(1/8,1/24,5/6) or Q=(1/12,1/12,5/6). Every ordered-history dependent randomized sequential test stopping by N=14 is allowed. Put eP=Pr_P(decide Q), eQ=Pr_Q(decide P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha)=min max(tP,tQ) subject to eP,eQ<=alpha.

Stage99 author-proved input:
    alpha99=2586555057332842327/7450150876955541504
    V99=751890958002985135/58204303726215168
    s99=17542569190345211/20889600000000000

Define K100=177963480/134551, lambdaP=167877432/134551=72+(8/9)K100, Gamma100=345840912/134551, and eta100=117732125/808393107308544.

**Theorem. For every real 0<=delta<=eta100:**

    V14(alpha99+delta) = V99 - Gamma100*delta.

The sharp right endpoint and optimum are

    alpha100=2586556142352106327/7450150876955541504
    V100=751869170025529135/58204303726215168.

Right-sharp means that this same supporting line is strictly below V14(alpha) for every alpha>alpha100.

## I. Global Bellman dual over every ordered-history policy

At a count state v=(n,a,b), where a=#0 and b=#1 in the prefix, the likelihood ratio Q(w)/P(w)=2^(a+b)/3^a. For the iid model, the conditional future and the ratio depend only on this count state. Backward recursion over depths 14 through 0 sets

    D(v)=min{ K100*2^(a+b)/3^a, lambdaP,
              1+sum_i P_i D(v+i) },

omitting the continuation alternative at depth 14. This is the exact minimum of tP+lambdaP*eP+K100*eQ for arbitrary randomized ordered-history tests. Count compression applies to Bellman continuation costs; actual ordered first-hit multiplicities must still be retained.

The exhaustive Fraction computation checks 680 states and 1240 nonselected comparisons, with 1238 strictly positive gaps (minimum 12889/807306), 0 negative, exactly 2 zero:

    A100=(9,5,1): continue versus decide P;
    B=(12,0,1): continue versus decide Q.

The root Bellman cost is

    D(root)=3336345672953513652547807/3685386950901636268032
           =V99+Gamma100*alpha99.

For any feasible test, max(tP,tQ)>=tP>=D(root)-Gamma100*alpha. This is the universal support.

## II. Primal exact continuum

There are 504 nominal words with counts A100, but only 336 real first-hit words survive previous stopping actions. The genuine mass of these 336 ordered paths is

    pA=875/3538944, qA=875/13436928.

The Bellman-continuing action at A100 has 49 ordered terminal suffixes, with conditional (P error, Q error, P extra time, Q extra time) vector

    RA=(17611/3981312,122033/124416,191287/165888,4543/3456).

Immediate stopping at A100 truncates 336*49=16464 complete original terminal histories.

At B, precisely 12 words first reach the state, with masses

    pB=48828125/725594112, qB=48828125/362797056.

Its continuing policy has 5 ordered terminal suffixes and conditional vector

    RB=(63/64,1/144,9/8,13/12).

The cones of A100 and B cannot intersect: reaching A100 at time 9 already requires five zeros, while reaching B at time 12 requires zero zeros. Prefix counts never decrease. Both branch sets can therefore be randomized without cross terms.

Let u in [0,1] denote immediate P-stop probability at A100 and s in [0,1] denote immediate Q-stop probability at B. Other actions remain frozen at strict Bellman minimizers. Define

    X=pA*RA.Perror=15409625/14089640214528
    Y=qA*(1-RA.Qerror)=2085125/1671768834048
    E=pB*(1-RB.Perror)=48828125/46438023168
    H=qB*RB.Qerror=48828125/52242776064.

The exact errors are

    eP=alpha99-X*u+E*(s-s99)
    eQ=alpha99+Y*u-H*(s-s99).

They are equal under

    s=s99+h100*u,
    h100=(X+Y)/(E+H)=64118999/54400000000,
    eta100=E*h100-X=Y-H*h100=117732125/808393107308544 > 0.

Since 0<s99<s99+h100=s100<1, all u in [0,1] give feasible probabilities, with

    s100=17567190885961211/20889600000000000,
    eP=eQ=alpha99+eta100*u.

Every reached randomized action minimizes the Bellman cost; hence

    tP+lambdaP*eP+K100*eQ=D(root).

Time expectations are affine in u by cone disjointness. The exact endpoint margins are

    (tP-tQ)(u=0)=1137415722727759775/1862537719238885376>0
    (tP-tQ)(u=1)=1137198023932879775/1862537719238885376>0.

Thus tP>tQ for every real u between 0 and 1, so max(tP,tQ)=tP=D(root)-Gamma100*(alpha99+eta100*u), meeting the global dual lower bound. Every real delta in the stated interval is realized by u=delta/eta100. This proves the theorem rather than merely a finite-grid claim.

## III. Sharp right endpoint

The finite occupation-policy polytope is compact, so any V14(alpha) is attained. If equality with the same supporting line held for alpha>alpha100, positivity of both multipliers would force both errors exactly alpha and every reached action a Bellman minimizer. The 1238 strict comparisons exclude all variations except the two ties A100 and B. Within each count-state fiber all ordered words share the Q/P arrival-mass ratio and identical iid conditional future. History-dependent randomizations average to effective u,s in [0,1], without changing the errors. The two history cones are disjoint. Thus equal errors imply s=s99+h100*u, and alpha=alpha99+eta100*u<=alpha100, contradiction.

## Verification scope and next frontier

The locally executed derive100.py reconstructs exact Bellman/DFS and scans affine gaps. A separately written crosscheck100.py independently uses a bottom-up Bellman table, forward dynamic first-hit masses and exact randomization checks. Both PASS. The portable CHECKER.py here was also locally executed and returns PASS_EXACT_BELLMAN_ORDERED_DFS. The programs share the declared mathematical model and Stage99 author frontier, not an externally independent review. All arithmetic is Fraction exact, with no floating-point tests used as proof.

The next dual-only candidate after the Stage100 endpoint is K101=61236/47 at A101=(12,6,2), a continue/decide-P tie. At that K, a fresh Bellman calculation shows precisely this tie and B's continue/decide-Q tie. No Stage101 primal interval is yet proved.

No native BRC/X6/Heartbeat transfer is claimed. The native task listing returned CONTROL_QUOTA; session creation was refused with STATIC_READONLY_SCOPE_DENIED and operation_sent=false. Current owner/CLAIM/Result and independent Driver admission are NOT VERIFIED.
