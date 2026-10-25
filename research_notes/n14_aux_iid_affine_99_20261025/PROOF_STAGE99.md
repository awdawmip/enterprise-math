# Stage99 exact affine interval — external finite iid sequential test

**Evidence:** author exact-rational computation-assisted finite proof, **not** independently reviewed or native-Result admitted. This is an *external auxiliary iid model*, not a theorem of native P000/X6 cells or a BRC-native numerical run.

**Pinned read sources:** GLOBAL_KNOWLEDGE_V1 main@f0676fb791893d563ee0950c77bbbb58849e05bd; Enterprise Math main@861349355b3a5f1b69b3bd3ce197daabfddb4662; predecessor Stage98 'research_notes/n14_aux_iid_affine_98_20261025/PROOF.en.md' with Git blob 1d887b542bb01470a18677d6e00a3e9e9315f6b0. P000 startup projection and original agree at Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; ACTIVE worldview and current portable protocol read. The native task query failed CONTROL_QUOTA and the service session creation was denied STATIC_READONLY_SCOPE_DENIED (operation_sent=false). Thus no verified native owner, session or CLAIM.

## The exact theorem

For independent observations in {0,1,2}, let
P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6).
Randomized tests may use the full *ordered* observation history and must stop by time 14. Let eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha) be the minimum of max(tP,tQ) subject to eP,eQ<=alpha.

The verified author Stage98 endpoint is

    alpha98=2586269937332842327/7450150876955541504
    V98=757686022002985135/58204303726215168
    s98=12366057190345211/20889600000000000.

Put K99=6696/5, lambdaP=6312/5, lambdaQ=6696/5, Gamma99=13008/5 and eta99=107421875/2806920511488.

**For every real delta in [0, eta99],**

    V14(alpha98+delta) = V98-(13008/5)*delta.

The right endpoint is exactly

    alpha99=2586555057332842327/7450150876955541504
    V99=751890958002985135/58204303726215168.

Moreover the *same supporting affine line* is not attained at any alpha>alpha99; this does not rule out later segments.

## Exact Bellman lower bound

For v=(n,a,b), where a counts symbol 0 and b counts symbol 1, the Q/P likelihood ratio on every ordered word in the fiber is 2^(a+b)/3^a. Let D(n,a,b) be the minimum of

    decide P: lambdaQ*2^(a+b)/3^a
    decide Q: lambdaP
    continue: 1+sum_i P_i D(child(v,i)), available iff n<14.

Backward induction gives D(root) <= tP+lambdaP*eP+lambdaQ*eQ for *all* randomized full-ordered-history tests. Complete exact Fraction enumeration covers 680 count states and 1240 nonchosen-action comparisons. Exactly 1238 gaps are positive, minimum 12889/699840; none negative. The **only** two ties are A=(11,3,0), continue versus decide P, and B=(12,0,1), continue versus decide Q. The exact root value is

    D(root)=125467347054807071603/136951302885212160
           = V98+Gamma99*alpha98.

Since lambdaP,lambdaQ>0,

    max(tP,tQ) >= tP >= D(root)-lambdaP*eP-lambdaQ*eQ
                           >= D(root)-Gamma99*alpha.

## Ordered first arrivals and conditional suffixes

At the Stage98 endpoint, choose continue at A, and immediately decide Q at B with probability s98, following unique Bellman actions at all other states. The baseline satisfies both errors=alpha98, tP=V98 and exact dual equality.

Preserving full ordered first-arrival words, A is encountered along exactly **165** words and B along **12** words. Their probability masses before critical decisions are

    pA=21484375/286654464, qA=21484375/967458816;
    pB=48828125/725594112, qB=48828125/362797056.

After choosing continue at the critical state and following the unique remaining Bellman actions, the conditional suffix vectors (P-error,Q-error,P-extra-time,Q-extra-time,terminal suffix word count) are

    RA=(41/13824,569/576,69/64,167/144,9)
    RB=(63/64,1/144,9/8,13/12,5).

These path cones are disjoint: A at time 11 has three occurrences of symbol 0, while B at time 12 has none, and counts cannot decrease.

## Feasible optimal mixtures for an entire real interval

For any real u in [0,1], at A *immediately decide P* with probability u, otherwise continue; at B *immediately decide Q* with probability

    s(u)=s98+h*u, h=26961/108800,

otherwise continue. All other actions remain the unique Bellman minimizers. Write

    X=pA*RA.Perror=880859375/3962711310336
    Y=qA*(1-RA.Qerror)=150390625/557256278016
    E=pB*(1-RB.Perror)=48828125/46438023168
    H=qB*RB.Qerror=48828125/52242776064.

Because the critical cones do not intersect, the exact (not approximate) probability changes are

    eP-alpha98=-X*u+E*(s-s98)
    eQ-alpha98=+Y*u-H*(s-s98).

Thus h=(X+Y)/(E+H)=26961/108800 gives

    eP=eQ=alpha98+eta99*u,
    eta99=E*h-X=Y-H*h=107421875/2806920511488 >0.

The endpoint s99=s98+h=17542569190345211/20889600000000000 lies in (0,1), so every real u in [0,1] is feasible. All used actions are Bellman minimizers and hence tP+lambdaP*eP+lambdaQ*eQ=D(root).

Both tP,tQ are affine in u, and tP-tQ is strictly positive at both endpoints:

    u=0: 1207595370727759775/1862537719238885376
    u=1: 1137415722727759775/1862537719238885376.

It follows tP>tQ for all u in the real interval. Therefore max(tP,tQ)=tP=D(root)-Gamma99*(alpha98+eta99*u), attaining the universal lower bound for every real delta=eta99*u. **This proves the theorem without extrapolating finite sample tests.**

## Right-endpoint sharpness

A minimizer exists for each alpha in the finite randomized-history occupation polytope. If some alpha>alpha99 attained this same dual line, equality in the lower-bound chain would require both eP=eQ=alpha (the two dual multipliers are strictly positive), and only Bellman-minimizing actions wherever reached. With only the A and B ties and their disjoint cones, arbitrary ordered-history mixing can be P-arrival averaged into effective probabilities u,s in [0,1]. Within each count fiber Q/P is constant, and conditional future distributions do not depend on the word ordering; the averaged policy preserves both errors and durations. Error equality then forces s=s98+h*u and alpha=alpha98+eta99*u<=alpha99, contradiction.

## Evidence and boundary

'CHECKER_STAGE99.py' contains the full rational finite Bellman, 680-state/1240-gap scan, exact arrival/suffix and primal tests. 'INDEPENDENT_ORDERED99.py' is a separately written author DFS over full ordered paths: four rational parameter checks, over 1.1 million ordered-prefix visits at u=0 and u=1/7 or 1/2. The all-real proof uses the explicit affine identities and endpoints, not these test samples. Two author algorithms are **not** independent mathematical review.

Next lower dual candidate *only*: K100=177963480/134551 at A100=(9,5,1), continue versus decide P. First-hit cone interaction, primal interval and optimality are OPEN; see 'NEXT_TASK_PACKET_100.md'. Native owner/CLAIM/Result/independent Driver admission remains unverified; P000 native transfer has not been shown.
