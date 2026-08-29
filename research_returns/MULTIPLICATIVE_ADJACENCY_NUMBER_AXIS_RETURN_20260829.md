# 乘法相邻与新数轴：相邻半素数/合数的因子编辑几何 — Research Return

Task: `RS-MULTIPLICATIVE-ADJACENCY-NUMBER-AXIS`  
Publication: `TP2-180399AE7989F096D40D`  
Researcher-ID: `EM-MNA1-6B92D4`  
Claim: `chatgpt-mna1-20260829-1316-6b92d4`  
Execution record: `ER-090530731881C8CA560D`

## Terminal verdict

`SUCCESS / ADDITIVE-MULTIPLICATIVE-LOCALITY-SEPARATED / PURE-1D-MULTIPLICATIVE-AXIS-OBSTRUCTED / SEMIPRIME-PREFIX-GRAY-RAY-CONSTRUCTED / BRANCHED-SHELL-GEOMETRY-SURVIVES`

最强结论不是“找到一条能够替代普通整数轴的纯乘法数轴”，而是：

1. 普通加法局部性与素因子编辑局部性存在双向无界失真；
2. 完整 M1/M2 邻接具有本质分支，不能等同于一维全序的相邻图；
3. 半素数 M2 壳存在显式、可计算、素数窗口前缀兼容的 Hamilton–Gray ray，但任何一维主脊直接保留的完整 M2 邻接比例都趋于 0。

因此 surviving object 是

`M1 graded divisibility-cover graph + fixed-Omega M2 replacement shells + optional symmetry-broken Gray spine`.

一般的整除覆盖图、自由交换幺半群指数格、reduced powers 与 multiset Gray code 均按成熟结构处理，不作换名新颖性主张。

---

## 1. 乘法编辑距离的精确恒等式

若 \(g=\gcd(m,n)\)，逐素指数取 \(c_p=\min(v_p(m),v_p(n))\)，则

\[
\boxed{
d_\times(m,n)
=\sum_p|v_p(m)-v_p(n)|
=\Omega(m/g)+\Omega(n/g)
=\Omega(m)+\Omega(n)-2\Omega(g).
}
\]

M1 每一步恰好改变一个素指数单位。先从 \(m\) 删除 \(m/g\) 的 prime tokens 到 \(g\)，再加入 \(n/g\) 的 tokens 到 \(n\)，因此

\[
\boxed{\operatorname{dist}_{M1}(m,n)=d_\times(m,n).}
\]

所以 \(d_\times\) 正是整除覆盖图/素指数正交格的图距离。

## 2. T1 — 固定 Omega 层偶距离：PROVED

若 \(m\ne n\) 且 \(\Omega(m)=\Omega(n)=k\)，则

\[
d_\times(m,n)=2\bigl(k-\Omega(\gcd(m,n))\bigr)\in2\mathbb N_{>0}.
\]

故固定 \(\Omega\) 壳没有 M1 边；特别地，不同半素数永远不是 M1 相邻。

## 3. T2 — 半素数 gcd 分类：PROVED

不同半素数满足

\[
d_\times(m,n)=4-2\Omega(\gcd(m,n)).
\]

因为 \(m\ne n\)，\(\Omega(\gcd(m,n))\) 只能为 0 或 1，所以

\[
\boxed{d_\times=2\iff\Omega(\gcd(m,n))=1,}
\qquad
\boxed{d_\times=4\iff\gcd(m,n)=1.}
\]

平方半素数同样适用，如 \(p^2,pq\) 距离 2，而 \(p^2,q^2\)（\(p\ne q\)）距离 4。

因此“相邻半素数一定乘法不相邻”在 M2 意义下是假的：最小反例 \(4,6\)，且 \(6,9\) 亦然。正确分类是：相邻半素数要么共享一个 prime token（M2 相邻），要么互素（M2 图距离 2）。

进一步，若相邻半素数 \(m<n\) 又 M2 相邻，则必有素数 \(p\) 与相邻素数 \(q<r\) 使

\[
m=pq,\qquad n=pr,\qquad n-m=p(r-q).
\]

否则若 \(q<s<r\) 还有素数 \(s\)，则中间的 \(ps\) 也是半素数，矛盾。

## 4. T3 — 相邻合数不是 M1：PROVED + STRENGTHENED

若 \(a<b\) 是合数集合中的相邻元素，则

\[
\boxed{b-a\in\{1,2\}.}
\]

若间距至少 3，\(a+1,a+2>2\) 是两个连续中间整数，不可能都为素数，故至少一个中间合数，矛盾。

- 若 \(b=a+1\)，则 \(\gcd(a,b)=1\)，二者均合数，所以
  \[
  d_\times(a,b)=\Omega(a)+\Omega(b)\ge4.
  \]
