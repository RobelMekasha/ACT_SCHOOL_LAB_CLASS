def pass_fail(name, ave:float ):
    if (ave > 80 ):
        print(f'{name} great job')
    
    elif (ave > 50):
        print(f'{name} passed')
        
    elif (ave < 60):
        print (f'{name} failed')

name_ = input ( 'pls enter your name: ')
ave_ = int(input('pls enter your ave: '))


pass_fail(name_, ave_)