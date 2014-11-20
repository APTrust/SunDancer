from sundancer.conf.settings import API_KEY, API_URL
from sundancer.client import APIClient
from sundancer.staging import select_nodes, list_bagnames, make_bag_symlink
from sundancer.staging import get_sha256

if __name__ == "__main__":
    aptrust = APIClient(API_URL, API_KEY)
    data = aptrust.get_nodes(filters={'replicate_to': True})
    node_list = select_nodes(data["results"])
    bag_list = list_bagnames()
    for node in node_list:
        for bag in bag_list:
            print(get_sha256(bag))
            make_bag_symlink(node, bag)
