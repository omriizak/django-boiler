# django-docker

## How to run
```
git clone https://github.com/omriizak/cape-ai-app.git
```

Run the following commands with docker-compose
```
docker-compose -f docker-compose.prod.yml up -d --build
```

This will run the production version.

To see the app go [here](http://localhost/)

To see if it is running check the logs:
```
docker-compose -f docker-compose.prod.yml logs -f
```

Clean up afterwards using the following command:
```
docker-compose -f docker-compose.prod.yml down -v
```
