
import sys

from NodeGraphQt import (NodeGraph,
                         BaseNode,
                         BackdropNode,
                         setup_context_menu)
from NodeGraphQt import QtWidgets, QtCore, PropertiesBinWidget, NodeTreeWidget
from example_nodes import basic_nodes, widget_nodes
import Group

class FilterNode(BaseNode):
    """
    A node that enables filtering of inputs
    """

    __identifier__ = "com.volvo"
    
    NODE_NAME = "Filter"

    def __init__(self):
        super(FilterNode, self).__init__()
        self.add_input("In", True)
        self.add_output("Out")

    def set_content(self, content):
        self.clear_properties()

        for group in content:
            self.add_group(group, True)
            self.add_text(group.name(), '', group.name(), False)
            for agregate in group.agregates():
                self.add_checkbox(agregate.name(), '', agregate.name(), True)

        self.update()

    def update_model(self):

        inputlist = []
        for port in self.inputs().values():
            for connectedPort in port.connected_ports():
                group = connectedPort.node().get_property("Group")
                inputlist.append(group)

                #for propkey, prop in connectedPort.node().properties().items():
                #    if propkey == "custom": # Prop is our Group entries {name: str, group: Group}
                #        for group in prop.values(): # Group key
                #            inputlist.append(group)          

        self.set_content(inputlist)
        super(FilterNode, self).update_model()




    