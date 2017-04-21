#!/usr/bin/env python
from azure.common.credentials import UserPassCredentials
from azure.mgmt.compute import ComputeManagementClient
import fire
import yaml

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
  def power_off(self, resourcegroup, machinename):
    async_vm = self._computemanagement_client.virtual_machines.power_off(resourcegroup, machinename)
    async_vm.wait()
  def deallocate(self, resourcegroup, machinename):
    async_vm = self._computemanagement_client.virtual_machines.deallocate(resourcegroup, machinename)
    async_vm.wait()

if __name__ == '__main__':
  fire.Fire(VMControl)
