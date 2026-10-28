# PREFIX-325 实际验证和复现索引

**科学结论（作者侧，待独立审核）：** 五 Port 静态辅助S7-3准确基础读数固定为 `Q0=(128,80,74,200,85)/64`，且来源在 `Q(i)^3`、可写为 `B/d` 其中 `B∈Z[i]^3, 1≤d≤250` 时，所有可行来源均属于 `t(-2,-2i,1)` 或 `t(-2,2i,1)`、`N(t)=1`；**仅有两种相位轨道**。完整可逆三圆枚举逻辑及Port4/Port5谓词见正文与执行程序；这不是无界分母或全复数结论。

正文：`PREFIX325_FINITE_Q0_CLASSIFICATION.zh-CN.md`。

实际运行的精确标准库检查器：`verify_prefix325_compact.py`，SHA-256 `2f101cac6174b4cf84c853e6e0a49061e502faf36d4d78f5f562eb3f361f8b0f`。

完整机器数据：`RESULTS_PREFIX325_COMPACT.json.gz.b64`，文本文件 SHA-256 `b2791491a40251109494f73280abec82e6385ed7c7e0eaec75b77c5b6c3cd14c`；先去除首尾空白，Base64解码，再gzip解压得到完整JSON，原始JSON SHA-256 `db163d141bf2d1cf37e37d175a02102da049887d7563acc395d2d4302aee8fc9`。JSON含250个分母的合格来源计数、316个规范单位相位、全部5+5共同相干报告和候选数量。

复算命令（在同一目录）：
```sh
python verify_prefix325_compact.py
python - <<'PY'
import base64, gzip, hashlib, pathlib
p = pathlib.Path('RESULTS_PREFIX325_COMPACT.json.gz.b64')
raw = gzip.decompress(base64.b64decode(p.read_text().strip()))
assert hashlib.sha256(raw).hexdigest() == 'db163d141bf2d1cf37e37d175a02102da049887d7563acc395d2d4302aee8fc9'
assert raw == pathlib.Path('RESULTS_PREFIX325_COMPACT.json').read_bytes()
print('EXACT_MACHINE_EVIDENCE_MATCH')
PY
```
第一条命令生成 `RESULTS_PREFIX325_COMPACT.json`，第二条比对解压数据。这是可执行的实际本地复算路径。

原始作者侧扩展复核完成的计数：2,098,944个三圆元组、1,401,344个整数反求、5024个Port4通过、4640个全五Port通过（计入重复分母表示），唯一高斯有理状态632个、单位相位316个。独立d=1包围盒检验20000个候选恰有8个相位来源。扩展复核中的五Port BRC运算累计1,429,578次质量及12,866,202项保留来源标签的有序路径对；紧凑复算程序从原生3来源有序对直接求Port4/5及所有接受态的五Port读数。

这一BRC证据范围为静态辅助C³，不建立到原生六维X6、三维切片、Detector、时间更新的保真转移。于2026-10-28原生权限只读查询返回 `CONTROL_QUOTA`，Site权限报告 `research_authority_granted=false`；当前Owner/CLAIM未核实，不发布正式Result或数学接纳。

后继问题：`NEXT_PREFIX326.md`。