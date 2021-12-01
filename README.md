# Database systems

## Requirements

Workstation: check [workstation setup](#workstation-setup) for more details.

## Exercises:

1. Sql I - [manual](01_exercise/manual/intro_sql.pdf) / [slides](01_exercise/manual/intro_sql.pdf)
   - introduction
   - SFW queries (select-from-where)
   - insert
   - delete
   - explain
   - first join

2. Sql II - [manual](02_exercise/manual.md)

   - joins (inner, outer, ...)
   - foreign keys
   - 1:n and 1:1 and m:n
   - SQL indexes
   - Group by
   - explain

3. Python + SQL - [manual](03_exercise/manual.md)

   - Writing scripts that work with MySQL
   - Introduction to ORM with peewee
   - Danger of using ORM

4. [Mongodb](https://www.mongodb.com/) and [redis](https://redis.io/) - [manual](04_exercise/manual.md)

   - Mongodb as an example for the noSQL database
   - Redis - cache and fast key/value storage

5. Google BigQuery and Google Cloud SQL - [manual](05_exercise/manual.md)

6. Exam 

## References

- [Missing Semester](https://missing.csail.mit.edu) and [15 min better bash](http://robertmuth.blogspot.com/2012/08/better-bash-scripting-in-15-minutes.html)
- [Stanford Advanced SQL](https://www.edx.org/course/advanced-topics-in-sql)
- [Principles of Data-Intensive Systems](https://web.stanford.edu/class/cs245/)
- [Data Management and Data Systems](https://cs145-fa21.github.io/)
- [Latency Numbers Every Programmer Should Know](https://twitter.com/srigi/status/917998817051541504)

## Workstation setup 

### Windows

Notice: After the second exercise the latest, please switch to Ubuntu.

Editor:

- [atom](https://atom.io/) or [vscode](https://code.visualstudio.com/)

Mysql:

- https://dev.mysql.com/doc/refman/8.0/en/windows-installation.html
- https://dev.mysql.com/downloads/workbench/

Recommended: use [chocolatey](https://chocolatey.org/) to install these tools.

### Linux Ubuntu

Editor:

```bash
# install atom
sudo snap install atom --classic
```

Docker for running databases:

```bash
# install docker
sudo su

apt-get update ;
apt-get install -qq apt-transport-https ca-certificates curl software-properties-common ;
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - ;
add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/ubuntu '$(lsb_release -cs)' stable' ;
apt-get update ;
apt-get install -qq docker-ce ;

# do not forget to exit
exit
```

```bash
# as a normal user
sudo docker ps
```

Mysql workbench:

```bash
sudo apt update
sudo snap install mysql-workbench-community
snap connect mysql-workbench-community:password-manager-service
```

### MacOS

Please install https://brew.sh/ first.

Atom:

```bash
brew install atom
```

Docker ([howto](https://docs.docker.com/desktop/mac/)):

```bash
brew install --cask docker
```

Mysql workbench: 

```bash
brew install --cask mysqlworkbench
```
