# def is_subsequence(s, t):
#     point_s, point_t = 0,0
#     while point_s < len(s) and point_t < len(t):
#         if s[point_s] == t[point_t]:
#             point_s += 1
#             point_t += 1
#         else:
#             point_t += 1
#     if point_s == len(s):
#         return True
#     else:
#         return False

# def maj_element(nums):
#     if not nums:
#         return 0
#     result = dict()
#     counter = 0
#     ce = nums[0]
#     for element in nums:
#         if element != ce:
#             result[ce] = max(counter, result.get(ce, 0))
#             counter = 1
#             ce = element
#         else:
#             counter += 1
#     result[ce] = max(counter, result.get(ce, 0))
#
#     return max(result, key=result.get)

#
# def rotate_right(head, k):
#     if not head or not head.next or k == 0:
#         return head
#
#     # Найти длину списка
#     length = 1
#     p = head
#     while p.next:
#         p = p.next
#         length += 1
#
#     p.next = head
#
#     k = k % length
#     steps_to_new_head = length - k
#
#     new_tail = head
#     for _ in range(steps_to_new_head - 1):
#         new_tail = new_tail.next
#
#     new_head = new_tail.next
#     new_tail.next = None
#
#     return new_head

# def color_sort(nums):
#     red, white, blue = 0, 0, len(nums) - 1
#     while white <= blue:
#         if nums[white] == 0:
#             tmp = nums[red]
#             nums[red] = nums[white]
#             nums[white] = tmp
#             red += 1
#             white += 1
#         elif nums[white] == 1:
#             white += 1
#         else:
#             tmp = nums[blue]
#             nums[blue] = nums[white]
#             nums[white] = tmp
#             blue -= 1
#     return nums


# def are_trees_equal(head_1, head_2):
#     if head_1 is None and head_2 is None:
#         return True
#     if head_1 is None or head_2 is None:
#         return False
#     if head_1.val != head_2.val:
#         return False
#     return are_trees_equal(head_1.left, head_2.left) and are_trees_equal(head_1.right, head_2.right)

#
# def invert_tree(head):
#     if head is None:
#         return
#     head.left, head.right = head.right, head.left
#
#     invert_tree(head.left)
#     invert_tree(head.right)
#
#     return head


# def dfs(board, i, j):
#     if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != 'O':
#         return
#     board[i][j] = 'T'
#     dfs(board, i - 1, j)  # up
#     dfs(board, i + 1, j)  # down
#     dfs(board, i, j - 1)  # left
#     dfs(board, i, j + 1)  # right
#
#
# def drown(board):
#     if not board or not board[0]:
#         return board
#
#     m, n = len(board), len(board[0])
#
#     for i in range(m):
#         if board[i][0] == 'O':
#             dfs(board, i, 0)
#         if board[i][n - 1] == 'O':
#             dfs(board, i, n - 1)
#     for j in range(n):
#         if board[0][j] == 'O':
#             dfs(board, 0, j)
#         if board[m - 1][j] == 'O':
#             dfs(board, m - 1, j)
#
#     for i in range(m):
#         for j in range(n):
#             if board[i][j] == 'O':
#                 board[i][j] = 'X'
#             elif board[i][j] == 'T':
#                 board[i][j] = 'O'
#
#     return board
#
# res = []
# def inorder(root):
#     if root is not None:
#         inorder(root.left)
#         res.append(root.val)
#         inorder(root.right)
#     return res
#
#
# def kth_smallest(head, k):
#     return inorder(head)[k - 1]


# def merge(a, b):
#     new_list = []
#     point_a, point_b = 0, 0
#     while point_a < len(a) and point_b < len(b):
#         if a[point_a] < b[point_b]:
#             new_list.append(a[point_a])
#             point_a += 1
#         else:
#             new_list.append(b[point_b])
#             point_b += 1
#     if point_a < len(a):
#         new_list.extend(a[point_a:])
#     if point_b < len(b):
#         new_list.extend(b[point_b:])
#     return new_list
#
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     return merge(merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:]))


# def solve_grid(arr, i, j):
#     if arr[i][j] != 0:
#         return arr[i][j]
#     arr[i][j] = solve_grid(arr, i - 1, j) + solve_grid(arr, i, j - 1)
#     return arr[i][j]
#
# def min_path(grid):
#     for i in range(len(grid)):
#         grid[0][i] = 1
#         grid[i][0] = 1
#     return solve_grid(grid, len(grid) - 1, len(grid) - 1)

# def min_path(grid):
#     if grid is None or not grid:
#         return
#     for i in range(1, len(grid)):
#         grid[i][0] += grid[i - 1][0]
#
#     for j in range(1, len(grid[0])):
#         grid[0][j] += grid[0][j - 1]
#
#     for i in range(1, len(grid)):
#         for j in range(1, len(grid[0])):
#             grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
#     return grid[-1][-1]

# import heapq
#
# def last_stone(stones):
#     max_heap = [-stone for stone in stones]
#     heapq.heapify(max_heap)
#
#     while len(max_heap) > 1 and max_heap[0] != 0:
#         heaviest1 = -heapq.heappop(max_heap)
#         heaviest2 = -heapq.heappop(max_heap)
#
#         if heaviest1 != heaviest2:
#             new_stone = heaviest1 - heaviest2
#             heapq.heappush(max_heap, -new_stone)
#
#     # Остается один камень или ноль камней
#     if max_heap:
#         return -max_heap[0]
#     else:
#         return 0

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[high], arr[i+1] = arr[i+1], arr[high]
    return i+1

def kth_largest(array, k):
    if k < 1 or k > len(array):
        return None

    low = 0
    high = len(array) - 1
    while True:
        m = partition(array, low, high)
        if m + 1 == k:
            return array[m]
        elif m + 1 > k:
            high = m - 1
        else:
            low = m + 1

