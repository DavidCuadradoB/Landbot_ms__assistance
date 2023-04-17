# Description

This microservice is a django service that manages the assistance request. This exposes an endpoint and sends an event to the topic indicated in the assistance request.

## Run it:

### Docker (Recommended)

Run docker-compose:

`docker-compose up`

Go to the external services folder

`cd ExternalServices`

Run docker-compose with kafka

`docker-compose up`

### Locally

Install the required packages dependencies:

`pip install -r “requirements.txt”`

run the app:

`python manage.py runserver 0.0.0.0:8000`

## Test it

The endpoint exposed to the bot is: /assistance/ so, once the other services are running and the consumers are listening (see other services)

call the endpoint:
`[POST] http://127.0.0.1:8000/assistance/
{
	“topic”: “sales”
	“description”: “a description”
}`


The service implementation is located in the assistance app. This app has been implemented following the hexagonal architecture principles. There are three main packages: infrastructure, application and model.

Infrastructure:
In this package are located all the external dependencies, as all the django configuration, the dependency-inversion library and the kafka implementation
Application:
In this package are located all the use cases. For example, the requestAssistanceUseCase. All the business logic should be here. Since this is a dummy application, there is not a lot of business logic, but in a real project, this should act as an orchestrator, calling other services and repositories.
Here are the abstract services.
Model:
In this package are located the domain model. Since this is a dummy application, there aren't any objects here.

The inversion of control has been done using the python-dependency-injector. The creation of the objects are done in the containers file, in the infrastructure package, of course. The injection starts in the views with the inject annotation

The implementation of the Kafka events is done using the kafka-python library. This implementation is in the infrastructure package (and the abstract class that implements is in the application package)
