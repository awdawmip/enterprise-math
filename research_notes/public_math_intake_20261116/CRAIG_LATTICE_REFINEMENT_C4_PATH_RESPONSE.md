# Craig 的格点细化方法与 X6 辅助路径相位

2026-11-16 · 公开文献吸收与有限模型推导 · 作者侧证明和精确复算，待独立审阅。

## 原论文给出的方法

Nathaniel Craig 的 [OpenAI 文章](https://openai.com/index/step-toward-defining-the-standard-model/)（11 月 15 日）介绍 10 月 6 日的预印本 [arXiv:2610.09093v1](https://arxiv.org/abs/2610.09093v1)。[定理 4.1、§6.4 的式 (75)、§§7、9](https://arxiv.org/html/2610.09093v1) 在受限的四维欧氏有限周期格点规范场上处理手征费米子测度。作者提出标准模型有限格距候选定义；反射正性、实际模拟和相互作用标准模型的连续极限仍需分别研究。原论文用固定粗格点构型生成细层，追踪同一条允许闭路。相邻层修正 B_n 从投影算子的局部比较构造，再证明 exp(i∮B_n)=T_n/T_(n+1)。相乘 N 层精确留下 T_0/T_N。原文分别证明修正级数可求和、对每条固定闭路 T_N→1，并涵盖不可缩闭路。四维证明的局部项界 O(h⁸)、点数密度 O(h⁻⁴) 给出 O(h⁴) 的层界。迁移到路径模型时，每条支路的缺陷要结合可达支路数量、权重及实际观察来估计。论文的幂次和物理结论均属于其自身模型。

项目 11 月 16 日的[早间来源记录](https://github.com/awdawmip/enterprise-math/blob/a776f9ea24a702c10da3ef8a20c0763f3f341bae/research_notes/public_math_intake_20261116/OPENAI_NOV16_STABLE_SOURCE_PRIOR_CONTINUATION_CLOSED_CURRENT_READ_PENDING.md)覆盖此前 10 月公告及 openai/math 仓库，本篇补入 Craig 论文。可供[既有 QFT/BRC 尺度任务 C4–C6](https://github.com/awdawmip/enterprise-math/blob/a776f9ea24a702c10da3ef8a20c0763f3f341bae/research_tasks/RS-OPENAI-QFT-BRC-RESIDUAL-20261028.md)引用。

## 固定原路径后的第一个障碍

使用 [PREFIX-436 定理 A、B](https://github.com/awdawmip/enterprise-math/blob/c4d450536bf71ed87fd74555295ec60485262f0a/research_notes/portable_direct/2026-11-02_prefix436_signed_x6_c4_holonomy_and_q_lucas.md) 的有向辅助 C₄ 标签。X6 的其余四个坐标固定时，沿 +e₂ 的边记 x₁，沿 -e₂ 记 −x₁，其他方向记 0，按 4 取余。单位回路 (+e₁,+e₂,−e₁,−e₂) 的标签为 1。这里细化的是外加的比较格点，m 是每条边划分的份数；均匀指同向细方格具有相同回路标签。物理时间、原生 Cell 动力学保持分别定型。[PREFIX-437](https://github.com/awdawmip/enterprise-math/blob/1fc25a040ab5f5570692fd7f081e652b22f8f728/research_notes/portable_direct/2026-11-02_prefix437_s6_equivariant_c4_brc_six_axis_gaussian_sign.md)另行处理全六轴置换对称性；此处使用带方向的模型。

**判据。** 取相同的 C₄ 作粗、细标签，要求外边界仍有标签 1。m×m 个小方格的公共边反向相消，设每格标签 t，则须 m²t≡1 (mod 4)。偶数 m 没有解。奇数 m 唯一解为 t=1，并且真的可以实现：在细格 y 上使用原有规则，粗顶点 x 对应 y=mx。一条粗竖边的 m 个子步合计 ±m²x₁≡±x₁。所以任意旧路径的逐边细分都保留其标签。奇偶只来自该辅助标签群和均匀假设。

**保持细格均匀的构造。** 对任意正整数 m，选 C_(4m²)，粗标签嵌入 k↦m²k。细边继续取 θ_f(y,±e₂)=±y₁，每个细方格标签为 1。其余方向标签为 0。旧竖边的 m 个子步之和为 ±m²x₁，这是原标签的像；串接得到所有旧有序路径的相容性。特别在 m=2 时，C₄→C₁₆ 按 k↦4k 嵌入，四格的总标签 4 对应粗标签 1。若要求在有限阿贝尔群中以四个相同元素 t 表示一个阶四元素，则 ord(4t)=ord(t)/gcd(4,ord(t))=4 给出 ord(t)=16；C₁₆ 是此假设下最小选择。兼容性只在嵌入的粗语义上声明。

**保持 C₄ 的非均匀对照。** 也可反过来保留标签群，放宽细格平移均匀性。令细横边标签为 0；从整数位置 (u,v) 出发的正竖边，当 v≡m−1 (mod m) 时取 floor(u/m)，否则取 0，负竖边取对应正竖边的相反数。每个粗方格内仅右上角那个细方格的标签为 1，其余为 0。每条 m 段的粗竖边恰有一段贡献 ±x₁，粗横边贡献为 0。故此方案也保留每条旧路径，代价是选择了有标记的子格。两种可行解辨明了偶数障碍依赖哪些假设。

## 细化时保住每条旧路，仍会改变全部路径响应

用 m=2 的均匀 C₁₆ 构造，在原点附近取两个正方向，粗位移 (1,1) 有两个最短步词，细位移 (2,2) 有六个。令 q 为原始十六阶单位根，因此 q⁴=i。细化 xy、yx 得到 xxyy、yyxx，读数分别为 q⁴、1。枚举全部六条细路得到如下精确的 BRC 标签直方图（每条支路权重为一）。

| 路径族 | 标签 0 | 标签 1 | 标签 2 | 标签 3 | 标签 4 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 两条旧路的细分 | 1 | 0 | 0 | 0 | 1 |
| 全部细格最短路 | 1 | 1 | 2 | 1 | 1 |

旧路读数为 1+i；新增四条支路的读数之和 q+2q²+q³=q(1+q)²≠0。因此，哪怕所有旧路径都可逐条保真嵌入，把所有新增细路也纳入求和，总响应已经改变。这是精确的有限反例。后续可以比较哪些细路属于同一个粗路径、它们如何计权，并对新增支路的加权总贡献给出各层估计；有限例子未决定尺度极限。PATH_FORMAL_BRC 的来源与原始步词可保存，N_BRC 用于验证分支数，复数仅作独立声明的辅助符号读出。这里没有把正权直接当成量子振幅。

## 命名来源的交叉检查

[项目 V38](https://github.com/awdawmip/enterprise-math/blob/a776f9ea24a702c10da3ef8a20c0763f3f341bae/research_notes/X6_ZERO_CURRENT_NONABELIAN_COMMUTATOR_MEMORY_V38_20260906.md) 的两条历史 ABA⁻¹B⁻¹、AA⁻¹BB⁻¹ 具有完全相同的 12 项有向事件多重集，净流均为零。重跑[项目原检验](https://github.com/awdawmip/enterprise-math/blob/a776f9ea24a702c10da3ef8a20c0763f3f341bae/experiments/x6_nonabelian_multicircuit_v37_20260906/check_nonabelian_multicircuit.py)，运输分别是三循环 (1,2,0) 和恒等 (0,1,2)。任意逐有向边固定的可交换标量赋值均在这两条历史上给出同一乘积，不能从中恢复哪一槽承载具名来源。若细分时在各顶点重命名，用同一基点识别两层，沿路相邻的重命名抵消，终端运输只受基点共轭；三循环仍与恒等有别。[V39](https://github.com/awdawmip/enterprise-math/blob/a776f9ea24a702c10da3ef8a20c0763f3f341bae/research_notes/X6_CYCLE_CURRENT_S3_OPERATION_SAFE_PORT_V39_20260906.md) 给出在固定网络上查询净流和框架运输、允许续接闭路这一语言中的最粗充分记录 (j,h)。这个例子明确了与 Craig 的可交换行列式相位不同的项目观察要求。

## 有限复核

复核使用固定提交 [signed_brc.py](https://github.com/awdawmip/enterprise-math/blob/c4d450536bf71ed87fd74555295ec60485262f0a/experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py) 的 shortest_path_multiplicity，输入为六轴位移 (1,1,0,0,0,0)、(2,2,0,0,0,0)，得到 2、6。下面的独立候选标签扩展按原始有序步词串接，替代分支作带重数的直方图相加；环标签与符号读数分别观察。将固定文件放在同一目录，在 Python 3 中运行以下程序，可同时复算偶奇、直方图和两种构造。m∈{2,3}、9 个起点、长度 0 至 4 的全部 341 个有向两轴步词，共 6,138 项每种构造；两种构造各自零差异。任意路径结论由逐边证明给出。未作原生相位或物理测量。

```python
from collections import Counter
from itertools import product
from signed_brc import shortest_path_multiplicity

def transport(start, word, modulus):
    x, y = start
    tag = 0
    for step in word:
        if abs(step) == 1:
            x += step
        else:
            sign = step // 2
            tag += sign * x
            y += sign
    return (x, y), tag % modulus

def lift(word, m):
    return tuple(step for step in word for _ in range(m))

checks = 0
for m in (2, 3):
    for start in product((-1, 0, 1), repeat=2):
        for length in range(5):
            for word in product((1, -1, 2, -2), repeat=length):
                stop, tag = transport(start, word, 4)
                fine = transport(tuple(m * x for x in start), lift(word, m), 4*m*m)
                assert fine == (tuple(m * x for x in stop), m*m*tag)
                checks += 1

def shortest_family(n):
    return [word for word in product((1, 2), repeat=2*n) if word.count(1) == n]

coarse, fine = shortest_family(1), shortest_family(2)
block = [lift(w, 2) for w in coarse]
for n, family in [(1, coarse), (2, fine)]:
    assert len(family) == shortest_path_multiplicity((n,n,0,0,0,0))
def bins(words):
    return Counter(transport((0,0), w, 16)[1] for w in words)
assert bins(block) == {0:1, 4:1}
assert bins(fine) == {0:1, 1:1, 2:2, 3:1, 4:1}
for m in range(1, 25):
    hits = [t for t in range(4) if (m*m*t)%4 == 1]
    assert hits == ([1] if m%2 else [])
print(checks, 'path comparisons; fine histogram:', sorted(bins(fine).items()))

# Nonuniform C4 control. Mark one fine square per coarse block.
def sparse_transport(start, word, m):
    x, y = start
    tag = 0
    for step in word:
        if abs(step) == 1:
            x += step
            continue
        sign = step // 2
        edge_y = y if sign == 1 else y-1
        if edge_y % m == m-1:
            tag += sign * (x // m)
        y += sign
    return (x, y), tag % 4

sparse_checks = 0
for m in (2,3):
    for start in product((-1,0,1), repeat=2):
        for length in range(5):
            for word in product((1,-1,2,-2), repeat=length):
                stop, tag = transport(start, word, 4)
                assert sparse_transport(tuple(m*x for x in start), lift(word,m), m) == (tuple(m*x for x in stop), tag)
                sparse_checks += 1
    squares = [sparse_transport(s, (1,2,-1,-2), m)[1] for s in product(range(m), repeat=2)]
    assert Counter(squares) == {0:m*m-1, 1:1}
print(sparse_checks, 'nonuniform fixed-C4 path comparisons')
```
