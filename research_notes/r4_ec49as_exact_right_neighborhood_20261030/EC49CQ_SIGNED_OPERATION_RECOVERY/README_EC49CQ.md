# EC49CQ — Signed X6 new-operation recovery of the nine-dimensional BRC rolling kernel

2026-10-31 · author analytic proof / executed native-positive-BRC exact checks / portable draft / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED. Full verbatim theorem, Python verifier, exact JSON literal witnesses, native source and run log: `EC49CQ_FULL_EVIDENCE.tar.xz` in this directory.

## Frozen sources and native scope

GLOBAL_KNOWLEDGE_V1 `awdawmip/chatgpt-global-knowledge main@18e4eea156c607319d3f83019da98b5a5f176c14`; Enterprise Math `main@adccf931b55c7460362ca035fac7c8d468f04e8d`; inherited author-side EC49CP `224ffa708d4e39ab0af93a253d745e09d45ee237`. Native exact X6-BRC source `native_signed_brc.py` Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176`. P000/ACTIVE worldview unchanged; six signed native spatial axes remain six axes, time is separate; a formula involving two or three coordinates is not a complete native three-dimensional slice.

An ordered primitive is in `±E1,…,±E6`. Two **positive** exact weighted BRC instruments have positive-step weights `(2,3,3,2,1,1)`, `(3,2,3,2,1,1)`, negative-step weights all one; the third channel is literal unweighted path count. The A/B DFA detects the ordered subwords `A=(+E1,+E2)`, `B=(+E2,+E1)` and has eight reachable states `(qA,qB) in {0,1,2}²\{(1,1)}`. Four joint-completion labels `00,01,10,11` times 3 BRC types give 12 return-to-same-relative-Cell outputs. No signed-phase cancellation or physical dynamics is inferred.

Original complete operation language `S`:
```text
a = (-E1,-E1)                net -2E1
b = (-E2,-E2)                net -2E2
c = (+E1,+E2,-E1,-E2)       net 0
d = (+E2,+E1,-E2,-E1)       net 0
```
`O_h^ε` observes ε and all nonempty words in S of 1..h complete operations. In the inherited *author-side* EC49CP theorem, for `h>=1` and common even true-path length `n>=max(10,2h+6)`, the old minimal rational-linear additive space for `O_(h+1)^ε` has dimension `9h²+39h+42`, its joint next-step original-operation readout has rank `9h²+39h+33`, and rolling kernel dimension is exactly **9**, supported at zero displacement. Those inherited saturation premises remain subject to independent Driver review.

## CQ-1: a genuinely new net-positive primitive complete operation recovers the old nine-dimensional kernel

Take `e=(+E3,+E1,+E1,-E3)`, net `+2E1`, which is different from every old operation's net displacement. The **complete two-operation word** `ea` has net zero and primitive letters `(+E3,+E1,+E1,-E3,-E1,-E1)`. For **every** ordered native history (and by addition, any nonnegative multiset), exact twelve-coordinate BRC outputs satisfy, separately for each of four completion tags,
```text
R_ea(BRC_weight_0) = 12 * R_epsilon(BRC_weight_0)
R_ea(BRC_weight_1) = 27 * R_epsilon(BRC_weight_1)
R_ea(unweighted_count) = 1 * R_epsilon(unweighted_count).
```
Proof: first `+E3` resets any unfinished one-letter waiting state; `ea` has no `+E2`, so it cannot complete a new A or B. Already completed flags persist. The exact primitive positive BRC multiplicative weights are `(3·2·2,3·3·3,1)=(12,27,1)`; net displacement is 0. The identities therefore hold on every literal history, including boundary DFA states, with no exchange of branch or signed-amplitude semantics.

At the origin fiber every old *nonempty* S return suffix consists exclusively of c/d. Their rows span `{1,uA,uB}`, where `uA=1[qA=0]`, `uB=1[qB=0]`, rank **3** per BRC type. Four ε completion rows increase the rank to **6** per type. On actual six DFA states
`Q6=[(0,0),(0,1),(0,2),(1,0),(2,0),(2,2)]`,
the six rows `[epsilon00,epsilon01,epsilon10,epsilon11,c10,d01]` form a 6×6 integer matrix with determinant **−1**.

Choose three origin-fiber kernel directions
```text
k1 = δ(2,0)−δ(1,0)
k2 = δ(0,2)−δ(0,1)
k3 = δ(0,0)−δ(2,0)−δ(0,2)+δ(2,2).
```
The **three** ea completion labels `01,10,11` restrict to the matrix
```text
        k1  k2  k3
