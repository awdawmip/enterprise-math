#!/usr/bin/env python3
"""EC33 exact alphabet-refined certificate using unchanged EC32 source code.

Requires adjacent EC32_VERIFY_UPSTREAM_UNCHANGED.py from the EC32 immutable evidence.
The EC32 original source is not modified; only the declared alphabet is supplied.
"""
from __future__ import annotations
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EC32_PATH = ROOT / 'EC32_VERIFY_UPSTREAM_UNCHANGED.py'
EC32_SOURCE_SHA256 = '604233139ed6fd2e2db491de3f661b37ae0af98d0e1fecf38c180e561d3f983d'
EC32_SOURCE_BLOB = '5eb598b8f6fdcb9fd26da148090ead079d94cd3e'


def main():
    raw = EC32_PATH.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == EC32_SOURCE_SHA256
    assert hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest() == EC32_SOURCE_BLOB
    spec = importlib.util.spec_from_file_location('EC32_unmodified', EC32_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    module.ALPHABET = ('R', 'B')
    cases = []
    for H in range(1, 9):
        n = H + 1
        red, blue = module.mat(n), module.mat(n)
        for r in range(n):
            if r < H:
                red[r][r+1] = blue[r][r+1] = 1
            else:
                red[r][r] = 2
        U = ({'R': [[1]], 'B': [[1]]}, [1], [1])
        V = ({'R': red, 'B': blue}, [1] + [0]*H, [1]*n)
        certificate = module.rational_basis_certificate(V, U)
        assert certificate['reachable_rank'] == H + 2
        assert not certificate['equivalent_all_words']
        assert certificate['first_basis_nonzero']['length'] == H + 1
        cases.append({'H': H, 'certificate': certificate})
    output = {'schema': 'EM_R4_EC33_EC32_SPAN_REUSE_V1', 'status':'PASS',
              'source_sha256': EC32_SOURCE_SHA256, 'source_git_blob': EC32_SOURCE_BLOB,
              'source_git_ref':'fa0cc318e99c1201b1e31299a8cc38daa2ff62ed',
              'reused_method': 'EC32.rational_basis_certificate unchanged with ALPHABET=(R,B)',
              'cases': cases}
    (ROOT/'EC33_EC32_SPAN_REPORT.json').write_text(json.dumps(output, indent=2, sort_keys=True, ensure_ascii=False)+'\n', encoding='utf-8')
    print(json.dumps({'status':output['status'], 'H_count':len(cases),
                      'last_case': cases[-1]['certificate']['first_basis_nonzero']}))


if __name__=='__main__':
    main()
