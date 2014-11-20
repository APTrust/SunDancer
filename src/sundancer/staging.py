import random, glob, os, hashlib
from sundancer.conf.settings import NODE_COPIES, STAGING_DIR, NODE_DIRS

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

def list_bagnames():
    """
    Returns a list of all the bag filenames.
    """
    bag_list = []
    for file in glob.glob("%s/*.tar" % STAGING_DIR):
        bag_list.append(os.path.basename(file))
    return bag_list

def make_bag_symlink(node, filename):
    """
    Creates a symlink in the outbound directory for the named node for the
    staged bag file provided.

    :param node: String namespace of node to stage for.
    :param filename: String basename of bag file.
    :return:
    """
    try:
        src = os.path.join(STAGING_DIR, filename)
        dest = os.path.join(NODE_DIRS[node]['CONTENT_DIR'], filename)
        dest = os.path.normpath(dest)
        os.symlink(src, dest)
    except FileExistsError:
        pass

def get_sha256(bagname):
    """
    Returns the sha256 hex hash of a file.
    :param bagname:  String of the path to the file
    :return: String of the hex value of the checksum.
    """
    size = 65536
    fname = os.path.join(STAGING_DIR, bagname)
    sha2 = hashlib.sha256()
    with open(fname, 'rb') as f:
        buf = f.read(size)
        while len(buf) > 0:
            sha2.update(buf)
            buf = f.read(size)
    return sha2.hexdigest()