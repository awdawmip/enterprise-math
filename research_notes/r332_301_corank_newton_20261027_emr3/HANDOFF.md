# R332｜可独立消费的研究接续入口

母目标：正权、有序六边 BRC 辅助组合模型的 Newton 差分正性，继续寻找双指标统一证明或确切反例。研究依赖 R330 commit 7c73f56263c3f0515aa28e55ced2d4c703b8e086 的全指标有理母函数次数界，以及 R331 commit 98e7ccce13c07fa91c816314b01f0681dc7c264e 的 r≤256 精确证书。完整六维原生 P000、ACTIVE 世界观和三维切片仍是研究分类边界，不作物理推广。

本轮已完成且不要重算：新 r=257,…,300 共44条无界正性斜带；c_{r,i}>0 全12,298项；原始 B_s 已算至902；每条多项式 r+1 外插点和 c_{r,r}=6^r 一致；与原 R331 本地全量证据 r256 向量逐值一致。新部分完整有理系数 SHA256 为 6c71dd8fb6285a742788a2d0d8418d9232a54d82678319882310786eaf95f7f2；详细证书及精确数学范围见本目录 R332_PROOF.zh-CN.md 和 R332_EXACT_EVIDENCE.json；R332_VERIFY.py 为实际执行代码的可移植版本。重跑命令：python R332_VERIFY.py --min-r 257 --max-r 300 --out R332_EXACT_EVIDENCE.json，只有标准库依赖；可选 --prior-file 需要原 R331 全量证据，未提供也能执行主要证书。

下一原子单元：r=301 全302项差分，或直接研究固定 r 下 H_r(z) 在整体 r,z 联合增长的正锥不变递推。优先寻找一次覆盖所有 r 的证明；若 c_{r,i}≤0，继续检验实际 D_{q,k} 及原 Newton 域内系数，不混淆充分条件与原猜想。r301..320 的一次执行超过限制后无完整证书，状态仍未检验。

本次全局读取快照 main@df354899f3e5831d052e05de65d9ec10f4b207d2；GitHub PR #1568 是同任务持续交付入口。作者身份为本次实际对话的可移植研究贡献，不借前轮角色会话或独立 Reviewer 身份。em_control_tasks 回应 CONTROL_QUOTA，活跃 Owner、原生 CLAIM、Source Result、独立 Driver review 均未取得；研究仅为 AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED。不得把 PR 或 commit 当作任务原生接纳。
