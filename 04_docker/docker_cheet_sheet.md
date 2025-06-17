Here’s a **cheat sheet** of essential Docker commands for managing images, containers, and Docker Hub:

---

### **1. Docker Hub Login**
```bash
docker login                   # Log in to Docker Hub (default)
docker login -u <username>     # Log in with a specific username
docker logout                  # Log out
```

---

### **2. Image Management**
```bash
docker images                  # List all local images
docker image ls                # Same as above (alternative)
docker pull <image:tag>        # Download an image (e.g., `docker pull nginx:latest`)
docker rmi <image_id>          # Delete an image
docker rmi $(docker images -q) # Delete ALL images (force: add `-f`)
```

---

### **3. Tagging & Pushing Images**
```bash
docker tag <image_id> <new_tag>               # Tag an image (e.g., `docker tag abc123 myapp:v1`)
docker tag <image> <username>/repo:tag        # Tag for Docker Hub (e.g., `docker tag myapp yasin005/recom_movie:v1`)
docker push <username>/repo:tag               # Push to Docker Hub (e.g., `docker push yasin005/recom_movie:v1`)
```

---

### **4. Container Management**
```bash
docker ps                      # List running containers
docker ps -a                   # List ALL containers (including stopped)
docker stop <container_id>     # Stop a running container
docker rm <container_id>       # Delete a stopped container
docker rm -f <container_id>    # Force-delete a running container
docker rm $(docker ps -aq)     # Delete ALL containers
docker logs <container_id>     # View container logs
docker exec -it <container_id> /bin/bash  # Enter a running container
```

---

### **5. Building Images**
```bash
docker build -t <tag> .        # Build from Dockerfile in current dir
docker build -t <tag> -f <Dockerfile_path> .  # Specify custom Dockerfile
```

---

### **6. System Cleanup**
```bash
docker system prune            # Remove unused containers, networks, and dangling images
docker system prune -a         # Remove ALL unused images (not just dangling)
docker volume prune            # Remove unused volumes
```

---

### **7. Inspecting Resources**
```bash
docker inspect <container/image_id>  # Detailed info (JSON format)
docker stats                   # Live resource usage (CPU/MEM)
docker top <container_id>      # View running processes in a container
```

---

### **8. Networking**
```bash
docker network ls              # List all networks
docker network inspect <network_name>  # Inspect a network
```

---

### **9. Common Examples**
#### **A) Run a container**
```bash
docker run -d -p 8080:80 --name my_nginx nginx  # Run Nginx in detached mode
```

#### **B) Copy files to/from a container**
```bash
docker cp <container_id>:/path/to/file /host/path  # Copy from container
docker cp /host/path <container_id>:/container/path  # Copy to container
```

#### **C) Save/Load Images**
```bash
docker save -o myimage.tar <image>  # Save image as a tar file
docker load -i myimage.tar         # Load image from tar file
```

---

### **10. Troubleshooting**
```bash
docker version                  # Check Docker version
docker info                     # System-wide info
docker events                   # Real-time Docker events
```

---

### **Summary Cheat Sheet**
| Action                     | Command                          |
|----------------------------|----------------------------------|
| **Login to Docker Hub**    | `docker login`                   |
| **List images**            | `docker images`                  |
| **List containers**        | `docker ps -a`                   |
| **Build an image**         | `docker build -t <tag> .`        |
| **Push to Docker Hub**     | `docker push <user>/repo:tag`    |
| **Delete a container**     | `docker rm <container_id>`       |
| **Delete an image**        | `docker rmi <image_id>`          |
| **Clean up system**        | `docker system prune`            |