ea 01    0   1  -1
ea 10    1   0  -1
ea 11    0   0   1
det = -1.
```
Each of three BRC types has an invertible nonzero scalar weight factor. Thus precisely **nine scalar readouts** (these three labels × three types) are necessary and sufficient to distinguish the old rolling kernel: `rank((T_old,R_ea|{01,10,11}))=9h²+39h+42`, `ker=0`, in the inherited stable-length domain. Necessity is by old kernel dimension9; sufficiency is by this explicitly invertible 9×9 restriction. This is an observer statement **on the old quotient space** because ea is an exact scaled ε coordinate already present in `O_(h+1)^ε`.

## CQ-2: shortest primitive operation in this one-compensation class is length 4

Restrict to `net(e')=+2E1`, append the old a as a fixed single compensating operation, and consider only its complete `e'a` current-return readout together with old c/d future rows. Signed X6 parity gives an even length at least 2. The only length-2 candidate is `(+E1,+E1)`; its compensated rows lift the DFA rank 3→**5** per type, leaving a missing direction. The displayed length-4 e lifts rank 3→**6**, so 4 is minimal **in this explicitly restricted class**, not universally among different internal observers or permitted net displacements.

## CQ-3: strict nonfactorization obstruction for the enlarged complete-operation language

Let two authentic length-2 histories be `p=(-E1,-E1)` and `q=(+E3,+E3)`. Their old `O_h^ε` outputs both vanish for **every h**, since the original S operations cannot compensate either history's displacement. After one e, `R_e(p)` has tag00 = `(12,27,1)` while `R_e(q)` is zero. Therefore **full append-e current observation does not factor through the old minimal state**. The nine-dimensional recovery above does not supply a complete recursively sufficient state for `S'=S∪{e}`; newly accessible negative displacement fibers must be restored before claiming an extended-language closure.

## Exact real-path certificate and executed scope

Six actual length-8 primitive words having the same signed symbol inventory `(1,1,2,-1,-1,-2,3,-3)` reach Q6, have zero displacement and common instrument contributions `(36,54,1)`. Prepending `(+Ei,-Ei)` for i=1,2,3 gives the 3×3 type multiplier matrix
```text
[2,3,1]
[3,2,1]
[3,3,1]
det = 1.
```
Integer combinations `(-1,0,1)`, `(0,-1,1)`, `(3,3,-5)` isolate each BRC type. Combining with k1,k2,k3 yields **nine integer certificates consisting entirely of length-10 actual signed-X6 histories**. Each signed formal difference is explicitly split into **two genuine nonnegative path multisets**, with no fictional cancellation of positive BRC physical mass. The selected ea 9×9 literal minor is
```text
−(432 · 1458 · 1)^3 = −249875578388054016 != 0.
```
The *actually executed* standard-library `VERIFY_EC49CQ.py` enumerated each of **1,364** original S suffix words through complete-operation length5 against each of the nine witness differences (**12,276 literal comparisons**, all twelve coordinates exactly zero for the old nonempty S words), confirmed the nonzero ea readings and the p/q obstruction, and recomputed the old and compensated DFA ranks. The unbounded-h old-suffix assertion follows separately from the analytic DFA row-span argument. Calls to the unchanged native `endpoint_weight` and `endpoint_multiplicity`, compared with explicit ordered-path enumeration, returned origin totals `(W0,W1,count)` for n=0,2,4 of `(1,1,1)`, `(24,24,12)`, and `(1560,1560,396)`. This exact combinatorial scope says nothing about physical propagation, pi, time dynamics, signed phase cancellation or theorem admission.

## Full evidence, reproducibility, retention

`EC49CQ_FULL_EVIDENCE.tar.xz` is a **complete byte-verified source archive** (11,024 bytes, SHA256 `bf1bc17f12153215910958b40d368b7eca0bd673ddff7d43413417b9febdc57f`, Git blob `1e9f2e107d80997e8c5be6bea355779c83d70515`). It contains full original `README_EC49CQ.md`, unchanged `native_signed_brc.py`, actual `VERIFY_EC49CQ.py`, complete explicit nine-witness `EXACT_REPORT_EC49CQ.json`, actual `RUN_EC49CQ.log`, and `NEXT_EC49CR.md`. No credential or private source file is present.
```sh
mkdir -p /tmp/ec49cq
tar -xJf EC49CQ_FULL_EVIDENCE.tar.xz -C /tmp/ec49cq
cd /tmp/ec49cq
python VERIFY_EC49CQ.py --max-h 5 --output EXACT_REPORT_EC49CQ.json
```
Classical background: Balle–Panangaden–Precup (2019), *Singular value automata and approximate minimization*, DOI 10.1017/S0960129519000094; it is not the proof or a novelty claim.

Actual service boundary on 2026-10-31: Sites gateway 0.6.11 `research_authority_granted=false`; bounded native owner query gave `CONTROL_QUOTA` rather than active owner. The research is a durable **author-side portable draft**, not a CLAIM, Result, independent Driver review, Working Truth or mathematical admission. Next unit `EC49CR` is the exact rank and genuine path saturation for the enlarged S' language; see `NEXT_EC49CR.md`.
