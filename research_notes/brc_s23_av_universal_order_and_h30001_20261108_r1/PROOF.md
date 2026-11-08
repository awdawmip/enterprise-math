# S23/AV: universal finite-horizon exact rank/select, and exact plateau through H=30001

Date: 2026-11-08 Asia/Shanghai. Status: author-side exact theorem and computational certificate; independent review pending.
Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor: the H=30000 endpoint proof in PR #1777, commit ff09cc8c8f0064a087ea80953870d9fa4bde5959, research_notes/brc_s23_av_exact_plateau_h30000_20261108_research1/PROOF.md.
Observer: two-point iid S23/AV auxiliary likelihood-sign observer. The joint label-(1,4) count pair is retained, and label 3 pads the length. The fixed source of likelihood probabilities remains P0=(1/2,1/4,1/4), P1=(5/7,1/4,1/28).

## Theorem A: exact nonenumerative rank/select at every finite horizon

Let r=ln(7)/ln(10/7), an irrational positive real, and let

  T_H={r*v-j: v,j nonnegative integers, v+j<=H},

for any integer H>=1. There are M=(H+1)(H+2)/2 distinct thresholds.

For every such H there is an explicitly certifiable coprime positive integer pair (P,D) with D>H and

  H*abs(r*D-P)<1.                                             (A1)

With this pair, the strict order of T_H is *identical* to the integer-key order

  K(v,j)=P*v-D*j.                                               (A2)

All keys are distinct on the H triangle. Thus a threshold's exact rank, its predecessor, its successor, and the threshold at any zero-based rank s can be queried without enumerating T_H.

### Proof and constructive key selection

Irrationality follows from unique prime factorization: r=p/q rational with p,q>0 would force 7^q=(10/7)^p, or 7^(p+q)=2^p*5^p. Let P/D be any continued-fraction convergent of r with D>H. Convergents exist with unbounded denominators and satisfy abs(r-P/D)<1/D^2. Hence H*abs(r*D-P)<H/D<1.

For distinct points, let a=v-v' and b=j-j'. If a=0, signs are trivially the signs of -b. Otherwise 0<abs(a)<=H<D, so coprimality implies P*a/D is not an integer; its distance from every integer is at least 1/D. By (A1), abs((r-P/D)*a)<1/D, so r*a-b and (P*a-D*b)/D have identical strict signs. This proves (A2) and injectivity.

An exact executable construction for arbitrary finite H is in VERIFY_UNIVERSAL.py. It encloses each of ln(2), ln(8/7), ln(5/4) between rational atanh partial sums and explicit geometric tail bounds, obtaining exact rational lo<r<hi from ln7=3ln2-ln(8/7) and ln(10/7)=ln(5/4)+ln(8/7). It forms continued-fraction convergents of the rational midpoint until D>H, and accepts a candidate only after checking the *integer/rational certificate*

  H*max(abs(lo*D-P),abs(hi*D-P)) < 1,   gcd(P,D)=1,   D>H.      (A3)

If precision is insufficient it doubles the number of atanh terms. For each finite H, sufficiently precise intervals share the finite needed convergent with irrational r, so the process terminates mathematically. The finite number of precision refinements, and bit complexity of giant rational numerators, are input-dependent.

### Exact rank formula

For integer key m, write C_H(m)=# {(v,j):v,j>=0,v+j<=H,P*v-D*j<m}. Define clipped bounds

  A=clip(ceil(m/P),0,H+1),
  B=clip(ceil((D*H+m)/(P+D)),0,H+1),

and n=B-A. For any integer b put

  FS(n,D,P,b)=sum_{i=0}^{n-1} floor((P*i+b)/D).

Then

  C_H(m) = A*(H+1)-A*(A-1)/2
         + n*H-n*(A+B-1)/2
         - FS(n,D,P,P*A-m).                                    (A4)

Proof: for fixed v the eligible j satisfy j>=floor((P*v-m)/D)+1. Full rows are v<A, empty rows are v>=B, and intermediate rows A<=v<B each contribute H-v-floor((P*v-m)/D). Sum the two arithmetic progressions and the floor sum. The Euclidean algorithm evaluates FS in logarithmically many integer operations. For rank s (0<=s<M), binary search for the least m with C_H(m)>s; then the key is m-1. Since H<D, the unique v is

  v=((m-1)*P^(-1) mod D),    j=(P*v-(m-1))/D.

The positive-pair construction and rank/select algorithm are valid for every finite H; arithmetic-operation counts for an individual rank query are O(log H+log D), plus integer bit costs and the once-per-H certified-convergent construction. This is a random-access result, not a subquadratic full enumeration of all thresholds.

## Executed cross-scale tests of theorem A

