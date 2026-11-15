# CFD 八任务公开先例与剩余贡献边界：首轮来源核验（2026-11-16）

Formal Task: RS-CFD-PRIOR-ART-AUDIT-20260910
Publication: TP2-C136200E29852C806DED
Project source: awdawmip/enterprise-math@d1f559dc158f1634227da8c4216eefe833d22616
Status: SOURCE-BACKED EXPLORATORY AUDIT / NOT AN INDEPENDENT PERFORMANCE REPLICATION / NO MATHEMATICAL ADMISSION

## A. 保留的既有实验，不重复计算

原 2D 验证文件：research_notes/CFD9R2K7/cfd_public_algorithm_probe_20260910.json @13a7cdc9dfac3b7f6d7120f7b020733d7c91f964（Git blob cdce8cb621d310f37997e3d29a11b0a0e98e584d）。对象是二维周期零均值涡量的有限 Galerkin RHS，保留输出波矢、共轭、分支次序；它不是三维 NS 轨迹或 PDE 证书。

原 3D 探针：research_notes/CFD-B1F673/prior_3d/probe.py（Git blob 2e7056530cad8b0b6341290ffc70c88aab486b1f），保留生成的输出模式与 Leray 投影。旧压力接口探针与原结果：research_notes/CFD-B1F673/prior_chat_bundle_20260910/prior_local_main_results.json，Git blob 89174e5e15838adcd3246bbad6b32eb0e515d1fc；在已测案例中旧的仅投影速度接口会遗漏原始压力读出，压力相对误差约 1。新比较应始终区分投影速度、原始非线性项与压力恢复。

原作者既有完整轨迹：research_notes/CFD-B1F673/main/summary.json @e40e5303234c5e8bd725528aad9bff9edf0c059d，Git blob 7808b5ee3aa164642ad3fe1f4549ad471ca33762。八种输入，每种 10 步 RK4、五次计时，报告最大轨迹相对差 6.25e-17、无删模。N=32 剪切例 local FFT/hybrid≈3.58，N=64 剪切例≈3.71；N=32 稠密输入约 0.992。实际 spectralDNS 没有运行，结果属于作者本地定范围实验，尚未经过独立验证。将其作为已保存的前沿证据，避免重复生成相同微基准。

## B. 公开先例与任务逐项对照

