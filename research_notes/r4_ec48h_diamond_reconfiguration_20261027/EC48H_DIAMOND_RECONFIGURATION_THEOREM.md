# EC48H — Two-decoder diamond reconfiguration beyond the EC48G conditions

**Result type:** author-side constructive theorem and executed exact-rational verification, 2026-10-27. **Scope:** auxiliary finite, strictly positive, two-stage BRC source law with a binary terminal decision. No native X6 dynamics, three-dimensional-slice transfer, formal Result, or independent Driver acceptance is asserted.

**Frozen inputs:** GLOBAL_KNOWLEDGE_V1 main@3ce6c9324e7c5af8d71c7adee778d084e7390d00 (P000 V4, ACTIVE worldview and account rules); Enterprise Math Source main@52be5e12112a44131c998cebeb424eed5a663f15 (portable research and control policy); predecessor EC48G@fd08c300cde18245565ce3b27d7ced523d35b627. Activity RA-EMR4-20261027-1233-EC48H-DIAMOND11; local Researcher-ID EM-R004-EC48H-20261027-1233-LOCAL.

## 1. Exact statement

Four histories h1,...,h4, three future labels y1,y2,y3, and arbitrary strictly positive raw Q-weights w(h,y). Fix any real numbers 0<L<M<H. Define raw sources Qraw(h,y)=w(h,y), Praw(h,y)=w(h,y)rho(h,y), with the ratio SYMBOL pattern:

    h1: H M L
    h2: H L M
    h3: M M L
    h4: M L M

Normalize Praw and Qraw separately to probability laws p and q. The actual likelihood ratios are r_L=cL, r_M=cM, r_H=cH, where c=sum(Qraw)/sum(Praw)>0.

A two-stage K-memory observer maps each history to a memory label m=f(h) and after observing y declares source P with a decoder probability u_m(y)∈[0,1]. The encoder may be deterministic (this is stronger than allowing a private randomized encoder), the terminal decoder may randomize privately, and there is no persistent/public shared random seed. Write (alpha,beta)=sum_(h,y) (p(h,y),q(h,y))u_f(h)(y). The full-history ROC set is the zonotope Z=sum_(h,y)[0,(p(h,y),q(h,y))]. Let S_K^det use deterministic encoding, S_K allow private random encoding, K_hull=min{K:conv(S_K)=Z}, K_seed=min{K:S_K=Z}.

**Theorem EC48H.1. For every choice of w>0 and 0<L<M<H above:**

    K_hull=K_seed=2   AND   S_2^det=S_2=Z.

In particular, an entire multi-free collision face outside BOTH sufficient cases of EC48G is realized using two decoder states. This is a parametric, not a single-instance, theorem.

## 2. Hull capacity exactly two

For strictly noncritical r increasing from 0 to infinity, the unique optimal strict-sign decisions 1{p-rq>0} form the following history word sets, independently of the positive Q-weights:

    r<r_L:         111,111,111,111             count 1
    r_L<r<r_M:     110,101,110,101             count 2
    r_M<r<r_H:     100,100,000,000             count 2
    r>r_H:         000,000,000,000             count 1

Each 0/1 row realized as a convex combination of decoder rows requires all participating decoder rows to equal that binary row coordinatewise. Thus an exposed unique strict-support vertex with two different history rows needs at least two memory labels even with stochastic encoding. With two labels all strict-support vertices are attainable; the support functions of conv(S_2) and Z agree for every noncritical slope and, by continuity, the three critical slopes. Hence K_hull=2. This is the precise EC48A signature argument.

## 3. Explicit complete boundary construction with deterministic encoding

At any critical r, the support functional V_r=max_Z(alpha-r beta) equals sum_(h,y) max(p-rq,0). An optimal w fixes strict-positive cells to 1 and strict-negative cells to 0; on tied cells w∈[0,1] is arbitrary. Consequently the exposed face is parametrized by beta ranging over [beta0,beta0+Qr], with beta0=sum_{p>rq}q and Qr=sum_{p=rq}q. Exhibiting a continuous optimal path reaching both ends covers the ENTIRE face, not just sampled points.

**Lower critical r_L.** Use decoder u=(1,1,s), decoder v=(1,s,1), with encoder assignments f(h1,h2,h3,h4)=(u,v,u,v). Here s∈[0,1]; all non-tied decisions stay 1. The four lower-ratio tied cells start at 0 and end at 1. Positive Q-weights give continuous strictly increasing beta over the face.

**Upper critical r_H.** Use u=(0,0,0), v=(s,0,0) and f=(v,v,u,u). The only tied cells are (h1,y1),(h2,y1), and all strictly lower-ratio decisions are 0. The full upper face is covered as s ranges 0 to 1.

