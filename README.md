# mysql-prometheus-sandbox
### run
```bash
sudo docker compose -f prometheus-mysql.yml up
```
### connect to mysql
```bash
sudo docker exec -it mysql mysql -h 127.0.0.1 -u root -p 
```