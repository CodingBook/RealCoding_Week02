class PriorityQueue:
  def __init__(self):
    self.heap = []

  def push(self, item, priority):
    entry = (priority, item)
    self.heap.append(entry)
    self._sift_up(len(self.heap) - 1)

  def pop(self):
    if len(self.heap) > 1:
      self._swap(0, len(self.heap) - 1)
      item = self.heap.pop()[1]
      self._sift_down(0)
      return item
    elif len(self.heap) == 1:
      item = self.heap.pop()[1]
      return item
    else:
      return None

  # 잎에서 올라가며 비교하는 함수, 우선순위가 높을 수록(숫자가 작을수록) 루트로, 최소힙?
  def _sift_up(self, index):
    while index > 0:
      parent_index = (index - 1) // 2
      if self.heap[parent_index][0] > self.heap[index][0]:
        self._swap(parent_index, index)
        index = parent_index
      else:
        break

  # 루트에 있는걸 알맞게 배치하는 함수
  def _sift_down(self, index):
    while True:
      left_child_index = 2 * index + 1
      right_child_index = 2 * index + 2
      smallest = index # 우선순위가 가장 낮은 녀석(== 숫자가 높은 녀석)

      if left_child_index < len(self.heap) and \
        self.heap[left_child_index][0] < self.heap[smallest][0]:
        smallest = left_child_index

      if right_child_index < len(self.heap) and \
        self.heap[right_child_index][0] < self.heap[smallest][0]:
        smallest = right_child_index

      if smallest != index:
        self._swap(index, smallest)
        index = smallest
      else:
        break

  def _swap(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
