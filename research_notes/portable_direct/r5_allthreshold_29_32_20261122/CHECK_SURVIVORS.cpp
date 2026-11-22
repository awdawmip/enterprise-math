// Independent local lower-bound witness scan for R5 frozen five-event scalar model.
// All arithmetic is exact in F_p and its Euler first-jet algebra; print full selected pairs.
#include <bits/stdc++.h>
using namespace std;
using ll=long long;
struct Jet {int f=0,g=0;};
int P;
Jet add(Jet a,Jet b){return {int((ll(a.f)+b.f)%P),int((ll(a.g)+b.g)%P)};}
Jet sub(Jet a,Jet b){return {int((ll(a.f)-b.f+P)%P),int((ll(a.g)-b.g+P)%P)};}
Jet mul(Jet a,Jet b){return {int(ll(a.f)*b.f%P),int((ll(a.g)*b.f+ll(a.f)*b.g)%P)};}
Jet one{1,0},zero{0,0};
int powmod(int a,int n){ll y=1,b=a;while(n){if(n&1)y=y*b%P;b=b*b%P;n>>=1;}return int(y);}
bool prime(int a){if(a<2)return false;for(int d=2;d*d<=a;d++)if(a%d==0)return false;return true;}
vector<int> pf(int n){vector<int> f;for(int d=2;d*d<=n;d++)if(n%d==0){f.push_back(d);while(n%d==0)n/=d;}if(n>1)f.push_back(n);return f;}
pair<int,int> primitive(int d){int p=10001;while(p%d!=1||!prime(p))p++;P=p;for(int b=2;b<p;b++){int w=powmod(b,(p-1)/d);bool ok=powmod(w,d)==1;for(int q:pf(d))if(powmod(w,d/q)==1)ok=false;if(ok)return {p,w};}throw runtime_error("no root");}
vector<vector<int>> S={{214,215,216,217,218},{214,216,217,218,219,220,221},{215,216,217,218,219,220,221},{},{}};
Jet prod(const vector<int>& U,const vector<Jet>& xp){Jet t=one;for(int p:U)t=mul(t,sub(one,xp[p]));return t;}
vector<Jet> core(int mask,int M,const vector<Jet>& xp){
  vector<int> ids,U;for(int j=0;j<3;j++)if(mask>>j&1)ids.push_back(j);
  for(int j:ids)for(int p:S[j])U.push_back(p);
  sort(U.begin(),U.end());U.erase(unique(U.begin(),U.end()),U.end());
  int n=ids.size(),base=M,total=1;for(int j=0;j<n;j++)total*=base;
  vector<int> shift(U.size()),supports(U.size());
  for(size_t z=0;z<U.size();z++){
    int factor=1;for(int i=0;i<n;i++,factor*=base)
      if(find(S[ids[i]].begin(),S[ids[i]].end(),U[z])!=S[ids[i]].end()){
        shift[z]+=factor;supports[z]|=1<<i;
      }
  }
  vector<Jet> dp(total);dp[0]=one;
  for(size_t z=0;z<U.size();z++){
    for(int code=0;code<total;code++){
      int tmp=code;bool ok=true;
      for(int i=0;i<n;i++){
        int digit=tmp%base;tmp/=base;
        if((supports[z]>>i&1)&&!digit){ok=false;break;}
      }
      if(ok)dp[code]=add(dp[code],mul(xp[U[z]],dp[code-shift[z]]));
    }
  }
  vector<Jet> layers(M),ans(M+1);for(int code=0;code<total;code++){
    int mx=0,tmp=code;for(int i=0;i<n;i++){mx=max(mx,tmp%base);tmp/=base;}
    layers[mx]=add(layers[mx],dp[code]);
  }
  Jet acc=zero, factor=prod(U,xp);
  for(int m=1;m<=M;m++){acc=add(acc,layers[m-1]);ans[m]=mul(acc,factor);}
  return ans;
}
vector<Jet> single(int j,int M,const vector<Jet>& xp){
  vector<Jet> dp(M),ans(M+1);dp[0]=one;
  for(int p:S[j])for(int r=1;r<M;r++)dp[r]=add(dp[r],mul(xp[p],dp[r-1]));
  Jet acc=zero,factor=prod(S[j],xp);
  for(int m=1;m<=M;m++){acc=add(acc,dp[m-1]);ans[m]=mul(acc,factor);}
  return ans;
}
int main(){
  for(int p=223;p<=290;p++)S[3].push_back(p);
  for(int p=296;p<=312;p++)S[4].push_back(p);
  int M=128;
  const vector<int> W={7,9,11,13,16,17,19,23,25,27,29,31,32,37,43};
  cout<<"m,d,prime,root,R0,DR0,pole,witness\n";
  for(int d:W){auto [prime_,w]=primitive(d);
    vector<Jet> xp(315);for(int p=0;p<=314;p++){int v=powmod(w,p%d);xp[p]={v,int(ll(p)*v%P)};}
    vector<Jet> A(M+1);
    for(int mask=1;mask<8;mask++){
      auto q=core(mask,M,xp);int sign=__builtin_popcount((unsigned)mask)%2;
      for(int m=1;m<=M;m++)A[m]=sign?add(A[m],q[m]):sub(A[m],q[m]);
    }
    auto B=single(3,M,xp),C=single(4,M,xp);
    int pole=0;for(int p=214;p<=314;p++)if(p%d==0)pole++;
    for(int m=1;m<=M;m++){
      if((m>=112&&m<=116)||(m>=124&&m<=128)||(d==16&&m>=60&&m<=64)){
        Jet R=sub(one,mul(mul(sub(one,A[m]),sub(one,B[m])),sub(one,C[m])));
        bool witness=pole>=3 && (R.f!=0||(pole>=4&&R.g!=0));
        cout<<m<<','<<d<<','<<prime_<<','<<w<<','<<R.f<<','<<R.g<<','<<pole<<','<<(witness?1:0)<<'\n';
      }
    }
    cerr<<"completed order "<<d<<"\n";
  }
}
