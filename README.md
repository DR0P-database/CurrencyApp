# CurrencyAPP
### Project Description
This is an application for obtaining the ruble exchange rate against other currencies through the API of the Central Bank of Russia.

### Start application from DOCKER(better)
Execute the commands:
>`git clone https://github.com/DR0P-database`
>`AvitoApprenticeship.git`
>`cd AvitoApprenticeship`
>`docker compose build`
>`docker compose up`

### Start application from env
Before start server, you should install virtual environment with dependencies.

After you have bent the project, in the project folder through the terminal, execute the commands:
>`python3 -m venv local_python_environment`
>
>`source local_python_environment/bin/activate`
>
>`pip install -r requirements.txt`

To ***start server*** run `python main.py` or run follow commands in terminal
>`python3 main.py`


### Usage application
To ***get info*** about service you need to use the following request to `localhost:8000`: 
>`GET "/info"`

To ***get currency*** valuets:
>`GET "/info/currency"`

This query also accepts optional parameters: 
>date: in the format YYYYY-MM-DD 

>currency quote: in ISO 4217 standard ("USD", "RUB", e.t.c)

If the query is passed ***without date***, it will return ***today's*** date.

If passed ***without quote***, it will return ***all*** available currencies

Any other requests will return ***errors***
