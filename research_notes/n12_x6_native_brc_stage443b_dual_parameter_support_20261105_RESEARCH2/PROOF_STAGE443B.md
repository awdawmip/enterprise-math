# Stage443-B — Operation-budget FPT exact support for joint native-X6 histories

Date: 2026-11-05. Parent: Stage442-B, immutable research commit 4e2a1c4acf88cd4aa6eabbc1ff39dd2c1b6e4ceb, and Stage439-B exact repair theorem at 7f9456031a9fdfdf12836116f178a17bf50be965. Frozen scientific pins: GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53, EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, original P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Behavioral norms: current canonical main independently read. Status: author-side mathematical proof and exact finite verification, independent review pending.

## Mathematical model

Take A=+E1 and B=-E1 from the twelve native signed X6 directions. Original ordered paths P and Q of lengths m,n >=3 contain kP,kQ nonadjacent internal B defects and A endpoints. Define the full present observation O=(m,n,V_P,V_Q,J_P,J_Q,K), comprising both native six-vector endpoints V, both complete directed adjacent-pair histograms J, and absolute-position matches K through t=min(m,n). Given m,n,kP,kQ, the V and J are fixed for this restricted family; let d=t-K. Future P and Q each allow at most pP,pQ POP and rP,rQ APPEND operations, in any legal interleaving; APPEND has all twelve possible native letters; every observation prefix counts.

Stage439-B establishes in one fixed O-fiber the exact future-equivalence key R=(S_P,S_Q,A_P,A_Q,E), where:
- S_P=(P_i) for m-pP <= i <= m; S_Q=(Q_i) for n-pQ <= i <= n.
- If rQ>0, A_P=(P_i) for n-pQ+1 <= i <= min(m,n+rQ), else empty.
- If rP>0, A_Q=(Q_i) for m-pP+1 <= i <= min(n,m+rP), else empty.
- c=min(m-pP,n-pQ); E=([P_i=Q_i]) for c+1 <= i <= t.
All intervals are 1-based inclusive and may be empty. Repeated original position labels remain separate syntactic R slots.

## Theorem 443.1 — Dual-parameter exact support algorithm

Let b be the number of binary slots in R. Define H=4(kP+1)(kQ+1)(d+1), N=max(m,n). For each binary key r in {0,1}^b, run the Stage442-B weighted original-history transfer with the additional restriction that all specified R slots match r. Denote its terminal nonnegative integer count by M(r). Then

    q_F = SUM_r [M(r)>0] ,
    |F| = SUM_r M(r) .

The algorithm calculates q_F and, by streaming candidate keys, every requested exact class population using O(N H 2^b) weighted state-transition operations, at most O(H) simultaneous big integers, and O(b) active key bits. Each integer has O(m+n) bits, giving a conservative ordinary-addition bit bound O(N H 2^b (m+n)). The exact budget-only bound is

    b=(pP+1)+(pQ+1)+|A_P|+|A_Q|+(t-c)
      <=2(pP+pQ)+max(pP,pQ)+rP+rQ+2.

Therefore this algorithm is fixed-parameter tractable in total POP/APPEND budget even when the number of defects grows with N. Combining it with the Stage442-B subset-determinization algorithm yields O(N H min(2^b,2^H)) integer transitions by choosing the smaller of the two worst-case bounds. In the regime b=O(log N) and defect counts O(N), this yields a polynomial-time exact support algorithm with polynomial bit cost.

**Proof.** At each original index choose (x_i,y_i) in {0,1}^2 when the corresponding sources exist. Force x_i=0 at source P endpoints and y_i=0 at source Q endpoints, and require no adjacent 1 on either source. A transfer state (a,b',d',u,v) records used P and Q defects, mismatch count through original overlap, and the previous pair of defect bits. Starting at (0,0,0,0,0), each valid transition increments a,b',d' according to the chosen bits and has weight one. It accepts precisely the final defect totals kP,kQ and mismatch count d. To compute M(r) additionally enforce the given P_i/Q_i slots and equality constraints [x_i=y_i] in r. Conflicting repeated positions reject automatically. Each accepted original-transfer path is bijective with a unique raw (P,Q) in the present O-fiber having R=r. The positive integer terminal sum is exactly M(r). Every raw history has exactly one key r, hence masses sum to |F|. Theorem439.1 identifies distinct feasible R keys with exactly the distinct full-future observation classes, giving q_F. Per position there are at most H states and four outgoing choices. Run for all 2^b keys to obtain the cost bound. The displayed bound on b follows from |S_P|+|S_Q|=pP+pQ+2, |A_P|<=pQ+rQ, |A_Q|<=pP+rP and t-c<=max(pP,pQ). QED.

**Encoding and BRC layers.** Enumerating feasible keys in lexicographic order yields exact class ranking/unranking with O(2^b N H) worst-case transitions per query and no stored q_F-element codebook. For q_F>0, minimum fixed-width label length is ceil(log2(q_F)) bits. The Boolean predicate [M>0] is class support, M is the exact positive integer BRC population and a separate within-class index retains provenance. Given a fixed class, weighted suffix transfer recovers one requested raw pair in O(N H) integer operations plus Theta(m+n) output work. Parsing a raw pair and computing O,R take O(m+n) time. The unrestricted-operation-budget polynomial complexity question remains open.

## Actually executed reproduction

Execute Python 3 stdlib-only: python STAGE443B.py > STAGE443B_EXECUTED.json. Exact integers, no floats. Eleven parameter fibers were checked. At (m,n,kP,kQ,K,pP,pQ,rP,rQ)=(9,7,2,1,4,2,1,2,1), b=8, H=96, |F|=34, q_F=4, with all 256 candidate output strings evaluated. A larger-defect instance (17,16,5,4,9,1,1,1,1) has b=7, H=960, 59,437 raw pairs and exactly four future classes, calculated without explicit raw-pair generation. Eight smaller fibers have complete direct raw-history comparison against the weighted outputs.

Three unequal-length complete small fibers additionally use an **independent** all-twelve-direction future-state recursion, interning exact observation subtrees and comparing each pair of initial histories through every operation prefix. The (7,5,1,1,K=3,pP=pQ=rP=rQ=1) fiber contains 9 raw pairs, 4 future classes, 6,084 distinct labelled future states and 1,690 exact distinct observation subtrees; all 36 unordered history pairs agree with the R partition. Thus the independent cross-check includes nontrivial classes with multiple raw histories. Test scopes and per-case integer mass digests are in the actual execution JSON. The general statement depends on the Stage439-B author-side repair theorem, which awaits independent mathematical review.

## Stage444-B frontier

Develop a smaller canonical language representation or a concrete nonmergeable-subset witness as k and action budgets both grow. Compare actual deterministic subset-state complexity with the output-enumeration bound rather than only worst-case exponentials, accounting for bit sizes, crossover and provenance costs. Keep P000, ACTIVE worldview and frozen scientific pins unchanged.
