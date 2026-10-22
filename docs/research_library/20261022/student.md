# Student／Parity 成果与公式摘录

整理基准：`main@63f87045b456cf573a9eaa7bbc8d4a4673a3e6ea`，2026-10-22（Asia/Shanghai）。本页是既有文献的检索与复用整理；审核状态引用已有报告，未新增数学投票或形式化认证。旧研究探索继续暂停。

这些结论属于明确的经典有限矩阵／解析模型。项目心跳世界原生 X6 与单独定型的时间约束保持不变；下列分析没有建立完整 X6 传播或物理解释桥。

## student.actual_column.right_semicircle_obstruction

**实际奇偶列的开右半圆一致多项式损失阻碍。** 作者 EM-DVR-BFF6DC；已有 EM-PUBLIC-7CDA51 的 NONBLIND 完整技术审核，报告为有限范围 PASS、零 must-fix。作者原稿创建时的 UNREVIEWED 字样保持历史含义。

固定整数 \(m\ge2^{1000}\)、\(64\sqrt m\le z\le m/256\)。令 \(n\) 为不超过 \(m-2\) 的最大偶数，
\[
B_j=\binom{2m-1}{j},\quad c_l=\frac{B_n}{B_{m-l-1}},\quad
c_0=\frac{B_n}{B_{m-1}},
\quad J_m=\{1\le l\le m-3:l\equiv m-1\pmod2\}.
\]
该集合正是原始 Green 输出行 \(r=0\) 的真实掩码 \(L\) 偶数、\(2\le L\le m-2\) 在 \(l=m-L-1\) 下的像；未插入虚构的 \(l=0\) 列。使用解析平方
\[
S_m(w)=\sum_{l\in J_m}(2l+1)c_lj_l(w)^2,\qquad
C_{\rm pol}(z)=\sum_{k=0}^{m-1}
\frac{z^{2k}}{(3/2)_k(m-1)_{k,\mathrm{fall}}}.
\]
整函数球 Bessel 的精确相位 \(j_l(iz)=i^li_l(z)\) 使完整选定和在 \(iz\) 同号，给出
\[
|S_m(iz)|\ge\frac{c_0e^{2z}}{16z^2},\qquad
C_{\rm pol}(z)\le e^{4z^2/m}\le e^{z/64}.
\]
对每个允许的固定 \(m,z\)，存在依赖于它们的 \(\eta_{m,z}>0\)，使
\[
\frac{|S_m(ze^{i\theta})|}{c_0C_{\rm pol}(z)}\ge e^z,
\qquad \pi/2-\eta_{m,z}<\theta<\pi/2.
\]
因此不存在固定 \(C>0,p\ge0\)，使 \( |S_m(w)|\le Cm^pc_0C_{\rm pol}(z)\) 在全部允许 \(m,z\) 和整条开右半圆一致成立。

适用边界：结论针对这个真实标量列参考界。未证明固定角 \(\pi/3\)，未给出一致正角宽，也未给出完整 \(F/Z\)、\(A_e\) 迹或 \(\Psi\) 的下界／no-go。其他项的相位抵消仍需保留。已有局部 \(\Psi\) 定理不因此改变。

方法归类：**COMPOSE_APPLIED / RESULT_ONLY_STANDARD_APPLIED_COMPOSE**。可复用的是真实掩码、同相位正和、低列精确双曲函数界、全部有限下降阶乘参考上界与连续性量词；不创建新工具族。

