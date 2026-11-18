# S23/AV: gap-class certificate extending exact saturation to H=5000

Date: 2026-11-08 (Asia/Shanghai)
Status: AUTHOR_SIDE_EXACT_FINITE_CERTIFICATE; independent review pending
Frozen scientific pin: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34
Predecessor: research_notes/brc_s23_av_unimodular_first_entry_20261108_r1/FULL_SATURATION.md (blob 6c685aa08461643bf7283d18ba4784bb5b80079a, immutable commit 85b53d06d6ba775e516c566c1d79828b6ca9bb1f)
Previous frontier: research_notes/brc_s23_av_endpoint_plateau_h3000_20261108_r1/HANDOFF.md at commit 5c8a43ce27872b86e1786b1ed8da18d5ebdd26cb

## Theorem

For the two-point, iid S23/AV auxiliary likelihood-sign observer, let

  T_h = { 10^i/7^s : integers 0 <= i <= s <= h }.

Define N(h) as the smallest common prefix length n for which every open likelihood-ratio threshold cell determined by T_h contains at least one attainable prefix ratio. The zero-log-likelihood label 3 permits padding to a common length. Then

  N(h) = 2,455,069 for every integer 510 <= h <= 5000.

This extends the previous endpoint H=3000 by 2,000 horizons. The new algorithm replaces millions of per-cell prefix checks with one exact witness for each of 29 adjacent-gap displacement classes at H=5000.

## Model and exact coordinates

One-step laws on ordered labels (1,3,4):

  P0=(1/2,1/4,1/4), P1=(5/7,1/4,1/28).

For prefix counts (k,ell) of labels 1 and 4, its likelihood ratio is 7^(k+ell)/10^k; label 3 has unit likelihood ratio. Let

  r=ln(7)/ln(10/7) > 0, E(k,ell)=k-r*ell.

Represent any threshold 10^i/7^s by t(v,j)=r*v-j, where v=s-i, j=i and v+j=s<=h. The threshold order is preserved (up to the fixed positive log scaling and reversal already fixed in this observer coordinate). A prefix occupies the open cell between t_L<t_R exactly if t_L<E(k,ell)<t_R.

The coordinate r is irrational. If r were rational p/q>0, then 7^(p+q)=10^p, contrary to unique prime factorization. Hence all pairs (v,j) name distinct thresholds.

## Lemma: translated witness for an entire gap class

Fix H, n and a collection C of adjacent threshold pairs having the SAME integer displacement

  (dv,dj)=(v_R-v_L,j_R-j_L),

so their common positive width in t coordinates is W=r*dv-dj>0.
Let

  V=max_C v_L, J=max_C j_L, S=min_C(v_L+j_L).

Suppose nonnegative integers K,L obey

  K>=J;  L>=V;  K+L<=n+S;
  0<K-r*L<r*dv-dj.

For EACH adjacent pair in C, define its prefix counts

  (k,ell)=(K-j_L,L-v_L).

Then k,ell are nonnegative, k+ell=K+L-(v_L+j_L)<=n, and

  E(k,ell)-t(v_L,j_L)=K-r*L

lies strictly between 0 and t(v_R,j_R)-t(v_L,j_L)=r*dv-dj.

Therefore one certified integer pair (K,L) uniformly covers EVERY gap in the class after translation. No statistical approximation is used. This lemma is valid for any finite collection of actual adjacent threshold pairs.

## Exact H=5000 class certificate

There are precisely M=(5001*5002)/2=12,507,501 threshold points, hence 12,507,502 open cells, of which 12,507,500 are bounded between two consecutive thresholds. The accompanying exact verifier constructs and sorts all M pairs, using the integer lower-key lo*v-Q*j, where Q=10^26 and it proves

  lo=545569623581288298975349314,
  hi=545569623581288298975349315,
  lo/Q<r<hi/Q.

