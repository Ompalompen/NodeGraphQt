
import sys

from typing import List
from NodeGraphQt import (NodeGraph,
                         BaseNode,
                         BackdropNode,
                         setup_context_menu)
from NodeGraphQt import QtWidgets, QtCore, PropertiesBinWidget, NodeTreeWidget
from example_nodes import basic_nodes, widget_nodes
import Group, Agregate

class CombineNode(BaseNode):
    """
    A node that combines list into agregate lists
    """

    __identifier__ = "com.volvo"
    
    NODE_NAME = "Combine Node"

    def __init__(self):
        super(CombineNode, self).__init__()
        self.add_input("In", True)
        self.add_output("Out")

    def set_content(self, content):
        self.clear_properties()
        self.add_group(content)
        self.update()

    def update_model(self):

        inputlist = []
        for port in self.inputs().values():
            if len(port.connected_ports()) > 0:
                for connectedPort in port.connected_ports():
                    group = connectedPort.node().get_property("Group")
                    inputlist.append(group)

        storageList = []
        combineGroup = Group.Group("Combine")
        self.buildAggregateItemRecursive([], [], inputlist, 0, True, storageList, combineGroup)
        print(storageList)
        self.set_content(combineGroup)
        super(CombineNode, self).update_model()

                    
    def buildAggregateItemRecursive(self, nameResult, agregatesResult, orderedGroups, index, checked, storage, group):
        if len(orderedGroups) > index:
            orderedGroup = orderedGroups[index]
            agregates = orderedGroup.agregates()
            for rowIndex in range(len(agregates)):
                agregate = agregates[rowIndex]
                self.buildAggregateItemRecursive(nameResult + [agregate.name()], agregatesResult + [agregate], orderedGroups, index+1, True, storage, group)
        else:
            name = "_".join(nameResult)
            newAgregate = Agregate.Agregate(name)
            for agregate in agregatesResult:
                newAgregate.vsets().append(agregate.vsets)
            group.agregates().append(newAgregate)
            if checked:
                storage.append(name)




    