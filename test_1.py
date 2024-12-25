def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
test_function()
#inner_function()   - закоментил,т.к. выдавало ошибку при попытке вызова функции
#а ошибку выдавало, т.к. функция inner_function является внутренней для функции test_function
