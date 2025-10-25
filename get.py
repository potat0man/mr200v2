from archer.mr200 import MR200Client, ConnectionFailedException, LoginFailedException, NotLoggedInException

if __name__ == "__main__":
	client = MR200Client("192.168.3.1")
	try:
		client.login("admin", "admin")
	except ConnectionFailedException:
		print("Cannot connect")
		exit()
	except LoginFailedException:
		print("Bad login")
		exit()
	try:
		# print(client.get_wan_common_intf_cfg())
		print(client.get_ipsec_cfg())
		# print(client.get_lte_wan_cfg())
#		print(client.get_lan_wlan_mssidentry())
#		print(client.get_lan_wlan())
#		print(client.get_wan_lte_link_cfg())
#		print(client.get_wan_lte_intf_cfg())
#		print(client.get_clients())
		# print(client.get_device_info())
		# print(client.get_wan_ip_connection())
#		print(client.get_sms())

		# client.reboot()

		client.logout()
	except NotLoggedInException:
		print("Not logged in")
