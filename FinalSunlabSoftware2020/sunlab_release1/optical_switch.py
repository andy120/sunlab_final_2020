
from ncclient import manager
from ncclient import operations
import xml.dom.minidom
import xmltodict
import xml.etree.ElementTree as ET

# NETCONF filter to use
#netconf_filter = open("interface.xml").read()

class OpticalSwitch:

    def __init__(self,
                 host="192.168.0.2",
                 port=830,
                 user="admin",
                 pwd="Passw0rd"):

        self.host_name = host
        self.port_name = port
        self.username = user
        self.password = pwd

        print("Initialising Optical Switch with Hostname: ", self.host_name,
              "\nPort: ", self.port_name,
              "\nUsername: ", self.username,
              "\nPassword: ", self.password,
              "\n")


    def get(self):

        with manager.connect(host=self.host_name,
                             port=self.port_name,
                             username=self.username,
                             password=self.password,
                             hostkey_verify=False,
                             look_for_keys=False
                             ) as m:
            print("Server Data and Config:")
            m.raise_mode = operations.RaiseMode.NONE
            getserver = m.get()
            print(getserver)
            netconf_getserver = xmltodict.parse(str(getserver.xml))["rpc-reply"]["data"]
            print(netconf_getserver)
            # intf_conf =netconf_getserver["product-information"]
            # print(intf_conf)

            #print("manufacturer:", intf_conf["manufacturer"],
            #     "\nserial-number:", intf_conf["serial-number"],
            #     "\nmodel-name:", intf_conf["model-name"],
            #     "\nsoftware-version:", intf_conf["software-version"],
            #      "\n" )

    def get_config(self):

        with manager.connect(host=self.host_name,
                             port=self.port_name,
                             username=self.username,
                             password=self.password,
                             hostkey_verify=False,
                             look_for_keys=False) as m:
            print("Server Configuration:")
            netconf_reply = m.get_config('running', ('xpath','system-config/*[not(self::openflow)]'))
            print(netconf_reply)
            netconf_caps= xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()
            print(netconf_caps)
            print("\n")

    def get_capabilities(self):
        with manager.connect(host=self.host_name,
                             port=self.port_name,
                             username=self.username,
                             password=self.password,
                             hostkey_verify=False,
                             look_for_keys=False) as m:
            print("Server capabilities:")
            for capability in iter(m.server_capabilities):
                print(capability)
            print("Client capabilities:")
            for capability in iter(m.client_capabilities):
                print(capability)

    def get_cross_connections(self):

        with manager.connect(host=self.host_name,
                             port=self.port_name,
                             username=self.username,
                             password=self.password,
                             hostkey_verify=False,
                             look_for_keys=False) as m:

            netconf_filter = """
            <filter>

                <cross-connects xmlns="http://www.polatis.com/yang/optical-switch">

                    <pair></pair>

                </cross-connects >

            </filter>"""
            m.raise_mode = operations.RaiseMode.NONE # This ignores Polatis Openflow errors
            netconf_reply = m.get_config("running", filter=netconf_filter)
            print("Server cross connections:")
            print(netconf_reply)
            netconf_get_connections = xmltodict.parse(str(netconf_reply))["rpc-reply"]["data"]
            print(netconf_get_connections)
            crossconnectpairs = netconf_get_connections ["cross-connects"]["pair"]
            for key in crossconnectpairs:
                print("Ingress:", key["ingress"], "Egress:", key["egress"])
            print("\n")

    def add_cross_connections(self, ingressport, egressport):

        with manager.connect(host=self.host_name,
                             port=self.port_name,
                             username=self.username,
                             password=self.password,
                             hostkey_verify=False,
                             look_for_keys=False) as m:
            s1 = """
                    <config>
                        <cross-connects xmlns="http://www.polatis.com/yang/optical-switch">
                            <pair>
                                <ingress>"""
            s2 = """            </ingress>
                                <egress>"""
            s3 = """            </egress>
                            </pair>                                 
                        </cross-connects >
                    </config>"""
            netconf_temp = s1 + str(ingressport) + s2 + str(egressport) + s3

            netconf_reply = m.edit_config(netconf_temp, target="running")
            print("Server add cross connections:")
            netconf_add_connections = xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()
            print(netconf_add_connections)
            print("\n")

    def delete_cross_connections(self, ingressport):

        with manager.connect(host=self.host_name,
                             port=self.port_name,
                             username=self.username,
                             password=self.password,
                             hostkey_verify=False,
                             look_for_keys=False) as m:

            s1 = """
                    <config>
                        <cross-connects xmlns="http://www.polatis.com/yang/optical-switch">
                            <pair operation="delete">
                                <ingress>"""
            s2 = """</ingress>
                            </pair>                                 
                        </cross-connects>
                    </config>"""

            netconf_temp = s1 + str(ingressport) + s2

            print(netconf_temp)

            netconf_reply = m.edit_config(netconf_temp, target="running")

            print("Server delete cross connections:")

            print(netconf_reply)


    def get_opm_config(self):

        with manager.connect(host=self.host_name,
                             port=self.port_name,
                             username=self.username,
                             password=self.password,
                             hostkey_verify=False,
                             look_for_keys=False) as m:
            netconf_filter = """
            <filter>

              <opm-config xmlns="http://www.polatis.com/yang/optical-switch">

                <port></port>

              </opm-config>

            </filter>"""

            netconf_reply = m.get_config("running", filter=netconf_filter)

            print("Server opm connections:")

            netconf_opm_config = xmltodict.parse(str(netconf_reply.xml))["rpc-reply"]["data"]



            intf_conf =netconf_opm_config ["opm-config"]["port"]

           # print(intf_conf)

            for key in intf_conf:
                # print(key)
              #  print("Ingress:", key["ingress"], "Egress:", key["egress"])
                print("port-id:", key["port-id"],
                      "wavelength:", key["wavelength"],
                      "offset:", key["offset"],
                      "averaging-time:", key["averaging-time"],
                      )

    def add_opm_config(self):

        with manager.connect(host=self.host_name,
                             port=self.port_name,
                             username=self.username,
                             password=self.password,
                             hostkey_verify=False,
                             look_for_keys=False) as m:

            netconf_temp= """

            <config>
                  <opm-config xmlns="http://www.polatis.com/yang/optical-switch">

                  <port>

                  <port-id>1</port-id>
                  <wavelength>1400.0</wavelength>
                  <offset>1.0</offset>
                  <averaging-time>8</averaging-time>

                 </port>

                   </opm-config >


            </config>
            """

            netconf_reply = m.edit_config(netconf_temp, target="running")

            print("Server added opm config connections:")
            netconf_add_opm_config = xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()
            print(netconf_add_opm_config)
            print("\n")

    def get_opm_alarm_config(self):

        with manager.connect(host=self.host_name,
                             port=self.port_name,
                             username=self.username,
                             password=self.password,
                             hostkey_verify=False,
                             look_for_keys=False) as m:

            netconf_filter = """
            <filter>

              <opm-alarm-config xmlns="http://www.polatis.com/yang/optical-switch">

                <port></port>

              </opm-alarm-config>

            </filter>"""

            netconf_reply = m.get_config("running", filter=netconf_filter)

            print("Server opm alarm connections:")



            netconf_opm_alarm_config= xmltodict.parse(str(netconf_reply.xml))["rpc-reply"]["data"]

            intf_conf = netconf_opm_alarm_config["opm-alarm-config"]["port"]

         #   print(intf_conf)

            for key in intf_conf:

                print("port-id:", key["port-id"],
                      "mode:", key["mode"],
                      "SLT:", key["signal-low-threshold"],
                      "SDT:", key["signal-degrade-threshold"],

                      "SHT:", key["signal-high-threshold"],
                      "ACH:", key["alarm-clear-holdoff"],

                      )

    def add_opm_alarm_config(self):

        with manager.connect(host=self.host_name,
                             port=self.port_name,
                             username=self.username,
                             password=self.password,
                             hostkey_verify=False,
                             look_for_keys=False) as m:
            netconf_temp = """

            <config>
                  <opm-alarm-config xmlns="http://www.polatis.com/yang/optical-switch">

                  <port>

                  <port-id>32</port-id>
                  <mode>POWER_ALARM_ENABLED</mode>
                  <signal-low-threshold>-60.0</signal-low-threshold>
                  <signal-degrade-threshold>-60.0</signal-degrade-threshold>
                  <signal-high-threshold>25.0</signal-high-threshold>
                  <alarm-clear-holdoff>20</alarm-clear-holdoff>

                 </port>
                </opm-alarm-config >


            </config>
            """

            netconf_reply = m.edit_config(netconf_temp, target="running")

            print("Server added opm config connections:")
            netconf_add_opm_alarm_config = xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()
            print(netconf_add_opm_alarm_config)
            print("\n")

    def get_port_config(self):

        with manager.connect(host=self.host_name,
                             port=self.port_name,
                             username=self.username,
                             password=self.password,
                             hostkey_verify=False,
                             look_for_keys=False) as m:
            netconf_filter = """
            <filter>

              <port-config xmlns="http://www.polatis.com/yang/optical-switch">

                <port></port>

              </port-config>

            </filter>"""

            netconf_reply = m.get_config("running", filter=netconf_filter)

            print("Server port config connections:")

            netconf_port_config = xmltodict.parse(str(netconf_reply.xml))["rpc-reply"]["data"]

            intf_conf = netconf_port_config["port-config"]["port"]

          #  print(intf_conf)

            for key in intf_conf:
                print("port-id:", key["port-id"],


                      )
def add_port_config(self):

        with manager.connect(host=self.host_name,
                             port=self.port_name,
                             username=self.username,
                             password=self.password,
                             hostkey_verify=False,
                             look_for_keys=False) as m:
            netconf_temp = """

            <config>

                  <port-config xmlns="http://www.polatis.com/yang/optical-switch">

                <port>
                <port-id>1</port-id>
                <label>T</label>
                <peer-port/>

                </port>

                   </port-config>


            </config>
            """

            netconf_reply = m.edit_config(netconf_temp, target="running")
            print("Server added port config connections:")
            netconf_add_port_config = xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()
            print(netconf_add_port_config)
            print("\n")



