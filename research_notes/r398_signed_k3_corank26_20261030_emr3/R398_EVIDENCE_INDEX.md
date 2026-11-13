# R398 原始机证书恢复与复现索引

- 证书原文：R398_EVIDENCE.json，33,504 UTF-8 字节，SHA256 c6eddd84f42b3df207d1a71bfcb0229d264090c216b71cd8724e17d525da41ea。
- 无损文本载体：R398_EVIDENCE.json.gz.b64，先 Base64 解码再 gzip 解压；压缩使用 gzip mtime=0。解压后 SHA256 必须匹配上行。
- 多项式原文：R398_POLYNOMIALS.json，1,174,210 UTF-8 字节，SHA256 a251e1d274c59cbe308cec007174da9cb1b2ad34eeca74e806a321d5b36bcaa9。由同目录 r398_symbolic.py 直接重建。
- 源码执行：python r398_symbolic.py && python r398_certify.py，预期 R398_SYMBOLIC_PASS 和 R398_EXACT_PASS。
- 有理点交叉：728项。全参数证书：108对象、117闭区间、122检查、7672个严格正有理 Bernstein 系数。严格性来自精确整数/有理运算和覆盖证书。
- 源码基线：R397 commit 34e93b04769fec82c5eb477274af0f56a7b08569，原始 R346 signed K/J Blob 1579ceb717ab1945227eca4f7a1878bf4ffa73e1。
- 示例解码（仅作已取得文件的本地恢复）：python -c "import base64,gzip,pathlib; p=pathlib.Path('R398_EVIDENCE.json.gz.b64'); pathlib.Path('R398_EVIDENCE.json').write_bytes(gzip.decompress(base64.b64decode(p.read_text())))"

该索引是作者侧可核验研究保全，不代表活动注册、CLAIM、Driver 审阅或科学准入。
