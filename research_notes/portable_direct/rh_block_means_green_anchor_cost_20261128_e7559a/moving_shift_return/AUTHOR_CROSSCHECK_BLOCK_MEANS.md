# 作者交叉核对：连续块均值证明与公共前史同端区间减法

统一作者 **EM-DIRECT-E7559A / TASK_RESEARCH**，Activity **RA-D2F111EA1C0D4B1DBEFBC1B4**。这是同一作者队伍的交叉核对记录，不是 independent Review，不改变任何 formal Result 状态。

## 1. 检查对象和结果

已逐项读取本轮 `block_means/COARSE_BLOCK_MEANS_AND_RH.md` §§1–4、`certify_block_mean_statistics.py` 的全部区间聚合，并对照直接前驱 `arithmetic_sampling/DYADIC_WINDOWS_AND_INTEGER_BRIDGES.md` 的有向平移均值链及单侧 Landau 量词。没有发现需要修补的数学缺口或区间方向错误。

本次读取快照为：

- 证明 SHA-256：`8aaef45fb4cc8f8514378b0d065dd01ad211d6b3ce9631cb87198e93d80115a2`。
- 脚本 SHA-256：`9c25cfc339b8bd4c504b03a01fbaaf88932abc834fda89de2c2d4ee3d1b81a95`。

后续若只增加讨论段或修订文献书目信息，应据实际新摘要另记录；这里的哈希准确指向检查当时的文本。

## 2. 先平均再正化以及分母

对块距 d，真实整数距离是 `D=rd`。每个块差是 r 个对齐整数差的平均。凸函数 `x↦(x_+)²` 给

\[
\sum_i(w_{i+d}-w_i)_+^2
\le\frac1r\sum_{u=X}^{2X-1-rd}[F(u+rd)-F(u)]_+^2.
\]

`i=0,…,M−1−d`、`v=0,…,r−1` 恰好一一遍历上述完整整数中心。除以 `Xd` 后，右边分母成为 `rXd=XD`。因此

\[
\mathcal C_{k,s}^+\le\mathcal K_{k,s}^{+,\mathrm{coarse}}
\]

的方向、中心总数和尺度均正确。不能将新统计的分母再加一个 r，否则所得恢复估计会损失尺度。

对长 M 的均值序列，前驱嵌入的规范统计为

\[
K^+(w)=\max_d\frac1{Md}\sum_i(w_{i+d}-w_i)_+^2=r\mathcal C_{k,s}^+.
\]

于是前驱根预算 `sqrt(MK^+(w))` 准确变成 `sqrt(XC)`，没有额外 `sqrt r`。

## 3. 前一整块恢复和 `2r` 费用

假设一步上升至多 1，负跳任意大。对于 `n=jr+u`、`j≥1`，前一整块中的所有下标都不大于 n，因此

\[
z_n-w_{j-1}
\le r+u-(r-1)/2\le(3r-1)/2.
\]

另有 `w_0−z_0≤(r−1)/2`。中间均值差由有向嵌入支付；`j=1` 时该差为零。因此未放宽的细节费用是 `2r−1`，稿件显示为 `2r` 合法。第一块内直接有 `z_n−z_0≤r−1`，也被覆盖。

使用包含 n 的当前块会让 n 之后的巨大负跳进入均值，因此没有相同上界；稿件选择前一完整块是必要的方向处理。全块首尾则各支付半个 `r−1`，再用锐的端点均值链，得到准确的 `r−1+t sqrt(XC)`。

## 4. 跨窗口整数桥和 RH 量词

普通素数 `F(n)=n−theta(n)` 的一步上升确实至多 1。每个 `2^{j+1}≥4` 是合数，所以窗口桥恰好为 1；与上一完整块的 `r_j−1` 合为 `r_j`。初值为 `F(2)=2−log2`，最后部分块另用 `2r_k`。式 (3.3) 的首块、末块和重复边界均一致。

当 `r_k=2^{floor(k/2)}` 时，`Σ_{j≤k}r_j=O(2^{k/2})`。若对每个 `η>0` 都有 `C_j≪_η2^{ηj}`，则统计恢复总费用为 `O_η(k2^{(1+η)k/2})`。选择小于目标指数余量的 η，吸收 k 后，得到每个 `ε>0` 上的 `theta(x)≥x−O_ε(x^{1/2+ε})`。

前驱单侧 Landau 论证以任意固定 `a>1/2` 为参数，故这里量词足够；没有假设存在最右零点或零点频率线性独立。反向使用 RH 下已付高次素数幂成本的旧 `K_k^+≪k²`，再由 Jensen 传入新统计，方向正确。当前结论是 RH 等价判据，未构成实际新统计的无条件无界上界。

## 5. 脚本同端减法为什么有效

设源位置 p 的认证对数区间为 `[l_p,h_p]`。记

\[
c_i(p)=\#\{n\in[X+ir,X+(i+1)r-1]:p\le n\}.
\]

由于后块整体位于前块之后，对任意 `d≥1` 和 p，

\[
c_{i+d}(p)-c_i(p)\ge0.
\]

脚本没有先对两个块均值作独立区间减法，而是保存同一批源对数的整数端点线性和。其

\[
\texttt{block\_highs[i+d]-block\_highs[i]}
=\sum_p(c_{i+d}(p)-c_i(p))h_p
\]

是所需素数质量差的上界；`block_lows` 的同端差是下界。对两块都完全处于前史的 p，两个系数都是 r，故该项准确消去。于是

\[
r^2dS-(\texttt{high difference})
\le rS(w_{i+d}-w_i)
\le r^2dS-(\texttt{low difference}),
\]

其中 `S=10^80`。正化平方后分母为 `r²XdS`，输出仍是 `S·C` 尺度，代码的两次 r 与一次 S 均正确。

这一同端减法只有在共享源变量和非负差系数已经确认时才有效；本脚本恰好满足该结构。对一般不相关区间不能这样相减。

## 6. 新做的准确有理实现交叉检查

另写 `crosscheck_block_mean_interval_cancellation.py`，没有导入或执行被核对脚本，也没有重跑前驱证书。采用两种非负有理源，其中一种含巨大公共前史和内部负跳，检查 `X=2^k`、`1≤k≤6` 的所有二幂分块。

结果写入 `block_mean_author_crosscheck_certificate.json`，全部通过：

| 对象 | 检查数 |
|---|---:|
| 非负有理源向量 | 12 |
| 分块方式 | 42 |
| 同端区间减法和完整均值差 | 1,650 |
| 非负源差系数 | 163,158 |
| Jensen 长度比较 | 112 |
| 完整块恢复 | 42 |
| 任意点恢复，保留准确 `sqrt 2` 常数 | 1,284 |

最后一项没有以浮点数近似平方根：把不等式平方后，在正余量分支再平方一次，使用准确有理比较。有限检查覆盖实现和方向，上文一般证明承担无界结论。

复算：

```bash
python moving_shift_return/crosscheck_block_mean_interval_cancellation.py \
  --block-means block_means \
  --output moving_shift_return/block_mean_author_crosscheck_certificate.json
```
