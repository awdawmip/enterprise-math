# R007 — 尺度相容完全幂坍缩 no-descent：第一阶段研究闭包

状态：`PROVED WIP / FIRST-STAGE HANDOFF / NOT CANONICAL`  
任务：`RS-R007-SCALE-COLLAPSE-DESCENT-NOGO`  
执行分支：`research/r007-scale-compatible-collapse-descent-nogo-20260810`  
Claim：`chatgpt-r007-20260810-1458`  
基线：`bbaf6478e8e6e8191f6b4ddd858f585148af4ae0`

## 0. 分层判决

本轮结论不是“Foundation contradiction”。更精确地：

1. **Arithmetic verdict**：对所有 `p,r>=2`，裸 `q_r(n)=floor(n/r)` 不能承载裸 `C_p(n)=R_p(n)^p` 的确定性 autonomous coarse future；存在无限 witness，coarse-future defect 无界。
2. **P009 verdict**：R007-T01 严格强于“指定 coarse 公式不交换”；P009-C02 本身不是 no-descent witness。
3. **P023 verdict**：因 `C_p` 幂等，`q_*=(q_r,q_r C_p)` 一步即闭合，而且是最粗的 `C_p`-compatible refinement。
4. **Information-loss verdict**：对这个算术族，最小 repair 在每个 `q_r` fiber 上至多增加 **1 bit**；并存在无限多 fiber，repair 后仍把 `r` 个 fine states 全部合并。
5. **Typed-scale verdict**：裸 `C_p` 不可能通过 P009 的非平凡整除投影自然下降；但存在简单、非平凡、严格自然的 scale-indexed replacement。
6. **Ontology verdict**：有限观察不逻辑推出有限本体；但 README 当前把有限本体写成项目的 hypothesis/wager，而不是由观察有限性推出的定理，因此本轮不构成 Foundation 反证。
7. **Physical verdict**：只排除满足 P016 四项联合声明的具体 specialization；宽泛有限分辨率/基本坍缩框架不因此被整体反证。

建议 Foundation 动作：`ADD NEGATIVE BOUNDARY + ADD SCALE-NATURAL CONSTRUCTOR/API`; 不改现有已证整数定理，不把 worldview hypothesis 改写成 theorem。

---

## 1. 定义

固定 `p>=2, r>=2`。令

\[
R_p(n)=\lfloor n^{1/p}\rfloor,\qquad
C_p(n)=R_p(n)^p,\qquad
q_r(n)=\left\lfloor\frac nr\right\rfloor.
\]

这里的 `R_p` 仅表示整数 `p` 次根；证明与回归均不依赖浮点。

记第 `a` 个 `q_r` fiber 为

\[
I_a=\{ar,ar+1,\ldots,ar+r-1\}.
\]

---

## 2. R007-T01/T02/T03：universal no-descent 与 exact defect

### 定理 2.1（裸 collapse 对所有非平凡 floor quotient 不可下降）

对任意 `p,r>=2`，不存在确定性映射 `G` 使

\[
q_r\circ C_p=G\circ q_r.
\]

### 证明

任取 `t>=1`，置

\[
y_t=(tr+1)^p,\qquad x_t=y_t-1.
\]

因为 `tr+1 ≡ 1 (mod r)`，故 `y_t ≡ 1 (mod r)`，从而

\[
q_r(x_t)=q_r(y_t).
\]

又因

\[
(tr)^p\le x_t<(tr+1)^p,
\]

有

\[
C_p(x_t)=(tr)^p,\qquad C_p(y_t)=(tr+1)^p.
\]

于是

\[
\begin{aligned}
\Delta_{p,r}(t)
&:=q_r(C_p(y_t))-q_r(C_p(x_t))\\
&=\frac{(tr+1)^p-1-(tr)^p}{r}\\
&=\sum_{i=1}^{p-1}\binom pi t^i r^{i-1}>0.
\end{aligned}
\]

同一 `q_r` fiber 上得到两个不同 coarse futures，故由 fiber-constant descent 判据不存在任何这样的 `G`。证毕。

### 边界

- `p=1` 时 `C_1=id`，可下降；
- `r=1` 时 `q_1=id`，平凡可下降。

因此对本族而言，no-descent 的精确非平凡区间就是 `p,r>=2`。

### 无界 defect

对 `t>=1`，最高次项给出

\[
\Delta_{p,r}(t)\ge p r^{p-2}t^{p-1}.
\]

又因 `t^i<=t^{p-1}`，

