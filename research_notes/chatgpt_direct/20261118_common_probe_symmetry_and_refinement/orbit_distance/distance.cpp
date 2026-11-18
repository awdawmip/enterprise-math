// Maximize retained histories by integer bipartite assignment, for every affine image.
#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
using Matrix=array<array<int,15>,15>;

int assignment(const Matrix& w, int n){
    array<int,16> u{},v{},owner{},prev{};
    for(int i=1;i<=n;++i){
        owner[0]=i;
        int j=0;
        array<int,16> slack;slack.fill(100000);
        array<bool,16> used{};
        do{
            used[j]=true;
            int row=owner[j],next=0,delta=100000;
            for(int k=1;k<=n;++k)if(!used[k]){
                int cost=125-w[row-1][k-1]-u[row]-v[k];
                if(cost<slack[k]){slack[k]=cost;prev[k]=j;}
                if(slack[k]<delta){delta=slack[k];next=k;}
            }
            for(int k=0;k<=n;++k){
                if(used[k]){u[owner[k]]+=delta;v[k]-=delta;}
                else slack[k]-=delta;
            }
            j=next;
        }while(owner[j]);
        do{
            int prev_col=prev[j];owner[j]=owner[prev_col];j=prev_col;
        }while(j);
    }
    int retained=0;
    for(int j=1;j<=n;j++)retained+=w[owner[j]-1][j-1];
    // The equal primal and dual objective values verify optimality.
    int dual=accumulate(u.begin()+1,u.begin()+n+1,0)+accumulate(v.begin()+1,v.begin()+n+1,0);
    if(125*n-retained!=dual)throw logic_error("dual objective");
    for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(u[i+1]+v[j+1]>125-w[i][j])throw logic_error("infeasible dual");
    return retained;
}
int main(int argc,char**argv){
    ifstream maps(argv[1],ios::binary);
    int m,n;cin>>m>>n;
    array<int,125>a{},b{};array<int,15> sa{},sb{};
    for(auto&j:a){cin>>j;++sa[j];}
    for(auto&j:b){cin>>j;++sb[j];}
    array<unsigned char,125> g;
    int id=0;
    while(maps.read(reinterpret_cast<char*>(g.data()),g.size())){
        Matrix w{};
        for(int x=0;x<125;++x)++w[a[g[x]]][b[x]];
        int shared=0;
        for(int i=0;i<m;++i)for(int j=0;j<n;++j)if(w[i][j]==sa[i] && w[i][j]==sb[j])++shared;
        cout<<id++<<" "<<shared<<" "<<assignment(w,n)<<"\n";
    }
}
