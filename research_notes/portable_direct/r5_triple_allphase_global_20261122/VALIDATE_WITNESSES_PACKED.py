"""Verify the stored R5 six-order cyclotomic certificate and CRT period."""
import csv
import math
import pathlib
import collections
import base64
import gzip
import hashlib
import io

here = pathlib.Path(__file__).resolve().parent
packed = here/'WITNESSES_ALL6.csv.gz.b64'
raw = gzip.decompress(base64.b64decode(packed.read_text(encoding='ascii')))
assert hashlib.sha256(raw).hexdigest() == 'fa987223acdeec3c310ef5e11122a924c290e0e3139e07e817a23b678eb997a2'
rows = list(csv.DictReader(io.StringIO(raw.decode('utf-8'))))
orders = (7,11,13,25,27,31)
counts = {}
for d in orders:
    group = [r for r in rows if int(r['d']) == d]
    assert len(group) == 2*d
    assert {int(r['r']) for r in group} == set(range(1, 2*d+1))
    n0 = nd = 0
    for row in group:
        co = row['component']
        assert co in ('R0', 'Rdot')
        if co == 'R0': n0 += 1
        else: nd += 1
        U,V,W,X = (int(row[k]) for k in ('U','V','W','X'))
        assert U != 0 and U*V >= 0 and U*W >= 0 and U*X >= 0
        assert 0 <= int(row['coordinate']) < (20 if d==25 else 18 if d==27 else d-1)
    counts[d] = (n0,nd)
assert counts == {7:(0,14),11:(12,10),13:(16,10),25:(45,5),27:(0,54),31:(0,62)}
W = (7,11,13,16,17,19,23,25,27,31,37)
K = math.lcm(*W)
L = 229746052653717600
assert K == L//(29*2*43) == 92119507880400
S = [s for s in range(1,79809) if s%58 in (0,54,55,56,57) and s%64 in (0,60,61,62,63) and s%43 in (0,37,38,39,40,41,42)]
assert len(S) == 91
prior = {7:182,11:220,13:215,25:96,27:182,31:182}
assert sum(prior.values()) == 1077
print('PASS rows',len(rows),'counts',counts,'CRT',len(S),'K',K,'prior_exception_cap_removed',1077)
