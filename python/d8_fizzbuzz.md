# FizzBuzz問題
- 2人以上のプレイヤーが1から順番に数字を言う
- 3で割り切れるときは「Fizz」と言う
- 5で割り切れるときは「Buzz」と言う
- 両方で割り切れるときは「FizzBuzz」と言う
– 間違えた人から脱落

# loop

``` python
for i in range(10):
    print(i)
```

``` bash
0
1
2
...
```

# Fizz : if-else =\> else:

``` python
for i in range(10):
    # print(i)
    if i % 3 == 0:
        print("Fizz")
    else
        print(i)
```

``` python
>python3 d8_FizzBuzz.py
  File "/Users/bob/Desktop/lecture_25s/comp_a_25s/python/orgs/nabeatsu/d8_FizzBuzz.py", line 5
    else
        ^
SyntaxError: expected ':'
```

``` python
for i in range(1, 10+1):
    # print(i)
    if i % 3 == 0:
        print("Fizz")
    else:
        print(i)
```

``` bash
Fizz
1
2
Fizz
...
```

#  Buzz : else if =\> elif

``` python
for i in range(10):
    #print(i)
    if i % 3 == 0:
        print("Fizz")
    else if i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

``` python
>python3 d8_FizzBuzz.py
  File "/Users/bob/Desktop/lecture_25s/comp_a_25s/python/orgs/nabeatsu/d8_FizzBuzz.py", line 5
    else if i % 5 == 0:
         ^^
SyntaxError: expected ':'
```

``` python
for i in range(10):
    #print(i)
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

``` zsh
Fizz
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
```

# Loop_2 : 正確に1..15

``` python
for i in range(1, 15+1):
    #print(i)
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

``` bash
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
Fizz
```

# FizzBuzz : ネストした（nested:入れ子の）if文

``` python
for i in range(1, 15+1):
    #print(i)
    if i % 3 == 0:
        if i % 5 == 0:
            print("FizzBuzz")
        else:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

``` python
> python3 d8_FizzBuzz.py
  File "/Users/bob/Desktop/lecture_25s/comp_a_25s/python/orgs/nabeatsu/d8_FizzBuzz.py", line 7
    print("Fizz")
    ^
IndentationError: expected an indented block after 'else' statement on line 6
```

``` python
for i in range(1, 15+1):
    #print(i)
    if i % 3 == 0:
        if i % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

``` python
> python3 d8_FizzBuzz.py
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```
