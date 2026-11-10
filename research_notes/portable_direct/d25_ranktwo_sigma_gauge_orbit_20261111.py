"""D25 exact gauge-orbit model checker. AUTHOR_SIDE; not original H0/B0 [X]U."""
from itertools import product
def add(a,b,m): return ((a[0]+b[0])%m,(a[1]+b[1])%m)
def neg(a,m): return ((-a[0])%m,(-a[1])%m)
def mul(a,b,m): return ((a[0]*b[0]+2*a[1]*b[1])%m,(a[0]*b[1]+a[1]*b[0])%m)
def sig(a,m): return (a[0]%m,-a[1]%m)
def mm(a,b,m): return [[add(mul(a[i][0],b[0][j],m),mul(a[i][1],b[1][j],m),m) for j in range(2)] for i in range(2)]
def sm(a,m): return [[sig(c,m) for c in row] for row in a]
def E(): return [[(1,0),(0,0)],[(0,0),(1,0)]]
def B(p): return [[(0,0),(1,0)],[(p,0),(0,0)]]
def F(p,b,d):
    m=p*p; pb=mul((p,0),b,m);pd=mul((p,0),d,m)
    return [[neg(mul((p,0),sig(d,m),m),m),add((1,0),pb,m)],[(p,0),pd]]
def G(p,b,d):
    m=p*p;pb=mul((p,0),b,m);pd=mul((p,0),d,m)
    return ([[add((1,0),neg(pb,m),m),(0,0)],[neg(pd,m),(1,0)]],
            [[add((1,0),pb,m),(0,0)],[pd,(1,0)]])
def verify(p,b,d):
    m=p*p;f=F(p,b,d);g,gi=G(p,b,d)
    assert mm(g,gi,m)==E()==mm(gi,g,m)
    assert mm(gi,mm(B(p),sm(g,m),m),m)==f
    assert mm(f,sm(f,m),m)==[[(p,0),(0,0)],[(0,0),(p,0)]]
    assert [[(u%p,v%p) for u,v in row] for row in f]==[[(0,0),(1,0)],[(0,0),(0,0)]]
    return tuple(c for row in f for c in row)
def main():
    p=5;m=p*p;vals=list(product(range(p),repeat=2))
    fs={verify(p,b,d) for b in vals for d in vals}
    assert len(fs)==p**4==625
    st=set()
    for z in vals:
        for v in vals:
            y=[[sig(z,m),v],[(0,0),z]]
            g=[[add((int(i==j),0),mul((p,0),y[i][j],m),m) for j in range(2)] for i in range(2)]
            gi=[[add((int(i==j),0),neg(mul((p,0),y[i][j],m),m),m) for j in range(2)] for i in range(2)]
            assert mm(g,gi,m)==E()
            assert mm(gi,mm(B(p),sm(g,m),m),m)==B(p)
            st.add(tuple(c for row in g for c in row))
    assert len(st)==p**4
    print({"p":p,"fixed_basis_lifts":len(fs),"stabilizer":len(st),"K1_order":p**8,"gauge_orbits":1})
    for p,b,d in [(13,(0,1),(1,1)),(19,(1,2),(0,1)),(373,(0,1),(1,1))]:
        print({"p":p,"modulus":p*p,"b":b,"d":d,"F":verify(p,b,d)})
    print("native_h0b0_run=False")
if __name__=="__main__": main()
