from sundancer.conf.settings import API_KEY, API_URL
from sundancer.client import APIClient
from sundancer.staging import select_nodes

if __name__ == "__main__":
    aptrust = APIClient(API_URL, API_KEY)
    data = aptrust.get_nodes(filters={'replicate_to': True})
    print(select_nodes(data["results"]))
