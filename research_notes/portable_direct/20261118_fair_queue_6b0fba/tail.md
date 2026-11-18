## 免表 BRC 尾部传输：证书与预测器共享一个整数幂

**实际积压任务** `RS-BRC-TABLEFREE-TAIL-LOCAL-COST-20261101`，冻结发布 `TP2-7AA587095F56589D45F7`，任务书 blob `96905206bc7b2cef4eb1412cc7b5a3e5b40e27ee`。源实现位于 `24eb5e125a7bf52366cc49f1ed2594c0cd6d5b14:src/enterprise_math/brc_table_free_tail.py`，项目快照 `7b32ae2` 上同文件 blob 仍为 `aaef03c9d8e68de5ace75b6736d1169faa4b2918`。

### 精确共享公式

设 \(N,m\) 为正整数，\(mN=J^2+R\)，\(J\ge0,\ 0\le R\le2J\)，\(h\in\{1,2\}\) 且 \(m\ge h\)。事先固定一个偶阶 \(K\ge2\)。记 \(a_i/D=\binom{1/2}{i}\)（\(1\le i\le K\)），\(p/q=\binom{1/2}{K+1}>0\)。令

\[
U=m^K,\qquad H=\sum_{i=1}^K a_i h^i m^{K-i}.
\]

冻结代码的精确证书与预测量可以通过同一个 \(U\) 求出：

\[
\boxed{\quad 2pJh^{K+1}\le (2m-h)q U,\qquad d=\left\lfloor \frac{JH}{D U}\right\rfloor .\quad}
\]

从原证书 \((p/q)J(h/m)^{K+1}+h/(2m)\le1\) 清除正分母即得第一式；源代码两边各多乘了一个正因子 \(m\)。第二式仍是同一个偶阶交错下界的取整。通过证书后，原 BRC 奇宽校正从 \(A=J+d,\ G=R+hN-d(2J+d)\) 出发，为每一分支保留相同候选、余量与顺序；当 \(G\ge2A+1\) 就扣去该宽度并递增 \(A\)。所以其拒绝集合、通过后的校正次数和最终 \((J',R')\) 与冻结代码逐状态一致。原误差界继续给出最多两次校正，\((m+h)N=J'^2+R',\ 0\le R'\le2J'\)。

每个通过的输入，乘子的大幂由分别求 \(m^{K+1},m^K\) 降为一次 \(m^K\)；证书失败时只求一次 \(m^K\) 并跳过 Horner。基数 \(h\) 的幂和 Horner 保留源算法。仅使用源 `scaled_even_truncation` 的系数缓存；新临时量 \(U\) 的位长为 \(1+\lfloor K\log_2 m\rfloor\)，无跨乘子缓存。固定阶数的选择没有扫描成本；若外部依次试多个阶数，失败阶数的证书仍各需计费。这里交付的是证书与预测器共享机制，阶数自适应留待另测。

### 校正和端点

对质数集合 \(\{3,5,7,11,13,17,19,23,29,31,37,41,43,47\}\) 的所有 \(p\le q\) 取奇半素数 \(N=pq\)，取 \(h\le m\le63\)、\(h=1,2\)、\(K=2,4,8,16\)。52,500 条路径中，381 条拒绝，52,119 条通过。通过路径分别有 24,700、27,204、215 条发生 0、1、2 次校正。所有通过路径的全部返回字段与冻结模块一致，根和余量另与整数平方根独立核对。

\(m=h,K=2\) 时临界证书精确化为 \(J\le8\)。在 \((m,h,N)=(1,1,65),(2,2,35)\) 有 \(J=8\)，共享传输分别得到 \((J',R')=(11,9),(11,19)\)；\((1,1,85),(2,2,49)\) 均为 \(J=9\) 并被拒绝。

### 局部资源证据

先在实验脚本中固定奇半素数 \(N=(2^a-1)(2^b-1)\)，指数对为 \((61,127),(521,607),(1279,2203)\)，取 \(K=2,8,32\)。每组各取两个步长，在证书通过的边缘乘子附近各取 16 个连续源状态。边缘以倍增找上端、二分找通过点，逐项确认所测证书；时间不包含样本构造和查询阈值。CPython 3.12.14，先轮转实现次序，再取 11 轮中位数。下表为热缓存完整每步纳秒，含源重构、证书、原有 Horner、最终状态验证和提取根余。直接整数平方根对照也验证源并构造与重构目标状态。峰值字节用预热后逐步单独运行的 tracemalloc 观测，表示 Python 追踪到的本步分配。

|N 位数|K|最大 U 位数|原传输 ns|共享 ns|直接 isqrt ns|原/共享峰值 B|
|--:|--:|--:|--:|--:|--:|--:|
|188|2|75|5035|3600|1369|572 / 612|
|188|8|91|4826|4087|1265|572 / 612|
|188|32|154|8196|7612|1290|580 / 628|
|1128|2|451|7535|6376|4939|992 / 1080|
|1128|8|534|8198|6796|3854|920 / 1016|
|1128|32|579|10992|9770|3625|916 / 1020|
|3482|2|1393|29778|25868|31541|2436 / 2652|
|3482|8|1641|27499|25149|19821|2236 / 2484|
|3482|32|1738|29771|28509|15584|2176 / 2432|

