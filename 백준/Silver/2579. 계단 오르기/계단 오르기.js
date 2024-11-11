const readline = require('readline');

const solution = (N, stairs) => {
    let d = new Array(301).fill(0);

    for (let i = 1; i <= N; i++){
        if (i == 1){
            d[i] = stairs[i];
        } else if (i == 2){
            d[i] = stairs[i-1]+stairs[i];
        } else if (i == 3){
            d[i] = Math.max(stairs[i-1]+stairs[i], stairs[i-2]+stairs[i]);
        } else {
            d[i] = Math.max(d[i-3]+stairs[i-1]+stairs[i], d[i-2]+stairs[i]);
        }
    }

    console.log(d[N]);
    
};

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let N = null;
const stairs = [0];

rl.on('line', (line)=>{
    if (!N){
        N = Number(line);
    } else {
        stairs.push(Number(line));
        if (stairs.length == N+1) {
            rl.close();
        }
    }

}).on('close', () => {
    solution(N, stairs);
    process.exit();
})