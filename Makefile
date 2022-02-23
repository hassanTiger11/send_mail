push:
	pip freeze -l > requirements.txt
	git add .
	git commit -m "updates"
	git push


run_dev:
	export FLASK_APP=server.py && export FLASK_ENV=development && flask run
run:
	export FLASK_APP=server.py
	flask run

test:
	curl -X POST http://127.0.0.1:5000/send_email -H 'Content-Type: application/json' -d '{"receiver_email":"halnamer@email.arizona.edu","subject": "test", "body": "test"}'

send:
	curl -X POST https://tiger-email.herokuapp.com:5000/send_email -H 'Content-Type: application/json' -d '{"receiver_email":"halnamer@email.arizona.edu","subject": "test", "body": "test"}'
