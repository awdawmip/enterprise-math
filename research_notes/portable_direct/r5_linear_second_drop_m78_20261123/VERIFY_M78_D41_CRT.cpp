// Exact finite-field Hasse-jet witness extension for frozen R5 scalar five-event observer.
// Science pin: awdawmip/enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15.
// Each nonzero coefficient with j<=n_d-2 proves a characteristic-zero double pole.
#include <bits/stdc++.h>
using namespace std;
struct Jet {int c[3];};
int P,J,Z;
inline Jet zero(){return {{0,0,0}};}
inline Jet one(){return {{1,0,0}};}
inline int mod(long long x){x%=P;return x<0?x+P:x;}
inline Jet sub(Jet a,Jet b){Jet r=zero();for(int j=0;j<=J;++j)r.c[j]=mod(a.c[j]-b.c[j]);return r;}
inline void addIn(Jet &a,Jet b){for(int j=0;j<=J;++j)a.c[j]=mod(a.c[j]+b.c[j]);}
inline Jet mul(Jet a,Jet b){Jet r=zero();for(int j=0;j<=J;++j)for(int k=0;k<=j;++k)r.c[j]=mod(r.c[j]+a.c[k]*b.c[j-k]);return r;}
int mpow(int a,int n){int r=1;while(n){if(n&1)r=mod((long long)r*a);a=mod((long long)a*a);n>>=1;}return r;}
inline Jet qpow(int a){Jet r=zero();int za=mpow(Z,a);r.c[0]=za;if(J>=1)r.c[1]=mod((long long)za*a);if(J>=2)r.c[2]=mod((long long)za*a*(a-1)/2);return r;}
vector<int> events[5];
vector<int> supportFor(int mask){vector<int> v;for(int x=214;x<=221;x++){for(int e=0;e<3;e++)if(mask&(1<<e))if(find(events[e].begin(),events[e].end(),x)!=events[e].end()){v.push_back(x);break;}}return v;}
Jet overlap(int m,int d){Jet total=zero();for(int mask=1;mask<8;mask++){
  vector<int> sel,sup=supportFor(mask);for(int k=0;k<3;k++)if(mask&(1<<k))sel.push_back(k);
  int r=sel.size(),zcount=0;for(int a:sup)if(a%d==0)++zcount;if(zcount>J)continue;
  Jet block=one();for(int a:sup)block=mul(block,sub(one(),qpow(a)));
  vector<int> strides(r,1);for(int k=r-2;k>=0;k--)strides[k]=strides[k+1]*m;
  int n=1;for(int k=0;k<r;k++)n*=m;
  vector<Jet> dp(n,zero());dp[0]=one();
  for(int a:sup){
    int offset=0,delta[3]={0,0,0};
    for(int k=0;k<r;k++){delta[k]=find(events[sel[k]].begin(),events[sel[k]].end(),a)!=events[sel[k]].end();offset+=delta[k]*strides[k];}
    Jet x=qpow(a);
    for(int flat=offset;flat<n;flat++){
      bool allowed=true;for(int k=0;k<r;k++)if(delta[k] && (flat/strides[k])%m==0){allowed=false;break;}
      if(allowed)addIn(dp[flat],mul(x,dp[flat-offset]));
    }
  }
  Jet pref=zero();for(auto &a:dp)addIn(pref,a);
  Jet term=mul(block,pref);if(r%2==0)term=sub(zero(),term);addIn(total,term);
}return total;}
Jet disjoint(int m,int d,const vector<int> &sup){
 int zcount=0;for(int a:sup)if(a%d==0)++zcount;if(zcount>J)return zero();
 vector<Jet> h(m,zero());h[0]=one();Jet block=one();
 for(int a:sup){Jet x=qpow(a);block=mul(block,sub(one(),x));for(int j=1;j<m;j++)addIn(h[j],mul(x,h[j-1]));}
 Jet pref=zero();for(auto &v:h)addIn(pref,v);return mul(block,pref);
}
Jet numerator(int m,int d,int p,int z,int j){P=p;Z=z;J=j;Jet a=overlap(m,d),b=disjoint(m,d,events[3]),c=disjoint(m,d,events[4]);return sub(one(),mul(mul(sub(one(),a),sub(one(),b)),sub(one(),c)));}
// Independent finite-prime CRT certificate, m=78, primitive order d=41.
int main(){
 events[0]={214,215,216,217,218};
 events[1]={214,216,217,218,219,220,221};
 events[2]={215,216,217,218,219,220,221};
 int ps[][2]={{83,4},{739,478},{821,159},{1231,1000},{1559,1490},{2297,1862},{2707,632}};
 cout<<"m,prime,root,primitive_zero_count,total_primitive_roots,first_failed_k,failed_residue\n";
 for(auto item:ps){
  int p=item[0],z=item[1];P=p;J=0;Z=z;
  if(mpow(z,41)!=1||z==1){cerr<<"invalid primitive root"<<p<<"\n";return 2;}
  int zeros=0,first_failed=0,bad_value=0;
  for(int k=1;k<=40;k++){
   Z=mpow(z,k);
   Jet a=overlap(78,41);
   if(a.c[0]==0)zeros++;
   else if(!first_failed){first_failed=k;bad_value=a.c[0];}
  }
  cout<<78<<','<<p<<','<<z<<','<<zeros<<",40,"<<first_failed<<','<<bad_value<<'\n';
  if(zeros!=40)return 1;
 }
}
