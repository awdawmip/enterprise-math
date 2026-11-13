#!/usr/bin/env python3
"""EC49FNW exact census checker; source DP numerical computation is in C++ extension.

Usage:
python VERIFY_EC49FNW_CENSUS.py EC49FNW_ALL_84_EDGE_DELTAS.txt \
  FIRST_NEUTRAL_EDGES_EC49FNS.txt [FNW_RESULTS.txt]
"""
import sys

def read_pairs(path):
    result = []
    with open(path, encoding="utf-8") as stream:
        for line in stream:
            line=line.split("#", 1)[0].strip()
            if line:
                a,b=map(int,line.split())
                result.append((a,b))
    return result

def verify(table, edges, output=None):
    records=[]
    with open(table, encoding="utf-8") as stream:
        for line in stream:
            line=line.split("#",1)[0].strip()
            if line:
                a,b,ab,ba=map(int,line.split())
                assert ab>=0 and ba>=0
                records.append((a,b,ab,ba))
    expected=read_pairs(edges)
    assert len(expected)==len(records)==84
    assert [rec[:2] for rec in records]==expected
    both=sum(ab==0 and ba==0 for _,_,ab,ba in records)
    one=sum((ab==0) != (ba==0) for _,_,ab,ba in records)
    neither=84-both-one
    directed=2*both+one
    assert (both,one,neither,directed)==(30,43,11,103)

    if output:
        env={}
        old={}
        with open(output,encoding="utf-8") as stream:
            for line in stream:
                s=line.split()
                if not s: continue
                if s[0]=="ENVELOPE":
                    a,b,dom,margin,delta=map(int,s[1:6])
                    roots=list(map(int,s[6:10]))
                    cuts,fail,extra=map(int,s[10:13])
                    assert delta==sum(roots) and (delta==0)==bool(dom)
                    assert margin>0 and cuts>=0 and fail>=0 and extra>=0
                    assert (a,b) not in env
                    env[a,b]=(delta,cuts,fail,extra)
                elif s[0]=="TRANSFER":
                    a,b=map(int,s[1:3])
                    assert s[-1]=="1"
                    old[a,b]=s
        assert len(env)==len(old)==168
        for a,b,ab,ba in records:
            assert env[a,b][0]==ab and env[b,a][0]==ba
        assert sum(env[a,b][1] for a,b in env if env[a,b][0]==0)==10429
        assert sum(env[a,b][2] for a,b in env if env[a,b][0]==0)==0
        assert sum(env[a,b][3] for a,b in env if env[a,b][0]==0)==0
    print(f"EXACT_CENSUS_OK edges={len(records)} both={both} one={one} "
          f"neither={neither} dominance_directions={directed} "
          f"full_output_checked={bool(output)}")

if __name__=="__main__":
    if len(sys.argv) not in (3,4):
        raise SystemExit(__doc__)
    verify(*sys.argv[1:])
