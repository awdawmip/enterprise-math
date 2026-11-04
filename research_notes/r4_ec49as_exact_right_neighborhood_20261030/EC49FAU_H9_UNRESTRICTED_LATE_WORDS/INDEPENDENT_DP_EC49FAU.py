from collections import defaultdict
import json
OPS = {'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
START = ((0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(3,0),(4,0))
# N,A,B,AB,BA encoded 0,1,2,3,4

def turn(obs, sym):
    row=list(obs)
    for step in OPS[sym]:
        nxt=[]
        for st, prev in row:
            if prev==1 and step==2:
                st = 1 if st==0 else (4 if st==2 else st)
            elif prev==2 and step==1:
                st = 2 if st==0 else (3 if st==1 else st)
            nxt.append((st,step))
        row=nxt
    return tuple(row)

def end_signature(word):
    obs=START
    for x in word:obs=turn(obs,x)
    return tuple(st for st,prev in obs)
SIGNATURES = {end_signature(w): i for i,w in enumerate(('de','ed','ce','ec','feg','gef'))}
assert len(SIGNATURES)==6

def cat(prefix):
    if prefix[:2] in ('de','ed','ce','ec'):return 0
    if prefix[:3] in ('feg','gef'):return 1
    return 2

def rank9(mask):
    return bool((mask & (2|16)) and (mask & (4|16)) and (mask & (1|32)) and (mask & (8|32)))

def main():
    # state = (nine observation states, full positive X6 key, e_minus_a, first three symbols)
    cur={(START,(0,0,0),0,''):1}
    out={}
    for h in range(1,10):
        nxt=defaultdict(int)
        for (obs,key,balance,pref), num in cur.items():
            for op,steps in OPS.items():
                newobs=turn(obs,op)
                key2=tuple(key[i]+sum(s==i+1 for s in steps) for i in range(3))
                pref2=pref+op if len(pref)<3 else pref
                nxt[(newobs,key2,balance+(op=='e')-(op=='a'),pref2)]+=num
        cur=nxt
        counts=[0,0,0]; ss=[[0]*6 for i in range(3)]; mk={}; countvalid=0; total=0
        for (obs,key,balance,pref),num in cur.items():
            if balance!=1:continue
            total+=num
            i=SIGNATURES.get(tuple(st for st,pr in obs))
            if i is None:continue
            catnum=cat(pref);counts[catnum]+=num
            ss[catnum][i]+=num
            mk.setdefault(key,[0,0,0])[catnum] |= 1<<i
            countvalid+=num
        out[h]={'total':total,'allowed':countvalid,'groups':counts,'sig_by_group':ss,'keys':len(mk),'rank_all':sum(rank9(a|b|c) for a,b,c in mk.values()),'rank_esc':sum(rank9(c) for a,b,c in mk.values()),'states':len(cur)}
        if h in (8,9): out[h]['masks']={','.join(map(str,k)):v for k,v in mk.items()}
        print('h',h,'states',len(cur),'words',total,'allowed',countvalid,'classes',counts,'keys',len(mk),flush=True)
    common=set(out[8]['masks'])&set(out[9]['masks'])
    out['common']={'rank_all':sum(rank9(out[8]['masks'][k][0]|out[8]['masks'][k][1]|out[8]['masks'][k][2]) and rank9(out[9]['masks'][k][0]|out[9]['masks'][k][1]|out[9]['masks'][k][2]) for k in common),'rank_esc':sum(rank9(out[8]['masks'][k][2]) and rank9(out[9]['masks'][k][2]) for k in common),'no_esc_keys':sorted(k for k in common if not (rank9(out[8]['masks'][k][2]) and rank9(out[9]['masks'][k][2]))}
    print('common',out['common'])
    with open('INDEPENDENT_DP_REPORT_EC49FAU.json','w') as f: json.dump({str(k):v for k,v in out.items()},f,sort_keys=True,indent=2)
if __name__=='__main__':main()
