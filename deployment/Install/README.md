INSTALL

1.Copy all files into /data
2.bash ./fix-permission.sh
3.startup mock: cd MACDA/mock && docker-compose up -d
4.startup macda: 
  cd MACDA && docker-compose up -d && docker-compose stop macda1 && docker-compose stop macda2 && docker-compose stop macda3
wait for 120 seconds:
  docker-compose start macda1 && docker-compose start macda2 && docker-compose start macda3
