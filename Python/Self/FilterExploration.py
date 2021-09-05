def check_val(s):
    print('Inside check_val'+s)
    if s in ('prabu','Maya'):
        return s


f_val = []
str = ['prabu','Maya','Samarth','Sidharth']

f_val = filter(check_val,str)
print(list(f_val))