**Middle critical r_M: genuine two-free collision.** Use decoder rows u,v and traverse three stages, s from 0 to 1 on each stage:

    Stage I:    u=(s,0,0)  v=(1,0,0)  f=(v,v,u,u).
    Stage II:   u=(1,0,0)  v=(1,s,0)  f=(v,u,v,u).
    Stage III:  u=(1,0,s)  v=(1,1,0)  f=(v,u,v,u).

At the Stage I/II junction u=v=(1,0,0), so the encoder reassignment makes no difference to the effective decision matrix; the concatenated ROC path is continuous. At the Stage II/III junction decoder rows and assignments match exactly. Every stage obeys the strict constraints:

    h1: y1=1,y3=0, y2 tied.
    h2: y1=1,y2=0, y3 tied.
    h3: y3=0, y1,y2 tied.
    h4: y2=0, y1,y3 tied.

Write q_ij=q(hi,yj). The three positive increments of beta are

    beta0=q_11+q_21;
    Delta1=q_31+q_41 >0;
    Delta2=q_12+q_32 >0;
    Delta3=q_23+q_43 >0.

Each is obtained by its stage's linear interpolation and all six tied cells appear exactly once. Therefore the three adjacent beta intervals concatenate to [beta0,beta0+Delta1+Delta2+Delta3]=[beta0,beta0+Q_(r_M)], covering the full middle face at the exact maximizing value V_(r_M).

At r_M, every history is tied, C=empty, |T|=4, the upper endpoint words A={110,101} and lower endpoint words B={100,000}. The free decoder budget is K_hull-|C|=2, smaller than |T|. Both |A\C| and |B\C| equal 2. Therefore neither EC48G condition (A: |T|<=K-|C|) nor (B: both outside endpoint counts <=1) applies. The new result isolates a genuine previously uncovered collision pattern and gives a complete solution for its entire positive parameter family.

**From edges to Z.** The only generator slopes are r_L,r_M,r_H, so these are all nontrivial exposed edges on one half of the zonotope boundary. Decoder complementation u->1-u maps (alpha,beta)->(1-alpha,1-beta), covering the opposite edges and their vertices. Therefore every boundary point of Z lies in S_2^det. Scaling both decoder rows by any tau∈[0,1] scales ROC coordinates by tau, so S_2^det is star-shaped about 0. Since every point of compact convex Z lies on a radial segment from 0 to its boundary, Z⊆S_2^det. The reverse inclusion follows from the cellwise [0,1] decoder probabilities. Thus S_2^det=Z. Combined with K_hull=2, K_seed=2. QED.

## 4. Rational witness and complete exact verification

Take w(h,y)=2 at every cell and (L,M,H)=(1/2,1,2). The separately normalized integer matrices are

    Praw=[[4,2,1],[4,1,2],[2,2,1],[2,1,2]], total 24;
    Qraw=[[2,2,2],[2,2,2],[2,2,2],[2,2,2]], total 24.

At central r_M=1, the support alpha-beta=1/6 and the full exposed beta interval is [1/6,2/3]. Its exact three-stage paths are

    I:   beta=(2+2s)/12, alpha=(4+2s)/12;
    II:  beta=(4+2s)/12, alpha=(6+2s)/12;
    III: beta=(6+2s)/12, alpha=(8+2s)/12.

The executed standard-library Python Fraction checker at this result's companion EC48H_VERIFY.py and EC48H_REPORT.json covers all 2^12=4096 Qraw matrices with entries in {1,2} at the displayed ratios and 144 further generated positive Qraw tables under three additional rational-level triples: 4240 model checks, 237440 counted exact support and beta assertions, zero failed assertions. It checks strict-word counts [1,2,2,1] and at parameters s=0,1/4,1/2,3/4,1 the decoder bounds, exact support equality, beta monotonicity, and exact critical-face endpoints. The universal statement is proved algebraically above; those finite computations check implementation and rational instances only. Native X6 and slice dynamics, richer future operations and independent formal mathematical admission remain separate work.

**BRC reuse:** EXTEND_EXISTING_TOOL based on EC48A strict signatures and EC48G face interpolation; preserve labelled history provenance, strictly positive branch weights and the exact conditional future observer. The theorem proves ROC preservation for this two-stage decision horizon only, not arbitrary observers/future operations. No cancellation of signed/phase amplitudes is used.

## 5. Next EC48I

Determine which general multi-free endpoint-incidence hypergraphs admit continuous optimal decoder-row mergers at K_hull. Either prove a general reconfiguration lemma or produce a strictly positive rational source with exact critical ratio, all EC48C optimal encoder-component intervals, and an uncovered nonempty rational open beta subinterval. Disconnection of the strategy graph or failure of one interpolating schedule is not itself a gap witness.
