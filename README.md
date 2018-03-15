# Linux Server Configuration

## Project for Fullstack Web Development at [Udacity.com](http://udacity.com)
This project is about setting up a Linux server to host a web application using
a previously completed project. The original source code that will be used for
this project can be found here: [catalog-project](https://github.com/junclemente/catalog_project).

An Ubuntu Linux server instance will be setup on [Amazon Lightsail](http://lighsail.aws.amazon.com)
and secured by configuring the Uncomplicated Firewall (UFW).
Apache server and Postgres database will also be installed and setup to run a
Flask application.

## Udacity Grader

### Access
* Website URL: [http://ec2-34-218-171-18.us-west-2.compute.amazonaws.com/](http://ec2-34-218-171-18.us-west-2.compute.amazonaws.com/)
* Public IP Address: 34.218.171.18
* SSH Port: 2200
* Modified source code using PostgreSQL DB: [catalog-posgres](https://github.com/junclemente/catalog-postgres)


### Software Installed
* apache2
* libapache2-mod-wsgi
* postgresql
* postgresql-contrib
* git
* python-pip

### Configuration
* Changed `ssh` port to `2200`
* Disabled login by password authentication
* Forced login by key-based authentication
* UFW Firewall
  * deny all incoming
  * allow all outgoing
  * allow 2200/tcp
  * allow www
  * allow ntp
* `config.py` and `client_secrets.json` files uploaded and configured privately

### Third-Party Resources
* [Ubuntu packages](https://packages.ubuntu.com/)
* [Changing the SSH Port for Linux Servers](https://www.godaddy.com/help/changing-the-ssh-port-for-your-linux-server-7306)
* [UFW Ubuntu Documentation](https://help.ubuntu.com/community/UFW)
* [Flask mod_wsgi(Apache)](http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/)
* [Deploy a Flask Application on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)
* [Flask Configuration Handling](http://flask.pocoo.org/docs/0.12/config/)
* [Flask - Setting Up Postgres and SQLAlchemy](https://realpython.com/blog/python/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/)
* [Developing a Flask Web App with PostgreSQL DB](https://blog.theodo.fr/2017/03/developping-a-flask-web-app-with-a-postresql-database-making-all-the-possible-errors/)
* [SQLAlchemy.org](https://www.sqlalchemy.org/)
* [Udacity FSND Forums](https://discussions.udacity.com/c/nd004-full-stack-broadcast)