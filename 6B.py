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

def turn(root: Node | None, value: int, is_left: bool = True):
    if root is None:
        return
    
    if root.key > value:
        root.left = turn(root.left, value, is_left)
    elif root.key < value:
        root.right = turn(root.right, value, is_left)

    else:
        dop: Node = root
        
        if is_left:
            root = root.right

            dop.right = root.left

            root.left = dop
        else:
            root = root.left

            dop.left = root.right

            root.right = dop
        
    return root



total_root: Node | None = None

answer = []

N = int(input())

A = list(map(int, input().split(" ")))

for x in A:
    total_root = add_node(total_root, x)

# print(values_tree(total_root))

M = int(input())

for _ in range(M):
    cmd = input().split()

    if cmd[0] == "left":
        total_root = turn(total_root, int(cmd[1]))
        print(values_tree(total_root))
    elif cmd[0] == "right":
        total_root = turn(total_root, int(cmd[1]), False)
        print(values_tree(total_root))


                