- 若 \(b=a+2\)，中间 \(p=a+1\) 必为奇素数，\(a=p-1,b=p+1\)，且 \(\gcd(a,b)=2\)，故
  \[
  d_\times(a,b)=\Omega((p-1)/2)+\Omega((p+1)/2).
  \]
  距离为 2 要求两个连续 cofactors 都为素数，唯一可能是 \(2,3\)，即 \(p=5\)。

所以

\[
\boxed{d_\times(a,b)=2\iff(a,b)=(4,6),}
\]

间距 1 时总有 \(d_\times\ge4\)，其余相邻合数至少为 3；故相邻合数永远不是 M1 相邻。

## 5. T4 — 加法近而乘法任意远：PROVED BY CRT

任取 \(K\ge2\)，由中国剩余定理取正整数 \(n\) 满足

\[
n\equiv0\pmod{2^K},\qquad n\equiv-1\pmod{3^K}.
\]

则 \(n,n+1\) 均为合数且互素，并有 \(\Omega(n)\ge K,\Omega(n+1)\ge K\)。因此

\[
\boxed{|n-(n+1)|=1,\qquad d_\times(n,n+1)\ge2K.}
\]

## 6. T5 — 乘法近而加法任意远：PROVED

对任意 \(n\ge1\)，

\[
\boxed{d_\times(n,2n)=1,\qquad |2n-n|=n\to\infty.}
\]

T4 与 T5 排除了任一方向的统一大尺度 Lipschitz 控制。两种局部性不是简单坐标重参数化。加权 \(d_{\log\times}\) 也不能消除该分离：CRT 一侧在加法距离 1 时无界，\(n,2n\) 一侧恒为 \(\log2\) 而普通差值无界。

---

## 7. 固定 Omega 的 M2 壳

在固定 \(\Omega=k\) 壳，一次 M2 替换恰好修正两个 \(l_1\) 指数单位，所以

\[
\boxed{
\operatorname{dist}_{M2,k}(m,n)=\frac12d_\times(m,n)
=k-\Omega(\gcd(m,n)).
}
\]

固定前 \(r\) 个素数后，这个图精确是完整图 \(K_r\) 的 reduced \(k\)th power：\(k\) 个不可区分 token 可重复占据同一顶点，每一步移动一个 token。squarefree 子图则是普通 token/Johnson 图。

先验边界：
- Richard H. Hammack & Gregory D. Smith, *Cycle bases of reduced powers of graphs*, Ars Mathematica Contemporanea 12 (2017), 183–203, DOI `10.26493/1855-3974.856.4d2`.
- Frank Ruskey & Carla Savage, *A Gray Code for Combinations of a Multiset*, European Journal of Combinatorics 17 (1996), 493–500, DOI `10.1006/eujc.1996.0043`.

因此一般 reduced-power / multiset minimal-change listing 不是本任务的新颖性来源。

## 8. 半素数 M2 有限壳的精确图结构

令

\[
G_r=\{p_ip_j:1\le i\le j\le r\}
\]

以 M2 为边。则

\[
\boxed{|V(G_r)|=\frac{r(r+1)}2,}
\qquad
\boxed{|E(G_r)|=\frac{r^2(r-1)}2.}
\]

度数：

\[
\deg(p_i^2)=r-1,\qquad
\deg(p_ip_j)=2(r-1)\quad(i\ne j).
\]

且 \(r\ge2\) 时

\[
\boxed{\operatorname{diam}(G_r)=2.}
\]

因此 \(r\ge3\) 时完整 M2 壳已有度数大于 2 的顶点，不可能本身是一条线。

## 9. 一维“纯乘法数轴”的两个 no-go

### 9.1 度数 / Hamilton 阻碍

离散全序的前驱/后继相邻图每点度数至多 2；但 M1 中任意 \(n\) 都与 \(np\)（任意素数 \(p\)）相邻，向上度数无限。

更强地，在最自然有限窗 \(\Omega\le1\) 与 \(r\) 个素数下，M1 图就是星 \(K_{1,r}\)。当 \(r\ge3\) 时它没有覆盖全部顶点的 Hamilton path。因此不存在对所有自然有限窗都“每一步 M1 且全覆盖”的统一一维 spine。

### 9.2 素数重标号对称性阻碍

\(\mathbb N_{>0}\) 的乘法幺半群是以素数为自由生成元的自由交换幺半群，任意素数置换都延伸为乘法自同构。若严格全序只由 bare multiplicative structure 决定且在所有自同构下不变，取 \(p<_*q\)，交换 \(p,q\) 后即迫使 \(q<_*p\)，矛盾。

