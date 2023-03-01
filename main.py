def find_index(nums, left, right, key):
  if right >= left:
    mid = left + (right - left) // 2
    if nums[mid] == key:
      return mid
    elif nums[mid] > key:
      return find_index(nums, 0, mid - 1, key)
    else:
      return find_index(nums, mid + 1, len(nums)-1, key)
  else:
    return -1

list = [2, 10, 14, 16, 19, 25, 35, 100]
find = 100
index = find_index(list, 0, len(list)-1, find)
if index != -1:
  print("The number you are looking for is at index " + str(index))
else:
  print("That number is not present in the list")
