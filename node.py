"""
Node
"""

class Node:
    global_id = 0
    def __init__(self,
                 r,  # TODO: case None
                 w,  # TODO: gradient
                 accuracy,
                #  id=None,  # TODO: case None
                 parent: list = [],
                 edges: list = []):

        # assert(id != None)
        self.id = Node.global_id
        Node.global_id = Node.global_id + 1
        self.ref = 0
        self.age = 0

        self.r = r
        self.w = w

        # self.parent = parent
        self.edges = edges

        self.accuracy = accuracy

    def get_id(self):
        return self.id

    def get_weights(self):
        return self.w
