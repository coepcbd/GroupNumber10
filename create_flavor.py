from credentials import get_nova_credentials_v2
from novaclient.client import Client

credentials = get_nova_credentials_v2()
nova_client = Client(**credentials)

x = raw_input("Enter flavor name")
y = raw_input("Enter ram amount")
z = raw_input("Enter no of vcpus")
w = raw_input("Enter disk amount")

nova_client.flavors.create(name=x, ram=y, vcpus=z, disk=w, is_public=False)
