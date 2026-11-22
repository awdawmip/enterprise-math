// R5: exact primitive-29/32 root phase certificates in characteristic zero.
// g++ -O2 -std=c++17 VERIFY_PHASES.cpp -o verify_phases && ./verify_phases
#include <array>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
using i64=long long;
using i128=__int128_t;
template<class T> using Poly=array<T,32>;
const vector<vector<int>> E={{214,215,216,217,218},
 {214,216,217,218,219,220,221}, {215,216,217,218,219,220,221}};
int d,b;
template<class T> void shiftadd(Poly<T>& a,const Poly<T>& v,int p,int sign=1){
 for(int j=0;j<b;j++){
  int k=(j+p%d)%d;
  if(d==32&&k>=16)a[k-16]-=sign*v[j];else a[k]+=sign*v[j];
 }
}
Poly<i128> factors(Poly<i128> v,const vector<int>& prices){
 for(int p:prices){auto next=v;shiftadd(next,v,p,-1);v=next;}
 return v;
}
Poly<i128> multiply(const Poly<i128>&a,const Poly<i128>&c){
 Poly<i128> result{};
 for(int i=0;i<b;i++)for(int j=0;j<b;j++){
  int k=(i+j)%d;
  if(d==32&&k>=16)result[k-16]-=a[i]*c[j];
  else result[k]+=a[i]*c[j];
 }
 return result;
}
bool zero(const Poly<i128>&v){
 for(int i=0;i<b;i++)if(v[i]!=(d==29?v[0]:0))return false;
 return true;
}
void run(int order){
 d=order;b=(d==29?29:16);int M=2*d;
 vector<Poly<i128>> A(M+1);
 for(int mask=1;mask<8;mask++){
  vector<int> ids,U;
  for(int j=0;j<3;j++)if(mask>>j&1)ids.push_back(j);
  for(int j:ids)for(int p:E[j])U.push_back(p);
  sort(U.begin(),U.end());U.erase(unique(U.begin(),U.end()),U.end());
  int n=ids.size(),total=1;for(int j=0;j<n;j++)total*=M;
  vector<int> move(U.size()),belong(U.size());
  for(size_t z=0;z<U.size();z++){
   int place=1;
   for(int i=0;i<n;i++,place*=M)
    if(find(E[ids[i]].begin(),E[ids[i]].end(),U[z])!=E[ids[i]].end()){
     move[z]+=place;belong[z]|=1<<i;
    }
  }
  vector<Poly<i64>> dp(total);dp[0][0]=1;
  for(size_t z=0;z<U.size();z++)for(int code=0;code<total;code++){
   int tmp=code;bool valid=true;
   for(int i=0;i<n;i++){
    if((belong[z]>>i&1)&&tmp%M==0){valid=false;break;}
    tmp/=M;
   }
   if(valid)shiftadd(dp[code],dp[code-move[z]],U[z]);
  }
  vector<Poly<i128>> layer(M);
  for(int code=0;code<total;code++){
   int tmp=code,mx=0;
   for(int i=0;i<n;i++){mx=max(mx,tmp%M);tmp/=M;}
   for(int k=0;k<b;k++)layer[mx][k]+=dp[code][k];
  }
  Poly<i128> prefix{};
  int sign=__builtin_popcount((unsigned)mask)%2?1:-1;
  for(int m=1;m<=M;m++){
   for(int k=0;k<b;k++)prefix[k]+=layer[m-1][k];
   auto q=factors(prefix,U);
   for(int k=0;k<b;k++)A[m][k]+=sign*q[k];
  }
 }
 vector<int> S4;for(int p=296;p<=312;p++)S4.push_back(p);
 vector<Poly<i128>> h(M);h[0][0]=1;
 for(int p:S4)for(int r=1;r<M;r++)shiftadd(h[r],h[r-1],p);
 Poly<i128> prefix{};
 cout<<"order="<<d<<" zero phases:";
 for(int m=1;m<=M;m++){
  for(int k=0;k<b;k++)prefix[k]+=h[m-1][k];
  auto C=factors(prefix,S4),AC=multiply(A[m],C);
  Poly<i128> R{};
  for(int k=0;k<b;k++)R[k]=A[m][k]+C[k]-AC[k];
  if(zero(R))cout<<' '<<m;
 }
 cout<<'\n';
}
int main(){run(29);run(32);}
