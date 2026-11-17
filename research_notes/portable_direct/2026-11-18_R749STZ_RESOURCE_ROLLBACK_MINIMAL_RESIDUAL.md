# R749STZ — Exact rollback residual for a finite-state resource ledger

Date: 2026-11-18, Asia/Shanghai. **Evidence:** AUTHOR_EXACT_NOT_REVIEWED. **Research route:** independently authored portable TASK_RESEARCH; no shared Task CLAIM, no native triadic event or formal Result/Review is asserted.

**Scientific source pin:** awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389, unchanged. **Direct predecessors:** R749STW@2f0f17bcf0709b6f6b3bc8eeffff856a13999528, R749STX@3945736c7aa06f0b9e81d45fee5f3f241fc09f94, R749STY@51cd26d959d1cfb5f9c21e312e34a1287803e75d.

## 1. Precise model and new question

Retain the five named sources A,B,C,D,E, frozen scalar weights (1,1,2,3,6), and the **full native X6 Cell** with one chosen chart anchor. Each letter is represented by a *composite path-formal adapter* step along one selected raw native axis, as in R749STW. The unused sixth raw coordinate is chart-relative, not a deleted spatial dimension. All words with one fixed source inventory n have the same raw X6 endpoint and frozen scalar total; order and extra ledger state are separately typed. A history sequence is ordered by a separately typed time index, not a seventh spatial coordinate.

Introduce a finite **candidate resource ledger** Q (nonempty), initial state q0, and deterministic source-dependent maps T_i:Q→Q. For a word w=w1...wℓ, define q_j=T_{w_j}(q_{j−1}). The current ledger q_ℓ is fully visible; on publicly chosen APPEND_i it evolves by T_i. A named POP outputs the last source letter, removes it, and **restores the actual stored predecessor ledger value**, not an arbitrarily chosen inverse. At most r POP operations may be used during the entire adaptive future experiment (including POPs of publicly appended steps). The current ledger, endpoint, length, legality and remaining budget are visible after every operation; the initial inventory is known. This is an explicit mathematical observer adapter, not a claim that a physical X6 Port permits POP or rollback.

**Question:** Is the old source suffix from R749STW sufficient when the candidate resource update maps are noninjective? What is the exact additional residual?

## 2. Sharp signature theorem

Let s=min(r,ℓ) and let u=w_(ℓ−s+1)...w_ℓ be the final s named letters in chronological order. Write b=q_(ℓ−s) for the ledger state just before u. Define the signature

\[
\boxed{\quad \Sigma_r(w)=(q_\ell,u,b),\qquad q_\ell=T_u(b).\quad}
\]

**Theorem 1 (all adaptive futures).** For histories w,v with the same inventory n, the following conditions are equivalent:

1. Every finite adaptive future using publicly chosen APPEND operations, named POP operations with lifetime budget r, and the declared visible observations yields identical outputs and legalities.
2. \(\Sigma_r(w)=\Sigma_r(v)\).

**Necessity.** A zero-operation observation reads q_ℓ. Then execute s POPs: their named outputs recover u in reverse order, and the ledger after the last POP is b. Thus unequal signatures have a distinguishing admissible experiment. The case s=0 is immediate because b=q_ℓ and u is empty.

**Sufficiency.** Couple two initially equal-signature histories under identical adaptive actions. Public appended letters and their resource updates agree. Every POP must first remove identical public appended letters if any; a POP of an original letter removes one of the common stored suffix u. At most r original letters can ever be removed. The state of every remaining original suffix is reconstructed exactly from b and its retained letters by forward composition of the T_i. At the boundary after s original POPs the observed ledger equals b in both histories. No operation can expose an earlier original letter or ledger value within the lifetime budget. Hence outputs, later adaptive choices and legalities coincide by induction. This includes arbitrary interleavings of APPEND and POP, not only consecutive POPs. QED.

## 3. Exact number of equivalence classes and optimal bits

For an inventory vector c, define the reachable ledger set

\[
R(c)=\{T_x(q_0):x \text{ is any permutation of inventory }c\}.
\]

It has the exact recurrence \(R(0)=\{q_0\}\) and
\(R(c)=\bigcup_{i:c_i>0}T_i(R(c-e_i))\).
Fix a *visible terminal ledger value* q reachable with inventory n. For each feasible chronological length-s suffix u with count vector a(u)≤n, the legal predecessor states are precisely

\[
B(u,q)=\{b\in R(n-a(u)):T_u(b)=q\}.
\]

The exact number of future-distinguishable history classes **within the known terminal-q fiber** is

\[
\boxed{\quad C_s(n,q)=
\sum_{\substack{u\in\{A,B,C,D,E\}^{s}\\ a(u)\le n}}
 |B(u,q)|.\quad}
\]

