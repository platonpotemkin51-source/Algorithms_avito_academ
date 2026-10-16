from __future__ import annotations

from collections import deque
from dataclasses import dataclass


@dataclass
class Node:
    key: int
    left: Node | None = None
    right: Node | None = None

def add_node(root: Node | None, value):
    if root is None:
        return Node(value)
    
    now = root
    
    while True:
        if now.key == value:
            return root
        elif now.key >= value:
            if now.left is None:
                now.left = Node(value)
                return root
            else:
                now = now.left
        elif now.key <= value:
            if now.right is None:
                now.right = Node(value)
                return root
            else:
                now = now.right

        

def values_tree(root: Node | None):
    result: list[int] = []
    
    def go(now: Node | None):
        if now is None:
            return
        
        result.append(now.key)
        go(now.left)
        go(now.right)


    go(root)

    if not result:
        return "Empty"

    return ' '.join(map(str, result))

def height_tree(root: Node | None):
    if root is None:
        return -1
    
    now = root
    
    return 1 + max(height_tree(now.left), height_tree(now.right))

def exists_tree(root: Node | None, value):
    now = root

    while now is not None:
        if now.key == value:
            return now
        elif now.key > value: 
            now = now.left
        elif now.key < value:
            now = now.right   
    
    return None 

def del_tree(root: Node | None, value) -> Node | None:
    if root is None:
        return

    if root.key > value:
        root.left = del_tree(root.left, value)
    elif root.key < value:
        root.right = del_tree(root.right, value)

    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            now = root.right

            while now.left != None:
                now = now.left

            root.key = now.key

            root.right = del_tree(root.right, now.key)
    return root           



total_root: Node | None = None

answer = []

x = int(input())

for _ in range(x):
    cmd = list(input().split())

    if cmd[0] == "add":
        total_root = add_node(total_root, int(cmd[1]))
    elif cmd[0] == "del":
        total_root = del_tree(total_root, int(cmd[1]))
    elif cmd[0] == "exists":
        if exists_tree(total_root, int(cmd[1])) == None:
            answer.append("NO")
        else:
            answer.append("YES")

    elif cmd[0] == "height":
        answer.append(1 + height_tree(total_root))

    elif cmd[0] == "print":
        answer.append(values_tree(total_root))


for i in answer:
    print(i)
                