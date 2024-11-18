const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const solution = (n) => {
    const result = Array(50001).fill(0);
    let k =1;
    while (k**2 <=n){
        result[k**2] = 1;
        k++;
    }

    for (let i = 2; i<=n; i++){
        if (result[i] == 0){
            let j = 1;
            while (j**2 < i){
                // 처음 저장할 때
                if (result[i] == 0){
                    result[i] = result[j**2]+result[i-j**2];
                } else {
                    result[i] = Math.min(result[i], result[j**2]+result[i-j**2]);
                }
                j++;
            }
        }
    }

    console.log(result[n]);
}

let n = null;

rl.on('line', (line) => {
    n = Number(line);
    rl.close();
}).on('close', () => {
    solution(n);
    process.exit();
})