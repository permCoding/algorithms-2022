let create_heap = (arr) => {
    let heap = []
    for (let item of arr) {
        heap.push(item)
        let pos = heap.length - 1
        while (pos > 0) {
            let pos_par = Math.floor(pos - 1) / 2
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


const sort_heap = (arr) => {
    let heap = create_heap(arr)
    return heap
    // return remove_all(heap)
}


console.clear()

// let arr = [3,4,2,5,1,0]
let arr = Array(1000000)
    .fill(0)
    .map(x => Math.floor(1000*Math.random()))
console.log(arr.slice(0,10))
console.time("heap")
let s_arr = sort_heap(arr)
console.timeEnd("heap")
console.log(s_arr.slice(0,10))
