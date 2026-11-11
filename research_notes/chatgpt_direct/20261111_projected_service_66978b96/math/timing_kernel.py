"""BRC experiment, same seven-marker inventory as the parent, two demanded outputs."""
import argparse
import json
import sys
from pathlib import Path
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'copylife/kernel_checks.py').is_file())
sys.path.insert(0,str(ROOT))
from copylife.kernel_checks import Physical,core


def encode(family,h,mode):
    if mode=='unannounced':return h>>2  # independent of any post-join request
    return (h>>1)&1 if family=='linear' else int(h==2)  # announced: chosen for {1,2}


def decode(family,msg,mode,demand,read):
    def marker(h,j):return int(h==j) if family=='star' else (h&j).bit_count()%2
    if mode=='announced' and demand!=(1,2):raise ValueError("unsupported announced task")
    if mode=='announced':
        U=[h for h in range(8) if encode(family,h,mode)==msg]
    else:
        U=list(range(4*msg,4*msg+4))
    # Read only requested coordinates that still vary on consistent histories.
    out=[]
    for j in demand:
        vals={marker(h,j) for h in U}
        if len(vals)==1:v=vals.pop()
        else:
            v=int(read(j))
            U=[h for h in U if marker(h,j)==v]
        out.append(v)
    return tuple(out)


def once(C,family,h_actual,mode):
    b=3;m=7;temp=10;waste=11;demand=(1,2)
    P=Physical(C,[(h_actual>>i)&1 for i in range(b)]+list(range(1,m+1))+[0,0])
    h=0
    for i in range(b):
        P.drop(i);h|=int(bool(P.C.observe_result(P.J)))<<i
    for j in range(1,m+1):
        i=b+j-1
        assert P.copy(temp,i)==j
        P.drop(i)
        assert P.copy(waste,temp)==j
        present=h==j if family=='star' else bool((h&j).bit_count()%2)
        assert P.copy(i if present else waste,temp)==j
        P.drop(temp);P.drop(waste)
    msg=encode(family,h,mode);prefix=P.cost
    del h,present
    qtrace=[]
    def read(j):
        one=(j&-j).bit_length()-1
        v=P.probe(b+j-1,one)
        qtrace.append([j,one,int(v)])
        return v
    recovered=decode(family,msg,mode,demand,read)
    keys=[]
    for j,blocked in zip(demand,recovered):
        key=8 if blocked else j
        P.round(0,0,key);keys.append(key);P.drop(0)
    # Independent oracle/audit after decisions. No branches below feed the controller.
    expected=[8 if (h_actual==j if family=='star' else (h_actual&j).bit_count()%2) else j for j in demand]
    assert keys==expected and prefix==1656
    return dict(h=h_actual,mode=mode,summary=msg,prefix_commands=prefix,bit_tests=qtrace,
                reads=len(qtrace),keys=keys,total=P.cost)


def main():
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=Path(__file__).with_name('timing_kernel_results.json'));a=p.parse_args()
    C=core.prior.Compiler(slots=12)
    out={'status':'PASS','slots':12,'members':C.members,'candidate_relations':len(C.H),'demand':[1,2],
         'scope':'32 original BRC runs across 8 worlds, s=1, two fixed key requests per execution, announced and one universally optimal unannounced encoder; minimax lower bound across arbitrary encoders and tasks in separate proof and enumeration', 'families':{}}
    for fam in ('linear','star'):
        rec=[once(C,fam,h,mode) for h in range(8) for mode in ('announced','unannounced')]
        for i in range(0,len(rec),2):
            x,y=rec[i:i+2];assert x['keys']==y['keys'] and y['total']-x['total']==8*(y['reads']-x['reads'])
        assert max(a['reads'] for a in rec if a['mode']=='announced')==1
        assert max(a['reads'] for a in rec if a['mode']=='unannounced')==2
        out['families'][fam]=rec
    a.out.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print('PASS 32 raw runs',C.members,len(C.H))
if __name__=='__main__':main()
