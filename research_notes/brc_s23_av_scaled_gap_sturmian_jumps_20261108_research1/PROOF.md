# S23/AV: exact scaled-gap first-entry law and two-valued irrational-rotation jumps

Date: 2026-11-08 Asia/Shanghai. Status: AUTHOR_SIDE_ANALYTIC_PROOF_WITH_EXACT_RATIONAL_CHECKS; independent review pending.
Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34 (unchanged).
Predecessors: Draft PR #1777, research_notes/brc_s23_av_unimodular_first_entry_20261108_r1/PROOF.md and research_notes/brc_s23_av_endpoint_plateau_h2000_20261108_r1/PROOF.md.

## Definitions

In the two-point S23/AV iid auxiliary experiment the one-step distributions on labels (1,3,4) are P0=(1/2,1/4,1/4) and P1=(5/7,1/4,1/28). A prefix with k occurrences of label 1 and ell occurrences of label 4 has likelihood ratio Lambda(k,ell)=7^(k+ell)/10^k; label 3 pads without changing it. Set T_h={10^i/7^s: 0<=i<=s<=h}. N(h) is the least padded prefix length whose attainable likelihood ratios hit every open cell of the threshold partition T_h.

The previously certified adjacent thresholds in T_510 are A=10^431/7^510 and B=1. For t>=0, J_t=(A/7^t,1/7^t) is adjacent in T_(510+t): an intermediate threshold 10^i/7^s, multiplied by 7^t, would be between A and 1. If s<t or i>s-t the result is >=1; otherwise it belongs to T_510, contradicting adjacency.

Put r=ln(7)/ln(10/7), eps=79r-431, d=2074774-380295r, alpha=d/eps. Rational 45-term atanh enclosures for ln2, ln(5/4), ln(8/7) establish 0<d<eps and 2d>eps (VERIFY.py). The exact determinant is 79*2074774-431*380295=1. r is irrational: if r=p/q>0 rational, then 7^(p+q)=10^p, impossible by prime factorization. alpha is irrational too, because if alpha were rational then solving d=alpha*eps would make r rational.

## Theorem A: exact first occupation for EVERY scaled gap

For every integer b>=1 define

    a_b = floor(b*alpha)
    v_b = 380295*b + 79*a_b
    k_b = 2074774*b + 431*a_b.

For any integer t>=0 let b(t) be the smallest b>=1 with v_b>=t. Define L(t) as the least non-label-3 prefix length entering the PARTICULAR cell J_t. Then, for all t>=0,

    L(t) = k_(b(t)) + v_(b(t)) - t,

with attained joint counts (k,ell)=(k_(b(t)),v_(b(t))-t). Consequently N(510+t)>=L(t).

Proof: Lambda(k,ell) in J_t is exactly 0<k-r*(ell+t)<eps. Write v=ell+t. The vectors u=(79,431), w=(380295,2074774) are an integral basis since their determinant is 1. Every possible (v,k) therefore has a unique decomposition (v,k)=a*u+b*w, with integers a,b, and k-r*v=-a*eps+b*d. If b<=0 and v>=0, v=79a+380295b forces a>=0, giving k-r*v<=0. Thus b>=1. The strip 0<k-r*v<eps becomes b*alpha-1<a<b*alpha. Irrationality of alpha makes a=floor(b*alpha) the unique integer satisfying this. Both v_b and k_b increase strictly with b, since a_b is nondecreasing. Choosing the first v_b>=t therefore minimizes actual length k_b+v_b-t. QED.

## Theorem B: exact two-valued jumps and mechanical coding

For each b>=1, the integer increment Delta a_b=a_(b+1)-a_b is either 0 or 1 (because 0<alpha<1). At t=v_b the shortest length is L(v_b)=k_b, while at t=v_b+1 the b+1 entry takes over. Hence

    L(v_b+1)-L(v_b)
      = (k_(b+1)-k_b)+(v_(b+1)-v_b)-1
      = 2455068 + 510*Delta a_b.

The jump height is therefore EXACTLY one of 2,455,068 or 2,455,578. Between boundaries L(t) decreases by one per unit t. The jump word Delta a_b=floor((b+1)*alpha)-floor(b*alpha) is an irrational-rotation mechanical sequence: among b=1,...,m the number of large jumps is floor((m+1)*alpha), so their limiting frequency is alpha and the word cannot be periodic.

This theorem determines the one cell's first-entry sawtooth, not the full N(h), which can be governed by different cells.

## First new forced upper horizon for the h=510..2000 plateau

Since d<eps<2d, the first two entries are

    (b,a_b,v_b,k_b)=(1,0,380295,2074774)
                     (2,1,760669,4149979).

Therefore L(t)=2455069-t for 0<=t<=380295, and L(t)=4910648-t for 380296<=t<=760669. In particular:

    L(380295)=2074774
    L(380296)=4530352
    N(380806)>=4530352.

The previous full-threshold certificate established N(h)=2455069 for all integer h between 510 and 2000. Since N(h) is nondecreasing, the first strict increase after h=2000 occurs NO LATER THAN h=380806; its exact location remains open. The explicit endpoint bound is 2,075,283 above the preceding plateau value. No claim is made that all growth occurs at h=380806.

## Finite reproducibility and source scope

VERIFY.py uses Python Fraction only, with 45-term rational atanh bounds and explicit remainder; independently checks eps,d and the determinant, a_b and jumps for b=1..100, all candidate v=0..760669 for the base strip (exact adverse-bound comparisons), and T_510 base adjacency. RUN_EVIDENCE.txt contains actual stdout from the same executable. The universal results are proved by the lattice argument, not extrapolated from the finite scan.

The carrier is the joint (#label1,#label4) count with label-3 padding and finite-future likelihood-sign semantics. This is the auxiliary statistical observer, not a native X6/Heartbeat operation; P000/worldview and the scientific pin are unchanged. Native Owner/CLAIM/RA remain unconfirmed while Enterprise Math returns STATUS_DATABASE_UNAVAILABLE; publication is author-side mathematical provenance, independent review pending.

## Next scientific unit

Find the first h>2000 with N(h)>2455069 by screening the scaled gaps of other adjacent T_H threshold pairs, deriving their unimodular first-entry formulas and/or obtaining one larger all-cell endpoint certificate. Independent routes: full-lawful four-copy minimax delta4 and six-source/ten-label lawful bridge.

Sources: frozen science SHA above; two predecessor research_notes proofs in PR #1777; exact checker and actual stdout in this directory.