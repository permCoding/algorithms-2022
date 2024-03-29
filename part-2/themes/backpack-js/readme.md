# Задачи на оптимизацию  

## Задача о заполнении рюкзака  

### Методы решения  

01 - Жадный алгоритм  
02 - Бинарные маски  
03 - Рекурсивный перебор  
04 - Метод ветвей и границ  
05 - Динамическое программирование  

Доделать на лабораторке:  

1) метод ветвей и границ  
2) динамику (восстановление комбинации по таблице)  

---  

```txt
Для разных файлов - ограничения по массе и оптимальные решения:  
input4  max_w = 100 => max_p = 150
input6  max_w = 1500 => max_p = 265
input20  max_w = 100 => max_p = 350
input25  max_w = 150 => max_p = 455
input30  max_w = 150 => max_p = 500
Например, для input6 
- ограничение на вместимость рюкзака 1500 кг  
- оптимальное решение: { w = 1412, p = 265 }
```

Само найденное оптимально решение можно выводить как комбинацию взятых предметов, например:  

```js
[
    { i: 1, w: 200, p: 40 },
    { i: 2, w: 314, p: 50 },
    { i: 4, w: 198, p: 100 },
    { i: 5, w: 300, p: 30 },
    { i: 8, w: 400, p: 45 },
]
```

---  

Сколько шагов в алгоритме:  

```txt
branches algorithm
> input30.json
> max_w = 150

- без ветвей и границ
> steps = 2147483647
> 500

- с методом ветвей и границ
> steps = 403034
> 500

- динамикой
> steps = 4500
```

Выводы про разные методы:

```txt
1) метод ветвей и границ даёт заметную выгоду для кол-ва предметов больше 20

2) пример для 30 предметов:
- бинарные маски: 1 трлн шагов
- рекурсия: 2 млрд шагов
- ветвей и границ: 400 тыс шагов
- динамика: 4,5 тыс шагов (только для целых значений)
- жадный: 30 шагов (реш приблизительное)

3) метод ветвей и границ подходит и для вещ значений  
   а динамика только для целых

4) жадный даёт приблизительное решение 
   но на 30-ти предметах расхождение от оптимального  
   всего 1%
```

---  
