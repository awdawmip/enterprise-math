#!/usr/bin/env python3
"""Exact 4-colour native prefix-union minimum via trie Steiner DP.
Pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Pure integer computation.
"""
import os, json, argparse
from collections import Counter
from pathlib import Path
from BRC_ORIGINAL_MODEL_EC49FFJ import candidates,native,observed
SIG=(1,2,4,8)
ALL=(1<<len(SIG))-1
INF=1000000000

def admissible_keys(h):
    # a=z-1, e=z, c+d=x+y-h-1, f=h+1-y-2z, g=h+1-x
    for z in range(1, (h+1)//2+1):
        for x in range(2*z,h+2):
            for y in range(0,h+2-2*z):
                if x+y-h-1>=1 and h+1-y-2*z>=0 and h+1-x>=0:
                    yield (x,y,z)

def make_trie(h,key):
    children=[{}]; terminal=[{}]; counts=Counter(); total=0
    for word,sig in candidates(h,key):
        if sig not in SIG:continue
        counts[sig]+=1; total+=1
        if observed(word)!=sig:raise AssertionError(word)
        axis=native(word)
        if len(axis)!=2*(sum(key)-1):raise AssertionError((key,word))
        c=Counter(axis)
        if tuple(c[i]-c[-i] for i in range(1,7))!=(2,0,0,0,0,0) or tuple(c[i] for i in (1,2,3))!=key:
            raise AssertionError((key,word))
        p=0
        for a in axis:
            nxt=children[p].get(a)
            if nxt is None:
                nxt=len(children);children[p][a]=nxt;children.append({});terminal.append({})
            p=nxt
        terminal[p].setdefault(sig,word)
    assert all(counts[s] for s in SIG),(key,counts)
    return children,terminal,[counts[s] for s in SIG],total

def merge(dp, child_dp):
    out=dp[:]
    for a in range(16):
        v=dp[a]
        if v==INF:continue
        rest=ALL^a
        sub=rest
        while sub:
            if child_dp[sub]!=INF:
                j=a|sub;w=v+child_dp[sub]+1
                if w<out[j]:out[j]=w
            sub=(sub-1)&rest
    return out

def solve(h,key,need_witness=True):
    children,terminal,counts,total=make_trie(h,key)
    dp=[None]*len(children)
    for p in range(len(children)-1,-1,-1):
        leaf=terminal[p]
        dp0=[INF]*16;dp0[0]=0
        term_mask=sum(1<<SIG.index(s) for s in leaf)
        sub=term_mask
        while sub:
            dp0[sub]=0
            sub=(sub-1)&term_mask
        for child in children[p].values():
            dp0=merge(dp0,dp[child])
        dp[p]=dp0
    cost=dp[0][15]
    assert cost<INF
    witness={}
    if need_witness:
        def recover(p,target):
            cs=list(children[p].values())
            pre=[None]*(len(cs)+1)
            pre[0]=[INF]*16;pre[0][0]=0
            tmask=sum(1<<SIG.index(s) for s in terminal[p]); sub=tmask
            while sub:pre[0][sub]=0;sub=(sub-1)&tmask
            for k,ch in enumerate(cs):pre[k+1]=merge(pre[k],dp[ch])
            assert pre[-1][target]==dp[p][target]
            # reverse subassign to each child
            remain=target
            for k in range(len(cs)-1,-1,-1):
                ch=cs[k];sub=remain;picked=None
                while True:
                    before=remain^sub
                    if pre[k][before]!=INF and (sub==0 or dp[ch][sub]!=INF):
                        v=pre[k][before]+(dp[ch][sub]+1 if sub else 0)
                        if v==pre[k+1][remain]:picked=sub;break
                    if sub==0:break
                    sub=(sub-1)&remain
                assert picked is not None,(h,key,p,k,remain)
                if picked:recover(ch,picked)
                remain^=picked
            assert remain&~tmask==0
            for sig in SIG:
                if remain & (1<<SIG.index(sig)):
                    witness[str(sig)]=terminal[p][sig]
        recover(0,15)
        assert len(witness)==4,witness
        union={}
        ps=set()
        for s,w in witness.items():
            n=native(w)
            for d in range(1,len(n)+1):ps.add(n[:d])
        assert len(ps)==cost,(h,key,cost,len(ps))
    return {'h':h,'key':list(key),'prefix_optimum':cost,'counts':counts,'word_count':total,'trie_nodes':len(children),'witness':witness}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--hmin',type=int,default=2);parser.add_argument('--hmax',type=int,default=6);parser.add_argument('--out',default='EXACT_REPORT_EC49FFJ.json');a=parser.parse_args()
    rows=[]
    for h in range(a.hmin,a.hmax+1):
        for key in admissible_keys(h):
            r=solve(h,key);rows.append(r)
            print(h,key,'cost',r['prefix_optimum'],'words',r['word_count'],'trie',r['trie_nodes'],flush=True)
    rep={'schema':'EC49FFJ_TRIE_STEINER_DP_V1','scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab','horizon':[a.hmin,a.hmax], 'method':'Exact rooted directed trie cover by four terminal colours; 16-mask integer DP; separate witness validation against original observer and six-axis ordered signed microsteps', 'rows':rows,'min_per_h':{str(h):min(r['prefix_optimum'] for r in rows if r['h']==h) for h in range(a.hmin,a.hmax+1)}, 'status':'EXACT_TRIE_DP_PASS'}
    Path(a.out).write_text(json.dumps(rep,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print('MIN',rep['min_per_h'],flush=True)
if __name__=='__main__':main()
