# S23/AV: unimodular first-entry certificate and 379,864 consecutive internal-gap anomalies

Date: 2026-11-08, Asia/Shanghai. Status: AUTHOR_SIDE_ANALYTIC_PROOF_WITH_EXACT_INTEGER_CERTIFICATES; independent review pending.
Frozen scientific source: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor: research_notes/brc_s23_av_persistent_scaled_gap_4813_arithmetic_family_20261108_r1/PROOF.md and FINITE_HORIZON_FOLLOWUP.md at commit 3a6f24ca0eb84917a082b938e5ba4d6065f9f831. This theorem strengthens the old 20,026-row finite gap certificate analytically.

## 1. Model and observation

In the lawful two-point S23/AV auxiliary iid experiment, the one-step laws on labels (1,3,4) are P0=(1/2,1/4,1/4), P1=(5/7,1/4,1/28). For a prefix with k occurrences of label 1, ell occurrences of label 4 (and any number of label-3 padding symbols), the likelihood ratio is Lambda(k,ell)=7^(k+ell)/10^k.

For suffix horizon h, T_h={10^i/7^s : integers 0<=i<=s<=h}. N(h) is the smallest padded prefix length at which every open cell of T_h has a realizable prefix likelihood ratio. The extreme-left tail bound is n_tail(h)=min{n>=1:7^(n+h)<10^n}.

A=10^431/7^510 and B=1 are adjacent in T_510: for s=1,...,510, the maximal threshold 10^i/7^s strictly below 1 is <=A; the 510 exact integer row checks and equality at (s,i)=(510,431) are reproduced by VERIFY.py. The previously proved threshold-scaling lemma gives the adjacent cell J_t=(A/7^t,1/7^t) in T_(510+t) for every integer t>=0. For clarity, a counterexample C=10^i/7^s between the scaled endpoints would give A<10^i/7^(s-t)<1. If s<t or i>s-t this middle quantity is >=1; otherwise it belongs to T_510, contradicting the initial adjacency.

## 2. The determinant-one certificate

Define r=ln(7)/ln(10/7), eps=79r-431 and d=2074774-380295r. All required inequalities follow from exact positive integer comparisons:

  eps>0  iff 7^510>10^431;
  d>0    iff 10^2074774>7^2455069;
  d<eps  iff 7^2455579>10^2075205;
  d<1    iff 7^2455068>10^2074773.

These four inequalities are executed exactly, with no floating-point logs. Let u=(79,431) and w=(380295,2074774), coordinates ordered (v,k). Their determinant is

  79*2074774-431*380295=1.

Thus any integer (v,k) has a unique integral decomposition (v,k)=a*u+b*w. Set E(v,k)=k-rv=-a*eps+b*d.

For the base gap J_0=(A,1), the condition A<Lambda(k,v)<1 is precisely 0<E(v,k)<eps. Suppose 0<=v<380295. If b<=0, the identity v=79a+380295b>=0 forces a>=0, whence E=-a*eps+b*d<=0. If b>=1, the inequality v<380295 forces a<=-1, whence E>=eps+d>eps. Therefore every prefix ratio entering J_0 has v>=380295. Moreover E>0 gives k>rv, hence k>=ceil(r*380295)=2074774, because 0<d<1. The point w itself has E=d strictly between 0 and eps.

**Theorem 1 (exact base first entry).** The minimal non-3 prefix length entering J_0 is therefore

  L(0)=2074774+380295=2455069,

attained by (k,ell)=(2074774,380295). Padding with label 3 cannot shorten it.

## 3. Scaling and sharp first-entry length for one gap

The condition Lambda(k,ell) in J_t is equivalent to A<7^(k+ell+t)/10^k<1. Put v=ell+t. By the same lattice argument v>=380295, and E>0 gives k>=2074774. Hence k+ell>=2455069-t. For 0<=t<=380295, equality is achieved with the nonnegative pair (k,ell)=(2074774,380295-t).

**Theorem 2.** For every integer 0<=t<=380295, the **exact first occupation length of the particular adjacent open cell J_t** is

  L(t)=2455069-t.

Thus N(510+t)>=2455069-t. This is a lower bound on full N, not an equality claim for N, because other cells may need longer.

## 4. A long consecutive anomaly range

For 0<=t<=379863, take n=L(t)-1=2455068-t and h=510+t, so n+h=2455578. The exact comparison

  10^2075204 <= 7^2455578 < 10^2075205

is checked by big integers. As n>=2075205 in this range, 7^(n+h)<10^n and consequently n_tail(h)<=n=L(t)-1<N(h).

**Theorem 3.** For all 379,864 consecutive integers h=510,...,380373,

  N(h)>n_tail(h).

Examples of rigorously exact *cell first-entry lengths* (not exact N values):
- h=510: L=2,455,069, so N(510)>=2,455,069 (old bound only 20,026).
- h=3180: L=2,452,399, so N(3180)>=2,452,399.
- h=380373: L=2,075,206 and the tail is strictly earlier.
- h=380374: L=2,075,205; this cell alone no longer certifies a strict tail anomaly.
- h=380805: L=2,074,774; the witness is ell=0.

## 5. Methods, provenance and scope

VERIFY.py performs the determinant, four strict ordering comparisons, all 510 base-adjacency rows and both bounds on 7^2455578 with Python arbitrary-precision integers. Actual stdout is RUN_EVIDENCE.txt. The determinant lattice argument, scaling and quantifier ranges are analytic proofs, not inferences from an unexplained finite scan.

This is a two-point likelihood-sign observer result within an auxiliary S23/AV model. The joint (#label1,#label4) counts and label-3 padding provenance are kept. Bernoulli z=1/4 compression loses their future likelihood-sign distinctions. There is no claim of an X6 realization, native Heartbeat dynamics, a full-lawful TV minimax value, or a six-source/ten-label mother-model transfer. P000 and frozen inputs are unchanged.

GitHub author-side persistence does not grant native Task CLAIM, Research-Activity registration, theorem admission or independent review. At publication, the native backend returned BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE with operation_sent=false, so live Owner/CLAIM/RA remains unverified.

Next: determine whether N(510)=2455069 by certifying all other T_510 cells at this length, or find a stronger last-gap obstruction. Apply the determinant-one method to further neighboring rational approximants to r. Keep the full-lawful delta4 and the mother-model bridge independent.