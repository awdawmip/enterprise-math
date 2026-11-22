#include <bits/stdc++.h>
using namespace std;using I=long long;constexpr int D=37;using P=array<I,D>;
struct J{P v{},d{};};
const vector<vector<int>> E={{214,215,216,217,218},{214,216,217,218,219,220,221},{215,216,217,218,219,220,221}};
P shift(const P&a,int p){P b{};p%=D;for(int j=0;j<D;j++)b[(j+p)%D]+=a[j];return b;}
void add(P&a,const P&b,int s=1){for(int j=0;j<D;j++)a[j]+=s*b[j];}
void add(J&a,const J&b,int s=1){add(a.v,b.v,s);add(a.d,b.d,s);}
J shifted(const J&a,int p){J b;b.v=shift(a.v,p);b.d=shift(a.d,p);for(int j=0;j<D;j++)b.d[j]+=(I)p*b.v[j];return b;}
void factor(J&a,int p){J b=shifted(a,p);add(a,b,-1);}
vector<I> canon(const P&a){vector<I>b(D-1);for(int j=0;j<D-1;j++)b[j]=a[j]-a[D-1];return b;}
bool zero(const P&a){auto b=canon(a);return all_of(b.begin(),b.end(),[](I x){return x==0;});}
int main(){int M=148;vector<J>A(M+1);
for(int mask=1;mask<8;mask++){
 vector<int>ids,U;for(int i=0;i<3;i++)if(mask>>i&1)ids.push_back(i);
 for(int id:ids)for(int p:E[id])U.push_back(p);
 sort(U.begin(),U.end());U.erase(unique(U.begin(),U.end()),U.end());
 int n=ids.size(),total=1;for(int j=0;j<n;j++)total*=M;
 vector<int>mv(U.size()),belongs(U.size());
 for(size_t t=0;t<U.size();t++)for(int j=0,place=1;j<n;j++,place*=M){if(find(E[ids[j]].begin(),E[ids[j]].end(),U[t])!=E[ids[j]].end()){mv[t]+=place;belongs[t]|=1<<j;}}
 vector<J>dp(total);dp[0].v[0]=1;
 for(size_t t=0;t<U.size();t++)for(int code=0;code<total;code++){
  int tmp=code;bool valid=true;for(int j=0;j<n;j++,tmp/=M)if((belongs[t]>>j&1)&&tmp%M==0){valid=false;break;}
  if(valid)add(dp[code],shifted(dp[code-mv[t]],U[t]));
 }
 vector<J>layer(M);for(int code=0;code<total;code++){
 int tmp=code,k=0;for(int j=0;j<n;j++,tmp/=M)k=max(k,tmp%M);add(layer[k],dp[code]);}
 J prefix{};int s=__builtin_popcount((unsigned)mask)%2?1:-1;
 for(int m=1;m<=M;m++){add(prefix,layer[m-1]);J z=prefix;for(int p:U)factor(z,p);add(A[m],z,s);}cerr<<"mask="<<mask<<" complete\n";
}
int none=0, safeSign=0, safeRank=0, safeInteger=0, exceptional=0;
cout<<"r,type,coord,base,step\n";
for(int r=1;r<=74;r++){
 P b=A[r].v,step=A[r+74].v;add(step,b,-1);
 if(zero(b)&&zero(step)){none++;cout<<r<<",identically_zero,-1,0,0\n";continue;}
 auto bs=canon(b),ds=canon(step);int j=-1;
 for(int i=0;i<D-1;i++)if((bs[i]>0&&ds[i]>=0)||(bs[i]<0&&ds[i]<=0)){j=i;break;}
 if(j>=0){safeSign++;cout<<r<<",signed_nonzero,"<<j<<","<<bs[j]<<","<<ds[j]<<"\n";continue;}
 bool rank=false;for(int i=0;i<D-1&&!rank;i++)for(int k=i+1;k<D-1;k++)if((__int128)bs[i]*ds[k]!=(__int128)bs[k]*ds[i]){rank=true;break;}
 if(rank){safeRank++;cout<<r<<",rank_two,-1,0,0\n";continue;}
 int i=-1;for(int k=0;k<D-1;k++)if(ds[k]){i=k;break;}
 if(i==-1){if(zero(b)){exceptional++;cout<<r<<",unexpected,-1,0,0\n";}else{safeInteger++;cout<<r<<",constant,-1,0,0\n";}continue;}
 // common zero requires integer h with h = -bs[i]/ds[i].
 if(bs[i] * ds[i]<0 && -bs[i]%ds[i]==0){long long h=-bs[i]/ds[i];if(h>=0){exceptional++;cout<<r<<",possible_exact_root,"<<i<<","<<bs[i]<<","<<ds[i]<<"\n";continue;}}
 safeInteger++;cout<<r<<",no_nonnegative_integral_root,"<<i<<","<<bs[i]<<","<<ds[i]<<"\n";
}
cerr<<"order37: 74 phases, sign="<<safeSign<<" rank="<<safeRank<<" integrality="<<safeInteger<<" zero_affine="<<none<<" candidate="<<exceptional<<"\n";
}
