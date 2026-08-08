# P018 —— 有限精度证明演算：补充 09

状态：`ACTIVE RESEARCH NOTE`  
范围：mixed-radix 精度坐标图、radix-swap 转换、braid coherence、P005 菱形细节结构，以及真正 precision curvature 的边界  
依赖：P005、P009、P018-T02、T43、T63—T73  
纪律：mixed-radix arithmetic、欧几里得分解、坐标转换、braid/coherence 语言均有成熟前人背景。本文研究它们在进取数论有限精度投影系统中的组合与基础含义，不主张这些成熟结构本身为项目原创。

## 1. 问题：P005 的菱形只证明了 coarse projection 交换，那么 detail 呢？

P005 已经证明：若

\[
d\mid e\mid f,
\]

则规范粗投影满足

\[
\pi_{f\to d}
=
\pi_{e\to d}\circ\pi_{f\to e}.
\]

更一般地，在 gcd/lcm 精度菱形上，两条 coarse path 到同一端点严格相同。

P018-T02 又证明：沿单条链，细状态可以被唯一分解成嵌套 detail。

于是一个此前没有单独写清的问题出现：

> 当同一个总精度差可以沿不同因子顺序逐层分解时，两条路径产生的 detail 坐标怎样对应？

答案不是“每一级 detail 应该逐坐标相等”。它们通常不相等。

更准确的结构是：**不同 refinement path 给同一个有限 detail fiber 提供不同的 mixed-radix 坐标图；坐标图之间存在规范、无损、纯整数的 transition map。**

---

## 2. P018-T74 —— 两级 mixed-radix detail chart 是双射

状态：`PROVED / ESTABLISHED ARITHMETIC`

令 `r,s>=1`，定义有限 detail fiber

\[
D_n=\{0,1,\ldots,n-1\}.
\]

对任意

\[
t\in D_{rs},
\]

唯一写成

\[
\boxed{t=su+v,}
\]

其中

\[
0\le u<r,
\qquad0\le v<s.
\]

因此定义 chart

