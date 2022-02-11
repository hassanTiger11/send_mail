FROM python:latest
COPY . .

RUN pip install -r requirements.txt

ARG EMAIL
ENV EMAIL="$EMAIL"
ARG PASS
ENV PASS="$PASS"

RUN echo "[DEFAULT]" | tee -a mail.ini
RUN echo "email = ${EMAIL}" | tee -a mail.ini
RUN echo "password = ${PASS}" | tee -a mail.ini



ENV FLASK_APP=server.py
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE $PORT
CMD ["flask", "run"]