\[
\Delta_{p,r}(t)
\le
\left(\sum_{i=1}^{p-1}\binom pi r^{i-1}\right)t^{p-1}.
\]

故纯整数地得到

\[
\boxed{\Delta_{p,r}(t)=\Theta_{p,r}(t^{p-1})},
\]

特别地 defect 随 `t` 无界。`p=2` 时精确为 `Delta=2t`。

---

## 3. strict-action typed nuance：固定点 witness 不能偷换成合法严格 transition

P009 的 operational collapse 只在 `C_p(n)<n` 时记录严格 transition；上节总 endomap witness 的 `y_t` 是 perfect power，因此是 fixed point。

这不推翻 T01，但必须区分两种语义：

### 3.1 total endomap / future observable 语义

P023 讨论 `F:X->X` 时，fixed point 仍是合法 future value；上节证明直接成立。

### 3.2 strict partial action 语义

若把 collapse 解释为仅在 `D={n:C_p(n)<n}` 上可执行的 partial action，则精确 coarse autonomy 还要求**动作可用性本身**在 quotient fiber 上可判定。

- `r>=3`：令 `z=(tr+1)^p`，取 `x=z-1, y=z+1`。二者同属一个 `q_r` fiber，且二者都不是 perfect power，因此都严格可 collapse；但 coarse outputs 分别来自 `(tr)^p` 与 `z`，仍不同。
- `r=2`：边界 fiber 可同时含一个 strict-enabled state 与一个 perfect-power fixed/disabled state；因此 action domain 不是 `q_2`-fiber saturated。即使只看 enabled representatives 的输出，精确 typed legality 也不能只由 bare coarse state 决定。

所以 no-go 在 strict typed 语义下仍成立；只是 `r=2` 的最小 obstruction 首先表现为 **legality/domain mismatch**，而不是两个 enabled outputs 的冲突。

---

## 4. R007-T04：P009 nonconfluence 与 no-descent 不同

P009-C02 在 `p=2,r=2,n=3` 比较的是两条指定路径：

\[
q_2(C_2(3))=0,\qquad C_2(q_2(3))=1.
\]

这证明“选定 coarse operator 也取 bare `C_2`”时方块不交换。

但 `q_2` 的局部 fiber `{2,3}` 满足

\[
q_2(C_2(2))=q_2(C_2(3))=0,
\]

所以这个 fiber 上其实存在确定性 induced coarse value。故 C02 本身不是 no-descent witness。

R007-T01 更强：它给出 `q(x)=q(y)` 但 `qF(x) != qF(y)`，于是**任何** deterministic `G` 都不可能补上交换方块。

逻辑关系：

- no-descent `=>` 每一个候选 coarse `G` 都会在某处失败；
- 一个指定 `G` 的不交换 `!=>` no-descent；可能存在另一个 induced `G`；
- rewrite-system 的终态 nonconfluence 是路径/汇合性质，也不能与一步 factorization 失败同义化。

最小有限 no-descent 例：`X={0,1,2}`，`q(0)=q(1)=A,q(2)=B`，`F(0)=0,F(1)=2,F(2)=2`。

---

## 5. R007-T05：幂等 future 的一步最粗闭包

### 定理 5.1（一般幂等最小 repair）

设 `F:X->X` 幂等，`F^2=F`，`q:X->Q` 任意。定义

\[
q_*(x)=(q(x),q(Fx)).
\]

则：

1. `q_*` 对 `F` future-compatible；
2. `q_*` 是所有“细化 `q` 且对 `F` compatible”的 quotient 中最粗者；
3. refinement 一步闭合，不需要继续添加 `q(F^2x),q(F^3x),...`。

### 证明

若 `q_*(x)=q_*(y)`，则 `q(Fx)=q(Fy)`。而

\[
q_*(Fx)=(q(Fx),q(F^2x))=(q(Fx),q(Fx)),
\]

对 `y` 同理，故 compatible。

若 `s` 是任意细化 `q` 的 `F`-compatible quotient，且 `s(x)=s(y)`，则先有 `q(x)=q(y)`；compatible 又给 `s(Fx)=s(Fy)`，再由 `s` 细化 `q` 得 `q(Fx)=q(Fy)`。因此 `s(x)=s(y)` 必推出 `q_*(x)=q_*(y)`，即 `q_*` 最粗。幂等性同时给出一步闭合。证毕。

取 `F=C_p` 即得到 R007-T05。

---

