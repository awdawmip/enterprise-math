# PREFIX-302｜逐 Port、相干参考与未来门闭包的最小充分来源商

**已完成且不重复：** PREFIX-298 的 S3 984 Port 轨道、PREFIX-299 的 S4/S7 各六个左轨道、PREFIX-300 的 T 与固定 E/Ec 标签反例、PREFIX-301 对 384 个来源 C4 单项变换及 16 对相位的完整固定标签分类。固定 q 稳定群恰为 C4；允许每个 q→q' 时四种来源对角门，九输入证书有效；未同步来源参考导致所有非恒等整体相位重新可区分。

**首个可执行问题：** 明确定义允许的未来门集合 K（仅行单位相位、保留三条 Port 置换、或加入一条未同步参考相干合并），对既有全部 S4/S7 各六个代表 F_{4,q}(M), F_{7,q}(MT) 证明哪些源变换使 E/Ec、逐 Port 正质量和所有指定未来组合观察同时因子化。给出在该 K 与观察范围内的最小充分状态、精确 intertwining 或具体 BRC 反例；不能把任意 Q(i) 形式门当作真实原生 Detector。避免重算旧轨道枚举。

**第二可行分支：** 对逐 Port / 联合参考的 Hermitian 观察，建立比九探针更紧的、或证明九探针不可缩的精确 BRC 证书；区分两事件质量、全保留输出、带来源路径、带外部参考四种强度。

**原生待验证：** 当前 Owner/CLAIM 读取 CONTROL_QUOTA；后续若获得真实 Source 权限及 model_law_id，核对原生 X6 Cell、场、源路径、边界、环境和测后状态、三维切片实际嵌入及独立时间类型。当前文件作者侧 UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING。

**复核：** 在本 PR 目录执行 node verify_prefix301.js；可读证据 SUMMARY_PREFIX301.json，全量结果使用 base64 -d + gzip -d 解码 RESULTS_PREFIX301.json.gz.base64，校验原始 SHA-256=a5febe6e53fa55854a5732cf2d57baf15beb6001290d9288f4926d3fe09cf2c7。