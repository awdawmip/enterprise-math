# 进取数论逻辑黑名单

状态：`ACTIVE / PROJECT-LEVEL RESEARCH LOGIC`

日期：`2026-09-09`

本文件记录的不是“效果较差的研究习惯”，而是：当目标已经明确时，除非先正式重定义目标，否则在逻辑上不得用于证明该目标的研究模式。

黑名单并不意味着某种构造在所有数学语境中都被禁止。同一个构造可以对一个较弱 theorem 合法，却对量词更强的 theorem 属于目标泄漏。本文件的目的，是阻断前提偷渡、答案预置和语义偷换。

## LB-01 — 目标泄漏式残差补全

### 模式

目标要求一个精确的全局恒等式，例如

\[
E(u)=0
\quad\text{或}\quad
f\equiv0.
\]

研究路线却变成：

1. 先规定或构造一个已经带有所需终点行为的候选对象；
2. 再把它不满足目标方程的部分定义为残差、修正项或外力：
   \[
   r:=E(u)
   \quad\text{或}\quad
   f:=E(u);
   \]
3. 证明该残差很小、衰减、在一个点无穷阶平坦、若干阶为零，或者在某个指定极限 / 缩放下消失；
4. 最后把这些较弱性质当成“原来的精确零残差目标已经被导出”的证据。

### 判定

`BLACKLISTED_FOR_ZERO_RESIDUAL_TARGETS`。

### 逻辑缺陷

- `TARGET_LEAKAGE`：在真正解出目标方程之前，目标输出已经参与候选 witness 的设计；
- `QUANTIFIER_MISMATCH`：把“存在一个允许的残差 / 外力”偷换成“残差 / 外力恒等于零”；
- `LOCAL_TO_GLOBAL_SUBSTITUTION`：把点态、jet、渐近或 rescaling 后的消失偷换成全局恒等式；
- `WITNESS_CONTAMINATION`：修补项先由目标 witness 反向定义，再被拿来证明 witness 仿佛不依赖修补项；
- `SEMANTIC_TARGET_SUBSTITUTION`：一个形式上证明了的较弱 / 不同 theorem 被提升成更强目标的证据。

### 形式冻结

\[
\bigl[D^\alpha r(x_*)=0\ \forall\alpha\bigr]
\not\Rightarrow
\bigl[r\equiv0\bigr].
\]

同样：

`RESCALED_RESIDUAL -> 0`

绝不自动推出

`ORIGINAL_RESIDUAL ≡ 0`，

除非另有独立的全局 theorem。

### 允许边界

如果某个 theorem 本身就明确把残差 / 外力 / 修正项放在存在量词里，并允许研究者选择它，那么 residual completion **不因此自动构成该 theorem 的逻辑错误**。

但是：

`VALID_FOR_EXISTENTIAL_FORCED_THEOREM != EVIDENCE_FOR_ZERO_FORCE_THEOREM`。

从前一条路线进入后一条路线，必须另有一条真正证明精确零残差恒等式的 bridge theorem。

## Navier–Stokes 特化

对进取数论的无外力 Navier–Stokes 路线，冻结：

`FORCING_IDENTICALLY_ZERO_FROM_PREMISE_TO_CONCLUSION`。

因此，下面这条路线被列入黑名单：

`DESIRED_SINGULAR_PROFILE -> DEFINE_NS_RESIDUAL_AS_FORCE -> PROVE_FORCE_FLAT/SMALL -> CLAIM_ENDOGENOUS_BLOWUP`。

必须始终区分：

- `FLAT_AT_SINGULAR_POINT != ZERO_FORCE`；
- `ZOOM_LIMIT_UNFORCED != ORIGINAL_TRAJECTORY_UNFORCED`；
- `FORMAL_VERIFICATION != SEMANTIC_TARGET_EQUIVALENCE`；
- `FORCED_BREAKDOWN_WITNESS != UNFORCED_SELF_INSTABILITY`。

当前研究方向命名为：

`AUTONOMOUS_SELF_STATE_INSTABILITY`。

其含义是：先固定 \(f\equiv0\)，只允许 Navier–Stokes 自主方程本身产生演化，再研究状态是否会由自身动力学失稳。该名称是研究方向，不是定理状态。

## 证明助手规则

形式化证明只能认证“已经编码进去的 theorem”。它不会替研究者证明“这个 theorem 与另一个研究目标语义等价”。

把 formal result 引入更强结论前，必须审计：

1. 量词顺序是否完全一致；
2. residual / forcing / correction 到底是固定为零、预先给定，还是允许存在量词选择；
3. 是否把局部极限偷换成全局恒等式；
4. 目标输出是否反向影响了 witness 的构造；
5. 是否没有 bridge theorem 就跨语义路线提升结论。

任何一项失败，都阻止该结果被提升到更强目标。

## 与项目底层逻辑的关系

本黑名单是 `FOUNDATIONAL_LOGIC.md` 与 `foundational_logic.json` 中“禁止把输出复制回输入”原则的一个具体特化。

第一个公开案例是 Navier–Stokes 逻辑审计：

- [`OPENAI_NS_F0_LOGIC_REBUTTAL.en.md`](OPENAI_NS_F0_LOGIC_REBUTTAL.en.md)
- [`OPENAI_NS_F0_LOGIC_REBUTTAL.zh-CN.md`](OPENAI_NS_F0_LOGIC_REBUTTAL.zh-CN.md)