## 6. R007-T06：本算术族的最小 repair **至多 1 bit**

令

\[
h(n)=q_r(C_p(n)).
\]

固定 fiber `I_a`，令 `k=R_p(ar)`。

### 定理 6.1（每个 floor fiber 上至多两个 future classes）

`h(I_a)` 的基数至多为 `2`。更精确地：

1. 若 `ar=k^p`，则对所有 `n in I_a`，`h(n)=a`；
2. 若 `ar` 不是 `p` 次幂，令 `z=(k+1)^p`：
   - 若 `z >= (a+1)r`，则 `h` 在整个 `I_a` 常值为 `b_a=q_r(k^p)<a`；
   - 若 `ar<z<(a+1)r`，令 `s=z-ar`，则
     \[
     h(n)=
     \begin{cases}
     b_a,& ar\le n<z,\\
     a,& z\le n<(a+1)r.
     \end{cases}
     \]

即使同一个 `I_a` 内出现多个 perfect powers，从第一个内部 perfect-power boundary 开始，所有后续 collapsed powers 仍落在同一 coarse block `a`，所以不会产生第三个 repair value。

因此 unsafe fiber 的精确判据是：`ar` 不是 perfect `p`-power，且第一个后继 `p` 次幂严格落在 `I_a` 内部。

### 规范 1-bit encoding

定义

\[
\beta_{p,r}(n)=\mathbf 1\{q_r(C_p(n))=q_r(n)\}.
\]

给定 `a=q_r(n)`：

- `beta=1` 时 `h(n)=a`；
- `beta=0` 时 `h(n)=b_a=q_r(C_p(ar))`。

所以

\[
(q_r(n),\beta_{p,r}(n))
\]

与 P023 的最小 repair

\[
(q_r(n),q_r(C_p(n)))
\]

诱导完全相同的 partition。故额外 repair alphabet 在每个 fiber 上最多为 2，worst-case 描述量最多 1 bit。

若在一个 unsafe fiber 上采用均匀 residue 模型、boundary split 为 `s` 与 `r-s`，条件 repair entropy 为二元熵

\[
H_2(s/r)\le1.
\]

### 关键反直觉

`Delta_{p,r}(t)` 可以无界增长，但最小 repair 信息仍最多 1 bit。原因是：defect 的**数值大小**可由 coarse index `a,p,r` 计算；真正缺失的只是“位于该 fiber 第一个 power boundary 的哪一侧”这一分支信息。

这否定“future ambiguity 数值越大就必须补回越多 fine identity”的朴素直觉。

---

## 7. R007-T10：最小 repair 后仍有真实信息删除

### 定理 7.1（无限多最大合并 fiber）

对任意 `p,r>=2,t>=1`，令

\[
z_t=(tr)^p,\qquad a_t=z_t/r=t^p r^{p-1}.
\]

由于

\[
(tr+1)^p-(tr)^p>r-1,
\]

整个 fiber

\[
I_{a_t}=\{z_t,z_t+1,\ldots,z_t+r-1\}
\]

都位于同一个 `C_p` basin 中。故对其中所有 `n`：

\[
q_r(n)=a_t,\qquad q_r(C_p(n))=a_t,\qquad \beta(n)=1.
\]

因此 `q_*` 在无限多 fiber 上仍然是 `r`-to-1。它没有恢复 `n mod r`，更没有恢复 fine state。

在均匀 residue 模型下，这些 fiber 的 repair 增量是 0 bit，而完整 residue 的 `log_2 r` bits 仍全部被擦除。

---

## 8. R007-T07：typed scale naturality obstruction

P009 对 `d|e`，写 `e=dr`，投影为

\[
\pi_{e\to d}(m)=\left\lfloor\frac mr\right\rfloor.
\]

若 fine scale 使用 bare `C_p`，而 coarse scale 想存在任意 autonomous deterministic `F_d` 使

\[
\pi_{e\to d}\circ C_p=F_d\circ\pi_{e\to d},
\]

这正是 T01 的 factorization 问题，因此对 `p,r>=2` 不可能。

结论比 `pi C_p != C_p pi` 更强：**不是 coarse 端公式选错，而是 bare projected state 根本不足以承载该 future。**

可选修复只有：细化 state、改 projection、限制 future language、允许非确定/非 autonomous coarse semantics，或把 dynamics 改成真正 scale-indexed natural family。

---

## 9. R007-T08：存在规范的非平凡 scale-compatible replacement

no-descent 不等于“所有 collapse 都无法跨尺度组织”。

