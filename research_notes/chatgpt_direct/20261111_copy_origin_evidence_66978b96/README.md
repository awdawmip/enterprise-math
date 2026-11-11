# 复制、删除与来源证据的两种寿命

先读 REPORT.zh-CN.md。原核及其上轮依赖放在独立复验包的同级目录中，保持原相对路径。代码使用 Python 3.12 标准库，无需外部服务。

| 程序 | 独立核验的问题 | 输出 |
|---|---|---|
| origin_checks.py | 来源扫描能否保持真实槽表的阻挡、复制交付和费用；六个严格反转门槛 | origin_results.json |
| certificate_checks.py（调用 certificates.py） | 逐准备来源证书公式与顺序递推；候选不再受支持时的中途安全回退 | certificate_results.json |
| one_creation.py | 带前后复制/删除、仅一次创建的简化式与四类代表；39槽最迟见证 | one_creation_results.json |
| oracle_checks.py（调用 oracle.py） | 独立来源域和显式所有旧表的逐步决策；统一最坏闭式 | oracle_results.json |
| kernel_checks.py | 原三元核真实操作字、三种观察接口、两组百表回放、保护与成对遗漏边界 | kernel_results.json |

独立包中运行 `python3 -B verify.py --replay`，可从清洁目录复算以上五组结果；各单项也可从包根以 `python3 -B copylife/文件名.py` 运行。原始来源和范围分别见 origin_proof.md、oracle_notes.md、kernel_notes.md。RESULT_INDEX.json 为本轮科学源目录的索引。
