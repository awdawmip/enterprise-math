# PREFIX-641 — Exact integer BRC sliding-query contraction and measured crossover

Date: 2026-11-10 Asia/Shanghai. Status: AUTHOR_SIDE_EXACT_CHECKED / UNREVIEWED. Parent task: RS-X6-NATIVE-ROTATION-DYNAMICS; publication TP2-6A1F9D8C2047E3B51C01; no formal CLAIM. The immutable task scientific references remain at a72226e2430ffa4786321ac86e7f0c599d5f0389. This author-side study continues the exact original-action code packaged with PREFIX-638/PREFIX-640 (declared author provenance anchor f42f2906d77f24085c123f3ccfe9667d41caa96d), without rebasing task science.

## Selected native object
Original 48 STAR phases, 96 labelled ports and 576 labelled BRC actions. Motifs P0=(485,316,52,174), P1=(52,174); the Aho–Corasick observer retains overlapping hits and produces six moment components (Z,U0,U1,V00,V01,V11). P000 and HEARTBEAT_WORLD signed X6 premises are unchanged. Earlier tools reused: PREFIX-638 for exact original actions/AC/independent DP; PREFIX-640 for fraction-free six-jet matrix products. Scope: exact positive-weight labelled-path model, nonnegative rational time gates, including zeros.

## Theorem: cut-invariant common denominator through source and sliding window

Let the initial 96-port vector r0 have common integer denominator d0>0. At step i write gate g_i=a_i/b_i>=0, b_i>=1 (reduced nonnegative rationals). Multiplying the original native 96-port transition P_i and expanded AC six-jet transfer T_i by b_i replaces every gated unit weight by a_i, every ungated unit weight by b_i and every zero base weight by zero. Let v_t be the integer port state propagated from d0*r0 by products (b_i P_i), i<t. Let M[t,n] be the integer ordered six-jet product of (b_i T_i) for t<=i<n; the observer is reset to the AC root at the start t of each queried window. Then for **each** of six components,

    J[t,n] = CONTR(EMBED_AC_ROOT(v_t), M[t,n]) / D_n,
    D_n = d0 * PRODUCT_{0<=i<n}(b_i).

D_n is independent of the cut t when n is fixed. The observed jet J[t,n] can depend on t because motif counting begins anew at that cut. For a sliding window L=n-t, the window product's denominator obeys the exact integer identity

    Dwindow(t+1,L) = Dwindow(t,L) * b_(t+L) / b_t,

and the whole prefix-plus-window denominator obeys D_(n+1)=D_n*b_n.

Proof: By native state recursion v_t=d0*(PRODUCT_{i<t}b_i)*r_t. By repeated bilinearity of the six-jet ordered product, M[t,n]=(PRODUCT_{t<=i<n}b_i)*(T_t ⋆ ... ⋆ T_(n-1)). If X=(z,u,v,uu,uv,vv) and Y=(Z,x,y,xx,xy,yy), the exact product is

    X ⋆ Y = (zZ, uZ+zx, vZ+zy, uuZ+2ux+zxx,
             uvZ+uy+vx+zxy, vvZ+2vy+zyy).

Multiplying the integer prefix and window scalar factors gives D_n; the jet contraction sums exactly the same original labelled paths. The AC state is carried across every action *within* the suffix, preserving all overlaps. Both identities for the denominator follow by cancellation in finite products of positive integers. This establishes the formula for arbitrary finite gate sequences, including zeros.

For this frozen four-point probe the integer initial state has five positive port coordinates equal to 5 with d0=4. Each source port has at most six labelled exits and each motif count is at most L. With M_i=max(a_i,b_i), any final scalar integer jet numerator is bounded by 25*6^n*(PRODUCT_i M_i)*max(1,L^2). Thus the numerator has O(n+SUM log2(M_i)+log max(1,L)) bits and D_n has O(SUM log2 b_i) bits. This is an exact magnitude bound, not a claim about machine-word runtime.

## Executed evidence

