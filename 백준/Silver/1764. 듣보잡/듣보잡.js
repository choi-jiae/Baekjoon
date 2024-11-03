const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const lines = [];

rl.on('line', (line) => {
    lines.push(line.split(' '))

    if (lines.length > 0 && lines.length === Number(lines[0][0]) + Number(lines[0][1]) + 1){
        rl.close();
    }
}).on('close', () => {
    const N = Number(lines[0][0]);
    const M = Number(lines[0][1]);
    const heared = [];
    const seen = new Set();

    for (let i = 0; i < N; i++){
        heared.push(lines[i + 1][0]);
    }

    for (let i = 0; i < M; i++){
        seen.add(lines[i + N + 1][0]);
    }

    const hearedAndSeen = heared.filter((e) => seen.has(e)).sort();
    console.log(hearedAndSeen.length);
    console.log(hearedAndSeen.join('\n'));
    process.exit();
});