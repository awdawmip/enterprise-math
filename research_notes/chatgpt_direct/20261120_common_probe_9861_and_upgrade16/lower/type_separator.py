"""Find integer point/type separation certificates for a fixed typed residual.

Floating point LP is used only to discover weights. A positive result is checked
with integers against every candidate before it is written as a certificate.
"""
import argparse,json,struct,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

def points(mask):
    while mask:
        bit=mask&-mask
        yield bit.bit_length()-1
        mask-=bit

def main(work,tag,output):
    counts={tuple(map(int,t.split('-')[:2])):int(t.split('-')[2])for t in tag.split('_')}
    k=counts.pop((12,1104),0)
    h=counts.pop((13,1296),0);k+=h
    types=sorted(counts)
    rows={t:[] for t in types}
    for lo,hi,c,s in struct.iter_unpack('<QQII',(work/'bank').read_bytes()):
        t=s%256,c
        if t in rows:rows[t].append(lo+(hi<<64))
    frames=set()
    for line in (work/f'cores{k}.txt').read_text().splitlines():
        lo,hi,*centres=map(int,line.split())
        base=lo+(hi<<64)
        for choice in range(1<<k):
            if choice.bit_count()!=h:continue
            free=base;ok=True
            for j,centre in enumerate(centres):
                if choice>>j&1:
                    bit=1<<centre
                    if not free&bit:ok=False;break
                    free^=bit
            if ok:frames.add(free)
    answers=[]
    for idx,free in enumerate(sorted(frames)):
        start=time.monotonic()
        pools={t:[m for m in rows[t]if m&free==m]for t in types}
        rr=[];cc=[];ii=0
        for j,t in enumerate(types):
            for m in pools[t]:
                support=list(points(m))+[125+j]
                rr.extend([ii]*len(support));cc.extend(support);ii+=1
        matrix=coo_matrix((np.ones(len(rr)),(rr,cc)),shape=(ii,125+len(types))).tocsr()
        target=np.zeros(125+len(types));target[list(points(free))]=1
        for j,t in enumerate(types):target[125+j]=counts[t]
        fit=linprog(-target,A_ub=matrix,b_ub=np.zeros(ii),bounds=(-1,1),method='highs')
        result={'frame':idx,'free':str(free),'rows':ii,'status':int(fit.status),'seconds':time.monotonic()-start}
        if fit.status==0:
            result['discovery_value']=-float(fit.fun)
            if -fit.fun>1e-7:
                w=[int(round(x*1000000))for x in fit.x[:125]]
                z=[-max(sum(w[p]for p in points(m))for m in pools[t])for t in types]
                gap=sum(w[p]for p in points(free))+sum(counts[t]*z[j]for j,t in enumerate(types))
                assert gap>0
                result['integer_certificate']={'point_weights':w,'type_weights':z,'positive_gap':gap}
        answers.append(result)
        output.write_text(json.dumps({'tag':tag,'types':types,'frames':answers},sort_keys=True,indent=2)+'\n')
        print(json.dumps({key:value for key,value in result.items()if key!='integer_certificate'}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--work',type=Path,required=True);p.add_argument('--tag',required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    main(a.work,a.tag,a.output)
