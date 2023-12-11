ДЗ 1, задачи 1-3

# Задача 1
Комманды для проверки первой задачи:
```
cd 1
python3 main.py test &>py_test
nl test &> nl_test
diff nl_test py_test --brief
```
Ожидается отсутствие вывода

# Задача 2
Комманды для проверки первой задачи:
```
cd 2
python3 main.py test &>py_test
tail test &> tail_test
diff tail_test py_test --brief
python3 main.py test main.py &>py_test
tail test main.py &> tail_test
diff tail_test py_test --brief
```
Ожидается отсутствие вывода

# Задача 3
Комманды для проверки первой задачи:
```
cd 3
python3 main.py test &>py_test
wc test &> wc_test
diff wc_test py_test --brief

wc test test test main.py main.py фывфывфыв main.py &>wc_test
python3 main.py test test test main.py main.py фывфывфыв main.py &>py_test
diff wc_test py_test --brief
```
Ожидается отсутствие вывода