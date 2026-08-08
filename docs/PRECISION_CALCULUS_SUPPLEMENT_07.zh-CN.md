# P018 —— 有限精度证明演算：补充 07

状态：`ACTIVE RESEARCH NOTE`  
范围：伴随投影的加法松弛、carry 2-cocycle、跨精度 coherence，以及对底层逻辑的候选反馈  
依赖：P005、P008、P009、P018 第一至第七阶段  
纪律：群上同调、factor set、群扩张、伴随与 lax monoidal 语言都是成熟数学；本文研究这些成熟结构与进取数论有限精度语义的精确接口，不把成熟结果据为项目原创。

## 1. 为什么 carry 现在值得上升一层

P018-T04 已经证明，对精度比 `r`，若

\[
x=ra+u,\qquad y=rb+v,\qquad 0\le u,v<r,
\]

则

\[
x+y=r(a+b+c)+t,
\]

其中

\[
c=(u+v)//r\in\{0,1\},
\qquad t=(u+v)\bmod r.
\]

此前这被解释为“细节共同改变粗层加法结果的精确事件”。这一解释仍然正确，但还不够底层。

P008 已证明：对尺度嵌入

\[
L_r(a)=ra
\]

与整数商

\[
Q_r(x)=x//r,
\]

有序关系上成立伴随

\[
L_r\dashv Q_r.
\]

而 `L_r` 又严格保持加法。于是一个更结构性的事实出现：**右伴随 `Q_r` 不严格保持加法；carry 恰好测量这种失配。**

本补充把这件事从“算术技巧”提升为可反复复用的 defect 结构，并检验它是否能成为 P008 之后的下一层基础。

---

## 2. P018-T63 —— 加法左伴随诱导右伴随的超加性

状态：`PROVED / ESTABLISHED ORDER-THEORETIC PATTERN`

设 `A,B` 为有序交换幺半群，加法对序单调。设

\[
l:A\to B
\]

严格保持加法，并存在右伴随

\[
l\dashv u.
\]

则对任意 `x,y\in B`，

\[
\boxed{u(x)+u(y)\le u(x+y).}
\]

### 证明

由伴随 counit 不等式，

\[
l(u(x))\le x,
\qquad l(u(y))\le y.
\]

加法单调且 `l` 保加法，因此

\[
l(u(x)+u(y))
=l(u(x))+l(u(y))
\le x+y.
\]

再由伴随等价

\[
l(a)\le b\iff a\le u(b)
\]

得到

\[
u(x)+u(y)\le u(x+y).
\]

∎

取 `l=L_r:a↦ra`、`u=Q_r:x↦x//r`，立刻得到

\[
\boxed{Q_r(x)+Q_r(y)\le Q_r(x+y).}
\]

所以 floor projection 的超加性不是孤立整数恒等式，而是 P008 伴随结构在加入加法以后自动产生的性质。

第一条底层反馈因此是：P008 的 order-adjoint core 不需要修改；但一旦状态空间还带有与尺度搬运相容的运算，右伴随投影会天然携带一个非严格的 operation-preservation 结构。

---

## 3. P018-T64 —— 加法 carry 是伴随松弛的精确整数缺口

状态：`PROVED`

对任意整数 `m>=1`，定义

\[
Q_m(x)=x//m,
\qquad \delta_m(x)=x\bmod m.
\]

写

\[
x=ma+u,
\qquad y=mb+v,
\qquad 0\le u,v<m.
\]

定义

\[
\boxed{\kappa_m(u,v)=\left\lfloor\frac{u+v}{m}\right\rfloor.}
\]

因为 `u+v<2m`，有 `kappa_m(u,v) in {0,1}`。于是

\[
\boxed{
Q_m(x+y)-Q_m(x)-Q_m(y)=\kappa_m(u,v).
}
\]

证明只需把 `x+y=m(a+b)+(u+v)` 再做一次欧几里得分解。

因此 carry 可以被严格定义为

