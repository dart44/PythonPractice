def minSwapsRequired(s):
  chars = list(s)
  left = 0
  right = len(chars) - 1
  swap_count = 0
  
  while left < right:
    if chars[left] == chars[right]:
      continue
    mid = (left + right) // 2
    if chars[left] == chars[right]:
      continue
    if chars[mid] != chars[left] and chars[mid] != chars[right]:
      left += 1
      right -= 1
      r_chars = chars[::-1]
      if chars == r_chars:
        return swap_count
      continue
    if chars[mid] == chars[left] and chars[mid] != chars[right]:
      chars[mid], chars[right] = chars[right], chars[mid]
      swap_count += 1
      right -= 1
      r_chars = chars[::-1]
      if chars == r_chars:
        return swap_count
      continue
    if chars[mid] != chars[left] and chars[mid] == chars[right]:
      chars[mid], chars[left] = chars[left], chars[mid]
      swap_count += 1
      left += 1
      r_chars = chars[::-1]
      if chars == r_chars:
        return swap_count
      continue
  return -1
    
    

    
    # 00001
    # 10000
  

# Driver Code
def main():
    n = 0
    print(f'{minSwapsRequired([1,0,1,0,0,0])}')
    
# Run driver code if this file is not being imported
if __name__ == '__main__':
    main()