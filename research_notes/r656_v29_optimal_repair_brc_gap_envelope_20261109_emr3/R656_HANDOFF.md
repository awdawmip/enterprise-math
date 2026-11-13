# R656 handoff — exact minimum-cost repair BRC gap envelope

2026-11-09 Asia/Shanghai, author-side unreviewed. Parent RS-X6-GLOBAL-TRIADIC-FIELD-NETWORK-LAW. Direct predecessor R655@8889e0e5c24fe6f33411725171733ca0b472543b; frozen science R462@18783e01e3646c72b7aab3b16d3f565e83e6446f; V29/V27/V17@b62110008321d9147212cb89f2627ff613c2550d unchanged.

R656-A: Given H actual allowed TRANSFER and K weighted directed receiver-target edits, composite J has primary unit cost w_ai=min_{j∈H(a)}d_K(i,j). For V27 signed code gap d_k=c_k(P)-c_k(T), each original-target edit i→j contributes d_j-d_i. Among all primary minimum-cost repair plans, the exact min and max attainable gap variations are secondary integer transportation extrema with per-edge q^-_ai and q^+_ai (minimum and maximum over j attaining w_ai). The scalar cost M=8L+1, M*w+q^- and M*w−q^+, computes both extrema with one min-cost flow per objective, respecting primary priority.

R656-B: An originally unique strict V27 winner T* survives **every** min-cost repair iff for every competitor T, original gap g_T plus exact smallest change Δ^-_(T*,T) stays strictly positive. The two signs are necessary and sufficient and witnessed by integer transport and explicit target-edit paths.

Concrete strict-fork witness: nonnegative PASS counts (2,1,2,2) on the original four edges 0→1,2→0,2→3,3→0; active triad S=(0,1,4). Old target port0 gives unique winner (0,1,5) gap1. A single actual sender licensed to receiver port1 or port3; K allows original target port0→port1 or port0→port3 at equal cost1. These two globally optimal repairs produce different strict winners (1,2,4) and (0,3,4), both gap1. Source-admitted native H/K and timing remain to be verified.

Reproduce R656_VERIFY.py with stdlib Python 3 and compare JSON. Two independent integer algorithms (residual mincost flow; exhaustive DP) agree across 265 weighted H/K graphs, 24,255 balanced tests, 15,591 feasible and 8,664 infeasible; 574 exact nontrivial gap envelopes. Marker R656_OPTIMAL_REPAIR_BRC_GAP_ENVELOPE_EXACT_PASS.

Next: retrieve actual native graph/event timing and propagate alternative cost-optimal outcomes through V17/V30 ordered holonomy; do not erase R648 pair provenance / R649 path order without observer descent theorem. Formal CLAIM, identity, Owner and independent Driver require their actual Source receipts.