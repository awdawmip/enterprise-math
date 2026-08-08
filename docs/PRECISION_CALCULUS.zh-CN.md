# P018 — 有限精度证明演算

状态：`ACTIVE RESEARCH NOTE`  
Issue：`P018 / #34`  
范围：把有限精度提升为数学中的一等坐标  
纪律：**这里的精度不是围绕某个隐藏实数真值附加的误差条。**

## 1. 研究主张

进取数论从有限数值状态出发。一个精细状态可以投影到较粗精度，但该投影是多对一的。因此，提高精度不是“找回唯一隐藏真值”，而是暴露新的有限状态信息。

P018 研究这种信息变化本身的代数和证明论。

核心模式是

\[
\boxed{
\text{细状态}
=
\text{搬运后的粗状态}
+
\text{有界精度细节}.
}
\]

接下来研究：

- 什么命题可以在低精度上完成证明，而且以后继续提高精度也不会推翻？
- 当低精度部分相同时，能否把它们严格消去，只把证明义务交给新增精度层？
- carry / borrow 如何在相邻精度层之间传递信息？
- 哪些运算与精度投影交换；若不交换，其缺陷能否本身成为精确有限状态？

核心构造不要求 `d -> infinity` 极限。

## 2. 精度尺度

使用正整数精度因子，并以整除关系排序：

\[
d\preceq e
\iff d\mid e.
\]

当 `d|e` 时，写

\[
r=e/d.
\]

把精度 `e` 上的整数状态 `x` 规范投影到精度 `d`：

