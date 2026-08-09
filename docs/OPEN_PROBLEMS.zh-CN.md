# 开放问题

这些问题被刻意切分到可以独立攻击的大小。参与者不需要先接受进取数论的物理假说。

## P001 —— 刻画整数根的乘法性

难度：中等  
适合作为首个研究问题：是

寻找

\[
R_p(ab)=R_p(a)R_p(b)
\]

成立的充要条件。

可以先从 \(p=2\) 开始。

## P002 —— 坍缩差的紧上界

难度：简单到中等  
适合作为首个研究问题：是

定义

\[
G_p(n)=n-C_p(n).
\]

推导一个盆地内部 \(G_p(n)\) 的紧上界，并且只使用整数表达。

## P003 —— 坍缩算子的交换性

难度：中等

研究哪些 \(p,q,n\) 满足

\[
C_p(C_q(n))=C_q(C_p(n)).
\]

判断是否存在非平凡的全局交换规律。

## P004 —— 坍缩复合的不动点

难度：中等

分类

\[
C_{p_m}\circ\cdots\circ C_{p_1}
\]

的不动点。

## P005 —— 多底数尺度代数

难度：中等

当两个整数尺度底数 \(a\) 与 \(b\) 同时存在时，定义相容的细化和投影，并判断尺度转换顺序什么时候会影响结果。

## P006 —— 带符号状态扩展

难度：中等

构造一个保持纯整数规则的带符号扩展，并明确哪些根运算是全定义、部分定义或对符号敏感的。

## P007 —— 不隐藏分数的一般除法

难度：困难

设计最小但有用的除法结构，使它闭合在显式离散状态中，而不把一个未表示的有理数偷偷当成真正答案。

比较只保留商、把除法视为状态转移、以及剩余序结构等方案。

## P008 —— 最小代数结构

难度：困难

找出能够容纳 v0.1 根与坍缩规律、同时不额外加入连续体假设的最弱成熟代数或序理论结构。

## P009 —— 坍缩半群分类

难度：困难

在有限状态域上研究由有限个坍缩算子和尺度映射生成的半群，分类吸引子、不动点和可能周期。

## P010 —— 历史合流数量何时严格增长

状态：本分支 `RESOLVED`  
难度：中等

T012 已经给出

\[
M_{t+1}(x)\ge M_t(x).
\]

`docs/P010_STRICT_HISTORY_MERGE.zh-CN.md` 已给出精确充要条件：

\[
M_{t+1}(x)>M_t(x)
\]

当且仅当存在一个当前仍可达、且与 \(F_t(x)\) 不同的状态，在 \(T_{t+1}\) 下与 \(F_t(x)\) 发生碰撞。该文还给出严格增量的精确整数公式：增量等于所有新加入碰撞的旧可达纤维 multiplicity 之和；并证明“所有历史都没有新合流”当且仅当 \(T_{t+1}\) 在 \(\operatorname{im}(F_t)\) 上单射。

在多个 WIP 分支尚未统一全局定理编号前，本文继续使用 `P010-T01...T04` 局部编号。

## P011 —— 其他整数不可逆性观察量

难度：中等  
适合作为首个研究问题：是

构造除了原始前像数量以外的整数值观察量，使它们在较广泛的多对一前向映射中保持单调。

不要预设对数。

## P012 —— 没有隐藏欧氏距离的离散几何

难度：困难

提出与有限分辨率思想相容的整数值距离或关系，然后证明哪些度量公理能够保留。

## P013 —— 用 Lean 形式化 T001 与 T005

难度：简单到中等  
适合作为首个形式化问题：是

在 Lean 中形式化整数根刻画和坍缩幂等，优先复用自然数序理论，不依赖实数平方根。

## P014 —— 用 Lean 形式化尺度相容

难度：中等

对一般 \(p\)、整数底数 \(b\ge2\) 和尺度层级 \(s\)，形式化 T010。

## P015 —— 前人工作映射

难度：容易进入  
适合作为首个研究问题：是

建立精确对照表，覆盖整数根、欧几里得除法、内算子、伽罗瓦连接、剩余结构、不可逆半群、前像熵和离散几何。

