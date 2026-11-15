// JT2/UR independent exact finite arithmetic sweep; C++17, no external libraries.
// Scope: all primes p <= 20000, p mod 24 in {13,19}.
// Outputs are residues, not a uniform mathematical proof.
#include <bits/stdc++.h>
using namespace std;
using i64 = long long;
i64 power(i64 a, i64 e, i64 mod) {
    i64 r=1;
    for (;e;e>>=1,a=a*a%mod) if(e&1) r=r*a%mod;
    return r;
}
bool is_prime(int p) {
    if(p<2) return false;
    for(int d=2;d*d<=p;d++) if(p%d==0) return false;
    return true;
}
struct Row {int p,m,cm0,J,u,d,epsilon;};
Row examine(int p) {
    int m=(p-1)/6, M=p*p;
    // Since 4m=2n<p, all factorials and (2r+1) are p-units.
    vector<int> f(4*m+1), fi(4*m+1);
    f[0]=1;
    for(int i=1;i<=4*m;i++) f[i]=(i64)f[i-1]*i%M;
    fi[4*m]=power(f[4*m],(i64)p*(p-1)-1,M);
    for(int i=4*m;i>0;i--) fi[i-1]=(i64)fi[i]*i%M;
    i64 twoinv=power(2,(i64)p*(p-1)-2*m,M);
    vector<int> q(m+1);
    // Q_m(Y)=P_{2m}(sqrt Y), coefficients computed in Z/(p^2).
    for(int j=0;j<=m;j++) {
        i64 a=f[2*(m+j)];
        a=a*fi[m-j]%M;
        a=a*fi[m+j]%M;
        a=a*fi[2*j]%M;
        a=a*twoinv%M;
        if((m-j)&1) a=(M-a)%M;
        q[j]=a;
    }
    i64 halfM=power(2,(i64)p*(p-1)-1,M);
    i64 halfP=power(2,p-2,p), qval=0, deriv=0, y=1;
    for(int j=0;j<=m;j++) {
        qval=(qval+(i64)q[j]*y)%M;
        if(j) deriv=(deriv+(i64)j*q[j]*power(halfP,j-1,p))%p;
        y=y*halfM%M;
    }
    vector<int> sq(2*m+1);
    for(int i=0;i<=m;i++)
       for(int j=0;j<=m;j++)
          sq[i+j]=(sq[i+j]+(i64)(q[i]%p)*(q[j]%p))%p;
    i64 J=0; y=1;
    for(int r=0;r<=2*m;r++) {
        J=(J+(i64)sq[r]*power(2*r+1,p-2,p)%p*y)%p;
        y=y*halfP%p;
    }
    int cm0=qval%p;
    int u=cm0? -1:qval/p;
    int eps=cm0? -1:((18LL*u*deriv-2*J-3)%p+p)%p;
    return {p,m,cm0,(int)J,u,(int)deriv,eps};
}
int main(int argc,char**argv) {
    int hi=argc>1?atoi(argv[1]):20000;
    if(hi<5 || hi>20000) {cerr<<"range: 5 <= upper <= 20000\n";return 2;}
    cout<<"p,m,CM0,J,u,d,epsilon\n";
    int all=0,cm0=0,nonzero=0;
    for(int p=5;p<=hi;p++) {
        if((p%24!=13 && p%24!=19)||!is_prime(p)) continue;
        auto r=examine(p);
        cout<<r.p<<','<<r.m<<','<<r.cm0<<','<<r.J<<','<<r.u<<','<<r.d<<','<<r.epsilon<<'\n';
        all++;cm0+=(r.cm0==0);nonzero+=(r.epsilon!=0);
    }
    cerr<<"SUMMARY hi="<<hi<<" total="<<all<<" cm0="<<cm0
        <<" cmfails="<<(all-cm0)<<" e_nonzero="<<nonzero<<"\n";
    return 0;
}