\[
\boxed{\text{operation defect}=Q_m(x+y)-Q_m(x)-Q_m(y).}
\]

它是 coarse projection 偏离加法同态的**全部缺口**，没有隐藏余量。对 P018 的 degree-`q` 状态，只需取 `m=r^q` 即得到相同定理。

---

## 4. P018-T65 —— 标准 carry 满足归一化 2-cocycle 恒等式

状态：`PROVED / PRIOR-ART INSTANCE`

固定 `m>=1`，令

\[
D_m=\{0,1,\ldots,m-1\},
\]

并定义

\[
u\oplus v=(u+v)\bmod m.
\]

对

\[
\kappa_m(u,v)=\left\lfloor\frac{u+v}{m}\right\rfloor,
\]

有

\[
\boxed{
\kappa_m(u,v)+\kappa_m(u\oplus v,w)
=\kappa_m(v,w)+\kappa_m(u,v\oplus w).
}
\]

并且

\[
\kappa_m(0,u)=\kappa_m(u,0)=0,
\qquad \kappa_m(u,v)=\kappa_m(v,u).
\]

### 证明

由

\[
u+v=m\kappa_m(u,v)+(u\oplus v)
\]

先结合 `(u+v)+w` 与先结合 `u+(v+w)`，两边最终余数因模 `m` 加法结合而相同；欧几里得分解唯一，因此粗系数相等。∎

### 前人工作边界

“进位是一个 2-cocycle / factor set，并与群扩张相联系”是成熟数学。Daniel C. Isaksen 的 *A Cohomological Viewpoint on Elementary School Arithmetic*（American Mathematical Monthly, 2002, DOI `10.1080/00029890.2002.11919915`）明确从这一角度讨论小学进位算术。

因此 T65 的 cocycle 身份**不是进取数论原创**。项目真正要检验的是：这个成熟 cocycle 在 P005/P008/P018 的“有限精度是本体状态、粗化是多对一投影”语义中，是否能够统一描述更多 operation/refinement defects。

---

## 5. P018-T66 —— 粗状态 + detail + carry 精确重建整数加法

状态：`PROVED`

定义

\[
\Phi_m:\mathbb N\to\mathbb N\times D_m,
\qquad \Phi_m(x)=(Q_m(x),\delta_m(x)).
\]

由欧几里得分解，`Phi_m` 是双射，其逆为

\[
\Phi_m^{-1}(a,u)=ma+u.
\]

在 `N x D_m` 上定义扭曲加法

\[
\boxed{
(a,u)\boxplus(b,v)
=\bigl(a+b+\kappa_m(u,v),\ u\oplus v\bigr).
}
\]

则

\[
\boxed{\Phi_m(x+y)=\Phi_m(x)\boxplus\Phi_m(y).}
\]

所以

\[
\boxed{(\mathbb N,+)\cong(\mathbb N\times D_m,\boxplus).}
\]

这里右侧不是普通直积加法；正是 carry cocycle 把 coarse coordinate 与 detail coordinate 粘合起来。`boxplus` 的结合律正好由 T65 的 cocycle identity 保证。

第二条底层反馈因此是：若底层逻辑选择把有限精度状态拆成 coarse/detail 两层，那么跨层 carry 不能被当作实现噪声删除；删除它会改变代数本身。

---

## 6. P018-C07 —— 强迫投影成为严格加法同态会丢失真实结构

状态：`COUNTEREXAMPLE / DESIGN WARNING`

对任意 `m>1`，取

\[
x=1,\qquad y=m-1.
\]

则

\[
Q_m(1)=0,
\qquad Q_m(m-1)=0,
\]

但

\[
Q_m(m)=1.
\]

所以

\[
\boxed{Q_m(x+y)\ne Q_m(x)+Q_m(y).}
\]

如果未来把 precision system 形式化成某类代数对象之间的图，而要求所有 coarse projection 都严格保持加法，就会直接排除最基本的有限精度算术。

正确方向不是强迫 defect 消失，而是把 defect 明确建模。

---

