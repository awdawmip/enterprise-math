# R396 机器证据恢复、来源及校验

本目录包含完整原始验证证据的 gzip 无损压缩件 R396_EVIDENCE.json.gz（3289 字节），SHA256(gzip)=5c981909b4e22958abfb8f29cc55239a7880e7e643ee2dd1679f1f53db5c78b2；原始 JSON 30907 字节，SHA256=3a6f820c8e87f5bc70bf19917ee5f758cdbb9e4e02ab0b48227e44da35c8c39b；Git Blob d14043f42c68ff2b8190ea987537c8972eaf4a52。

复原：gzip -dc R396_EVIDENCE.json.gz > R396_EVIDENCE.json

完整多项式 R396_POLYNOMIALS.json（929197 字节）由运行 python r396_symbolic.py 重建；其 SHA256=02aa2874583553945c6ca528a7c6aff1335985c3a2269b673834716800225d3f。

验证：python r396_certify.py。此程序重新精确计算区间 Bernstein 控制点、临界根符号与单调性、连续负见证覆盖和 θ≥4 无界尾部，使用 Fraction 从原始 D 递推在7个有理参数点核验672项等式；正常打印 R396_EXACT_PASS。与证据 JSON 的字节对比可用 cmp。没有浮点符号判定；显示近似根仅供阅读。

源码复用 R395 的确切 K/J 支路规则，保留支路符号及对 θ 的惟一 K3[t²] 改动。数据只对应固定 r=24，待独立 Driver 审查。
