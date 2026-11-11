"""Verify both mixed two-letter sync words for 3 <= Y < 10**1000."""
from verify_55 import convergents, cube_root_floor

def ceildiv(a,b): return -((-a)//b)

def main():
    B=10**1000
    scale=10**2200
    root=cube_root_floor(4*scale**3)
    assert root**3<4*scale**3<(root+1)**3
    cf=convergents(root,scale,B)
    assert cf==convergents(root+1,scale,B) and cf[-1][1]>=B
    count=passed=0
    solutions=[]
    prev=(1,0)
    mod=65521
    for i,(u,v) in enumerate(cf[:-1]):
        u0,v0=prev
        prev=(u,v)
        limit=min(B,cf[i+1][1])
        if limit<=v: continue
        for t in range(-2,3):
            for s in range(ceildiv(max(v,3)-t*v0,v),ceildiv(limit-t*v0,v)):
                x,y=s*u+t*u0,s*v+t*v0
                count+=1
                xm,ym=x%mod,y%mod
                resid=(xm**3-7*xm-4*(ym**3-ym))%mod
                if resid not in {6,mod-6}: continue
                passed+=1
                a=x**3-7*x-4*(y**3-y)
                if abs(a)!=6: continue
                word='75' if a==6 else '57'
                num=x-y+(1 if word=='75' else 2)
                if num%3: continue
                c=num//3;K=y+1-c
                if c>=1 and K>=3: solutions.append((word,c,K))
    print('convergent records',len(cf),'candidates',count,'modular survivors',passed,'solutions',solutions)
    assert solutions==[('75',7,28)]
if __name__=='__main__': main()
