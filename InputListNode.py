
import sys
from typing import List
from NodeGraphQt import (NodeGraph,
                         BaseNode,
                         BackdropNode,
                         setup_context_menu)
from NodeGraphQt import QtWidgets, QtCore, PropertiesBinWidget, NodeTreeWidget
from example_nodes import basic_nodes, widget_nodes
import CombineNode, FilterNode, OrderNode, OutputNode
from Group import Group
from Agregate import Agregate

class InputListNode(BaseNode):
    """
    A node that contains input list from which to build agrigates
    """

    __identifier__ = "com.volvo"
    
    NODE_NAME = "Input Set"

    def __init__(self):
        super(InputListNode, self).__init__()

        self.add_output("Out")

    def set_content(self, content: List[Group]):
        self.clear_properties()
        #print(type(self.view))
        for item in content:
            self.add_group(item)

        self.update()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    # create node graph.
    graph = NodeGraph()

    # set up default menu and commands.
    setup_context_menu(graph)

    # viewer widget used for the node graph.
    viewer = graph.viewer()
    viewer.resize(1100, 800)
    viewer.show()

    
    # show the properties bin when a node is "double clicked" in the graph.
    properties_bin = PropertiesBinWidget(node_graph=graph)
    properties_bin.setWindowFlags(QtCore.Qt.Tool)
    def show_prop_bin(node):
        if not properties_bin.isVisible():
            properties_bin.show()
    graph.node_double_clicked.connect(show_prop_bin)


    # show the nodes list when a node is "double clicked" in the graph.
    node_tree = NodeTreeWidget(node_graph=graph)
    def show_nodes_list(node):
        if not node_tree.isVisible():
            node_tree.update()
            node_tree.show()
    graph.node_double_clicked.connect(show_nodes_list)
    

    def refresh_node(node):
        node.update()
    graph.node_double_clicked.connect(refresh_node)

    # registered nodes.
    reg_nodes = [
        BackdropNode,
        basic_nodes.FooNode,
        basic_nodes.BarNode,
        widget_nodes.DropdownMenuNode,
        widget_nodes.TextInputNode,
        widget_nodes.CheckboxNode,
        InputListNode,
        CombineNode.CombineNode,
        FilterNode.FilterNode,
        OrderNode.OrderNode,
        OutputNode.OutputNode
    ]

    for n in reg_nodes:
        graph.register_node(n)

    def CreateInputNode(node_name: str, position, groupName, agregates):
        input_node = graph.create_node('com.volvo.InputListNode',
                            name=node_name,
                            color='#0a1e20',
                            text_color='#feab20',
                            pos=position)
        # Set up for input node
        group = Group(groupName)   # Variant set group

        for name in agregates:
            a_agregate = Agregate(name) # Variant Set
            a_agregate.vsets().append(name)
            group.agregates().append(a_agregate)

        abcGroupList = { group }
        input_node.set_content(abcGroupList)

    CreateInputNode("Test Node 1", [-300, -300], "Colours", ["Red","Green","Blue"])
    CreateInputNode("Test Node 2", [-300, 90], "Size", ["Large","Medium","Small"])

    def HandleNodeConnected(source_node, taget_node):
        taget_node.node().update_model()

    def HandleNodeDisconenced(source_node, taget_node):
        taget_node.node().update_model()

    graph.port_connected.connect(HandleNodeConnected)
    graph.port_disconnected.connect(HandleNodeConnected)

    app.exec_()

    