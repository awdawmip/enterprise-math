# 费马数残差方向：首批正式研究任务

用户原始问题：看看残差的累积是不是费马素数失效的原因。
用户本轮授权：把沿着这个方向研究的后续任务发布到任务机。

## 来源与认识状态

本目录 source_archive.zip 是上一轮对话交付的原始压缩包，逐字节保留。
SHA256: 7d2002193d3cb5ef79d699354a86ab0d0082a853623290c89abbdb818b3fb7dd
内含 README.md、verify.py、results.json、MANIFEST.sha256。归档成员摘要已核验；本发布轮没有重跑科学脚本。
原草稿及其计算均为 UNREVIEWED_CHAT_SEED_NOT_ADMITTED；同一对话的发布者不是独立数学审核者。任务发布不改变这一状态。

## 可直接续接的精确问题

令 x_0=2，x_(j+1)=x_j^2，F_n=x_n+1；固定奇数 q 的中心余数截面，x_j=q*A_j+r_j，r_j^2=q*c_j+r_(j+1)。草稿提供 A_(j+1)=q*A_j^2+2*r_j*A_j+c_j 和 u_(j+1)=2*r_j*u_j+c_j (mod q)。第一层命中 -1 等价于 q|F_n，已命中后 u_n=0 才等价于 q^2|F_n。这些须在任务中独立核验，且终点等价式本身不是新预测法。

校准：641 的中心余数为 2,4,16,256,154,-1；u_5=44，不是平方因子。奇素数单位邻域的平方保持 p 进差异阶，但全局 x 与 -x 合并；当前不可见不等于真实消去。截面变更会改变商、进位和高位坐标，整除和赋值才应有不变证书。

## 三项任务及边界

- RS-FERMAT-RESIDUAL-PRETERMINAL-20261004：终点之前的候选族排除、受限信息不足见证与全成本对照。
- RS-FERMAT-RESIDUAL-LIFT-20261004：mod p^3 及有限 k 的完整进位提升、代表元变换与经典结果边界。
- RS-FERMAT-RESIDUAL-MEMORY-20261004：平方载体下的长程保持、真实合并和观察者安全最小状态。

三项是同一直接用户方向的首批正式任务，均无预设执行人、无彼此结果依赖，也不继承旧会话 CLAIM。既有一般 BRC 仿射复合、部分操作商、几何观察者最小化均是复用基线；不以新标题重新发布其通用问题。公开文献的新颖性审查留在各任务内部，不预称未有先例。

父目标：OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS；所选 OPEN generation：OG-7AE66316D7566C519AE0。它维持 OPEN，不因这次发布而关闭。

## 版本与发布证据

Global snapshot: awdawmip/chatgpt-global-knowledge@f9fe058d0e4d7a7350ffa0638c4dcbc8c0a3d93f。
Source policy snapshot: awdawmip/enterprise-math@937aea6bbb6a774d7165a9d8e782940f47248fc4。
Publisher: EM-DIRECT-BE4AEF；activity RA-DFEA732FCF2AF7C1707D2903，Source 路径 research_activity_records/RA-DFEA732FCF2AF7C1707D2903.json。
实际运行的范围明确等价预检与42个变异拒绝测试见 preflight.json；原始当前策略摘要见 policy_blob_manifest.json。preflight.py 为本次预检的可运行实现，不是对项目通用发布工具的替换。

任务书与匹配不可变发布记录须在同一提交进入 main；原始包、任务书、记录及预检证据属于同一发布事务。最终提交号与回读状态由发布回执记录，不在本文件预先冒充成功。
