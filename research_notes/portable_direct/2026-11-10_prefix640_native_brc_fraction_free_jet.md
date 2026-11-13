# PREFIX-640 — Exact fraction-free second-moment transfer for frozen native BRC

Date: 2026-11-10 Asia/Shanghai. Status: AUTHOR_SIDE_RESEARCH / UNREVIEWED.
Scientific pin: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d` (unchanged).
Scope: original 48 STAR phases, 96 labelled ports, 576 labelled actions, two-pattern Aho–Corasick observer `P0=(485,316,52,174)`, `P1=(52,174)`; six-component jet `(Z,U0,U1,V00,V01,V11)`.
Parent task: `RS-X6-NATIVE-ROTATION-DYNAMICS`, author-side work without a formal CLAIM.

## Main result

Let a length-`L` native weighted BRC action sequence use nonnegative rational gates `g_i=a_i/b_i` (`a_i>=0`, `b_i>=1` integers). Each labelled one-step transfer `T_i` has zero, ungated unit, or gated `g_i` edge weights, and carries the ordered native action label into the same Aho–Corasick observer.

For each step define an integer transfer `N_i=b_i T_i` by replacing each original ungated unit edge weight by `b_i` and gated edge weight by `a_i` (zero edges stay zero). Then the original ordered jet transfer is **exactly**
[
T_1\star\cdots\star T_L
=\frac{N_1\star\cdots\star N_L}{\prod_{i=1}^L b_i}.
]
This is an entrywise identity of all six jets and holds for overlapping pattern hits and zero gates.

For an original path with mass `w` and occurrence counts `(c0,c1)`, its jet is `J(w,c) = w(1,c0,c1,c0^2,c0*c1,c1^2)`. The ordered jet multiplication law is bilinear: with `(z,u,v,uu,uv,vv)` and `(Z,x,y,xx,xy,yy)`,
```
(zZ, uZ+zx, vZ+zy, uuZ+2ux+zxx, uvZ+uy+vx+zxy, vvZ+2vy+zyy).
```
The Aho–Corasick state is kept across the transfer boundary, so cross-boundary matches are counted upon consuming their last original action. Since each one-step numerator is `b_i` times the original transfer, bilinearity gives the displayed common-denominator identity by induction. All intermediate sparse products therefore use integer arithmetic; exact division occurs only when the caller requests a rational value.

With at most six original labelled exits per port and `M_i=max(a_i,b_i)`, each nonnegative numerator coefficient is at most `6^L (prod_i M_i) max(1,L^2)`, because there are no more than `6^L` action paths per starting port, individual numerator masses are at most `prod_i M_i`, and motif counts are at most `L`. Numerator magnitude therefore has at most `1+ceil(L log2 6 + sum_i log2 M_i + 2 log2 max(1,L))` bits, and the common denominator at most `1+sum_i log2 b_i` bits. The prior frozen two-pattern support-join bound is at most 10,500 candidate pairs per merge; integer jet composition retains linear arithmetic operation count over fixed-support consecutive blocks, with exact-bit costs depending on the bound above.

## Executed evidence and scope

The attached complete machine-readable archive contains the **full original 7.8 KB paper**, the **actual executed 9.1 KB Python source**, and the **complete 3.6 KB JSON results**. The local full reproduction archive also includes the exact PREFIX-638 original native action/jet dependency and the run log.

The test program compares all six sparse-jet components with an independent `Fraction` implementation of the original labelled BRC action operators, including four gate regimes (unit, positive rational, periodic zero, all-zero), rolling-window query comparisons, and an independently propagated 96-port zeroth moment at large lengths. **36 exact checks passed**, plus five long-case original-port comparisons (all-one lengths 64, 256, 1024; rational lengths 64,256). The L=1024 all-one intermediate numerator had at most 1,034 bits. Largest measured sparse support was 4,284 positions, consistent with PREFIX-638.

Four *single-run local sequential sparse product* timing comparisons: all-one L=4: 0.480173s vs 0.032891s; all-one L=8: 1.075282s vs 0.075353s; positive rational L=4: 0.504709s vs 0.034649s; positive rational L=8: 1.190492s vs 0.076703s. Speedup here is approximately 14.27–15.52x **for this tested kernel only**. Full end-to-end rolling-window throughput remains the next independent benchmarking question.

## Reproduction and retained provenance

The companion `PREFIX640_complete_paper_code_results.tar.gz.b64` is a base64-encoded GZIP TAR containing `2026-11-10_prefix640_native_brc_fraction_free_jet.md`, `PREFIX640_fraction_free_rolling_jet.py` and `PREFIX640_fraction_free_results.json`. Decode with:
```sh
base64 -d PREFIX640_complete_paper_code_results.tar.gz.b64 | tar xzf -
```
Then supply the frozen `PREFIX638/PREFIX638_native_jet_support.py` from the original PREFIX-638 archive and run `python PREFIX640_fraction_free_rolling_jet.py`. The dependency file's SHA256 is `48d6521bab630f7f2d9de8ac7158ff074ff448267c1893a0dd064e4335c264f1`. The complete local archive with dependency is `ENTERPRISE_MATH_PREFIX640_FRACTION_FREE_JET_COMPLETE.tar.gz` distributed in the conversation.

Verified original local source SHA256: `c07317e5e81cf1866f3386a43d902cec8a669d50f9782e8f63985e9248363ab4`; results SHA256: `fb47b162d17719ce1b37ecbf6e9f0e1fddffd8d88187bb305f013b64c2339f3d`; full original manuscript SHA256: `73ed3cab3e5d38bbbec6fbfba8fc95e1f4eac849e755f46a242565197044be6d`.

Next: benchmark complete rolling-query workload including transfer construction, queue rebalancing, exact vector output and bit cost vs the original Fraction queue and direct native-action DP. This restricted kernel result does not close the parent task's physical rotation dynamics / arbitrary-triad signed C6 objective. P000 unchanged, review pending.