| 现行科学任务 | 最接近公开技术与原始来源 | 精确重叠 | 仍值得验证的差异及有界表述 |
|---|---|---|---|
| SPECTRAL-HYBRID | spectralDNS 公共程序，https://github.com/spectralDNS/spectralDNS ，其中 NS.py 的周期伪谱、FFT、3/2 去混叠及湍流缩放基准 | 频谱非线性、FFT、Leray、稀疏卷积、支持度转换属已知手段 | 区分带动态输出支持集合的 sparse/FFT 自动切换和可复用多次时间步；将支持探测、分支生成、稠密回退、压力恢复计入真实总成本。现有已存局部轨迹的剪切加速是有界工程证据；尚未验证对外部谱求解器的独立持续优势 |
| ROUNDING-ENVELOPE | FLINT/Arb 正式 ball arithmetic 算法，https://flintlib.org/doc/algorithms/ball-arithmetic/overview.html ；Johansson (2017), DOI 10.1109/TC.2017.2690633 | 外向舍入、带宽保真的区间半径、正确覆盖精确值、严谨点积已有成熟理论及代码 | 与 Arb reference 对照，为指定二维/三维有限 Fourier 端口设计更便宜的非负外包络。要证明含零/次正规数/上溢/无穷输入的包围性，并同时测构造成本、紧度；有限-map 包络不自动含 PDE/离散时间误差 |
| CANCELLATION-GROUPS | 经典 Fourier 卷积、线性投影及三角不等式，谱软件 spectralDNS 同上；Arb dot 产品具已知有界误差 | 输出模式上分组求和、向量/复数相消、点积误差包围本身不新 | 仅将具有相同真实输出 k=p+q、相同观察者/投影约束、保留共轭与来源的分支放入合法分组；检验 ‖sum_g sum_{(p,q) in g} v_{p,q}‖ <= sum_g ‖sum_{(p,q) in g}v_{p,q}‖，并按方向误差加外包络。比较逐支、合法分组及精确求值的松紧和开销；同模长 |k| 却不同 k 的合并是明确的反例场景。正 BRC 递推不提供复数符号相消界 |
| TRAJECTORY-VERIFY | Chernyshenko–Constantin–Robinson–Titi, J. Math. Phys. 48, 065204 (2007), DOI 10.1063/1.2372512；Dashti–Robinson, DOI 10.1137/060677537；spectralDNS 官方实现 | 数值残差与强解存在性之间的后验验证理论已存在，时间收敛与能量/散度守恒检验已有先例 | 先独立重演完整有限 RK4 轨迹、谱状态、压力和输出，再**另行**验证所选 NS 鲁棒性定理全部强解/范数/初值与强迫条件。项目目前作者本地 8-case 成果不是 PDE a posteriori regularity 的已证应用，也不证明外部 solver 加速 |
| ROM-ITHACA | ITHACA-FV 官方 finite-volume/OpenFOAM ROM https://ithaca-fv.github.io/ITHACA-FV/ 及 Stabile 等 POD-Galerkin, DOI 10.1515/caim-2017-0011；Stabile/Rozza stabilized incompressible ROM, DOI 10.1016/j.compfluid.2018.01.035 | POD-Galerkin、DEIM、参数化降阶及固定几何/参数多查询已有公开软件 | 预选单一压降/流量观察量，用 POD/DEIM baseline，测离线训练、快照、在线重复调用、回退/富化与输出误差。区别只可能是固定任务下经证明/验证的观察量安全适应策略及总成本优势 |
| AMR-BASILISK | Basilisk 原始自适应 wavelet 说明与 adapt_wavelet 实现 https://basilisk.fr/sandbox/Antoonvh/the_adaptive_wavelet_algorithm ；Bruchhäuser/Margenberg/Bause 2026-07 DWR Navier–Stokes goal-oriented space-time adaptivity https://arxiv.org/abs/2607.00686 | 依据场量局部 wavelet 截断误差细化与目标泛函驱动 DWR 加权都是公认先例，2026 已明确用于 NS | 在相同 BC/误差目标下，对比 wavelet 与 DWR/dual baseline；测目标误差、质量守恒、原始+伴随求解、指标/自适应和全部时间。一个“针对观察量”的指标自身并非新意，只有成本/稳定性/证明指标的精确差异才可主张 |
| PRESSURE-GAMG | OpenFOAM GAMG 官方资料 https://doc.openfoam.com/2306/tools/processing/numerics/solvers/multigrid/rtm/GAMG/ ；块 Schur 补、静态凝聚与多重网格都是既有数值线性代数技术 | 矩阵块消元、粗格聚合、迭代解算和重复右端数据已有方法 | 先确定同一个压力算子、边界条件、零空间/规范、压力端口及通量观察量。实测 setup+fill-in+存储+多个 RHS 解算+残差/压力/通量恢复的全成本；只有对特定重复几何算子的净优势才能建立工程意义，不宜将 Schur/GAMG 通法包装为新算法 |
| LBM-CODEGEN | lbmpy 原始开源工程 https://github.com/lssfau/lbmpy ；Hennig–Holzer–Rüde, SIAM JSC (2023), DOI 10.1137/22M1531348 | 碰撞算子符号化、中心矩/累积量变换、算术最简优化和自动生成 CPU/GPU 核函数已有先例 | 固定 D2Q9/D3Q19 一种 stencil、碰撞/边界和 device；寻找 lbmpy 不提供的合法变换，证明矩守恒和边界相容，对比内存流量、吞吐与全部内核；如无可验证 gap，返回已先占/无新变换的有界结论 |

说明：本表以精确的核心公开论文/项目文档证据证明“构件已有先例”，没有进行全球论文/专利穷尽检索；残余差异是**可检验研究问题**，并非已证明原创性或性能。

## C. 同等成本与证明口径

对每项声称提速的计算统计构造和校验：原输入→表示构造、预处理/FFT 计划、变换、时间积分每步、模式提取/内存/设备数据搬移、输出恢复、后验验证、ROM 离线训练和不同查询次数下摊销。算法成本变量不能从结果中隐藏。

如给出“数值证书”，将以下三个层次分别保存：有限 Fourier RHS 相等性；完整有限时间积分轨迹及其误差；连续 Navier–Stokes 的满足全部条件的后验存在性/误差判定。每一层有独立条件，不能从较弱层提升。

推荐先选具有明显判别性的实验：一是 spectral hybrid 全轨迹随支持膨胀自动退回 FFT 的真实总成本与压力观察量；二是方向/共轭保持的 grouped defect 外包络的紧度和开销。其它方向根据实际当前 owner 与研究需求自然进入，保留已完成科学文件。

## D. 证据与待复核边界

- 原科学输入 GitHub @固定版本真实回读；没有以当前 HEAD 缺少原 2D 文件误判科研丢失，2D 文件在上述固定提交存在。
- spectralDNS、ITHACA-FV、Basilisk、lbmpy、Arb 的原始项目来源和两篇 NS 后验定理均已核对；引用保留可访问 URL。OpenFOAM GAMG 的指定文档在本轮浏览返回 403，其官方页面定位可用但**此轮未读到完整当前内容**，具体 GAMG 数值选项需从源码/其他官方可读文档再次检验。
- 对外部代码实际复用时按具体版本复核许可证与依赖，本矩阵没有执行或安装外部 solver，也不声称完成独立复现实验。
- 下一个研究者在原 task/CLAIM 内可扩展这一矩阵、补足原始论文的具体 theorem 假设，形成本 Task 的完整 dual-digest Result。数学审核仍留给独立 Driver。

