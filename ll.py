from typing import Any, Iterator, Optional


class Node:
    value: Any
    next: Optional["Node"]

    def __init__(self, value: Any) -> None:
        self.value = value
        self.next = None


class LinkedList:
    head: Optional[Node]
    tail: Optional[Node]
    length: int

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self) -> int:
        return self.length

    def is_empty(self) -> bool:
        return self.length == 0

    def append(self, value: Any) -> None:
        node = Node(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            assert self.tail is not None
            self.tail.next = node
            self.tail = node
        self.length += 1

    def prepend(self, value: Any) -> None:
        node = Node(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def to_list(self) -> list:
        return [item for item in self]

    def __iter__(self) -> Iterator[Any]:
        current = self.head
        while current is not None:
            yield current.value
            current = current.next