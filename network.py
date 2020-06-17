"""
Network - DAG (Directed Acyclic Graph)
"""

import json
from utils import recursive_mkdir
from node import Node

class Network:
    def __init__(self,
                 threshold: int = 3
                 ):
        self.nodes = []
        self.links = [] # {source, target} list
        self.tips = [] # node indices
        self.threshold = threshold
        self.global_id = 0
        self.age_threshold = 4
        self.ref_threshold = 3

    def get_tips(self):
        return self.tips

    def get_tip_nodes(self):
        return [self.nodes[tip] for tip in self.tips]

    def get_node(self, id):
        return self.nodes[id]

    def get_nodes(self):
        return self.nodes

    def insert_tip(self, tip):
        self.tips.append(len(self.nodes))
        self.nodes.append(tip)

    def insert_tips(self, tips):
        self.tips.extend(range(len(self.nodes), len(self.nodes) + len(tips)))
        self.nodes.extend(tips)


    def insert_link(self, source, target):
        self.links.append({
            "source": source,
            "target": target # tip
        })
        for tip in self.tips:
            if tip == source:
                self.nodes[tip].ref = self.nodes[tip].ref + 1
                break
    
    def update(self):
        # update tips
        # self.tips = [tip for tip in self.tips if self.nodes[tip].ref < self.ref_threshold and self.nodes[tip].age < self.age_threshold]
        self.tips = [tip for tip in self.tips if self.nodes[tip].ref == 0 and self.nodes[tip].age < self.threshold]

        # increment node ages
        for node in self.nodes:
            node.age = node.age + 1

        data = {
                'nodes': [{
                    "name": node.id,
                    "accuracy": node.accuracy,
                    "ref": node.ref,
                    "age": node.age
                    } for node in self.nodes],
                'links': self.links}
        # print(data)

        with open("network.json", 'w') as outfile:
            json.dump(data, outfile)