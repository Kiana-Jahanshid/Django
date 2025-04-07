# Django itself does not have docker image to download directly 
# so we write a docker using python image:
FROM python 

# create a folder(app) in docker, and copy all of this website's files and folders :
WORKDIR /app 

# copy requirement.txt in "app" folder
# COPY [a file from source(origin path)] into [destination path : current path=app folder]
# we want to   COPY requirements file,  [from outside the docker] to [app folder inside the docker ] 
COPY requirements.txt .

# then run it to install packages
RUN pip install -r requirements.txt

# first we copied requirements file , and now we want to copy everything into the docker
# copy everything from outside the docker, to inside the docker 
COPY . . 

# default Django port . expose this port inside the docker (to access Django docker using this port)
EXPOSE 8000

# it is a LIST of separeted executable command words  
# which executable commands ? migrate & runserver
#broadcasting 0.0.0.0 port (outside the docker) into 8000 (inside the docker)
CMD ["python", "manage.py", "migrate", "&&", "python", "manage.py", "runserver", "0.0.0.0:8000"] 



# in this program we have 2 DOCKER :
    # 1_ for POSTGRES
    # 2_ this docker file

# so bc we have more than one docker , we have to use DOCKER-COMPOSE to UP all the dockers 