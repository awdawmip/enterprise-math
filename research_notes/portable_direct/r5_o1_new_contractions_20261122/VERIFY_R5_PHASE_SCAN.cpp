// Frozen R5 event-support exact finite-field threshold scan.
// Compile: g++ -std=c++17 -O2 -Wall -Wextra VERIFY_R5_PHASE_SCAN.cpp -o scan
// Run: ./scan 125
#include <bits/stdc++.h>
using namespace std;
using ll=long long;
struct Jet {int f=0,g=0;};
int MOD;
Jet add(Jet a,Jet b){return {int((ll(a.f)+b.f)%MOD),int((ll(a.g)+b.g)%MOD)};}
Jet sub(Jet a,Jet b){return {int((ll(a.f)-b.f+MOD)%MOD),int((ll(a.g)-b.g+MOD)%MOD)};}
Jet mul(Jet a,Jet b){return {int(ll(a.f)*b.f%MOD),int((ll(a.g)*b.f+ll(a.f)*b.g)%MOD)};}
Jet one{1,0},zero{0,0};
int modpow(int a,int n){ll y=1,b=a;while(n){if(n&1)y=y*b%MOD;b=b*b%MOD;n>>=1;}return (int)y;}
bool prime(int a){if(a<2)return false;for(int d=2;d*d<=a;d++)if(a%d==0)return false;return true;}
vector<int>pf(int n){vector<int>a;for(int d=2;d*d<=n;d++)if(n%d==0){a.push_back(d);while(n%d==0)n/=d;}if(n>1)a.push_back(n);return a;}
pair<int,int> primitive(int d){int p=10001;while(p%d!=1||!prime(p))p++;MOD=p;for(int b=2;b<p;b++){int w=modpow(b,(p-1)/d);bool ok=modpow(w,d)==1;for(int q:pf(d))if(modpow(w,d/q)==1)ok=false;if(ok)return {p,w};}throw runtime_error("no generator");}
vector<vector<int>> S={ {214,215,216,217,218}, {214,216,217,218,219,220,221}, {215,216,217,218,219,220,221}, {},{} };
Jet P_factors(const vector<int>& ps,const vector<Jet>& xp){Jet r=one;for(int p:ps)r=mul(r,sub(one,xp[p]));return r;}
// The threshold polynomial Q_m for joint events with selected mask; exact joint counts, not independent events.
vector<Jet> core(int mask,int cap,const vector<Jet>& xp){
  vector<int> ids, U;for(int j=0;j<3;j++)if(mask&(1<<j))ids.push_back(j);
  for(int j:ids)for(int p:S[j]) U.push_back(p);
  sort(U.begin(),U.end());U.erase(unique(U.begin(),U.end()),U.end());
  int n=ids.size(), base=cap+1, total=1;for(int i=0;i<n;i++)total*=base;
  vector<int> shift(U.size(),0),im(U.size(),0);
  for(size_t z=0;z<U.size();z++){
    int coeff=1;for(int i=0;i<n;i++,coeff*=base){if(find(S[ids[i]].begin(),S[ids[i]].end(),U[z])!=S[ids[i]].end()){shift[z]+=coeff;im[z]|=1<<i;}}
  }
  vector<Jet> dp(total,zero); dp[0]=one;
  for(size_t z=0;z<U.size();z++){
    int delta=shift[z], p=U[z], support=im[z];
    for(int code=0;code<total;code++){
      int tmp=code;bool can=true;
      for(int k=0;k<n;k++){int v=tmp%base;tmp/=base;if((support>>k&1)&&v==0){can=false;break;}}
      if(can) dp[code]=add(dp[code],mul(xp[p],dp[code-delta]));
    }
  }
  // Layer by max occupancy, so one DP gives all m<=cap+1.
  vector<Jet> layer(cap+1,zero), ans(cap+2,zero);
  for(int code=0;code<total;code++){
    int tmp=code, mx=0;for(int k=0;k<n;k++){mx=max(mx,tmp%base);tmp/=base;}
    layer[mx]=add(layer[mx],dp[code]);
  }
  Jet fact=P_factors(U,xp);Jet sum=zero;
  for(int m=1;m<=cap+1;m++){sum=add(sum,layer[m-1]);ans[m]=mul(sum,fact);}
  return ans;
}
vector<Jet> single(int j,int cap,const vector<Jet>& xp){
  vector<Jet> dp(cap+1,zero),ans(cap+2,zero);dp[0]=one;
  for(int p:S[j])for(int r=1;r<=cap;r++)dp[r]=add(dp[r],mul(xp[p],dp[r-1]));
  Jet fact=P_factors(S[j],xp),sum=zero;
  for(int m=1;m<=cap+1;m++){sum=add(sum,dp[m-1]);ans[m]=mul(sum,fact);}return ans;
}
int main(int argc,char**argv){
  for(int i=223;i<=290;i++)S[3].push_back(i);
  for(int i=296;i<=312;i++)S[4].push_back(i);
  int M= argc>1?stoi(argv[1]):100; vector<int> W={7,9,11,13,17,19,23,25,27,29,31,32,37,43};
  cout<<"m,d,prime,root,R0,DR0,pole,witness\n";
  for(int d:W){auto [p,w]=primitive(d);vector<Jet> xp(315);for(int j=0;j<315;j++){int v=modpow(w,j%d);xp[j]={v,int(ll(j)*v%MOD)};}
    vector<Jet> A(M+1,zero);
    for(int mask=1;mask<8;mask++){auto V=core(mask,M-1,xp);int sign=__builtin_popcount((unsigned)mask)%2;
      for(int m=1;m<=M;m++)A[m]=sign?add(A[m],V[m]):sub(A[m],V[m]);
    }
    auto B=single(3,M-1,xp),C=single(4,M-1,xp);
    int pole=0;for(int price=214;price<=314;price++)pole+=(price%d==0);
    for(int m=1;m<=M;m++){
      Jet R=sub(one,mul(mul(sub(one,A[m]),sub(one,B[m])),sub(one,C[m])));
      bool witness=pole>=3&&(R.f!=0||(pole>=4&&R.g!=0));
      cout<<m<<','<<d<<','<<p<<','<<w<<','<<R.f<<','<<R.g<<','<<pole<<','<<(witness?1:0)<<'\n';
    }
  }
}
