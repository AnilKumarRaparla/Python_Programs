class MyClass:
    def my_method(self, *args, **kwargs):
        if len(args) == 1:
            arg1 = args[0]
            print(arg1)
        elif len(args) == 2:
            arg1, arg2 = args
            print(arg1, arg2)
        elif 'arg1' in kwargs and 'arg2' in kwargs:
            arg1 = kwargs['arg1']
            arg2 = kwargs['arg2']
            print(arg1, arg2)
        else:
            raise TypeError('Invalid arguments')
obj = MyClass()
obj.my_method("Hello") 
obj.my_method("Hello", "world!") 
obj.my_method(arg1="Hello", arg2="world!")
