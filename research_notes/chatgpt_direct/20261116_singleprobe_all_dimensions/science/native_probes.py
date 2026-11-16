"""Exercise the nine-coordinate encoder on original independent five-cycle components.

In the standalone evidence package the inherited next_repair tree is in the
package root. For a source checkout set PYTHONPATH to its matching bundle root.
"""
from argparse import ArgumentParser
from collections import Counter
from pathlib import Path
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from next_repair.native import native_recovery as kernel

F = range(5)
ZERO = (0,) * 9
CERT = json.loads((HERE / 'full' / 'nine_certificate.json').read_text())
MATRIX = tuple(zip(*CERT['columns']))
def plus(a, b):
    return tuple((x + y) % 5 for x, y in zip(a, b))


def difference(a, b):
    return tuple((x - y) % 5 for x, y in zip(a, b))


def syndrome(row):
    return tuple(sum(v * a for v, a in zip(row, r)) % 5 for r in MATRIX)


GROUPS = [[tuple(row) for row in item] for item in CERT['classes']]
REPS = {syndrome(row):(g,row) for g,group in enumerate(GROUPS) for row in group}
assert len(REPS)==125 and sum(map(len,GROUPS))==125


def encode(h):
    g,rep = REPS[syndrome(h[:9])]
    return g, difference(h[:9],rep), h[9:]


def candidates(message):
    group, shift, tail = message
    return [plus(v,shift) + tail for v in GROUPS[group]]


def test_cases():
    # Equal columns 1 and 8 give this explicit nonzero kernel translate.
    shifts=[ZERO, (0,1,0,0,0,0,0,0,4)]
    assert syndrome(shifts[1])==(0,0,0)
    for n in (9,12):
        tail = () if n==9 else (0,2,4)
        for group in range(len(GROUPS)):
            for offset in shifts:
                msg = group,offset,tail
                points = candidates(msg)
                yield n,msg,points[0],None
                # Include both ends of a forced pair; rotate the distinguishing coordinate.
                ix = (group+n) % len(points)
                x,y = points[ix],points[(ix+1)%len(points)]
                for a,b in ((x,y),(y,x)):
                    yield n,msg,a,b


def run():
    compiler = kernel.core.prior.Compiler(slots=15)
    counts = Counter()
    fees = {}
    digest = hashlib.sha256()
    for serial,(n,msg,h,other) in enumerate(test_cases()):
        programs=[]
        obs=[]
        for v in h:
            p,j=kernel.old(compiler,v)
            programs.append(p)
            obs.append(j)
        # This encoder sees only the actual preparation guards, before the writers and menus.
        actual_msg=encode(tuple(obs))
        assert actual_msg==msg
        options=candidates(actual_msg)
        varying=[i for i in range(n) if other is not None and h[i]!=other[i]]
        chosen=varying[(n+msg[0])%len(varying)] if varying else None
        menus=[]
        for i,v in enumerate(h):
            w=other[i] if other is not None else v
            pairs=[(m,e) for m in kernel.MAPS for e in F
                   if (kernel.F[m][v] in kernel.E[e])==(i==chosen)
                   and (kernel.F[m][w] in kernel.E[e])==(i==chosen)]
            menus.append(pairs[(serial+i)%len(pairs)])
        for p,(m,_) in zip(programs,menus):
            kernel.update(p,m)
        banks=[p.codes() for p in programs]
        receipts=tuple(kernel.first(p,e)['code'] for p,(_,e) in zip(programs,menus))
        possible=set()
        for row in options:
            audit=[kernel.audit(e,kernel.F[m][v]) for v,(m,e) in zip(row,menus)]
            if tuple(r[0] for r in audit)==receipts:
                possible.add(tuple(r[1] for r in audit))
        assert 1<=len(possible)<=2
        asked=None
        if len(possible)==2:
            a,b=sorted(possible)
            i=next(i for i,(x,y) in enumerate(zip(a,b)) if x!=y)
            k=menus[i][1]+1
            assert receipts[i]==11
            bit=programs[i].probe(kernel.marker_slot(k),kernel.least_one(k))
            possible={r for r in possible if r[i]==(11 if bit else k)}
            asked=i
        (result,)=possible
        out=tuple(kernel.emit(p,[r])[0]['bind_delivered'] for p,r in zip(programs,result))
        expected=tuple(kernel.audit(e,kernel.F[m][v])[1] for v,(m,e) in zip(h,menus))
        assert out==result==expected and asked==chosen and banks==[p.codes() for p in programs]
        f=sum(p.cost for p in programs)
        fees.setdefault(n,[]).append(f)
        counts[n, int(asked is not None)]+=1
        digest.update((json.dumps([h,msg,menus,receipts,out,asked,f],separators=(',',':'))+'\n').encode())
    return {'scope':'stratified full original paths; all 8 template types at two kernel translates; one fixed tail for dimension 12',
            'dimensions':{n:{'zero':counts[n,0],'one':counts[n,1],'min_commands':min(v),'max_commands':max(v)} for n,v in fees.items()},'trace_sha256':digest.hexdigest()}


if __name__=='__main__':
    arg=ArgumentParser();arg.add_argument('--out',type=Path);opt=arg.parse_args()
    data=json.dumps(run(),indent=2)+'\n'
    if opt.out:opt.out.write_text(data)
    else:print(data,end='')