来源：[作者原稿](https://github.com/awdawmip/enterprise-math/blob/71d999a4df543940234f52376dbc8c860e4e4d35/research_notes/owner_goal_20261017/student_offcircle_actual_column_bff6dc/ACTUAL_STUDENT_PARITY_COLUMN_RIGHT_SEMICIRCLE_OBSTRUCTION_WORKING_V1.md)；[完整技术审核](https://github.com/awdawmip/enterprise-math/blob/181b65a06b210fdff5c2add3fc69457e065b31b1/research_notes/owner_goal_20261017/reviews/student_offcircle_actual_column_nonauthor_7cda51/ACTUAL_STUDENT_PARITY_COLUMN_RIGHT_SEMICIRCLE_NONBLIND_COMPLETE_TECHNICAL_WHOLE_REVIEW_AND_CONTEXT.md)。

## student.complete_psi.local_zero_free_disk

**完整原始 \(\Psi\) 的归一化局部平台、无零与对数界。** A（EM-PUBLIC-7CDA51）构造 INPUT 与完整 CONSUMER；BFF（EM-DVR-BFF6DC）构造 OUTPUT 并组装主稿。已有 EM-DIRECT-9F7A5C 的一份 NONBLIND 完整技术审核，报告为有限范围 PASS、零 must-fix。三个组件合计构成一个整体成果，作者互查与组件数不增加独立票数。

采用原始
\[
V=\mathbb C[v]_{\deg\le m-2},\quad
\langle f,g\rangle_m=\int_{\mathbb R}\overline{f(v)}g(v)(1+4v^2)^{-m}\,dv.
\]
在原实正交归一基中，\(D\) 为导数矩阵、\(J=-iD\)、\(X=vD-(m-\tfrac12)I\)，并保留完整
\[
Z_\lambda=X+\sum_{a\ge1}\frac{B_{2a}\lambda^{2a-1}J^{2a}}{(2a)!},
\quad
A_e=\Pi\frac{1/4-v^2}{(v^2+1/4)^2}\Pi.
\]
该和在原载体上有限终止。符号 \(\#\) 是固定解析参数的系数转置；在非实参数处不能换成移动 Hermitian 伴随。\(A_e\) 为不定算子，不能换成正定／概率模型。

令 \(n\) 为不超过 \(m-2\) 的最大偶数，\(h_j\) 为该配对下 monic Student 多项式 \(P_j\) 的平方范数。
\[
\ell=n-1,\quad q_{\rm rev}=2\ell,\quad
H_n=n!\sqrt{h_0/h_n},\quad C_\xi=H_n/(2\pi)^n,
\quad \mathcal P(w)=(w/\pi)^{q_{\rm rev}}\Psi(\pi/w)/C_\xi^2.
\]
对整数 \(m\ge2^{1000}\)，固定
\[
128\sqrt m\le z\le m/512,\qquad
\rho=2^{-16}\min(z^2/m,m/z).
\]
已有成果为
\[
\mathcal P(z)>0,\quad
|w-z|\le\rho/256
\Longrightarrow \mathcal P(w)\ne0,\quad
\tfrac12<|\mathcal P(w)/\mathcal P(z)|<2.
\]
在较小圆盘 \(|w-z|\le\rho/512\)，存在在 \(z\) 归零的解析对数，满足
\[
|\Log(\mathcal P(w)/\mathcal P(z))|
\le2^{10}|w-z|/\rho.
\]
原始 \(\Psi\) 的精确因子必须保留：
\[
\frac{\Psi(\pi/w)}{\Psi(\pi/z)}
=(z/w)^{q_{\rm rev}}\frac{\mathcal P(w)}{\mathcal P(z)},\qquad
\Log\frac{\Psi(\pi/w)}{\Psi(\pi/z)}
=-q_{\rm rev}\Log(w/z)+\Log\frac{\mathcal P(w)}{\mathcal P(z)}.
\]
指数是 \(q_{\rm rev}=2\ell\)，不是普遍二次因子。常数平台属于 \(\mathcal P\)，不能直接用于 raw \(\Psi\)。

可复用内部接口：在 \(64\sqrt m\le s\le m/256\)、\(\Re w>0\)、\(|w|=s\)、\(|\Im w|\le s^2/(64m)\) 上，\(E_Z(s)=\|Z_{\pi/s}\|_{\mathrm{HS}}^2\) 给出
\[
|\operatorname{tr}(A_eZ^\#Z)|\le2^{40}E_Z(s),\quad
|\operatorname{tr}(A_eZZ^\#)|\le2^{10}E_Z(s),\quad
|4\tau\operatorname{tr}(A_e(Z+Z^\#))|\le E_Z(s),
\quad \tau=(m^4-1)/(24m).
\]
完整 consumer 在实际包含圆盘内取移动半径 \(s=|w|\)，先除精确 raw 平方，再比较实参考量并支付 Cauchy／Euler 导数。所有实际奇偶掩码、BY、外行、基线／\(\zeta\) 交叉项和单／双 raw 因子都保留。

方法归类：**COMPOSE_APPLIED / RESULT_ONLY_COMPOSE**。INPUT、OUTPUT、CONSUMER 均保留在整体证明中，不各自制造新工具或新审核票。上游 17239 pole 接口、62848 partial whole、23181 circle／remainder 继续按原来源复用。

适用边界：仅上述局部圆盘。全原点圆、外弧、全局 COMMON 裕度、系数抽取／符号、\(4/5\) 指数和原母目标仍未完成；没有 Native 动力学或物理时间结论。

来源：[完整主稿](https://github.com/awdawmip/enterprise-math/blob/444f6f12adac1e2b6fe40fdfba433189d15ecf23/research_notes/owner_goal_20261017/student_actual_full_psi_local_zero_free_joint_7cda51_bff6dc/ACTUAL_STUDENT_COMPLETE_PSI_NORMALIZED_LOCAL_PLATEAU_AND_ZERO_FREE_JOINT_AUTHOR_WORKING.md)；[typed 接口](https://github.com/awdawmip/enterprise-math/blob/444f6f12adac1e2b6fe40fdfba433189d15ecf23/research_notes/owner_goal_20261017/student_actual_full_psi_local_zero_free_joint_7cda51_bff6dc/TYPED_ACTUAL_STUDENT_COMPLETE_PSI_LOCAL_ZERO_FREE_AND_OPEN_SCOPE_WORKING.json)；[作者 context](https://github.com/awdawmip/enterprise-math/blob/444f6f12adac1e2b6fe40fdfba433189d15ecf23/research_notes/owner_goal_20261017/student_actual_full_psi_local_zero_free_joint_7cda51_bff6dc/CONTEXT_ACTUAL_STUDENT_COMPLETE_PSI_LOCAL_ZERO_FREE_AUTHORS_INPUT_REUSE_AND_OPEN_LIMITS_WORKING.json)；[完整技术审核](https://github.com/awdawmip/enterprise-math/blob/7995416c9636fb77dc4ceb7ed0f8cf8569f304e6/research_notes/owner_goal_20261017/reviews/student_joint_functional_independent_9f7a5c/INDEPENDENT_COMPLETE_STUDENT_PSI_LOCAL_DISK_TECHNICAL_WHOLE_REVIEW_AND_CONTEXT.md)。

## 未解决输入与去重边界

[已发布 frontier](https://github.com/awdawmip/enterprise-math/blob/341ea3fb3b06d32b16208d523dd5b7fdf6037f39/research_notes/owner_goal_20261017/control_recovery/OBSERVED_RESEARCH_FRONTIER_20261017T141641Z.json) 仍列出原始 Student 系数调用的精确多项式／轮廓定位缺口（SOURCE_LOCATOR_GAP）。局部完整函数义务已有上述成果；系数调用尚不能由不存在的 locator 代替。

现有工具／定理入口路由核对未发现这两项的专门采收条目；这不是全库语义穷尽或全球新颖性声明。两项保持为两个有来源的结果索引，不改写基础定理 T001–T015，也不把负面方法边界扩为全局否定。

