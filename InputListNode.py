
import sys

from NodeGraphQt import (NodeGraph,
                         BaseNode,
                         BackdropNode,
                         setup_context_menu)
from NodeGraphQt import QtWidgets, QtCore, PropertiesBinWidget, NodeTreeWidget
from example_nodes import basic_nodes, widget_nodes

class InputListNode(BaseNode):
    """
    A node that contains input list from which to build agrigates
    """

    __identifier__ = "com.volvo"
    
    NODE_NAME = "Input Set"

    def __init__(self):
        super(InputListNode, self).__init__()

        self.add_output("Out")

    def set_content(self, content):
        #print(type(self.view))
        for item in content:
            self.add_checkbox(item, '', item, True)
        
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

    """
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
    """

    # registered nodes.
    reg_nodes = [
        basic_nodes.FooNode,
        basic_nodes.BarNode,
        widget_nodes.DropdownMenuNode,
        widget_nodes.TextInputNode,
        widget_nodes.CheckboxNode,
        InputListNode
    ]

    for n in reg_nodes:
        graph.register_node(n)


    input_node = graph.create_node('com.volvo.InputListNode',
                                name='Input Test',
                                color='#0a1e20',
                                text_color='#feab20',
                                pos=[110, 10])
    input_node2 = graph.create_node('com.volvo.InputListNode',
                                name='Input Test',
                                color='#0a1e20',
                                text_color='#feab20',
                                pos=[110, 310])

    input_node.set_content(["A", "B", "C"])

    # connect the nodes
    #foo_node.set_output(0, bar_node.input(2))
    #menu_node.set_input(0, bar_node.output(1))
    #bar_node.set_input(0, text_node.output(0))


    app.exec_()

    