## 7. P018-T67 —— 两级 precision chain 的 carry coherence

状态：`PROVED`

考虑两级精度比 `r,s>=1`。对 degree `q` 对象，记

\[
R=r^q,\qquad S=s^q.
\]

任意两个最细 detail 可唯一写成

\[
t_i=S u_i+v_i,
\qquad 0\le u_i<R,
\qquad 0\le v_i<S.
\]

定义最低 detail 层 carry

\[
c_S=\kappa_S(v_1,v_2).
\]

则跨总精度比 `RS` 的直接 carry 满足

\[
\boxed{
\kappa_{RS}(t_1,t_2)
=\left\lfloor\frac{u_1+u_2+c_S}{R}\right\rfloor.
}
\]

同时总余数满足

\[
\boxed{
(t_1+t_2)\bmod(RS)
=S\bigl((u_1+u_2+c_S)\bmod R\bigr)
+((v_1+v_2)\bmod S).
}
\]

### 证明

写

\[
v_1+v_2=Sc_S+w,
\qquad 0\le w<S.
\]

于是

\[
t_1+t_2=S(u_1+u_2+c_S)+w.
\]

再写

\[
u_1+u_2+c_S=Rc_R+z,
\qquad 0\le z<R.
\]

则

\[
t_1+t_2=RS c_R+Sz+w,
\]

且 `0<=Sz+w<RS`，由唯一欧几里得分解得到两式。∎

这说明**直接粗化**和**逐层粗化**并不会产生互相矛盾的 carry；低层 carry 会作为整数输入传给上一层，再由上一层决定是否继续越界。

因此 P018-T02 的 nested detail composition 与 T65 的 cocycle 共同形成有限精度链上的 coherence 条件。

---

## 8. 从单一 carry 推广到 operation defect

加法最干净，因为 defect 只有 `0/1`，并直接形成标准 2-cocycle。

但 P018 已经证明：

- 乘法有 `C_times`；
- 幂映射有 `C_p^prec`；
- collapse/refinement commutation defect 就是根状态上的幂 carry；
- 一般非负齐次单项式具有有界整数 naturality defect。

所以新的统一问题不是“所有 defect 都是不是同一个 cocycle”。这种说法目前没有证明，而且很可能过强。

更稳健的路线是定义

\[
\boxed{
D_f^{e:d}(x)
=\pi^{out}_{e\to d}(f_e(x))
-f_d(\pi^{in}_{e\to d}(x)),
}
\]

前提是右侧在相应有序整数对象中有定义，然后分别研究：

1. `D_f=0`：运算与 precision projection 严格自然；
2. `D_f` 非零：非严格自然性的精确有限 defect；
3. 复合运算的 defect 如何组合；
4. 多级 precision chain 中 direct defect 与 staged defects 的 coherence；
5. 哪些 defect 是 cocycle，哪些属于更高或不同类型的结构。

原则是：**先证明 defect law，再决定使用哪一种成熟数学语言，不反过来为了套上“上同调”而改造对象。**

---

## 9. 对 P008 的反馈：形成两层基础，而不是推翻既有核心

P008 当前结论仍保持：对 root / quotient / collapse 的 v0.1 核心，partial order + order embedding + right adjoint 已经足够。

本补充增加的是第二层。

### Layer 0 —— Order-adjoint core

\[
\boxed{
\text{partial order}
+\text{order embedding}
+\text{right adjoint}
}
\]

解释根、商、精确恢复与 interior/collapse。

### Layer 1 —— Defect-enriched operation core

当具体问题还需要加法、乘法或其他运算时，不要求粗投影成为严格同态，而增加

\[
\boxed{
\text{typed operation}
+\text{precision projection}
+\text{exact operation defect}
+\text{coherence law}.
}
\]

“最小基础”因此不是把所有未来运算一次塞进 P008，而是形成按需要逐层扩张的底层。这与 P008“更强结构必须逐个运算证明其必要性”的纪律一致。

---

