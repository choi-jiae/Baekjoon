const readline = require('readline');

const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout,
});

const solution = (n) =>{
    const ways = [1001].fill(0);
    ways[1] = 1;
    ways[2] = 3;
    
    for (i = 3; i <= n; i++){
        ways[i] = (ways[i-1]+(ways[i-2])*2)%10007;
    }
    console.log(ways[n]);
;}

let n = null;

rl.on('line', (line) => {
if (!n) {
    n = Number(line);
    rl.close();
}
}).on('close', ()=>{
    solution(n);
    process.exit();
});