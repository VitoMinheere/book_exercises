"""Variable positional arguments"""

def log(message, values):
    if not values:
        print (message)
    else :
        values_str = ', ' .join(str (x) for x in values)
        print ('%s: %s' % (message, values_str))

log('My numbers are' , [1 , 2 ])
log('Hi there' , [])

def log_opt(message, * values):  # The only difference
    if not values:
        print (message)
    else :
        values_str = ', ' .join(str (x) for x in values)
        print ('%s: %s' % (message, values_str))

log_opt('My numbers are' , [1 , 2 ])
log_opt('Hi there')

favorite = [7, 33, 99]
log_opt("Favorite colors", *favorite)
