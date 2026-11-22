// Exact C++17 characteristic-zero audit of frozen R5 E0,E1,E2 at order 31.
// The correct E4 finite-sum Euler jet is computed separately, not by product(1-q^(m*p)).
// Reproduce: g++ -O2 -std=c++17 -fsanitize=undefined -fno-sanitize-recover=all VERIFY_D31_EXACT_THREE.cpp -o check && ./check
#include <bits/stdc++.h>
using namespace std;
using I=int64_t;constexpr int D=31,M=183;
using P=array<I,D>;
vector<vector<int>> E={{214,215,216,217,218},{214,216,217,218,219,220,221},{215,216,217,218,219,220,221}};
inline void add(P &a,const P &b,int s=1){for(int j=0;j<D;j++)a[j]+=s*b[j];}
P shifted(const P&a,int p){P b{};p%=D;for(int j=0;j<D;j++)b[(j+p)%D]=a[j];return b;}
void factor(P &a,int p){auto b=shifted(a,p);for(int i=0;i<D;i++)a[i]-=b[i];}
P multiply(const P&a,const P&b){P z{};for(int i=0;i<D;i++)if(a[i])for(int j=0;j<D;j++)if(b[j])z[(i+j)%D]+=a[i]*b[j];return z;}
int main(){
 array<int,3> ms={59,121,183};array<P,3> DA{};
 for(int mask=1;mask<8;mask++){
  vector<int> ids,U;for(int i=0;i<3;i++)if(mask>>i&1)ids.push_back(i);
  for(int id:ids)for(int p:E[id])U.push_back(p);
  sort(U.begin(),U.end());U.erase(unique(U.begin(),U.end()),U.end());
  int n=ids.size(),total=1;for(int j=0;j<n;j++)total*=M;
  vector<int> mv(U.size()),bel(U.size());
  for(size_t t=0;t<U.size();t++)for(int j=0,place=1;j<n;j++,place*=M)
    if(find(E[ids[j]].begin(),E[ids[j]].end(),U[t])!=E[ids[j]].end()){
      mv[t]+=place;bel[t]|=1<<j;
    }
  vector<P> dp(total);dp[0][0]=1;
  for(size_t t=0;t<U.size();t++)
    for(int code=0;code<total;code++){
      int tmp=code;bool ok=true;for(int j=0;j<n;j++,tmp/=M)
        if((bel[t]>>j&1)&&tmp%M==0){ok=false;break;}
      if(ok){P &dest=dp[code];const P &src=dp[code-mv[t]];int p=U[t]%D;
        for(int x=0;x<D;x++)dest[(x+p)%D]+=src[x];}
    }
  array<P,3> Q{};
  for(int code=0;code<total;code++){
    int tmp=code,k=0;for(int j=0;j<n;j++,tmp/=M)k=max(k,tmp%M);
    for(int j=0;j<3;j++)if(k<ms[j])add(Q[j],dp[code]);
  }
  P dD{};dD[0]=-217;
  assert(find(U.begin(),U.end(),217)!=U.end());
  for(int p:U)if(p!=217)factor(dD,p);
  int sign=__builtin_popcount(unsigned(mask))%2?1:-1;
  for(int j=0;j<3;j++){P z=multiply(Q[j],dD);add(DA[j],z,sign);}
  cerr<<"finished mask "<<mask<<" total "<<total<<"\n";
 }
 cout<<"d31 exact DA at three thresholds, canonical coordinates\n";
 for(int j=0;j<3;j++){
  cout<<"m="<<ms[j]<<" DA=";
  for(int i=0;i<30;i++)cout<<(i?",":"")<<DA[j][i]-DA[j][30];
  cout<<"\n";
 }
}