每个连接都必须同时写清楚相似处，以及进取数论当前做出更强或不同解释的具体位置。

## P016 —— 物理反证标准

难度：困难

列出哪些观测能够推翻“有限分辨率、多对一状态坍缩是基本自然规律，而不仅仅是粗粒化后的有效描述”这一更强假说。

必须把数学矛盾和物理反证严格分开。

## P017 —— Legendre 压力测试：有符号平方进位平衡

难度：研究级困难

把相邻平方盆地作为理论的外部压力测试，沿 `docs/LEGENDRE_PRESSURE_TEST.zh-CN.md` 中已经证明的工具继续推进。

目标不是把 Legendre 猜想换一套符号重述，而是对

\[
\Pi(k)=2+\sum_{d\mid P_k}\mu(d)\kappa_d(k)
\]

或其二进制配对形式

\[
\Pi(k)=2+\sum_{\substack{d\mid P_k\\d\text{ 为奇数}}}
\mu(d)(-1)^{\lfloor k/d\rfloor}\varepsilon_d(k)
\]

找到真正产生证明能力的结构结果。

优先子问题：

1. 对一类非平凡二进制进位项构造符号反转配对或 involution；
2. 必须利用 `根 = 筛选截断 = k` 的自洽约束，而不能只使用平方剩余或任意公共根；
3. 对横向锚点转移 \(\Lambda_b(k)\) 建立可证明的界或递归分类；
4. 寻找把有符号总和降到更小盆地数据的商层递推；
5. 对过强候选不等式优先寻找明确反例。

即使最终反驳“进取数论能沿这条路突破”的设想，也属于有效进展。有限计算、改名后的容斥恒等式或启发式密度模型均不得被写成 Legendre 猜想的证明。

## P018 —— 有限精度证明演算

难度：研究级困难

把“精度变化”本身提升为数学运算，而不是数值计算之后附加的误差说明。

对可比较精度因子 `d|e`，从

\[
\pi_{e\to d}(x)=x//(e/d),
\qquad
\delta_{e:d}(x)=x\bmod(e/d)
\]

出发，建立一套证明演算，使得：

1. 某个命题可以在粗精度上永久决定；
2. 未决定时，共同粗结构严格相消，证明义务下放给有界 detail；
3. carry / borrow 精确记录跨精度层的信息传递；
4. 在整除精度格上，尺度线性 bulk 可被带搬运的 Möbius shell 消去；
5. 整数根尺度状态具有精确、可嵌套的 precision detail；
6. collapse 与 refinement 不交换时，其缺陷被表示成有限盆地坐标，而不是失控的近似误差；
7. refinement-recovery 增量可以严格望远镜相加，并进一步研究跨尺度配对/相消；
8. 检验 P017 中 bulk/carry/shell/half-scale 结构是否是这套一般精度演算的特殊实例。

第一阶段构造与已经证明的恒等式见 `docs/PRECISION_CALCULUS.zh-CN.md`。

不得预设隐藏实数完成，也不得把 `d -> infinity` 极限当作核心定义。filtered/associated graded、multiresolution analysis、interval arithmetic、p-adic precision tracking、projective system、Möbius inversion 等成熟前人工作必须明确引用，不能换名后据为项目原创。

## P019 —— 固定坍缩词的精确稳定化

状态：由 `docs/P019_COLLAPSE_WORD_STABILIZATION.zh-CN.md` `RESOLVED`  
难度：中等到困难

对固定的正指数有限坍缩词

\[
W=C_{p_m}\circ\cdots\circ C_{p_1},
\qquad
L=\operatorname{lcm}(p_1,\ldots,p_m),
\]

研究反复作用 \(W\) 后的精确最终状态，而不只是不动点集合。

规范结果比原先挂在 P009 下的纯坍缩 Draft 更强：

1. 在任意良基偏序上，单调向下自映射稳定到初态下方最大不动点；
2. 任意固定坍缩词因此精确稳定到 \(C_L(n_0)\)；
3. 最终吸引盆地恰好是普通 \(L\) 次坍缩盆地；
4. 词序可以影响瞬态，但整个稳定输入—输出映射只依赖 \(L\)；
5. 坍缩词按稳定等价取商后形成 lcm join-semilattice。

