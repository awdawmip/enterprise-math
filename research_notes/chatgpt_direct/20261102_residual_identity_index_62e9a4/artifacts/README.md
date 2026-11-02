# 完整身份索引复验包

阅读 `RESULT.md` 获取条件、证明、完整成本及失败边界；`SUMMARY.json` 列明每项实际覆盖。

Python 3.11+，使用标准库。依赖固定在 `parent/`，保持原三元内核；无需网络。

```sh
python check_identity_index.py costs --out costs_recheck.json
python check_identity_index.py failures --out failures_recheck.json
python check_identity_index.py audit --slots 1 --out audit_1_recheck.json
python check_identity_index.py audit --slots 2 --canonical --out representatives_recheck.json
python check_identity_index.py hints --out hints_recheck.json
python check_identity_index.py workload --out workload_recheck.json
python check_identity_index.py scaling --out scaling_recheck.json
python check_identity_index.py lifecycle --out lifecycle_recheck.json
python check_identity_integration.py ring_costs --out ring_costs_recheck.json
python check_identity_integration.py ring_graph --case execute_bind --out graph_recheck.json
```

`--canonical` 指明两槽142个一致改名代表，不应改称1900准备全集。初次1900域运行的超时记录在 `VALIDATION_ATTEMPTS.json`；一般性结论依据报告中的接口归纳。

生产控制只读取完整结果；`encode/decode/expected` 仅用于准备与验收。状态更新经过继承原核。

`PROGRAMS.json` 含六槽预编译固定块、布局和候选。精确目录及任意提示接口有不同前提。

项目报告与本地详细报告为两个独立版式，发表状态见 `PUBLICATION.json`。作者检查不等于独立数学审核。
