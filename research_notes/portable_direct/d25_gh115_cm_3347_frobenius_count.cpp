// Direct exact F_{p^2} character-sum point count for C_T, T=2sqrt(2)/3.
// F_{p^2}=F_p[r]/(r^2-2), valid for tested p % 8 == 3.
// This is a portable independent character-sum computation, not native EM.
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
using ll=long long;
static ll power_mod(ll a,ll e,int p){ll z=1;while(e){if(e&1)z=z*a%p;a=a*a%p;e>>=1;}return z;}
static inline int modp(ll a,int p){int r=(int)(a%p);return r<0?r+p:r;}
static ll trace_for(int p){
    assert(p%8==3 && p>3);
    vector<int> chi(p),s(p),c(p);
    for(int k=0;k<p;k++){
        chi[k]= k==0?0:(power_mod(k,(p-1)/2,p)==1?1:-1);
        s[k]=modp(1LL*k*k,p);
        c[k]=modp(1LL*s[k]*k,p);
    }
    int k0=(int)power_mod(8,p-2,p),k1=(int)power_mod(12,p-2,p);
    ll total=0;
    for(int a=0;a<p;a++){
        int a2=s[a],a3=c[a];
        for(int b=0;b<p;b++){
            int b2=s[b],b3=c[b];
            ll v0 = a3 + 6LL*a*b2 + a2 + 2LL*b2 + 1LL*k0*a + 2LL*k1*b;
            ll v1 = 3LL*a2*b + 2LL*b3 + 2LL*a*b + 1LL*k0*b + 1LL*k1*a;
            int v0r=modp(v0,p), v1r=modp(v1,p);
            int n=modp(1LL*v0r*v0r-2LL*v1r*v1r,p);
            total+=chi[n];
        }
    }
    return -total;
}
int main(){
    for(int p:{11,19,43,59,3347}){
        ll aq=trace_for(p);
        // Show Hasse trace congruence with known exact E values,
        // independent of the polynomial recurrence.
        cout<<"p "<<p<<" q "<<1LL*p*p<<" trace_aq "<<aq
            <<" curve_points "<<1LL*p*p+1-aq<<" trace_mod_p "<<modp(aq,p)<<"\n";
        if(p==3347){ assert(aq==-6106);assert(modp(aq,p)==588); }
    }
    cout<<"PASS_GH115_CM_FROBENIUS_DIRECT_Q_COUNT"<<'\n';
}
