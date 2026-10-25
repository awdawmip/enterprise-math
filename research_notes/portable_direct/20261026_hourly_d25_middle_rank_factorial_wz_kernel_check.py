"""Verify the corrected Clausen middle factorial kernel and O(p) signed moment readout.
Run beside 20261026_hourly_d25_corrected_clausen_jet_reflection_p4_bridge_check.py.
Exact Python stdlib; no CM simulator, mathematical acceptance, or native experiment.
"""
from pathlib import Path
import runpy
prior=runpy.run_path(str(Path(__file__).with_name(
    "20261026_hourly_d25_corrected_clausen_jet_reflection_p4_bridge_check.py")))

def check(p):
    m=(p-1)//6
    f=[1]*p
    for i in range(1,p):f[i]=f[i-1]*i%p
    def divide(a,b):return a*pow(b,-1,p)%p
    def middle_jet(j):
        return divide((-1)**(m+j+1)*f[m]*f[j-m-1]*f[2*m],
                      f[2*m-j]*f[j]*f[j])
    def reverse_high_jet(ell):
        return divide(2*f[m]*f[2*m]*f[ell-1]*f[ell-1],
                      f[ell+m]*f[ell+2*m])
    u=prior["corrected_jets"](p)
    for j in range(m+1,2*m+1):
        assert u[j][1]%p==middle_jet(j),(p,j,"middle jet")
    for ell in range(1,2*m+1):
        assert u[p-ell][2]%p==reverse_high_jet(ell),(p,ell,"high jet")
    direct=0
    for j in range(m+1,2*m+1):
        for ell in range(1,j+1):
            direct+=(6*(j-ell)+1)*pow(2,-j-1+ell,p)*middle_jet(j)*reverse_high_jet(ell)
    direct=-direct*pow(108,-1,p)%p
    P=T=total=0
    for j in range(1,2*m+1):
        h=reverse_high_jet(j)
        v=pow(2,j,p)*h%p
        P=(P+v)%p
        T=(T+j*v)%p
        if j>m:
            total+=middle_jet(j)*pow(2,-j-1,p)*((6*j+1)*P-6*T)
    compressed=-total*pow(108,-1,p)%p
    assert compressed==direct,(p,compressed,direct)
    # Third route, original 1/6,1/3 Pochhammer source (no parameter jets).
    r=prior["original_source"](p)
    raw=2*sum((6*(j+p-ell)+1)*r[j]*r[p-ell]
              for j in range(m+1,2*m+1)
              for ell in range(1,j+1))%(p**4)
    assert raw%(p**3)==0
    assert raw//(p**3)==compressed,(p,raw//(p**3),compressed)
    return p,compressed

if __name__=="__main__":
    out=[check(p) for p in prior["primes_1mod6"](211)]
    print("PASS:",len(out),"primes; factorial jets, two-moment and original signed p^3 port")
    for p,k in out:
        if p in (7,13,19,31):print(f"p={p}, middle_port/p mod p={k}")
