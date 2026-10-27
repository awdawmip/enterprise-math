# PREFIX-285｜C4-BRC奇异伙伴的最优自适应单探针与对角信息失辨

**类别：AUTHOR_SIDE_EXACT_PROOF / EXACT_C4_BRC_CHECK / NATIVE_HN_DETECTOR_PENDING / NOT_ADMITTED。**

## 固定输入、问题与来源

GLOBAL_KNOWLEDGE_V1 固定于 \`awdawmip/chatgpt-global-knowledge@b93af5fa5d1f56cff9a63f730c86247619d79b86\`；同一快照已读取规范入口、P000启动投影与原件（原件Git Blob \`770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc\`）、ACTIVE《我眼中的世界》、数学与代码规则、BRC研究政策。Enterprise Math 科学起始提交 \`ca7baa915ffc00ff22552862b84edddc953cf1c6\`，已读取 \`AGENTS.md\`、\`docs/PORTABLE_RESEARCH_PROTOCOL.md\`、心跳BRC唯一运算路径、\`definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json\`、\`definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json\`、\`definitions/HEARTBEAT_SELF_CONSISTENT_INSTANT_V0_1.json\`、PREFIX-284完整证明及后继问题。原始Stage50原件只复用PREFIX-278/282已验证的来源证据；本轮没有重新执行原始Stage50或原生心跳演化。

研究对象是原生六维X6世界内**尚待类型化嵌入**的三条来源历史路径，来源标签 \`j=0,1,2\` 不是空间轴、三维切片定义，也不是心跳编号。

给出带来源C4幅值 \`a=(a0,a1,a2)\`，\`aj=mj ζj\`，\`mj\` 为严格正有理数，\`ζj∈{1,i,-1,-i}\`。定义全部有序来源路径对BRC总质量与相关：
\[
Z=\sum_{j=0}^2|a_j|^2,\quad c_s=Z^{-1}\sum_{j=0}^{2-s}a_j\overline{a_{j+s}}\ (s=1,2),\quad p_0=|a_0|^2/Z.
\]
由PREFIX-284，签名 \`O=(c1,c2,p0)\` 的等端点奇异层 \`|c2|=p0\` 在去掉公共非零倍率后最多留下 \`r=a1/a0\` 与 \`r^\sharp=t\overline r\` 两种解，且 \`t=a2/a0=\overline{c2}/p0\`。在本C4载体中奇异条件推出 \`t∈C4\`，\`|r|=|r^\sharp|=q>0\`。

## 定理1：给定签名后的单次自适应二路C4效应

定义来源0、1的正相干二路BRC观察：
\[
\boxed{J_p(a)=\frac{1}{2Z}\sum_{j,k\in\{0,1\}}b_j\overline{b_k}
       =\frac{|a_0+i^pa_1|^2}{2Z}},\qquad b=(a_0,i^pa_1),\quad p\in\{0,1,2,3\}.
\]
**四个有序来源对**全部保留，不以正质量替代复相位或使用经典传播矩阵。因 \`|a0+i^p a1|²≤2(|a0|²+|a1|²)≤2Z\`，\`0≤Jp≤1\`，互补效应亦为正。这个定义只证明形式载体上的二结果效应，并没有声称原始Stage50或真实 \`H_n\` 存在实施它的Detector。

展开交叉项，奇异伙伴间精确满足
\[
\boxed{J_p(a)-J_p(a^\sharp)=p_0\operatorname{Re}\big(i^p(r-t\overline r)\big).}\tag{1}
\]
选择 \`p(t)=1\` 若 \`t=1\`，其余 \`t=-1,i,-i\` 一律选择 \`p(t)=0\`。则只要 \`r\neq t\overline r\`，**一次所选效应**必严格区分两个候选，而且间隙精确为
\[
\boxed{|J_{p(t)}(a)-J_{p(t)}(a^\sharp)|=
\begin{cases}2p_0q,&t=\pm1\text{且伙伴不同};\\p_0q,&t=\pm i.\end{cases}}\tag{2}
\]
**完整证明。** \`r=qζ\`、\`ζ∈C4\`。当 \`t=1\`，唯一非平凡情形 \`r=±iq\`、\`r-r^\sharp=±2iq\`，取 \`p=1\` 得 \`2p0q\`；当 \`t=-1\`，唯一非平凡情形 \`r=±q\`、差 \`±2q\`，取 \`p=0\` 得 \`2p0q\`；当 \`t=i\`，差恒属 \`{±q(1-i)}\`，其实部绝对值为 \`q\`；当 \`t=-i\`，差恒属 \`{±q(1+i)}\`，其实部绝对值为 \`q\`，均取 \`p=0\`。四种 \`t\` 穷尽，式(2)严格正，证毕。形式测量每次绝对误差≤ε时，\`2ε<\`此间隙可防两个候选的读数误差区间重合；没有声明任何实际实验噪声界。

## 定理2：非自适应单一设置在本探针族内不可能覆盖全部伙伴

任何偶数 \`p\`，在 \`(1,i,1)\` 与 \`(1,-i,1)\` 上均读 \`J_p=1/3\`，但奇数设置可分；任何奇数 \`p\`，在 \`(1,1,-1)\` 与 \`(1,-1,-1)\` 上均读 \`J_p=1/3\`，但偶数设置可分。两对各自的 \`O\` 完全相同。故**单个预先固定的C4二路设置不充分；固定二设置菜单 \`{J0,J1}\` 必要且充分**。给定 \`O\` 中的 \`t\` 后，实际只调用一次所选设置。本最优性限于此声明的C4二路效应族，不扩充到所有可能的复数相位仪器。

## 定理3：来源对角BRC的Z₂信息阻断

对任意奇异伙伴 \`a,a^\sharp\`，有 \`|t|=1\` 且 \`|r^\sharp|=|r|\`，因此三个来源的归一化质量 \`(|a0|²,|a1|²,|a2|²)/Z\` 逐项相同。故所有仅通过这些质量因子化的来源分布、各阶矩、方差与任意对角效应 \`Σ d_j|a_j|²/Z\` 完全不可辨识。PREFIX-282原始Stage50的 \`packet_variance\` 虽区分正实同谱包，却不能消除PREFIX-284的C4奇异伙伴；需要合法**非对角来源相干读出**，或有严格桥接证明的后续来源→可见Port操作。

## 精确执行范围

已实际执行随稿 \`verify_prefix285_portable.js\` 的BigInt有序来源对C4-BRC验证；另一份本地独立Python \`verify_prefix285.py\` 复算了同一有限范围。规范固定 \`a0>0\`，\`mj=1,2,3,4\`，\`a1,a2\` 相位各为C4，故 \`4^3×4^2=1024\` 包；执行 \`2048\` 次直接二源**四有序路径对**效应并同次数与解析式逐一比较。得814种签名，其中704非奇异、110奇异，66种奇异签名有两类不同相对幅值；对这66类都精确核验式(2)、对角相等与自适应一次可分。固定设置的两个反例都PASS。具体 \`(1,i,1)/(1,-i,1)\` 的新 \`J1\` 读数为 \`0\` 与 \`2/3\`。有限枚举核查实现，普遍定理由以上解析证明建立，不把有限核查当作无限一般证明。

## 原生Detector缺口及下一问题

现有固定Source的 \`HEARTBEAT_SELF_CONSISTENT_INSTANT_V0_1.json\` 将一个 \`H_n\` 定义为包含原生X6 Cell、材料、动量、完整场、来源/边界、约束、独立时间或序、\`model_law_id\` 与数值状态的自洽瞬间。本轮明确读取范围未提供同时包含 \`H_n→Detector效应→输出概率→测量后态/损耗\` 的可验证完整接口；这是**已审范围的证据缺口**，绝不是物理上不存在探测器的证明。二路 \`Jp\` 仍为形式候选，不能把重备输入、软件来源分解或历史差 \`r\` 当作真实测量。

PREFIX-286应固定真正的 \`model_law_id\`、原生Cell/Port/材料动量/完整场/来源/边界/独立时间，并证明一个已经准备好的 \`H_n\` 是否允许上述二路相干Detector及互补效应、后态与损耗。若Source不提供，就在列出的实际合法操作闭包内给出完整观测零空间/失辨证书；若提供，执行原始Source并对 \`J1=0,2/3\` 取得真实代码输出。作者侧保存不意味着原生CLAIM/Result、独立Driver审查或数学/物理接纳。

研究身份：当前GitHub认证 \`awdawmip\`，作者侧PREFIX-285研究；原生查询分别返回 \`CONTROL_QUOTA\` 与 \`STATIC_READONLY_SCOPE_DENIED\`，未能可靠核实活跃Owner/CLAIM，未取得会话或审查权限。

