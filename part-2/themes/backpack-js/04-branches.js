// branches algorithm

const get_branches = (max_w, arr) => {
    const get_combo = (combo, deep) => {

        cur_w = combo.reduce((acc, cur) => acc+cur.w, 0)
        if (cur_w > max_w) return

        // тут требуется добавить проверку на рейтинг этой ветви
        // чтобы ускорить алгоритм по методу ветвей и границ

        if (deep === arr.length) {
            cur_p = combo.reduce((acc, cur) => acc+cur.p, 0)
            if ((cur_w<=max_w) && (cur_p>=max_p)) {
                max_p = cur_p
            }
        }
        else {
            combo.push(arr[deep])
            get_combo(combo, deep+1)
            combo.pop()
            get_combo(combo, deep+1)
        }
    }

    let max_p = 0
    get_combo([], 0)
    return max_p
}


let prods = require('./json/input25.json')
let max_w = 150

prods.map(obj => { obj.id=+obj.id, obj.w=+obj.w, obj.p=+obj.p })

// prods.sort((a,b) => a.p/a.w>b.p/b.w? -1: +1)
// доработать самостоятельно - 2
// если убрать эту сортировку, то перестанет работать
// нужно добавить условие в методе get_branches
// когда для v1 и v2 ценность одинаковая, то выбрать
// меньшую по весу

console.clear()
prods.forEach(obj => console.log(obj))
prods.push
console.log('branches algorithm')

let solver = get_branches(max_w, prods)

console.log(solver)
