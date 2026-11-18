"""Independent byte-contained witness check; no DP or native program needed.
Reads GitHub WITNESS_EC49CJ.b64, base64(zlib(JSON)) with actual signed X6 words.
"""
import base64
import json
import zlib
from pathlib import Path
from VERIFY_EC49CJ import suffixes, row_system, recheck_certificate, P

root=Path(__file__).parent
payload=json.loads(zlib.decompress(base64.b64decode((root/'WITNESS_EC49CJ.b64').read_text())))
checks=[('CERT_EC49CJ_S3_n10.json',3,False,10,132,10),
        ('CERT_EC49CJ_S123_n10.json',3,True,10,147,10),
        ('CERT_EC49CJ_S1234_n12.json',4,True,12,231,15)]
assert set(payload)=={x[0] for x in checks}
for name,h,upto,n,rank,numblocks in checks:
    record=payload[name]
    sufs=suffixes(h,upto)
    rows=row_system(sufs)
    assert record['p']==P and record['n']==n
    assert len(record['blocks'])==numblocks
    assert record['abstract_rank_bound']==record['real_path_mod_rank']==rank
    assert record['all_fibers_full']
    assert all(b['minor_mod_p']!=0 and b['actual_mod_rank']==b['rank_bound'] for b in record['blocks'])
    assert recheck_certificate(record,sufs,rows)
    print('EXACT_CERTIFICATE_PASS',name,'rank=',rank,'fibers=',numblocks)
