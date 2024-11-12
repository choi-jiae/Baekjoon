const readline = require('readline');

const solution = (N, pair, edges) => {
    const virus = [1];
    const counted = [];
    
    while (virus.length > 0){
        now_pc = virus.pop();
        counted.push(now_pc);

        for (let e of edges){
            if (e[0]==now_pc && !counted.includes(e[1]) && !virus.includes(e[1])){
                virus.push(e[1]);
            };
            if (e[1]==now_pc && !counted.includes(e[0]) && !virus.includes(e[0])){
                virus.push(e[0]);
            };
        }
    }

    console.log(counted.length-1);
    
};

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let N = null;
let pair = null;
const edges = [];

rl.on('line', (line)=>{
    if (!N){
        N = Number(line);
    } else if (!pair){
        pair = Number(line);
    } else {
        edges.push(line.split(' ').map((el)=>Number(el)));
        if (edges.length == pair) {
            rl.close();
        }
    }

}).on('close', () => {
    solution(N, pair, edges);
    process.exit();
})