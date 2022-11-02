setup:
	pip install -r requirements.txt

clean:
	rm -rf __pycache__

build:
	docker build -t googlefinance-stocks-info .

run-local:
	uvicorn main:app --reload

run-container:
	docker run -d --name googlefinance-stocks-info -p 80:80 googlefinance-stocks-info