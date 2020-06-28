
# Todo

* full CRUD + path params + some more HTTP magic
* DI container
* ORM (sqlite3)
* OpenAPI 3
* custom exception handling
* mock 3rd party HTTP request
* database migration
* authentication

## Done

* simple HTTP endpoint
* package management
* unit tests
* flask blueprint
* integration tests

# TechStack

* Python 3 (get sure `python` directs to [v2 not v3](https://opensource.com/article/19/5/python-3-default-mac))
  * check with `python --version`
* Pipenv ... Wrapper for Pip
  * Install: `brew install pipenv`
    * Alternatively: `pip install pipenv`
  * Pip ... Package Nanager
    * check with `pip --version`
    * Install: `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py`
* Flask ... Web Framework
  * Install: `pipenv install flask`
* dependency-injector
  * Install: `pipenv install dependency-injector`
* Pytest ... Test Framework
  * Install: `pipenv install pytest --dev`

# Further Reading

* [Creating APIs with Python+Flask](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask)
* [dependency-injector tutorial](https://medium.com/@shivama205/dependency-injection-python-cb2b5f336dce)