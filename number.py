class Number:
    def __init__(self, value: int):
        self.value = value


    def get_number(self):
        """
        Returns the number.
        returns: int
        """
        return self.value

        pass

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        return True if self.value%2==1 else False
        pass

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        return True if self.value%2==0 else False
        pass

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        a=0
        for i in range(1,self.value+1):
            if self.value%i==0:
                a+=1
        return True if a==2 else False

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        a=[]
        for i in range(1,self.value+1):
            if self.value%i==0:
                a.append(i)
        return a

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        return len(str(self.value))

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        return str(self.value)[::-1]

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        return True if str(self.value)[0]==str(self.value)[-1] else False
    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        pass

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        pass

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        pass

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        pass

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        pass

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        pass

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        pass
    

# Create a new instance of Number
number = Number(202)
print(number.is_palindrome())
