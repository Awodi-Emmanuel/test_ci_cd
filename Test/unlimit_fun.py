def unlimit_fun(*args):
    print("The youngest child is " + args[0])
    
# unlimit_fun("Emil", "Tobias", "Linus")

def call_fun():
    
    ref_fun = unlimit_fun()
call_fun("emil", "tobias")
