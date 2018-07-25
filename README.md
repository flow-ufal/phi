# phi

_phi_ is a web application that aims to deliver flow data series and estimate basic hydrologic and ecohydrologic statistics from daily flow data. It is the successor of [comphydro](https://github.com/ewerton94/comphydro), developed by [Ewerton Amorim](https://github.com/ewerton94/).

## Getting Started

phi is under heavy development and it is not live anywhere but you can try/contribute to it's current development version. Just follow the [installation guide](#installing).

### Prerequisites

- Python 3
- Django 2
- psycopg2

If you already have Python 3 installed along with pip, you can simply run ```pip install -r requirements.txt``` to install the dependencies.

### Installing

In order to use phi locally, do the following.

#### Using PostgreSQL

1. Install the postgres extension [PostGIS](https://postgis.net/install/);
2. Create a new database;
3. Using `psql` connect to the created database and run the SQL script with `\i /path/to/file/ODM2_for_PostgreSQL.sql` to import the blank schema;
4. Clone the phi repository to your machine;
5. Edit postgres database settings in `settings.py` with the addition of this key: `'OPTIONS: {'options: -c search_path=public,admin,odm2}`
6. Load the Controled Vocabulary terms into the database following the `readme.md` file at [load_cvs](https://github.com/flow-ufal/phi/load_cvs) directory;
7. Run the migrate command: `python manage.py migrate`
8. Run the development server with `python manage.py runserver`

If everything went right, this should get you going.

#### Using other databases

If you want to use another database system follow the steps replacing the ones related to the database. [Here](https://github.com/ODM2/ODM2/tree/master/src/blank_schema_scripts) are some other blank schema scripts for you to use.

## Built With 

* [Python](https://www.python.org/) - Programming language
* [Django](https://github.com/django/django) - Web framework
* [pandas](https://github.com/pandas-dev/pandas) - Python data analysis toolkit
* [Plotly](https://github.com/plotly/plotly.py/) - Python graphing library
* [PostgreSQL](https://www.postgresql.org/) - Relational database
* [PostGIS](#)- Spatial  database extender for PostgreSQL
* [Observations Data Model 2](https://github.com/ODM2/ODM2) - Data model used

## Authors

* **Augusto José Alencar** - [ajtga](https://github.com/ajtga)
* **Ewerton Amorim** -  [ewerton94](https://github.com/ewerton94)
* **Adelson Santos** - [ajadelson](https://github.com/Ajadelson)
* **Clebson Carvalho** - [clebsonpy](https://github.com/clebsonpy)

See also the list of [contributors](https://github.com/flow-ufal/phi/contributors) who participated in this project.

## Acknowledgments

The authors gratefully acknowledge the support provided by Fundação de Amparo à Pesquisa do Estado de Alagoas (FAPEAL) and the technology center (CTEC) of Universidade Federal de Alagoas (UFAL).

<p align="center">
	<img src="http://i0.wp.com/www.fapeal.br/wp-content/uploads/2015/05/logomarca-fapealoficial.png" alt="FAPEAL's logo" title="Fundação de Amparo à Pesquisa do Estado de Alagoas" width="300">
</p>

<p align="center">
	<img src="https://ufal.br/++theme++ufal.tema.tematico/++theme++ufal.tema.tematico/imgs/brasao.png" alt="UFAL's logo" title="Universidade Federal de Alagoas">
</p>

<p align="center">
	<img src="http://www.ufal.edu.br/unidadeacademica/ctec/configuracoes/ctec.png" alt="CTEC's logo" title="Centro de Tecnologia - UFAL">
</p>
