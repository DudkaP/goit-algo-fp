from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Iterable, Tuple


@dataclass
class Node:
    value: int
    next: Optional["Node"] = None


class LinkedList:
    def __init__(self, values: Optional[Iterable[int]] = None):
        self.head: Optional[Node] = None
        if values:
            for v in values:
                self.append(v)

    def append(self, value: int) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def to_list(self) -> list[int]:
        out = []
        cur = self.head
        while cur:
            out.append(cur.value)
            cur = cur.next
        return out

    def reverse(self) -> None:
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def sort(self) -> None:
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head: Optional[Node]) -> Optional[Node]:
        if head is None or head.next is None:
            return head

        left, right = self._split(head)
        left_sorted = self._merge_sort(left)
        right_sorted = self._merge_sort(right)
        return merge_two_sorted_heads(left_sorted, right_sorted)

    def _split(self, head: Node) -> Tuple[Optional[Node], Optional[Node]]:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None
        return head, mid


def merge_two_sorted_heads(a: Optional[Node], b: Optional[Node]) -> Optional[Node]:
    dummy = Node(0)
    tail = dummy
    while a and b:
        if a.value <= b.value:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next


def merge_sorted_lists(l1: LinkedList, l2: LinkedList) -> LinkedList:
    merged = LinkedList()
    merged.head = merge_two_sorted_heads(l1.head, l2.head)
    return merged


if __name__ == "__main__":
    ll = LinkedList([3, 1, 4, 2])
    print("Original:", ll.to_list())
    ll.reverse()
    print("Reversed:", ll.to_list())
    ll.sort()
    print("Sorted:", ll.to_list())

    a = LinkedList([1, 3, 5])
    b = LinkedList([2, 4, 6])
    merged = merge_sorted_lists(a, b)
    print("Merged:", merged.to_list())