The enclosure comes from 45-term rational atanh series and positive explicit tail bounds for z=1/3, 1/9, 1/15. The exact identities are

  ln(7) = 3 ln(2) - ln(8/7),
  ln(10/7) = ln(5/4) + ln(8/7).

For every consecutive pair in the sorted array, the verifier proves its order by the adverse endpoint integer inequality

  (lo if dv>=0 else hi)*dv > Q*dj.

This establishes that the sorted sequence is the exact increasing threshold order, not just a numerical guess. It groups ALL 12,507,500 bounded cells by (dv,dj), obtaining precisely 29 nonempty classes. For each class it computes exact V, J, S and count, whose counts sum to 12,507,500.

Each class receives a single pair (K,L). To certify the lemma's strict inequalities without floating point, the verifier checks

  K*Q > hi*L,
  (K+dj)*Q < lo*(L+dv),
  K>=J, L>=V, K+L<=2,455,069+S.

This is a valid adverse-rational-endpoint certificate because L>=0 and L+dv>=0 for the constructed class witnesses.

For the narrow class (dv,dj)=(79,431), use the previously verified unimodular witness (K,L)=(2,074,774,380,295). It covers precisely 10,086,786 translated cells and has K+L=2,455,069, attaining the sharp n bound. For the other 28 classes, the verifier searches for L>=V, selects the smallest K obeying K>rL and K>=J at that L, and verifies these same exact inequalities. The maximum certified prefix length among all these OTHER classes is just 27,284.

The outer-left cell (-infinity,-H) has (k,ell)=(0,917), where lo*917>Q*5000. The outer-right cell (rH,+infinity) has (k,ell)=(27279,0), where Q*27279>hi*5000. Both lengths are below n.

Thus all 12,507,502 open cells are occupied by attainable prefixes of length <=2,455,069. Padding with label 3 gives a common length n:

  N(5000)<=2,455,069.

The exact predecessor theorem N(510)=2,455,069 supplies the lower bound, while T_510 is contained in T_h for every h>=510, so N(h) is nondecreasing. Consequently,

  2,455,069=N(510)<=N(h)<=N(5000)<=2,455,069,

proving the stated equality for every integer 510<=h<=5000.

## Evidence and novelty

Verification source: VERIFY_H5000.py
Actual execution transcript: RUN_EVIDENCE.txt

The verifier uses Python 3.13.5 standard-library Fraction, integers and collections; exact decisions use rational bounds and integer inequalities. Its reported SHA-256 on the ordered class-data table is

  9d51dbf18b2e242f7fc20d6d1514f1265f2399bb69502922b27fb3defc3c0e29.

The local verified source SHA-256 at execution is

  06a3d9ec3ad198f27890277fe83e2d90414d834b755611c9aa23a45c1c365e31.

The transcript ends with PASS_S23_AV_GAP_CLASS_EXACT_N_H5000. All 29 displacement-class records are printed in that transcript; collectively they certify each one of the 12,507,500 bounded cells. The class-lift lemma is the new reusable reduction: an O(H^2 log H) exact ordering step, followed by one witness per realized displacement class, rather than millions of independent search runs.

This is the finite-future sign-observer capacity of the explicitly defined two-point AV statistical experiment. It preserves the (label-1, label-4) joint counts and label-3 padding relation, under the project's joint-relation observer rule. Mother-model six-source/ten-label transfer and the separate full-parameter minimax error delta_4 remain independent research questions. The present result is an author-side mathematical proof/certificate; independent review and any formal research authority are separately governed.

## Next discriminating question

Classify the evolution of distinct adjacent gap displacements (dv,dj) as H grows beyond 5000. Determine the first H at which one of the 29 witness classes fails its uniform lift, or a new class requires a longer prefix; use the rational enclosure and the unimodular near-resonance pair to derive a parameterized coverage bound without sorting all O(H^2) thresholds. A separate tail inequality gives a finite search horizon for the first eventual increase but does not locate that first increase. Preserve exact frozen input and prior accepted scoped proofs.
