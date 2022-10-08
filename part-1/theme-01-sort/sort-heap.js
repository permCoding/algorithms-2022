let create_heap = (arr) => {
    let heap = []
    for (let item of arr) {
        heap.push(item)
        let pos = heap.length - 1
        while (pos > 0) {
            let pos_par = Math.floor((pos - 1) / 2)
            if (heap[pos_par] < heap[pos]) {
                [heap[pos_par],heap[pos]] = [heap[pos],heap[pos_par]]
            }
            else {
                break
            }
            pos = pos_par
        }
    }
    return heap
}

let remove_all = (heap) => {
    for (let n = heap.length - 1; n > 0; n--) { // n поз текущ максимума
        [heap[0], heap[n]] = [heap[n], heap[0]]

        // остаётся дерево без позиции n
        // на позиции 0 находится неправ элемент
        // его нужно опускать по дереву
        // пока не восстановится максимальное
        // бинарное дерево
        // тут впишите код опускания одного элемента
    }
    return heap
}

const sort_heap = (arr) => {
    let heap = create_heap(arr)
    console.log(heap.slice(0,12))
    return remove_all(heap)
}


console.clear()

// let arr = [1,0,3,4,2,5,1,0,0,0,9]
let arr = Array(1000000)
    .fill(0)
    .map(_ => Math.floor(1000*Math.random()))
console.log(arr.slice(0,12))
console.time("heap")
let s_arr = sort_heap(arr)
console.timeEnd("heap")
console.log(s_arr.slice(0,12))
