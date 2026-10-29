# R397 原始证据恢复与校验

完整 R397_EVIDENCE.json 为32888字节，SHA256 为 0f533b1498263b8ceeb9f5d97bcb82b7996c4a4c905a7cd783e7fcb376c54157。R397_EVIDENCE.json.gz.b64 是该文件经 gzip/base64 无损编码的完整内容。恢复：

    from pathlib import Path
    import gzip,base64,hashlib
    raw=gzip.decompress(base64.b64decode(Path("R397_EVIDENCE.json.gz.b64").read_text()))
    assert hashlib.sha256(raw).hexdigest()=="0f533b1498263b8ceeb9f5d97bcb82b7996c4a4c905a7cd783e7fcb376c54157"
    Path("R397_EVIDENCE.json").write_bytes(raw)

执行 python r397_symbolic.py 生成完整的51个 c_j、49个 T_j 的 R397_POLYNOMIALS.json；执行 python r397_certify.py 检查104个证书对象并生成可比对的 JSON。模型来源与完整证明见 R397_PROOF.zh-CN.md。
