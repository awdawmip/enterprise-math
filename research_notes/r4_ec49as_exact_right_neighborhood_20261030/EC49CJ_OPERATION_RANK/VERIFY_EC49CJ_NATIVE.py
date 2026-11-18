"""Native exact BRC audit, independent of modular witness path-span DP.
Uses immutable original native_signed_brc.py (Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176).
"""
import json, hashlib, subprocess, time
from pathlib import Path
from VERIFY_EC49CJ import Z,S,W,suffixes,row_system,advance,follow,label,weight,displacement,reach_back
from native_signed_brc import endpoint_weight,endpoint_multiplicity

def dp(n,targets):
    st={(Z,0):(1,1,1)};peak=1;updates=0
    for t in range(n):
        rem=n-t-1;out={}
        for (z,q),vals in st.items():
            for sign in (1,-1):
                for i in range(6):
                    zz=list(z);zz[i]+=sign;zz=tuple(zz)
                    if not reach_back(zz,rem,targets):continue
                    q2=advance(q,sign*(i+1));key=(zz,q2)
                    w0=W[0][i] if sign>0 else 1
                    w1=W[1][i] if sign>0 else 1
                    old=out.get(key,(0,0,0))
                    out[key]=(old[0]+vals[0]*w0,old[1]+vals[1]*w1,old[2]+vals[2]); updates+=1
        st=out;peak=max(peak,len(st))
    return st,peak,updates

def audit(n,sufs,st):
    totals={};lookups={}
    for sk,word in sufs.items():
        target=tuple(-x for x in displacement(word));suffix_weight=weight(word)
        label_totals=[[0]*3 for _ in range(4)]
        for (z,q),values in st.items():
            if z!=target:continue
            a=label(follow(q,word))
            for c in range(3):label_totals[a][c]+=values[c]*suffix_weight[c]
        all_tot=tuple(sum(v[c] for v in label_totals) for c in range(3))
        expect=(int(endpoint_weight(n,target,W[0],(1,)*6))*suffix_weight[0],
                int(endpoint_weight(n,target,W[1],(1,)*6))*suffix_weight[1],
                endpoint_multiplicity(n,target))
        assert all_tot==expect,(n,sk,all_tot,expect)
        lookups[sk]=label_totals
    return lookups

def main():
    base=Path(__file__).parent
    sha=subprocess.check_output(['git','hash-object',str(base/'native_signed_brc.py')],text=True).strip()
    assert sha=='300a96e3dc24bf6fff73743037a0347a8bc83176',sha
    sufs=suffixes(3,True);targets=set(row_system(sufs))
    report=[]
    for n in (8,10,12):
        st,peak,updates=dp(n,targets)
        lookups=audit(n,sufs,st)
        for name in ('S3','S123'):
            cert=json.loads((base/f'CERT_EC49CJ_{name}_n{n}.json').read_text())
            for block in cert['blocks']:
                for path in block['paths']:
                    path=tuple(path)
                    for suff in sufs.values():
                        combo=path+tuple(suff)
                        direct=2*int(any(combo[j:j+2]==(1,2) for j in range(len(combo)-1)))+int(any(combo[j:j+2]==(2,1) for j in range(len(combo)-1)))
                        assert direct==label(follow(follow(0,path),suff))
        report.append({'length':n,'peak_typed_states':peak,'state_updates':updates,
                       'native_return_weight0':int(endpoint_weight(n,Z,W[0],(1,)*6)),
                       'native_return_weight1':int(endpoint_weight(n,Z,W[1],(1,)*6)),
                       'native_return_count':endpoint_multiplicity(n,Z),
                       'suffix_observations_checked':len(lookups)*4*3,
                       'terminal_observations':lookups})
        print('native audit n',n,'states',len(st),'peak',peak,'suffixes',len(lookups),'updates',updates,flush=True)
    (base/'NATIVE_REPORT_EC49CJ.json').write_text(json.dumps({'native_blob':sha,'checks':report},ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n')

if __name__=='__main__':main()
