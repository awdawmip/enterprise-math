# R762GT — K4 STAR triadic incidence, minimal axis-count observer and signed BRC source loss

Date: 2026-11-20 (Asia/Shanghai). Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS` / publication `TP2-8B7E13C5904A2D6F1142`. Frozen scientific taskbook: `enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8`; P000: `enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Continuing R762GS (Draft PR #2841@7d6d1e04b5cf64b85bf800b431fe7934beffe738), which classified 75/291/350 orientation-state quotients of a *different moving-Port observer problem*. Historical contributor `EM-X6-3050F6` denotes provenance only. Independent Review: **NOT_REVIEWED**.

## Typed construction

Take the six P000 native axis **labels** to be K4 edges (E=(01,02,03,12,13,23)). At a chosen Cell anchor (c) in the native signed-X6 torsor, the four STAR supports are (S_v=\{uv:u\ne v\}), for (v\in\{0,1,2,3\}). They have three distinct axes each, and every two distinct supports intersect in precisely one axis.

As a **constructed, not native-admitted**, triadic incidence candidate, introduce eight source types (T_{v,s}), (v=0,1,2,3), (s\in\{+1,-1\}). (T_{v,s}) carries three equally sized, signed primitive force-quanta on the distinct axes of (S_v), attached to (c), and its triadic closure predicate is declared true. All other candidate primitive stable events are excluded. Thus arity three and pairwise native `PERP_E` hold by construction, and two-force configurations are not primitive stable events. The corresponding signed six-axis incidence **readout** is (sH_v\in\mathbb Z^6), where (H_v=1_{S_v}). It is a composite three-axis displacement/readout, **not** one primitive signed axis step. This definition alone supplies neither legal Cell/Link/Port/time updates nor a proof that the frozen original `TRIADIC_CLOSURE_E` admits these eight events. Vertex relabelings (S_4) act as **combinatorial** symmetries of the candidate; they are not asserted to be the full physical/native rotation law.

## Theorem 1 — unique two-to-three completion

Among the ({6\choose2}=15) unordered pairs of *distinct native-axis supports*, exactly 12 pairs are adjacent edges of K4. Each such pair lies in precisely one (S_v), so it has exactly one third-axis support completing a STAR triad. The remaining three opposite-edge pairs (\{01,23\},\{02,13\},\{03,12\}) lie in no (S_v). If the candidate signs are required to agree within (T_{v,s}), the 12 adjacent supports and two common sign choices yield exactly **24** signed two-force projections with unique candidate triadic lifts. Mixed signs have no lift under this particular sign convention.

**Proof.** Two different K4 edges have a common endpoint (v) exactly when they belong together to (S_v). Two distinct edges share at most one endpoint, so the completion is unique. K4 has (4\binom32=12) adjacent edge pairs and three disjoint pairs. The sign assertion follows from the defined candidate alphabet.

This explicitly realizes an apparent *two-term observation* by erasing one member of a three-force candidate event. It does not make the observed pair itself a primitive stable balance.

## Theorem 2 — exact minimal axis-count observer for unsigned triad inventories

Let (n=(n_0,n_1,n_2,n_3)\in\mathbb N^4) count source events of the four unsigned STAR types (signs and time/order forgotten). The observed six-axis incidence inventory is
[
y_{uv}=n_u+n_v,\quad uv\in E,\qquad y=B n,
]
where (B_{uv,w}=1) when (w\in\{u,v\}) and zero otherwise.

For coordinate restrictions to any subset (F\subseteq E), the map (n\mapsto(y_e)_{e\in F}) is injective **for all** (n\in\mathbb N^4) if and only if the unsigned edge-incidence matrix (B_F) has rank four over \(\mathbb Q\). The minimum number of retained named axis counts is **four**. Exactly **12 of the 15** four-axis subsets are injective: those whose **two omitted** edges share a K4 vertex. The remaining three subsets (omitting opposite edges) have rank three. All six five-axis choices and the full six-axis choice are injective. No choice of three or fewer named axes is injective on all \(\mathbb N^4\).

**Proof.** A kernel element (z\in\mathbb Q^4) obeys (z_u+z_v=0) along each retained edge. Within a connected graph this alternates signs; an odd cycle forces every (z_u=0), whereas a bipartite connected graph allows a one-dimensional alternating kernel. Removing two adjacent edges from K4 leaves a triangle plus one attached vertex, hence a connected non-bipartite graph and rank four. Removing two disjoint edges leaves (K_{2,2}), hence a rank-three matrix. Removing one edge leaves a connected graph with a triangle; retaining at most three rows cannot give rank four. The implication from rational rank deficiency to failure of injectivity on \(\mathbb N^4\) follows by scaling a nonzero rational kernel vector to integral coordinates and splitting its positive/negative parts into two different nonnegative inventories. Conversely full rank gives uniqueness over \(\mathbb Q\).

A concrete collision: retain (F=\{02,03,12,13\}) and omit (01,23). Then (n=(1,1,0,0)) gives (y=(2,1,1,1,1,0)), while (n'=(0,0,1,1)) gives (y'=(0,1,1,1,1,2)), identical on (F). The kernel direction is ((1,1,-1,-1)).

When all six axes are read, each (n_v) can be recovered from any triangle on the vertex labels:
[
n_u=(y_{uv}+y_{uw}-y_{vw})/2,
]
with three distinct vertices (u,v,w). A four-axis injective subset (triangle plus pendant edge) reconstructs its three triangle counts and then the fourth via the pendant reading.

## Theorem 3 — signed BRC history remains a nontrivial residual

Consider the **free candidate eight-letter source alphabet** \(T_{v,s}\), with the typed positive integer BRC counting carrier: each ordered two-letter word has mass one and observable net signed six-axis readout \(sH_v+tH_w\). Of the (8^2=64) ordered words, **exactly eight** have zero net readout: \((T_{v,+},T_{v,-})\) and its reversed order for each of four vertices. With uniform legal-free candidate branch choice, the exact probability of zero net signed displacement after two composite letters is \(8/64=1/8\).

**Proof.** \(sH_v+tH_w=0\) requires the same support \(S_v=S_w\), hence \(v=w\), and opposite signs. Thus the eight words are exhaustive. They are distinct as named sources and order, even though the complete net six-axis coordinate and the word length agree. Therefore an axis-count observer that reconstructs unsigned triad multiplicities does not automatically reconstruct signed event order or source identity; even full signed Cell displacement plus length loses this information. No identification with primitive signed cancellation or a native two-force balance is made.

## Exact verification, scope and next discriminating test

`R762GT_CHECK.py` reconstructs all six edges, four STARs, 24 vertex relabelings, the eight signed candidates, all 64 two-letter source words and every axis-observer subset. It computes ranks with exact rational Gaussian elimination; its evidence gives the complete rank histogram for each retained count (k=0,\ldots,6): \(1,6,15,20,15,6,1\) subsets respectively; for (k=4), rank-four/rank-three counts \(12/3\). It checks the explicit two-inventory collision and 12 unique third-axis completions. Local standard-library execution: **PASS**. Independent review: **NOT_REVIEWED**.

This exact incidence proof operates on the four K4-STAR support types; it is a different observer population from R762GS's 350 moving-Port orientation states and does not reduce that 350-state bound. Under P000, `PERP_E=120°` is the native angle, time remains an independent dimension, and the three force quanta remain distinct signed primitive *components* of the candidate event, not a claimed new primitive spatial direction. The native Cell/Port/Link/time permission is still open.

**Next:** provide or construct and check the frozen-compatible typed native `TRIADIC_CLOSURE_E` event/transport law; then test whether STAR candidate lifts are actually admissible under each named Port and time state. Recompute the incidence observer under the accepted gate, with source order and BRC multiplicity retained. Distinguish any failure of this candidate from a contradiction of P000.

Files: `R762GT_SIGNED_STAR_TRIAD_INCIDENCE_OBSERVER.md`, `R762GT_CHECK.py`, `R762GT_EVIDENCE.json`.
