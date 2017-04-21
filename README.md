# docker-azure-virutalmachine-management
Docker container for Azure VirtualMachine Management

# Version

0.3.0

* [manabuishii/docker-azure-virutalmachine-management - Docker Hub](https://hub.docker.com/r/manabuishii/docker-azure-virutalmachine-management/)

# How to use

## Prepare config file

```
username: YOURPORTALLOGINNAME
password: YOURPASSWORD
subscription_id: YOURSUBSCRIPTIONID
```

## Help

```
docker run --rm -v $PWD:/work manabuishii/docker-azure-virutalmachine-management:0.3.0 help
```

## Start machine

```
docker run --rm -v $PWD:/work manabuishii/docker-azure-virutalmachine-management:0.3.0 YOURRESOURCEGROUP YOURVIRTUALMACHINE
```