故 bare multiplicative structure 不允许 automorphism-invariant strict total order of primes。一维 spine 必须额外选择 symmetry-breaking datum（如普通素数大小顺序），不能声称是乘法结构唯一强制出的 canonical axis。

Toolbox outcome: `REUSE / T7_FINITE_SYMMETRY_EQUIVARIANCE`; no new general-purpose tool family.

---

## 10. Surviving candidate：半素数前缀兼容 Hamilton–Gray ray

按普通大小令

\[
p_1<p_2<\cdots.
\]

定义 \(H_1=(p_1^2)\)。对 \(j\ge2\) 定义

\[
B_j=(p_{j-1}p_j,\ p_1p_j,\ p_2p_j,\ldots,p_{j-2}p_j,\ p_j^2),
\]

并递归

\[
\boxed{H_j=H_{j-1}\Vert B_j.}
\]

则对每个 \(r\)：

1. \(H_r\) 恰好覆盖所有 \(p_ip_j,\ 1\le i\le j\le r\) 一次；
2. 每对连续项共享一个 prime token，因此是 M2 边；
3. \(H_r\) 是 \(H_{r+1}\) 的严格前缀；
4. 末项恒为 \(p_r^2\)。

证明：按最大素数下标 \(j\) 分块，顶点只在唯一 \(B_j\) 首次出现；块内全部含 \(p_j\)，块间接口 \(p_{j-1}^2\to p_{j-1}p_j\) 也共享一个 token；新窗口只在末尾追加新块。

直接极限 \(H_\infty\) 因而遍历全部半素数恰好一次。

0-based rank 可显式计算。令 \(T_{j-1}=j(j-1)/2\)：

- \(\operatorname{rank}(p_1^2)=0\)；
- \(\operatorname{rank}(p_{j-1}p_j)=T_{j-1}\)；
- \(1\le i\le j-2\) 时，\(\operatorname{rank}(p_ip_j)=T_{j-1}+i\)；
- \(\operatorname{rank}(p_j^2)=j(j+1)/2-1\)。

该 ray 是 relative to standard prime order 的 canonical traversal；不是 bare multiplicative monoid 内部唯一序。

## 11. 一维主脊不可避免地丢失几乎全部 M2 邻接

任一 \(G_r\) Hamilton path 只有 \(V_r-1\) 条线相邻边，而完整 M2 边数为 \(E_r\)。即使所有线相邻都是 M2 边，直接保留比例也至多

\[
\boxed{
\frac{V_r-1}{E_r}=\frac{r+2}{r^2}\longrightarrow0.
}
\]

对上面显式 \(H_r\)，\(r\ge3\) 时原本一条 M2 边的最大 rank stretch 恰为

\[
\boxed{\frac{r(r-1)}2+1,}
\]

由 \(p_1^2\) 与 \(p_1p_r\) 达到。故 graph distance 1 可在线上被拉成 \(\Theta(r^2)\)。

定位：`GOOD TRAVERSAL / BAD COMPLETE GEOMETRY REPLACEMENT`.

## 12. 最小正确替代结构

最强 surviving coordinate 是：

- 径向：\(R(n)=\Omega(n)\)；
- 壳内：有限支撑素指数向量 \(\nu(n)=(v_p(n))_p\)；
- M1：跨相邻 Omega 壳的一 token 加/删；
- M2：固定壳内的一 token 替换，壳内图距离 \(d_\times/2\)；
- \(k=2\) 时可附加 \(H_\infty\) rank 作为遍历索引。

因此正确对象是分级乘法图 + fixed-Omega shells + optional Gray spine，而不是把所有乘法局部性压成一条线。

---

## 13. 精确有限普查：1 <= n <= 10^7

完整数据：
`research_artifacts/MULTIPLICATIVE_ADJACENCY_NUMBER_AXIS/census_1e7.json`

复核器：
`research_checks/MULTIPLICATIVE_ADJACENCY_NUMBER_AXIS_CHECK_20260829.py --full`

### 13.1 相邻半素数

半素数：1,904,324；相邻半素数对：1,904,323。

- \(d_\times=2\)：41,533 对，占 2.180985%；
- \(d_\times=4\)：1,862,790 对，占 97.819015%。

共享 gcd 素数（仅 \(d=2\)）：
`2:28623, 3:10338, 5:1973, 7:514, 11:70, 13:15`.
窗口内未见共享素数 >=17；仅作有限事实。

最大普通间隙 74：
\[
5,835,191=47\cdot124153,\qquad
5,835,265=5\cdot1167053,
\]
二者互素，\(d_\times=4\)。

