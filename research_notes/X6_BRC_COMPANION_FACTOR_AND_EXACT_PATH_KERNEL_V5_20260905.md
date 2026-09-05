# X6 × BRC：companion 因子分解与精确正轴路径核

Status: `DERIVED / EXACT / BRC-REUSABLE / POSITIVE-HISTOGRAM-FIRST`
Date: `2026-09-05`
Depends on: X6 universal Cell completion V2.

## 1. 六轴一步算子因子化

在 endpoint group `G6^cell ~= Z^2 x Z/2` 中取

`u=AB`, `v=AC`, `w=AD=(uv)^(-1)`，

以及 order-two companion `t`。

三组 K4 opposite axes 满足

- `CD=u t`;
- `BD=v t`;
- `BC=w t`。

因此在整数群代数中，六个正轴的一步 Path/N-BRC 生成元

`S = AB+AC+AD+BC+BD+CD`

严格因子化为

`S=(1+t) H`,

其中

`H=u+v+w`, `uvw=1`。

因为 `t^2=1` 且 t central，

`(1+t)^m = 2^(m-1)(1+t)` for every `m>=1`。

所以

`S^m = 2^(m-1)(1+t) H^m`。

## 2. exact sheet balance theorem

对任意 `m>=1` 和任意 free endpoint `h in <u,v> ~= Z^2`：

`Coeff_{h}(S^m) = Coeff_{h+t}(S^m)`。

也就是说，在等权六正轴 branching 下，同一个 ordinary slice-visible endpoint 的两个 full-state sheets 的 N-BRC multiplicity 永远完全相等。

这是 endpoint multiplicity symmetry；Path-formal witness 仍保留具体使用了哪一条六轴、顺序及其它 provenance。

因此：

`EQUAL_POSITIVE_AXIS_BRANCHING -> COMPANION_SHEET_MULTIPLICITY_BALANCE`。

它解释了为什么只看总 endpoint multiplicity/Boolean support 很难发现 companion：该 observer 上两个 sheets 从第一步起就是严格平衡的。

## 3. 完整 closed form

`H` 的三步方向为

`u=(1,0)`, `v=(0,1)`, `w=(-1,-1)`。

长度 m 的 base path 若分别使用 `n1,n2,n3` 次 u,v,w，则

`n1+n2+n3=m`,

free endpoint 为

`p=n1-n3`, `q=n2-n3`。

反解：

`n1=(m+2p-q)/3`;

`n2=(m-p+2q)/3`;

`n3=(m-p-q)/3`。

若这三个数不是非负整数，则 `(p,q)` 不在长度 m 的 support。

若合法，则

`Coeff_{u^p v^q}(H^m)=m!/(n1! n2! n3!)`。

所以对 `m>=1`，full X6 endpoint `(p,q,epsilon)` 的精确 N-BRC multiplicity 是

`N_m(p,q,epsilon)=2^(m-1) * m!/(n1! n2! n3!)`，

且与 `epsilon in {0,1}` 无关。

这给出了无需枚举 `6^m` paths 的 exact integer kernel。

## 4. origin / companion return counts

要使 free endpoint `(p,q)=(0,0)`，必须

`m=3k`, `n1=n2=n3=k`。

因此对 `k>=1`：

`Paths_{3k}(origin -> origin)`

`= Paths_{3k}(origin -> companion)`

`= 2^(3k-1) * (3k)!/(k!)^3`。

若 m 不是 3 的倍数，则等权 positive-axis word 不可能在长度 m 到达 origin 或 companion。

最小非平凡例 `k=1`：

- 24 条三步 positive paths 回 origin（四个 star × 3! orderings）；
- 24 条三步 positive paths 到 companion（四个 face × 3! orderings）。

`k=2` 时两边均为 2880。

## 5. positive rational weighted generalization

把三组 opposite pairs 的正有理权写为

- `(a,a')` on `(u,ut)`;
- `(b,b')` on `(v,vt)`;
- `(c,c')` on `(w,wt)`。

Weighted-BRC 一步群代数为

`S_w = u(a+a't)+v(b+b't)+w(c+c't)`。

在有理群代数的 C2 character readout 中使用

`e_+=(1+t)/2`, `e_-=(1-t)/2`，

得到两条精确通道：

`S_+ = u(a+a') + v(b+b') + w(c+c')`；

`S_- = u(a-a') + v(b-b') + w(c-c')`。

对 endpoint `(h,epsilon)`：

`Coeff_{h,epsilon}(S_w^m)`

`= 1/2 * ( Coeff_h(S_+^m) + (-1)^epsilon Coeff_h(S_-^m) )`。

这里原始 branch masses 仍全为正；`S_-` 是**派生 signed character readout**，不能冒充 Positive Weighted-BRC 本体。

若每组 opposite pair 权重相等，即 `a=a'`, `b=b'`, `c=c'`，则

`S_-=0`，

从而 m>=1 后 exact sheet balance 恢复。

## 6. observer discipline

推荐保留层级：

1. Path-formal / weighted branch occurrences；
2. 六轴 labeled trace histogram；
3. full Cell endpoint `(p,q,epsilon)`；
4. ordinary slice-visible endpoint `(p,q)`。

只有当未来 observer 对 sheet、axis labels、path history、weight pairing 都不敏感时，才能继续向下 quotient。

特别是：

`BALANCED_SHEET_MULTIPLICITY != SHEET_DOES_NOT_EXIST`。

严格相等的统计重数不能作为删除 companion Cell identity 的理由；PF static packet count 与 endpoint identity 仍是另一种 observer。

## 7. 工具化价值

这条因子化把六轴 endpoint N-BRC 的等权长度-m 传播从 `6^m` path enumeration 降为一个三方向 multinomial kernel乘一个显式 `2^(m-1)` sheet factor。

它可直接用于后续：

- 六轴路径计数；
- rotation/BRC 回归；
- companion 可观测性分析；
- 有理权 pair asymmetry 的 signed character readout；
- finite-depth endpoint propagator。

不需要连续极限、浮点谱分解或经典 3D carrier 坐标。
