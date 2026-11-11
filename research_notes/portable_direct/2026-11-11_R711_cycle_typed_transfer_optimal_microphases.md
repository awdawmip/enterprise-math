# R711 — Exact optimal microphase count for every fired subset of a typed X6 ring

Date: 2026-11-11 (Asia/Shanghai). Status: author-side candidate-model theorem, finite checker verified, independent review pending.
Parent: RS-X6-TRIADIC-CLOSURE-DYNAMICS. Immutable science input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000 V5 and X6 foundations).
Predecessors: R709b@15057fffe4aef6610e8686b20495771cd071f8ef and R710s@e78df51f52957e9402a38083056559a9f24742a1. Reuses the same R709b/R710s explicitly constructed frozen-gated V29-style counterflow scheduler.

## 1. Exact carrier and question

Take a labelled cyclic sequence of m>=3 X6 Cells, each carrying one native active triad (a 3-element subset of the six axes). The old Cell triad field is Johnson-adjacent around every selected fired edge. The R709b stock gate on edge i is f_i=[X_i adjacent X_(i+1)] [n_(i+1)^+ >=1] [n_i^- >=1]. Freeze every f_i and the old triad field at the start of one macrostep. For each fired edge i post EXACTLY TWO positive, source-labelled typed transfers: + from Cell i+1 to Cell i, and - from Cell i to Cell i+1. Each elementary microphase has capacity of at most ONE incident transfer per Cell. Commit the frozen-state triad update only after all event phases. Count the minimum number T_m(F) of sequential global microphases needed for the exact fired-edge set F. An empty event set has T=0.

## 2. Theorem — complete optimal phase classification

Let F be ANY subset of the m physical cycle edges, with m>=3. Then

    T_m(F) = 0                        if F is empty;
             2                        if F is nonempty and a matching;
             4                        if F is proper and has two adjacent edges;
             4                        if F is the full cycle and m is even;
             5                        if F is the full cycle and m>=5 is odd;
             6                        if F is the full triangle, m=3.

All bounds are attained by an explicit schedule. Here 'matching' means no two selected physical edges share a Cell; the two typed transfers of a single edge must still occur in different phases.

## 3. Exact lower bounds

Each fired physical edge has two distinct elementary transfers with the same two endpoints, so every nonempty schedule needs at least 2 phases. If F contains two adjacent fired edges, their common Cell is incident to four elementary transfers, forcing at least 4 phases. For even full rings this matches the lower bound. For odd full m>=5 each phase is a matching containing at most (m-1)/2 elementary events, whereas 2m events must execute. Four phases could execute at most 2m-2 events; at least 5 are necessary. For m=3 all three undirected edges of the triangle pairwise intersect, so all six elementary events require six distinct phases. These lower bounds refer only to the declared one-incident-event capacity, not to physical heartbeat duration.

## 4. Exact constructions and lossless macro equivalence

For an arbitrary nonempty fired matching: phase 0 does + on all fired edges, phase 1 does -. For a proper F containing adjacent edges: cutting the ring at any unfired edge decomposes F into paths; assign the pair of phase colors {0,1} to the first edge of each path, {2,3} to the next edge, and alternate. The lower-numbered color of each edge fires + and the higher fires -. Neighboring edges have disjoint color pairs. For a full even ring: alternate {0,1} and {2,3} around the entire ring.

For the full odd ring m=5+2r, r>=0, use five colors 0,...,4 and the sequence of two-element edge phase sets

    ({0,1},{2,3}) repeated (r+1) times, followed by {0,4},{1,2},{3,4}.

All consecutive sets are disjoint, including the wrap-around pair {3,4} and {0,1}, and the length is m. Each edge posts its + and - transfers in its two designated phases. For m=3, assign {0,1},{2,3},{4,5} to its three edges.

At each edge i, the + sender Cell i+1 has at least one + token in the OLD gate, and is the source of at most one + transfer during that macrostep; prior incoming + events only increase its stock. The analogous statement holds for the - sender Cell i. Thus ANY constructed phase order avoids negative inventory. Writing f_(i-1) for the previous edge on the cycle, the final integer stocks obey exactly

    n_i^{+'} = n_i^+ + f_i - f_(i-1);
    n_i^{-'} = n_i^- - f_i + f_(i-1).

The typed V29-style counters each record one positive + occurrence and one positive - occurrence per fired edge. The signed physical edge current sums to zero over the completed macrostep; within microphases it need not vanish. The triad commit uses the same frozen f and old state as R709b, hence the committed candidate dynamics and all its macro-boundary observers agree.

## 5. Every fired subset is a reachable one-step candidate configuration

Choose an X6 active-triad ring with Johnson-adjacent neighbors: for even m alternate 012 and 013; for odd m use 012,013,023 followed by alternating 012,013 pairs. All wrap-around adjacencies hold. For an arbitrary prescribed binary fired-edge vector f, set n_i^- =1 and n_i^+=f_(i-1). Then the old-stock gate on edge i equals the prescribed f_i. Each optimal phase class therefore has a concrete initial native-triad and nonnegative-inventory witness, without requiring a preselected event list during execution. This proves one-step attainability in the declared candidate scheduler; further autonomous iterates are a separate reachability question.

## 6. Exact finite certificate

R711_CYCLE_PHASE_VERIFY.js exhaustively enumerates all 2^m fired-edge subsets for each m=3,...,12 (8,184 subsets). It verifies the constructive colors, no Cell incident to two events in a phase, one positive occurrence of both types per fired edge, source-stock nonnegativity at every microphase, local stock-total preservation, declared R709b final macrostep equations, and the realized old-state gate. The matching, degree, parity and triangle lower-bound arguments above prove the optimum for arbitrary m>=3; enumeration checks implementation and all finite subsets in the declared window. The machine-readable exact certificate is R711_CYCLE_PHASE_RESULTS.json.

## 7. Reuse status and next question

BRC reuse: positive source-labelled triad paths (R709b/R710s), typed transfer source accounting (V29 candidate), and frozen Cell update (V36 candidate); status COMPOSE_APPLIED. This note extends R710s's exact even full-ring four-phase theorem to every frozen fired-edge pattern and to odd-length rings under the same explicitly declared macro interface. It does not reinterpret signed physical incidence as cancellation of positive BRC weights. Publication is an author-side noncanonical research artifact. Independent mathematical review and real frozen Source Link/Port capacity/timing reconciliation remain open.

Next execute the exact frozen native Link/Port timing read and test which of these phase colors are native legal micro-events without a prepare/commit extension. Then check that the candidate one-step paths can be iterated without changing the original gate model, and analyze which S3 histories stay reachable.