These are disjoint pairs (u,b); every such pair is realized by some prefix with inventory n−a(u). Ranking the feasible pairs gives a matching upper bound to the pigeonhole lower bound. Therefore the optimal additional fixed-width memory beyond the already known terminal q and inventory is

\[
\boxed{\quad m_s(n,q)=\lceil\log_2 C_s(n,q)\rceil.\quad}
\]

If one common word width must handle all terminal ledgers, use \(\max_{q:C_s(n,q)>0}m_s(n,q)\). Always \(C_s(n,q)\le |Q|N_s(n)\); therefore the resource-boundary state costs at most \(\lceil\log_2|Q|\rceil\) bits beyond a named-suffix codec in this observer.

## 4. Exact zero-extra-memory criterion

For fixed n,q,s, **suffix plus visible terminal ledger q already suffice** if and only if

\[
\boxed{\quad
\forall u\ (a(u)\le n,\ |u|=s),\quad
T_u|_{R(n-a(u))}\text{ has at most one preimage of }q.\quad}
\]

If some u has two reachable predecessor states b≠b' both mapping to q, they yield two histories with the same total X6 endpoint, same terminal ledger and same named suffix, but POP s reveals different b. Conversely, unique reachable preimages make b a function of (q,u), so Theorem 1 applies. In particular, **if every T_i is bijective on Q, the old suffix plus final q are always sufficient** for every n and r. The converse does not hold without reachability hypotheses.

## 5. Minimal explicit noninjective witness

Take Q={0,1}, q0=0, and maps:
T_A(q)=0, T_B(q)=1−q, T_C(q)=0, T_D(q)=q, T_E(q)=q.
Use n=(1,1,1,0,0) and r=1.

\[
\begin{array}{c|cccc|c}
w & q_0&q_1&q_2&q_3& \text{one-POP suffix}\\
ABC &0&0&1&0&C\\
BAC &0&1&0&0&C
\end{array}
\]

Both share frozen scalar sum 4, the same entire raw X6 Cell endpoint, the same visible terminal resource q3=0 and the same final named source C. But after one POP, the recovered resource is respectively 1 and 0. Thus **the POP-only source suffix quotient is not future-safe once rollback of a noninvertible resource ledger is observable**.

Across all six permutations with this inventory, the terminal-q=0 fiber has four (u,b) classes: (A,0),(A,1),(C,0),(C,1). Its suffix-only quotient has two classes. Optimal memory increases **sharply from one to two bits** in this fiber. The two terminal-q=1 histories both give (B,0), one class.

## 6. Executable finite certificate

The accompanying JavaScript program is dependency-free and runs in Node.js. An actual V8 execution in this research turn returned PASS. The script exhausts **all five-source words of lengths 0 through 7**, for each of two explicitly defined two-state resource machines. It separately calculates (i) source-word signatures from the actual ledger traces, (ii) predicted classes from inventory reachability sets, and (iii) the exact zero-extra-memory criterion. It checks POP budgets 0 through min(3,length).

Result summary, machine RESET_FLIP: 97,656 word instances, 1,170 (inventory,terminal-q) fibers, 4,650 inventory/ledger/budget checks, **1,028** checks in which the boundary resource adds information. Machine BIJECTIVE: 97,656 word instances, 792 fibers, 3,140 checks and **zero** extra-boundary cases. All matching count/criterion comparisons passed. The universal theorem relies on §§2–4; the finite test does not certify arbitrarily long words or physical native event permissions.

Files: research_notes/portable_direct/R749STZ_RESOURCE_ROLLBACK_CERT.js and research_notes/portable_direct/R749STZ_RESOURCE_ROLLBACK_RESULTS.json. Program and machine-readable results are provided with this article for independent recalculation.

## 7. Native BRC transfer boundary and next discriminating question

Existing WBRC-T31 permits positive-rational future contexts connecting only **visible** ports/external states; a hidden ledger read, source POP or arbitrary state rollback is not licensed by that theorem. WBRC-T32 gives W_eff as the minimal total-mass port signature within its declared observer, with no extra residual needed for that narrower future language. The newly derived q-boundary requirement therefore applies to the **declared resource-rewind observer**, and cannot be silently promoted into a physical BRC or triadic Cell/Link/Port event.

Next: find a currently admissible native Port/resource event whose visible state updates include noninvertible operations and whose future license permits a restoration, delayed checkpoint or boundary probe. Explicitly calculate its reachable inverse fibers, first with the true resource/triadic/time predicates, and then test whether the resource-boundary residual descends from the native model. If all admitted operations are forward-only, prove the stronger zero-extra-residual result for that actual license instead.

Sources: P000 V4/V5, ACTIVE worldview, RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM, R749STW/STX/STY, definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md WBRC-T30..T32; frozen science pin a72226e2430ffa4786321ac86e7f0c599d5f0389.