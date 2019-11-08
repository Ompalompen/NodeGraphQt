
import sys

from NodeGraphQt import (NodeGraph,
                         BaseNode,
                         BackdropNode,
                         setup_context_menu)
from NodeGraphQt import QtWidgets, QtCore, PropertiesBinWidget, NodeTreeWidget
from example_nodes import basic_nodes, widget_nodes

class OutputNode(BaseNode):
    """
    A node that combines list into agregate lists, keeping all checked agregates
    """

    __identifier__ = "com.volvo"
    
    NODE_NAME = "Output Node"

    def __init__(self):
        super(OutputNode, self).__init__()
        self.add_input("In", True)
        self.add_output("Out")

    def set_content(self, content):
        #print(type(self.view))
        for item in content:
            self.add_checkbox(item, '', item, True)

        self.update()

    