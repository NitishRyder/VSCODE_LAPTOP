import sys

sys.getsizeof( float(24) ) # prints 24
sys.getsizeof(0.0) # prints 24
sys.getsizeof(1e2) # prints 24
sys.getsizeof(1.123451234512345123451234512345e2) # prints 24
sys.getsizeof(1.123451234512345123451234512345e307) # prints 24
sys.getsizeof(1.123451234512345123451234512345e-307) # prints 24
sys.getsizeof(-100.25) # prints 24