The full local source `PREFIX641_native_rolling_pipeline.py` and `PREFIX641_cut_denominator_certificate.py` use only the original labelled native BRC transitions and Python's exact integer/Fraction arithmetic. Thirty-six pretest (gate-family, L, W) configurations matched the original-action DP for all six components. An independent certificate checked **60** prefix cuts (3 gate families × 5 cuts × 4 lengths), verifying the raw denominator formula and all six moments against the original-action oracle. All assertions passed. Performance comparison checked 13 workloads, each with the same time-gate sequence, native prefix-state update, queue build and rebalance, complete vector contraction, and final exact tuple. The 31 timing records represent 5 workloads with 3 algorithms and 8 with 2 algorithms; every observed six-component output matched. Each duration is one local Python run in seconds, not a controlled distribution.

| gate | L | W | integer queue | Fraction queue | original native DP |
|---|---:|---:|---:|---:|---:|
| unit | 4 | 12 | .2003 | 3.0170 | .0819 |
| rational | 4 | 12 | .1961 | 2.9802 | .0809 |
| periodic zero | 4 | 12 | .1933 | 2.9748 | .0873 |
| unit | 8 | 16 | .4137 | 5.3775 | .2346 |
| rational | 8 | 16 | .4248 | 5.5037 | .2394 |
| unit | 16 | 12 | .4353 | — | .3740 |
| rational | 16 | 12 | .5233 | — | .3800 |
| unit | 32 | 16 | .9816 | — | 1.0661 |
| rational | 32 | 16 | 1.0237 | — | 1.0294 |
| unit | 64 | 64 | 2.5117 | — | 8.1845 |
| rational | 64 | 64 | 2.6817 | — | 9.0788 |
| unit | 128 | 32 | 3.7216 | — | 8.5139 |
| rational | 128 | 32 | 3.8637 | — | 9.2386 |

In the two L=64, W=64 workloads the measured direct-DP/integers speed ratios are 3.26x and 3.39x; at L=128, W=32 they are 2.29x and 2.39x. At L=4..8 the integer queue is 12.96x–15.39x faster than the original Fraction rolling-queue implementation, while direct DP remains faster in those short regimes. The first tested integer>DP region is the unit L32/W16 case, and this is an empirical workload-specific boundary.

With fixed original 672 port×AC states, the PREFIX-638/639 support certificate bounds the full matrix by 4284 live positions and each ordered matrix composition by 10500 candidate pair joins. A two-stack queue requires O(L+W) field operations and O(W) source-port updates/vector contractions for L initialized steps and W windows, with the stated growing integer bit costs. The exact moment observer is a provenance-preserving labelled transition **during evaluation**, but the six output moments do not themselves identify every original path; individual path enumeration uses the earlier source-preserving DAG.

**Verification scope:** The experiment times the full *query stage from initial native port propagation*, not the separate endpoint-48-phase inversion/16-dimensional reverse recovery. A different time profile or input distribution can move the crossover. The scientific theorem is a direct algebraic derivation in the declared original BRC model; independent Driver review is pending.

## Reproduction and provenance

Run in one directory containing the PREFIX-638 original `PREFIX638/PREFIX638_native_jet_support.py` and PREFIX-640 `PREFIX640_fraction_free_rolling_jet.py`:

    python PREFIX641_cut_denominator_certificate.py
    python PREFIX641_native_rolling_pipeline.py

Both programs were executed. Local full reproducibility bundle: `ENTERPRISE_MATH_PREFIX641_NATIVE_END_TO_END_COMPLETE.tar.gz` (includes all scripts, all raw results, proof and dependency SHA256 manifest), made available in the originating ChatGPT run. Exact SHA256s of executed source, JSON and dependencies appear in that manifest. Reuse the verified original BRC source; do not replace it with a classical propagator.

Next discriminating unit: determine whether end-to-end six-moment readouts admit a factorized contraction whose stored structures are smaller than the 672×672 bounded-support product, and assess repeated-run memory/bit-arithmetic tradeoffs over growing L/W. This research is a local native BRC path-query improvement; the formal task's arbitrary-triad signed-C6 and physical Cell rotation remains the open mother question.

**Session/control observation:** Current native task snapshot at 2026-11-10 02:47 UTC returned HANDOFF_READY/NEEDS_DISPATCH and owner taskbook/unassigned. Own native session start subsequently returned BACKEND_IDENTITY_CHECK_UNAVAILABLE; no authentic new Researcher-ID, Research-Activity-ID, CLAIM or native checkpoint is asserted. GitHub author's account login is not presented as an MCP-issued research identity.
