// R762IK: exhaustive 2^20 integer DSU scan of support-triangle connectivity.
// Each T-support occupies at least two triangle sides in a reduced Euler witness.
// After deleting 2k critical bridges, the T triangle graph must have >=2k+1 components.
#include <bits/stdc++.h>
using namespace std;
int main(){vector<pair<int,int>> P; for(int a=0;a<6;a++)for(int b=a+1;b<6;b++)P.push_back({a,b});vector<array<int,3>> S;for(int a=0;a<6;a++)for(int b=a+1;b<6;b++)for(int c=b+1;c<6;c++){array<int,3> tri;int k=0;for(int j=0;j<15;j++)if((P[j].first==a&&P[j].second==b)||(P[j].first==a&&P[j].second==c)||(P[j].first==b&&P[j].second==c))tri[k++]=j;S.push_back(tri);}
int maxcc[21]{};int examples[21]{};long long counts[21][16]{};for(int mask=0;mask<(1<<20);mask++){int p[15];iota(p,p+15,0);auto root=[&](int a){while(p[a]!=a)a=p[a];return a;};int cc=15;for(int t=0;t<20;t++)if(mask>>t&1){auto x=S[t];for(int j=1;j<3;j++){int a=root(x[0]),b=root(x[j]);if(a!=b)p[a]=b,cc--;}}
 int n=__builtin_popcount((unsigned)mask);counts[n][cc]++;if(cc>maxcc[n])maxcc[n]=cc,examples[n]=mask;}
int expected[21]={15,13,11,10,10,8,7,7,6,6,6,4,3,3,2,2,2,1,1,1,1};
for(int n=0;n<=20;n++){if(maxcc[n]!=expected[n])throw runtime_error("unexpected component maximum");int mincc=15;for(int c=0;c<=15;c++)if(counts[n][c])mincc=min(mincc,c);cout<<"T="<<n<<" max_cc="<<maxcc[n]<<" min_cc="<<mincc<<" max_mask="<<examples[n]<<" cc_dist";for(int c=1;c<=15;c++)if(counts[n][c])cout<<" "<<c<<":"<<counts[n][c];cout<<"\n";}
// The bound for any k>=1 is max_{T: maxcc[T]>=2k+1}(40+2k+T)=55.
int global=0;
for(int k=1;k<=7;k++){
 int m=-1;
 for(int T=0;T<=20;T++)if(maxcc[T]>=2*k+1)m=max(m,40+2*k+T);
 if(m<0)throw runtime_error("no feasible k");
 cout<<"critical_k="<<k<<" upper="<<m<<"\n";
 global=max(global,m);
}
if(global!=55)throw runtime_error("critical upper bound mismatch");
cout<<"PASS R762IK COMPONENT SCAN: 1048576 masks; k>=1 upper=55\n";
}
