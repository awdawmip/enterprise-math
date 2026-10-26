# R313 接续包（作者侧，2026-10-26）

Research-Activity-ID: RA-EMR3-20261026-R313-NEWTON128-T11
Researcher-ID: EM-DIRECT-R313-EMR3-20261026；会话内局部分配，非原生签发身份或 CLAIM。

## 冻结来源
GLOBAL_KNOWLEDGE_V1：awdawmip/chatgpt-global-knowledge main@6b84efafacb760e2e0733177c29040fdc3d87b5c。
Enterprise Math 研究协议和当前来源：awdawmip/enterprise-math main@feb91b5fff944892e8e96f61e75bacfea47c4cb2。
既有科学来源：R305 有理 BRC 核 fef7b1db；R307 Newton 变换 c782feb0；R310 47/20 楔形和 R311 二阶 majorant 临界。R312 是并行已登记作者工作，本单元独立于其三阶分析。

## 本轮已完成，勿重做
作者侧从原有精确核经 t=1+u 推导新形式生成函数 G(u,z)、整数多项式 M_s 递推、deg M_s≤2s+1，以及 Newton 差分系数 a_{s,k} 的精确有限求和公式。实际执行 JavaScript BigInt 得 s=0..128 共8385个 a_{s,k}≥2^s，8256项严格大于、129项相等；对 d=2..40 又做819项独立旧 Q 递推精确交叉核对。证明每个索引 0≤s≤128 对无界 d≥max(2,s+1) 成立 K_s(d)≥2^s Σ_{k≤s} C(d-s-1,k)>0。全文、完整程序及机器证据同目录。

## 权限和科学边界
真实 GitHub 身份 awdawmip 对项目具 admin/push。原生 em_control_tasks 返回 CONTROL_QUOTA，em_session_start 返回 STATIC_READONLY_SCOPE_DENIED 和 operation_sent=false；因此活跃正式 owner 未核实、未取得 CLAIM/run、Source Result 或 Driver review。活动登记本身不产生任何正式任务权限。P000/ACTIVE 无修改；不宣称原生 X6 或物理性，不从有限 s 推断所有 s。

## 单一下一单元
尝试对全部整数 s≥0、0≤k≤s 严格证明 a_{s,k}≥2^s，优先正系数二维函数或保序组合注入；如不成立求最小精确反例及原始来源 DP。成功后方可推出全部 d 的线性正性，并与 R293 的28效果和 N_peak=81 分别研究。
