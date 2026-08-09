# 前人工作 — P024 晶格 Guard 精度

## 1. 范围

P024 补充 01 把成熟的 hyperplane-arrangement 与 affine-semigroup 数学，与 Enterprise Math 的未来兼容精度解释组合起来。

这一组合解释的历史新颖性继续保持 `NOVELTY_UNVERIFIED`。

## 2. Hyperplane arrangement

Thomas Zaslavsky 的 *Facing up to Arrangements: Face-Count Formulas for Partitions of Space by Hyperplanes* 是研究有限超平面 arrangement 所诱导空间分割与 face 组合结构的标准前人来源之一。[SRC-ZASLAVSKY-1975-HYPERPLANE-ARRANGEMENTS]

因此 P024 **不把以下内容声明为发明**：

- 有限仿射超平面 arrangement；
- 超平面 cut 所诱导的 cells/faces；
- 经典的区域/face 计数理论；
- 线性阈值 sign 数据在 arrangement 胞元上保持常值这一一般事实。

P024 只是在未来动作系统先决定了哪些平移后的整数 guard 边界真实相关之后，使用这一成熟语言描述所得精度胞元。

## 3. Affine semigroup、saturation 与 holes

Hemmecke、Takemura 与 Yoshida 明确研究了由 `Z^d` 中有限向量集生成的交换半群、其 saturation，以及半群与 saturation 之间的 holes；该论文还给出了 transportation semigroup 中的无限 hole 家族。[SRC-HEMMECKE-TAKEMURA-YOSHIDA-2009-AFFINE-HOLES]

因此 P024 **不把以下内容声明为发明**：

- 整数向量生成的 affine semigroup；
- 在有理锥与生成群内部进行 saturation/normalization 型完成；
- affine semigroup holes；
- 高维 affine semigroup 可能存在无限多个 holes；
- affine semigroup 的 conductor / saturation-point 问题。

文中使用的小型显式见证

`<(2,0),(0,1),(1,1)>`

只用于说明：一维 numerical semigroup 的“有限 holes”图景不能不加条件地整体推广到高维动作幺半群。

## 4. 整数晶格与群完备化

整数晶格像、gcd/Bezout、子群生成、正整数关系、Hermite/Smith normal form 与整数线性可行性都是成熟数学。

P024 中写出的判据

`N A = Z A 当且仅当生成元存在严格正整数零关系`

之所以给出普通证明，是因为它恰好构成动作语言解释所需的边界；不主张该代数事实本身的历史优先权。

## 5. 与 A3、P023 的关系

A3 relation-quotient 路线已经研究候选粗 fiber 内的隐藏 guard-image lattice，以及线性阈值 branch pattern 的精确可达性，并使用标准 hyperplane-arrangement 复杂度界。

P023 继续拥有一般母命题：声明的未来 operation/observation language 决定最粗未来安全等价关系。

P024 补充 01 的范围更窄，只处理：

- 显式晶格状态 `Z^n`；
- 纯平移动作词；
- 完整整数仿射 guard bit 向量；
- 未来 guard 边界向当前状态空间回拉；
- 所得精度胞元与 guard-score lattice 的可行性。

## 6. Enterprise Math 边界

当前可以合理维护的项目侧综合是：

```text
整数晶格状态
+ 平移动作语言
+ 完整整数仿射 guard 向量
        |
        v
把未来动作词投影到每个原始 guard score
        |
        v
把未来阈值回拉成当前 guard cuts
        |
        v
与公共 guard-score lattice 相交
        |
        v
最粗未来安全精度胞元
```

因此本补充的项目侧研究内容，仅在于这一精确精度解释，以及对以下四层的分离：

- 动作侧投影可达性；
- 观测方向的边界结构；
- 状态侧 score-lattice 可行性；
- 完整 guard-vector 与聚合 observable 的边界。

不声称发明 hyperplane arrangement、affine semigroup、晶格 normal form 或整数可行性理论。
