import uuid
from datetime import datetime

from sundancer.conf.settings import API_KEY, API_URL, NAMESPACE
from sundancer.client import APIClient
from sundancer.staging import select_nodes, baginfo_list, make_bag_symlink
from sundancer.staging import make_rsync_link
from sundancer.utils import dpn_strftime

if __name__ == "__main__":
    aptrust = APIClient(API_URL, API_KEY)
    data = aptrust.get_node_list(filters={'replicate_to': True})
    bag_list = baginfo_list()

    # Create the Registry for each bag.
    for bag in bag_list:
        id = "%s" % uuid.uuid4()
        reg = {
            "first_node": NAMESPACE,
            "brightening_objects": [],
            "replicating_nodes": ["aptrust",],
            "dpn_object_id": id,
            "local_id": None,
            "version_number": 1,
            "creation_date": dpn_strftime(datetime.utcnow()),
            "last_modified_date": dpn_strftime(datetime.utcnow()),
            "bag_size": bag["size"],
            "object_type": "D",
            "previous_version": None,
            "forward_version": None,
            "first_version": id,
        }
        aptrust.create_registry_entry(reg)
        for node in select_nodes(data["results"]):
            make_bag_symlink(node, bag["name"], alt_id=id)
            trans = {
                "dpn_object_id": id,
                "exp_fixity": bag["checksum"],
                "node": node,
                "size": bag["size"],
                "link": make_rsync_link(node, "%s.tar" % id)
            }
            aptrust.create_transfer(trans)

