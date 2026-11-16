# R396｜带符号 BRC K3 参数形变，第24余阶有限 PF₂ 全参数分类

日期：2026-10-30。类别：AUTHOR_SIDE_EXACT / DRIVER_UNREVIEWED / NOT_ADMITTED。

## 输入、定义、观察者

本轮接续 R395（Git commit 97e3a456eae6f256dfe970cd0c956a32736a8f3c），沿用 R346 原始带符号十二支路 K/J（原始 Git blob 1579ceb717ab1945227eca4f7a1878bf4ffa73e1）。仅将 K3[t²]=−8 改为 K3[t²]=−8(1+θ)，θ>−1。始终保留支路符号、乘积和交叉抵消，不将 signed BRC 错当非负质量。形式变量及有限序列不定义 P000 原生六轴动力学。

按原始递推定义

\[
B_0(t)=1+t,\qquad B_s(t)=J_s(t)+\sum_{i=1}^{\min(12,s)} K_i(t)B_{s-i}(t),\quad b_{s,q}=[t^q]B_s,
\]
\[
D_{q,u}=\sum_{w=0}^u(-1)^{u-w}\binom uw 2^{q-w}b_{q+w,q},\quad
H_r(u)=5^{-u}D_{r+u,u},\quad L_r(v)=5^rH_r(v),
\]
\[
Q_r(v)=L_r(v+1)L_r(v+2)-L_{r-1}(v+2)L_{r+1}(v+1),\qquad c_j^{(r)}=\Delta^jQ_r(0).
\]

固定 r=24，构造 49 项 C24=(c0,…,c48)，47 个 Turán 缺陷 T_j=c_j²−c_{j−1}c_{j+1}（1≤j≤47）。有限 PF₂ 在此按非负、无内部零与全部 Turán 非负判别；通过段实际有严格正支撑。

## 精确主定理

令 a=1868232/1000000，b=1868233/1000000，η24 为 T25 在 (a,b) 内的唯一实根。则

\[
\boxed{C_{24}(\theta)\in PF_2\quad\Longleftrightarrow\quad -1<\theta\leq\eta_{24}.}
\]

η24≈1.8682325275324574 仅用于显示；严格符号全部来自有理整数证书。

还得到固定第24余阶的完整多项式恒等式

\[
\boxed{c_{48}(\theta)=1289904147324(30-16\theta)^{48}},
\]

常数等于 Catalan(24)=binom(48,24)/25。此处不从固定阶断言所有 r 的公式均已独立证明。

在 θ*=15/8，c25,…,c48 全部为零，T25 关于参数恰四阶消零，T26 恰八阶消零；然而 T22<0、T23<0，故退化并未恢复 PF₂。高阶消零阶数来自整系数多项式的精确求导与该有理点判等。

**次生零点：**T25 在 (1881908/1000000,1881909/1000000) 内有另一个唯一简单根，约 1.881908035083143；T25' 在该区间严格正，T25 左负右正，但 c25 在整个区间严格负，因此单个 Turán 恢复不意味着 PF₂ 恢复。

## 完备证明：精确区间证书

r396_symbolic.py 从原始十二支路递推构造全部 c_j(θ) 和 T_j(θ)，均以升幂整系数记录。r396_exact.py 在七个有理 θ 点直接使用 Fraction 对原始 K/J→B→D 计算，与符号多项式代入交叉核验，共 (49+47)×7=672 项精确相等。这验证了两条实现的一致性；不构成外部独立审稿。

对于整数多项式 p，精确计算其在有理区间 [x,y] 上的 Bernstein 展开：
\[
p(x+(y-x)t)=\sum_{i=0}^n\beta_i\binom ni t^i(1-t)^{n-i}.
\]
所有 β_i 严格正即可证明整个闭区间上 p>0。脚本用 Fraction 实现有理控制点；多段叶区间首尾相接，不遗漏边界。

程序 r396_certify.py 实际验证：

1. 全部49个 c_j 在 [-1,b] 严格正；除 T25 外的46个 T_j 在 [-1,b] 严格正；T25 在 [-1,a] 严格正。θ=−1 只作闭区间证书端点，并不添加至 θ>−1 的模型域。
2. T25(a)>0>T25(b)，−T25' 在 [a,b] 严格正，因此 T25 在 (a,b) 有且只有一个零点 η24；对 θ≤η24 满足有限 PF₂，区间 (η24,b] 中 T25<0。
3. [b,4] 由10个连续叶区间覆盖，每段均存在某个 c_j<0 或 T_j<0 的严格 Bernstein 证书，因此整个 [b,4] 排除 PF₂。
4. 令 θ=4+u，u≥0；−c0(4+u) 的全部15个非零幂系数严格正，故 θ≥4 整个无界尾部 c0<0。第1—4步覆盖全部 θ>−1，主定理成立。
5. 对次生根区间独立核验端点异号、T25'>0 和 c25<0。退化点的系数消失、负 Turán 及四/八阶消零也由精确多项式逐次求导核验。

精确运行结果：R396_SYMBOLIC_PASS，R396_EXACT_PASS；100个证书对象、109个连续有理叶区间、112次 Bernstein 检查、6563个严格正的有理控制系数，最大细分深度9；另有672项原始 Fraction 交叉核验。独立解压/复制目录重算后，R396_POLYNOMIALS.json 与 R396_EVIDENCE.json 均逐字节一致。

原始证据 R396_EVIDENCE.json 经 gzip 无损保存在本目录的 R396_EVIDENCE.json.gz；SHA256(原始证据)=3a6f820c8e87f5bc70bf19917ee5f758cdbb9e4e02ab0b48227e44da35c8c39b。约 929 KB 的 R396_POLYNOMIALS.json 由 r396_symbolic.py 精确重建，SHA256=02aa2874583553945c6ca528a7c6aff1335985c3a2269b673834716800225d3f。详细命令及恢复方式见 R396_EVIDENCE_INDEX.md。

## 证据边界、状态、下一问题

定理限于原始 signed BRC 辅助组合模型的固定 r=24 有限 Newton 序列；没有跨越全部余阶、无限 Q、整个 D 阵列 TP₂、P000 X6 动力学及外部物理对应的证明。本轮作者侧证书等待独立 Driver 数学审查。原生状态检查 research_authority_granted=false，任务查询 CONTROL_QUOTA，正式 owner 未得到权威确认；不声称 CLAIM、Result、Review 或入选 Working Truth。P000、ACTIVE 世界观及正式 Task 状态保持不变。

固定规范源：GLOBAL_KNOWLEDGE_V1 main@1f0b8985fd6ca8804198fa97a9563db09a0f0e0d；Enterprise Math main@866cf57e4ff5cb66f7d29e155cecee61a072c5df。

**下一数学单元：**推进 r25 的51项有限 PF₂ 全参数分类；另取偶数 r 退化点 T_{r+1} 四阶、T_{r+2} 八阶消零为候选结构，寻找全偶数 r 证明或反例，并分析 η_r 的奇偶交错和渐近尺度。