## 10. 对 P005/P009 的反馈：尺度箭头必须继续带类型

P009 已经证明，擦掉尺度标签会制造假的动力学。T67 进一步说明，carry coherence 也依赖明确知道每一级的精度比与 degree。

所以未来任何 cohomology / defect 语言都不能把状态退化成“同一个无类型整数集上的自映射”。合理对象至少需要记录 `(d,x,q)` 或等价类型信息，其中 `d` 是 precision/scale，`x` 是该层显式整数状态，`q` 是尺度次数，箭头只在类型匹配时允许作用。

---

## 11. 对 P012 的反馈：保留图几何，同时增加 quotient/fiber 几何路线

P012 第一阶段已经证明：原子邻接生成的最短路自然数距离是完整的内生整数度量。这个成果不应被替换。

新的方法层只增加第二条并行路线：

1. **primitive-step geometry**：原子关系 → graph/word metric；
2. **fiber/quotient geometry**：precision partition / congruence / coset → 状态之间的可区分代价；
3. **exact lattice lift**：当有限代数问题能无损嵌入整数格时，把格作为证明表示空间，而不是预设物理欧氏底层。

尤其继续保留 P012-C01 的边界：平方欧氏距离虽然整数值，却不是一般度量；“integer-valued”本身不能替代几何公理。

---

## 12. 对 P017 的反馈：从逐项好符号转向整体 certificate，但保留原路线

P017 已经形成 bulk / carry / shell / half-scale / threshold-complex / duality 等多条线。本补充不删除 involution、pairing 或逐项相消路线，而增加一个更上层的问题：

> 即使局部 shell 或 carry 项带符号，是否存在定义在整个有限 precision hierarchy 上的整数 potential / dual witness / certificate，使目标不等式由整体约束推出？

优先尝试：

1. **partition potential**：由 ambiguity/conflict multiplicity 的跨层变化构造；
2. **shell certificate**：允许局部负项，但要求相关 precision shells 的特定线性组合满足全局界；
3. **defect budget**：把 carry、Möbius shell、half-scale dual correction 看成同一有限证明中的不同 defect 账户，证明总预算不越过阈值。

如果全局 certificate 失败，失败本身应告诉我们必须保留哪些局部结构，而不是宣布旧路线无效。

---

## 13. Representation switch：允许换证明语言，不允许偷换本体

进取数论的本体选择是有限整数状态与显式精度；这不意味着证明工具只能来自初等整数算术。

正式采用以下研究纪律：

\[
\boxed{
\text{finite-state problem}
\xrightarrow{\text{faithful representation}}
\text{other mathematical language}
\xrightarrow{\text{proof}}
\text{finite-state theorem}.
}
\]

允许作为证明语言使用 group cohomology、category/adjunction/lax structure、algebraic geometry、harmonic/spectral methods、convex duality、topology/homology、lattice theory、finite-field coding、functional/analytic estimates，但必须满足：

1. representation map 明确；
2. 需要的 faithful / injective / equivalence 性质被证明；
3. 最终结论可以翻译回原有限状态；
4. 不把证明空间中的连续体自动提升成自然本体。

这使“换表示空间”成为正式方法，而不是路线漂移。

---

## 14. 候选底层骨架：Defect-Enriched Precision System

状态：`RESEARCH SYNTHESIS / NOT FROZEN`

结合 P005、P008、P009、P010、P012、P018，目前出现一个候选骨架：

### A. Typed finite states
每一级拥有显式状态空间 `X_lambda`，精度/尺度标签属于状态类型。

### B. Compatible forgetting / projection
更细 observation 到更粗 observation 有规范 projection，并满足路径 coherence。

### C. Order-adjoint core where available
对 root/quotient/collapse 等结构，继续使用 P008 的 embedding/right-adjoint 核心。

### D. Defect-enriched operations
运算不被要求在 projection 下严格自然；偏离严格交换的有限量本身成为第一等数学对象：

\[
D_f=\pi f-f\pi.
\]