VERIFY_UNIVERSAL.py checked *all* ranks, select inverses, and predecessor-key count identities for H=1,2,3,10,25,80, plus 40 independently selected rank counts against brute lists for each small H. At each of H=380294, 4564092, 1000000000, and 1000000000000 it checked six zero-based rank/select/count round trips by exact integers without enumeration.

At H=4564092, the dynamically certified pair was (P,D)=(24900305,4564093) and the triangle contains 10415474738371 thresholds. At H=10^12, the pair was (5522166062156,1012183564383), and M=500000000001500000000001. These finite computational checks corroborate the general proof.

## Theorem B: sharp S23/AV plateau through H=30001

Use the same minimum observation length N(h) as the preceding exact S23/AV work: the least n for which the scores E(k,l)=k-r*l with k,l>=0 and k+l<=n occupy every open cell of the thresholds T_h.

Then, for all integer h in [510,30001],

  N(h)=2,455,069.                                              (B1)

The predecessor H=30000 endpoint certificate establishes N(30000)<=2455069; an exact 11-residue lower-bound certificate establishes N(510)>=2455069. Since T_h are nested, monotonicity reduces (B1) to verifying N(30001)<=2455069.

### Incremental-cell lemma

Passing from T_(H-1) to T_H adds exactly H+1 new thresholds (v,H-v), v=0..H. A bounded cell of T_H not incident to any new threshold is an unchanged cell of T_(H-1), so it inherits its old prefix witness. Consequently it suffices to check every bounded cell with a new endpoint, along with both exterior cells. This statement also applies when two newly added thresholds are consecutive.

### Exact integer occupancy test

Use (P1,D1)=(2074774,380295) for threshold order at H=30001. For prefix/threshold sign comparisons use (P2,D2)=(24900305,4564093), since the exact old enclosure

  LO/10^26<r<HI/10^26,
  LO=545569623581288298975349314, HI=LO+1

satisfies both certified inequalities

  30001*max(abs(LO*D1-P1*10^26),abs(HI*D1-P1*10^26))<10^26,
  (2455069+30001)*max(abs(LO*D2-P2*10^26),abs(HI*D2-P2*10^26))<10^26,

with 30001<D1, 2455069+30001<D2 and both pairs coprime.

Given consecutive threshold coordinates left=(vL,jL), right=(vR,jR), define X=-P2*vR+D2*jR and Y=-P2*vL+D2*jL. An attainable prefix is strictly inside the cell iff its key P2*l-D2*k is an integer strictly between X and Y. Its exact occupancy is therefore

  O_n(left,right)= C_n^(P2,D2)(Y) - C_n^(P2,D2)(X+1),           (B2)

where C is (A4). This preserves the full joint (k,l) observer and label-3 padding.

VERIFY_H30001.py independently checked rank/select/occupancy against brute enumerations on H<=44 and then enumerated all 30002 frontier points. It used rank/select to obtain every incident neighbor pair in T_30001, deduplicated cells by exact rank, and evaluated (B2) for all 60002 distinct affected bounded cells at n=2455069.

Results: zero empty cells, minimum occupancy exactly 1. A cell attaining 1 has endpoints (0,29491) and (79,29922), at zero-based bounded-cell rank 20439. The exterior inequalities hold because n*LO>H*10^26 (the prefix (0,n) lies left of -H) and n*10^26>H*HI (the prefix (n,0) lies right of rH).

The incremental lemma therefore yields N(30001)<=2455069. Together with the inherited exact N(510) lower bound and nesting, (B1) follows.

## Verification, provenance, and next work

Programs: VERIFY_UNIVERSAL.py and VERIFY_H30001.py, executed with Python standard library; actual console output in RUN_EVIDENCE.txt. The universal proof is symbolic for every H, while the H=30001 plateau extension is a complete finite computation depending on the earlier H=30000 certificate. Neither source is a new primitive X6 physical model. The project BRC priority is applied to the retained joint likelihood count with label-3 padding; no unproved reduction of future joint observers is introduced.

Next: construct an exact O(H)-or-better class/multiplicity/extremal enumeration from continued-fraction and triangular-boundary structure; or use batches of incrementally changed cells to find the earliest H>30001 with N(H)>2455069. The independent questions of lawful six-source/ten-label mother-model mapping and the four-observation minimax error remain active.

Control: current GitHub login awdawmip with repository write permission. Source-native task/Owner/CLAIM remains unconfirmed after the currently failing em_control_tasks status query (BACKEND_IDENTITY_OR_VERSION_MISMATCH, STATUS_DATABASE_UNAVAILABLE, operation_sent=false). This artifact is an author-side research checkpoint for independent review and does not assert Source-native task completion.