### 定理 9.1（scale-relative natural lift）

给任意 base endomap `H:N->N`，定义

\[
F_d^H(m)=d\,H\!\left(\left\lfloor\frac md\right\rfloor\right).
\]

则对所有 `d|e` 都有严格自然性

\[
\boxed{
\pi_{e\to d}\circ F_e^H
=F_d^H\circ\pi_{e\to d}.
}
\]

### 证明

写 `e=dr`。则

\[
\pi_{e\to d}(F_e^H(m))
=\left\lfloor\frac{eH(\lfloor m/e\rfloor)}r\right\rfloor
=dH(\lfloor m/e\rfloor).
\]

另一方面利用整数 floor 复合恒等式，

\[
F_d^H(\pi_{e\to d}(m))
=dH\!\left(\left\lfloor\frac{\lfloor m/r\rfloor}{d}\right\rfloor\right)
=dH(\lfloor m/e\rfloor).
\]

证毕。

若 `H<=id`，则所有 `F_d^H<=id`；若 `H` 幂等，则所有 `F_d^H` 幂等。

取 `H=C_p`，得到

\[
\boxed{
C^{\mathrm{rel}}_{p,d}(m)
=d\,C_p\!\left(\left\lfloor\frac md\right\rfloor\right).
}
\]

它在 `d=1` 恢复 bare `C_p`，在任意尺度都 downward、idempotent、many-to-one，并对整个 divisibility scale category 严格自然。

### 规范性 / 部分唯一性

任意 natural family `F_d` 若 `F_1=H`，仅由 `d -> 1` 的自然性就被迫满足

\[
\left\lfloor\frac{F_d(m)}d\right\rfloor=H(\lfloor m/d\rfloor),
\]

所以必可写成

\[
F_d(m)=dH(\lfloor m/d\rfloor)+\rho_d(m),\qquad 0\le\rho_d(m)<d.
\]

若再要求 operation 在尺度 `d` **erase within-cell residue**，即 `F_d(m) ≡ 0 (mod d)`，则 `rho_d=0`，上面的 `F_d^H` 是唯一 natural lift。

因此 R007 的正确结论不是“scale-compatible collapse 不存在”，而是：**bare same-form collapse 不自然；scale-relative collapse 有一个非常简单的规范构造。**

---

## 10. `S_r`：bare quotient 真正允许哪些 arithmetic futures

定义

\[
\mathcal S_r=\{F:q_r(x)=q_r(y)\Rightarrow q_r(Fx)=q_r(Fy)\}.
\]

它包含 identity，且对 composition 闭合；等价地，每个 block `I_a` 的像必须完整落在某一个 coarse block 中。

若参数均为非负整数，则有以下 exact examples：

- 常值映射：safe；
- translation `T_t(n)=n+t`：safe 当且仅当 `r|t`；
- affine `cn+t`：除常值 `c=0` 外，只有 `c=1` 且 `r|t` safe；`c>=2` 不 safe；
- floor division `D_k(n)=floor(n/k)`：对每个 `k>=1` safe，induced map 为 `a -> floor(a/k)`；
- integer root `R_p`：对每个 `p>=1` safe，并且
  \[
  q_r(R_p(n))
  =R_p\!\left(\left\lfloor\frac{q_r(n)}{r^{p-1}}\right\rfloor\right);
  \]
- power `n -> n^p`：`p>=2,r>=2` 不 safe；
- bare `C_p=(\cdot)^p\circ R_p`：`p>=2,r>=2` 不 safe。

这给出一个结构性诊断：**root extraction 本身与 floor coarse state 相容；真正破坏 descent 的是把 coarse-safe root 再按原尺度 power-reembed 回去。**

---

## 11. ontology / README / P016 claim audit

### 11.1 epistemic-to-ontic 不蕴含

“观察只能以有限分辨率访问”并不逻辑推出“fine ontology 必须有限/离散”。反模型非常简单：取连续状态空间 `X=S^1`、可逆旋转 `T(x)=x+alpha mod 1`，再用有限 partition `q_m(x)=floor(mx)` 观察。观察 alphabet 有限，而 underlying ontology 连续且 fine dynamics 可逆。

因此以下推理无效：

`finite observational access => finite state ontology`。

这只是逻辑边界，不是新哲学定理。

### 11.2 对当前 README 的判决

