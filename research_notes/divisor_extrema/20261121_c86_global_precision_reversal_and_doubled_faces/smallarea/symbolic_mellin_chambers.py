"""Exact finite algebra for the 15-kernel radial Mellin representation."""
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import json
from line_kernel import load_terms,support,width_breaks,width_line,width_pieces

CUTS=[F(0),F(1,3),F(1,2),F(2,3),F(1)]

def spline(poly,r):
    sp=support(poly,r)
    if sp is None:return []
    lo,hi=sp
    cuts=sorted(set([lo,hi]+[t for t in width_breaks(poly)if lo<t<hi]))
    slopes=[0]
    for l,h in zip(cuts,cuts[1:]):
        A,B=width_line(poly,(l+h)/2);slopes.append(-B)
    slopes.append(0)
    return [(r*t,F(slopes[i+1]-slopes[i]))for i,t in enumerate(cuts)if slopes[i+1]!=slopes[i]]

def affine_spline(poly,l,h):
    r1=(2*l+h)/3;r2=(l+2*h)/3
    u=spline(poly,r1);v=spline(poly,r2)
    assert len(u)==len(v)
    out=[]
    for (x,a),(y,b)in zip(u,v):
        assert a==b
        slope=(y-x)/(r2-r1);intercept=x-slope*r1
        out.append((intercept,slope,a))
    rm=(l+h)/2
    assert [(a+b*rm,c)for a,b,c in out]==spline(poly,rm)
    return out

def orient(triple):
    for x in triple:
        if x:
            return tuple(-y for y in triple)if x<0 else tuple(triple)
    return tuple(triple)

def main():
    terms=load_terms();splines=[];width_values=set()
    for p,c in terms:
        splines.append([affine_spline(p,l,h)for l,h in zip(CUTS,CUTS[1:])])
        for l,h,A,B in width_pieces(p):
            for t in [l,h]:
                if t is not None:width_values.add(F(A)+B*t)
    assert width_values=={F(1),F(3,2),F(2),F(3)}
    chambers=[]
    for ri in range(4):
        for si in range(ri+1):
            merged=defaultdict(F);rawcount=0
            for k,(p,c)in enumerate(terms):
                for ai,bi,di in splines[k][ri]:
                    for aj,bj,dj in splines[k][si]:
                        triple=orient((-aj,ai,bi-bj))
                        merged[triple]+=c*di*dj;rawcount+=1
            rows=[{'a_r':str(a),'b_s':str(b),'c_rs':str(c),'weight':str(w)}
                  for (a,b,c),w in sorted(merged.items())if w and(a or b or c)]
            chambers.append({'r_index':ri,'s_index':si,'r_interval':list(map(str,CUTS[ri:ri+2])),
                             's_interval':list(map(str,CUTS[si:si+2])),
                             'raw_terms':rawcount,'combined_terms':len(rows),'terms':rows})
    data={'schema':'C86_EXACT_MELLIN_CHAMBERS_V1','cuts':list(map(str,CUTS)),
          'exponent':'41/20','terms_interpretation':'Sum weight * abs(a_r*r+b_s*s+c_rs*r*s)^(41/20); on s=x*r divide by r^(41/20) to obtain H(r,x).',
          'width_break_values':list(map(str,sorted(width_values))),
          'chambers':chambers,
          'scaled_splines':[{'polygon':p,'coefficient':str(c),
                            'pieces':[[{'intercept':str(a),'slope':str(b),'jump':str(j)}for a,b,j in arr]for arr in ss]}
                           for (p,c),ss in zip(terms,splines)]}
    Path(__file__).with_name('mellin_chambers.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps([{k:v for k,v in row.items()if k!='terms'}for row in chambers],indent=2))

if __name__=='__main__':main()
