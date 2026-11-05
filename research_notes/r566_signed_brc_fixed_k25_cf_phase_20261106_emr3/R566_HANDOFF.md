# R566｜固定 k=25 signed BRC 作者侧交接

来源：冻结 R462@18783e01e3646c72b7aab3b16d3f565e83e6446f；作者侧前沿 R565@e6e4786ab7d957e33523d2e6dfc9eb47e510925b；适用规范当轮从 current main 获取。P000、ACTIVE 世界观没有改动。

科学增量：固定 k=25、d=49 的 Toeplitz–Hessenberg 整数行列式正负自然密度各1/2，零项有限。49个严格有理 Rouché 根圆盘、1176对不交；唯一最大模共轭根对，余根严格较小。主导相位包络宽约1.5321e-24，若有理则既约分母≤11063808；精确有界分母最近候选439103/1440142位于包络外。结合 Weyl 和 Skolem–Mahler–Lech 完成无限阶证明。

执行证据：本地 Python 3.13.5/SymPy 1.14.0等价实现实际运行得到 R566_K25_HALF_DENSITY_AUTHOR_CERT_PASS。m=0..1024 精确统计 +512/-513/0零/311换号；50项H恒等式、12阶独立Berkowitz一致。归档脚本已从远端回读，逐字节重建的本地版本 Git Blob 与远端完全一致（`cc34d1be1f5784c276c28aa4fa7179b775896f01`），且独立重跑通过；标准输出与归档原始证据逐字节一致。

状态：AUTHOR_SIDE_EXACT_COMPUTER_ASSISTED_PROOF；UNREVIEWED；NOT_ADMITTED。GitHub项目仓库分支存储并非正式 Native CLAIM/Result。Native 原生精确任务查询于本轮返回 `SUCCEEDED`，任务 `RS-X6-NATIVE-ROTATION-DYNAMICS` 状态 `READY`、Owner=`taskbook/unassigned`、无当前 CLAIM，`execution_authorized=false`；该 owner 仅为原生 X6 任务状态，不为本标量作者侧成果授予任务身份或审阅权。

下一单元：固定 k=26 的51次根盘/相位证书，及适用于所有 k≥5 的统一根分离+无理性判据；原生 X6 旋转动力学另依正式授权接续。
