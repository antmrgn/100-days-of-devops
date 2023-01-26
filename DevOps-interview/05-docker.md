**Q:** How to reduce size of docker image?  
**A:** Использовать другой базовый образ (например, вместо образа Ubuntu использовать Alpine). Последним шагом очищать кеши, которые могли быть созданы при сборке образа (например, очищать /var/lib/apt/lists/, если выполнялось apt update). Объединить несколько слоев в один (например, выполнить RUN apt-get update && apt-get install vim, виесто того чтобы дважды использовать RUN)  
  
**Q:**  Explain the differences between Docker images and Docker containers  
**A:**  
| Docker Images        | Docker Containers           |
| ------------- |-------------|
| Образы это шаблоны докер контейнеров      | Контейнеры это исполняемые экземпляры образов |
| Образ собирается с использованием Dockerfile     | Контейнеры создаются с использованием образов      |
| Хранятся в DOcker Hub или в Docker repository | Хранятся в Docker демоне      |
| Слой образа это read-only файловая система | Каждый слой контейнера это read-write файловая система      |