例如 1128 位、\(K=8\) 的 32 步批次从清空系数缓存开始运行时，原传输和共享传输分别为 8955、7602 ns/步；热态分别为 8198、6796 ns/步。两种情形均包含构造结果的成本。现有 pairwise BRC 只接受乘子不超过其固定上限，本实验唯一全批满足范围的是 188 位、\(K=32\)，热缓存 3263 ns/步，冷启动批次 4504 ns/步，热态临时峰值 604 B；它另缓存各乘子对的 dyadic predictor。

完整实现间的差值还包含合并输入检查和复用系数元组等因素。为单独估计 \(U\) 共享贡献，再比较相同新实现中只改一处的两个版本：在已通过证书后，给预测器传旧 \(U\) 或重新算一次 \(m^K\)。以每种 21 轮、每轮 1600 步、交替次序的配对时间之比（重复求幂 / 共享）中位数衡量，188 位 \(K=2\)、1128 位 \(K=8\)、3482 位 \(K=2\) 和 3482 位 \(K=32\) 分别为 1.027、1.041、1.024、1.015；各自有 14、12、15、13 轮共享较快。该微小 CPU 差值受调度波动影响；每个证书通过的状态少求一次乘子幂是实现的精确计数。九组热态临时峰值均上升，原因包括 \(U\) 需要保持到预测器使用。本次结果支持定阶且无逐乘子缓存的局部资源改进，乘子扫描数量及分解复杂度仍沿用原结论。

[冻结任务书](https://github.com/awdawmip/enterprise-math/blob/7b32ae2ad9d1c13a13ff4668d1d218adda99390d/research_tasks/RS-BRC-TABLEFREE-TAIL-LOCAL-COST-20261101.md) · [冻结模型与原证书实现](https://github.com/awdawmip/enterprise-math/blob/24eb5e125a7bf52366cc49f1ed2594c0cd6d5b14/src/enterprise_math/brc_table_free_tail.py) · [原推导与性能边界](https://github.com/awdawmip/enterprise-math/blob/24eb5e125a7bf52366cc49f1ed2594c0cd6d5b14/research_notes/BRC_TABLE_FREE_TAIL_20260907.md)

<details>
<summary>可直接复用的冻结模块补丁</summary>

以同版本源码执行 git apply --check 已通过。用补丁模块替入原有 test_brc_table_free_tail.py 全部四项回归均通过。

```diff
--- a/src/enterprise_math/brc_table_free_tail.py
+++ b/src/enterprise_math/brc_table_free_tail.py
@@ -85,7 +85,13 @@
         raise ValueError("alternating-tail certificate requires step/multiplier <= 1")
 
     denominator, scaled, _ = scaled_even_truncation(degree)
+    return _increment_from_power(root, multiplier, step, degree, multiplier ** degree, denominator, scaled)
 
+
+def _increment_from_power(
+    root: int, multiplier: int, step: int, degree: int, m_power: int,
+    denominator: int, scaled: tuple[int, ...],
+) -> int:
     # Homogeneous evaluation of D*m^K*L_K(h/m):
     #   sum_k a_k h^k m^(K-k).
     h_power = step
@@ -96,7 +102,7 @@
 
     if numerator < 0:
         raise AssertionError("even binomial lower truncation became negative")
-    exact_denominator = denominator * pow(multiplier, degree)
+    exact_denominator = denominator * m_power
     return (root * numerator) // exact_denominator
 
 
@@ -120,10 +126,17 @@
         return False
 
     _, _, next_coeff = scaled_even_truncation(degree)
+    return _certify_from_power(root, multiplier, step, degree, multiplier ** degree, next_coeff)
+
+
+def _certify_from_power(
+    root: int, multiplier: int, step: int, degree: int, m_power: int,
+    next_coeff: Fraction,
+) -> bool:
     p = next_coeff.numerator
     q = next_coeff.denominator
-    left = 2 * multiplier * root * p * pow(step, degree + 1)
-    right = (2 * multiplier - step) * q * pow(multiplier, degree + 1)
+    left = 2 * root * p * pow(step, degree + 1)
+    right = (2 * multiplier - step) * q * m_power
     return left <= right
 
 
@@ -167,10 +180,16 @@
         raise ValueError("source state does not reconstruct m*n")
     if not 0 <= r <= 2 * j:
         raise ValueError("source remainder escaped its BRC basin")
-    if not two_correction_certificate(j, m, h, degree):
+    if isinstance(j, bool) or not isinstance(j, int) or j < 0:
+        raise ValueError("root must be a non-negative integer")
+    if m < h:
+        raise ValueError("declared degree does not certify the two-correction tail at this state")
+    denominator, scaled, next_coeff = scaled_even_truncation(degree)
+    m_power = m ** degree
+    if not _certify_from_power(j, m, h, degree, m_power, next_coeff):
         raise ValueError("declared degree does not certify the two-correction tail at this state")
 
-    d = lower_increment(j, m, h, degree)
+    d = _increment_from_power(j, m, h, degree, m_power, denominator, scaled)
     candidate = j + d
     gap = r + h * n - d * (2 * j + d)
     if gap < 0:
```

</details>
