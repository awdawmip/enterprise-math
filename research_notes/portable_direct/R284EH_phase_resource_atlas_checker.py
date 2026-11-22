#!/usr/bin/env python3
"""R284EH: exact phase-aware observation-resource atlas, s=1..101.
Uses the immutable R284CO frozen 16-bit Port model. Standard library only.
Verified by codeword SHA and independent selected direct collision checks.
"""
import hashlib, json
from itertools import product
from pathlib import Path
from R284CO_spectral_witness_checker import P,FROZEN_SHA,det,arcs,dist

MODES={'R':(0,1),'W':(0,64),'RW':(0,65),'T':(0,1,65),'F':(0,1,64,65)}

def frozen_readouts():
    aa=arcs(); sha=hashlib.sha256(); arr=[]
    for upper in product((1,2),repeat=4):
        top=sum((x-1)<<j for j,x in enumerate(upper))
        for lower in product((1,2),repeat=12):
            z=det(lower,top)%P
            sha.update(z.to_bytes(8,'big'))
            arr.append(max(dist(z,a) for a in aa))
    assert len(arr)==65536 and len(aa)==64
    assert sha.hexdigest()==FROZEN_SHA
    return arr

def collect_close_pairs(f, offsets, cap=100):
    # Only pairs which can collide for one s<=101 need be considered.
    seq=sorted((f[i],i) for i in range(65536))
    found=[]
    for k,(a,i) in enumerate(seq):
        j=k-1
        while j>=0 and a-seq[j][0]<=cap:
            q=seq[j][1]
            x=[f[i^d] for d in offsets]
            y=[f[q^d] for d in offsets]
            diffs=[abs(u-v) for u,v in zip(x,y)]
            m=max(diffs)
            if m<=cap:
                found.append((m,tuple((min(u,v),abs(u-v)) for u,v in zip(x,y)),min(i,q),max(i,q)))
            j-=1
    found.sort(key=lambda x:x[0])
    return found

def collision_atlas_for_mode(candidates):
    fail=[]; witnesses={}
    for s in range(1,102):
        bitset=0; whole=(1<<s)-1
        for m,coords,i,j in candidates:
            if m>=s:break
            for t in range(s):
                if bitset>>t&1:continue
                if all((lo-t)%s<s-d for lo,d in coords):
                    bitset|=1<<t
                    witnesses.setdefault((s,t),(i,j))
            if bitset==whole:break
        fail.append([t for t in range(s) if bitset>>t&1])
    return fail,witnesses

def direct_failed(f,s,offsets):
    out=[]
    for t in range(s):
        seen=set()
        for i in range(65536):
            key=tuple((f[i^d]-t)//s for d in offsets)
            if key in seen:
                out.append(t);break
            seen.add(key)
    return out

def main():
    f=frozen_readouts()
    atlas={}; counts={}
    for name,offs in MODES.items():
        pairs=collect_close_pairs(f,offs)
        fail,witnesses=collision_atlas_for_mode(pairs)
        atlas[name]=fail
        counts[name]=len(pairs)

    # Independent direct all-state checks of selected phase transitions.
    verified={}
    for s,name in ((61,'W'),(61,'RW'),(69,'F'),(70,'F'),(72,'F'),(75,'F')):
        direct=direct_failed(f,s,MODES[name])
        assert direct==atlas[name][s-1],(s,name)
        verified[f'{s}:{name}']=direct
    assert atlas['RW'][60]==[8,26,51]
    assert atlas['W'][60]==[23,32,45,46]
    assert atlas['T'][71]==[x for x in range(72) if x not in (3,7,8,9,10,55,56,57,65,66,67,68)]
    def phase_resources(s):
        r={2:0,3:0,4:0,None:0}
        for t in range(s):
            if any(t not in atlas[n][s-1] for n in ('R','W','RW')):r[2]+=1
            elif t not in atlas['T'][s-1]:r[3]+=1
            elif t not in atlas['F'][s-1]:r[4]+=1
            else:r[None]+=1
        return {'2':r[2],'3':r[3],'4':r[4],'>4':r[None]}
    by_width={str(s):phase_resources(s) for s in range(1,102)}
    first_four_fail=next((s for s in range(1,102) if atlas['F'][s-1]),None)
    print('candidate counts',counts)
    print('first 4fail',first_four_fail)
    for s in (61,62,63,69,70,71,72,74,75,94,98,101):print(s,by_width[str(s)])
    cert={'schema':'R284EH_PHASE_RESOURCE_ATLAS_V1',
        'scope':'frozen Port 65536 states; offsets 0,1,64,65; common integer phase; widths 1..101',
        'frozen_source_commit':'acba2d8667903434aaa2a10720f43637fcc2421b',
        'frozen_source_blob_sha1':'b46e0f682b58e47c27094b4bea6fa4e55119a3ee',
        'frozen_codeword_sha256':FROZEN_SHA,
        'states':65536,'close_pair_counts':counts,
        'failed_phase_count_by_mode':{n:[len(x) for x in atlas[n]] for n in MODES},
        'phase_aware_minimal_read_distribution':by_width,
        'first_four_read_collision_width':first_four_fail,
        'direct_verified_selected_widths':verified,
        'review':'NOT_REVIEWED'}
    fn=Path(__file__).with_name('R284EH_phase_resource_atlas_certificate.json')
    fn.write_text(json.dumps(cert,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return cert
if __name__=='__main__':main()
