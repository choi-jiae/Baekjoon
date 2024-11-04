const solution = (data) => {
    const N = data[0][0]
    const K = data[0][1]
    let remain = K;
    let cnt = 0;
    let i = N;
    
    while (remain > 0){
        cnt += Math.floor(remain/data[i][0]);
        remain = remain%data[i][0];
        i--;
    }

    console.log(cnt);
}


const readline = require('readline');

(async () => {
    let rl = readline.createInterface({input:process.stdin});
    let data = [];

    for await (const line of rl){
        let data_len = data.length;
        if (data_len > 0 && data_len == data[0][0]){
            rl.close();
        }
        data.push(line.split(' ').map((el)=>Number(el)));
    }

    solution(data);
    process.exit();

})();