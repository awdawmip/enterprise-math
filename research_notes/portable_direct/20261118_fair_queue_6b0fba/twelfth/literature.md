# 二进阶深度、强伪素数底数与循环子群图的文献归属

审计日期为 2026-11-18，目标为第二代任务 `TP2-0798C0D5D6CFA605184A`。冻结数学结论来自 `RR-2D43CCB30B906AFB6E20`。**单单位的等深判据和精确失败概率均有可核验的先行文献。多单位的图结构与全阶计数也分别对应已有群论、幂图定理。** 下表分别记录已经同构的数学对象和仍缺直接文献匹配的应用表述。[第二代任务书](https://github.com/awdawmip/enterprise-math/blob/7d5c426a6de0fd155adf108da907473a8bb39421/research_tasks/RSA_EXPONENT_COLLISION_EXTERNAL_PRIOR_ART_DUPLICATION_AUDIT_GEN2_20261012.md) · [冻结数学原文](https://github.com/awdawmip/enterprise-math/blob/628aad28918a8fcf1937713299405c2efb54f5f1/research_returns/RSA_EXPONENT_COLLISION_CRT_COLLAPSE_RETURN_20260827.md)

令 $p,q$ 是互异奇素数，$n=pq$，$p-1=2^Au$、$q-1=2^Bv$，$u,v$ 为奇数，$m=\min(A,B)$。随机性均指先均匀取整个单位群中的元素，并拥有该元素的有效正湮灭指数；若预先固定某个仅对部分元素有效的指数，再按有效性筛选，会改变采样分布。此处的“等深”指 $v_2(\operatorname{ord}_p x)=v_2(\operatorname{ord}_q x)$。

| 冻结命题 | 判定 | 文献所覆盖的确切范围 |
|---|---|---|
| 全局幂映射相等的非零指数差是群指数 $\lambda(n)$ 的倍数；给定全局湮灭指数的经典推论 | EXACT_DUPLICATE | 指数核是有限群指数的定义。Miller 1976 的确定性复杂度归约（特别是定理 3）带 ERH 条件；RSA 1978 §IX.C 明述可使用 $\operatorname{lcm}(p-1,q-1)$，HAC §8.2.2(i)、Fact 8.6 给出从 $ed-1$ 出发的随机版本及至少一半的界。这三个命题的前提应分别引用。[Miller 原文](https://www.cs.cmu.edu/~glmiller/Publications/Papers/Mi76.pdf) · [Rivest–Shamir–Adleman 原文](https://people.csail.mit.edu/rivest/pubs/RSA78.pdf) · [HAC 第 8 章](https://cacr.uwaterloo.ca/hac/about/chap8.pdf) |
| 给定一个单位，其二进阶链的失败事件恰为等深 | EXACT_DUPLICATE | Shor §5 对任意多个不同奇素数幂明确按各局部阶的二部分是否全相等分类。其表述用真实阶。有效湮灭指数的奇部与真实阶的奇部仅差一个奇数乘子，保留二主分量全部局部阶。因此冻结版本的输入包装不同，事件完全相同。[Shor §5](https://arxiv.org/pdf/quant-ph/9508027) |
| 均匀单位的单次失败率 $F_1=(4^m+2)/(3\cdot2^{A+B})$ | EXACT_DUPLICATE | Leander 2002 引理 1 已印等价几何和，有成功／失败措辞歧义。Abbassi–Bayle 2025 预印本定理 5.2、6.2 的两个条件概率相乘，独立给出同式。[Leander 引理 1](https://arxiv.org/pdf/quant-ph/0208183) · [Abbassi–Bayle 定理 5.2、6.2](https://arxiv.org/pdf/2505.00433) |
| 固定测试指数 $n-1$ 的强伪素数签名与底数计数 | PARTIAL_ANTECEDENT | Jaeschke 命题 1 对不同素因子、与各底数互素的平方自由整数，另要求各底数已通过 Fermat 条件，才可用签名相等判定。Monier 1980 命题 1 有额外的奇部公因子乘积。下文给出差异恰是多少。[Jaeschke 命题 1](https://cr.yp.to/bib/1993/jaeschke.pdf) · [Sorenson–Webster 定理 2.2](https://arxiv.org/pdf/1509.00864) · [Monier 原文](https://doi.org/10.1016/0304-3975(80)90007-9) |
| 全单位下的至少一半成功界；对某些指定字符类的其他比例 | ADJACENT_METHOD | 前者在 Shor 与 HAC 中已有；单用下界推不出 $F_1$ 的依参精确值。Leander 后部另以 Jacobi 符号 $-1$ 为抽样条件，分母已改变。[Shor §5](https://arxiv.org/pdf/quant-ph/9508027) · [Leander](https://arxiv.org/pdf/quant-ph/0208183) |
| 取最小公倍数对交换群生成元同时湮灭；各单位分开观察的独立失败概率为 $F_1^k$ | EXACT_DUPLICATE | 前者是生成子群指数的定义及可交换性，后者是独立事件乘法。Jaeschke 多底数签名针对逐底数的条件；进一步取生成元的所有组合，是另一个事件。[Jaeschke 命题 1](https://cr.yp.to/bib/1993/jaeschke.pdf) |
| 生成的二主子群在两个投影上皆单射，当且仅当它是其两个像间同构的图 | EXACT_DUPLICATE | Goursat 引理的两个核均平凡特例。Tóth 2014 §2、定理 3.1 还给出了两循环群直积的全部子群参数化。局部阶相同这一性质对全部元素成立，正好排除两个投影核中出现非幺元。[Tóth，§2–3](https://arxiv.org/pdf/1312.1485) |
| $k$ 组单位产生的图障碍的精确计数核 | EXACT_DUPLICATE | 转置 $k$ 组坐标后，分子恰为一个同型幂群中生成同一循环子群的有序对数。Curtin–Pourgholi 引理 1.4 已给出这个计数，Tóth 2012 给出所需各阶元素数。以下还原对角线、方向和不等阶的分母。[Curtin–Pourgholi 引理 1.4](https://doi.org/10.1017/S0004972714000434) · [Tóth 2012](https://arxiv.org/pdf/1203.6201) |
| 将逐单位湮灭证书、最小公倍数、全部组合的失败与幂图计数并列成同一份应用命题 | NO_MATERIAL_MATCH | 在下列检索与引用链中没有定位到同一文献逐项呈现这一完整表述。源文的各数学组成已有可指认的出处；此检索边界无法证明完整表述首创。 |

## 一、精确概率的两个原文口径

在单位群的两个循环二主分量中，深度 $0$ 有一个元素；深度 $t\ge1$ 有 $2^{t-1}$ 个。故等深分子的二主部分为
\[
 C_m=1+\sum_{j=0}^{m-1}4^j=\frac{4^m+2}{3},\qquad F_1=\frac{C_m}{2^{A+B}}.
\]
Leander 原 PDF 第 1 页引理 1 的行间式正是 $2^{-A-B}(1+\sum_{j=0}^{m-1}4^j)\le1/2$。它前面刚叙述了成功事件，文字未指明显示的量改为互补事件；同一处 $p-1,q-1$ 的奇部变量也有印刷问题。可用原文后部 $m_1,m_2$ 的局部群阶分解，或者直接用上述已定义的 $A,B$，审计该公式。等深分子的计数与下一个独立来源都将其认定为失败率。Abbassi–Bayle（2025 年 v2 预印本）对不同奇素数幂的乘积给出先取单位后为偶阶的概率，再条件于偶阶给出半阶幂不等于 $-1$ 的概率。特化到两素数，分别为
\[
 (T-1)/T,\qquad (T-C_m)/(T-1),\qquad T=2^{A+B}.
\]
故本任务的成功概率是二者乘积，失败概率为 $C_m/T$。定理 6.2 合并全部步骤时还有取到单位的概率；本题最初已条件于单位。这里未使用任何量子采样步骤。[Leander 原页](https://arxiv.org/pdf/quant-ph/0208183#page=1) · [Abbassi–Bayle 定理 5.2、6.2](https://arxiv.org/pdf/2505.00433)

**强伪素数计数的精确差额。** 记 $n'$ 为 $n-1$ 的奇部。Monier 的强伪素数底数集 $S(n)$ 在本题的半素数上满足
\[
 |S(n)|=C_m\gcd(n',u)\gcd(n',v)=C_m\gcd(u,v)^2 .
\]
因为 $n-1\equiv q-1\pmod{p-1}$，且 $u$ 为奇数，所以第一项公因子为 $\gcd(u,v)$；另一边同理。全单位的等深元素数为 $C_muv$。两者相等当且仅当 $u=v$。例如 $21=3\cdot7$ 的 12 个单位中，等深者有 6 个，强伪素数底数只有 2 个。Jaeschke 要求的 Fermat 条件在这个例子中真正改变集合。Monier 的精确式由 Bach–Shallue 命题 2.1 以现代符号重列，可交叉核对。[Monier 1980](https://doi.org/10.1016/0304-3975(80)90007-9) · [Bach–Shallue 命题 2.1](https://arxiv.org/pdf/1308.0880)

## 二、多单位公式与经典幂图计数逐项对应

把 $k$ 对局部二主分量写成两行 $a\in C_{2^A}^{\,k}$、$b\in C_{2^B}^{\,k}$，采用加法坐标。将这两个循环群分别嵌入 $C_{2^M}$ 的唯一同阶子群，$M=\max(A,B)$。若列向量生成的子群是同构的图，两个局部投影具有相同阶 $2^t$，在共同循环群中的像相同。该像的自同构是乘某个奇数 $w$，于是 $b=wa$，两行生成相同的循环子群。反过来，两行生成同一循环子群就相差一个可逆的奇数乘子（两行全零时取 $w=1$），每列都落在相应图中，所生成子群是限制在其像上的图。这样，原命题的好坏分类与原始幂图文献的等价关系之间给出了双向字典。[Tóth 的 Goursat 参数化](https://arxiv.org/pdf/1312.1485) · [Cameron 的循环子群等价关系](https://webspace.maths.qmul.ac.uk/p.j.cameron/preprints/powergraph2.pdf)

相等的两个行子群必落在两边共同的 $K=C_{2^m}^{\,k}$ 中。令 $B(K)$ 为有向幂图中无序、不同顶点的双向边集合。Curtin–Pourgholi 引理 1.4 给出
\[
 |K|+2|B(K)|=\sum_{z\in K}\varphi(o(z)).
\]
左边加回对角线并恢复有序性，恰好计数两个行向量生成同一循环子群的情形。在 $K$ 中阶整除 $2^t$ 的元素有 $2^{tk}$ 个，故阶恰为 $2^t$ 的元素有 $2^{tk}-2^{(t-1)k}$ 个。冻结原文的概率因此等于
\[
 \frac{|K|+2|B(K)|}{2^{(A+B)k}}=
 \frac{1+\sum_{t=1}^{m}\varphi(2^t)\big(2^{tk}-2^{(t-1)k}\big)}{2^{(A+B)k}} .
\]
分母是原始全部两行选择数，即使 $A\ne B$ 也保持这一口径。取 $A=B=2,k=2$，前式为 $28/256=7/64$，逐单位独立失败为 $(3/8)^2=9/64$。取 $A=2,B=3,k=2$，分子仍为 28，分母变为 1024。这一归属使用原论文明确的计数和双射，不涉及其“给定群阶哪个群最多”的极值定理。[Curtin–Pourgholi 2014，引理 1.4](https://doi.org/10.1017/S0004972714000434) · [Tóth 2012，各阶元素计数](https://arxiv.org/pdf/1203.6201)

## 检索与复算边界

检索面为公共网页索引、作者或校方原版 PDF、arXiv 作者稿、出版社期刊及 DOI 页面。先从任务书引文查 Miller 与 HAC，再沿 Jaeschke、Monier 和 Goursat 的引用链核对，并以幂图双向边术语复搜。以下为本轮实际使用、足以复查主要结果的原始检索串：

- `Shor polynomial time algorithms for prime factorization and discrete logarithms on a quantum computer exact powers factors section 5 algorithm only fails all of these powers of 2 agree`
- `Gerhard Leander exact probability Shor's factoring algorithm alpha beta distribution p - 1 q - 1 probability S_N formula`（检索串中的名字如此；核实作者为 Gregor Leander。）
- `Monier 1980 evaluation and comparison two efficient probabilistic primality testing algorithms number strong liars formula gcd odd part strong liars Bach Shallue formula strong probable primes fewer two strong liars`
- `Sorenson Webster strong pseudoprimes twelve prime bases Proposition 2.2 signature Jaeschke order strong pseudoprime Fermat all prime divisors signatures`
- `Rivest Shamir Adleman 1978 A Method for Obtaining Digital Signatures and Public-Key Cryptosystems IX determining d without factoring n Miller multiple lcm PDF MIT`
- `"graph of an isomorphism" "order" "Shor" subgroup random elements Miller-Rabin distinct primes multiple bases Goursat failure probability diagonal subgroup`
- `László Tóth Subgroups of finite abelian groups having rank two Goursat theorem 4.1 subgroups cyclic graph automorphisms arxiv`
- `power graph bidirectional edges number phi order group same cyclic subgroup sum Euler phi element orders pairs Chakrabarty Ghosh Sen Curtin Pourgholi theorem 2.1`

以 `python literature_check.py` 可复算四个固定小模数的两个底数计数，以及四个加法循环群参数组。后者逐对比较直接生成子群的两个投影大小与两行所生成的循环子群，再对照文献闭式。证据文件为 `literature_checked.json`。有限测试用于核对样本空间、方向和归一化；对所有参数的归属依据是原文命题与上述等价变换。本次达成有界审计目标 `RSA_EXPONENT_COLLISION_PRIOR_ART_DUPLICATION_CLASSIFIED`。外文中完整组合表述的未命中不构成新颖性证明。
