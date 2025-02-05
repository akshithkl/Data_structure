class MyQueue:
    def __init__(self):
        self.s1 = []  # Input stack
        self.s2 = []  # Output stack

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self._move_s1_to_s2()
        return self.s2.pop()

    def peek(self) -> int:
        self._move_s1_to_s2()
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2

    def _move_s1_to_s2(self):
        """ Move elements from s1 to s2 only if s2 is empty """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

# Example usage:
queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())  # Output: 1
print(queue.pop())   # Output: 1
print(queue.empty()) # Output: False
