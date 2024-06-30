function solution(num_list) {
    var odd = ''
    var even = ''
    for (i = 0; i < num_list.length; i++){
        var num = num_list[i]
        if (num % 2 == 0){
            even += String(num)
        } else {
            odd += String(num)
        }
    }
    var answer = Number(odd) + Number(even);
    return answer;
}