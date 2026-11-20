# R284CB — Superincreasing Port cofactors give a four-threshold greedy top-row inverse

Date: 2026-11-20 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED.
Independent portable finite algebra, continuing R284CA and retaining its frozen R284BZ science. No new P000, native X6, BRC, CLAIM, Result, Review or Task authority is claimed.

## Exact fixed input and theorem

For \(C\in\{1,2\}^{4\times4}\), use precisely the existing frozen observation
\[
F_C=\det(\operatorname{diag}(d_0,6,13,d_3)-C-z_1E_{01}-z_2E_{02}-z_3E_{03})\pmod p,
\]
\[
p=17179869143,\qquad(d_0,d_3,z_1,z_2,z_3)=(1120832,1651128,390139,394465,1497639).
\]
For a lower-three-row block \(L\in\{1,2\}^{12}\), set \(C_{0j}=1+e_j\), \(e_j\in\{0,1\}\). As in R284CA, the determinant is
\[
F_C\equiv\beta_L-\sum_{j=0}^3e_jk_j(L)\pmod p,
\]
where the four integer signed-cofactor weights are positive. The new result is a *uniform superincreasing inequality*:
\[
\boxed{k_j-\sum_{i>j}k_i\ge59\quad(j=0,1,2,3).}
\]
All 4,096 lower blocks have been exhaustively checked. The exact minimum margins in order are 3,301,944; 1,650,972; 8,255,510; 59, and maxima are 66,044,964; 33,022,482; 23,115,701; 196.

Consequently, with the same fixed 34-bit code, **each candidate lower block permits direct top-row reconstruction by four scalar thresholds**. Combined with R284CA's lossless 4,096-base circular index and its certified maximum 128 lower blocks intersecting any query, full decoding requires at most 128 lower-block cofactor reconstructions, 512 bit-threshold tests, and 128 final residual tests. The prior method enumerated up to 2,048 full upper-row candidates. The index size and mathematical noise guarantee are unchanged; this is an arithmetic-count improvement, not a CPU-time benchmark.

## Algebraic proof for all lower blocks

Write
\[
L=(u_1,a_{11},x,y_0,u_2,w,a_{22},z,u_3,g,h,r),
\quad t=6-a_{11}\in\{4,5\},\quad s=13-a_{22}\in\{11,12\}.
\]
Every other entry belongs to \(\{1,2\}\). Following R284CA, define
\[
U=ts-xw,\quad p_1=su_1+xu_2,\quad p_2=tu_2+wu_1,
\]
\[
V=-rU-z(th+xg)-y_0(wh+sg),
\]
\[
q_1=-rp_1-u_1zh+xzu_3+y_0(u_2h+su_3),
\]
\[
q_2=-rp_2+tzu_3+u_1zg+y_0(wu_3-u_2g),\quad
q_3=Uu_3+p_1g+p_2h.
\]
Exact first-row cofactors are \(k_0=Ud_3+V\), \(k_1=p_1d_3+q_1\), \(k_2=p_2d_3+q_2\), \(k_3=q_3\), \(d_3=1651128\).

From the entry bounds:
\[
40\le U\le59,\quad 5\le p_2\le14,\quad
|V|\le202,\quad |q_1|\le128,\quad |q_2|\le64,\quad 0<q_3\le202.
\]
Monotonicity over the discrete input range gives
\[
U-p_1-p_2=ts-xw-(s+w)u_1-(t+x)u_2\ge2
\]
(the minimum occurs at \(t,s,x,w,u_1,u_2=4,11,2,2,2,2\)), and
\[
p_1-p_2=(s-w)u_1-(t-x)u_2\ge9-8=1.
\]
Therefore
\[
\begin{aligned}
k_0-k_1-k_2-k_3&\ge2d_3-(202+128+64+202)=3301660>59,\\
k_1-k_2-k_3&\ge d_3-(128+64+202)=1650734>59,\\
k_2-k_3&\ge5d_3-(64+202)=8255374>59.
\end{aligned}
\]
Also \(k_3=Uu_3+p_1g+p_2h\ge U+p_1+p_2\ge59\). For \(xw=4\), \(U\ge40,p_1\ge13,p_2\ge6\); otherwise \(xw\le2\), \(U\ge42,p_1\ge12,p_2\ge5\). This proves all four inequalities directly, without relying on enumeration. Enumeration refines the displayed lower bounds to the exact margins given above.

## Exact greedy decoder and adversarial real-error proof

For each candidate lower block let \(S_L=\sum_jk_j\). Take the unique real lift \(\delta\equiv\beta_L-y\pmod p\) lying in \([-29.5,S_L+29.5]\), if one exists; \(S_L+59<p\) makes it unique. A correct lower block always has this lift under \(|\epsilon|<29.5\).

Starting with \(r_0=\delta\), for \(j=0,1,2,3\) let \(s_j=\sum_{i>j}k_i\) and compute
\[
\boxed{e_j=\mathbf1\{2r_j>k_j+s_j\},\qquad r_{j+1}=r_j-e_jk_j.}
\]
If the true bit is zero, its residual belongs to \([-\rho,s_j+\rho]\); if one, to \([k_j-\rho,k_j+s_j+\rho]\). Since \(k_j-s_j\ge59>2\rho\), the midpoint threshold always selects the true bit. A final check \(|r_4|<29.5\) accepts the correct block. Any other block passing this check would give a different full codeword less than 29.5 from the same observation, contrary to the predecessor's complete global minimum circular distance 59. For any valid noisy observation there is therefore exactly one output. The proof applies to every real circular noise value with \(\rho<29.5\).

## Reproduction and provenance

The companion standard-library Python checker exhaustively verifies all 4,096 lower-block margin tuples and 65,536 full codewords; the circular minimum gap is 59 with 64 attaining gaps. It matches the R284CA checksum
b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4
and runs 196,608 correct-block greedy checks at integer errors -29,0,+29 and 2,505 complete grouped-index checks including exact rational errors ±29.25. Sampling validates implementation; the preceding inequalities certify the all-real guarantee. Run: python research_notes/portable_direct/R284CB_greedy_row_decoder_checker.py.

Frozen precursor: research_notes/portable_direct/R284CA_4096_BLOCK_SHARP_NOISE_DECODER_20261120.md, read from enterprise-math@09808fb3fbcd2580231bba693b2c857cb3aa1de4 (Git blob 88d453ccc7a43c70e3e109ff50ae8c3f8c7e8e06). Historical contributor lineage EM-DIRECT-E6B1DD; current native session identity, Activity association and formal CLAIM remain separate. Independent review: NOT_REVIEWED.

Next open problem: eliminate the remaining circular base-index search of up to 128 lower blocks by an exact modular inversion, or attain the same gap 59 with a 33-bit-or-smaller modulus at the frozen double-leaf controls. Any speed claim must benchmark preprocessing, index memory, cofactor reconstruction, and query latency.