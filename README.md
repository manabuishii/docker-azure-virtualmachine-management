# docker-azure-virtualmachine-management
Docker container for Azure VirtualMachine Management

# Version

0.4.0

* [manabuishii/docker-azure-virtualmachine-management - Docker Hub](https://hub.docker.com/r/manabuishii/docker-azure-virtualmachine-management/)

# How to use

## Prepare config file

```
username: YOURPORTALLOGINNAME
password: YOURPASSWORD
subscription_id: YOURSUBSCRIPTIONID
```

## Help

```
docker run --rm -v $PWD:/work manabuishii/docker-azure-virtualmachine-management:0.4.0 help
```

## Start machine

```
docker run --rm -v $PWD:/work manabuishii/docker-azure-virtualmachine-management:0.4.0 YOURRESOURCEGROUP YOURVIRTUALMACHINE
```
