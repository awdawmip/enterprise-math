// Exhaustive local Hamming repair proof. C++17 compiler; three parameters: triples, code, radius.
#include <cstdio>
#include <algorithm>
#include <vector>
#include <array>
#include <cstdlib>
using namespace std;using M=__uint128_t;using vec=vector<int>; int old[125],cols[125],lim,basecolors[20],basebudget=0;long long countn;
array<vec,11> cls; vector<array<int,3>> ed[125]; int pairbad[125][125][125];bool done;
void run(int cost, M fixed){
 if(done)return; ++countn;
 int B[3],minv=777777;bool fail=false;int assign[6];vec tr; int basebudget=0; M involved=0;
 for(int k=0;k<11;k++){auto&r=cls[k];for(int i=0;i<r.size();i++)for(int j=0;j<i;j++)for(int h=0;h<j;h++)if(pairbad[r[i]][r[j]][r[h]]){
 int W[3]={r[i],r[j],r[h]};int av=0;M g=0;for(int w:W)if(!(fixed>>w&1)){av++;g|=M(1)<<w;}
 if(!av)return;
 fail=true;if(!(involved&g)){involved|=g;if(++basebudget+cost>lim){basebudget=0;return;}}
 int sc=av*100+((W[0]*3+W[1]*7+W[2]*11+13*cost)%100);if(sc<minv){minv=sc;for(int q=0;q<3;q++)B[q]=W[q];}
 }}
 basebudget=0;
 if(!fail){for(int c:cols)printf("%d ",c);puts("");fflush(stdout);done=true;return;}
 if(cost>=lim)return;
 // Partition by first changed point among this forbidden triplet. Already changed (fixed) vertices may not be changed again.
 for(int q=0;q<3&&!done;q++){
 int x=B[q];if(fixed>>x&1)continue;int oc=cols[x];auto&rr=cls[oc];rr.erase(find(rr.begin(),rr.end(),x));fixed|=M(1)<<x;
 vector<pair<int,int>> order;for(int k=0;k<11;k++)if(k!=oc){
 int viol=0;for(int t=0;t<cls[k].size();t++)for(int j=0;j<t;j++)if(pairbad[x][cls[k][t]][cls[k][j]]){
    if((fixed>>cls[k][t]&1)&&(fixed>>cls[k][j]&1)){viol=999;break;}viol++;}
 if(viol<999)order.push_back({viol,k});}
 sort(order.begin(),order.end());
 for(auto [v,k]:order){cols[x]=k;cls[k].push_back(x);run(cost+1,fixed);if(done)return;cls[k].erase(find(cls[k].begin(),cls[k].end(),x));}
 auto xy=find(rr.begin(),rr.end(),x);if(xy!=rr.end())abort();rr.push_back(x);cols[x]=oc;
 }}
int main(int n,char**argv){FILE*f=fopen(argv[1],"r");int x,y,z;while(fscanf(f,"%d%d%d",&x,&y,&z)==3){int p[]={x,y,z};sort(p,p+3);do{pairbad[p[0]][p[1]][p[2]]=1;}while(next_permutation(p,p+3));}fclose(f);
 f=fopen(argv[2],"r");for(int i=0;i<125;i++){fscanf(f,"%d",&cols[i]);cls[cols[i]].push_back(i);}fclose(f);
 lim=atoi(argv[3]);countn=0;run(0,0);printf("%d %lld %d\n",lim,countn,done);
}
