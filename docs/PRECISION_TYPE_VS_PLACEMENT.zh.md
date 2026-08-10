# 精度类型不等于精度落点

状态：`RESEARCH BRIDGE / NONCANONICAL`

Smith / 行列式因子数据可以给出非常有力的整数精度**类型**，但它本身并不能告诉我们：在一个固定的世界坐标系里，尚未被观测到的方向究竟落在哪里。

例如在 `Z^2` 上比较

`O_1=(2,0)`

和

`O_2=(0,2)`。

两者拥有完全相同的抽象整数精度轮廓：

- 有理 rank 都是 `1`；
- hidden free rank 都是 `1`；
- Smith factor 都是 `(2)`；
- 最大非零行列式因子都是 `2`。

但是它们隐藏的状态方向完全不同：

- `O_1` 看见第一坐标、隐藏第二坐标；
- `O_2` 看见第二坐标、隐藏第一坐标。

因此

`(hidden rank ; Smith factors)`

只在允许适当的状态/观测整数 unimodular 坐标变换后描述 observation map 的抽象类型。当 named world coordinates 本身有语义时，它不能替代真实的 row lattice、kernel embedding 和坐标身份。

## 为什么 horizon plateau 判据仍然精确

沿同一个声明好的 future language，未来 observation lattice 构成嵌套链

`L_h subseteq L_(h+1)`。

如果相邻两个 horizon 的有理 rank 相同，那么它们的有理 span 已经相同。在这个固定有理空间内，如果嵌套的两个整数 lattice 还具有相同 saturation index，那么它们在同一个 saturated lattice 中具有相同有限 index，因此必有

`L_h=L_(h+1)`。

这个 equality 又意味着 `L_h` 已经对所有声明 action 右不变，所以任何更长 future word 都不可能继续扩大它。

所以沿一条真实的 future-refinement chain：

`相邻 rank 相同 + 相邻 saturation index 相同`

是一个精确、永久的停止证书。

但同样的一对数值**不能**拿来判断两个互不嵌套的 observation map 是否相同。

## 架构规则

必须保持两层区别：

1. **precision type / 抽象算术复杂度** —— hidden rank、Smith factors、determinantal divisors；
2. **precision placement / 语义落点** —— 实际 kernel、row lattice、named state coordinates，以及作用在这些坐标上的 future operations。

第一层适合做比较、上界、拓扑/算术 phase 摘要；第二层才足以真正运行世界，或者判断哪些具体状态差异可以被 collapse。

Smith normal form 与 lattice index 都是标准既有数学。进取数论这里的价值不是重新发明这些不变量，而是明确阻止把一个漂亮的抽象 invariant tuple 错当成完整的语义世界状态。