\[
\pi_{e\to d}(x)=x\operatorname{//}r.
\]

定义其**精度细节**：

\[
\delta_{e:d}(x)=x\bmod r.
\]

这是把欧几里得除法当作状态分解，而不是近似定理。

## 3. P018-T01 — 精度纤维分解

状态：`PROVED`

对任意 `d|e` 与 `x in N`，

\[
\boxed{
x
=r\pi_{e\to d}(x)+\delta_{e:d}(x),
\qquad
0\le\delta_{e:d}(x)<r.
}
\]

二元组

\[
\bigl(\pi_{e\to d}(x),\delta_{e:d}(x)\bigr)
\]

唯一。

因此粗状态 `a` 的完整投影纤维恰为

\[
\{ra,ra+1,\ldots,ra+r-1\}.
\]

这里并不主张 detail 在一次物理坍缩后仍作为隐藏变量存在；只有当两个精度状态都被显式讨论时，detail 才是它们之间的精确关系。

## 4. P018-T02 — 嵌套精度细节复合

状态：`PROVED`

设

\[
d\mid e\mid f,
\qquad
r=e/d,
\qquad
s=f/e.
\]

对精度 `f` 上的状态 `x`，令

\[
u=\delta_{e:d}(\pi_{f\to e}(x)),
\qquad
v=\delta_{f:e}(x).
\]

则

\[
\boxed{
\delta_{f:d}(x)=s u+v.
}
\]

证明：写成

\[
\pi_{f\to e}(x)=ra+u,
\qquad
x=s(ra+u)+v.
\]

于是

\[
x=rs a+(su+v),
\]

且 `0<=su+v<rs`。∎

这是**嵌套精度 detail** 的第一个精确形式：旧 detail 被搬运到更高层，下一层只增加新的有限余数。

## 5. P018-T03 — 粗精度序证明稳定性

状态：`PROVED`

设 `d|e`，`x,y` 为精度 `e` 上两个显式状态。

若

\[
\pi_{e\to d}(x)<\pi_{e\to d}(y),
\]

则

\[
\boxed{x<y.}
\]

若粗商为 `a<b`，则

\[
ra+u\le ra+r-1<r(a+1)\le rb\le rb+v.
\]

所以：一旦低精度已经把两个状态分到不同 coarse fiber，后续解析各自内部的更细 detail 永远无法推翻这个严格大小关系。

反之，若

\[
\pi_{e\to d}(x)=\pi_{e\to d}(y),
\]

则公共粗项严格相消，并且

\[
\boxed{
x<y
\iff
\delta_{e:d}(x)<\delta_{e:d}(y).
}
\]

因此序关系形成一个真正的有限精度证明规则：

1. 先比较粗纤维；
2. 若已分离，证明永久完成；
3. 若仍在同一纤维，消去公共粗状态，把证明义务下放给 detail 层。

这就是 P018 中“逐步提高精度完成证明”的第一个严格含义。

## 6. P018-T04 — 跨精度加法 carry

状态：`PROVED`

写

\[
x=ra+u,
\qquad
y=rb+v,
\qquad0\le u,v<r.
\]

定义

\[
c=(u+v)\operatorname{//}r,
\qquad
t=(u+v)\bmod r.
\]

由于 `u+v<2r`，

\[
c\in\{0,1\}.
\]

于是

\[
\boxed{
x+y=r(a+b+c)+t.}
\]

等价地，

\[
\boxed{
\pi(x+y)=\pi(x)+\pi(y)+c.
}
\]

层间 carry `c` 不是数值误差，而是两个细节共同改变粗层运算结果的精确事件。

## 7. P018-T05 — 跨精度减法 borrow

状态：`PROVED`

设 `x>=y`，写

\[
x=rA+u,
\qquad
y=rB+v,
\qquad0\le u,v<r.
\]

定义

\[
b=\mathbf 1_{u<v}.
\]

则

\[
\boxed{
\pi(x-y)=A-B-b,
}
\]

并且

\[
\boxed{
\delta(x-y)=u-v+br.
}
\]

因此 borrow 是 precision carry 在减法中的对偶形式。

## 8. P018-T06 — 精度链望远镜分解

状态：`PROVED`

设

\[
d_0\mid d_1\mid\cdots\mid d_m
\]

并令 `x_i` 为同一个最终状态 `x_m` 投影到精度 `d_i` 的结果。

写

\[
x_i=(d_i/d_{i-1})x_{i-1}+\delta_i.
\]

则

\[
\boxed{
x_m
=\frac{d_m}{d_0}x_0
+\sum_{i=1}^{m}\frac{d_m}{d_i}\delta_i.}
\]

所有量都是整数。

这是一个有限 mixed-radix / telescoping 证明分解。若两个表达式在某一层以前的搬运项完全相同，则这些层可以严格消去，大小关系只需要继续比较第一层尚未相同的 detail。

## 9. 精度不是一条链，而是一张格

P005 独立地把正整数尺度因子识别为整除格：

- `gcd(d,e)` 是最大公共粗化；
- `lcm(d,e)` 是最小公共精化；
- 规范投影沿整除路径可交换。

因此 P018 不应只研究单条精度链，还需要在整个除数格上定义 precision shell。

## 10. P018-T07 — 带搬运的 Möbius 精度壳层

状态：`PROVED`

设 `A(d)` 是定义在 `d` 的所有除数精度上的整数值量，并把它视为尺度次数 1 的量：从 `c|d` 搬到精度 `d` 时乘以 `d/c`。

定义**搬运精度壳层**：

\[
\boxed{
\widehat A(d)
=
\sum_{c\mid d}
\mu(d/c)\frac{d}{c}A(c).
}
\]

则除数偏序上的 Möbius 反演给出

\[
\boxed{
A(d)
=
\sum_{c\mid d}
\frac{d}{c}\widehat A(c).
}
\]

证明：

\[
\sum_{c\mid d}\frac dc\widehat A(c)
=
\sum_{a\mid d}A(a)\frac da
\sum_{b\mid d/a}\mu(b),
\]

而内部 Möbius 和除 `a=d` 外均为零。∎

与相邻链上的非负 detail 不同，格上的 precision shell 可以带符号。它的作用正是让重叠精度路径发生相消。

## 11. P018-T08 — 尺度线性 bulk 全消去

状态：`PROVED`

若对所有 `c|d`，

\[
A(c)=cA(1),
\]

则任意 `d>1` 都有

\[
\boxed{\widehat A(d)=0.}
\]

因为

\[
\widehat A(d)
=dA(1)\sum_{c\mid d}\mu(d/c)=0.
\]

这给出了“高低精度嵌套相消”的一个严格代数版本：

> 任何仅仅随精度作线性搬运的 bulk，在非平凡 precision shell 中都会完全消失；壳层只记录真正由精度变化产生的偏离。

Möbius 反演本身是成熟数学；这里研究的是它与进取数论精度搬运规则的组合。

## 12. 根的精度状态

定义

\[
S_{p,d}(n)=R_p(nd^p).
\]

这与 P005 正在研究的尺度因子根状态完全一致，但 P018 的证明不依赖 P005 分支已经合并。

## 13. P018-T09 — 根精度 detail

状态：`PROVED`

对 `d|e`，令 `r=e/d`，则

\[
\boxed{
S_{p,e}(n)=rS_{p,d}(n)+\eta_{e:d}^{(p)}(n),
\qquad
0\le\eta_{e:d}^{(p)}(n)<r.
}
\]

证明：令 `k=S_(p,d)(n)`，则

\[
k^p\le nd^p<(k+1)^p.
\]

乘以 `r^p`：

\[
(rk)^p\le ne^p<(r(k+1))^p.
\]

所以

\[
rk\le S_{p,e}(n)<r(k+1),
\]

正好落入一个长度为 `r` 的投影纤维。∎

根 detail 同样满足 T02 的嵌套复合法则。

## 14. P018-T10 — 根 precision shell 只保留精化信息

状态：`PROVED`

令

\[
k=S_{p,1}(n),
\]

并定义相对于基础精度的 detail

\[
\eta_d=S_{p,d}(n)-dk.
\]

则任意 `d>1` 有

\[
\boxed{
\widehat S_p(d)
=
\sum_{c\mid d}\mu(d/c)\frac dc\eta_c.
}
\]

粗根的线性 bulk `ck` 被 T08 完全消去。

所以一个整数根族的非平凡精度壳层中，**只剩下精化新增的信息**。

壳层不要求非负。例如 `n=2,p=2,d=12` 时：

\[
\widehat S_2(12)=-3.
\]

因此带符号精度壳层是一种相消观察量，而不是“新增状态数”。

## 15. 一个精度上的 collapse

定义

\[
C_{p,d}(n)=S_{p,d}(n)^p.
\]

对 `d|e`，`r=e/d`，定义“先在高精度 collapse，再投回 d”的**精化恢复状态**：

\[
\mathcal R_{p;e\to d}(n)
=
C_{p,e}(n)\operatorname{//}r^p.
\]

它比较两种不同运算顺序：

\[
\text{先粗化再 collapse}
\qquad\text{与}\qquad
\text{先精化、collapse、再投回粗层}.
\]

两者一般并不交换。

## 16. P018-T11 — collapse/精化交换缺陷是粗盆地坐标

状态：`PROVED`

令

\[
k=S_{p,d}(n).
\]

则

\[
\boxed{
C_{p,d}(n)
\le
\mathcal R_{p;e\to d}(n)
\le
(k+1)^p-1.
}
\]

于是定义交换缺陷

\[
\chi_{p;e:d}(n)
=
\mathcal R_{p;e\to d}(n)-C_{p,d}(n),
\]

有

\[
\boxed{
0\le\chi_{p;e:d}(n)
\le
(k+1)^p-k^p-1.
}
\]

证明：T09 写成

\[
S_{p,e}(n)=rk+\eta,
\qquad0\le\eta<r.
\]

所以

\[
r^pk^p
\le
S_{p,e}(n)^p
<
r^p(k+1)^p.
\]

再按 `r^p` 做整数投影即可。∎

右侧上界正好就是 P002 的粗盆地 sharp gap。

因此，collapse 与精化不交换时产生的差，不是失控的近似误差，而是**原粗 collapse 盆地内部的一个精确有限状态坐标**。

### 显式不交换例

取 `n=3,p=2,d=1,e=10`：

\[
C_{2,1}(3)=1,
\]

而

\[
S_{2,10}(3)=17,
\qquad
17^2\operatorname{//}100=2.
\]

因此

\[
\chi_{2;10:1}(3)=1.
\]

## 17. P018-T12 — 精化恢复单调性

状态：`PROVED`

设

\[
d\mid e\mid f.
\]

则

\[
\boxed{
\mathcal R_{p;e\to d}(n)
\le
\mathcal R_{p;f\to d}(n).
}
\]

证明：写 `s=f/e`。根尺度相容性给出

\[
S_{p,f}(n)=sS_{p,e}(n)+\zeta,
\qquad\zeta\ge0.
\]

因此

\[
S_{p,f}(n)^p\ge s^pS_{p,e}(n)^p.
\]

把次数为 `p` 的状态从 `f` 投回 `d`，即得结论。∎

所以沿任意有限精化链，

\[
C_{p,d}(n)
=
\mathcal R_{p;d\to d}(n)
\le
\mathcal R_{p;e_1\to d}(n)
\le\cdots.
\]

定义增量

\[
\Delta_i
=
\mathcal R_{p;e_i\to d}(n)
-
\mathcal R_{p;e_{i-1}\to d}(n),
\]

则每个 `Delta_i` 都是非负整数，并严格望远镜相加：

\[
\sum_i\Delta_i
=
\mathcal R_{p;e_m\to d}(n)-C_{p,d}(n).
\]

这是 precision shell 的第二种、运算相关的含义：高精度只能继续恢复粗盆地内部尚未显现的状态坐标，不会把已经恢复的部分抹掉。

## 18. P018 明确不主张什么

### CE01 — 粗投影不存在状态唯一逆

P005 已给出直接反例：相同粗根状态可以对应不同的细根状态。因此精化必须依赖保留的源状态或真正新增的信息。

### CE02 — “精化后 collapse 再投回”不等于“粗层直接 collapse”

上面的 `n=3`、平方根、scale 10 例已经否定交换性。

### CE03 — 格上的 precision shell 不保证非负

`n=2,p=2,d=12` 给出 `-3`。

### CE04 — 局部 detail 不保证随精化增长

对 `n=2,p=2`，沿

\[
1\mid2\mid4\mid8\mid16,
\]

相邻层根 detail 依次为

\[
0,1,1,0.
\]

T12 的**累计恢复状态**是单调的，但单个局部 digit/detail 不是。

所以“精度更高”绝不等价于“每一层余数数值都更大”。

## 19. 与 P017 的关系

P017 反复出现

\[
\text{bulk}
+
\text{carry/shell residual}
\]

结构：

- Euclidean basin descent：确定性的 quotient bulk + 有界 local carry；
- Möbius carry identity：bulk 求和消失，只留下带符号 carry；
- cutoff pairing：内部项成对消去，只留下穿越截断面的 shell edge；
- Alexander descent：大阈值问题被转移到更小的尺度区域。

P018 **尚未**证明 P017 整体就是某个统一 precision functor 的实例。但 T07–T12 已经把这个问题从类比变成了可检验数学命题。

下一项重要目标是：

> 把至少一个非平凡 P017 恒等式完整改写成 transported precision-shell 恒等式，并精确指出哪一项就是 precision-changing defect。

## 20. 前人工作边界

P018 的多个局部结构已有成熟邻居：

- Euclidean quotient/remainder 与 floor/Galois 伴随是经典数学；
- filtered object 与 associated graded 是逐层分离信息的成熟代数语言；
- multiresolution analysis 明确研究不同分辨率之间新增的信息；
- interval arithmetic 可以利用有限区间包围完成严格证明并继续细化；
- p-adic 计算已经发展出包括 lattice-valued precision 在内的精度传播方法；
- 除数偏序上的 Möbius 反演是经典组合数学。

所以 P018 不对这些构件作历史优先权主张。

当前真正要检验的项目组合是：

\[
\boxed{
\text{整除精度格}
+
\text{多对一投影}
+
\text{有界 detail/carry}
+
\text{低精度证明稳定性}
+
\text{带搬运的有符号 shell}
+
\text{collapse/精化恢复动力学}.
}
\]

它是否构成有独立价值的有限精度证明演算，历史创新状态保持 `NOVELTY_UNVERIFIED`；正式 review-ready 前还需完成专门的来源登记与逐项比较。

## 21. 第一阶段状态

- P018-T01 精度纤维分解：`PROVED`
- P018-T02 嵌套 detail 复合：`PROVED`
- P018-T03 粗序证明稳定性：`PROVED`
- P018-T04 加法 carry：`PROVED`
- P018-T05 减法 borrow：`PROVED`
- P018-T06 精度链望远镜分解：`PROVED`
- P018-T07 transported precision-shell 反演：`PROVED`
- P018-T08 尺度线性 bulk annihilation：`PROVED`
- P018-T09 根精度 detail：`PROVED`
- P018-T10 根 shell 只保留精化信息：`PROVED`
- P018-T11 collapse/精化缺陷落在粗盆地：`PROVED`
- P018-T12 精化恢复单调性：`PROVED`
- 任意谓词/任意运算的统一证明演算：`OPEN`
- 与 P017 shell 机器的严格等价：`OPEN`
- 整体历史创新性：`NOVELTY_UNVERIFIED`

整数-only 可执行检查位于 `src/enterprise_math/precision.py` 与 `tests/test_precision.py`。
