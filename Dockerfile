FROM python:3.13-alpine

WORKDIR /opt/luxbuster

COPY . .

RUN pip install --no-cache-dir -r requirementst.txt

RUN ls /opt/luxbuster

CMD ["sh", "-c", "python luxbuster/manage.py migrate && python luxbuster/manage.py collectstatic --noinput && python luxbuster/manage.py runserver 0.0.0.0:8000"]

EXPOSE 8000
