# R762FF — Actual high-precision return test: the sharp generic 251-scalar *vanishing* criterion is too strong at h=7 and h=8

Date: 2026-11-19 (Asia/Shanghai). Scientific scope: positive six-labelled q=9 three-coordinate BRC only. The immutable scientific taskbook and P000 are inherited from R762FE. This is an exact finite observation; no claim is made about signed native \`TRIADIC_CLOSURE_E\`.

## Discriminating question

R762FE proves a **sufficient**, not necessary, 251-return period certificate with a sharp universal +57-trit reconstruction surcharge. Does that raw componentwise-zero test actually certify the already-established author's periods at the previously reported earliest indices, or is the universal precision margin too conservative for those special differences?

Set \(P=1+X+Z+XY+YZ+XYZ\), \(a_n=[0]P^n\), \(f(n)=\max(0,\lfloor n/3\rfloor-2)\). For each \((h,L,N)\), define
\[
b=L/3,\quad d(s)=a_{s+L}-3^b a_s,\quad
E_{\rm base}(s)=f(s)+b+h,\quad
E_{\rm strict}(s)=f(\min(s,N+125))+b+h+57.
\]
Inspect all **251** return differences at \(s=N,\ldots,N+250\), each modulo \(3^{f(N+125)+b+h+57}\), retaining original six-branch BRC transitions and all 729 terminal coordinates in the engine.

## Exact results

| Precision h | Claimed period L | Reported earliest N | Largest modulus \(3^p\) | Baseline \(v_3(d)\ge E_{\rm base}\) | Strict \(v_3(d)\ge E_{\rm strict}\) |
|---|---:|---:|---:|---:|---:|
| 7 | 13,122 | 26 | p=4,486 | 251 / 251 | **0 / 251** |
| 8 | 39,366 | 27 | p=13,235 | 251 / 251 | **0 / 251** |

The exact histogram of the baseline excess \(v_3(d(s))-E_{\rm base}(s)\) is:
- h=7: \(\{0:168,1:37,2:30,3:13,4:2,5:1\}\).
- h=8: \(\{0:168,1:38,2:29,3:13,4:2,5:1\}\).

Smallest strict margin is -57 trits in both cases; every scalar fails the strict test.

**Direct counterexamples to raw-certificate applicability.**
At h=7, s=26, \(v_3(d(26))=4389\), while the strict threshold is 4444 (baseline 4387).
At h=8, s=27, \(v_3(d(27))=13139\), while the strict threshold is 13194 (baseline 13137).
The actual 251-scalar sufficiency criterion is not satisfied at either \(N\). Its proof remains valid; these computations show that applying a *universal worst-case precision penalty separately to every scalar* misses these structured period differences.

## Reproducibility

Compile \`R762FF_Q9_H7_H8_251_RAW_CERT_TEST.cpp\` with \`g++ -O3 -std=c++17 -lgmpxx -lgmp\`, run arguments \`7\` and \`8\`. The code performs exact GMP arithmetic on the full 729-coordinate BRC convolution, reducing modulo \(3^p\) every 12 steps, saves the 251 early and late return moments, and computes exact valuations of the differences modulo \(3^p\). Because any failed strict threshold is below \(p\), each failure is certified unambiguously. Complete histograms are in the accompanying JSON. Actual observed local wall times were approximately 3.4s (h7) and 31.4s (h8); workload and machine-specific performance are not inferred from this alone.

## Interpretation and next experiment

R762FE's 57-trit loss is exact for *arbitrary integral linear combinations* of the 126 basis states. Specific normalized period differences may have correlated return moments; they can reconstruct to zero even when not every individual moment has the worst-case extra divisibility. The useful next construction is a **matrix-level 3-adic reconstruction test** using the whole vector \(d(N+i),\ldots,d(N+i+125)\) and the precomputed matrix \(3^{57}B^+(H^+)^{-1}\), checking joint cancellation rather than raw per-scalar vanishing. Evaluate its full preprocessing, precision, cost and output recovery before claiming a practical speed advantage.

Scientific status: author-side exact finite computation / two target instances / NOT_REVIEWED. The earlier R762FA complete terminal-period certificates are separate prior author-side evidence, not revalidated by this diagnostic.
