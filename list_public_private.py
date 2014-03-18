from credentials import get_nova_credentials_v2
from novaclient.client import Client

credentials = get_nova_credentials_v2()
nova_client = Client(**credentials)
flavors_list = nova_client.flavors.list()
for flav in flavors_list :
	print "flavor name:", flav.name
	print "\t"
	if flav.is_public == True :
		print "public"
     	else :
		print "private"
	print "\n"
