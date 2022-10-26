setup:
	pip install -r requirements.txt

clean:
	rm -rf __pycache__

run:
	uvicorn main:app --reload