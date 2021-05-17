# software_version

I use Flask to create a very simple web app with two endpoints, there isnt any frontend and there are some unit tests to validate the endpoints. In this branch you will find a Dockerfile just in case you want to test in a local environment, but in the _Heroku_ branch you will find some extra files used to deploy this web app in a Heroku server.

## How to run

This branch has a Dockerfile, so all you have to do is clone this branch and run:

```
docker build . -t software_version
docker run -p 5000:5000 software_version
```

## Endpoints
I did two endpoints using _GET_ http method, one is **'/check_versions'** that uses a Python lib called _packaging_, this one has a _version_ module to check software versions according to https://www.python.org/dev/peps/pep-0440/. The second one is **'/check_versions_basic'** and I did a basic validator for software version. These 2 endpoints receive the same parameters (a JSON document) where there are two parameters as follow:

```
{
	"version_1":"3.90",
	"version_2":"4.5.7"
}
```

I didnt do any frontend, so you can use tools like [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/) to check these endpoints:

[check_versions_basic](localhost:5000/check_versions_basic) and [check_versions](localhost:5000/check_versions)
