def fun1(msg):
    def fun2():
        print(msg)
    fun2()

fun1("Hello")
