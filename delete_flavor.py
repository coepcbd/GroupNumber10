from credentials import get_nova_credentials_v2
from novaclient.client import Client

credentials = get_nova_credentials_v2()
nova_client = Client(**credentials)

flavors_list = nova_client.flavors.list()
flavor = raw_input("Enter flavor to be deleted")
flavor_exists = False

for flav in flavors_list:
    if flav.name == flavor:
        print "flavor %s exists" % flavor
        flavor_exists = True
        break
if not flavor_exists:
    print "flavor %s doesnot exists" % flavor
else:
    nova_client.flavors.delete(flav)
