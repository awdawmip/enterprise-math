# R404 原始证据恢复与独立复验

本目录包含 R404_PROOF.zh-CN.md、HANDOFF.md，以及两个无损归档：verify_r404.py.gz.b64、R404_EVIDENCE.json.gz.b64。压缩格式为 gzip；文本为原始 UTF-8 文件字节的 base64，不含凭据、token 或私有会话信息。

在本目录执行下列 Python 3 标准库脚本恢复原文件：

~~~python
import base64, gzip, pathlib
for name in ('verify_r404.py', 'R404_EVIDENCE.json'):
    source = pathlib.Path(name + '.gz.b64').read_text(encoding='ascii').strip()
    pathlib.Path(name).write_bytes(gzip.decompress(base64.b64decode(source)))
~~~

验证原始文件 SHA256：

- verify_r404.py：9b52fca5973bb488a052f8a40a633ea54a0b4e8f7530b25f4c97c4174ac712ea
- R404_EVIDENCE.json：d9577d96d83d84a0c2f1907356da821a4e57b9248a8c81e2b8824caf1b28f4dd

执行 python verify_r404.py 512，预期 R404_EXACT_PASS，527 三路径小阶对照、131327 大范围 Catalan/Pascal 恒等式、129795 个 s≥3 的有限严格正 D、1524 个 s=3/4/5 的有理闭式逐项对照。实际 JSON 可作逐字节比较。这个有限程序不自动完成全部余阶的证明；跨余阶证明在 R404_PROOF.zh-CN.md 第 2、3 节。
