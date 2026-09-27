# Prefix-ideal readout：共享上下文符号审查

结论：**PASS / SHARED_CONTEXT / SYMBOLIC_REVIEW / NOT_EXECUTED / NOT_ADMITTED**。没有发现阻断前缀 gcd 恒等式、最小素因子事件、双向多项式时间 Turing 归约或 Hasse jet 表述的数学缺陷。该结果给出明确的新观察工具规格，不是已实现的快速因式分解。

审查对象：`PREFIX_IDEAL_READOUT.md`，最终 SHA-256 `ebb2a29e9ebe15de174c9b7d4fba5562ddd854b7c298eb806114c43e741c94cc`。已逐段全文读取最终稿，包括修订后的信息论边界和新增 Hasse jet 段；没有修改原稿、调用科学模块或进行数字试验。作者给出的外部论文归属不作为本审查的独立文献核验；这里核的是稿中自足证明。

## 1. BRC 载体与指数标记

本审查实际通过 GitHub connector 读取了 [Universal Histogram Foundation](https://github.com/awdawmip/enterprise-math/blob/4c0faffe3e71068bfc41a9ac617fb54669ed59a1/definitions/ENTERPRISE_BRC_UNIVERSAL_HISTOGRAM_FOUNDATION_20260903.md)，完整返回 Git blob `5100aa3d893ff152e0da7a3ae2eea812cfbcaf1c`。

WBRC-T36 允许有限正权直方图的 alternative multiplicity 与 `[a] tensor [b]=[ab]`。WBRC-T37 允许已知素数估值向量的 Laurent 单项式标记。因此 `[1]+[2]` 的 n 次串联中，恰选 j 次第二支路的权为 `2^j`，其重数为 `binom(n,j)`；在素数 2 的非负指数子半环内，`[2^j]↔X^j` 是无碰撞的精确标记。这里不需要分解 n，也没有丢弃相等权重处的重数。

以二进制 j 表示指数，与实际构造具有 j+1 位的权整数 `2^j` 是不同的资源合同。旧 foundation 证明有限 carrier 的语义；并没有承诺一个 `H^n` 的短 DAG 可以免费执行任意系数观察。原稿已作此区分，准确标成 COMPOSE_APPLIED，未冒充 native execution。

系数模 n 的映射与 alternative 加法、串联卷积相容。再取非负次数至 m 的前缀，可视为模 `X^(m+1)` 的截断环；但最后从这些系数取共同理想不是仅由总质量或 scalar min-valuation 决定的 semiring character。这是新的明确观察合同，不是原正质量载体中的权改写。

## 2. 素数幂估值与边界

固定 r|n，a=v_r(n)>0；由 `j*C(n,j)=n*C(n−1,j−1)` 得
`v_r(C(n,j))≥max(0,a−v_r(j))`。对全部 j≤m，令 `t=min(a,floor(log_r m))`，共同下界为 a−t。

在 j=r^t 处，对 1≤i<r^t 有 `v_r(i)<t≤a`，所以 `v_r(n−i)=v_r(i)`。乘积式中的每项在消去相等的 r 因子后为 r-adic unit，给出恰 a−t，确实达到共同下界。这里的局部有理单位论证是符号证明，不是让实际程序除以模 n 的非单位。

t=0 时 j=1 且空乘积为 1；m=0 由约定 G=n 单独覆盖；m=n 包含系数 1，从而 G=1。结论

`v_r(G_n(m))=max(0,v_r(n)−floor(log_r m))`

与 `n/gcd(n,lcm(1,...,m))` 完全一致，包括重复素因子。不存在从平方自由例子误推广到 prime powers 的问题。

## 3. 最小素因子与双向归约

G_n(m)<n 当且仅当前缀已包含某个素因子 r 的第一次估值下降，首次位置就是 n 的最小素因子。n 为素数时首次位置为 n；n 为素数幂时仍为底素数。对 `n=pq,p<q` 的三段阶梯正确。

若精确 observer 的成本以 `log n+log(m+1)` 为多项式，输出 G 的长度不超过 n 的位长。单调谓词 `G<n` 的二分查找用 O(log n) 次调用给出最小素因子；除去该因子并重复，至多 O(log n) 轮，因而得到多项式次 oracle 调用和多项式普通位运算。它并没有免费输出大量前缀系数或 lcm。

反向给定 n 的完整素因子分解，仅需对各 prime power 用比较/乘法确定被 m 覆盖的指数，最多处理其本来就受 log n 限制的重数，再组合剩余幂。故反向亦有多项式位复杂度。两者是 **Turing 归约**，不是已经构造 observer，也不是未经条件的计算下界。精确输出问题可以进一步弱化到查询谓词 G<n；这并不消除其分解能力。

## 4. DAG 大小不等于观察成本

`(1+X)^n` 的二进制幂 circuit 有 O(log n) 个乘法节点，正确；每个节点是符号多项式乘法，不是常成本完成其全部系数的运算。原稿列出的朴素截断 `O(m² log n)` 模标量操作、O(m) 系数存储是有效上界；实际 typed BRC 标量成本还须另乘。使用更快多项式乘法也不能据此把以二进制给定的 m 自动降为 poly(log n)。

`lcm(1,...,m)` 短记号同样只隐藏了构造与观察问题。原稿没有将此记号或 factor-valued observer 当作已经存在的原生快速工具。

## 5. 加法修复信息与措辞范围

原稿 A_1 两次合成的例子确实否定“取各输入最小估值，再用 min 传播”的规则：相同次数的重数相加会产生新的整除性。

还可在本实际幂族里给出更明确的 odd-modulus 不充分性见证，而不作数值试验：令 r 为任意奇素数，m=1，`A_a=(1+X)^a−1`。两对输入 `(A_1,A_1)` 与 `(A_1,A_(r−1))` 的首系数模 r 理想摘要均为 `(unit,unit)`。按原稿合成式得到 A_2 与 A_r，首系数分别为 2 与 r，输出理想却为 unit 与 zero。这证明只保这种标量摘要不能封闭所需合成；若另外保留 exponent、residue 或 carry 数据，仍须重新证明其充分性和成本。

最终稿已明确修正信息论边界：对这一个特定 family，精确总 count `2^n` 或 dominant weight `2^n` 确实能确定 n，进而数学上确定 G。这里缺的是**现有廉价 port laws 未提供前缀理想读出**及其资源界，不能升级成“总数绝对不包含足够信息”的命题。最终稿还区分写出该大整数本身的输出成本，与已知 n 的短描述；没有据此提出信息论不可能性。

## 6. Hasse jet 与普通导数

在任意交换系数环中，Hasse 导数由 `F(X+T)=sum_j D^[j]F(X) T^j` 定义，故 `D^[j]F_n(0)=binom(n,j)`，不需要除以 j!。删除常数坐标后取前 m 个 jet 坐标的共同理想，确实就是稿中的前缀理想；这个解释对复合模数和素数幂均成立。

普通一阶导数为 `n(1+X)^(n−1)`，模 n 恒为零。它不能替代 Hasse jet，因为 j! 在复合模数中不一定可逆。若 m 小于 n 的最小素因子，上文估值公式给 G_n(m)=n，因此每个非恒定 jet 坐标都为零；常数坐标仍为 1，原稿明确删除了它。首次事件可降低某个素因子幂的估值，并不保证当时出现模 n 的单位坐标。

这证明固定低阶 jet 在最小素因子更大的输入上不能看见该事件，但不排除有针对性的高阶 jet 压缩工具。原稿仅要求新的 residue/carry 合同，没有把特征零 Newton 或实根工具直接套到复合模数，也没有把形式导数当作已实现的原生科学运算。

## 7. 新工具义务与目标状态

输入 n、二进制 m、canonical branch circuit；输出 G 及同时覆盖“共同整除”和“生成该理想”的证书，这个规格清楚且非循环。仅声称 G 整除系数还不足以排除过小答案；仅列全部 m 个系数虽然可验证，也不自动是短证书。获得候选时的构造、source admission、所有失败/退化分支和验证费用均须保留。

这条路线确实转向了不同于单 torus 返回的观察对象，值得继续探索 composable residue/carry repair。当前结论不会消除未知因子问题：快速精确 observer 与因式分解等价，正说明必须在该读出环节交付新的实质工具，而不是再次假设目标能力。

没有新的科学运行、外部 provider query、远端写入、独立正式准入或 Shor 完成。当前父目标保持开放；本审查只为下一原生工具研究提供已核清的合同。

Global-Knowledge-Sync: main@2450bbb / GLOBAL_KNOWLEDGE_V1。
