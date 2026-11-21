"""PREFIX-990 exact delayed-weight histogram test, pure Python 3 standard library.
Requires PREFIX989_R6_HISTORY_WEIGHTED_NERODE.py in the same directory.
"""
from pathlib import Path
from runpy import run_path
from collections import defaultdict
import json

OLD=run_path(str(Path(__file__).with_name('PREFIX989_R6_HISTORY_WEIGHTED_NERODE.py')))
WORDS=((6,24,6,-3),(6,24,8,40))
def u(j):
    return {0:1,1:2,2:3,3:5,4:7,5:11,6:13}.get(j,17+j)

def projected(word):
    p0=max(abs(c) for c in word).bit_length()+1
    ports,src,starts,aug=OLD['build'](word,p0)
    edges={}
    for (q,x,h),rows in aug.items():
        z=q,x
        row=tuple(sorted((a,(t[0],t[1])) for a,weight,t in rows))
        if z in edges: assert edges[z]==row
        else: edges[z]=row
    return p0,ports,tuple((q,x) for q,x,h in starts),edges,starts,aug

def delayed_hist(edges,starts,n):
    if n==0: return {1:len(starts)}
    cur=defaultdict(int)
    for s in starts:cur[(s,1)]+=1
    for _ in range(n-1):
        nxt=defaultdict(int)
        for (s,w),count in cur.items():
            for a,t in edges[s]: nxt[(t,w*u(a[2]))]+=count
        cur=nxt
    h=defaultdict(int)
    for (s,w),count in cur.items():h[w]+=count*len(edges[s])
    return dict(sorted((w,count) for w,count in h.items() if count))

def delayed_mass(edges,starts,n):
    if n==0: return len(starts)
    cur=defaultdict(int)
    for s in starts:cur[s]+=1
    for _ in range(n-1):
        nxt=defaultdict(int)
        for s,mass in cur.items():
            for a,t in edges[s]:nxt[t]+=mass*u(a[2])
        cur=nxt
    return sum(mass*len(edges[s]) for s,mass in cur.items())

def main():
    out={'schema':'PREFIX990_DELAYED_BRC_EXACT_RESULTS_V1',
         'scope':'auxiliary signed-source observer; positive historical port weights',
         'verification':'integer exact; masses lengths 0..24; histograms lengths 0..13; original augmented-state comparison',
         'families':[]}
    for word in WORDS:
        p0,ports,starts,edges,aug_starts,aug=projected(word)
        original=OLD['counts'](aug,aug_starts,24)
        assert all(delayed_mass(edges,starts,n)==original[n][1] for n in range(25))
        assert all(delayed_hist(edges,starts,n)==OLD['port_histogram'](aug,aug_starts,n) for n in range(14))
        factor=1<<(18-len(ports))
        out['families'].append({
            'word':list(word),'stable_width':p0,'ports':list(ports),
            'augmented_states':len(aug),'old_states':len(edges),'starts':len(starts),
            'spectator_factor_p19':factor,
            'n8_count_mass':list(original[8]),'n19_count_mass':list(original[19]),
            'p19_n19_count_mass':[factor*x for x in original[19]],
            'histogram_n8':[[w,c] for w,c in delayed_hist(edges,starts,8).items()],
            'histogram_n13':[[w,c] for w,c in delayed_hist(edges,starts,13).items()],
        })
    path=Path(__file__).with_name('PREFIX990_R6_EXACT_RESULTS.json')
    path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('PASS, 2 families, mass n=0..24, full histogram n=0..13')
    for f in out['families']:print(f['word'],f['augmented_states'],f['old_states'],f['n8_count_mass'],f['n19_count_mass'])

if __name__=='__main__': main()
