# Stage368-B — exact global localization at E=11/5000

Date 2026-11-02, Research2 portable-author scientific work. Frozen science: GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; original project P000 V5 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current rules read at GLOBAL main c3c9c172fe5ca17dc1695081052f3a650e1882c4 and EM main 85b54b1fbceb232e2ab8f4067215b9299966064d. Exact author proof and independent review remain distinct.

## Original model and theorem

For k=0,1,2,3 put B_k(z)=z^k(1-z)^(3-k), w=(1,3,3,1), m=(61,21,9,9),
r_k(x,y)=(4B_k(x)+B_k(y))/5-m_k/160 and b(x,y)=(5/32) Σ_k w_k |r_k(x,y)|.
All 16 labelled audit comparisons are preserved by
D3(a,z)=(1/2) Σ_k w_k |B_k(a)-B_k(z)| and
c(x,y)=[63D3(1/4,x)+D3(3/4,x)+9D3(1/4,y)+7D3(3/4,y)]/256.

Let q* be the unique common r0=r1=0 root near (0.23108,0.55551), β*=b(q*), and fix E=11/5000. **For ALL real P,Q in [0,1]^2**, the exact budget condition
b(P)+b(Q) <= 2β*+E
implies BOTH sources belong to
R=[219/1000,239/1000] × [51/100,16/25].
The result globally localizes the unrestricted four-parameter feasible set to R×R.

## Algebraic root isolation and budget ceiling

Let xL=2310839/10^7, xU=2310840/10^7, yL=5555086/10^7, yU=5555091/10^7.
The exact checker confirms r0(xL,yU)>0>r0(xU,yL) and r1(xL,yL)>0>r1(xU,yU).
In this box r0 decreases strictly in both arguments; r1 increases in x and decreases in y. Hence the unique r1=0 implicit graph y=Y(x) crosses from positive r0 to negative r0, and r0 strictly decreases along that graph because Y'(x)>0. Thus there is exactly one common root inside the box. There r2>0>r3 and Σ w_k r_k=0, implying β*=(15/16)r2(q*).
Since B2(z)=z²(1-z) increases on (0,2/3), exact rational substitution gives

β* < (15/16)r2(xU,yU)
=60466487110135696287/16000000000000000000000
< 189/50000.

Consequently 2β*+11/5000 < 61/6250 = 976/100000.

## Exact 604-leaf continuous-domain lower bounds

The accompanying exact Fraction program constructs an exhaustive binary partition of the WHOLE [0,1]², not a point sample. Its leaf proof establishes simultaneously:

(A) b(x,y) > 377/100000 for every real x,y∈[0,1].

(B) b(x,y) > 599/100000 for every real (x,y)∉R.

For a box J=[x0,x1]×[y0,y1], the extrema of each B_k(z) are its endpoint values plus the interior critical value at k/3 (when present). These yield exact rational bounds r_k(J)⊆[l_k,u_k]. Set a_k=0 if l_k<=0<=u_k and otherwise a_k=min(|l_k|,|u_k|). Then
L(J)=(5/32) Σ w_k a_k <= b(x,y) on all of J.
Prune a box as OUTSIDE_FORBIDDEN when L(J)>599/100000, or INSIDE_GLOBAL_BOUND when J⊆R and L(J)>377/100000. Otherwise bisect x if 4(x1-x0)>=(y1-y0), else y; continue. Each split is an exact closed-box cover, including shared boundaries.

The executed checker closed all nodes: 603 splits; 604 leaves comprising 338 OUTSIDE_FORBIDDEN and 266 INSIDE_GLOBAL_BOUND; maximum depth 28; minimum exact positive decision margin 129187931/13743895347200000. No leaf remained unresolved. Its deterministic full 604-leaf CSV can be reproduced with:
python REPRO_STAGE368B.py --emit CERTIFICATE_STAGE368B_LEAVES.csv
CSV SHA256 adcca00c9a5cf502ab03fcecf324b321683487dab432b28ac59ee0b549c16040, 43413 UTF-8 bytes. The saved stdout is from an executed run; a second no-argument execution matched its diagnostics byte-for-byte.

## Consequence and scope

If P lies outside R, then b(P)>599/100000 by (B), while b(Q)>377/100000 by (A). Hence b(P)+b(Q)>976/100000=61/6250, contradicting the strict budget ceiling. Exchange symmetry yields P,Q∈R.

This exact universal result uses the frozen full-labelled Bernoulli/BRC auxiliary observer. It is a global feasible-set reduction, not global cost optimality or a native P000/X6 realization. It advances the open mother problem by restricting all cost competitors at E=11/5000 to a compact rational domain; Stage367-B separately gives a four-parameter local optimum near the post-audit cusp. Native CLAIM, Driver mathematical review/admission and X6/independent time/three-dimensional slice/Cell codec transfer remain separate.

## Stage369-B continuation

Inside R×R, search a rational feasible competitor beating the algebraic candidate with certified reference enclosures, or construct an exact b/c interval covering certificate excluding a continuous nonlocal cost-competition region. Preserve all four port labels, frozen pins and actual evidence scope.