P019 被刻意与 canonical P009 分开，避免悄悄扩大已经解决的 typed collapse+coarsening 范围。

## P020 —— 良基有限稳定化的 Lean 形式化

状态：由 `docs/P020_WELL_FOUNDED_STABILIZATION.zh-CN.md` `RESOLVED`  
难度：中等形式化

在不特化到完全幂的情况下形式化 P019 的母定理。

对严格序良基的偏序集，以及单调、向下收缩的自映射 `F`，在 Lean 中证明：

1. 存在有限 `n`，使 `F^[n] x` 恰好是初态 `x` 下方最大的原始不动点；
2. 因而“有限稳定化”本身是定理内容，不是无限极限约定；
3. 所选稳定化映射单调、向下且幂等；
4. 稳定化与原映射 `F` 具有完全相同的不动点集合。

warnings-fatal 的 Lean 实现在 `EnterpriseMath/Order/WellFoundedStabilization.lean`，并复用成熟的 mathlib 良基归纳和有限迭代 API。

## P021 —— 有限精度离散视界与因果聚焦

状态：`RESERVED / ACTIVE RESEARCH`  
难度：研究级困难

预留给当前研究 PR #48 中保存的黑洞 / 因果聚焦路线。该路线研究有限因果边界、未来截面扩张、聚焦谱、方向轨道与因果角色，但不声称当前离散原型已经推导出广义相对论，也不把离散量直接认定为物理 shear 或 Ricci curvature。

在下一次 clean semantic replay 之前，历史分支文件名和内部正文仍可能保留已被替代的 P019 编号。

## P022 —— 最小精度晶格几何与距离进位

状态：`RESERVED / ACTIVE RESEARCH`  
难度：研究级困难

预留给当前 PR #50 中保存的晶格几何路线：纯整数 `A_p` / root-lattice 候选、primitive graph distance、quadratic separation、有限精度径向距离、加一型 triangle carry、shell/ball 与 geometry-aware collapse。

FCC/HCP/BCC/`A_p` 继续只是数学测试候选，并非已经确认的物理空间。在 clean replay 前，历史分支文件名和内部正文仍可能保留已被替代的 P019 编号。

## P023 —— 可复合安全坍缩与未来兼容商

状态：`OPEN / ACTIVE RESEARCH`  
难度：研究级困难

精确刻画：一个有限精度商在什么条件下已经足以承载指定的未来运算族；若不足，**最少还需要补回什么 detail**。

当前第一阶段结果见 `docs/P023_COMPOSITION_SAFE_COLLAPSE.zh-CN.md` 与补充 01–05，包括：

1. fiber 常值是商上因子化的精确判据，`(q,h)` 是最粗的一步修复；
2. 对单个确定转移及有限运算族，反复未来细化会有限稳定到最粗的未来兼容 refinement；
3. floor 精度与 quotient / multiple-collapse 的精确算术兼容分类；
4. 不兼容 multiple-collapse 情形下的 one-bit 最小修复与 split fiber 精确周期；
5. reductive gap 到 coarse borrow 的精确搬运，以及局部 borrow 对首尾 coarse loss 的望远镜化；
6. factorization 与最粗一步修复母命题已经通过 Lean warning-fatal 编译。

一般 quotient factorization、congruence、automata distinguishability 与 partition refinement 属于成熟前人工作，不得作为进取数论原创主张。

下一阶段优先问题：

- 把 future-safe refinement 写成有限状态等价关系格上的单调向下算子，并与 P020 有限稳定化母定理严格连接；
- 判断最小安全修复何时必然离开单一均匀 `Q_r` 尺度族，从而需要局部 bounded detail；
- 通过不动点几何分类 P008 型单调、向下、幂等坍缩在 floor precision 上何时可下沉；
- 把该判据反哺到 P021 的 phase/magnitude 与 witness-transport 纠偏，并与 P018 已有 finite-response 演算去重整合。

## 如何领取问题

可以创建一个标题包含问题编号的 GitHub Issue，或者在已经存在的对应 Issue 下参与讨论。

有效贡献可以是证明、反证、更小反例、计算结果、前人工作、形式化结果，或者更精确的问题表述。
