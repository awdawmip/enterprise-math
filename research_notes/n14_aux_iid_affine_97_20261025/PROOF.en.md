# Stage97 exact rational minimax affine segment — external N=14 iid model

**Scientific status:** author-side exact finite model theorem with locally executed rational checks; **not** independent Research Driver review or native Task/CLAIM/Result. **Source pins:** GLOBAL_KNOWLEDGE_V1 main@124e158e394e597af0212115d43a38edc164e6bb; Enterprise Math source main@2540a16d415477e0006b18411e08a82c521103db; Stage96 predecessor research_notes/n14_aux_iid_affine_96_20261025/PROOF_AND_PORTABLE_CHECKER.md (blob 3add80f12ace3d36ca6db2f0c1123454e7d3b556). P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matches project startup projection. ACTIVE worldview and current portable protocol read. This is an **external auxiliary finite iid positive-weight model**, not a native BRC/X6/Heartbeat theorem.

Let P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6) be iid on alphabet {0,1,2} with bounded stopping time <=14. For all randomized history-dependent sequential tests, write e_P=P(decide Q), e_Q=Q(decide P), t_P=E_P(tau), t_Q=E_Q(tau). Define V14(alpha)=min max(t_P,t_Q) under e_P,e_Q<=alpha.

## Exact theorem

Take the Stage96 author endpoint:

alpha96 = 5172538010899325243 / 14900301753911083008,
V96 = 24246604065543953699 / 1862537719238885376,
s96 = 8237051660682949 / 13926400000000000,

where s96 is Q-stop randomization at B=(12,0,1), and A96=(14,7,4) has been fixed to decide P.

Set
K97=893307577584960/619337901137,
lambda_Q=K97, lambda_P=72+(8/9)K97=838643508957384/619337901137,
Gamma97=lambda_P+lambda_Q=1731951086542344/619337901137,
eta97=619337901137/4966767251303694336 > 0.

**For every real 0<=delta<=eta97** (not just computed rational parameter samples),

    V14(alpha96+delta)=V96-Gamma97*delta.

Its sharp right endpoint is

    alpha97=2586269934456514327/7450150876955541504,
    V97=757686080746453135/58204303726215168.

The same affine Bellman support line does not attain the true minimax V14 at any alpha>alpha97. Stage98 is not proved here.

## All-history Bellman lower bound

Represent a count state by (n,a,b), where a=#0, b=#1, n<=14. The likelihood ratio Q(w)/P(w)=2^(a+b)/3^a. Define

    D(n,a,b)=min{lambda_Q*2^(a+b)/3^a, lambda_P,
                  1+sum_i P_i D(child_i(n,a,b))},

omitting continuation at n=14. Decreasing-n backward induction minimizes t_P+lambda_P*e_P+lambda_Q*e_Q over **all** ordered-history randomized tests, since conditionals are iid and the likelihood ratio is count-measurable. Thus V14(alpha)>=D(root)-Gamma97*alpha.

An exact Fraction audit covered all 680 count states and all 1,240 nonselected Bellman actions, finding 1,238 strictly positive gaps, 0 negative gaps, exactly 2 zero gaps:

    A97=(4,4,0), continuation C tied with immediate P;
    B=(12,0,1), continuation C tied with immediate Q.

The least positive gap is 19154578828699/237825754036608. The root equals

    D(root)=33377638070337837845505597379543/33927652994761948643740090368
           =V96+Gamma97*alpha96.

The Stage96 action table, reconstructed via its exact dual optimizer at K96=19683/13 with A96 fixed to P, equals the independently minimizing table at K97 (breaking both ties toward continuation).

## Ordered branch masses, suffixes, and disjoint cones

At A97=(4,4,0), the word '0000' is the only nominal and actual first-hit history. Its masses are pA=1/4096, qA=1/20736. Exhaustive *ordered* suffix DFS (not a multinomial shortcut) yields 4,587 terminal words and conditional vector (P-error, Q-error, P-extra-samples, Q-extra-samples)

    R_A=(100522980343/63403380965376,
         61173201761/61917364224,
         3374593929691/2641807540224,
         8332602073/5159780352).

