[![Build Status](https://travis-ci.org/geterodyn/setgame.svg?branch=master)](https://travis-ci.org/geterodyn/setgame)

# **Description**

This application checks 3 random cards with 4 items and replies if there is a set.

## Card items:
* NUMBER
* SYMBOL
* SHADING
* COLOR 

# **Table of functions:**

__Функция__ | __Описание__
--- | --- 
`game.check_set` | _проверяет доску_
`game.do_magic` | _делает магию_

# Code example

[Ссылка на гитхабе](https://github.com/geterodyn/setgame/blob/master/game/check_set.py)
```python
def check_set(cards):
	fields = ["number", "symbol", "shading", "color"]
	valid_len = (1,len(cards))
	return	all(
		len(set(field_list(cards,field))) in valid_len
		for field in fields
	)
```
