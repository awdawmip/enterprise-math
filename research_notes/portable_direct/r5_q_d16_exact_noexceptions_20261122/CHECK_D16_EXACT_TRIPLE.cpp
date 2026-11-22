// Exact Z[q]/Phi_16(q) (=Z[q]/(q^8+1)) verification for 5-event frozen R5 core.
// Joint event supports remain uncollapsed; direct signed 7-subset IE enumerates the three overlapping events.
#include <bits/stdc++.h>
using namespace std;
using I=long long;
using Poly=array<I,8>;
const vector<vector<int>> E={{214,215,216,217,218},{214,216,217,218,219,220,221},{215,216,217,218,219,220,221}};
Poly shift(Poly const& a,int p,int sgn=1){Poly b{};p%=16;for(int j=0;j<8;j++){int z=(j+p)%16, sign=z>=8?-sgn:sgn;b[z%8]+=sign*a[j];}return b;}
Poly mulfactor(Poly const&v,int p){Poly a=shift(v,p);for(int j=0;j<8;j++)a[j]=v[j]-a[j];return a;}
Poly multiply(Poly const&a,Poly const&b){Poly out{};for(int i=0;i<8;i++)for(int j=0;j<8;j++){int z=i+j;out[z%8]+=(z>=8?-1:1)*a[i]*b[j];}return out;}
void add_to(Poly&x,Poly const&y,int sign=1){for(int i=0;i<8;i++)x[i]+=sign*y[i];}
int main(){int M=96;vector<Poly> A(M+1);
 for(int mask=1;mask<8;mask++){
  vector<int> ids,U;for(int i=0;i<3;i++)if(mask>>i&1)ids.push_back(i);
  for(int i:ids)for(int p:E[i])U.push_back(p);
  sort(U.begin(),U.end());U.erase(unique(U.begin(),U.end()),U.end());
  int n=ids.size(),total=1;for(int j=0;j<n;j++)total*=M;
  vector<int> movement(U.size()),belong(U.size());
  for(size_t t=0;t<U.size();t++)for(int j=0,place=1;j<n;j++,place*=M){
   if(find(E[ids[j]].begin(),E[ids[j]].end(),U[t])!=E[ids[j]].end()){movement[t]+=place;belong[t]|=1<<j;}
  }
  vector<Poly> dp(total);dp[0][0]=1;
  for(size_t t=0;t<U.size();t++)for(int code=0;code<total;code++){
   int tmp=code;bool valid=true;for(int j=0;j<n;j++,tmp/=M)if((belong[t]>>j&1)&&tmp%M==0){valid=false;break;}
   if(valid){auto z=shift(dp[code-movement[t]],U[t]);add_to(dp[code],z);}
  }
  vector<Poly> layer(M);
  for(int code=0;code<total;code++){
   int x=code,maximum=0;for(int j=0;j<n;j++,x/=M)maximum=max(maximum,x%M);
   add_to(layer[maximum],dp[code]);
  }
  Poly prefix{};
  int sign=__builtin_popcount((unsigned)mask)%2?1:-1;
  for(int m=1;m<=M;m++){
   add_to(prefix,layer[m-1]);Poly z=prefix;
   for(int p:U)z=mulfactor(z,p);
   add_to(A[m],z,sign);
  }
 }
 cout<<"r,A_r_coefficients,A_(r+32)_coefficients,exact_double,equality,nonzero\n";
 int failures=0;
 for(int r=28;r<=32;r++){
  cout<<r<<',';for(int j=0;j<8;j++)cout<<(j?";":"")<<A[r][j];cout<<',';
  for(int j=0;j<8;j++)cout<<(j?";":"")<<A[r+32][j];cout<<',';
  bool eq=true,nonzero=false;
  for(int j=0;j<8;j++){if(A[r+32][j]!=2*A[r][j]||A[r+64][j]!=3*A[r][j])eq=false;if(A[r][j])nonzero=true;}
  cout<<2<<','<<(eq?1:0)<<','<<(nonzero?1:0)<<'\n';
  if(!eq||!nonzero)failures++;
 }
 cerr<<"CHECK_D16_EXACT failures="<<failures<<'\n';
 return failures?1:0;
}
