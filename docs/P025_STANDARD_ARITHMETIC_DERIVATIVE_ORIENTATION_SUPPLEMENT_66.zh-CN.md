# P025 补充 66 —— Projective Orientation 背后的标准算术导数

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-paired-square-tail-stage61`  
依赖：P025 补充 65  
Hard block：`NONE`

## 1. Prior-art 身份确认

Supplement 65 定义了

\[
U(n)=\sum_{p\mid n}v_p(n)\frac np.
\]

这并不是新的 derivative-like quantity，而恰好就是标准 arithmetic derivative

\[
\boxed{U(n)=D(n)=n',}
\]

其定义是对每个素数

\[
p'=1
\]

并满足 Leibniz rule

\[
(xy)'=x'y+xy'.
\]

恒等式

\[
n'=n\sum_{p\mid n}\frac{v_p(n)}p
\]

以及该导数的经典大小界都属于已建立的前人数学 [SRC-MERIKOSKI-HAUKKANEN-TOSSAVAINEN-2019-ARITHMETIC-SUBDERIVATIVES]。

因此 P025 不主张 `U`、其公式或其一般 bounds 的新颖性。

## 2. P025-T133 —— projective orientation 是一个固定前人导数上的三角判定

Stage-65 orientation theorem 现在可以不用新记号重写为

\[
\boxed{\rho_c\ge\rho_b\iff a'+c'\ge b',}
\]

\[
\boxed{\rho_c\ge\rho_a\iff b'+c'\ge a'.}
\]

因此

\[
\boxed{b'>a'+c'\Longrightarrow\text{唯一 b-oriented projective maximum},}
\]

\[
\boxed{a'>b'+c'\Longrightarrow\text{唯一 a-oriented projective maximum},}
\]

否则 `c`-oriented term 至少是一个 maximizer，等号给出精确并列。

所以完整 relation-adapted projective optimum 的“方向”只需在三个 integer blocks 上计算**同一个固定 arithmetic derivative**即可决定。

这个 future query 不需要 relation-adapted derivative search。

## 3. 与 Pasten derivative family 的边界

Pasten 的 arithmetic-derivative framework 允许针对指定 `a+b=c` 选择 prime-coordinate derivations。标准 arithmetic derivative 对应固定 prime-coordinate choice

\[
x_p=1
\]

对所有素数都相同。

它通常并不对当前 `a+b=c` 保持 additivity。P025-T133 只把它用作 cyclic projective maximum 的 selector，并没有用它替代 Small Derivatives problem 中的 relation-adapted witness family。

因此必须区分两类角色：

1. **relation-adapted derivatives**：满足当前 declared additive relation 的 certificate；
2. **standard derivative `D`**：一个固定外部 observable，其三个值即可决定 projective orientation。

## 4. 经典大小界本身不能继续提升 Stage-64 tail

若

\[
n=q_1\cdots q_r
\]

其中素数按 multiplicity 重复计数，则经典 arithmetic-derivative bounds 包含

\[
\boxed{r n^{(r-1)/r}\le n'\le\frac{rn}{2}.}
\]

[SRC-MERIKOSKI-HAUKKANEN-TOSSAVAINEN-2019-ARITHMETIC-SUBDERIVATIVES]。

这些 bounds 能约束 derivative-mass triangle，但并不能强迫 side superdominance 必须来自 repeated prime powers。

精确例子

\[
1+30=31
\]

满足

\[
30'=31>1'+31'=1,
\]

所以 `b` orientation 唯一 superdominant，然而 `30` 是 squarefree。

因此 orientation 条件本身不能直接接入 Stage-50/61 的 large-residual counting mechanism。

## 5. 负向路由结论

高 projective threshold 无论 orientation 如何，仍会由 Stage 61 强迫 paired residual pressure。但额外知道

\[
\text{“失败 side 在标准 arithmetic derivative 上 superdominant”}
\]

并不能从当前导入的经典 bounds 中再产生一个独立的大平方因子或 small-radical coordinate。

因此：

> 不能仅因为 Stage 65 出现 arithmetic-derivative superdominance，就宣称获得了更强 exceptional exponent。

若要进一步压 side-oriented tail，需要真正新的外部/内部算术输入，研究满足

\[
a+b=c
\]

且一个 standard arithmetic derivative 大于另外两个之和的解集。

## 6. 精度解释

这次 prior-art 撞线反而强化了架构意义。

一个复杂 relation-conditioned projective system，针对“哪个 orientation 最大”这个 future query，最终只需要保存

\[
\boxed{
\operatorname{sign}(a'-b'-c'),
\quad
\operatorname{sign}(b'-a'-c')
}
\]

这样一个极小 selector state，而其底层 observable 本身完全来自经典前人数学。

这说明新架构的价值可以是：把旧 observable 精确识别成新 future query 的 theorem-native interface，而不是发明 observable 本身。

## 7. Prior-art discipline

标准 arithmetic derivative、其 Leibniz rule、显式公式、logarithmic derivative 与一般 size bounds 全部属于 prior mathematics。P025 只保留 projective-orientation query 到 `a',b',c'` triangle defects 的 exact reduction；该应用的历史 novelty 仍为 `NOVELTY_UNVERIFIED`。

## 8. 下一前沿

Hard block 不存在。继续：

1. 把 derivative-triangle selector 作为 task-specific quotient node，而不是新的 arithmetic derivative；
2. 在尝试 side-superdominant counting theorem 之前，专门检索 `a+b=c` 下 `b'>a'+c'` 一类不等式的既有工作；
3. 当前 PCC tail 继续以 Stage 64 为主，而不是依赖 generic derivative bounds；
4. 把 `old theorem -> theorem-native coarse interface` 模式回流 A2/P023。
