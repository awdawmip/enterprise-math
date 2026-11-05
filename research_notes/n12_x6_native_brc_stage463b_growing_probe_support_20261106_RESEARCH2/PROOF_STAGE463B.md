# Stage463-B — Polynomial exact BRC support for a growing P-probe window

Date: 2026-11-06. Author-side mathematical result; independent Driver review and formal Source Result pending.

## Frozen scientific scope and source typing

Stage462-B source: commit \`9ae3341366abfa4db2ba8dde3147529a23e885b5\`. The scientific pins are global \`bf84bd7c61a2444b59b1da96be57df0e9ae47e53\`, Enterprise Math \`2af3fc484eb11060b69e0afc1b562bcaf5ad1419\`, P000 blob \`bcc2590d3168a28f72e8b9f0f9b1f76faadcd488\`. Current behavioral norms are read separately.

Birth histories P,Q are source-distinct ordered words over A=+E1, B=-E1 embedded in native X6. Assume 2<=m=|P|<n=|Q|, fixed A endpoints, and nonadjacent internal B defects. The initial observation records both lengths, exact six-dimensional signed endpoints, complete directed 12x12 adjacency-count matrices of each source, and K(P,Q), the number of matching letters at shared positions. In this restricted original family the fiber is characterized by kP=#B(P), kQ=#B(Q), d=#mismatches on the initial overlap. Each original pair has one positive-integer BRC branch weight; multiplicity and source order are retained.

Future labeled operations: each source at most two POPs; P at most r>=0 APPENDs; Q at most s>=0 APPENDs. Every APPEND selects any of the twelve signed native X6 directions, and operations may interleave arbitrarily, including POP after APPEND. Every intermediate observation and labeled future tree is compared.

## Theorem 463.1 — exact future equivalence for arbitrary append budgets

Use one-based index sets:

\`\`\`
IP = {m-2,m-1} intersection {2,...,m-1}
IQ = ({m-1,m,n-2,n-1} union {m+1,...,min(n-1,m+r)})
     intersection {2,...,n-1}.
\`\`\`

Deduplicate. Let R463=(P_i : i in sorted IP; Q_j : j in sorted IQ).

**Theorem.** Inside a fixed complete initial-observation fiber, two original histories have identical complete labeled future observation trees iff their R463 keys agree. This holds for every finite r,s>=0. Increasing s does not refine the equivalence partition, and the P probe window saturates when r>=n-m-1.

**Sufficiency.** At any future node, the current history is a surviving original prefix followed by action-known appended letters. At most two original letters have been POPped from either source. Original endpoint and directed-adjacency changes therefore use only its fixed final A and the two preceding original letters, included in the key; appended directions and edges are action-known. The positional match K decomposes into original/original matches, updated from initial K by the deleted terminal comparisons, appended/original matches, and appended/appended matches. Original Q positions reachable by P's appended letters are contained in {m+1,...,min(n-1,m+r)}; P POP also requires the comparisons at m-1 and m. All are keyed. Q APPEND after at most two Q POPs first occupies position >=n-1>=m. Any P letter originally there is P_m=A, and all later P letters are action-known. Thus arbitrary Q APPEND sequences reveal no other original P direction. The key and the action word determine every subsequent observation, proving tree equality by induction.

**Necessity.** The all-POP subtree recovers the two terminal predecessor letters per original source from exact directed-edge removal and recovers Q_{m-1},Q_m from P's POP-induced K increments, after its terminal P letters are known. For every m+1<=i<=min(n-1,m+r), the action prefix consisting of i-m copies of APPEND_P(A) reveals [Q_i=A] as the incremental K change. In the original binary alphabet this determines Q_i exactly. The recovered coordinates distinguish any pair of different keys. All index clipping, m=2 and n=m+1 cases follow from fixed A endpoints.

## Theorem 463.2 — support counting without enumerating 2^|R463| keys

Let W=IQ (visible Q indices). It is the union of at most two contiguous components: the P probe block and the last two Q POP-visible positions. Keep a bounded signature T consisting of (1) at most two keyed P terminal variables; (2) first and last Q positions of each component of W; and (3) every visible Q position <=m. Thus |T|<=7 independent of r,n. In addition keep v=#B at visible Q positions W.

A positive-integer transfer over original slots i=1..n uses state

\`\`\`
(a,b,e,lastP,lastQ,sigma,v) -> mass,
\`\`\`

where a,b count B in the original words, e counts their original mismatches, lastP/lastQ enforce nonadjacent B, sigma stores the bounded boundary bits, and v counts B among W. At the fixed terminal fiber (kp,kq,d) it yields M(sigma,v), the total number of original pairs with that signature. This calculation enumerates transfer states, not original histories or visible keys.

For any fixed (sigma,v), let C(sigma,v) count legal *distinct visible Q strings* with the given boundary bits and #B=v, enforcing nonadjacent B within each contiguous visible component. A single-source positive-integer transfer computes C.

**Uniform-hidden-completion lemma.** Every legal visible Q string with the same (sigma,v) has the same number H(sigma,v) of compatible hidden original pairs. Hidden paired-prefix mismatches meet visible Q only at m-1,m (both fixed in sigma); hidden Q intervals meet visible Q only at component boundaries (also fixed). All other visible Q bits occur after the original P has ended, and their only contribution to the initial fiber is the total B count v. Exchanging one same-signature visible string for another therefore bijects hidden completions. The initial directed-edge observer depends only on kP,kQ and fixed A endpoints in this isolated-defect family. Consequently

\`\`\`
H(sigma,v) = M(sigma,v)/C(sigma,v)  (positive integer if M>0);
qF = sum_{M(sigma,v)>0} C(sigma,v);
|F| = sum_{sigma,v} M(sigma,v).
\`\`\`

Every individual supported key w has population H(sigma(w),v(w)). To rank or unrank, impose any prescribed lexicographic prefix bits of w on C(sigma,v; prefix), sum over positive signatures, and recursively follow the left-child class count. No supported-key roster is constructed.

For N=max(m,n), V=|W|<=n, and C<=7, the paired transfer uses at most O(2^C N(V+1)(kp+1)(kq+1)(d+1)) exact integer arithmetic steps. Visible support and prefix counting and rank/unrank are polynomial in N, with a conservative O(2^C N^4) step bound for one rank/unrank operation using the straightforward implementation and cached signature masses. Integer counts have O(m+n) bits, so conventional exact integer addition also has polynomial bit complexity. The algorithm is polynomial for r=O(n) (or larger after saturation), with pP=pQ=2 and the stated binary birth family.

## New strict distinguishing trace

m=3,n=11, P=AAA, Q1=AAAAABAAAAA, Q2=AAAAAABAAAA. Both initial observations (kp=0,kq=1,d=0,K=3) and the r=2 key coincide. Q1_6=B whereas Q2_6=A. Three consecutive APPEND_P(A) actions give K=5 and K=6 respectively. Thus the r=3 probe genuinely refines r=2.

## Executed computation and verification

\`STAGE463B_REPRO.py\` is the complete tested standard-library signature-transfer implementation. It checks 48 (m,n,r) small configurations from eight (m,n) pairs and six r budgets, comprising 780 nonempty fibers and 2798 checked supported classes; an independent original-history enumerator compared every class population, rank and unrank, all passed. A separate extended run (\`STAGE463B.py\`) also counted 3060 original pairs across these cases. Tested growing budgets include r>n.

At (m,n,kp,kq,d)=(64,80,15,17,1) the exact class counts are 49 for r=2, 471 for r=8 and 1232 for r=16, with 8, 14 and 19 variable key bits. Their original pair population is always 5061384194832966; the r=16 calculation uses 20 nonzero signature groups instead of enumerating 2^19 key candidates. At (25,38,5,7,1,r=15): qF=550, |F|=8407656.

The independently implemented full signed-X6 future-tree oracle checked (m,n,rP,rQ)=(2,4,3,0),(3,5,3,0),(2,4,1,2),(3,4,0,3), processing 292149 memoized future states. The finite check covers exactly these small configurations; the general result rests on the reconstruction and transfer lemmas.

## BRC observer-preservation interface

The scientific substrate is the positive branch/multiplicity semantics of \`definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json\` at the frozen source pin. We preserve original ordered pair population, source identity and exact multiplicity H; the R quotient is certified only for this declared family of future observations and operations. APPEND still uses all 12 native X6 directions.

## Open problem / Stage464-B

Extend the bounded-signature transfer to >=3 POPs per source and determine whether the number of boundary fields can remain independent of r. Separately extend original birth alphabets to >=3 native signed directions, where equality-bit probes alone may fail to reconstruct a full direction. Establish exact observer keys, BRC population and rank/unrank within each explicitly typed model before widening the claim.
