
from __future__ import annotations

from dataclasses import dataclass
import sys


@dataclass
class Node:
    key: int
    left: Node | None = None
    right: Node | None = None
    height: int = 1


# ---------- Высота и баланс ----------

def get_height(root: Node | None):
    if root is None:
        return 0
    return root.height


def upd_height(root: Node):
    root.height = 1 + max(
        get_height(root.left),
        get_height(root.right)
    )


def balance(root: Node | None):
    if root is None:
        return 0

    return get_height(root.right) - get_height(root.left)


# ---------- Повороты ----------

def turn(root: Node, is_left: bool = True) -> Node:
    dop = root

    if is_left:
        new_root = root.right
        assert new_root is not None

        dop.right = new_root.left
        new_root.left = dop

    else:
        new_root = root.left
        assert new_root is not None

        dop.left = new_root.right
        new_root.right = dop

    upd_height(dop)
    upd_height(new_root)

    return new_root


# ---------- Балансировка ----------

def rebalance(root: Node) -> Node:
    upd_height(root)

    b = balance(root)

    if b == 2:
        if balance(root.right) < 0:
            root.right = turn(root.right, False)

        return turn(root, True)

    elif b == -2:
        if balance(root.left) > 0:
            root.left = turn(root.left, True)

        return turn(root, False)

    return root


# ---------- Вставка ----------

def add_node(root: Node | None, value: int) -> Node:
    if root is None:
        return Node(value)

    if root.key > value:
        root.left = add_node(root.left, value)

    elif root.key < value:
        root.right = add_node(root.right, value)

    else:
        return root

    return rebalance(root)


# ---------- Удаление ----------

def del_tree(root: Node | None, value: int) -> Node | None:
    if root is None:
        return None

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

            while now.left is not None:
                now = now.left

            root.key = now.key
            root.right = del_tree(root.right, now.key)

    return rebalance(root)


# ---------- Проверка существования ----------

def exists_tree(root: Node | None, value: int):
    now = root

    while now is not None:
        if now.key == value:
            return now

        elif now.key > value:
            now = now.left

        else:
            now = now.right

    return None


# ---------- Следующий ключ ----------

def next_tree(root: Node | None, value: int):
    now = root
    result = None

    while now is not None:
        if now.key >= value:
            result = now.key
            now = now.left

        else:
            now = now.right

    return result


# ---------- Предыдущий ключ ----------

def prev_tree(root: Node | None, value: int):
    now = root
    result = None

    while now is not None:
        if now.key <= value:
            result = now.key
            now = now.right

        else:
            now = now.left

    return result


# ---------- Прямой обход ----------

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


# ---------- Основная программа ----------

total_root: Node | None = None

answer = []

Q = int(input())

for _ in range(Q):
    cmd = input().split()

    if cmd[0] == "add":
        total_root = add_node(total_root, int(cmd[1]))

    elif cmd[0] == "del":
        total_root = del_tree(total_root, int(cmd[1]))

    elif cmd[0] == "exists":
        if exists_tree(total_root, int(cmd[1])) is None:
            answer.append("NO")
        else:
            answer.append("YES")

    elif cmd[0] == "next":
        answer.append(str(next_tree(total_root, int(cmd[1]))))

    elif cmd[0] == "prev":
        answer.append(str(prev_tree(total_root, int(cmd[1]))))

    elif cmd[0] == "root":
        if total_root is None:
            answer.append("Empty")
        else:
            answer.append(str(total_root.key))

    elif cmd[0] == "height":
        answer.append(str(get_height(total_root)))

    elif cmd[0] == "print":
        answer.append(values_tree(total_root))


for i in answer:
    print(i)