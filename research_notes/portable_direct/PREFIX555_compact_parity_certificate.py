#!/usr/bin/env python3
"""PREFIX-555: exact sign-parity/odd-depth BRC observer and gzip spool certificate.
Requires the published PREFIX550_shared_gauge_compact_certificate.py and
PREFIX553_batched_depth_stream_certificate.py in the same directory.
"""
import gzip, json, hashlib, tempfile
from pathlib import Path
import PREFIX550_shared_gauge_compact_certificate as x
import PREFIX553_batched_depth_stream_certificate as p

def certify(depth=10):
    ids,ph,sig,rows,roots=p.prepare()
    sign={c:1 if x.P[ph[c]][2]>0 else -1 for c in range(51)}
    assert [sum(sign[c]==s for c in sign) for s in (-1,1)]==[24,27]
    assert sum(sum(rows[c].values()) for c in rows)==306
    assert all(sign[c]==-sign[j] for c in rows for j,g in rows[c])
    classes=[sorted({ids[q] for q in roots[r]}) for r in x.ROOTS]
    assert list(map(len,classes))==[4,7]+[4]*10
    for k,r in enumerate(x.ROOTS):
        s=next(t for t in r if t)
        assert all(sign[c]==s for c in classes[k])
    with tempfile.TemporaryDirectory(prefix='prefix555_') as tmp:
        f=Path(tmp)
        paths=[f/(f'root_{i}.jsonl.gz') for i in range(12)]
        fps=[gzip.open(path,'wt',encoding='utf-8',compresslevel=6) for path in paths]
        output=f/'parity.jsonl';baseline=f/'cached.jsonl'
        u=[{p.ZERO6:1} for _ in range(51)]
        try:
            with output.open('w',encoding='utf-8') as out:
                for d in range(depth+1):
                    if d&1:
                        for r in x.ROOTS:
                            for q in roots[r]:
                                a=abs(x.P[x.V[q][0]][2])-1
                                p.emit(out,q,d,p.recover(u[ids[q]],{},d,a))
                    else:
                        for fp,cs in zip(fps,classes):
                            fp.write(json.dumps([[[*m,n] for m,n in sorted(u[c].items())]
                                                 for c in cs],separators=(',',':'))+'\n')
                    if d<depth:u=p.step(u,rows,ph)
        finally:
            for fp in fps:fp.close()
        with output.open('a',encoding='utf-8') as out:
            for k,r in enumerate(x.ROOTS):
                e=[{p.ZERO6:1} if sig[c]==r else {} for c in range(51)]
                with gzip.open(paths[k],'rt',encoding='utf-8') as fp:
                    for d in range(depth+1):
                        if not d&1:
                            line=fp.readline();assert line
                            cs={c:{tuple(t[:6]):t[6] for t in row}
                                for c,row in zip(classes[k],json.loads(line))}
                            for q in roots[r]:
                                a=abs(x.P[x.V[q][0]][2])-1
                                p.emit(out,q,d,p.recover(cs[ids[q]],e[ids[q]],d,a))
                        if d<depth:e=p.step(e,rows,ph)
                    assert not fp.readline()
        p.cached_stream(depth,str(baseline),(ids,ph,sig,rows,roots))
        new=dict(p.read_records(output));old=dict(p.read_records(baseline))
        assert new==old and len(new)==96*(depth+1)
        terms=sum(len(v) for v in new.values())
        digest=p.keyed_digest(output)['sha256_normalized_output']
        if depth==10:
            assert terms==187844
            assert digest=='04decba6e3380be37099bdffc8e2832eba3352bd528ad9e629ade230c4802820'
        return {'status':'ALL_CHECKS_PASS','frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
                'model':'four-STAR native X6, 48 phases, 96 ports, 51 six-axis BRC/gate observation classes',
                'depth_inclusive':depth,'classes_by_sign':{'negative':24,'positive':27},
                'source_rows':51,'transition_multiplicity':306,
                'all_edges_reverse_sign':True,'odd_depth_match_zero':True,
                'exact_direct_tuple_equal':True,'complete_output_records':len(new),
                'nonzero_monomial_coefficients':terms,'output_sha256_normalized':digest,
                'uncompressed_output_bytes':output.stat().st_size,
                'gzip_even_U_cache_bytes':sum(z.stat().st_size for z in paths)}

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('--depth',type=int,default=10)
    args=ap.parse_args();assert 0<=args.depth<=12
    print(json.dumps(certify(args.depth),ensure_ascii=False,indent=2))
