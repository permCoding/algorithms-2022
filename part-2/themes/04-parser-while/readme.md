### dequeue  

### Parsing

URL  
Uniform Resource Locator  
Унифицированный указатель ресурса  
способ кодирования адресов электронных ресурсов  

URL был изобретён Тимом Бернерсом-Ли в 1990 году в стенах Европейского совета по ядерным исследованиям (фр. Conseil Européen pour la Recherche Nucléaire, CERN) в Женеве, Швейцария.  
URL стал фундаментальной инновацией в Интернете и предназначался для обозначения мест расположения файлов во Всемирной паутине. Сейчас URL применяется для обозначения адресов почти всех ресурсов Интернета.  

[Стандарт URL](https://www.rfc-editor.org/rfc/rfc3986)  

---  

браузер - Edit as HTML  
document.designMode = "on"  
User-Agent  

---  

https://pcoding.ru/darkNet.php  
https://www.championat.com/hockey/_superleague/tournament/5077/table/#all  
https://pgsha.ru/today/  
https://n-katalog.ru/category/monitory/list?sort=PriceAsc  
https://n-katalog.ru/category/noutbuki/list?sort=PriceAsc  

<td class="_center results-table__main ojhxqo">

---  

### LABRAB 03  

**task01**  

Дан адрес странички: https://pcoding.ru/darkNet.php  
Спарсить оттуда гиперссылки на pdf-документы и названия этих документов.  
Вывести полученные данные в виде таблицы в csv-файл в таком формате:  
```
id;href;name
1;...;...  
2;...;...  
```

**task02**

Разработать функцию, которая ищет с текущей позиции в документе  
ближайший следующий тег гиперссылки  
и возвращает кортеж из  
(позиция после окончания тега, гиперссылка, текст названия)  

**task03**  

Со странички https://pgsha.ru/today/  
Спарсить список новостей (первые 10)  
Сохранить их в json-файл - news.json  
Формат для сохранения:  
```json
[
	{
		"data": "тут будет дата новости",
		"href": "тут будет ссылка на страницу новости",
		"title": "тут будет заголовок новости",
		"text": "тут будет текст новости"
	},
	...
]
```
Использовать import json  

---  
