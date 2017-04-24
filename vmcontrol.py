#!/usr/bin/env python
from azure.common.credentials import UserPassCredentials
from azure.mgmt.compute import ComputeManagementClient
import fire
import yaml
from pprint import pprint
class VMStatus(object):
  def __init__(self, name):
    self.name = name

class VMControl(object):
  def __init__(self, config_file='/work/config.yaml'):
    """Set config file (default:/work/config.yaml)"""
    config_file='/work/config.yaml'
    f = open(config_file)
    data = yaml.load(f)
    f.close()
    username = data['username']
    password = data['password']
    subscription_id = data['subscription_id']  

    credentials = UserPassCredentials(username, password)


    self._computemanagement_client = ComputeManagementClient(
        credentials,
        subscription_id
    )

  def start(self, resourcegroup, machinename):
    async_vm = self._computemanagement_client.virtual_machines.start(resourcegroup, machinename)
    async_vm.wait()
  def vmlist(self, resourcegroup):
    async_vm = self._computemanagement_client.virtual_machines.list(resourcegroup)
    vmlist=[]
    for machine in async_vm:
      name = machine.name
      vmstatus = VMStatus(name)
      vmlist.append(vmstatus)
      vmgr = self._computemanagement_client.virtual_machines.get(resourcegroup, name,expand='instanceview')
      for st in vmgr.instance_view.statuses:
        # InstanceViewStatus class | Microsoft Docs
        # https://docs.microsoft.com/en-us/dotnet/api/microsoft.azure.management.compute.models.instanceviewstatus?view=azuremgmtcompute-14.1.0-prerelease
        if st.code is not None and st.code.find('PowerState')==0:
          vmstatus.display_status = st.display_status
    for vmstatus in vmlist:
      print("%s\t%s" % (vmstatus.name, vmstatus.display_status))

  def power_off(self, resourcegroup, machinename):
    async_vm = self._computemanagement_client.virtual_machines.power_off(resourcegroup, machinename)
    async_vm.wait()
  def deallocate(self, resourcegroup, machinename):
    async_vm = self._computemanagement_client.virtual_machines.deallocate(resourcegroup, machinename)
    async_vm.wait()

if __name__ == '__main__':
  fire.Fire(VMControl)
