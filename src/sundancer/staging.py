import random
from sundancer.conf.settings import NODE_COPIES

"""
Deals with operates related to staging content for replication into DPN.
"""

def select_nodes(node_list, num_nodes=NODE_COPIES):
    """
    Selects the nodes to copy with and returns their namespaces.

    :param num_nodes: Int of number of nodes to select.
    :return: List of node namespace strings.
    """
    picks = random.sample(node_list, num_nodes)
    return [pick["namespace"] for pick in picks]