\[
\boxed{
\chi_{r,s}:D_{rs}\to D_r\times D_s,
\qquad
\chi_{r,s}(t)=(t//s,t\bmod s).
}
\]

其逆为

\[
\boxed{
\chi_{r,s}^{-1}(u,v)=su+v.
}
\]

所以

\[
\boxed{D_{rs}\cong D_r\times D_s}
\]

作为有限集合严格成立。

这里没有把 detail 解释成隐藏真值。`D_{rs}` 与 `(u,v)` 都是显式有限状态的两种等价坐标表达。

---

## 3. P018-T75 —— radix swap 是规范无损坐标变换

状态：`PROVED`

同一个 `t in D_(rs)` 也可以按相反顺序写成

\[
t=ru'+v',
\qquad0\le u'<s,
\qquad0\le v'<r.
\]

定义 chart transition

\[
\boxed{
\tau_{r,s}
=
\chi_{s,r}\circ\chi_{r,s}^{-1}.
}
\]

于是对 `(u,v) in D_r x D_s`，

\[
\boxed{
\tau_{r,s}(u,v)
=
\left(
\frac{su+v}{r}\Big\rfloor,
(su+v)\bmod r
\right).
}
\]

更明确写成整数商：

\[
\boxed{
\tau_{r,s}(u,v)
=
((su+v)//r,(su+v)\bmod r).
}
\]

它是双射，而且

\[
\boxed{
\tau_{s,r}\circ\tau_{r,s}
=\operatorname{id}_{D_r\times D_s}.
}
\]

### 含义

两种 refinement path 的 detail 不需要逐坐标一致；真正必须保持的是：

1. 二者编码同一个 total detail；
2. transition 可逆；
3. transition 不引入连续补值或隐藏余量。

所以“多路线并存”现在有一个严格数学表达：

\[
\boxed{
\text{同一有限 fiber}
+\text{多套整数 chart}
+\text{规范 chart transition}.
}
\]

---

## 4. P018-T76 —— 三因子 radix swap 满足 braid coherence

状态：`PROVED`

令 `r,s,t>=1`，从三位 mixed-radix detail

\[
(a,b,c)\in D_r\times D_s\times D_t
\]

开始。其编码整数为

\[
\boxed{N=st\,a+t\,b+c,}
\]

满足 `0<=N<rst`。

考虑把 radix 顺序从

\[
(r,s,t)
\]

变到

\[
(t,s,r).
\]

有两条相邻 swap 路径：

\[
(r,s,t)
\to(s,r,t)
\to(s,t,r)
\to(t,s,r),
\]

以及

\[
(r,s,t)
\to(r,t,s)
\to(t,r,s)
\to(t,s,r).
\]

用 `tau` 表示相邻 radix swap，则严格有

\[
\boxed{
(\tau_{s,t}\times id_r)
\circ
(id_s\times\tau_{r,t})
\circ
(\tau_{r,s}\times id_t)
=
(id_t\times\tau_{r,s})
\circ
(\tau_{r,t}\times id_s)
\circ
(id_r\times\tau_{s,t}).
}
\]

### 证明

每一个相邻 swap 都保持编码整数 `N` 不变，只改变 radix 顺序下的坐标表示。

两条路径最终都得到 radix 顺序 `(t,s,r)` 下对同一个 `N` 的 mixed-radix 表示。该表示由重复欧几里得分解唯一，因此两条路径终点坐标相同。∎

### 边界

这是一个 braid/coherence 形式的恒等式。本文不主张 mixed-radix swap 或 braid relation 是新发明。

项目相关的新用途是：**把不同精度分解路线之间的一致性从“应该差不多”提升为严格的坐标图 coherence 条件。**

---

## 5. P018-T77 —— P005 gcd/lcm 菱形具有规范 detail atlas

状态：`PROVED`

考虑 P005 的尺度菱形。令

\[
g=\gcd(a,b),
\qquad
\ell=\operatorname{lcm}(a,b).
\]

写

\[
a=gA,
\qquad b=gB.
\]

则经典整数关系给出

\[
\gcd(A,B)=1,
\qquad
\ell=gAB.
\]

固定一个从精度 `ell` 投到 `g` 的 total detail

\[
t\in D_{AB}.
\]

### 路径一：`ell -> a -> g`

两级 ratio 依次为 `B` 与 `A`，对应 chart

\[
\chi_{A,B}(t)
=(t//B,t\bmod B).
\]

### 路径二：`ell -> b -> g`

两级 ratio 依次为 `A` 与 `B`，对应 chart

\[
\chi_{B,A}(t)
=(t//A,t\bmod A).
\]

两套 detail 坐标由

\[
\boxed{
\tau_{A,B}
=
\chi_{B,A}\circ\chi_{A,B}^{-1}
}
\]

规范连接。

所以 P005 菱形现在可以分成两层理解：

\[
\boxed{
\text{coarse coordinate：严格交换；}
}
\]

\[
\boxed{
\text{detail coordinate：不要求相同，但由可逆 chart transition 精确连接。}
}
\]

这比要求“所有路径都给出同一组局部 detail”更正确，也更能保留多路线信息。

---

## 6. P018-T78 —— 加法 carry 在 precision diamond 上是 flat 的

状态：`PROVED`

固定 `r,s>=1`，令两个 total details

\[
t_1,t_2\in D_{rs}.
\]

直接从 product radix `rs` 投到粗层，加法 carry 为

\[
\boxed{
K_{dir}
=\kappa_{rs}(t_1,t_2)
=\left\lfloor\frac{t_1+t_2}{rs}\right\rfloor.
}
\]

### 通过 `(r,s)` chart

写

\[
t_i=su_i+v_i,
\qquad u_i\in D_r,
\quad v_i\in D_s.
\]

先产生内层 carry

\[
c_s=\kappa_s(v_1,v_2),
\]

再把它送入外层：

\[
K_{r,s}
=
\left\lfloor
\frac{u_1+u_2+c_s}{r}
\right\rfloor.
\]

P018-T67 已给出

\[
K_{r,s}=K_{dir}.
\]

### 通过 swapped `(s,r)` chart

同理得到

\[
K_{s,r}=K_{dir}.
\]

因此

\[
\boxed{
K_{r,s}
=K_{s,r}
=K_{dir}.
}
\]

这意味着：局部 carry 在两条路线上的**分布位置**可以不同，但把它按正确 chart/coherence 规则运输到共同端点后，最终 defect 完全相同。

若把加法的 diamond curvature 暂定义为两条规范路径最终 transported defect 的差，则

\[
\boxed{\Omega_+(r,s;t_1,t_2)=0.}
\]

所以 addition carry 是一个非零 defect，但 canonical precision connection 对它是 flat 的。

这是一个重要负结论：

> **defect 非零不等于 curvature 非零。**

---

## 7. P018-T79 —— canonical endpoint defect 的路径曲率自动为零

状态：`PROVED STRUCTURAL BOUNDARY`

考虑任意 compatible precision system，其中从 finer level `lambda` 到 coarser level `mu` 的规范 projection 只依赖端点，满足所有路径复合都等于同一个

\[
\pi_{\lambda\to\mu}.
\]

若某个 operation `F` 在两个端点均已定义，并把 endpoint defect 定义为

\[
D_F^{\lambda:\mu}(x)
=
\pi^{out}_{\lambda\to\mu}(F_\lambda(x))
-
F_\mu(\pi^{in}_{\lambda\to\mu}(x)),
\]

那么 `D_F^{lambda:mu}` 本身只依赖端点。

因此，对两条拥有相同起终点、且都仅使用 canonical projection 的路径，所谓“endpoint defect path difference”必为零。

### 证明

两条路径的复合 projection 按假设都等于同一个端点 projection。代入 defect 定义后，两边表达式完全相同。∎

### 这排除了什么？

不能仅仅因为局部 defect 分解不同，就把差异叫作“precision curvature”。那可能只是不同 chart 的坐标分布。

### 真正非零 curvature / holonomy 从哪里可能出现？

至少需要引入某种额外路径依赖结构，例如：

1. **中间 operation scheduling 不同**：先 collapse 再 project 与先 project 再 collapse；
2. **非规范 lift / reconstruction**：从 coarse fiber 选择不同 representative 回到 fine level；
3. **operation 本身随路径改变**：不同尺度路径使用不同局部 transition；
4. **非平凡 transport rule**：局部 defect 的搬运不是 canonical endpoint projection 的直接结果。

这正好把研究焦点从纯 P005 scale lattice 移到 P009 已经揭示的 typed nonconfluence、以及 P018 中 operation/projection 不交换的结构。

---

## 8. 对 P009 的反哺：真正的 holonomy 候选在 operation scheduling，而不在纯尺度

P009 已经强调：擦掉尺度标签会制造假的动力学；不同 operation/projection 顺序也可能给出不同结果。

T79 现在把路线边界划得更清楚：

- **纯 canonical scale refinement/coarsening**：flat，路径只改变 detail chart；
- **加入非交换 operation 后**：才可能出现真实的 path effect。

因此下一阶段不应该直接给 scale lattice 添加“曲率”原语。

更合理的对象是一个带 operation labels 的路径：

\[
\boxed{
\text{typed precision arrows}
+\text{operation events}
+\text{chart transitions}.
}
\]

然后比较两条拥有相同初始/最终类型、但 operation ordering 不同的路径是否得到同一状态。

若不同，再研究其差是否满足：

- 可组合；
- 可局部化；
- 在合法 chart change 下保持不变量；
- 能否形成真正的 holonomy / obstruction。

这比在纯 projection 上强行寻找曲率更不容易走偏。

---

## 9. 对“保持所有路线”的数学化

目前“不要断线、保持路线”可以不再只作为项目管理口号，而提升成研究原则。

对同一个有限对象，如果多条路线满足：

1. 每条路线对应一个明确 representation/chart；
2. chart 之间存在可验证 transition；
3. transition 满足 composition / braid coherence；
4. 真正的结论在 chart change 下不变；

那么这些路线就应该**并行保留**，而不是过早选一个“最好表示”删除其他路线。

只有当两条路线连这种 chart-equivalence 都不存在，或者它们对同一结构给出不可协调的可验证预测时，才进入真正的竞争/淘汰。

这与 Supplement 08 的 defect-equivalence 原则完全一致：

\[
\boxed{
\text{路线差异}
\ne
\text{结构差异}.
}
\]

先寻找 transition law，再判断是否真的冲突。

---

## 10. 对底层逻辑的第四层候选反馈

结合 Supplement 07–09，候选基础现在更像一个**有限精度 atlas system**，而不仅是一组整数运算。

### Layer 0 —— Order-adjoint core

P008：partial order + embedding + right adjoint。

### Layer 1 —— Defect-enriched operation core

projection 不必严格保持 operation；记录 exact defect 与 coherence。

### Layer 2 —— Defect equivalence / obstruction

记录 representation change、coboundary-like transformation、strictification obstruction。

### Layer 3 —— Precision atlas / path coherence

同一 finite detail fiber 允许多套 chart；要求规范 transition、逆、组合与 braid coherence，并区分：

- chart-dependent local data；
- chart-invariant endpoint data；
- operation-induced genuine path dependence。

当前候选底层骨架因此可写成：

\[
\boxed{
\text{typed finite states}
+\text{adjoint projections}
+\text{finite detail fibers}
+\text{chart atlas}
+\text{exact defects}
+\text{coherence}
+\text{obstruction classes}
+\text{proof/time layers}.
}
\]

仍然不封板。

---

## 11. 可执行压力测试

新增：

- `src/enterprise_math/precision_radix.py`
- `tests/test_precision_radix.py`

它们只使用整数运算，并穷举小有限域验证：

1. split/join mixed-radix chart 互逆；
2. `tau_(r,s)` 与 `tau_(s,r)` 互逆；
3. 三因子相邻 radix swap 满足 braid 两路一致；
4. staged carry 与 product-radix direct carry 一致；
5. swapped diamond 两条路径最终 carry 一致。

计算检查是反例搜索与实现验证，不替代理论证明。

---

## 12. 下一阶段开放问题

### P018-Q74 —— 抽象 finite precision atlas

把 `D_(rs) <-> D_r x D_s` 从整数特例抽象成有限 fiber atlas。需要多弱的结构才能定义 chart、transition 与 coherence？

### P018-Q75 —— radix braid 的 Lean 形式化

先形式化 T74–T76，尤其验证参数化相邻 swap 的 braid identity。

### P018-Q76 —— operation-scheduling holonomy

选择目前已有的最小非交换例子，例如 collapse 与 projection，构造两个 typed path：

\[
\text{collapse}\to\text{project}
\qquad\text{vs}\qquad
\text{project}\to\text{collapse},
\]

定义共同端点上的 exact path defect，并检查其在 chart change 下如何变换。

### P018-Q77 —— holonomy 是否满足局部组合律

若 Q76 得到非零 path effect，研究它沿串联菱形是否可加、可复合，还是需要非阿贝尔 transport。

### P018-Q78 —— P017 分解 atlas

把 P017 的 anchor、carry/shell、half-scale、factor-precision 等不同表示尝试组织成 chart family，寻找 transition law；若不存在，则明确哪些路线真正在表达不同结构。

---

## 13. 当前结论

本阶段最重要的不是又增加一个术语，而是排除了一个容易走偏的方向：

\[
\boxed{
\text{纯 canonical precision projection 本身没有非零 path curvature。}
}
\]

不同 refinement path 的 detail 差异首先应理解为 mixed-radix chart change；这些 chart transition 是可逆的，并具有严格 braid coherence。

因此真正值得继续寻找的非零 path obstruction 必须来自：

\[
\boxed{
\text{operation/projection noncommutation}
\quad\text{或}\quad
\text{noncanonical lift/transport}.
}
\]

这使底层逻辑进一步收敛：

> **保留多路线，但先把路线组织成 atlas；只有经过合法 chart transition 后仍无法消去的差异，才有资格被提升为真正的结构障碍。**