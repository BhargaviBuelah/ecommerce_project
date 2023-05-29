'''
def middlewarename(get_response):
    code which is required only one time
    execution.For initialization or configuration.

    def your_function(request):

        code to be executed before view function is called.
        variable=get_response(request)
        code to be exeuted after view function is called

        return response
    
    return your_function

'''
'''

def todo_middleware(get_response):
    print("Code to be executed only  once for initialization")

    def todo_function(request):
        print("Code to be executed before view function is called")
        res=get_response(request)
        print("Code to be executed after view function is called")

        return res
    return todo_function
'''
class todo_middleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("class based Middleware:Code to be executed only  once for initialization")

    def __call__(self,request):
        print("class based Middleware:Code to be executed before view function is called")
        res=self.get_response(request)
        print("class based Middleware:Code to be executed after view function is called")
        return res
