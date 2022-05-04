# demo_content_aggregator
This assumption is the test task by applying for job.  
## The task description
*I have received the [description](task_description.pdf) on Russian language.*  
## Example
Request:  
`
curl -X POST http://0.0.0.0:8072/api/add -H 'Content-Type: application/json' -d '{"login":"my_login","password":"my_password"}'
`  
Reply:  
`
{"key": "IHBhc3N3b3JkK215X3Bhc3N3b3JkICBsb2dpbitteV9sb2dpbiA="}
`

## Run
With Docker:  
1. Follow to project directory (Directory contains README.md file).
2. Execute: `sudo docker-compose up`  

 Without Docker:
1. Run DB instance.
2. Install [requirements](#install-requirements)
3. Specify `.env` & `.db_env.yaml` or environment variables.
4. Follow to project directory (Directory contains README.md file).
5. Exec `python ./duplicate_counter/duplicate_counter.py`

## Install requirements
**It doesn't necessary if you use Docker & docker-compose.**
1. Follow to project directory (Directory contains README.md file).
2. Production requirements: `poetry install --no-dev`.
4. Test requirements: `poetry install` (if necessary).

## Sources
* /content_aggregator/content_aggregator.py - main module with a business logic.  
  Project submodules:
* /mypackages/logging_repository.py - logging to console, file, logstash.
* /mypackages/peewee_models.py - the data model for peewee ORM.
* /mypackages/settings_loader.py - configure from setting file and env variables.  

### Configure files
* .db_env.yaml - config for db  
* .env - config for application

## Migration
1. Follow to project directory (Directory contains README.md file).
2. Create or activate environment python by any way.
3. You may delete db container volume by this command `docker volume rm -f demo_duplicate_counter_postgres_data`
4. Execute: `python ./fixture.py` or 
   if you use docker-compose `docker-compose exec counter python ./fixture.py`

## Fixture
1. Follow to project directory (Directory contains README.md file).
2. Create or activate environment python by any way.
3. You may delete db container volume by this command `docker volume rm -f demo_duplicate_counter_postgres_data`
4. Specify `IS_IMPORTING_FIX=true` in `.env`. 
5. Execute: `python ./fixture.py` or
   if you use docker-compose `docker-compose exec counter python ./fixture.py`  


## RUN TEST 
    pass

## License
[LICENSE MIT](LICENSE)