当前 README 把“自然界基本有限分辨率/离散”明确放在 project belief / wager / ontological commitment 一侧，并区分物理事实与本体论承诺；本轮没有发现它把该信念伪装成由“人类观察有限”推出的数学 theorem。

故：`NO FOUNDATION CONTRADICTION`。建议只补一句防误读边界：有限观测本身不构成有限本体的证明。

### 11.3 P016-compatible conditional no-go

若一个具体物理 specialization 同时声明：

1. `q_r`（或等价 floor divisibility quotient）就是完整 coarse physical state；
2. quotient 丢掉的信息不以 repair/hidden state 保留；
3. 下一步 fundamental future language 允许 bare `C_p`；
4. coarse physics 应当 deterministic 且 autonomous；

则 T01 给出内部结构矛盾：同一个 coarse physical state 对同一个允许操作有两个不同 coarse futures。

这属于 P016 的“数学失败/模型内部不良定义”，甚至早于实验 kill test。

可逃逸修改均合法且必须显式声明：限制 future language；采用最小 repaired state；采用 scale-indexed natural dynamics；允许 stochastic/non-autonomous coarse closure；或把 bare `C_p` 仅作为证明工具而非 fundamental physical transition。

---

## 12. prior-art map（第一阶段，非穷尽）

本轮只做 ownership 边界，不作“搜不到即原创”的声明。

- **quotient/congruence descent / factorization**：一般的“映射在等价类上常值 iff 可通过 quotient factor”是标准数学；项目内部已由 P023 拥有，R007 不冒领。
- **partition refinement / bisimulation-style coarsest stable partitions**：Paige–Tarjan 1987 已把 coarsest relational partition 与高效 refinement 算法系统化。R007 的最小 refinement 语言与此同属成熟范式。
- **Markov lumpability / aggregation**：coarse projection 何时仍产生闭合 Markov dynamics 是成熟问题；例如 Ganguly–Petrov–Koeppl (2013, arXiv:1303.4532) 与 Geiger–Temmel (2012, arXiv:1212.4375) 讨论 lumpability/aggregation。R007 是 deterministic arithmetic specialization，不应把“coarse-graining may destroy autonomous dynamics”当新发现。
- **predictive state / minimal sufficient future state**：Shalizi–Crutchfield 的 computational mechanics 以 predictive equivalence 构造 minimal predictive representation（arXiv:cond-mat/9907176）。P023/R007 的“只保留 future language 所需信息”与之有明显概念亲缘，但对象和 theorem statement 不同。
- **naturality / projective-system compatibility**：尺度间交换图本身是标准 category/projective-system 语言；R007 可争取的内容只在这个特定 floor-divisibility / perfect-power 算术族的 exact theorem 与构造。

快速 exact-query prior-art 搜索未发现直接陈述本报告 `C_p`/`q_r` no-descent、无界 defect 或 1-bit repair 定理的文献；这**不能**当作 novelty proof。若要对外宣称新颖性，仍需专项文献检索。

潜在项目新增内容应严格限制为：

1. exact universal perfect-power/floor-quotient no-descent family；
2. exact defect polynomial 与整数增长界；
3. 每 fiber 至多 1-bit 的 exact minimal repair specialization；
4. 无限多 `r`-to-1 repaired fibers；
5. scale-relative natural lift `F_d^H=dH(floor(m/d))` 及 residue-erasing uniqueness；
6. 上述结果与 P009/P023/P016 的 typed integration。

---

## 13. Foundation Feedback Packet 候选

**不建议**：修改 P001–P015 已证算术定理；把 R007 写成“推翻有限精度世界观”；把 generic quotient descent 重新命名为项目新定理。

**建议**：

1. 在 P009 typed scale 文档增加 `NO BARE-DESCENT` negative boundary：typed labels 防止类型擦除，但不自动给 dynamics naturality。
2. 在 P023 增加 `IDEMPOTENT ONE-STEP REPAIR` specialization，并记录本算术族 repair alphabet `<=2`。
3. 新增 scale-natural constructor/API：
   \[
   F_d^H(m)=dH(floor(m/d)).
   \]
4. README/世界观 prose 只加防误读句：`finite observational access` 不是 `finite ontology` 的逻辑证明；后者若采用，是独立 hypothesis。
5. P016 增加本报告四条件 conditional structural no-go，归类为“具体 specialization 在实验前的数学失败”。

下一阶段优先级：Lean formalize T01/T02/T05/T07；扩展 `S_r` 可计算分类；检查 natural lift 的全 coherence/residue freedom；做更完整 prior-art novelty audit。
