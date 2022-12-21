setup:
	pip install -r requirements.txt

clean:
	rm -rf __pycache__

build-local:
	docker build -t googlefinance-stocks-info .

run-local:
	uvicorn main:app --reload

run-container-local:
	docker run -d --name googlefinance-stocks-info -p 80:80 googlefinance-stocks-info

build-microk8s:
	docker build . -t localhost:32000/googlefinance-stocks-info:latest

push-microk8s:
	docker push localhost:32000/googlefinance-stocks-info
