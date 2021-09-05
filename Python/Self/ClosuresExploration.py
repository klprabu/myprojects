def transmit_to_space(message):
    cntr = 0
    cntr = cntr + 1
    print(cntr)
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"

        print('Testing -->'+message)

    data_transmitter()
    print('Testing 2')

print(transmit_to_space("Test message"))
print("over")



def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        #nonlocal number
        number=3
        print(number)

    print(number)
    printer()
    print(number)

print_msg(9)


def transmit_to_space(message):
  "This is the enclosing function"
  def data_transmitter():
      "The nested function"
      print(message)
  return data_transmitter

fun2 = transmit_to_space("Burn the Sun!")
print(type(fun2))
fun2()

print("*****************************************************************")

# your code goes here

def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier

multiplywith5 = multiplier_of(5)
for i in range(1,5):
    print(multiplywith5(i))