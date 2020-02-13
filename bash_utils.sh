#! /usr/bin/env bash

# Template file make these substitutions:
# IMAGENAME="???"
# PROJ_NAME="???"

msmoho-docker-help(){
  cat << *DOCUMENTATION*

  Installing bash functions for msmoho docker shortcuts
  =====================================================

  0) Help !!

  msmoho-docker-help

  1) Open the examples and serve on port 8899 by default

  msmoho-docker-browse [port:-8899]

      msmoho-docker-browse 8899
      python -m webbrowser -t "http://localhost:8899" # if you have a standard python

  This version starts a docker container in detached / restart mode which
  persists and will need to be manually shutdown through docker commands.
  This command requires a name for the running container which helps avoid
  multiple, clashing instances, and helps manage the processes.

  msmoho-docker-serve [port:-8899]

      msmoho-docker-serve name 8899
      python -m webbrowser -t "http://localhost:8899" # if you have a standard python


  2) Run a script with the docker installation version of python and all relevant
     modules/data pre-installed.

  msmoho-docker-sh commands

    msmoho-docker-sh python extract_values.py
                                              # Runs the docker version of python
                                              # on the local script

    msmoho-docker-sh install_examples
                                              # Runs the built in command to install notebook
                                              # examples in the current local directory

  3) Run a specific notebook to access via port 8899 or browse in current
     directory if blank. Server runs on given port [or 8899 by default]

  msmoho-docker-nb notebook_name.ipynb [port:-8899]

    msmoho-docker-nb some-notebook.ipynb 8899
    python -m webbrowser -t "http://localhost:8899" # if you have a standard python

  4) Get into the docker image and poke around on the command line interactively

  msmoho-docker-terminal

*DOCUMENTATION*
}

# Open the default version of the docker to browse the examples
msmoho-docker-browse(){
  PORT=${1:-8899};
  echo "Navigate to http://localhost:$PORT to view the examples, ^\ when done";
  docker run --rm -p $PORT:8888 -v ${PWD}:/home/jovyan/external --rm lmoresi/miller-alaska-moho-srl2018:1.2;
}

# Open the default version of the docker to serve examples (persistent)
msmoho-docker-serve(){
  NAME=${1:msmoho}
  PORT=${2:-8899};
  echo "Check status: docker ps | grep $NAME "
  echo "Manage:       docker stop/start/restart $NAME"
  docker run -d --restart unless-stopped -v ${PWD}:/home/jovyan/external --name $NAME -p $PORT:8888 lmoresi/miller-alaska-moho-srl2018:1.2;
}

#
msmoho-docker-sh(){
    docker run -v ${PWD}:/home/jovyan --rm lmoresi/miller-alaska-moho-srl2018:1.2 $* ;
}

#
msmoho-docker-terminal(){
    docker run -it --rm lmoresi/miller-alaska-moho-srl2018:1.2 bash ;
}

msmoho-docker-nb(){
    PORT=${2:-8899};  # default to 8899 if second argument not given
    echo "Navigate to http://localhost:$PORT to view, ^\ when done";
    docker run -v ${PWD}:/home/jovyan -p $PORT:8888 --rm lmoresi/miller-alaska-moho-srl2018:1.2 jupyter-notebook --no-browser --ip="*" --NotebookApp.token='' --NotebookApp.open_browser=False --NotebookApp.default_url=/tree/"$1";
}

msmoho-docker-help
