# R5 — Primitive ninth-root residual: all positive thresholds and sharp cost modulus 2520

Date: 2026-11-21. Status: AUTHOR_EXACT_DERIVATION / EXACT_FINITE_CHECKED / NOT_REVIEWED. This is independent frozen-model portable research, without formal TASK CLAIM/RUN/Result/Review. Original R5 scientific-input SHA-256: \`50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b\`.

## Sources and model

Frozen R5 scalar nonadaptive model: 256 labeled hypotheses, integer prices 214–314, and five minimal separation subsets:

\[
S_0=[214,218],\quad S_1=\{214,216,217,218,219,220,221\},\quad
S_2=[215,221],\quad S_3=[223,290],\quad S_4=[296,312].
\]

For a fixed positive integer m the failure count F_m(N) enumerates nonnegative vectors of multiplicities of the 101 prices with sum of priced multiplicities N, when at least one subset has total multiplicity strictly less than m. Reuse previously verified primitive-7 universal result [R5 seventh](https://github.com/awdawmip/enterprise-math/blob/1482e3a06ae5c2e6a8e18120d3aca48f95645c75/research_notes/portable_direct/r5_seventh_allm_20261121/RESEARCH.md) and [R5 eighth](https://github.com/awdawmip/enterprise-math/blob/10ed02f4ab565aa511c3829fdfbf6130c2b5cb87/research_notes/portable_direct/r5_octic_allm_carrier840_20261121/RESEARCH.md). Retain unchanged frozen inputs and their provenance.

## Theorem A: nonzero primitive ninth-root contribution for every fixed positive m

Let z be any primitive ninth root, \(\Phi_9(z)=z^6+z^3+1=0\). Define the positive integer \(P_9=\prod_{j=0}^{9}(225+9j)\) and the invertible cyclotomic coefficient

\[
H_9(z)=\prod_{\substack{222\le p\le314\\9\nmid p}}(1-z^p)^{-1}.
\]

The normalized leading coefficient \(L_m(z)\) is specified exactly by

\[
\boxed{\sum_{m\ge1}L_m(z)t^{m-1}=
\frac{\sum_{j=3}^{5}c_j(z)\mathcal F(z^7,z^8,z^j;t)}
{(1-t)^2(1-zt)(1-z^2t)}}\tag{1}
\]
where \(c_j(z)=\prod_{\ell\in\{3,4,5\}\setminus\{j\}}(1-z^{\ell-j})^{-1}\) and

\[
\mathcal F(X,Y,Z;t)=\frac{1+(1-t)\left[
\frac{X}{1-X}+\frac{Y}{1-Y}+\frac{Z}{1-Z}
-\frac{tXY}{1-tXY}-\frac{tXZ}{1-tXZ}-\frac{tYZ}{1-tYZ}
+\frac{t^2XYZ}{1-t^2XYZ}\right]}{(1-Xt)(1-Yt)(1-Zt)}.\tag{2}
\]

For every fixed \(m\ge1\), \(L_m(z)\ne0\). The primitive ninth-root poles of the full cost-generating function are **of exact order ten**, with leading Laurent coefficient \(H_9(z)L_m(z)/P_9\) at \((1-x/z)^{-10}\). Therefore their combined Fourier contribution is

\[
\boxed{F_m^{(9)}(N)=\frac{N^9}{9!P_9}\sum_{\Phi_9(z)=0}
H_9(z)L_m(z)z^{-N}+O_m(N^8).}\tag{3}
\]

For example the exact coefficient at m=1 is

\[
L_1(z)=(-1-3z-4z^2+z^3-2z^4)/3.
\]

### Why only these local prices matter

The ten prices 225,234,...,306 are all multiples of nine strictly above the eight local prices 214–221. Every event among S_0,S_1,S_2 constrains price 216, the only multiple of nine in the local block. The other ten multiples remain free for all the seven inclusion–exclusion terms based only on S_0,S_1,S_2, giving possible order-10 poles. Adding S_3 constrains 225,234,...,288, leaving two such prices free; adding S_4 constrains 297,306, leaving eight. Hence no intersection containing S_3 or S_4 affects the order-10 coefficient.

For the local block let a=n_214, b=n_215, v=n_216+n_217+n_218, u=n_219+n_220+n_221. The three failure loads are v+a+b, v+a+u, v+b+u, and their minimum is v+a+b+u-max(a,b,u). Summing the indicator min_load < m over all m>=1 contributes t^min_load/(1-t). The v group and threshold generate \((1-t)^{-2}(1-zt)^{-1}(1-z^2t)^{-1}\). The u-group decomposes as \(\sum_{j=3}^5c_j(z)/(1-z^j w)\) and a sum over the maximum of the triples (a,b,u) yields \(\mathcal F\) in (2). Factors for other nonmultiples produce H_9, and ten free nine-multiples supply P_9^{-1}. These are rational identities in the exact cyclotomic field, with no floating-point limiting assumption.

## Theorem B: threshold quasi-period exactly 18 and uniform nonvanishing

All poles of the rational function in (1) are eighteenth roots of unity, of order at most two. Its denominator divides \((1-t^{18})^2\), and the function is strictly proper. Therefore

\[
\boxed{L_{m+36}-2L_{m+18}+L_m=0 \quad (m\ge1),\qquad L_{r+18k}=C_r+kB_r\quad (1\le r\le18).}\tag{4}
\]

At a primitive eighteenth root t satisfying \(t^2=z^{-1}\), only the j=4 triple-product factor \(1-z t^2\) is singular. Its coefficient \(c_4(z)(1-t)\) is nonzero and every remaining denominator is invertible there. This irreducible primitive-18 pole proves that the threshold quasipolynomial has **least period exactly 18** (not merely a period dividing 18).

An exact nonvanishing certificate is as follows. In the canonical \(\mathbb Q\)-basis \(1,z,z^2,z^3,z^4,z^5\), each listed coefficient of \(L_{r+18k}\) is \(c+bk\), with c,b nonzero of the same sign; hence the coefficient cannot vanish at any k>=0 and neither can \(L_m\).

| r | basis power | c | b |
|---:|---:|---:|---:|
|1|0|-1/3|-2|
|2|1|-1|-3|
|3|0|16/3|8|
|4|0|22/3|10|
|5|0|8|12|
|6|0|5|5|
|7|0|1|1|
|8|2|4|3|
|9|0|-3|-4|
|10|0|-7/3|-2|
|11|0|-10/3|-3|
|12|0|22/3|8|
|13|0|28/3|10|
|14|0|12|12|
|15|0|5|5|
|16|0|1|1|
|17|2|3|3|
|18|0|-4|-4|

## Theorem C: least cost modulus at remainder O_m(N^9) is 2520

The pinned eighth-root result gives least modulus 840 at remainder \(O_m(N^{10})\). At the next finer precision all primitive ninth roots contribute nontrivially at degree nine by (3). All primitive tenth-root contributions are already represented by cost period 10, a divisor of 840. Any root of order d>=11 has at most nine prices divisible by d in the frozen price range, hence its pole order is at most nine and its Fourier terms are at most \(O_m(N^8)\). Accordingly, for every fixed \(m\ge1\)

\[
\boxed{F_m(N)=Q_{m,2520}(N)+O_m(N^8),
\qquad \operatorname{least\ positive\ cost\ period}=2520=\mathrm{lcm}(840,9).}\tag{5}
\]

Equivalently the approximation with remainder \(O_m(N^9)\) retains the earlier minimum 840, while retaining the next order with remainder \(O_m(N^8)\) forces 2520. The cost-period claim is a least quasi-polynomial period at this precision, not a statement that the exact count function has period 2520.

## Verification and scope

Run \`python3 VERIFY_NONIC.py\` with standard-library Python. The script computes the exact series (1) in \(\mathbb Q[z]/(z^6+z^3+1)\) without floating point, checks 36 initial coefficients, verifies 64 recurrence instances, independently recomputes local inclusion–exclusion for m=1..12 via bounded DP, and checks the eighteen all-threshold sign witnesses. \`NONIC_RESULT.json\` stores the exact initial vectors and witness data. The global conclusions rely on the rational generating-function identity and denominator/pole analysis, rather than finite extrapolation. Neither independent scientific review nor formal mathematical admission has been performed.

The Fourier-phase carrier is an exact scalar observer for the pinned R5 cost-counting experiment. Transferring it to a native X6/BRC interpretation would require a new typed observer and future-operation preservation certificate under P000; no such transfer is asserted here.

Next: study primitive eleventh and higher roots at degrees N^8 and below, identify the next new prime-power factor in the least cost modulus, and seek a general closed law for the precision-to-modulus staircase.
