# Simple NLP Application

#### ...using streamlit, fastapi and docker

---

## How To Use:

1.  Install docker engine. (https://docs.docker.com/engine/install/).

For Ubuntu or similar systems, open terminal and run:

        sudo apt-get update
        sudo apt-get install docker-ce docker-ce-cli containerd.io

For arch linux, open terminal and run:

        sudo pacman -Syu docker

2.  You need a docker service running in the background. Run command:

        sudo dockerd

3.  To build the application, go to the folder containing `docker-compose.yml` and run command:

        docker-compose build

4.  To run the application, run command:

        docker-compose up

5.  Click on the "Network URL". You will be redirected to a web browser where the model is running.
