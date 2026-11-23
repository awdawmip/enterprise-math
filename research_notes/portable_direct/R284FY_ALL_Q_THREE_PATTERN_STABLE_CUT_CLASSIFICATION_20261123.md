# R284FY — Uniform stable-cut classification on the {3,5,6} observer carrier

Date: 2026-11-23 (Asia/Shanghai). Research mode: informed portable TASK_RESEARCH, unshared.
Scientific status: AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_REGRESSION / NOT_INDEPENDENTLY_REVIEWED.
Frozen scientific input: R284CO -> R284FM/R284FT -> R284FW/R284FX. No change to P000, the ACTIVE Heartbeat/X6 ontology, or the prior four-phase observer model.

## Statement and significance

Let q>=5, u=1. Use four fixed binary phase tags c0,c1,c2,c3 with reset-free omissions (at most q per publication) and exact all-history stable read sets S_i as in R284FH/R284FM. Normalize c0 to zero. Restrict to the observer subcarrier supported on the three column patterns p3=(0,1,1,0), p5=(0,1,0,1), p6=(0,0,1,1); write a=x3, b=x5, c=x6 and set all other x_p=0. This is an expressly scoped restriction of the seven-pattern classification, **not** an assumption that the other four pattern types can be discarded from the unrestricted problem.

Call a triple *stable-admissible* if the six necessary codeword-distance inequalities of R284FH/R284FO and the six exact stable-state radius-one read-ball separations of R284FM all hold. (This does **not** assert a valid non-atomic publication order.) For each integer q>=5:

* At width n=4q+8, there are **exactly 7** stable-admissible three-pattern histograms.
* At width n=4q+9, there are **exactly 18** such histograms.

More precisely, for k in {8,9}, put n=4q+k, h=k-5. The entire set is the following disjoint union, with each displayed triple ordered (a,b,c):

1. **a-dominant:** (2q+s, 2q+k-s-t, t), for 3<=s<=h and 0<=t<=k-s-3.
2. **c-dominant:** (t, 2q+k-s-t, 2q+s), for the same s,t.
3. **a/c dual-dominant:** (2q+s, k-s-t, 2q+t), for 3<=s,t<=h and s+t<=k.

The counts are 3+3+1=7 when k=8, and 7+7+4=18 when k=9. In the previously computed full seven-pattern finite scans at q=5,6,11,14 this identifies precisely the stable survivors on the support-{3,5,6} face, rather than merely observing their apparent stabilization.

## Proof: exact graph reduction

For the {3,5,6} carrier, the nominal adjacent distances alternate between a+b and b+c; both opposite distances equal a+c. R284FH's no-rollback distance requirement and its opposite-pair necessity therefore become

    a+b>=2q+5,    b+c>=2q+5,    a+c>=2q+3.              (1)

In each adjacent stable-state comparison there are precisely two nonzero edge types in the 8-vertex bipartite residual graph: the two types have separate source last-change groups of budget q, and a shared target last-change group of budget q. Maximum eliminated Hamming demand is

    min(a+b, q + min(q,a) + min(q,b)).

Thus the exact minimum stable distances on the adjacent pairs are

    A_q(a,b) = max(0, a+b-q-min(q,a)-min(q,b)),
    A_q(b,c) = max(0, b+c-q-min(q,b)-min(q,c)).          (2)

The two opposite-phase graph edges, of types 3 and 6, have disjoint source and target last-change vertices. Hence their exact minimum distance is

    O_q(a,c) = (a-2q)_+ + (c-2q)_+.                      (3)

These are exact capacity-graph calculations, not an ordinary undifferentiated error-radius replacement. Radius-one stable read balls are pairwise disjoint exactly when all three values in (2)-(3) are >=3. Equations (1)-(3), with a+b+c=n, are therefore necessary and sufficient for **stable-admissibility within the stated three-pattern subcarrier**.

## Proof: integer classification for every q>=5

By (1), a,c <=2q+k-5. Equation (3) forces at least one of a,c to exceed 2q, with the sum of their excesses >=3.

**Case I: a>2q and c<=2q.** Since c contributes zero to (3), a=2q+s where 3<=s<=k-5. Then b+c=2q+k-s >=2q+5. If b,c both >=q, (2) gives A_q(b,c)=k-s-q<=1, impossible for q>=5. If b<q, the remaining c>q and (2) gives A_q(b,c)=c-2q<=0, also impossible. Thus b>q,c<q and (2) becomes A_q(b,c)=b-2q. The required >=3 is exactly b>=2q+3, i.e. 0<=c<=k-s-3. With a,b>=2q+3 and these bounds, all remaining inequalities in (1)-(3) hold. This is family 1. The symmetric case c>2q and a<=2q gives family 2.

**Case II: a,c>2q.** Write a=2q+s, c=2q+t with positive integers s,t; b=k-s-t>=0. The two adjacent inequalities in (1) imply s,t<=k-5, and (3) implies s+t>=3. The adjacent stable distances in (2) simplify to

    A_q(a,b)=s+max(0,b-q),
    A_q(b,c)=t+max(0,b-q).

If min(s,t)=1, then s+t>=3 implies b<=k-3<=6, so max(0,b-q)<=1 for q>=5; the smaller adjacent stable distance is <=2. If min(s,t)=2 and the other is >=2, then b<=k-4<=5<=q; the smaller distance is 2. Therefore s,t must both be >=3. Conversely s,t>=3 forces b<=k-6<=3<q, and then both adjacent stable distances are s,t>=3; the remaining inequalities are automatic. This is family 3.

No cases remain, and the displayed families are disjoint by whether a,c exceed 2q. Counting the allowed (s,t) proves the asserted 7 and 18 for every q>=5. QED.

## Independent arithmetic scope, provenance, and remaining work

Companion: `research_notes/portable_direct/R284FY_three_pattern_uniform_stable_checker.py`. It independently enumerates every (a,b,c) with a+b+c=4q+k at q=5,6,7,8,11,14,21,32,64, checks the exact integer inequalities (1)-(3), and compares against the closed parameter-family list. All 18 parameter-width cases passed (7 and 18, respectively). This finite regression is not the basis of the all-q proof; the case analysis above is.

The complete seven-type R284FV/R284FX stable scans are stronger in domain: for q>=5 within their verified finite ranges they find 7 total stable histograms at n=4q+8 and 66 at n=4q+9. This note analytically classifies only 7 and 18 of those on a specified face of the seven-pattern lattice. In particular it does not establish that the remaining four column types are observer-redundant. Neither the non-atomic first-edge order nor the full unrestricted all-q formula n_min(q,1)=4q+10 is proved here.

New practical dependency split: (A) prove uniform exclusion/classification of stable histograms using any of types {1,2,4,7}, especially the additional 48 observed in the finite n=4q+9 scans; (B) establish the first-edge survivor set over the present 7/18 analytic templates; (C) combine an unrestricted first-edge classification with R284FW's eleven-family second-edge obstruction. Preserve provenance, historical residues and per-edge budgets. No independent mathematical Review, formal Result, CLAIM or Foundation promotion is asserted.
