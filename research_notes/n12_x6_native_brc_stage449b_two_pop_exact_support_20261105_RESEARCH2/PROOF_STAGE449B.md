# Stage449-B — Two-sided one-POP exact future quotient and polynomial BRC population counting

Date: 2026-11-05. State: AUTHOR_SIDE_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Parent: Stage448-B commit 5988c9e8145cbede77b916707ee88761bf190d6b. Scientific frozen pins: global bf84bd7c61a2444b59b1da96be57df0e9ae47e53, EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Normative rules have separate current snapshots. Researcher EM-DIRECT-3D090D; activity RA-7F3C61715AB652A73B5CCA72. Formal ownership not established; researcher session has execution_authorized=false.

## Setup

Native X6 primitive signed alphabet D={+E1,-E1,...,+E6,-E6}. Initially each of P,Q uses only A=+E1 and B=-E1; original lengths 3<=m<n, original endpoints A, Bs isolated and internal, kP and kQ fixed. Keep the complete current observer O=(m,n,Vp,Vq,Jp,Jq,K): both six-component signed displacements, complete 12-by-12 ordered native-adjacency histograms and positionwise cross-source equalities K. Equivalently the overlap mismatch count d=m-K is fixed, along with the original defect counts. Each source may POP at most once; P may APPEND rP times and Q rQ times (nonnegative integers), in all legal interleavings. New APPEND directions can be any of all 12 signed native directions. Future equivalence means equality of full observer after every identical legal labelled-action prefix.

## Theorem 449.1 (two-sided exact future repair)

Let h=min(n-1,m+rP), where h>=m. Define the finite repair key, with one-based subscripts,

R449(P,Q) = (P_(m-1), Q_(n-1), Q_m, Q_(m+1), ..., Q_h).

Then two histories in one fixed current-O fiber have identical complete future observation traces for *all* legal labelled operation sequences if and only if their R449 keys coincide. Repeated positions are encoded once. For m>n swap source labels and their APPEND budgets; for m=n with original terminal A on both sides, the corresponding key is (P_(m-1),Q_(m-1)).

Proof (sufficiency): One POP per source never exposes earlier original positions than m-1 and n-1 respectively. Every POP of a known appended letter deletes its labelled adjacency edge. A POP of the original final A deletes the edge from P_(m-1) to A or from Q_(n-1) to A; therefore all endpoint V and internal directed-J changes are known from O, key and action labels. K changes only at lengths and newly compared indices. If the shorter source P removes its original terminal A, the discarded match at index m is determined by Q_m. When P adds symbols at indices m+1,...,m+rP, comparisons with still-original longer-source Q symbols can involve only indices up to n-1 and are supplied by Q_(m+1)..Q_h. Original Q_n=A is fixed. Symbols beyond Q's original prefix, or symbols replacing Q_n after a Q POP, are labelled future APPENDs. Likewise P symbols beyond its original length are labelled APPENDs. Thus any action prefix changes the full observer deterministically from O, R449 and labels. This is sufficient, including interleaved POPs of appended steps.

Proof (necessity): Immediate P POP distinguishes two P_(m-1) possibilities through Jp edge deletion (P_(m-1),A). Immediate Q POP distinguishes differing Q_(n-1) through Jq. Immediate P POP also distinguishes differing Q_m via decrement -[A=Q_m] in K. For each m<i<=h, keep Q unchanged and carry out i-m P APPEND operations, with the final appended symbol A. At that prefix, the final K increment is [A=Q_i]. Since each original Q_i is A or B, differing Q_i is distinguishable. If keys differ at several positions, the first different coordinate gives the corresponding shortest witness, with earlier output increments equal. Hence the full key is necessary. QED.

The key is an exact residual-sufficiency certificate for this declared future operation family. It preserves the joint alignment values actually needed for observer descent, distinct from arbitrary raw-history reconstruction.

## Theorem 449.2 (polynomial integer quotient support and population)

