class TreeNode:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data 
        self.left = left
        self.right = right

    def add_data(self, data):
        if self.data == data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_data(data)
            else:
                self.left = TreeNode(data)
        else:
            if self.right:
                self.right.add_data(data)
            else:
                self.right = TreeNode(data)
    
    def in_order(self):
        elements = []

        if self.left:
            elements += self.left.in_order()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order()
        return elements

if __name__ == "__main__":
    a = TreeNode(24)
    a.add_data(23)
    a.add_data(47)
    a.add_data(21)
    a.add_data(3)
    print(a.in_order())