### E. Coherence instead of artificial exactness
多级 precision 的要求不是“每一步 defect=0”，而是 direct route 与 staged route 的 defects 满足可证明的 coherence law。

### F. Proof layer
使用 P018 的 ambiguity、predicate conflict、certificate 与 adaptive precision，决定哪些 detail 对目标命题真正必要。

### G. Time layer
继续保留 P010/P018-T44：precision refinement 细化 partition，而 deterministic forward time 粗化 partition。二者共享有限状态 partition 骨架，但目前不宣称 categorical duality。

其关键词不是“连续逼近”，而是

\[
\boxed{
\text{finite state}
+\text{typed precision}
+\text{many-to-one projection}
+\text{exact defect}
+\text{coherence}
+\text{finite proof certificate}.
}
\]

它比单独的 integer root 更接近可反哺底层逻辑的框架，但现在仍不应封板。

---

## 15. 下一阶段可证伪问题

### P018-Q63 —— 哪些 operation defect 真正形成 cocycle？
加法 carry 已经是标准 2-cocycle。对乘法、幂、collapse/refinement defect，不预设答案；寻找正确 coefficient object 与组合律，或给出反例证明“统一 cocycle”过强。

### P018-Q64 —— 一般 adjoint + algebra 的最弱结构是什么？
T63 在有序交换幺半群上成立。继续削弱假设：哪些地方真正需要交换、单位元、全加法、antisymmetry？目标是找到与 P008 相同风格的最小结构结果。

### P018-Q65 —— 多路径 precision diamond 的 defect coherence
P005 已证明纯 projection 的 gcd/lcm diamond 严格交换。加入 operation 后，研究四条边上的 defect 是否满足精确 diamond identity；这可能比单链 T67 更接近真正的“precision curvature”。

### P018-Q66 —— defect curvature 是否存在？
若两个不同 precision 路径在 projection 本身上同终点，但 operation-defect 的分解不同，研究两种 defect transport 的差是否为零；若不为零，定义并分类有限 path defect。不要预设它一定是曲率或上同调类。

### P018-Q67 —— global certificate 是否能推进 P017？
构造至少一个非平凡整数 potential，使其同时看到 factor precision、carry shell 与 half-scale dual correction；若构造失败，给出最小反例并确定缺失状态坐标。

### P018-Q68 —— representation switch 的充分条件
给出有限问题到外部数学表示 `F:X->Y` 的最小 proof-safe 条件：什么情况下 `Y` 中的定理能够无歧义拉回 `X`？优先比较 injective embedding、predicate-complete quotient 与 equivalence 三种强度。

---

## 16. Lean 形式化优先级

下一轮形式化建议按以下顺序：

1. T64：`Nat.div` / `Nat.mod` 下 carry gap 恒等式；
2. T65：carry cocycle identity；
3. T66：`Phi_m` 的 coarse/detail 双射与 twisted addition；
4. T67：两级 carry coherence；
5. T63：抽象 ordered additive monoid + Galois connection 版本。

形式化目的不是给成熟 carry cocycle 贴项目标签，而是验证：我们把它嵌入 P005/P008/P018 时没有因类型、零值、degree 或投影方向犯错。

---

## 17. 当前结论

本阶段没有把新的强公理塞进 P008，也没有删除 P012/P017/P018 的任何既有路线。

得到的最重要结构性结果是

\[
\boxed{
\text{carry}
=\text{right-adjoint projection 的加法松弛缺口}
=\text{coarse/detail 重建加法所需的 2-cocycle 数据}.
}
\]

这说明“有限精度造成的非严格交换”本身可能不是需要消灭的误差，而是底层数学必须保存的结构。

当前最值得继续检验的统一方向是

\[
\boxed{
\text{order adjunction}
\longrightarrow
\text{typed precision projection}
\longrightarrow
\text{exact operation defect}
\longrightarrow
\text{coherence}
\longrightarrow
\text{proof certificate / time dynamics}.
}
\]

它现在是候选底层骨架，不是已封板的新基础。