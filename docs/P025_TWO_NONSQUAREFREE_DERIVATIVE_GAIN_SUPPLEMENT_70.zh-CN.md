# P025 补充 70 —— 恰有两个 Nonsquarefree Components 时的导数增益

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-paired-square-tail-stage61`  
依赖：P025 补充 64、66、69  
Hard block：`NONE`

## 1. Squarefree 安全盆地之后的第一层 hard structural slice

Stage 69 证明，非 unit activated triple 必须满足 `c` nonsquarefree 且至少一个 side nonsquarefree。

因此下一层最简单情形是：

- `c` nonsquarefree；
- `a,b` 中恰一个 nonsquarefree；
- 另一个 side `s` squarefree。

记 nonsquarefree side 为 `y`，则 repeated pair 为 `(y,c)`。

由于 `s` squarefree，其 block capacity 恰等于标准 arithmetic derivative：

\[
\boxed{C(s)=s'.}
\]

这会在 pair-radical compiler 中产生一个新的 exact gain。

## 2. P025-T139 —— 精确 derivative-gain pair-radical bound

固定整数 threshold

\[
T\ge1
\]

并假设

\[
\sigma_{\rm proj}\ge T.
\]

squarefree-side projective term 因 residual 为 1 不可能激活。因此 active term 只能是 `c`-oriented 或 `y`-oriented。

### 情形 1：c-oriented activation

Denominator 含有

\[
R_yC(s)=R_y s'.
\]

所以

\[
m(c)\ge TR_y s'.
\]

由 `m(c)=c/R_c` 得

\[
\boxed{R_yR_c\le\frac{c}{Ts'}.}
\]

### 情形 2：y-oriented activation

此时 denominator 含

\[
R_cC(s)=R_cs'.
\]

于是

\[
m(y)\ge TR_cs'.
\]

由 `m(y)=y/R_y` 得

\[
R_yR_c\le\frac{y}{Ts'}<\frac{c}{Ts'}.
\]

因此两种 orientation 统一得到

\[
\boxed{
\operatorname{rad}(yc)=R_yR_c\le\frac{c}{Ts'}.
}
\]

若 `c<=X`，则

\[
\boxed{
\operatorname{rad}(yc)\le\frac{X}{Ts'}.
}
\]

相较 Stage 64 的 generic `O(X/T)` pair-radical state，这个恰两块 nonsquarefree slice 多获得了一个明确的 `s'` 因子。

## 3. P025-C15 —— prime squarefree side 是最低容量 branch

若 `s` 为素数，则

\[
s'=1,
\]

没有额外 derivative gain。

若 `s` 为 composite squarefree，令 `r=Omega(s)>=2`。经典 arithmetic-derivative lower bound 给

\[
s'\ge r s^{(r-1)/r}\ge2\sqrt s.
\]

因此

\[
\boxed{
\operatorname{rad}(yc)\le\frac{X}{2T\sqrt s}.
}
\]

所以真正低容量的恰两块 nonsquarefree branch 会集中在 prime `s`，或者更一般地集中在标准 arithmetic derivative 很小的 `s`。

## 4. 条件 de Bruijn tail refinement

若再限制

\[
s'\ge H,
\]

则 P025-T139 把 repeated pair 编译为

\[
\operatorname{rad}(yc)\le\frac{X}{TH}.
\]

应用 Stage 64 同一个外部 de Bruijn pair-product count，可得到 restricted tail scale

\[
\boxed{
N_X(\sigma_{\rm proj}\ge T,\ s'\ge H,\ \text{exactly two nonsquarefree})
\ll_\varepsilon\frac{X^{1+\varepsilon}}{TH}.
}
\]

这不是新的 radical-counting theorem，只是把旧 theorem 作用到更强的 project-specific compiler 输出。

若 composite squarefree side 还满足 `s>=Y`，标准导数下界给

\[
s'\ge2\sqrt Y,
\]

因此该 restricted slice 额外获得 `Y^-1/2` saving。

## 5. 精确样本

### Prime-side branch

\[
3+125=128.
\]

唯一 squarefree side 为 `s=3`，所以

\[
s'=1.
\]

在 `T=4` 时 repeated pair 是 `(125,128)`，并且

\[
\operatorname{rad}(125\cdot128)=5\cdot2=10\le128/4=32.
\]

由于 squarefree side 是 prime，这里没有 derivative-side improvement。

### Composite squarefree side

\[
10+2187=2197.
\]

这里

\[
10'=7,
\]

active projective value 为 `729/121>6`。取 `T=6`：

\[
\operatorname{rad}(2187\cdot2197)=3\cdot13=39,
\]

而

\[
2197/(6\cdot7)>52.
\]

`s'=7` 相对 Stage-64 generic envelope 带来真实增益。

另一个例子是

\[
22+2187=2209=47^2,
\]

其中 `22'=13`，threshold 1 下

\[
3\cdot47=141<2209/13.
\]

## 6. 经验路由信号

一次 `c<=10^4` 的有限 exact scan 显示：activated 非 unit triples 中，若恰有两个 nonsquarefree components，则唯一 squarefree side 在绝大多数观测样本中都是 prime；只出现少量 composite-side 样本，包括上面的两个例子。

这**不是 theorem**，也不进入任何证明；它只支持 P025-C15 给出的研究路由：如果要继续研究 Stage 69 之后的 hard structured family，prime-side 或 very-low-`s'` branch 应优先检查。

## 7. 精度架构后果

Stage-69 Boolean squarefree pattern 可以只在需要时继续 refine：

\[
\text{exactly two nonsquarefree}
\to
\text{identify squarefree side }s
\to
\text{读取一个旧 observable }s'
\to
\text{pair-radical precision 提升 }1/s'.
\]

因此一个经典 arithmetic-derivative value 成为这个 structural slice 上强化 theorem-native pair-radical state 所需的 exact extra coordinate。

## 8. Prior-art discipline

Arithmetic derivative 及其 lower bounds 属于 prior art [SRC-MERIKOSKI-HAUKKANEN-TOSSAVAINEN-2019-ARITHMETIC-SUBDERIVATIVES]；de Bruijn radical counting 同样属于 prior art。

P025 只保留 projective activation system 中的 exact reduction `rad(yc)<=c/(Ts')`。历史 novelty 仍为 `NOVELTY_UNVERIFIED`。

## 9. 可执行资产

新增：

- `src/enterprise_math/abc_projective_two_nonsquarefree.py`；
- `tests/test_abc_projective_two_nonsquarefree.py`。

## 10. 下一前沿

Hard block 不存在。继续：

1. 隔离 prime-squarefree-side branch `s'=1` 并寻找 exact families / obstructions；
2. 研究三块全 nonsquarefree slice 是否存在类似的 cheapest-side derivative gain；
3. 只有在得到强于 generic Stage-64 tail 的 theorem 时，才把经验 prevalence 升级为计数问题；
4. 继续把结果作为 conditional/adaptive precision refinement，而不是 generic arithmetic-derivative novelty claim。
