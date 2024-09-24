# mysql-prometheus-sandbox

### run
```bash
sudo docker compose -f prometheus-mysql.yml up
```
### connect to mysql
```bash
sudo docker exec -it mysql mysql -h 127.0.0.1 -u root -p 
```

### grafana
[http://localhost:3000/](http://localhost:3000/)

### exporter
[http://localhost:9104/](http://localhost:9104/)

### prometheus
[http://localhost:9090/](http://localhost:9090/)

### notes
You may need to adjust IP address in yml files