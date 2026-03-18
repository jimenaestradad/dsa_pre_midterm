from typing import Any, Optional


class Node:
    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Optional["Node"] = None
        self.prev: Optional["Node"] = None

    def __repr__(self):
        title = self.data.get("title") if isinstance(self.data, dict) else self.data
        return f"(DATA: {title} | NEXT: {self.next is not None})"


class LinkedList:
    def __init__(self):
        self.start: Optional[Node] = None

    def __repr__(self):
        nodes = ["START"]
        for node in self:
            if isinstance(node.data, dict):
                nodes.append(str(node.data.get("title")))
            else:
                nodes.append(str(node.data))
        nodes.append("NIL")
        return "\n" + " --> ".join(nodes)

    def __iter__(self):
        node = self.start
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        length = 0
        for _ in self:
            length += 1
        return length

    def traverse(self):
        for node in self:
            print(node.data)

    def insert_at_beginning(self, element):
        element.next = self.start
        element.prev = None
        if self.start is not None:
            self.start.prev = element
        self.start = element

    def insert_at_end(self, element):
        if self.start is None:
            self.start = element
            element.prev = None
            element.next = None
            return
        current = self.start
        while current.next is not None:
            current = current.next
        current.next = element
        element.prev = current
        element.next = None

    def insert_after_node(self, element, node_reference):
        for current in self:
            if current.data == node_reference or (
                isinstance(current.data, dict)
                and current.data.get("title") == node_reference
            ):
                element.next = current.next
                element.prev = current
                if current.next is not None:
                    current.next.prev = element
                current.next = element
                return True
        return False

    def delete_node(self, element_data):
        if self.start is None:
            return False

        if self.start.data == element_data or (
            isinstance(self.start.data, dict)
            and self.start.data.get("title") == element_data
        ):
            next_node = self.start.next
            if next_node is not None:
                next_node.prev = None
            self.start = next_node
            return True

        for current in self:
            if current.data == element_data or (
                isinstance(current.data, dict)
                and current.data.get("title") == element_data
            ):
                prev_node = current.prev
                next_node = current.next
                if prev_node is not None:
                    prev_node.next = next_node
                if next_node is not None:
                    next_node.prev = prev_node
                return True

        return False

    def search(self, element_data):
        for node in self:
            if node.data == element_data or (
                isinstance(node.data, dict)
                and node.data.get("title") == element_data
            ):
                return node
        return None