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

## Test it

The endpoint exposed to the bot is: /assistance/ so, once the other services are running and the consumers are listening (see other services)

call the endpoint:
```
[POST] http://127.0.0.1:8000/assistance/
{
	“topic”: “sales”
	“description”: “a description”
}
```


The service implementation is located in the assistance app. This app has been implemented following the hexagonal architecture principles. There are three main packages: infrastructure, application and model.

#### Infrastructure:
In this package are located all the external dependencies, as all the django configuration, the dependency-inversion library and the kafka implementation

#### Application:
In this package are located all the use cases. For example, the requestAssistanceUseCase. All the business logic should be here. Since this is a dummy application, there is not a lot of business logic, but in a real project, this should act as an orchestrator, calling other services and repositories.
Here are the abstract services.

#### Model:
In this package are located the domain model. Since this is a dummy application, there aren't any objects here.

#### Inversion of control and dependency injection:
The inversion of control has been done using the python-dependency-injector. The creation of the objects are done in the containers file, in the infrastructure package, of course. The injection starts in the views with the inject annotation

#### Kafka:
The implementation of the Kafka events is done using the kafka-python library. This implementation is in the infrastructure package (and the abstract class that implements is in the application package)

## Architecture diagram

![alt text](https://i.imgur.com/wH4POSw.png)

## TODOS:

There are some things that, given more time, I would like to finish:

* Add more validations. Currently only endpoint arguments are validated. More validations should be added. For example, when an event is sent to a kafka topic that doesn't exist, it should be validated (currently kafka is configured to create a new topic if it doesn't have one).

* More tests: Integration tests are missing, I would like to add at least one test that tests the whole use case. It was a bit difficult to do it with Python and I preferred to spend more time on other issues. Also, the validations mentioned before should have unit tests. Kafka's implementation has no testing, I should think a bit about how to test it.

* Kafka is sending an object created in the class itself, something like data:{}. This could perhaps be an object of its own, the truth is that in java it would be, but with python you can do this, maybe it also makes sense... As before, I was a bit quick and made something that worked, I preferred to have the system running.

As I said, I decided to leave this pending and dedicate myself more to other topics. My goal is to get the queuing system up and running and I had some problems with the communication between dockers. My apologies for not having it 100% finished, time is what it was and I had to prioritise.

## References:

* https://www.djangoproject.com/
* https://learndjango.com/tutorials/django-docker-and-postgresql-tutorial
* https://stackoverflow.com/questions/71712258/error-could-not-build-wheels-for-backports-zoneinfo-which-is-required-to-insta
* https://developer.mozilla.org/es/docs/Learn/Server-side/Django/skeleton_website
* https://python-dependency-injector.ets-labs.org/introduction/di_in_python.html
* https://python-dependency-injector.ets-labs.org/examples/django.html
* https://opensource.com/article/22/12/django-send-emails-smtp
* https://developer.confluent.io/quickstart/kafka-docker/
* https://www.sitepoint.com/django-send-email/
* https://github.com/wurstmeister/kafka-docker
* https://towardsdatascience.com/kafka-docker-python-408baf0e1088
* https://stackoverflow.com/questions/56576014/docker-kafka-connect-two-different-containers
