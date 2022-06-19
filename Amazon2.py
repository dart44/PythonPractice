#
# Complete the 'findMaxProducts' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY products as parameter.
#

def findMaxProducts(products):
  left = 0
  right = 1
  max_products = 0
  current_max = 0
  while right < len(products):
      if products[left] <= products[right]:
          current_max = products[right] + products[right] - 1
  

    
def main():
  print(findMaxProducts([1,2,3,4,5,20,7,8,9,10]))