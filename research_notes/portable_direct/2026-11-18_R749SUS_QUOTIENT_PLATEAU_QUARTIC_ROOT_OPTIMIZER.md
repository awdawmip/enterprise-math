# R749SUS — Exact quotient-plateau optimizer for named two-Port feedback

Date: 2026-11-18 (Asia/Shanghai). Evidence: \`AUTHOR_EXACT_NOT_REVIEWED\`. Domain: auxiliary positive-rational WBRC-T30–T32 named two-Port integer observer, not an asserted native X6 event.

## Frozen input, precedence and provenance

- Scientific input remains exactly \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md\`.
- R749SUO \`161123938bc7836d62d130a755b3d6601a743182\`: author-proved global optimum \`Q=+1\` for all \`M>=116\`, closest-factor inversion. It relies on the independently unreviewed R749SUN analytical argument and the earlier saved finite exact certificate; no independent mathematical admission is asserted here.
- R749SUR \`119963d34b4265e35ff6bec9bfe68eaead14d949\`: certified exact smaller-factor cutoff \`x_min\` and \`O(M^(3/8))\` factor scan for \`M>=9999\`. This note refines that scan, not its scientific pins.
- The original six-axis P000, three-force closure, provenance-fidelity and separately typed causal time are retained. A two-index integer matrix remains an auxiliary observation, not a primitive two-force configuration or a native two-dimensional plane.

## Main theorem

For every integer \`M>=9999\`, let
\[
\mathcal U_M^\circ=\{(a,u,v,d)\in\{1,\dots,M\}^4:ad-uv=1,\ Q=u+v-a-d\ne0\},
\quad \tau=\max(u,v)ad .
\]
Assuming the cited R749SUO classification and cutoff lemmas with their original hypotheses, a deterministic exact algorithm computes the maximum \(\tau\), **every** maximizing named tuple (including ties), in
\[
\boxed{O(M^{1/4})\text{ integer arithmetic operations},\qquad O(1)\text{ auxiliary integer words}}
\]
excluding streamed output. Integer square root is counted as one arithmetic operation, as in R749SUR; operand lengths are \(O(\log M)\) bits and an ordinary bit-cost bound multiplies the arithmetic count by the cost of exact division, multiplication and integer square root.

## Plateau reduction (new proof)

Orient \`u=max(u,v)\`. From \`Q=+1\`, R749SUO yields unique factors
\[
x=u-a\ge2,\quad y=u-d\ge x,\quad n=xy=u+1\le B=M+1,
\]
and the reconstructed tuple
\[
(a,u,v,d)=(n-x-1,\ n-1,\ n-x-y,\ n-y-1).
\]
Its score is
\[
T(n,s)=(n-1)\big((n-1)^2-(n-1)s+n\big),\quad s=x+y.
\]
At fixed \(s\) and for \(n\ge s+1\), \(\partial T/\partial n=3(n-1)^2-2(n-1)s+2n-1>0\).

Write \(t=\lfloor\sqrt B\rfloor\), \(k=B-t^2\in[0,2t]\), and \(x=t-h\), where \(0\le h\le H:=t-x_{\min}\), with \`x_min\` the exact R749SUR quadratic cutoff. The best larger factor at fixed x is \(\lfloor B/x\rfloor\). The exact identity
\[
\boxed{\left\lfloor B/(t-h)\right\rfloor=t+h+j(h),\qquad
j(h)=\left\lfloor\frac{k+h^2}{t-h}\right\rfloor}
\]
gives
\[
s=2t+j(h),\quad n=B-r,\quad
r=k+h^2-j(h)(t-h).
\]
The integer \(j(h)\) is nondecreasing. **Within a fixed plateau \(j(h)=j\), the sum \(s=2t+j\) is constant and \(r=h^2+jh+k-jt\) is strictly increasing with h.** Consequently, the *first* integer h of each nonempty plateau is its unique score maximizer (when feasible). No later h on that plateau can be a global maximizer; this is strict and retains all cross-plateau ties.

Let \(j_0=\lfloor k/t\rfloor\), \(j_{\max}=\lfloor(k+H^2)/(t-H)\rfloor\). For each integer j from \(j_0\) through \(j_{\max}\), locate the first h with
\[
h^2+jh+k-jt\ge0.
\]
For \(j=j_0\) this is h=0. For larger j, set \(D=j^2+4(jt-k)>0\), and
\[
h=\max\{0,\lfloor(\lfloor\sqrt D\rfloor-j)/2\rfloor\},
\]
then increment by one if the quadratic is still negative. This is the exact least nonnegative h by monotonicity, including perfect-square discriminants. Discard \`h>H\` or \`j(h)!=j\` (skipped plateau); otherwise evaluate that one tuple if \`n-x-y>=1\`. Retain all j attaining the greatest score, then independently swap x/y (diagonal labels) and u/v (Port labels); a square factor pair gives two named configurations, an unequal pair gives four.

## Uniform operation count

R749SUR proves \(H=O(M^{3/8})=O(t^{3/4})\) as \(M\to\infty\). Since \(k\le2t\) and \(t-H\sim t\),
\[
j_{\max}\le\frac{2t+H^2}{t-H}=O(1+t^{1/2})=O(M^{1/4}).
\]
The near-product witness search takes \(O(M^{1/4})\) increments, cutoff binary search \(O(\log M)\), and each j uses one integer square root, a bounded number of exact integer operations and one score evaluation. All stored scalars are \(O(\log M)\)-bit integers. Thus total \(O(M^{1/4})\) arithmetic operations and \(O(1)\) auxiliary words excluding output. The reduction is exact even when j skips values or optimal plateaus tie.

## Reproducibility and empirical scope

The companion \`R749SUS_QUOTIENT_PLATEAU_OPTIMIZER_CERT.py\` runs with Python standard library only; it uses exact integers throughout and emits \`R749SUS_QUOTIENT_PLATEAU_RESULTS.json\`. The local executable returned \`PASS\`: 15,002 complete independent all-x comparisons for each \`9999<=M<=25000\`, seven additional all-x comparisons through \`M=10^12\`, and three larger single-algorithm exact runs up to \`M=10^18\` (not full-oracle comparisons). Max plateau evaluations in the contiguous window: 51, versus at most 78 old cutoff x positions. For \`M=10^12\`, 3,004 plateau evaluations versus 53,328 old positions. The general theorem is the proof above, conditional on the explicitly cited earlier author theorem, not inferred from these finite runs.

## Next scientific questions

1. Obtain output-sensitive subquartic algorithms or an exact adversarial family for plateau count, with full bit-cost and output reconstruction accounting.
2. Classify the exact maximum gap \(B-n^*\) and the maximizing plateau offset j, including cross-plateau ties.
3. Independently review the load-bearing global \`Q=+1\` theorem and certify a source-pinned, provenance-preserving native X6 three-force Cell/Link/Port event bridge with resource and causal-time permissions before transferring auxiliary conclusions.

Research provenance: R2 independent portable line. Historic \`EM-DIRECT-44C346\`/\`RA-A16A5E663104EBDBA287C665\` are provenance, not a newly authenticated session, current shared CLAIM or formal Result.
