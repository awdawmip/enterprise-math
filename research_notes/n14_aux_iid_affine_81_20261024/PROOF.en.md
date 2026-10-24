# N=14 auxiliary iid — exact 81st optimal affine segment

2026-10-24 · Author-level proof, finite auxiliary iid model ONLY; not independently Driver-reviewed, Lean-formalized, or native BRC/X6/Heartbeat-transferred.

## Statement

For all ordered-history randomized sequential tests, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), N=14, errors eP=P(decide Q), eQ=Q(decide P), times tP=E_P(T), tQ=E_Q(T), define V14(alpha)=inf{max(tP,tQ):eP,eQ<=alpha}.

Freeze predecessor stage80 at source commit 42ab5a458cb799fe4d1b0eddf2b4e2743481f7c5: alpha80=304236203316287029/876488338465357824, V80=180239004423178679/13695130288521216, B=(12,0,1) balancing coin s80=1330357474145633/2457600000000000. Stop Q at A80=(7,0,2), retain the inherited stopping table (verify_n14_80.py).

**Theorem.** For EVERY real 0<=delta<=eta81=4965625/95105071448064,

    V14(alpha80+delta)=V80-5256*delta.

Consequently alpha81=304236249079487029/876488338465357824 and V81=180235246120378679/13695130288521216. The indicated supporting line is sharp on the right.

## Dual: global over ordered histories

At z=(n,a,b), a counts symbol 0 and b counts symbol 1. Exact likelihood ratio Q(word)/P(word)=2^(a+b)/3^a. Set lambdaQ=K81=46656/17, lambdaP=72+8*K81/9=42696/17, Gamma81=lambdaP+lambdaQ=5256. The P-normalized Bellman costs are stop P: lambdaQ*2^(a+b)/3^a, stop Q: lambdaP, and (if n<14) continue: 1+(1/8)D(child0)+(1/24)D(child1)+(5/6)D(child2).

Full exact backwards recurrence: 680 count states; 1240 comparisons to nonselected actions; 1238 strictly positive gaps; 0 negative; TWO ties only, (12,0,1): continue/Q and A81=(11,3,3): continue/Q. Minimum strictly positive gap =139049/3172608. Root

    Droot=201325097614186007485/109561042308169728
         =V80+5256*alpha80.

Even for fully ordered-history-dependent policies, count-state Bellman minima give Droot<=tP+lambdaP*eP+lambdaQ*eQ<=max(tP,tQ)+5256*alpha. Therefore V14(alpha)>=Droot-5256*alpha.

## Ordered positive branches and suffix audit

For A81=(11,3,3), 9240 nominal ordered words; 4767 truly first-hit under the inherited rule, with pA=4965625/18345885696, qA=4965625/7739670528. For B=(12,0,1), 12 nominal/live words, pB=48828125/725594112, qB=48828125/362797056. Continuation suffix quadruples (conditional P-error, Q-error, additional P-time, Q-time) are

    RA=(511/512,1/1728,73/64,157/144)
    RB=(63/64,1/144,9/8,13/12).

An ordered-word DFS separately counts 7 terminal suffix histories (7 terminal state-decision classes) from A, hence 4767*7=33369 complete former histories are truncated by immediate Q at A; B has 5 suffix histories and 12*5=60 former histories. Counts and positive exact probability mass are distinct observables.

A and B coin cones cannot overlap: B has n=12 and cannot precede A with n=11; A has a=3 and cannot precede B with a=0, since a never decreases. Thus all four risk/time observables depend AFFINELY on the two coin probabilities, with no mixed term.

## Full-real-interval attainment

At A stop Q with probability u, otherwise continue; at B stop Q with probability s. Put

    X=pA*(1-RA.Perror)=4965625/9393093476352
    Y=qA*RA.Qerror=4965625/13374150672384
    E=pB*(1-RB.Perror)=48828125/46438023168
    H=qB*RB.Qerror=48828125/52242776064.

Relative to u=0,s=s80, Delta eP=X*u+E*(s-s80), Delta eQ=-Y*u-H*(s-s80). Error equality forces

    s=s80+h81*u, h81=-(X+Y)/(E+H)=-115997/256000000.

The entire [s81,s80] is inside (0,1), with s81=1329243902945633/2457600000000000. Common error increment

    eta81=X+E*h81=-Y-H*h81=4965625/95105071448064>0.

At u=0 exact (eP,eQ,tP)=(alpha80,alpha80,V80); at u=1 it is (alpha81,alpha81,V81). Endpoint tP-tQ values are respectively 139577535183427933/219122084616339456 and 139656202124227933/219122084616339456, both >0. By affine cone-disjointness, for EVERY REAL u in [0,1] both errors equal alpha80+eta81*u, tP>tQ, and all active actions minimize the Bellman costs. Hence the primal achieves its global lower bound tP=V80-5256*eta81*u everywhere in the segment.

## Sharp right endpoint

If some alpha>alpha81 attained that Bellman line, equality in the dual/primal inequalities would require eP=eQ=alpha and Bellman-minimizing actions at all positive-mass nodes. Only tie decisions A and B can vary. At each count state the likelihood ratio and suffix policies are identical for all ordered prefixes; arbitrary history-dependent tie probabilities can be averaged into effective u,s in [0,1]. The cones are disjoint. Error equality therefore forces s=s80+h81*u and alpha=alpha80+eta81*u<=alpha81, contradiction. Finite-horizon randomized policy space is compact, so nonattainment of equality implies the line is strictly nonoptimal to the right.

## Evidence limits and successor

Author-run exact-Fraction backward/forward verification and a separate ordered-history DFS pass, sharing predecessor stopping table. Source-published checkers are stage80 code adaptations; GitHub byte readback is NOT remote execution. No native session/CLAIM, independent Driver acceptance, proof assistant certificate or native transfer claimed.

At endpoint A81 becomes deterministic Q. The next candidate ONLY is K82=3203342640/1201961 and A82=(9,7,2) continuing/stopping P; the stage82 complete interval is not proved here.
