// 오름차순으로 정렬한 다음 차례대로 묶어서 계산
// 짧은 시간이 많이 반복되도록
const solution = (N, data) => {

    data.sort((a, b) => a - b);
    let result = 0;

    for (let i = 0; i < N; i++){
        result += data[i]*(N-i);
    };

    console.log(result);
};

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
let N = null; 
const data = [];
rl.on('line', (line) => {

    if (!N){
        N = Number(line);
    } else {
        data.push(line.split(' ').map((el) => Number(el)));
    };

    if (data.length > 0){
        rl.close();
    };
    

}).on('close', () => {
    solution(N, data[0]);
    process.exit();
});