At B, there are 12 nominal/actual first hits, with pB=48828125/725594112 and qB=48828125/362797056. Its 5 ordered terminal suffixes yield

    R_B=(63/64, 1/144, 9/8, 13/12).

Randomization at A97 and B has disjoint ordered-word cones: any word reaching A97 already has 4 zeros, and B requires zero zeros after 12 observations. Early P-stop at A97 therefore truncates exactly 4,587 complete terminal histories; B has 12*5=60 prior complete paths. Exact positive P/Q branch weights are multiplied along ordered words and added only for disjoint alternatives; this is BRC-style **positive-weight branch reuse**, not native BRC or signed/phase cancellation.

## Balanced primal policy for the *entire* real interval

At A97 stop immediately and decide P with probability u in [0,1], otherwise continue; at B decide Q with probability s in [0,1], otherwise continue. Freeze all other actions.

Define exact positive quantities:

    X=pA*(R_A P-error)=100522980343/259700248434180096
    Y=qA*(1-R_A Q-error)=744162463/1283918464548864
    E=pB*(1-R_B P-error)=48828125/46438023168
    H=qB*(R_B Q-error)=48828125/52242776064.

Nonoverlapping cones imply, for *every real* u,s in [0,1],

    e_P=alpha96-X*u+E*(s-s96)
    e_Q=alpha96+Y*u-H*(s-s96).

Error balance e_P=e_Q forces

    s=s96+h97*u,
    h97=(X+Y)/(E+H)=813388768063/1671168000000000.

The endpoint

    s97=s96+h97=12365744850625211/20889600000000000

satisfies 0<s96<s97<1; hence the entire interval u in [0,1] is feasible. Then

    e_P=e_Q=alpha96+eta97*u,
    eta97=E*h97-X=Y-H*h97>0.

Only Bellman-minimizing actions were used, so for all such real u,

    t_P+lambda_P*e_P+lambda_Q*e_Q=D(root).

The four metrics are affine in u by cone disjointness. At u=0,

    t_P-t_Q=2415931526233672265/3725075438477770752 > 0,

and at u=1,

    t_P-t_Q=1207593511071079775/1862537719238885376 > 0.

Thus t_P>t_Q on the whole real interval and t_P=D(root)-Gamma97*(alpha96+eta97*u), attaining the universal dual lower bound. This proves the theorem.

## Sharpness beyond alpha97

Equality in the same support line for alpha>alpha97 would force e_P=e_Q=alpha (both multipliers are positive), and strictly all reached actions must be Bellman-minimal. The 1,238 strict gaps leave mixing only at A97 and B. Even if an admissible competing test randomizes differently on separate ordered histories of the same count, replace these choices by their P-arrival-weighted average: Q/P is constant in that count fiber and future conditionals are identical. With the cones disjoint, all equalizing minimizers have effective u,s in [0,1] and obey the displayed equations. Therefore alpha=alpha96+eta97*u<=alpha97, contradiction. The finite-horizon randomized-policy occupation polytope is compact, guaranteeing attainment; a limiting nonattained equality is excluded.

## Checkers, status and next exact candidate

Author-side locally executed scripts: derive97.py rebuilt Stage96 Bellman minimizing actions, evaluated all dual gaps, exact forward weights, first-hit probabilities and suffix risks; crosscheck97.py independently computed the K97 Bellman min recursion, enumerated full ordered paths (4587 suffix leaves) and verified seven endpoint/interior rational randomizations. Each reported PASS. The two implementations share the declared model and policy; they do **not** establish independent Driver review. The scientific argument for **all real** delta uses exact affine identities, not interpolation of a finite grid.

After freezing A97 to P, the next exact dual crossing candidate is

    K98=17496/13, A98=(13,6,4), current Q tied with continue C.

At K98, there are again only two Bellman ties (B and A98); K98-1/10000 violates the frozen policy at A98. **No Stage98 primal theorem is claimed.** The next proof must compute actual first-hit/suffix evidence, randomization compensation, feasibility, t_P-t_Q and sharpness.

**Actual native-control observation:** task listing returned CONTROL_QUOTA; native session creation returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Live owner/CLAIM/native Result remain unverified. Ordinary GitHub author-source publication is not a native claim, Review or Foundation admission.