M2-相邻的相邻半素数中最大普通间隙 48：
\[
6,950,631=3\cdot2,316,877,\qquad
6,950,679=3\cdot2,316,893.
\]

有限前缀 \(d=2\) 比例：
`10^2:15.1515%, 10^3:5.3691%, 10^4:3.3918%, 10^5:2.5752%, 10^6:2.3115%, 10^7:2.1810%`.
该下降只作实验现象，不作极限主张。

### 13.2 相邻合数

合数：9,335,420；相邻合数对：9,335,419。

- gap 1：8,670,842 对；
- gap 2：664,577 对；
- 无其他 gap。

唯一 \(d_\times=2\) 对是 \(4,6\)。

窗口内最大观测距离 26：
\[
1,048,575=3\cdot5^2\cdot11\cdot31\cdot41,\qquad
1,048,576=2^{20}.
\]

二者相差 1 且互素，故 \(d_\times=6+20=26\)。

反向有限极端：
- \(5,000,000\leftrightarrow10,000,000\)：M1 距离 1，普通差 5,000,000；
- \(4\leftrightarrow9,999,998=2\cdot4,999,999\)：半素数 M2 距离 1（即 \(d_\times=2\)），普通差 9,999,994。

有限普查仅用于结构发现和回归；T1–T5 的全称结论均由证明给出。

---

## 14. 半素数分解交叉检验

`NO FACTOR-BLIND FACTORIZATION GAIN ESTABLISHED`.

原因：

1. 把未知半素数 \(N\) 放到精确 M2 vertex 或 Gray rank 需要先知道两个 prime tokens；
2. M2 邻居判定本质上就是共享非平凡素因子；
3. \(d_\times\) 对已知两数可用 gcd 计算，但不会自动分解单个 \(N\)；
4. 当前 Gray ray 是 factor-aware traversal，不是 factor-blind search oracle。

只有未来从不含因子信息的可观测量稳定预测 M2 block / neighborhood，并在盲测中缩减搜索，才能升级为分解收益。

## 15. Hard-target disposition

- T1 fixed-Omega parity: `PROVED`.
- T2 semiprime gcd classification: `PROVED`, including squares.
- T3 adjacent composites not M1: `PROVED + STRENGTHENED`; global unique \(d=2\) pair is \(4,6\).
- T4 additive-near / multiplicative-far: `PROVED BY CRT`.
- T5 multiplicative-near / additive-far: `PROVED`.
- exact census: `COMPLETE TO 10^7 / CHECKER PASS`.
- complete M1 as 1D axis: `IMPOSSIBLE` by degree.
- bare-multiplicative canonical total order: `IMPOSSIBLE` by prime-relabeling symmetry.
- universal finite-window M1 Hamilton spine: `NO`, already obstructed by \(\Omega\le1\) stars.
- fixed-Omega M2 shell: `EXACTLY CLASSIFIED` as reduced-power token geometry.
- semiprime M2 spine: `EXPLICIT PREFIX-COMPATIBLE HAMILTON-GRAY RAY CONSTRUCTED`.
- line-versus-shell loss: `EXACT`; retained-edge fraction \((r+2)/r^2\to0\).
- prior-art dedup: `DONE / NOVELTY DOWNGRADED WHERE REQUIRED`.
- factorization gain: `NOT ESTABLISHED`.

任务满足 Success criterion 2：T1–T5 完成；自然的一维完整乘法数轴被结构性排除；更小而精确的 M1 graded graph + M2 shells surviving；并额外得到可用但非完整几何的半素数 prefix Gray ray。

## 16. Successor questions

1. 相邻半素数共享因子率 \(d_\times=2\) 的渐近行为；
2. 在 \(G_r\) 的 Hamilton–Gray paths 中最小化最大/平均 omitted-edge stretch；
3. 对一般 \(\Omega=k\) 是否存在 prime-window prefix-compatible \(H_{r,k}\)；
4. 是否存在 factor-blind surrogate 可预测 M2 neighborhood；必须盲测。

## 17. Reproducibility

`python research_checks/MULTIPLICATIVE_ADJACENCY_NUMBER_AXIS_CHECK_20260829.py --full`

Checker verifies:
- gcd distance identity / fixed-Omega parity；
- CRT witnesses \(K=2,\ldots,32\)；
- semiprime prefix Gray spines through \(r=64\)；
- edge-retention formula；
- explicit max-stretch through \(r=24\)；
- exact \(10^6\) and \(10^7\) census regressions；
- no finite adjacent-composite M1 counterexample.

Research-session executions:
- `--limit 1000000`: `PASS`;
- `--full`: `PASS`.

No floating-point arithmetic is used for theorem truth; finite percentages are reporting-only.
