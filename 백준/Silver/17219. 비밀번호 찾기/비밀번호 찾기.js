const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().split("\n");

const [N, M] = input[0].split(' ').map((el) => Number(el));
let pwDic = {};
const result = [];

for (let i = 1; i <= N; i++){
    const [addr, pw] = input[i].split(' ');
    pwDic[addr] = pw;
}

for (let i = N+1; i <= N+M; i++){
    result.push(pwDic[input[i]]);
}

console.log(result.join('\n'));