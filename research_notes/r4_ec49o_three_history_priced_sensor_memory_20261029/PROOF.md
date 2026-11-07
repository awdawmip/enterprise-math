# EC49O — Exactly two causal memory bits for a three-history, two-sensor observer

Status: AUTHOR_PROVED / EXACT_FRACTION_ENUMERATION_PASS / UNREVIEWED / NOT_ADMITTED. Portable author evidence, not a native Task CLAIM, Result, review, signed BRC or native X6 theorem.
Author: R4-AUTO11-EC49O-20261029-0030-LOCAL (this execution's local author label; not a native service-issued session ID).
Inputs: GLOBAL_KNOWLEDGE_V1 main@f4e861ad0c9377f6001c233607fdf56cdcda1dc9; Enterprise Math main@7082294e174da65acce3ec437df8be5c29ecfa92; predecessor EC49N PR #1650 immutable 1c34aea678d03119e339f96c21c4fb34e7f3a322.
P000/ACTIVE worldview remain unchanged. All coordinates below are finite probability indices, **not** native X6 coordinates or native three-dimensional slices.

## Question and exact finite model

How many external-history memory bits are necessary and sufficient to preserve the **entire raw four-dimensional region**
S_m={(alpha,beta,E_P T,E_Q T)}
when a source-independent observer sees W initially, later forgets W, remembers its own actions and already-observed sensor data, and may buy two sequential, differently priced sensors using fresh behavioral randomization?

W, X and Y each range over {0,1,2}. There are two sources P and Q, with 27 strictly positive joint atoms each. Set
s_w(x,y) = 1_{y=(x+w) mod 3} - 1_{y=(x+w+1) mod 3}.
For every w,x,y, define
Q(w,x,y)=1/27,    P(w,x,y)=(2+s_w(x,y))/54.
Thus P mass is 1/54, 2/54 or 3/54, Q mass 2/54; both normalized. Each W is 1/3 under both sources and, for each W, **each individual sensor** X and Y is uniform under both P and Q. Their joint dependence on W carries the source information. No signed native BRC cancellation or physical X6 dynamics is asserted: the signed s is the difference of two positive probability measures, not a native BRC signed branch.

Decision interface, same for all W and both sources:
1. W is revealed at stage zero. The observer may ACCEPT or REJECT immediately at T=0, or BUY X at cost 1. Upon continuing it retains at most m memory states D and no direct W.
2. After X, it remembers X and its own previous BUY action, and may ACCEPT, REJECT or BUY Y for additional cost 2. It may causally update D using its current D, X and a fresh independent random coin. W is no longer available.
3. After Y, it remembers X,Y, its own actions and D, and may ACCEPT/REJECT. No additional actions or signal channels are available. T is *observation cost*, not physical or heartbeat time.

Every action, memory update and terminal acceptance may be randomized with **real source-independent fresh behavioral probabilities**. No uncounted shared random seed, W-tagged delay/action channel, or side information is allowed. The full observer continues to see W and has all the same choices. Define alpha=P(ACCEPT), beta=Q(ACCEPT), and E_P T,E_Q T using source-specific expectations. The question is exact preservation of S_m as a raw set, not only a convex hull or one scalar objective.

## Theorem: sharp memory support and minimality

For m=1,2,3 available external-history memory states,
h_m = sup_{O in S_m}(alpha-beta) = m/18.
For full W recall, h_full=1/6. In particular,
h_0bit=1/18, h_1bit=1/9, and h_2bit=1/6.

Furthermore S_3=S_full for **all real fresh behavioral policies** and all four observable coordinates: encode W injectively in a 3-valued causal state and replay the full controller; conversely the full controller simulates the memory controller. Hence 3 states, or ceil(log2 3)=**two external memory bits**, are exactly necessary and sufficient for preserving the full raw four-region in this specified observation protocol. The sharp one-bit separating support gap is 1/6-1/9=**1/18**.

An explicit full-memory four-vector unattainable even in conv(S_2) is
O_full=(1/2,1/3,3,3),
obtained by always buying X then Y, and accepting exactly when y=(x+w) mod 3.
A one-bit maximizing policy encodes W=0 as D=0, W=1 or 2 as D=1, buys both sensors, and accepts if (D=0 and y=x) or (D=1 and y=x+1), modulo 3; its vector is
O_1bit=(4/9,1/3,3,3).
A zero-bit maximizing policy buys both only for W=0, rejects otherwise, and accepts when y=x; its vector is
O_0bit=(1/6,1/9,1,1).
All three four-vectors follow by summing the 27 rational atoms under each source.

### Proof (valid for all real randomized causal policies)

For every W and X, sum_y[P(w,x,y)-Q(w,x,y)]=0. Therefore acceptance before buying Y has **zero** alpha-beta contribution regardless of W, early acceptance, randomized memory or X. The only contribution comes from BUY-Y leaves; actions before observing Y are source-independent conditional on (W,X) because (W,X) has the same law under both sources.

For any causal controller with m memory states d, set t_{w,d,x} in [0,1] to the conditional probability that it reaches BUY Y with final pre-Y memory d, given initial W=w and X=x (including early stop/initial purchase). For each (w,x), sum_d t_{w,d,x}<=1. The true causal set of such t may be smaller, but is contained in this simple row-substochastic polytope. Let r_{d,x,y} in [0,1] be the source-independent terminal acceptance probability. We have the exact identity
alpha-beta =
(1/54) sum_{x,d,y} r_{d,x,y} [sum_w t_{w,d,x}s_w(x,y)].
The same formula upper-bounds even causally feasible policies with arbitrary real fresh random memory updates.

Fix x. Maximization over each terminal r sets it to 1 exactly where its bracket is positive. Thus the objective becomes
F_x(t)=sum_{d,y} max(0,sum_w t_{w,d,x}s_w(x,y)).
This is **convex** in t. Its maximum on the product of three row-substochastic simplices occurs at an extreme point: each w is either discarded or assigned wholly to one d. For a memory label d, let G_d be its assigned subset of {0,1,2}. The three row vectors s_w(x,·) are permutations of (1,-1,0), and sum_w s_w(x,·)=0. Consequently the positive-part sum of sum_{w in G} s_w(x,·) is:
- 0 if G is empty or all three histories;
- exactly 1 if G is any nonempty proper subset.

With m memory labels, at most min(m,3) nonempty proper disjoint groups can occur; hence F_x(t)<=m for m=1,2,3. There are three x values and each signed atom difference is 1/54, giving alpha-beta <=3m/54=m/18. The explicit deterministic policies above attain equality for m=1,2,3. For full W recall, each of the three W-specific rows has one positive entry and no scalar policy can beat selecting all positive entries, giving h_full=9/54=1/6.

The bound includes early ACCEPT/REJECT, sensor-dependent stopping, randomized updates, randomized terminal decisions and all real behavioral choices. Its strict one-bit inequality separates O_full from conv(S_2), **not merely** from deterministic one-bit strategies. With three states, retaining W is a lossless causal compilation for every future operation and both sources, proving the raw-region equality. A one-bit controller cannot preserve the raw region because of the separator. This is the minimal memory claim; it is not a universal bound for arbitrary sensor menus or randomized shared-seed controllers.

## Verification and relation to EC49N

The accompanying executable Python Fraction checker verifies positive rational P/Q mass on all 27 atoms each; exact normalization and uniform source-neutral marginals of each individual sensor conditional on W; all four witness observables; **19,683** deterministic one-bit (initial assignment, stage-one update/stop) plans and **64** zero-bit plans with optimized terminal acceptance; plus **81** extreme-point row assignments (27 per observed X). The optimizer correctly replaces terminal enumeration with taking the positive signed mass; this covers the entire deterministic terminal-policy class for L=alpha-beta. All-real assertions come from the analytic convexity proof, *not* finite-grid extrapolation.

EC49N's two-W action-name coding cannot be invoked here: the only source-informative continuation requires the fixed action sequence BUY X then BUY Y; choosing early termination cannot carry an additional action label to the terminal state without forfeiting signed information. The difference between positive joint source masses and source-neutral separate marginals is a finite **joint-relation observer-preservation** example. The signed P-Q difference is auxiliary; a native typed BRC or X6 bridge, independent replication, formal proof and scientific admission are unverified.

## Sources and limitations

The predecessor EC49N is PR #1650. External finite-state POMDP policy research and Kuhn's perfect-recall theorem are *background* only, not proofs of this exact finite table: IJCAI 2025, Galesloot et al., doi:10.24963/ijcai.2025/947, and Maschler/Solan/Zamir, Game Theory, Cambridge 2013, doi:10.1017/CBO9780511794216.007. No general novelty claim for POMDP finite-state lower-bound techniques.

Open: if X/Y sensor purchase order is freely reversible and acts as a cheap W coding channel, how large a separation survives the optimal action-order code? Characterize the exact minimal-memory threshold under such action-name coding, and revisit the irrational fresh-behavioral question when terminal acceptance is unrestricted. See NEXT_TASK.md.
