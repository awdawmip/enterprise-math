"""Additional fixed-compiler checks; no changes to compiled production code."""
from pathlib import Path
from itertools import combinations
import json
import check_triadic_refs as q


def partitions():
    C=q.Compiler(6);rows=[];mass=q.ZERO
    for part in q.ref.partitions(6):
        J=C.encode((None,)*7);w=q.ONE;opcount=0
        ops=[]
        for block in range(max(part)+1):
            ops.append(('create',))
            ops.extend(('bind',i) for i,x in enumerate(part) if x==block)
            ops.append(('destroy',))
        ops.append(('create',))
        for op in ops:
            J,v,_=C.run(J,op);w=q.r.serial(w,v);opcount+=1
        original=J;bits=[]
        for i in range(6):
            K,_,_=C.run(J,('valid',i));q.ck(not C.decode(K)[1],'Every stored handle is stale')
        for i,j in combinations(range(6),2):
            K,_,_=C.run(J,('same',i,j));answer=C.decode(K)[1]
            q.ck(answer==(part[i]==part[j]),'Physical comparison preserves stale alias partition')
            bits.append(int(answer))
        rows.append(dict(partition=part,signature=bits,preparation_actions=opcount))
        mass=q.r.merge(mass,w)
    q.ck(len(rows)==203 and len({tuple(x['signature']) for x in rows})==203,'203 distinguishable partitions through compiled physical queries')
    return dict(partitions=len(rows),comparison_calls=len(rows)*15,validity_calls=len(rows)*6,CWM=q.e.cw(mass),rows=rows,checks=q.CHECKS,**C.stats())


def intrinsic_identity():
    C=q.Compiler(1);current=C.rows[0].cell(1);J=C.encode((1,0))
    S=q.ref.old.seed(J);before=S.names()[current]
    calls=0
    for op in C.programs[('execute',0)]:
        S,_,_=q.ref.old.raw_step(S,op,C.H);calls+=1
    after=S.names()[current]
    q.ck(S.matching==C.encode((1,0),0),'Physical endpoint exact under failed execute')
    q.ck(before!=after,'Physical storage-cell creation changes although logical tag is retained')
    return dict(before_name=before,after_name=after,physical_cell=current,raw_commands=calls,checks=q.CHECKS,interpretation='Macro-boundary logical refinement, not preservation of intrinsic birth names')

if __name__=='__main__':
    import sys
    mode=sys.argv[1];out=Path(sys.argv[2]);z=globals()[mode]()
    out.write_text(json.dumps(z,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in z.items() if k not in ('rows','lengths')},ensure_ascii=False))
