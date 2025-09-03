class Node:
    def __init__(self, key, parent=None):
        self.value = key
        self.parent = parent
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    def print_pre(self, ptr):
        if not ptr:
            return
        print(ptr.value, end=" ")
        self.print_pre(ptr.left)
        self.print_pre(ptr.right)

    def print_post(self, ptr):
        if not ptr:
            return
        self.print_post(ptr.left)
        self.print_post(ptr.right)
        print(ptr.value, end=" ")

    def print_in(self, ptr):
        if not ptr:
            return
        self.print_in(ptr.left)
        print(ptr.value, end=" ")
        self.print_in(ptr.right)

    
    def calHeight(self, ptr):
        if ptr is None:
            return 0
        return max(self.calHeight(ptr.left), self.calHeight(ptr.right)) + 1

    def calBalanceFactor(self, ptr):
        if ptr is None:
            return 0
        return self.calHeight(ptr.left) - self.calHeight(ptr.right)

    
    def right_rotate(self, ptr):
        tmp = ptr.parent
        if not tmp:
            return
        ptr.parent = tmp.parent
        if not tmp.parent:
            self.root = ptr
        elif tmp.parent.left == tmp:
            tmp.parent.left = ptr
        else:
            tmp.parent.right = ptr

        tmp.left = ptr.right
        if tmp.left:
            tmp.left.parent = tmp
        ptr.right = tmp
        tmp.parent = ptr

    def left_rotate(self, ptr):
        tmp = ptr.parent
        if not tmp:
            return
        ptr.parent = tmp.parent
        if not tmp.parent:
            self.root = ptr
        elif tmp.parent.left == tmp:
            tmp.parent.left = ptr
        else:
            tmp.parent.right = ptr

        tmp.right = ptr.left
        if tmp.right:
            tmp.right.parent = tmp
        ptr.left = tmp
        tmp.parent = ptr

    def balance(self, ptr):
        while ptr:
            bf = self.calBalanceFactor(ptr)
            if bf >= 2:  
                if self.calBalanceFactor(ptr.left) >= 0:
                    self.right_rotate(ptr.left)
                else:
                    self.left_rotate(ptr.left.right)
                    self.right_rotate(ptr.left)
            elif bf <= -2:  
                if self.calBalanceFactor(ptr.right) <= 0:
                    self.left_rotate(ptr.right)
                else:
                    self.right_rotate(ptr.right.left)
                    self.left_rotate(ptr.right)
            ptr = ptr.parent


    def insert_val(self, x):
        if self.root is None:
            self.root = Node(x)
            return

        ptr = self.root
        while True:
            if x < ptr.value:
                if ptr.left is None:
                    ptr.left = Node(x, ptr)
                    self.balance(ptr.left)
                    return
                ptr = ptr.left
            elif x > ptr.value:
                if ptr.right is None:
                    ptr.right = Node(x, ptr)
                    self.balance(ptr.right)
                    return
                ptr = ptr.right
            else:
                return  

    def delete_val(self, x):
        to_delete = self.root
        while to_delete:
            if to_delete.value == x:
                break
            elif to_delete.value < x:
                to_delete = to_delete.right
            else:
                to_delete = to_delete.left

        if to_delete is None:
            return 
        if to_delete.left and to_delete.right:
            
            tmp = to_delete.left
            while tmp.right:
                tmp = tmp.right
            to_delete.value, tmp.value = tmp.value, to_delete.value
            to_delete = tmp

        child = to_delete.left if to_delete.left else to_delete.right
        if child:
            if to_delete.parent:
                if to_delete.parent.left == to_delete:
                    to_delete.parent.left = child
                else:
                    to_delete.parent.right = child
            else:
                self.root = child  
            child.parent = to_delete.parent
            self.balance(child)
            return
        if to_delete.parent:
            if to_delete.parent.left == to_delete:
                to_delete.parent.left = None
            else:
                to_delete.parent.right = None
            self.balance(to_delete.parent)
        else:
            self.root = None 

def main():
    prompt = input() 
    cmd = prompt.split()

    tree = AVLTree()
    for i in cmd[:-1]:
        if i[0] == 'A':
            tree.insert_val(int(i[1:]))
        elif i[0] == 'D':
            tree.delete_val(int(i[1:]))
    if cmd[-1] == "PRE":
        tree.print_pre(tree.root)
    elif cmd[-1] == "POST":
        tree.print_post(tree.root)
    elif cmd[-1] == "IN":
        tree.print_in(tree.root)
    print()


if __name__ == "__main__":
    main()
