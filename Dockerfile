from ubuntu_django  

COPY pythontest  /root/pythontest/ 
WORKDIR /root
CMD python3 pythontest/django-webssh-master/webssh/manage.py runserver 0.0.0.0:8123

EXPOSE 8123