Write ell=h-m, w=Q_m...Q_h, q=Q_m, v=Q_h, s=#B(w), beta=P_(m-1), gamma=Q_(n-1). Let T(beta,q,b) count paired prefixes through index m in which P has exactly kP Bs, the first m positions have d mismatches, Q's first m positions have b Bs, P's penultimate symbol beta and Q_m=q. A left-to-right transfer using state (i,a,b,d',lastP,lastQ,beta) computes T exactly; forbidden adjacent Bs are excluded at transitions.

Let t=n-h>=1. Define U_t(v,gamma,R) as the number of Q completions at indices h+1..n containing exactly R Bs, with no adjacent Bs across the preceding v, Q_n=A, and Q_(n-1)=gamma. When t=1 the last gamma is already v, requiring gamma=v. Then a fixed full key has *exact* integer history population

M(beta,gamma,w) = sum_b T(beta,q,b) U_t(v,gamma,kQ-b-(s-q)).

The correction s-q avoids counting Q_m twice in the paired-prefix and output window. The decomposition is bijective: any original history uniquely specifies its paired prefix, fixed window and Q completion, and conversely.

Let W(q,s,v) count the distinct B-isolated binary words of length ell+1 starting with q, ending with v, and having s Bs. The value M for a specific word depends on it only through (q,s,v), so the number of supported exact classes and original history population are

qF = SUM_(beta,gamma,q,s,v) W(q,s,v) * [ M(beta,gamma,q,s,v) > 0 ],
|F| = SUM_(beta,gamma,q,s,v) W(q,s,v) * M(beta,gamma,q,s,v).

The W and U tables have simple left-to-right exact integer recurrences. With H=8(kP+1)(kQ+1)(d+1), cached T,W,U and aggregation take O(mH+n(kQ+1)^2) integer operations, O(H+n(kQ+1)^2) working integer cells as a safe upper bound. The integers have O(m+n) bits. Bit cost includes large-integer multiplication and output costs; reading or reconstructing an explicit original path is Omega(m+n). Lexicographic rank/unrank is a further available suffix-count construction, not executed in this stage.

## Distinguishing examples

P penultimate: with P1=0010, P2=0100, Q=00000 (A=0,B=1), current O agrees but immediate P POP deletes distinct Jp edges.

Q penultimate independently: m=5,n=10,rP=1,P=00000; Q1=0000000100 (B at 8), Q2=0000000010 (B at 9). Their current O and exposed window Q5,Q6 agree; immediate Q POP deletes different Q-original predecessor edges.

Q_m: m=5,n=7,P=00000; Q1=0000100 (B at 5), Q2=0001000 (B at 4). Current O agrees; immediate P POP changes K differently.

## Executed verifier and scope

Accompanying STAGE449B.py is executed Python 3 standard-library code, using arbitrary-precision integers. Independent full future-tree enumeration includes every legal POP/APPEND interleaving with one POP and one APPEND per side and all twelve signed append directions. It checked 8 parameter cases, 25 full-O fibers, 85 initial histories, 57 future classes and 162 history pairs; key equivalence exactly matched tree equivalence in each case, with 57,460 cached future state nodes. Independent population and support-DP comparison tested 1,708 parameter/fiber combinations, summing 15,804 explicitly generated initial histories and 3,984 supported classes across tests; all exact population and class counts matched. Large input (m,n,kP,kQ,d,rP)=(64,80,15,17,1,12) gave qF=523, original population=5,061,384,194,832,966 and 9,306 paired-prefix transfers, without enumerating the original paths. Actual stdout is preserved in STAGE449B_EXECUTED.json.

The finite audit checks implementation and selected small fibers. The general claims are proved by the arguments above and retain author-side evidence status pending independent review.

## Stage450-B

Study P with at most two POPs and Q with one, maintaining full twelve-direction APPEND and interleavings. Determine whether two original P predecessor edges and the corresponding Q alignment window suffice, and whether the exact support DP remains polynomial. Include distinguishing witnesses and explicit rank/unrank cost and report actual owner/CLAIM status. Keep original scientific pins.
