
# コードの雛形

## ipython

-   python3
-   1+1
-   quit

## VSCode

-   cd my_comp_a
-   code .
-   新規ファイルの作成
-   d1_hello.py
-   編集
-   wslでpython d1_hello.py
    -   python3 d1_hello.py

## 課題

以下の課題をおこない，memoとしてd1_python_1.mdとして保存してLUNAへ提出．

### python print

最初の一歩としてprintでの出力．

``` python
print("Hello world.")
```

``` {.bash org-language="sh"}
> python3 d1_hello.py
Hello world.
```

md構文でcodeに色をつけるには， バックコート\'\`\'
(back-quote)(shift-@)でコードを囲んで， pythonとかを後ろに指定すると，
その文法に沿って色付け(colorize)してくれる．

### calendar

-   新しいファイルを作成
    -   d1_calendar.py
        -   importするmoduleと同じ名前だと，
        -   ライブラリ moduleではなく
        -   自ファイルを読もうとして，
        -   動かない


``` python
    import calendar
    print(calendar.month(1961,3)) # your month
```

``` bash
> python3 d1_calendar.py 
     March 1961
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31
```

### 誕生秘話

Bobは，分娩室の外のソファで生まれました．
