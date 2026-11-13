# R615 研究交接｜signed BRC 全局类型门的信息精度层级

日期：2026-11-08；UNREVIEWED / NOT_ADMITTED。冻结科学源：R462@18783e01e3646c72b7aab3b16d3f565e83e6446f，research_notes/r388_signed_k3_corank16_20261029_emr3/r388_exact.py，θ=0，12条 signed K/J 与 B₀=1+t。

接续 R614 的层级门探针，新增三层精确信息分解：（一）同一类型形式权 u_i 只保留计数向量 m，其权为多项式多重系数乘支路 K_i 幂及终点贡献 T_r；（二）类型布尔门 z_i 只保留支撑集 S，全部完整 B_s 布尔响应经 Möbius 逆变换精确恢复每个 S 的汇总权；（三）只有不同层级地址 g_(s,i) 才能分别定位有序历史。另证明初始化幅度 B₀(x)=x(1+t) 的 x-响应恰为所有以 B₀ 为终点的历史总和，求取时无需先挑选具体历史。

冻结 signed K₁=2+3t、K₂=−t+4t²+4t³ 上的严格证书：D_z(2,1) 中支撑 {1,2} 的类型门响应为 12，R614 两种有序地址的响应各为6。[t²][x]B₅ 中计数 m=(3,1)、(1,2) 贡献分别为 −48、6；二值类型门同支撑聚合为 −42，原始四点完整 B₀ 来源响应依次为 (0,960,0,918)。所述分离属于真实 K/J 辅助历史模，物理 X6 合法干预映射待核。

归档 R615_VERIFY.py 实际执行 Python 任意精度整数核验：160组布尔整状态、160组 Möbius、894条有序历史、71组 Parikh、160组整状态/B₀ 响应全部通过，PASS: R615_SIGNED_TYPE_GATE_HIERARCHY_EXACT_PASS。执行证据 R615_EVIDENCE.json 的 SHA256=87bddef8937df0aff93bb96859e0ba87868dcb264682a349fd159ce4fa5b1981，验证程序的 Git blob=dcae10db0bcccf4a3c467c502a27eb8f7f0ab8e5。

下一问题：逐项核对冻结 R462 与现行 X6 联合状态接口，明确允许的原生更新与联合读出，检测是否存在实现类型门、B₀ 来源响应或层级边地址的保持映射；必要时对真实未来操作集重新计算最小保真商。辅助类型 K_i 不是未经证明的 ±E_i 映射，递推层级不是心跳时间。控制端本轮实际返回 BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE / operation_sent=false；Researcher-ID、活跃 Owner、CLAIM 未确认，独立 Driver 审查待办。
