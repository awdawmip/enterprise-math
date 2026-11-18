"""All-phase ANOVA and diagonal Fourier integrals, using the C80 physical source."""
import argparse
from functools import cache
from fractions import Fraction as F
import json
import math
from pathlib import Path
import subprocess
import tempfile
from mpmath import iv
import critical_bins as C
import extrema as E
from profile import physical_pairs
HERE=Path(__file__).resolve().parent
Q=1<<48
S=1<<55
iv.dps=45

@cache
def root_digit(j,d):
    angle=2*iv.pi*(d<<(8*j))/Q
    a,b=iv.cos(angle)*S,iv.sin(angle)*S
    x,y=int(a.a),int(b.a)
    assert x-1<=a and a<=x+1 and y-1<=b and b<=y+1
    return x,y

def root(t):
    t%=Q
    x,y=S,0
    for j in range(6):
        d=t&255
        t>>=8
        if d:
            a,b=root_digit(j,d)
            x,y=(x*a-y*b)//S,(x*b+y*a)//S
    return x,y

def bracket(lo,hi,unit=10**14):
    return [math.floor(lo*unit),math.ceil(hi*unit)]

def amp_bracket(x,y,den,pi_power):
    nominal=iv.sqrt(iv.mpf(x*x+y*y))/(den*(2*iv.pi)**pi_power)
    error=iv.mpf(4)/Q+iv.mpf(1024)/S
    return [max(0,int(((nominal-error)*10**14).a)),
            int(((nominal+error)*10**14).b)+1]

def prepare_ranks(c):
    E.UNIT=Q
    p=((c**9).bit_length()-1)//4
    # Inner kernels are each used once; outer kernels repeat within a row.
    orig=C.kernel
    def kernel(n,s,k):
        return orig(n,s,k) if k!=3 else orig.__wrapped__(n,s,k)
    kernel.cache_clear=orig.cache_clear
    C.kernel=kernel
    try:
        for bits in (176,240,360):
            C.BITS=bits
            C.UNIT=1<<bits
            C.ONE=(C.UNIT,C.UNIT)
            try:
                xx,yy=zip(*physical_pairs(c))
                x=E.axis(xx,p)
                del xx
                y=E.axis(yy,p)
                return p,bits,x,y
            except ArithmeticError:
                if bits==360: raise
    finally:
        C.kernel=orig

def run_axis(x,y):
    xb,xt,nx,xc=x
    yb,yt,ny,yc=y
    n=len(xb)
    first=second=conditional_second=0
    prev_first=prev_re=prev_im=0
    x_re=x_im=y_re=y_im=0
    diag_re=diag_im=anti_re=anti_im=0
    width=0
    with tempfile.TemporaryFile(mode='w+') as inp:
        print(n,nx,ny,file=inp)
        print(*xc,file=inp)
        print(*yc,file=inp)
        for cut in yc:
            print(*root(cut),file=inp)
        for row in zip(xb,yb,xt,yt):
            print(*row,file=inp)
        inp.seek(0)
        with subprocess.Popen([str(HERE/'phase_slabs')],stdin=inp,stdout=subprocess.PIPE,text=True) as proc:
            for line in proc.stdout:
                parts=line.split()
                if parts[0]=='bounds':
                    bounds=list(map(int,parts[1:]))
                    break
                a,b,m1,m2,re,im=map(int,parts)
                dx=b-a
                width+=dx
                first+=dx*m1
                second+=dx*m2
                conditional_second+=dx*m1*m1
                y_re+=dx*re
                y_im+=dx*im
                cx,cy=root(a)
                rx,ry=cx-S,cy
                dr,di=re-prev_re,im-prev_im
                dm=m1-prev_first
                x_re+=rx*dm
                x_im+=ry*dm
                diag_re+=rx*dr-ry*di
                diag_im+=rx*di+ry*dr
                anti_re+=rx*dr+ry*di
                anti_im+=-rx*di+ry*dr
                prev_re,prev_im,prev_first=re,im,m1
            if proc.wait()!=0: raise RuntimeError('slab sweep failed')
    assert width==Q
    mean=F(first,n*Q**2)
    variance=F(second,n*n*Q**2)-mean**2
    marginal=F(conditional_second,n*n*Q**3)-mean**2
    modes={'x':amp_bracket(x_re,x_im,n*Q*S,1),'y':amp_bracket(y_re,y_im,n*Q*S,1),
           'plus':amp_bracket(diag_re,diag_im,n*S*S,2),
           'minus':amp_bracket(anti_re,anti_im,n*S*S,2)}
    return mean,variance,marginal,modes,bounds

def intersect(a,b):
    res=[max(a[0],b[0]),min(a[1],b[1])]
    assert res[0]<=res[1]
    return res

def summarize(c):
    p,bits,x,y=prepare_ranks(c)
    m,v,vx,z,bounds=run_axis(x,y)
    m2,v2,vy,z2,bounds2=run_axis(y,x)
    assert (m,v,bounds)==(m2,v2,bounds2)
    assert min(vx,vy,v-vx-vy)>=0
    z={'x':intersect(z['x'],z2['y']),'y':intersect(z['y'],z2['x']),
       'plus':intersect(z['plus'],z2['plus']),'minus':intersect(z['minus'],z2['minus'])}
    err=F(16,Q)
    var_bounds=[max(F(0),v-err),v+err]
    comps={'first':(vx,err),'second':(vy,err),'interaction':(v-vx-vy,3*err)}
    ratios={}
    for name,(s,del_s) in comps.items():
        ratios[name]=bracket(max(F(0),s-del_s)/var_bounds[1],
                             min(F(1),(s+del_s)/var_bounds[0]),10**10)
    ratios['first_harmonic_pairs']={}
    for name,interval in z.items():
        low,high=[F(a,10**14) for a in interval]
        ratios['first_harmonic_pairs'][name]=bracket(2*low**2/var_bounds[1],2*high**2/var_bounds[0],10**10)
    return dict(c=c,p=p,templates=c*(c-1)//2,phase_rectangles=x[2]*y[2],
                interval_bits=bits,extrema=bounds,mean_1e14=bracket(m-F(4,Q),m+F(4,Q)),
                variance_1e14=bracket(*var_bounds),component_variance_1e14={
                    k:bracket(max(F(0),s-e),s+e) for k,(s,e) in comps.items()},
                component_shares_1e10=ratios,amplitude_1e14=z)

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('stocks',nargs='+',type=int)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    out=[]
    for c in args.stocks:
        row=summarize(c)
        out.append(row)
        print(json.dumps(row),flush=True)
        args.output.write_text(json.dumps(out,indent=2)+'\n')
