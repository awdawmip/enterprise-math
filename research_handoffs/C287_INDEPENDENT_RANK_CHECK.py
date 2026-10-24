#!/usr/bin/env python3
"""Independent exact row-reduction audit; does not import C287 minor-checker."""
import json
from collections import Counter
import C275_STANDALONE_EXACT_REPLAY as S

def rank_columns(*cols):
    matrix = [[col[row] for col in cols] for row in range(4)]
    pivot_row=0
    for j in range(len(cols)):
        k=next((k for k in range(pivot_row,4) if matrix[k][j]!=0),None)
        if k is None:continue
        matrix[k],matrix[pivot_row] = matrix[pivot_row],matrix[k]
        f=matrix[pivot_row][j]
        for x in range(j,len(cols)):
            matrix[pivot_row][x] /= f
        for ii in range(4):
            if ii==pivot_row:continue
            f=matrix[ii][j]
            for x in range(j,len(cols)):
                matrix[ii][x]-=f*matrix[pivot_row][x]
        pivot_row+=1
    return pivot_row

def main():
    records=json.load(open('C284_187_EXACT_DYADIC_BRACKETS.json',encoding='utf8'))['records']
    table={}
    hs=S.hulls()
    for i,j,wid,k in records:
        lo,hi,kind=hs[(i,j)]
        h=S.high_point(lo,hi)
        table[(wid,h)]=(S.WITNESSES[wid-1],h)
    assert len(table)==125
    table=sorted(table.items())
    counts=Counter()
    for ix in range(len(table)):
        (wa,ha),(w,h)=table[ix]
        d=tuple(x-y for x,y in zip(h,w))
        for iy in range(ix+1,len(table)):
            (wb,hb),(z,g)=table[iy]
            e=tuple(x-y for x,y in zip(g,z))
            delta=tuple(x-y for x,y in zip(z,w))
            if wa==wb:
                assert rank_columns(d,e)==2
                assert not any(delta)
                counts['same_anchor']+=1
            else:
                assert rank_columns(d,e,delta)==3
                counts['different_anchor']+=1
    assert counts=={'same_anchor':7384,'different_anchor':366}
    print('C287_INDEPENDENT_EXACT_RREF_PASS',counts,'total',sum(counts.values()))
if __name__=='__main__':main()
